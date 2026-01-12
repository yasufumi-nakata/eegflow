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
HTML_OUTPUT_FILE = os.path.join(BASE_DIR, "mind_uploading_papers.html")
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


def generate_html_report(papers, cache):
    """Generate a premium HTML report of all papers sorted chronologically."""
    print(f"\n[Report] Generating premium HTML report...")

    sorted_papers = sorted(papers, key=lambda x: (x['year'], x['published']), reverse=True)

    papers_by_year = {}
    for paper in sorted_papers:
        year = paper['year']
        if year not in papers_by_year:
            papers_by_year[year] = []
        papers_by_year[year].append(paper)

    # CSS for premium look
    css = """
    :root {
        --primary-color: #6366f1;
        --primary-hover: #4f46e5;
        --bg-color: #0f172a;
        --card-bg: #1e293b;
        --text-primary: #f8fafc;
        --text-secondary: #94a3b8;
        --accent-gradient: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        --glass-bg: rgba(30, 41, 59, 0.7);
    }

    * { margin: 0; padding: 0; box-バランス: border-box; }

    body {
        font-family: 'Outfit', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        background-color: var(--bg-color);
        color: var(--text-primary);
        line-height: 1.6;
        padding: 2rem 1rem;
    }

    .container {
        max-width: 1000px;
        margin: 0 auto;
    }

    header {
        text-align: center;
        margin-bottom: 4rem;
        padding: 3rem;
        background: var(--glass-bg);
        backdrop-filter: blur(10px);
        border-radius: 24px;
        border: 1px solid rgba(255,255,255,0.1);
        box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5);
    }

    h1 {
        font-size: 3rem;
        margin-bottom: 1rem;
        background: var(--accent-gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }

    .stats {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin-top: 1.5rem;
        font-size: 0.9rem;
        color: var(--text-secondary);
    }

    .year-section {
        margin-bottom: 4rem;
    }

    .year-header {
        font-size: 2rem;
        margin-bottom: 2rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid var(--primary-color);
        display: inline-block;
        font-weight: 700;
        position: sticky;
        top: 1rem;
        background: var(--bg-color);
        z-index: 10;
        padding-right: 2rem;
    }

    .paper-card {
        background-color: var(--card-bg);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 2rem;
        border: 1px solid rgba(255,255,255,0.05);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .paper-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 25px -5px rgba(0,0,0,0.3);
        border-color: rgba(99, 102, 241, 0.3);
    }

    .source-tag {
        position: absolute;
        top: 1.5rem;
        right: 1.5rem;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        background: var(--accent-gradient);
    }

    h3.paper-title {
        font-size: 1.5rem;
        margin-bottom: 1rem;
        padding-right: 5rem;
        line-height: 1.3;
        color: #fff;
    }

    .meta-info {
        font-size: 0.85rem;
        color: var(--text-secondary);
        margin-bottom: 1.5rem;
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
    }

    .meta-item b { color: var(--text-primary); }

    .translation-box {
        background: rgba(0,0,0,0.2);
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 1.5rem;
        border-left: 4px solid var(--primary-color);
    }

    .jp-title {
        font-weight: 700;
        font-size: 1.1rem;
        margin-bottom: 1rem;
        color: #fff;
    }

    .jp-summary {
        font-size: 0.95rem;
        margin-bottom: 1.5rem;
        color: #d1d5db;
    }

    .five-point-title {
        font-weight: 700;
        margin-bottom: 0.75rem;
        font-size: 0.9rem;
        color: var(--primary-color);
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .five-point-list {
        list-style: none;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1rem;
    }

    @media (max-width: 768px) {
        .five-point-list { grid-template-columns: 1fr; }
        h1 { font-size: 2rem; }
    }

    .point-item {
        background: rgba(255,255,255,0.03);
        padding: 0.75rem;
        border-radius: 8px;
        font-size: 0.85rem;
    }

    .point-label {
        font-weight: 700;
        color: var(--text-primary);
        display: block;
        margin-bottom: 0.25rem;
    }

    .url-btn {
        display: inline-block;
        margin-top: 1.5rem;
        padding: 0.6rem 1.2rem;
        background: var(--primary-color);
        color: white;
        text-decoration: none;
        border-radius: 10px;
        font-weight: 600;
        font-size: 0.9rem;
        transition: background 0.2s;
    }

    .url-btn:hover { background: var(--primary-hover); }

    .abstract-raw {
        font-size: 0.85rem;
        color: var(--text-secondary);
        font-style: italic;
        margin-top: 1rem;
        border-top: 1px solid rgba(255,255,255,0.05);
        padding-top: 1rem;
    }
    """

    import html

    with open(HTML_OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mind Uploading Paper Collection</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800&display=swap" rel="stylesheet">
    <style>{css}</style>
</head>
<body>
<div class="container">
    <header>
        <h1>Mind Uploading Paper Collection</h1>
        <p>学術論文集（2016-2026）</p>
        <div class="stats">
            <span>総論文数: <b>{len(papers)}</b></span>
            <span>arXiv: <b>{len([p for p in papers if p['source'] == 'arXiv'])}</b></span>
            <span>Scopus: <b>{len([p for p in papers if p['source'] == 'Scopus'])}</b></span>
            <span>更新日: <b>{datetime.now().strftime('%Y-%m-%d')}</b></span>
        </div>
    </header>
""")

        for year in sorted(papers_by_year.keys(), reverse=True):
            f.write(f'<section class="year-section"><h2 class="year-header">{year}年</h2>')
            for paper in papers_by_year[year]:
                translation = cache.get(paper['id'], "")

                # Parse translation parts
                parts = {"title": paper['title'], "summary": "", "5point": []}
                if translation:
                    t_match = re.search(r'【日本語タイトル】\n(.*?)\n\n【日本語要約】', translation, re.DOTALL)
                    if t_match: parts["title"] = t_match.group(1).strip()

                    s_match = re.search(r'【日本語要約】\n(.*?)\n\n【5点要約】', translation, re.DOTALL)
                    if s_match: parts["summary"] = s_match.group(1).strip()

                    p_match = re.search(r'【5点要約】\n(.*)', translation, re.DOTALL)
                    if p_match:
                        points = re.findall(r'\d+\.\s+(.*?)\n(.*?)(?=\n\d+\.\s+|$)', p_match.group(1) + "\n", re.DOTALL)
                        parts["5point"] = points

                doi_link = f'<a href="https://doi.org/{paper["doi"]}" style="color:var(--primary-color)">{paper["doi"]}</a>' if paper['doi'] else 'N/A'

                f.write(f"""
        <div class="paper-card">
            <span class="source-tag">{paper['source']}</span>
            <h3 class="paper-title">{html.escape(paper['title'])}</h3>
            <div class="meta-info">
                <span class="meta-item"><b>Date:</b> {paper['published']}</span>
                <span class="meta-item"><b>Authors:</b> {html.escape(paper['authors'])}</span>
                <span class="meta-item"><b>DOI:</b> {doi_link}</span>
                {f'<span class="meta-item"><b>Affil:</b> {html.escape(paper["affiliation"])}</span>' if paper['affiliation'] else ''}
            </div>
""")
                if translation:
                    escaped_summary = html.escape(parts["summary"]).replace('\n', '<br>')
                    f.write(f"""
            <div class="translation-box">
                <div class="jp-title">{html.escape(parts["title"])}</div>
                <div class="jp-summary">{escaped_summary}</div>
                <div class="five-point-title">Quick Review</div>
                <div class="five-point-list">
""")
                    for label, content in parts["5point"]:
                        f.write(f"""
                    <div class="point-item">
                        <span class="point-label">{html.escape(label)}</span>
                        {html.escape(content.strip())}
                    </div>""")
                    f.write("</div></div>")

                f.write(f"""
            <div class="abstract-raw"><b>Original Abstract:</b> {html.escape(paper['abstract'])}</div>
            <a href="{paper['url']}" target="_blank" class="url-btn">View Full Paper</a>
        </div>""")
            f.write('</section>')

        f.write("</div></body></html>")

    print(f"[Report] Saved to {HTML_OUTPUT_FILE}")


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

        # Periodically update the reports
        if i % 5 == 0:
            generate_markdown_report(unique_papers, cache)
            generate_html_report(unique_papers, cache)

        time.sleep(0.5)

    # 3. Final reports
    generate_markdown_report(unique_papers, cache)
    generate_html_report(unique_papers, cache)
    print("\n" + "=" * 60)
    print("Done!")
    print("=" * 60)


if __name__ == "__main__":
    main()
