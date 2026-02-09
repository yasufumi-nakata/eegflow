---
layout: default
title: "Technical Proposal: Addressing Logical Gaps in Causal Modeling and Thermodynamic Grounding"
description: "Response to Issue #61: Refining the physical and causal foundations of Whole Brain Emulation"
article_type: "Technical Proposal"
subtitle: "Issue #61: mind-upload.com Causal & Thermodynamic Critique Response"
author: "mind-upload Project Contributor"
last_updated: "2026-02-10"
note: "Proposal (Implemented)"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Abstract</h2>
<p>
本提案書は、Issue #61で提起された「因果モデリングおよび熱力学的基盤における論理的ギャップ」に対する正式な回答および技術的修正案である。
従来のデジタルエミュレーションアプローチが抱える「展開論法（Unfolding Argument）」への脆弱性、意識の熱力学的コスト（TCC）の過度な単純化、および反実仮想的等価性の検証における数理的厳密さの欠如について、具体的な改善策を提示する。
特に、<code>03_causal_modeling.py</code> における代謝的オーバーヘッドの導入、SCM識別可能性の要件としての摂動複雑性（PCI）の位置づけ、および「マルチモデル推論（Multi-Model Inference）」への理論的転換について詳述する。
</p>
</div>

<section class="section" id="introduction">
<h2 class="section-title">1. Introduction: Critique as a Catalyst</h2>
<p>
Issue #61で問われたのは、WBEがソフトウェア的な模倣で終わるのか、それとも脳と同じ因果メカニズムまで再現できるのかという点である。本提案はこの疑問に答えるため、因果構造・熱力学・反実仮想検証の3領域を順番に修正し、読者が改善内容を素早く把握できるよう整理した。
本プロジェクトは、この批判を全面的に受け入れ、以下の3つの主要な論理的修正を行う。
</p>
</section>

<section class="section" id="causal-structure">
<h2 class="section-title">2. Causal Structure Preservation vs. Digital Emulation</h2>
<h3>2.1 The Unfolding Argument & Hardware Limitations</h3>
<p>
IIT 4.0が要求する「内因的実在（Intrinsic Existence）」は、フィードフォワード構造に展開可能なフォン・ノイマン型アーキテクチャでは原理的に満たせない可能性がある（Unfolding Argument）。
これに対し、本プロジェクトは以下の立場へと修正する。
</p>
<ul>
<li><strong>Emulation as a Map, not the Territory:</strong> 現在のCPU上での実装は、あくまで因果構造の「記述（Description）」であり、物理的な「実演（Instiation）」ではないことを明記する。</li>
<li><strong>Bridging Constraints:</strong> 将来的なニューロモルフィック実装までの過渡期として、<code>OnlineActiveInference</code> クラスに「Markov Blanket 帯域幅・遅延制約」を導入し、生物学的相互作用の物理的限界をシミュレート上の制約として課す。</li>
</ul>
</section>

<section class="section" id="thermodynamics">
<h2 class="section-title">3. Refining Thermodynamic Grounding</h2>
<h3>3.1 Beyond Landauer's Limit</h3>
<p>
従来のTCC実装は、ビット消去に伴う論理的不可逆性（Landauerの原理）のみを考慮していたが、これは脳のエネルギー消費の氷山の一角に過ぎない。
生物学的脳は非平衡開放系であり、構造維持（静止膜電位の維持等）のために常に自由エネルギーを散逸させている。
</p>
<h3>3.2 Implementation Changes</h3>
<p>
<code>mind-upload/03_causal_modeling.py</code> を修正し、以下の2層のコストモデルを導入した。
</p>
<ol>
<li><strong>Informational Cost:</strong> 信念更新（Bayesian Belief Update）に伴うKL情報量に基づくコスト。</li>
<li><strong>Structural/Metabolic Cost:</strong> システムが散逸構造として存続するためのベースラインコスト（Metabolic Overhead）。</li>
</ol>
<p>
これにより、意識システムが「何もしなくてもエネルギーを消費する」という生物学的リアリティをモデルに組み込んだ。
</p>
</section>

<section class="section" id="scm-identifiability">
<h2 class="section-title">4. Mathematical Rigor in Counterfactual Equivalence</h2>
<h3>4.1 The Identifiability Problem</h3>
<p>
観測データのみから構造的因果モデル（SCM）を一意に特定することは不可能である（Markov Equivalence Class）。この状態で <code>do-calculus</code> を適用しても、誤った反実仮想を導くリスクがある。
</p>
<h3>4.2 Perturbational Complexity as a Constraint</h3>
<p>
この問題に対し、<strong>「摂動複雑性（Perturbational Complexity）」</strong>をSCM探索の制約条件として導入する。
<code>calculate_virtual_pci</code> メソッドを実装し、仮想的な摂動に対する応答の複雑性が生物学的範囲（PCI ~ 0.5-0.7）に収まるモデルのみを「識別可能」として採用するプロセスを定義した。
これは、Laukkonen et al. (2025) の反実仮想的等価性を検証するための必須前処理となる。
</p>
</section>

<section class="section" id="multi-model-inference">
<h2 class="section-title">5. Shift to Multi-Model Inference</h2>
<p>
Cogitate Consortium (2025) の結果を受け、IITとGNWTの「統合」を目指す従来の方針を撤回し、<strong>「マルチモデル推論（Multi-Model Inference）」</strong>へ移行する。
</p>
<ul>
<li>特定の理論を教条的に信奉するのではなく、各理論（IIT, GNWT, FEP）を「モデル」として扱い、観測データに対するそれぞれのモデル証拠（Model Evidence / Marginal Likelihood）を計算する。</li>
<li><code>calculate_model_evidence</code> メソッドを追加し、状況に応じて最も説明力の高い理論を動的に参照するフレームワークを構築した。</li>
</ul>
</section>

<section class="section" id="conclusion">
<h2 class="section-title">6. Conclusion</h2>
<p>
Issue #61による指摘は、mind-uploadプロジェクトを「SF的思考実験」から「検証可能な計算論的神経科学」へと引き上げるための重要な契機となった。
修正されたコードベースと理論的枠組みは、意識のハード・プロブレムに対するより謙虚かつ厳密なアプローチを体現している。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>On this page</h4>
<ul>
<li><a href="#introduction">1. Introduction</a></li>
<li><a href="#causal-structure">2. Causal Structure</a></li>
<li><a href="#thermodynamics">3. Thermodynamic Grounding</a></li>
<li><a href="#scm-identifiability">4. SCM Identifiability</a></li>
<li><a href="#multi-model-inference">5. Multi-Model Inference</a></li>
<li><a href="#conclusion">6. Conclusion</a></li>
</ul>
</div>
</aside>
</main>
