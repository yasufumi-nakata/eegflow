#!/usr/bin/env python3
"""
Mind Uploading Paper Collection Script

Collects papers about "mind uploading" from arXiv and Scopus (past 10 years),
translates them to Japanese using LM Studio, and outputs a chronologically
sorted markdown file.
"""

import os
import json
import sys
import requests
import feedparser
import urllib.parse
import re
import time
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
ELSEVIER_API_KEY = os.getenv("ELSEVIER_API_KEY")
LM_STUDIO_BASE_URL = os.getenv("LM_STUDIO_BASE_URL", "http://localhost:1234/v1")
LM_STUDIO_MODEL = os.getenv("LM_STUDIO_MODEL", "local-model")

# File paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_FILE = os.path.join(BASE_DIR, "translations_cache.json")
OUTPUT_FILE = os.path.join(BASE_DIR, "mind_uploading_papers.md")
DATA_FILE = os.path.join(BASE_DIR, "papers_metadata.json")

# Search parameters
SEARCH_QUERY = "mind uploading"
START_YEAR = 2016
END_YEAR = 2026

# Initialize LLM client
llm_client = OpenAI(base_url=LM_STUDIO_BASE_URL, api_key="not-needed")


def load_cache():
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}
    return {}


def save_cache(cache):
    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)


def fetch_arxiv_papers(query, start_year, end_year, max_results=1000):
    """Fetch papers from arXiv for the given query and date range."""
    print(f"[arXiv] Fetching papers for '{query}' ({start_year}-{end_year})...")

    base_url = 'http://export.arxiv.org/api/query?'
    search_query = f'all:"{query}"'

    papers = []
    start = 0
    batch_size = 100

    while start < max_results:
        url = (f'{base_url}search_query={urllib.parse.quote(search_query)}'
               f'&sortBy=submittedDate&sortOrder=ascending'
               f'&start={start}&max_results={batch_size}')

        print(f"  Fetching batch {start} to {start + batch_size}...")

        try:
            feed = feedparser.parse(url)

            if not feed.entries:
                break

            for entry in feed.entries:
                try:
                    pub_date = datetime.strptime(entry.published, '%Y-%m-%dT%H:%M:%SZ')
                except:
                    continue

                if pub_date.year < start_year or pub_date.year > end_year:
                    continue

                doi = entry.get('arxiv_doi', '')
                authors = [a.name for a in entry.get('authors', [])]
                categories = [tag.get('term', '') for tag in entry.get('tags', [])]

                unique_id = doi if doi else entry.id

                papers.append({
                    'source': 'arXiv',
                    'id': unique_id,
                    'title': entry.title.replace('\n', ' ').strip(),
                    'abstract': entry.summary.replace('\n', ' ').strip(),
                    'url': entry.link,
                    'doi': doi,
                    'authors': ", ".join(authors),
                    'published': entry.published,
                    'pub_date_raw': entry.published,
                    'year': pub_date.year,
                    'categories': ", ".join(categories),
                    'affiliation': ''
                })

            if len(feed.entries) < batch_size:
                break

            start += batch_size
            time.sleep(1)

        except Exception as e:
            print(f"  Error fetching arXiv: {e}")
            break

    print(f"[arXiv] Found {len(papers)} papers")
    return papers


