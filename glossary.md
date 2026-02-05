---
layout: default
title: "用語集（Glossary）"
description: "EEGFlowで頻出する用語を、人間が迷子にならない粒度でまとめます。厳密定義はRoadmapにリンクします。"
article_type: Reference
subtitle: "まずは“言葉のすり替え”を止める"
author: Mind Uploading Research Project
last_updated: "2026-02-05"
note: "Living document"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>How To Use</h2>
<p>
この用語集は「これ何？」を1分で解消するためのものです。厳密な定義や反証条件は、Roadmap（前進の定義）へリンクします。
WBEの議論は“言葉のすり替え”が起きやすいので、ここでは<strong>操作的にどう扱うか</strong>を重視します。
</p>
</div>

<section class="section" id="core">
<h2 class="section-title">コア概念</h2>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>EEGFlowでの意味（ざっくり）</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>マインドアップロード</strong></td>
<td>「意識や記憶をデジタルに移す」一般呼称。EEGFlowでは主張レベルをクレーム階段で分けて扱う。</td>
</tr>
<tr>
<td><strong>WBE（Whole Brain Emulation）</strong></td>
<td>脳の機能を別基盤で再現すること。何を再現したら“成功”かは定義依存なので、先に評価を固定する。</td>
</tr>
<tr>
<td><strong>クレーム階段（L0〜L5）</strong></td>
<td>成果の言い方を揃える枠組み。L1（デコーディング）をL4（本人性）と混同しないためのガードレール。</td>
</tr>
<tr>
<td><strong>検証基盤（Verification Commons）</strong></td>
<td>標準・データ・評価・登録・監査をまとめて提供し、「比較可能な前進」を積み上げる公共財。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="decode-emulate">
<h2 class="section-title">Decode と Emulate</h2>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>違い</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>デコーディング（Decoding）</strong></td>
<td>観測された信号から、状態・刺激・文章などを予測する（相関ベースになりやすい）。</td>
</tr>
<tr>
<td><strong>エミュレーション（Emulation）</strong></td>
<td>内部状態が時間発展し、介入に反応し、将来の出力を生成する（因果・生成の要求が強い）。</td>
</tr>
<tr>
<td><strong>反事実（Counterfactual）</strong></td>
<td>「もし条件Xを変えたら？」という分岐に対する予測。decode→emulateのギャップを埋める検証の中心。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="measurement">
<h2 class="section-title">計測（Measurement）</h2>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>メモ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG</strong></td>
<td>頭皮上の電位差を高時間分解能で測る。空間分解能は弱いので不確実性の扱いが重要。</td>
</tr>
<tr>
<td><strong>MEG</strong></td>
<td>磁場を測る。EEGとは異なる感度分布で補完関係があるが、装置は高価。</td>
</tr>
<tr>
<td><strong>fMRI</strong></td>
<td>血流（BOLD）を測る。空間分解能は良いが時間分解能は遅い。</td>
</tr>
<tr>
<td><strong>ECoG / 侵襲計測</strong></td>
<td>因果介入や高SNRの可能性がある一方、倫理・適用範囲の制約が大きい。</td>
</tr>
<tr>
<td><strong>QC（Quality Control）</strong></td>
<td>インピーダンス、ノイズ、欠損、アーティファクトなどを定量化し、ログとして残すこと。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="modeling">
<h2 class="section-title">モデル化（Modeling）</h2>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>EEGFlowでの使いどころ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>逆問題（Inverse Problem）</strong></td>
<td>観測（頭皮EEG）から原因（脳内活動）を推定する問題。一般に解が一意に定まらない。</td>
</tr>
<tr>
<td><strong>ESI（EEG Source Imaging）</strong></td>
<td>逆問題を解いて、脳内ソースを推定する。推定値だけでなく“不確実性”も一緒に扱うのが重要。</td>
</tr>
<tr>
<td><strong>DCM</strong></td>
<td>神経回路モデルを仮定し、結合を推定する枠組みの一種。介入設計と相性が良い。</td>
</tr>
<tr>
<td><strong>SCM（構造的因果モデル）</strong></td>
<td>因果関係を明示するモデル。反事実や介入予測を定義しやすい。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="open-science">
<h2 class="section-title">標準化・再現性（Open Science）</h2>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>意味</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>BIDS / EEG-BIDS</strong></td>
<td>神経計測データの整理規約。共有と再現の“最初の壁”を下げる。</td>
</tr>
<tr>
<td><strong>ベンチマーク</strong></td>
<td>タスク・データ・指標を固定して比較可能にする仕組み。</td>
</tr>
<tr>
<td><strong>ベースライン</strong></td>
<td>比較の出発点。改善を主張するならベースラインとの差分が必要。</td>
</tr>
<tr>
<td><strong>事前登録（Preregistration）</strong></td>
<td>“やる前”に計画を固定し、探索と検証を区別する。報告バイアスを減らす。</td>
</tr>
<tr>
<td><strong>モデルカード</strong></td>
<td>スコアだけでなく、学習データ、計算資源、既知の弱点、失敗例を公開するフォーマット。</td>
</tr>
</tbody>
</table>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>Related</h4>
<ul>
<li><a href="wbe_101.html">WBE入門 →</a></li>
<li><a href="eeg_101.html">EEG入門 →</a></li>
<li><a href="verification.html">検証基盤 →</a></li>
<li><a href="tech_roadmap.html#definition">前進の定義 →</a></li>
</ul>
</div>

<div class="note-box">
<strong>Note</strong>
<p>
この用語集は「統一のための暫定」です。曖昧な語は、Roadmap側で“測れる定義”に固定していきます。
</p>
</div>

</aside>
</main>

