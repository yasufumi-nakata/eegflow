---
layout: default
title: "技術提案書：物理的不可逆性・反実仮想的等価性・IIT計算量問題への対応"
description: "WBEフレームワークにおける熱力学・因果・IIT 4.0のギャップを埋めるための設計指針"
article_type: "Technical Proposal"
subtitle: "Issue #58: Thermodynamic and Causal Consistency"
author: "eegflow Project Contributor"
last_updated: "2026-02-01"
note: "Proposal (Draft)"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Abstract</h2>
<p>
本提案書は、EEGFlowのWBE実現フレームワークに対して指摘された3点の重大な不整合
（物理的不可逆性の軽視、反実仮想的等価性の定義不全、IIT 4.0の計算量問題）を体系的に整理し、
工学的に検証可能な設計指針と実装ロードマップを提示する。
</p>
</div>

<section class="section" id="thermo">
<h2 class="section-title">1. 物理的不可逆性：論理的コストから散逸構造へ</h2>
<p>
Landauer限界に基づく情報消去コストは、<strong>論理的不可逆性</strong>の下限であり、
生物学的脳が持つ<strong>非平衡定常状態（NESS）</strong>としての物理的散逸を直接保証しない。
デジタル基盤でこれを代替するには、計算の有無に関わらず、
「存在維持」に必要な散逸を明示的にモデル化する必要がある。
</p>
<ul>
<li><strong>Virtual Dissipation Protocol:</strong> 計算が停止してもゼロにならない「基底散逸」を定義する。</li>
<li><strong>Entropy Production Rate (EPR):</strong> 時間反転対称性の破れを定量化し、EPR &gt; 0 を必須制約にする。</li>
<li><strong>Metabolic Flux Proxy:</strong> 代謝的オーバーヘッド（構造維持コスト）をモデルに組み込む。</li>
</ul>
<p>
これにより、論理的な更新コスト（KL情報量）に依存しない
「散逸構造としての意識」の最小要件を定義する。
</p>
</section>

<section class="section" id="counterfactual">
<h2 class="section-title">2. 反実仮想的等価性：識別可能性の壁を越える</h2>
<p>
反実仮想（Level 3）は、観測データから一意に同定できない。
EEGFlowが掲げる「反実仮想的等価性」は、
<strong>構造方程式の同定可能性</strong>と<strong>介入設計</strong>をセットで要求する必要がある。
</p>
<ul>
<li><strong>最小分岐セット（Minimum Branching Set）:</strong> 反実仮想で分岐する最小の因果構造を定義する。</li>
<li><strong>Intervention-First:</strong> 受動観測ではなく、介入（do演算）を前提とした検証設計に切り替える。</li>
<li><strong>Identifiability Constraints:</strong> 因果モデルの関数形・ノイズ構造を限定し、同定可能な等価類を縮小する。</li>
</ul>
<p>
この枠組みでは、
「観測一致」ではなく<strong>介入に対する分岐構造の一致</strong>が主要な検証指標となる。
</p>
</section>

<section class="section" id="iit">
<h2 class="section-title">3. IIT 4.0 計算量問題：近似と境界条件の設計</h2>
<p>
IIT 4.0の厳密な$\Phi$計算は指数関数的であり、
全脳規模での実行は現実的ではない。
そこで、以下の「検証可能な近似指標」を採用する。
</p>
<ul>
<li><strong>Subsystem Φ:</strong> 小規模な部分系に限定した$\Phi$推定。</li>
<li><strong>Upper/Lower Bounds:</strong> 有効情報量や因果影響指標を用いた上下界評価。</li>
<li><strong>ΦID / Causal Structure Preservation:</strong> 完全計算の代替として因果構造の保存を評価する。</li>
<li><strong>Proxy Metrics:</strong> PCI/PCI-ST等の摂動複雑性指標と整合するかを確認する。</li>
</ul>
<p>
IITを「指標」ではなく「制約条件」として扱い、
実装可能な範囲で検証可能性を最大化する。
</p>
</section>

<section class="section" id="implementation">
<h2 class="section-title">4. 実装への影響</h2>
<ol>
<li><strong>03_causal_modeling.py:</strong> EPR/Metabolic Fluxを明示し、散逸制約を検証ループに組み込む。</li>
<li><strong>評価スイート:</strong> 最小分岐セットに基づく介入タスクを導入する。</li>
<li><strong>ロードマップ:</strong> IITの完全計算ではなく、部分系評価＋構造保存指標を標準化する。</li>
</ol>
</section>

<section class="section" id="references">
<h2 class="section-title">5. 参考文献</h2>
<ol>
<li>Landauer, R. (1961). Irreversibility and Heat Generation in the Computing Process.</li>
<li>Wolpert, D. H. (2019). The thermodynamics of computation.</li>
<li>Laukkonen, R. E., Friston, K., & Chandaria, S. (2025). A beautiful loop.</li>
<li>Pearl, J. (2000). <i>Causality: Models, Reasoning, and Inference</i>.</li>
<li>Albantakis, L., et al. (2023). Integrated information theory (IIT) 4.0.</li>
</ol>
</section>

</article>
</main>
