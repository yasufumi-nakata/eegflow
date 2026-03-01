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
<li><code>automation/rq_deepening_backlog_2026-03-01.csv</code>: 全60問いの実行バックログ</li>
<li><code>automation/rq_deepening_backlog_2026-03-01_enriched.csv</code>: 上記 + 一次情報リンク + 根拠確度</li>
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
