---
layout: default
title: "技術提案書：反実仮想的等価性検証における識別可能性と因果的介入"
description: "Mind Uploadingにおける同一性検証のための、摂動複雑性指数（PCI）とdo-calculusの導入について"
article_type: "Technical Proposal"
subtitle: "Issue #56: Identifiability and Causal Intervention"
author: "mind-upload Project Contributor"
last_updated: "2026-01-30"
note: "Proposal (Draft)"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Abstract</h2>
<p>
本提案書は、Mind Uploadingの同一性検証要件として提唱されている「反実仮想的等価性（Counterfactual Equivalence）」の実装可能性における課題を指摘し、その解決策を提示するものである。
Pearlの因果階層（Causal Hierarchy）に基づき、単なる観測データからは反実仮想（Level 3）が識別不可能であることを論じる。
解決策として、<strong>摂動複雑性指数（Perturbational Complexity Index: PCI）</strong>をGround Truthとして採用し、<strong>do-calculus</strong>を用いた能動的介入による構造的因果モデル（SCM）の同定プロセスを導入することを提案する。
</p>
</div>

<section class="section" id="problem-statement">
<h2 class="section-title">1. 問題の所在：識別不可能性の壁</h2>
<p>
以前のフレームワーク（Issue #38）では、デジタルエミュレーションが生物学的脳と「同一」であるための条件として、実際に起きたことだけでなく、「もし別の入力があったらどう反応したか」という反実仮想的な振る舞いの一致を求めた。
しかし、生物学的システムにおいて、観測可能なデータ（Level 1: Association）のみから、内部の因果構造や反実仮想（Level 3: Counterfactuals）を一意に決定（識別）することは数理的に不可能である。
</p>
<p>
すなわち、外部からの入力に対する出力が完全に一致していても、内部構造が異なる「哲学的ゾンビ」的なモデルを、受動的な観測だけでは排除できない。
</p>
</section>

<section class="section" id="proposal">
<h2 class="section-title">2. 提案手法：介入による因果構造の同定</h2>
<p>
この問題を解決するために、システムへの直接的な「介入（Intervention）」を検証プロセスに必須事項として組み込む。
</p>

<h3>2.1 Perturbational Complexity Index (PCI) の導入</h3>
<p>
意識の有無を判定する臨床指標として確立されつつあるPCIを、同一性検証の「ものさし」として利用する。
</p>
<ul>
<li><strong>Biological Brain:</strong> TMS（経頭蓋磁気刺激）により皮質に直接摂動を与え、EEGでその応答の時空間的な複雑さを計測する（PCI）。</li>
<li><strong>Digital Emulation:</strong> デジタル脳モデルに対して、等価な仮想的摂動（Virtual TMS）を与え、その応答（Virtual PCI）を計算する。</li>
</ul>
<p>
両者のPCI値だけでなく、摂動に対する「応答の時空間パターン」自体が高度に相関することを要求する。これにより、静的な結合マップだけでなく、動的な因果構造の一致を検証する。
</p>

<h3>2.2 do-calculus による介入モデリング</h3>
<p>
Judea Pearlのdo-calculusを導入し、エミュレーションモデルへの介入を形式化する。
</p>
<ul>
<li>観測データ: $P(Y | X)$ - Xを見たときのYの確率（受動的）</li>
<li>介入データ: $P(Y | do(X))$ - Xを強制的に操作したときのYの確率（能動的）</li>
</ul>
<p>
エミュレーションの検証において、観測データの一致 $P_{bio}(Y|X) = P_{digital}(Y|X)$ だけでなく、あらゆる介入 $do(X_i)$ に対して $P_{bio}(Y|do(X_i)) = P_{digital}(Y|do(X_i))$ が成立することを確認するループを構築する。
</p>
</section>

<section class="section" id="implementation">
<h2 class="section-title">3. 実装への影響</h2>
<p>
既存の因果モデリングスクリプト（<code>03_causal_modeling.py</code>）に対し、以下の拡張を行う必要がある。
</p>
<ol>
<li><strong>Intervention Interface:</strong> モデルの状態変数を強制的に書き換える <code>apply_do_operator()</code> メソッドの実装。</li>
<li><strong>PCI Calculation:</strong> インパルス応答からLZ複雑性等を算出するロジックの追加（またはプレースホルダー）。</li>
<li><strong>Verification Loop:</strong> 受動的な予測誤差最小化ループに加え、定期的な「介入テスト」を行う検証フェーズの追加。</li>
</ol>
</section>

<section class="section" id="references">
<h2 class="section-title">4. 参考文献</h2>
<ol>
<li>Pearl, J. (2009). <i>Causality: Models, Reasoning, and Inference</i>. Cambridge University Press.</li>
<li>Casali, A. G., et al. (2013). A theoretically based index of consciousness independent of sensory processing and behavior. <i>Science Translational Medicine</i>.</li>
</ol>
</section>

</article>
</main>
