---
layout: default
title: "Technical Proposal: Strengthening Thermodynamic and Causal Validity"
description: "Response to Issue #58: Addressing critical gaps in WBE framework regarding physical irreversibility, counterfactual identifiability, and computational complexity."
article_type: "Technical Proposal"
subtitle: "Issue #58: Response to Scientific Critique on Physics & Causality"
author: "mind-upload Project Contributor"
last_updated: "2026-02-01"
note: "Proposal (Implemented)"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Abstract</h2>
<p>
本提案書は、Issue #58「学術的批判：WBE実現フレームワークにおける熱力学的・因果論的整合性に関する重大な不備」に対する正式な技術的回答である。
指摘された3つの主要な不整合――(1) 生物学的脳の物理的不可逆性（NESS）とデジタル論理の乖離、(2) 反実仮想的等価性における数理的同定不能性、(3) IIT 4.0の計算量的爆発――に対し、
Mind-Uploadプロジェクトは以下の具体的修正を行うことで、科学的整合性を担保する。
</p>
</div>

<section class="section" id="thermodynamics">
<h2 class="section-title">1. Refining Thermodynamic Grounding (NESS)</h2>
<h3>1.1 Problem: The "Dissipation" Gap</h3>
<p>
デジタル計算機上のシミュレーションは、原理的に「論理的可逆性」を持ちうる（Landauer限界まで熱を出さない）が、生物学的脳は非平衡定常状態（NESS）にあり、常にエントロピーを生成し続けることで構造を維持している。
単なる計算コスト（Information Cost）の加算だけでは、この「存在のコスト」を表現できない。
</p>
<h3>1.2 Solution: Virtual Dissipation Protocol</h3>
<p>
<code>mind-upload/03_causal_modeling.py</code> において、以下の指標を導入する。
</p>
<ul>
<li><strong>Entropy Production Rate (EPR):</strong> システムの状態遷移が時間反転対称性を破る度合い（不可逆性）を定量化する。</li>
<li><strong>Metabolic Flux:</strong> 計算の有無に関わらず、モデルの構造的完全性（Structural Integrity）を維持するために消費され、熱として散逸される仮想エネルギー流。</li>
</ul>
<p>
これにより、WBEが「停止しても存在し続ける」静的なファイルではなく、「エネルギーを消費し続けなければ崩壊する」動的な散逸構造であることをシミュレート上で要請する。
</p>
</section>

<section class="section" id="identifiability">
<h2 class="section-title">2. Counterfactual Identifiability & Equivalence Classes</h2>
<h3>2.1 Problem: Uniqueness of Counterfactuals</h3>
<p>
Pearlの因果階層（Level 3）における反実仮想は、観測データ（Level 1）および介入データ（Level 2）から一意に定まらない（Markov Equivalence Classの問題）。
特定の構造方程式（SCM）を仮定せずに「反実仮想的等価性」を主張することは数学的に誤りである。
</p>
<h3>2.2 Solution: Explicit Assumptions & Equivalence Checks</h3>
<p>
「すべてのSCMを一意に同定できる」という過度な主張を取り下げ、以下の現実的なアプローチに修正する。
</p>
<ul>
<li><strong>Assumption Explicit:</strong> 反実仮想計算において仮定している関数形（線形性、加法性ノイズ等）を明示する。</li>
<li><strong>Equivalence Class Warning:</strong> 観測データと矛盾しないが、異なる反実仮想予測を与える「同等のモデル」が存在する可能性を常に計算し、その範囲（Bounds）を提示する。</li>
</ul>
</section>

<section class="section" id="complexity">
<h2 class="section-title">3. Addressing Computational Complexity of IIT 4.0</h2>
<h3>3.1 Problem: The NP-Hard Barrier</h3>
<p>
IIT 4.0の $\Phi$ 計測は、システムの部分系（Power Set）を探索するため、要素数 $n$ に対して $O(2^n)$ の計算量を要する。全脳レベルでの厳密な計算は不可能である。
</p>
<h3>3.2 Solution: Approximation & "Cut" Heuristics</h3>
<p>
「厳密な $\Phi$ の計算」をロードマップから削除し、以下の近似手法を採用する。
</p>
<ul>
<li><strong>PyPhi Approximation:</strong> 全探索を行わず、重要な分割（Minimum Information Partition, MIP）の候補をヒューリスティックに絞り込む（"Queyranne's algorithm" の応用等）。</li>
<li><strong>Sparse Phi / Effective Information:</strong> 結合が密な局所モジュール（Complex）内でのみ $\Phi$ を計算し、全脳レベルではそれらの相互作用を見るアプローチに切り替える。</li>
</ul>
</section>

<section class="section" id="conclusion">
<h2 class="section-title">4. Implementation Plan</h2>
<p>
本提案に基づき、直ちに <code>mind-upload/03_causal_modeling.py</code> および <code>tech_roadmap.md</code> を更新する。
これは、WBEを「魔法のコピー」から「物理法則と計算理論に縛られた工学的課題」へと再定義する重要なステップである。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>On this page</h4>
<ul>
<li><a href="#thermodynamics">1. Thermodynamics (NESS)</a></li>
<li><a href="#identifiability">2. Identifiability</a></li>
<li><a href="#complexity">3. IIT Complexity</a></li>
<li><a href="#conclusion">4. Implementation</a></li>
</ul>
</div>
</aside>
</main>
