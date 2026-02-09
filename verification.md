---
layout: default
title: "検証基盤：Mind Uploading Verification Commons"
description: "マインドアップロード/WBEを「進歩を測れる科学」に寄せるための、標準・ベンチマーク・登録・監査の設計図。"
article_type: Platform
subtitle: "PDB×BIDS×PhysioNet×OSFの発想で、WBEの“勝利条件”と“再現可能な前進”を作る"
author: Mind Uploading Research Project
last_updated: "2026-02-05"
note: "Operational Specification"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>One Problem</h2>
<p>
マインドアップロード（WBE）を「夢の話」で終わらせないために、まず必要なのは<strong>共通のルール</strong>です。Mind-Uploadでは、データの置き方、評価のしかた、失敗の判定、再現手順を先にそろえて、誰でも同じ基準で確かめられる土台を作ります。
</p>
</div>

<section class="section" id="tldr">
<h2 class="section-title">TL;DR（人間向け）</h2>
<div class="key-points">
<h4>3つだけ覚える</h4>
<ul>
<li><strong>主張より先に物差し：</strong>「何を満たせば前進か」を固定しないと、成果が比較できない</li>
<li><strong>データだけでも不足：</strong>規格（標準）＋置き場（共有）＋評価（ベンチ）がセットで必要</li>
<li><strong>WBEは特に“すり替え”が起きる：</strong>decode（相関）を emulation（生成/因果）と混同しない</li>
</ul>
</div>
</section>

<section class="section" id="definition">
<h2 class="section-title">このサイトで解く「1問」</h2>
<p>
<strong>問い：</strong>「何を満たせば“前進”と言えるか？」を事前に固定し、第三者が同じ入力（データ）で同じ結論（評価）に到達できる状態を作る。
</p>
<div class="key-points">
<h4>Outcome</h4>
<ul>
<li><strong>勝利条件の固定：</strong>クレーム階段（L0〜L5）を明示し、L1をL4のように語る“すり替え”を防ぐ</li>
<li><strong>再現可能な入力：</strong>BIDS等の標準＋メタデータで、解析対象を第三者に渡せる</li>
<li><strong>比較可能な出力：</strong>スコア・ログ・失敗例まで含む評価スイートを公開する</li>
<li><strong>継続運用：</strong>ベンチマーク更新、バージョン管理、監査ログで公共財を積み上げる</li>
</ul>
</div>
</section>

<section class="section" id="non-goals">
<h2 class="section-title">これは何ではないか（誤解防止）</h2>
<div class="note-box">
<strong>Non-goals</strong>
<p>
このページは「マインドアップロードが可能/不可能」を断言する場所ではありません。Mind-Uploadが作るのは、<strong>断言が可能になるための検証基盤</strong>です（測定・評価・反証のルール）。
</p>
</div>
</section>

<section class="section" id="deliverables">
<h2 class="section-title">Mind-Upload Commons の成果物（公共財）</h2>
<div class="stage-list">
<div class="stage-item">
<div class="stage-number">01</div>
<div class="stage-body">
<h4>Data Standard（入力の固定）</h4>
<p>BIDS/EEG-BIDSをベースに、課題・刺激・同期・QC・匿名化のメタデータを拡張し、「解析可能な形」で共有できる規格を整備する。</p>
<div class="tag-list">
<span class="tag">BIDS</span><span class="tag">EEG</span><span class="tag">Metadata</span><span class="tag">QC</span>
</div>
</div>
</div>
<div class="stage-item">
<div class="stage-number">02</div>
<div class="stage-body">
<h4>Benchmark Suite（出力の固定）</h4>
<p>デコーディング（相関）だけでなく、<strong>反事実・介入予測</strong>や<strong>閉ループ安定性</strong>まで含めたタスク群を定義し、同じ物差しで比較できる状態にする。</p>
<div class="tag-list">
<span class="tag">Counterfactual</span><span class="tag">Intervention</span><span class="tag">Closed-loop</span>
</div>
</div>
</div>
<div class="stage-item">
<div class="stage-number">03</div>
<div class="stage-body">
<h4>Registry & Prereg（“やる前”の固定）</h4>
<p>実験・解析計画を事前登録し、探索と検証を区別する。プロトコルと変更履歴を残し、報告バイアスを下げる。</p>
<div class="tag-list">
<span class="tag">Preregistration</span><span class="tag">Protocol</span><span class="tag">Audit</span>
</div>
</div>
</div>
<div class="stage-item">
<div class="stage-number">04</div>
<div class="stage-body">
<h4>Leaderboard & Model Cards（比較の運用）</h4>
<p>スコアだけでなく、データリーク対策、失敗例、計算資源、既知の弱点を“カード”として公開し、再現性と安全性を担保する。</p>
<div class="tag-list">
<span class="tag">Leaderboard</span><span class="tag">Reproducibility</span><span class="tag">Safety</span>
</div>
</div>
</div>
</div>
</section>

