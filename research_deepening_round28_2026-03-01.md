---
layout: default
title: "Research Deepening Round 28 (2026-03-01): 外部依存タスク分離と適用準備度の固定"
description: "10問いを外部依存タスクとリポジトリ内実行タスクに分離し、本文適用準備度を明示。"
article_type: "Evidence Addendum"
subtitle: "U12/U15 問い別の実行境界を固定"
author: Mind Uploading Research Project
last_updated: "2026-03-01"
note: "Round 28 (external dependency split and apply readiness)"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Round 28 の狙い</h2>
<p>
10問いそれぞれについて、外部依存タスク（ブラウザ実確認）と
このリポジトリ内で直ちに実行できるタスク（本文据え置き文/更新文適用）を分離しました。
これにより、continue 時の実行境界を明確化しています。
</p>
</div>

<section class="section" id="deliverables">
<h2 class="section-title">成果物</h2>
<ul>
<li><a href="automation/rq_regulation_external_dependency_tasks_round28_2026-03-01.csv" target="_blank">rq_regulation_external_dependency_tasks_round28_2026-03-01.csv</a>（外部依存タスク分離, 10行）</li>
<li><a href="automation/rq_regulation_apply_readiness_round28_2026-03-01.csv" target="_blank">rq_regulation_apply_readiness_round28_2026-03-01.csv</a>（本文適用準備度, 10行）</li>
</ul>
</section>

<section class="section" id="summary">
<h2 class="section-title">結果（平易版）</h2>
<table class="data-table">
<thead><tr><th>項目</th><th>値</th></tr></thead><tbody>
<tr><td>対象RQ</td><td>10問い</td></tr>
<tr><td>外部依存タスク分離</td><td>10件（担当/前提/完了条件を明記）</td></tr>
<tr><td>本文適用準備度</td><td>10件（現状は no_change 適用）</td></tr>
<tr><td>risk_flag=access_path_resolved</td><td>6件</td></tr>
<tr><td>risk_flag=stable</td><td>4件</td></tr>
<tr><td>作成時刻(UTC)</td><td>2026-03-01T14:43:35Z</td></tr>
</tbody></table>
</section>

<section class="section" id="next">
<h2 class="section-title">次の continue で行うこと</h2>
<ul>
<li>Round 26 の次回監視日（2026-03-08 UTC）に再監視を実行します。</li>
<li>差分が出た問いのみ Round 27 の更新文テンプレへ切り替えて本文反映します。</li>
</ul>
</section>

</article>
</main>
