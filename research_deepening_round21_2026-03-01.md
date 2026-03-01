---
layout: default
title: "Research Deepening Round 21 (2026-03-01): Highキュー法制度リンク差分監査"
description: "Round 20 highキュー10件を対象に、法制度リンク差分監査を再実行。"
article_type: "Evidence Addendum"
subtitle: "priority=high の監視実行ログ"
author: Mind Uploading Research Project
last_updated: "2026-03-01"
note: "Round 21 (high queue legal-link diff check)"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Round 21 の狙い</h2>
<p>
Round 20 で作った priority=high キュー（10件）に対して、法制度リンクの差分監査を実行しました。
今回は URL差分とRQ差分の2層で、更新反映が必要かを判定しています。
</p>
</div>

<section class="section" id="deliverables">
<h2 class="section-title">成果物</h2>
<ul>
<li><a href="automation/rq_regulation_link_diff_round21_2026-03-01.csv" target="_blank">rq_regulation_link_diff_round21_2026-03-01.csv</a>（URL単位差分）</li>
<li><a href="automation/rq_regulation_priority_queue_status_round21_2026-03-01.csv" target="_blank">rq_regulation_priority_queue_status_round21_2026-03-01.csv</a>（RQ単位判定）</li>
</ul>
</section>

<section class="section" id="summary">
<h2 class="section-title">結果（平易版）</h2>
<table class="data-table">
<thead><tr><th>項目</th><th>値</th></tr></thead><tbody>
<tr><td>監査URL数</td><td>5</td></tr>
<tr><td>HTTP 2xx</td><td>5</td></tr>
<tr><td>URL差分あり</td><td>2</td></tr>
<tr><td>RQ差分あり</td><td>10</td></tr>
<tr><td>監査時刻(UTC)</td><td>2026-03-01T14:18:24Z</td></tr>
</tbody></table>
<p class="small">
補足: RQ差分ありが10件になっているのは、U12/U15 の high キューが同じ監視URL群を共有しているためです。
実際のURL単位の差分は2件（DOIリダイレクト初回確定と OECD URL の正規化）でした。
</p>
</section>

<section class="section" id="next">
<h2 class="section-title">次の continue で行うこと</h2>
<ul>
<li>差分あり行が発生した場合の本文更新テンプレを固定します。</li>
<li>制度文書の改訂履歴ページ直リンクを補完します。</li>
</ul>
</section>

</article>
</main>