<section class="section" id="example">
<h2 class="section-title">具体例：1つの「比較可能な前進」はこう見える</h2>
<p>たとえば「EEGから状態を推定するモデル」を例にすると、Commonsとして必要なのは次の4点です。</p>
<table class="data-table">
<thead>
<tr>
<th>要素</th>
<th>最低限の中身（例）</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>入力（Data）</strong></td>
<td>BIDS準拠のデータ一式、計測条件、同期ログ、QCログ、匿名化/同意の範囲</td>
</tr>
<tr>
<td><strong>手順（Code/Protocol）</strong></td>
<td>前処理→特徴→学習→評価の固定レシピ、環境情報、乱数シード</td>
</tr>
<tr>
<td><strong>出力（Metrics）</strong></td>
<td>スコア（精度/不確実性/頑健性）、失敗例、ベースラインとの差分</td>
</tr>
<tr>
<td><strong>反証（Falsification）</strong></td>
<td>データリーク検査、反事実テスト、刺激条件の変更に対する予測外れの記録</td>
</tr>
</tbody>
</table>
<p>これが揃うと「誰がやっても同じ条件で比較できる」ようになり、はじめて進捗が積み上がります。</p>
</section>

<section class="section" id="casework">
<h2 class="section-title">歴史のケースワークから借りる設計</h2>
<p>
Mind-Uploadの設計は“新規発明”ではなく、他分野が既に解いてきた「検証の型」の移植です。代表例は <a href="casework.html">ケースワーク集</a> に整理しています。
</p>
<div class="note-box">
<strong>移植のコツ</strong>
<p>
PDB（単一アーカイブ）やBIDS+OpenNeuro（規格＋置き場）、PhysioNet（データ＋評価）、OSF/PROSPERO（事前登録）などの型は、分野が違っても「前進を測れる」構造を作ります。WBEは特に、<strong>達成条件</strong>と<strong>反証条件</strong>を先に固定する必要があります。
</p>
</div>
</section>




</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>Start Here</h4>
<ul>
<li><a href="tech_roadmap.html#definition">前進の定義（Roadmap）→</a></li>
<li><a href="casework.html">ケースワーク集（歴史の型）→</a></li>
<li><a href="research_harvest_50.html">50ワーカー文献地図（未解決問題分解）→</a></li>
<li><a href="proposals.html">技術提案の一覧（Issue連動）→</a></li>
<li><a href="glossary.html">用語集（Glossary）→</a></li>
<li><a href="datasets.html">データ&ベンチ（Datasets）→</a></li>
<li><a href="faq.html">FAQ →</a></li>
<li><a href="hands_on.html">ハンズオン（L0）→</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Related Pages</h4>
<ul>
<li><a href="idea.html">Framework（理論）→</a></li>
<li><a href="mind_uploading_papers.html">Papers（文献）→</a></li>
<li><a href="issue.html">Contribute（参加）→</a></li>
</ul>
</div>

<div class="note-box">
<strong>Scope</strong>
<p>
このページは「最終結論」を主張する場所ではなく、研究が積み上がるための<strong>ルールと成果物</strong>を置く場所です。大きな主張ほど、先に“小さく反証できる形”に分解します。
</p>
</div>

</aside>
</main>