def get_elsevier_abstract(api_key, eid):
    """Retrieve full abstract from Elsevier's Abstract Retrieval API."""
    url = f"https://api.elsevier.com/content/abstract/eid/{eid}"
    headers = {
        "X-ELS-APIKey": api_key,
        "Accept": "application/json"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            coredata = data.get('abstracts-retrieval-response', {}).get('coredata', {})
            return coredata.get('dc:description')
        else:
            print(f"  Elsevier Retrieval Status {response.status_code} for {eid}")
    except Exception as e:
        print(f"  Error fetching abstract for {eid}: {e}")
    return None


def get_crossref_abstract(doi):
    """Retrieve abstract from CrossRef API using DOI."""
    if not doi:
        return None
    url = f"https://api.crossref.org/works/{doi}"
    headers = {
        "User-Agent": "MindUploadingPaperBot/1.0"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            abstract = data.get('message', {}).get('abstract')
            if abstract:
                abstract = re.sub(r'<[^>]+>', '', abstract)
                return abstract.strip()
    except Exception as e:
        print(f"  Error fetching CrossRef abstract: {e}")
    return None


def fetch_scopus_papers(api_key, query, start_year, end_year, max_results=1000):
    """Fetch papers from Scopus for the given query and date range."""
    if not api_key:
        print("[Scopus] API key not found, skipping Scopus search")
        return []

    print(f"[Scopus] Fetching papers for '{query}' ({start_year}-{end_year})...")

    url = "https://api.elsevier.com/content/search/scopus"
    headers = {
        "X-ELS-APIKey": api_key,
        "Accept": "application/json"
    }

    papers = []
    start = 0
    batch_size = 25

    while start < max_results:
        params = {
            "query": f'TITLE-ABS-KEY("{query}") AND PUBYEAR > {start_year - 1} AND PUBYEAR < {end_year + 1}',
            "count": batch_size,
            "start": start,
            "sort": "coverDate",
            "view": "STANDARD"
        }

        print(f"  Fetching batch {start} to {start + batch_size}...")

        try:
            response = requests.get(url, headers=headers, params=params, timeout=30)

            if response.status_code != 200:
                print(f"  Scopus API Error: {response.status_code}")
                break

            data = response.json()
            entries = data.get('search-results', {}).get('entry', [])

            if not entries or (len(entries) == 1 and 'error' in entries[0]):
                break

            for entry in entries:
                pub_date_str = entry.get('prism:coverDate', '')
                try:
                    pub_date = datetime.strptime(pub_date_str, '%Y-%m-%d')
                except:
                    pub_date = datetime.min

                if pub_date.year < start_year or pub_date.year > end_year:
                    continue

                eid = entry.get('eid')
                title = entry.get('dc:title', 'No Title')
                doi = entry.get('prism:doi', '')
                # Get abstract
                abstract = entry.get('dc:description')

                if (not abstract or abstract == "（アブストラクトなし）") and eid:
                    abstract = get_elsevier_abstract(api_key, eid)

                if (not abstract or abstract == "（アブストラクトなし）") and doi:
                    abstract = get_crossref_abstract(doi)

                if (not abstract or abstract == "（アブストラクトなし）"):
                    abstract = "（アブストラクト取得不可）"

                paper_url = ""
                links = entry.get('link', [])
                if isinstance(links, list):
                    paper_url = next((l.get('@href') for l in links if l.get('@ref') == 'scopus'), "")

                affiliation = ""
                affiliations = entry.get('affiliation', [])
                if affiliations:
                    if isinstance(affiliations, list):
                        affiliation = ", ".join([a.get('affilname', '') for a in affiliations[:3]])
                    elif isinstance(affiliations, dict):
                        affiliation = affiliations.get('affilname', '')

                papers.append({
                    'source': 'Scopus',
                    'id': doi if doi else eid,
                    'title': title,
                    'abstract': abstract,
                    'url': paper_url,
                    'doi': doi,
                    'authors': entry.get('dc:creator', 'Unknown Authors'),
                    'published': pub_date_str,
                    'pub_date_raw': pub_date_str,
                    'year': pub_date.year,
                    'categories': entry.get('prism:publicationName', ''),
                    'affiliation': affiliation
                })

            if len(entries) < batch_size:
                break

            start += batch_size
            time.sleep(0.5)

        except Exception as e:
            print(f"  Error fetching Scopus: {e}")
            break

    print(f"[Scopus] Found {len(papers)} papers")
    return papers


def translate_paper_with_llm(paper):
    """Translate paper title and abstract to Japanese using LM Studio."""
    system_prompt = "あなたは優秀な翻訳者です。学術論文のタイトルとアブストラクトを正確かつ自然な日本語に翻訳してください。"

    user_prompt = f"""以下の論文情報を日本語に翻訳してください。

【原文タイトル】
{paper['title']}

【原文アブストラクト】
{paper['abstract']}

以下の形式で出力してください：
【日本語タイトル】
（翻訳したタイトル）

【日本語要約】
（翻訳したアブストラクト）

【5点要約】
1. どんなもの？
（一文で回答）
2. 先行研究との違いは？
（一文で回答）
3. 技術のキモは？
（一文で回答）
4. 検証方法は？
（一文で回答）
5. 議論点・限界は？
（一文で回答）
"""

    try:
        response = llm_client.chat.completions.create(
            model=LM_STUDIO_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3,
            timeout=180
        )
        content = response.choices[0].message.content
        content = re.sub(r'<(think|thought)>.*?</\1>', '', content, flags=re.DOTALL)
        content = re.sub(r'\[(thought|thinking)\].*?\[/\1\]', '', content, flags=re.DOTALL)
        return content.strip()
    except Exception as e:
        print(f"    Translation error for {paper['title'][:30]}: {e}")
        return None


def generate_markdown_report(papers, cache):
    """Generate a markdown report of all papers sorted chronologically."""
    print(f"\n[Report] Generating markdown report...")

    sorted_papers = sorted(papers, key=lambda x: (x['year'], x['published']))

    papers_by_year = {}
    for paper in sorted_papers:
        year = paper['year']
        if year not in papers_by_year:
            papers_by_year[year] = []
        papers_by_year[year].append(paper)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("# Mind Uploading 論文集（2016-2026）\n\n")
        f.write(f"収集日: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write(f"総論文数: {len(papers)} 件\n")
        f.write(f"- arXiv: {len([p for p in papers if p['source'] == 'arXiv'])} 件\n")
        f.write(f"- Scopus: {len([p for p in papers if p['source'] == 'Scopus'])} 件\n\n")
        f.write("---\n\n")

        for year in sorted(papers_by_year.keys()):
            f.write(f"## {year}年\n\n")
            for i, paper in enumerate(papers_by_year[year], 1):
                f.write(f"### {i}. {paper['title']}\n\n")
                f.write(f"**ソース**: {paper['source']} | **公開日**: {paper['published']} | **著者**: {paper['authors']}  \n")
                if paper['affiliation']:
                    f.write(f"**所属**: {paper['affiliation']}  \n")
                if paper['doi']:
                    f.write(f"**DOI**: [{paper['doi']}](https://doi.org/{paper['doi']})  \n")
                f.write(f"**URL**: [{paper['url']}]({paper['url']})  \n")

                translation = cache.get(paper['id'])
                if translation:
                    f.write(f"\n{translation}\n\n")
                else:
                    f.write(f"\n**原文アブストラクト**:\n{paper['abstract']}\n\n")
                f.write("---\n\n")

    print(f"[Report] Saved to {OUTPUT_FILE}")


def main():
    print("=" * 60)
    print("Mind Uploading Paper Collection Script (Resumable)")
    print("=" * 60)

    cache = load_cache()

    # 1. Fetch metadata if not already saved
    if os.path.exists(DATA_FILE):
        print(f"[Data] Loading existing metadata from {DATA_FILE}")
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            unique_papers = json.load(f)
    else:
        arxiv_papers = fetch_arxiv_papers(SEARCH_QUERY, START_YEAR, END_YEAR)
        scopus_papers = fetch_scopus_papers(ELSEVIER_API_KEY, SEARCH_QUERY, START_YEAR, END_YEAR)

        all_papers = arxiv_papers + scopus_papers
        seen_ids = set()
        unique_papers = []
        for paper in all_papers:
            if paper['id'] in seen_ids:
                continue
            seen_ids.add(paper['id'])
            unique_papers.append(paper)

        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(unique_papers, f, ensure_ascii=False, indent=2)

    print(f"\n[Total] {len(unique_papers)} unique papers found")

    # 2. Translate
    to_translate = [p for p in unique_papers if p['id'] not in cache]
    print(f"[LLM] {len(cache)} papers already translated. {len(to_translate)} remaining.")

    for i, paper in enumerate(to_translate, 1):
        print(f"  [{i}/{len(to_translate)}] Translating: {paper['title'][:50]}...")
        translation = translate_paper_with_llm(paper)
        if translation:
            cache[paper['id']] = translation
            save_cache(cache)

        # Periodically update the report
        if i % 5 == 0:
            generate_markdown_report(unique_papers, cache)

        time.sleep(0.5)

    # 3. Final report
    generate_markdown_report(unique_papers, cache)
    print("\n" + "=" * 60)
    print("Done!")
    print("=" * 60)


if __name__ == "__main__":
    main()
