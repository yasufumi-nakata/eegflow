---
layout: default
title: "ハンズオン：再現可能なEEG解析（L0）を最短で作る"
description: "公開データでも自前データでも使える、BIDS→QC→前処理→評価の“最小ループ”を作る手順。"
article_type: Tutorial
subtitle: "まずは“再現できる”を達成してから、性能を競う"
author: Mind Uploading Research Project
last_updated: "2026-02-05"
note: "Practical"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Goal</h2>
<p>
ここでの目標は「賢いモデルを作る」ではなく、<strong>第三者が同じ結果を再現できる最小ループ（L0）</strong>を作ることです。
L0がないと、どんなSOTA主張も“検証不能”になり、積み上がりません。
</p>
</div>

<section class="section" id="overview">
<h2 class="section-title">最小ループ（L0）の形</h2>
<div class="key-points">
<h4>L0 Loop</h4>
<ul>
<li><strong>入力：</strong>BIDS（データ + メタデータ）</li>
<li><strong>品質：</strong>QCログ（数値で）</li>
<li><strong>処理：</strong>前処理の設定・バージョン・乱数を記録</li>
<li><strong>出力：</strong>ベースライン指標（最低1つ）</li>
<li><strong>監査：</strong>失敗例・除外基準も残す</li>
</ul>
</div>
</section>

<section class="section" id="bids-skeleton">
<h2 class="section-title">Step 1：BIDSの“骨格”を作る</h2>
<p>EEGのBIDSは「置き方が決まっている」のが強みです。まずは最小構成で形だけ作ります。</p>

<div class="note-box">
<strong>例：最小ディレクトリ</strong>
<p>（実データがなくても、構造だけは先に作れます）</p>
</div>

```text
my_bids_eeg/
  dataset_description.json
  participants.tsv
  sub-01/
    eeg/
      sub-01_task-rest_eeg.edf
      sub-01_task-rest_eeg.json
      sub-01_task-rest_channels.tsv
      sub-01_task-rest_events.tsv
```

<p>
`dataset_description.json` はすでにこのリポジトリにも雛形があります（概念段階ですが、発想は同じです）。
</p>
</section>

<section class="section" id="validator">
<h2 class="section-title">Step 2：BIDS Validator を回す</h2>
<p>
機械的にチェックできる部分は、機械に任せます。BIDS Validatorは「規格違反」を早期に潰すための重要な道具です。
</p>

```bash
# Node.js がある環境で
npx bids-validator my_bids_eeg
```

<div class="note-box">
<strong>ポイント</strong>
<p>
Validatorが通る＝研究として十分、ではありません。でも、通らない状態で“共有”はほぼ成立しません。
</p>
</div>
</section>

<section class="section" id="qc">
<h2 class="section-title">Step 3：QCログを“数値”で残す</h2>
<p>
再現性が壊れる典型は「どのデータが悪かったか」が人依存になることです。最低限、次をログにします。
</p>
<div class="key-points">
<h4>QC Items</h4>
<ul>
<li><strong>欠損/飽和：</strong>チャンネルごとの欠損率、飽和区間</li>
<li><strong>ノイズ：</strong>電源周波数のピーク、ノイズフロア推定</li>
<li><strong>アーティファクト：</strong>眼球/筋電/動きの混入指標</li>
<li><strong>除外基準：</strong>どの閾値で除外したか（理由つき）</li>
</ul>
</div>
</section>

<section class="section" id="baseline">
<h2 class="section-title">Step 4：ベースラインを1本置く（最初は小さく）</h2>
<p>
最初は “たった1つの指標” で十分です。例：
安静EEGのスペクトル要約、睡眠段階分類のベースライン、運動想起の2クラス分類など。
</p>
<div class="note-box">
<strong>重要</strong>
<p>
「ベースラインがある」と「改善を主張できる」ようになります。ベースラインなしのSOTA議論は、ほぼノイズになります。
</p>
</div>
</section>

<section class="section" id="tie-to-verification">
<h2 class="section-title">このハンズオンがVerificationに繋がる点</h2>
<p>
ここまでできると、次は「同じ物差しで比較できる」方向へ進めます。つまり、ベンチマーク化です。
</p>
<div class="cta-box">
<h4>Next</h4>
<p>L0を“公共財”にして積み上げる設計図。</p>
<a href="verification.html">検証基盤を見る →</a>
</div>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>Related</h4>
<ul>
<li><a href="datasets.html">データ&ベンチ →</a></li>
<li><a href="eeg_101.html">EEG入門 →</a></li>
<li><a href="tech_roadmap.html#definition">前進の定義 →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>External</h4>
<ul>
<li><a href="https://bids.neuroimaging.io/" target="_blank">BIDS</a></li>
<li><a href="https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/03-electroencephalography.html" target="_blank">BIDS EEG Spec</a></li>
</ul>
</div>

</aside>
</main>

