---
layout: default
title: "技術提案（一覧）"
description: "Mind-Uploadの技術提案（Technical Proposal）をIssue連動で一覧化します。"
article_type: Index
subtitle: "From Ideas to Implementable Milestones"
author: Mind Uploading Research Project
last_updated: "2026-02-05"
note: "Auto-generated from site pages"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Purpose</h2>
<p>
このページは、提案書（Technical Proposal）を探しやすくするための一覧ページです。各提案が「何を解決するのか」「どう確かめるのか」を見比べながら、Roadmapの前進条件につなげて読めます。
</p>
</div>

{% assign proposals = site.pages | where: "article_type", "Technical Proposal" | sort: "last_updated" | reverse %}

<section class="section" id="list">
<h2 class="section-title">Technical Proposals</h2>

{% if proposals and proposals.size > 0 %}
<div class="papers-list">
{% for p in proposals %}
<div class="paper-entry">
  <h3 class="paper-title"><a href="{{ p.url | relative_url }}" style="color:inherit; text-decoration:none;">{{ p.title }}</a></h3>
  <div class="paper-meta">
    {% if p.last_updated %}<span>{{ p.last_updated }}</span>{% endif %}
    {% if p.subtitle %}<span>{{ p.subtitle }}</span>{% endif %}
  </div>
  {% if p.description %}
  <div class="paper-abstract">{{ p.description }}</div>
  {% endif %}
  <a href="{{ p.url | relative_url }}" class="btn-action">Open Proposal</a>
</div>
{% endfor %}
</div>
{% else %}
<p>Technical Proposal がまだありません。</p>
{% endif %}
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>Related</h4>
<ul>
<li><a href="verification.html">検証基盤（Verification）→</a></li>
<li><a href="tech_roadmap.html">技術ロードマップ（学習）→</a></li>
<li><a href="issue.html">貢献ガイド（Contribute）→</a></li>
</ul>
</div>

<div class="note-box">
<strong>Rule of Thumb</strong>
<p>
提案は「やりたいこと」だけで終わらせず、<strong>測れる達成条件</strong>と<strong>反証条件</strong>（失敗の定義）まで書くと、検証基盤に乗ります。
</p>
</div>

</aside>
</main>
