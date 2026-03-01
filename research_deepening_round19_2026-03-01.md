---
layout: default
title: "Research Deepening Round 19 (2026-03-01): U12 規制トラック整合"
description: "U12 の補助文献を制度文書へ再配列し、タグ・読了順・時間目安を再計算。"
article_type: "Evidence Addendum"
subtitle: "U12/U15監査対象の整合を強化"
author: Mind Uploading Research Project
last_updated: "2026-03-01"
note: "Round 19 (U12 regulation alignment)"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Round 19 の狙い</h2>
<p>
Round 18 では U12 が監査対象なのに補助文献タグが experiment のままでした。
今回は U12 の補助文献を制度文書へ再配列し、タグ・読了順・時間目安を一貫させました。
</p>
</div>

<section class="section" id="deliverables">
<h2 class="section-title">成果物</h2>
<ul>
<li><a href="automation/rq_u12_regulation_alignment_round19_2026-03-01.csv" target="_blank">rq_u12_regulation_alignment_round19_2026-03-01.csv</a>（U12置換ログ, 6件）</li>
<li><a href="automation/rq_supplementary_thematic_tags_round19_2026-03-01.csv" target="_blank">rq_supplementary_thematic_tags_round19_2026-03-01.csv</a>（タグ再計算）</li>
<li><a href="automation/rq_reference_layering_round19_2026-03-01.csv" target="_blank">rq_reference_layering_round19_2026-03-01.csv</a>（二層化再計算）</li>
<li><a href="automation/rq_minimal_reading_path_round19_2026-03-01.csv" target="_blank">rq_minimal_reading_path_round19_2026-03-01.csv</a>（3ステップ再計算）</li>
<li><a href="automation/rq_reading_path_timed_round19_2026-03-01.csv" target="_blank">rq_reading_path_timed_round19_2026-03-01.csv</a>（時間目安再計算）</li>
</ul>
</section>

<section class="section" id="result">
<h2 class="section-title">結果（平易版）</h2>
<table class="data-table">
<thead><tr><th>項目</th><th>Round 18</th><th>Round 19</th></tr></thead><tbody>
<tr><td>tag_regulation</td><td>4</td><td>10</td></tr>
<tr><td>tag_experiment</td><td>44</td><td>38</td></tr>
<tr><td>update_audit_flag_yes</td><td>10</td><td>10</td></tr>
<tr><td>平均読了時間（分）</td><td>25.67</td><td>25.47</td></tr>
</tbody></table>
<p class="small">U12の6問いは、補助文献タグが experiment から regulation へ移行しました。</p>
</section>

<section class="section" id="next">
<h2 class="section-title">次の continue で行うこと</h2>
<ul>
<li>U12/U15 の regulation-track に法域ラベル（EU/CoE/NIST/OECD）を付与します。</li>
<li>法制度リンク差分監査（Round 15）を再実行し、監査フラグ行の優先更新キューを作ります。</li>
</ul>
</section>

</article>
</main>
