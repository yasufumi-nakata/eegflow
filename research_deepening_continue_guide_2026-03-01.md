---
layout: default
title: "Continue運用ガイド: リサーチクエスチョン深掘り"
description: "continue 指示時に、各問いを網羅的に深掘りするための実行ガイド。"
article_type: "Operations"
subtitle: "60問いの反復調査フロー"
author: Mind Uploading Research Project
last_updated: "2026-03-01"
note: "for iterative deep research"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<section class="section" id="purpose">
<h2 class="section-title">目的</h2>
<p>
このガイドは、ユーザーから <code>continue</code> と指示されたときに、
全リサーチクエスチョンを漏れなく深掘りするための手順を固定するものです。
</p>
</section>

<section class="section" id="assets">
<h2 class="section-title">使用ファイル</h2>
<ul>
<li><code>research_harvest_50.md</code>: 元の問い定義（U0-U15）</li>
<li><code>research_deepening_2026-03-01.md</code>: 平易な追補説明</li>
<li><code>research_deepening_round2_2026-03-01.md</code>: U0/U1/U3 の深掘り追補（Round 2）</li>
<li><code>research_deepening_round3_2026-03-01.md</code>: U4/U7 の深掘り追補（Round 3）</li>
<li><code>research_deepening_round4_2026-03-01.md</code>: U8 の深掘り追補（Round 4）</li>
<li><code>research_deepening_round5_2026-03-01.md</code>: U10/U11/U12 の深掘り追補（Round 5）</li>
<li><code>research_deepening_round6_2026-03-01.md</code>: U13/U14/U15 の深掘り追補（Round 6）</li>
<li><code>research_deepening_round7_2026-03-01.md</code>: U8/U13/U14/U15 の参照精査（Round 7）</li>
<li><code>automation/rq_deepening_backlog_2026-03-01.csv</code>: 全60問いの実行バックログ</li>
<li><code>automation/rq_deepening_backlog_2026-03-01_enriched.csv</code>: 上記 + 一次情報リンク + 根拠確度</li>
<li><code>automation/rq_deepening_progress_round2_2026-03-01.csv</code>: Round 2 進捗管理（U0/U1/U3）</li>
<li><code>automation/rq_deepening_progress_round3_2026-03-01.csv</code>: Round 3 進捗管理（U4/U7）</li>
<li><code>automation/rq_deepening_progress_round4_2026-03-01.csv</code>: Round 4 進捗管理（U8）</li>
<li><code>automation/rq_deepening_progress_round5_2026-03-01.csv</code>: Round 5 進捗管理（U10/U11/U12）</li>
<li><code>automation/rq_deepening_progress_round6_2026-03-01.csv</code>: Round 6 進捗管理（U13/U14/U15）</li>
<li><code>automation/rq_deepening_consistency_audit_2026-03-01.md</code>: 全60問いの整合性監査（coverage missing=0）</li>
<li><code>automation/rq_deepening_coverage_summary_2026-03-01.csv</code>: U別カバレッジ集計</li>
<li><code>automation/rq_reference_relevance_audit_2026-03-01.md</code>: 引用関連性の機械点検（要目視確認）</li>
<li><code>automation/rq_reference_manual_triage_round7_2026-03-01.csv</code>: 高ノイズ比率ユニットの手動トリアージ</li>
</ul>
</section>

<section class="section" id="progress">
<h2 class="section-title">進捗（2026-03-01時点）</h2>
<ul>
<li>Round 1: U0-U15 を平易に再整理済み。</li>
<li>Round 2: U0/U1/U3 の全14問いを深掘りし、追加一次情報を紐づけ済み。</li>
<li>Round 3: U4/U7 の全10問いを深掘りし、追加一次情報を紐づけ済み。</li>
<li>Round 4: U8 の全6問いを深掘りし、追加一次情報を紐づけ済み。</li>
<li>Round 5: U10/U11/U12 の全14問いを深掘りし、追加一次情報を紐づけ済み。</li>
<li>Round 6: U13/U14/U15 の全16問いを深掘りし、追加一次情報を紐づけ済み。</li>
<li>Round 7: U8/U13/U14/U15 の疑義文献 32件を手動トリアージし、置換候補を固定済み。</li>
<li>統合反映: research_harvest_50.md 本体へ Round 1-7 結果を統合済み。</li>
<li>整合監査: 全60問いカバレッジ監査と引用関連性点検を生成済み。</li>
<li>次回 continue の優先対象: research_harvest_50.md の主要先行研究リストを、Round 7 判定に沿って段階置換。</li>
</ul>
</section>

<section class="section" id="loop">
<h2 class="section-title">continue時の反復フロー</h2>
<ol>
<li>未完了の問いを <code>rq_deepening_backlog_2026-03-01_enriched.csv</code> から抽出します。</li>
<li>各問いについて、一次情報を最低2件追加します（DOI / PubMed / 公式規格）。</li>
<li>「何が分かったか」「何が未解決か」を分離して追記します。</li>
<li>外部依存タスクは、担当者・前提・完了条件を明記して分離します。</li>
<li>差分・検証結果をコミットし、都度 push します。</li>
</ol>
</section>

<section class="section" id="done-criteria">
<h2 class="section-title">1問いの完了条件</h2>
<ul>
<li>一次情報リンクが2件以上あること</li>
<li>評価指標（metric）が定義されていること</li>
<li>このリポジトリで今すぐ実行できる次作業が1件以上あること</li>
<li>外部依存タスクが分離されていること</li>
</ul>
</section>

<section class="section" id="notes">
<h2 class="section-title">注意点</h2>
<ul>
<li>理論先行領域（U10/U12/U13）は、断定ではなく確度ラベルを維持します。</li>
<li>法制度領域（U15）は、必ず最新の公式文書日付を確認します。</li>
<li>計測領域（U1/U7/U8）は、閾値を数値で記録します。</li>
</ul>
</section>

</article>
</main>
