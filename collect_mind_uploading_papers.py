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
    """Generate a high-end, responsive HTML report with a sticky sidebar and modern UI."""
    print(f"\n[Report] Generating overhaul HTML report...")

    sorted_papers = sorted(papers, key=lambda x: (x['year'], x['published']), reverse=True)

    papers_by_year = {}
    for paper in sorted_papers:
        year = paper['year']
        if year not in papers_by_year:
            papers_by_year[year] = []
        papers_by_year[year].append(paper)

    # UI Constants & Icons (Lucide-like SVGs)
    ICON_SOURCE = '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5z"/><path d="M8 7h6"/><path d="M8 11h8"/><path d="M8 15h6"/></svg>'
    ICON_DATE = '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"/><path d="M16 2v4"/><path d="M8 2v4"/><path d="M3 10h18"/></svg>'
    ICON_USER = '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>'
    ICON_LINK = '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>'

    css = """
    :root {
        --primary: #818cf8;
        --primary-dark: #6366f1;
        --bg: #0f172a;
        --sidebar-bg: #1e293b;
        --card-bg: #1e293b;
        --text: #f1f5f9;
        --text-muted: #94a3b8;
        --border: rgba(255, 255, 255, 0.1);
        --accent-gradient: linear-gradient(135deg, #818cf8 0%, #c084fc 100%);
        --shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
        font-family: 'Outfit', sans-serif;
        background-color: var(--bg);
        color: var(--text);
        line-height: 1.6;
        display: grid;
        grid-template-columns: 260px 1fr;
    }

    /* Sidebar */
    .sidebar {
        height: 100vh;
        background: var(--sidebar-bg);
        border-right: 1px solid var(--border);
        position: sticky;
        top: 0;
        padding: 2rem 1.5rem;
        display: flex;
        flex-direction: column;
        gap: 2rem;
        z-index: 100;
    }

    .sidebar-logo {
        font-size: 1.25rem;
        font-weight: 800;
        background: var(--accent-gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }

    .sidebar-nav {
        list-style: none;
        overflow-y: auto;
    }

    .sidebar-nav li a {
        display: block;
        padding: 0.75rem 1rem;
        color: var(--text-muted);
        text-decoration: none;
        border-radius: 12px;
        transition: all 0.2s;
        font-weight: 500;
    }

    .sidebar-nav li a:hover {
        background: rgba(255, 255, 255, 0.05);
        color: var(--text);
    }

    .sidebar-nav li a.active {
        background: var(--primary);
        color: white;
    }

    /* Main Content */
    main {
        padding: 4rem 2rem;
        max-width: 1000px;
        margin: 0 auto;
    }

    header {
        margin-bottom: 5rem;
        text-align: left;
    }

    header h1 {
        font-size: 3.5rem;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 1rem;
        letter-spacing: -0.02em;
    }

    header p {
        color: var(--text-muted);
        font-size: 1.125rem;
        max-width: 600px;
    }

    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
        gap: 1.5rem;
        margin-top: 2.5rem;
    }

    .stat-card {
        background: rgba(255,255,255,0.03);
        padding: 1.25rem;
        border-radius: 16px;
        border: 1px solid var(--border);
    }

    .stat-card span { font-size: 0.75rem; text-transform: uppercase; color: var(--text-muted); letter-spacing: 0.05em; }
    .stat-card div { font-size: 1.5rem; font-weight: 700; color: var(--primary); }

    .year-title {
        font-size: 2.5rem;
        margin: 6rem 0 3rem;
        font-weight: 800;
        scroll-margin-top: 2rem;
        position: relative;
    }

    .year-title::after {
        content: '';
        position: absolute;
        bottom: -0.5rem;
        left: 0;
        width: 60px;
        height: 6px;
        background: var(--accent-gradient);
        border-radius: 3px;
    }

    /* Paper Card */
    .paper-card {
        background: var(--card-bg);
        border: 1px solid var(--border);
        border-radius: 24px;
        padding: 2.5rem;
        margin-bottom: 3rem;
        box-shadow: var(--shadow);
        transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .paper-card:hover { transform: translateY(-4px); border-color: rgba(129, 140, 248, 0.4); }

    .badge {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.4rem 0.8rem;
        background: rgba(129, 140, 248, 0.1);
        color: var(--primary);
        border-radius: 8px;
        font-size: 0.75rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
    }

    .paper-card h3 {
        font-size: 1.75rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        line-height: 1.3;
    }

    .meta {
        display: flex;
        flex-wrap: wrap;
        gap: 1.5rem;
        margin-bottom: 2rem;
        color: var(--text-muted);
        font-size: 0.875rem;
    }

    .meta-item { display: flex; align-items: center; gap: 0.5rem; }
    .meta-item .icon { color: var(--primary); opacity: 0.8; }

    /* Japanese Translation Box */
    .translation-container {
        background: rgba(0,0,0,0.2);
        border-radius: 20px;
        padding: 2rem;
        border-left: 4px solid var(--primary);
    }

    .jp-title {
        font-size: 1.25rem;
        font-weight: 700;
        margin-bottom: 1.25rem;
        color: white;
    }

    .jp-summary {
        font-size: 1rem;
        color: #cbd5e1;
        margin-bottom: 2rem;
        white-space: pre-wrap;
    }

    .grid-5points {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 1.25rem;
    }

    .point-card {
        background: rgba(255,255,255,0.03);
        padding: 1.25rem;
        border-radius: 16px;
    }

    .point-card label {
        display: block;
        font-size: 0.75rem;
        font-weight: 800;
        color: var(--primary);
        text-transform: uppercase;
        margin-bottom: 0.5rem;
        letter-spacing: 0.05em;
    }

    .point-card p { font-size: 0.9rem; color: #e2e8f0; }

    .btn-action {
        display: inline-flex;
        align-items: center;
        gap: 0.75rem;
        margin-top: 2.5rem;
        padding: 0.875rem 1.75rem;
        background: var(--accent-gradient);
        color: white;
        text-decoration: none;
        border-radius: 14px;
        font-weight: 700;
        transition: opacity 0.2s;
    }

    .btn-action:hover { opacity: 0.9; }

    .raw-abstract {
        margin-top: 2rem;
        font-size: 0.875rem;
        color: var(--text-muted);
        border-top: 1px solid var(--border);
        padding-top: 1.5rem;
        font-style: italic;
    }

    @media (max-width: 900px) {
        body { grid-template-columns: 1fr; }
        .sidebar { display: none; }
        main { padding: 3rem 1.5rem; }
    }
    """

    import html

    def parse_translation_robust(translation):
        res = {"title": "", "summary": "", "points": []}
        if not translation: return res

        # Extract title
        title_m = re.search(r'【日本語タイトル】\s*(.*?)\s*(?=【|$)', translation, re.DOTALL)
        if title_m: res["title"] = title_m.group(1).strip()

        # Extract summary
        summary_m = re.search(r'【日本語要約】\s*(.*?)\s*(?=【|$)', translation, re.DOTALL)
        if summary_m: res["summary"] = summary_m.group(1).strip()

        # Extract 5 points
        points_m = re.search(r'【5点要約】\s*(.*)', translation, re.DOTALL)
        if points_m:
            p_text = points_m.group(1)
            # Match "1. Description \n Content"
            p_list = re.findall(r'(\d+\.\s*[^?\n]+)\n(.*?)(?=\n\d+\.|$)', p_text + "\n", re.DOTALL)
            res["points"] = p_list

        return res

    with open(HTML_OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mind Uploading Paper Collection</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800&display=swap" rel="stylesheet">
    <style>{css}</style>
</head>
<body>
    <aside class="sidebar">
        <div class="sidebar-logo">Mind Uploading</div>
        <ul class="sidebar-nav">
""")
        for year in sorted(papers_by_year.keys(), reverse=True):
            f.write(f'<li><a href="#year-{year}">{year}年</a></li>')

        f.write(f"""
        </ul>
    </aside>
    <main>
        <header>
            <h1>Mind Uploading Paper Collection</h1>
            <p>過去10年間のマインドアップロードに関する主要な論文を収集し、AIによって翻訳・要約した資料です。</p>
            <div class="stats-grid">
                <div class="stat-card"><span>Total</span><div>{len(papers)}</div></div>
                <div class="stat-card"><span>arXiv</span><div>{len([p for p in papers if p['source'] == 'arXiv'])}</div></div>
                <div class="stat-card"><span>Scopus</span><div>{len([p for p in papers if p['source'] == 'Scopus'])}</div></div>
            </div>
        </header>
""")

        for year in sorted(papers_by_year.keys(), reverse=True):
            f.write(f'<h2 id="year-{year}" class="year-title">{year}年</h2>')
            for paper in papers_by_year[year]:
                translation_raw = cache.get(paper['id'])
                parsed = parse_translation_robust(translation_raw)

                # Use translated title from LLM if available, otherwise original
                display_title_jp = parsed["title"] if parsed["title"] else "（翻訳中...）"
                display_summary = parsed["summary"] if parsed["summary"] else "アブストラクトの日本語訳を準備中です。"
                if not translation_raw and paper['abstract'] == "（アブストラクト取得不可）":
                    display_summary = "（この論文はアブストラクトの取得ができなかったため、詳細な翻訳・要約が生成できませんでした）"

                doi_link = f'<a href="https://doi.org/{paper["doi"]}" target="_blank" style="color:inherit">{paper["doi"]}</a>' if paper['doi'] else 'N/A'

                f.write(f"""
        <div class="paper-card">
            <div class="badge">{ICON_SOURCE} {paper['source']}</div>
            <h3>{html.escape(paper['title'])}</h3>

            <div class="meta">
                <div class="meta-item">{ICON_DATE} {paper['published']}</div>
                <div class="meta-item">{ICON_USER} {html.escape(paper['authors'])}</div>
                <div class="meta-item">{ICON_LINK} DOI: {doi_link}</div>
            </div>

            <div class="translation-container">
                <div class="jp-title">{html.escape(display_title_jp)}</div>
                <div class="jp-summary">{html.escape(display_summary)}</div>

                <div class="grid-5points">
""")
                if parsed["points"]:
                    for label, content in parsed["points"]:
                        f.write(f"""
                    <div class="point-card">
                        <label>{html.escape(label)}</label>
                        <p>{html.escape(content.strip())}</p>
                    </div>""")
                elif translation_raw:
                    # Fallback if points were not in "number. label\n content" format but text existed
                    f.write(f'<div class="point-card" style="grid-column: 1/-1"><p>{html.escape(translation_raw.split("【5点要約】")[-1].strip())}</p></div>')

                f.write("""
                </div>
            </div>
""")
                if paper['abstract'] != "（アブストラクト取得不可）":
                    f.write(f'<div class="raw-abstract"><b>Original Abstract:</b> {html.escape(paper["abstract"])}</div>')

                f.write(f"""
            <a href="{paper['url']}" target="_blank" class="btn-action">View Full Access {ICON_LINK}</a>
        </div>""")

        f.write("</main></body></html>")

    print(f"[Report] Overhaul HTML Saved to {HTML_OUTPUT_FILE}")


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
