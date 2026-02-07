---
layout: default
title: "データ & ベンチ：まず何を使って検証するか"
description: "公開データ（EEG中心）と共有基盤を、Mind-Uploadの目的（比較可能な検証）に沿って整理します。"
article_type: Resource
subtitle: "「データがある」だけでは足りない。規格・メタデータ・評価がセット。"
author: Mind Uploading Research Project
last_updated: "2026-02-05"
note: "Curated List (v0)"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>How To Use</h2>
<p>
このページは「まず何で検証する？」に答えるための実務用リストです。Mind-Uploadでは、公開データを使って <strong>L0（再現可能性）</strong> と <strong>L1〜L2（予測と介入検証）</strong> を積み上げることを重視します。
</p>
</div>

<section class="section" id="platforms">
<h2 class="section-title">1) まず押さえる共有基盤（置き場）</h2>
<div class="stage-list">
<div class="stage-item">
<div class="stage-number">A</div>
<div class="stage-body">
<h4>OpenNeuro（BIDS前提の共有）</h4>
<p>BIDS準拠の神経計測データを共有するための基盤。EEG/MEG/fMRIなどを扱う。</p>
<a href="https://openneuro.org/" target="_blank" class="btn-action">Open OpenNeuro</a>
</div>
</div>
<div class="stage-item">
<div class="stage-number">B</div>
<div class="stage-body">
<h4>PhysioNet（生体信号＋評価文化）</h4>
<p>生体信号データと関連リソースの公開基盤。EEGの定番データセットが多い。</p>
<a href="https://physionet.org/" target="_blank" class="btn-action">Open PhysioNet</a>
</div>
</div>
<div class="stage-item">
<div class="stage-number">C</div>
<div class="stage-body">
<h4>Human Connectome Project（大規模fMRI等）</h4>
<p>公開データとツールを通じて、ヒト脳の大規模計測を提供してきた代表例。</p>
<a href="https://www.humanconnectome.org/" target="_blank" class="btn-action">Open HCP</a>
</div>
</div>
</div>
</section>

<section class="section" id="starter">
<h2 class="section-title">2) EEGスターターパック（まずこれでL0〜L1）</h2>
<p>
最初は「使いやすい」「参照が多い」「前処理パイプラインが作りやすい」データから始めるのがおすすめです。
ここでは入口として有名なものを挙げます（網羅ではありません）。
</p>

<table class="data-table">
<thead>
<tr>
<th>データセット</th>
<th>何ができるか（例）</th>
<th>リンク</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG Motor Movement/Imagery</strong></td>
<td>運動/運動想起の分類、前処理の練習、ベースライン比較</td>
<td><a href="https://physionet.org/content/eegmmidb/" target="_blank">PhysioNet</a></td>
</tr>
<tr>
<td><strong>CHB-MIT Scalp EEG</strong></td>
<td>てんかん発作検出、イベント検出、長時間EEGの扱い</td>
<td><a href="https://physionet.org/content/chbmit/" target="_blank">PhysioNet</a></td>
</tr>
<tr>
<td><strong>Sleep-EDF</strong></td>
<td>睡眠段階推定、状態遷移のモデル化、縦断的変動の扱い</td>
<td><a href="https://physionet.org/content/sleep-edfx/" target="_blank">PhysioNet</a></td>
</tr>
<tr>
<td><strong>TUH EEG Corpus（大規模）</strong></td>
<td>スケールするEEG分類、実運用寄りの分布の難しさ、データリーク対策</td>
<td><a href="https://www.isip.piconepress.com/projects/tuh_eeg/" target="_blank">TUH EEG</a></td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="benchmark-mindset">
<h2 class="section-title">3) “データがある”だけで終わらせないチェックリスト</h2>
<div class="key-points">
<h4>Checklist</h4>
<ul>
<li><strong>再現：</strong>取得手順、ライセンス、前処理条件、乱数、環境が書けるか</li>
<li><strong>メタデータ：</strong>サンプリング、参照、電極配置、イベント定義、同期情報が揃うか</li>
<li><strong>QC：</strong>ノイズ・欠損・アーティファクトが定量化されているか</li>
<li><strong>比較：</strong>ベースラインがあり、同じ指標で比較できるか</li>
<li><strong>反証：</strong>データリーク検査、反事実テスト、失敗例の記録があるか</li>
</ul>
</div>
</section>

<section class="section" id="bids">
<h2 class="section-title">4) Mind-Uploadで「共有できるデータ」にする最短ルート</h2>
<p>
Mind-Uploadが目指すのは、単にデータを集めることではなく、<strong>第三者が検証できる形</strong>で残すことです。
そのための最短ルートは BIDS/EEG-BIDS に寄せることです。
</p>
<div class="cta-box">
<h4>Verification Commons</h4>
<p>「規格＋置き場＋評価」の設計図はこちら。</p>
<a href="verification.html">検証基盤を見る →</a>
</div>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>Related</h4>
<ul>
<li><a href="eeg_101.html">EEG入門 →</a></li>
<li><a href="tech_roadmap.html#measurement">Roadmap: 計測 →</a></li>
<li><a href="casework.html#data-standardization">Casework: 規格＋置き場 →</a></li>
<li><a href="glossary.html">用語集 →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Links</h4>
<ul>
<li><a href="https://bids.neuroimaging.io/" target="_blank">BIDS</a></li>
<li><a href="https://openneuro.org/" target="_blank">OpenNeuro</a></li>
<li><a href="https://physionet.org/" target="_blank">PhysioNet</a></li>
</ul>
</div>

</aside>
</main>

