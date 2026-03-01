---
layout: default
title: "Research Deepening Round 16 (2026-03-01): 補助文献タグ再分類"
description: "全60問いの supplementary_1 を 実験/規制/運用 タグへ再分類。"
article_type: "Evidence Addendum"
subtitle: "RQごとの読み分けを明示する運用ラウンド"
author: Mind Uploading Research Project
last_updated: "2026-03-01"
note: "Round 16 (supplementary thematic tagging)"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Round 16 の狙い</h2>
<p>
補助文献は揃いましたが、読み手によって「何を先に読むか」がぶれやすい状態でした。
そこで全60問いについて、補助文献を <strong>実験</strong> / <strong>規制</strong> / <strong>運用</strong> の3タグで再分類しました。
</p>
</div>

<section class="section" id="deliverables">
<h2 class="section-title">成果物</h2>
<ul>
<li><a href="automation/rq_supplementary_thematic_tags_round16_2026-03-01.csv" target="_blank">rq_supplementary_thematic_tags_round16_2026-03-01.csv</a>（60行）</li>
<li><a href="automation/rq_supplementary_thematic_tag_summary_round16_2026-03-01.csv" target="_blank">rq_supplementary_thematic_tag_summary_round16_2026-03-01.csv</a>（集計）</li>
</ul>
</section>

<section class="section" id="summary">
<h2 class="section-title">タグ集計（平易版）</h2>
<table class="data-table">
<thead><tr><th>タグ</th><th>件数</th><th>意味</th></tr></thead><tbody>
<tr><td>experiment</td><td>44</td><td>実験結果・理論レビューとして読む</td></tr>
<tr><td>regulation</td><td>4</td><td>制度・規格要件として読む</td></tr>
<tr><td>operation</td><td>12</td><td>実装・運用手順として読む</td></tr>
</tbody></table>
</section>

<section class="section" id="how-to-read">
<h2 class="section-title">読み分けルール</h2>
<ol>
<li>RQの結論根拠を補強したい場合は <code>experiment</code> を先に確認します。</li>
<li>権利・責任・適用範囲を決める場合は <code>regulation</code> を先に確認します。</li>
<li>データ処理や監査手順を決める場合は <code>operation</code> を先に確認します。</li>
</ol>
</section>

<section class="section" id="next">
<h2 class="section-title">次の continue で行うこと</h2>
<ul>
<li>タグ別に「必須/補助」の二層を追加し、RQごとの最短読了順を固定します。</li>
<li>U12/U15 は regulation タグを中心に更新差分監査を継続します。</li>
</ul>
</section>

</article>
</main>
