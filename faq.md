---
layout: default
title: "FAQ：よくある質問（と、よくある事故）"
description: "Mind-Uploadを読んでいて出やすい疑問に、短く正確に答えます。"
article_type: FAQ
subtitle: "派手な結論より、検証できる前進を"
author: Mind Uploading Research Project
last_updated: "2026-02-10"
note: "Human-first"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>How To Read</h2>
<p>
ここは「よくある勘違い」を先に避けるためのページです。主張が大きいほど、(1)言葉の定義、(2)評価の物差し、(3)間違いと判定する条件、(4)再現手順の順で確認します。
</p>
</div>

<section class="section" id="q0">
<h2 class="section-title">Q. Mind-Uploadは結局、何をするサイト？</h2>
<p>
A. マインドアップロード/WBEを「検証可能な研究プログラム」に寄せるための<strong>検証基盤（Verification Commons）</strong>を作るサイトです。
データ（入力）、評価（出力）、ルール（達成条件/反証条件）、運用（継続）を先に固定します。
</p>
<div class="cta-box">
<h4>Start</h4>
<p>全体像はここから。</p>
<a href="verification.html">検証基盤を見る →</a>
</div>
</section>

<section class="section" id="q1">
<h2 class="section-title">Q. EEGで“思考”は読める？</h2>
<p>
A. 「何をどこまで」と定義しない限り答えられません。EEGはノイズと個体差が大きく、言語モデルも尤もらしい文を補完するため、EEG由来情報とモデル補完を反事実テストで分離する手順を先に固定します。
</p>
<p>
Mind-Uploadの立場は、「派手な読み出し」を否定するのではなく、<strong>検証可能な主張に落とす</strong>ことです（失敗例まで含む）。
</p>
</section>

<section class="section" id="q2">
<h2 class="section-title">Q. decode（デコーディング）と emulate（エミュレーション）の違いは？</h2>
<p>
A. decodeは“観測を翻訳する”ことで、emulateは“内部状態が時間発展し、介入に反応し、出力を生成する”ことです。
WBEに近づくには、後者を評価できるベンチマーク（介入・反事実・閉ループ）へ寄せる必要があります。
</p>
<p><a href="wbe_101.html">入門（WBE 101）</a>と<a href="glossary.html">用語集</a>が近道です。</p>
</section>

<section class="section" id="q3">
<h2 class="section-title">Q. じゃあ、何を作れば“前進”になる？</h2>
<p>
A. まずは L0〜L2 が現実的です。つまり「再現できる解析」「比較できるベンチ」「介入予測で検証できるモデル」です。
Mind-Uploadでは、これを“サイトとして運用できる形”に落とします（テンプレ・ログ・ルール）。
</p>
<div class="key-points">
<h4>具体的な成果物</h4>
<ul>
<li><strong>入力：</strong>BIDS/EEG-BIDS + メタデータ + QCログ</li>
<li><strong>手順：</strong>固定パイプライン + 実行ログ + 失敗例</li>
<li><strong>出力：</strong>指標（スコア） + ベースライン差分 + 反証条件の結果</li>
</ul>
</div>
</section>

<section class="section" id="q4">
<h2 class="section-title">Q. なぜ“標準化”がそんなに大事？</h2>
<p>
A. 標準がないと、同じことを言っているようで違う入力・違う手順・違う指標を比較してしまい、進捗が見えなくなります。
PDBやBIDS+OpenNeuroなどの事例は、分野が違っても「前進を測れる」状態を作った点が共通しています。
</p>
<p><a href="casework.html">ケースワーク集</a>に、設計の型をまとめています。</p>
</section>

<section class="section" id="q5">
<h2 class="section-title">Q. “ベンチマークの罠”って何？</h2>
<p>
A. 指標に勝つことが、現実の目的達成とズレる現象です（Goodhartの罠）。
例えば、データリークや過学習でスコアだけ上がる、実装コストが高すぎて実運用されない、などがあります。
Mind-Uploadでは、失敗例・リーク検査・モデルカードを含めて運用設計します。
</p>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>Shortcuts</h4>
<ul>
<li><a href="index.html">Start →</a></li>
<li><a href="verification.html">Verification →</a></li>
<li><a href="wbe_101.html">WBE 101 →</a></li>
<li><a href="eeg_101.html">EEG 101 →</a></li>
<li><a href="datasets.html">Datasets →</a></li>
<li><a href="glossary.html">Glossary →</a></li>
</ul>
</div>

</aside>
</main>
