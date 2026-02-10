---
layout: default
title: "技術提案（統合本文）"
description: "Issue #46/#47/#48/#56/#58/#61/#62 に対応する Technical Proposal を1ページ本文に統合した根拠付きサマリー。"
article_type: Index
subtitle: "Issue対応・実装方針・根拠リンクを1ページで追跡"
author: Mind Uploading Research Project
last_updated: "2026-02-10"
note: "Integrated Compendium"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Purpose</h2>
<p>
このページは、Technical Proposal 群（Issue #46/#47/#48/#56/#58/#61/#62）を「一覧」ではなく<strong>本文として統合</strong>したページです。
各提案の主張、対応状況、実装影響、根拠節へのリンクを1か所にまとめ、検証と更新を容易にします。
</p>
</div>

<section class="section" id="reading-guide">
<h2 class="section-title">読み方（根拠ベース）</h2>
<div class="key-points">
<h4>Rule</h4>
<ul>
<li><strong>要約だけで判断しない：</strong> 各項目の「根拠」リンクから原文節に戻って確認してください。</li>
<li><strong>主張レベルを分離：</strong> 「提案」「実装済み」「外部依存」を混同せずに読む運用にしています。</li>
<li><strong>更新点を追う：</strong> `last_updated` が新しい順に、変更理由を `issue.html` でも確認できます。</li>
</ul>
</div>
</section>

<section class="section" id="issue-matrix">
<h2 class="section-title">Issue対応マトリクス（統合版）</h2>
<table class="data-table">
<thead>
<tr>
<th>Issue</th>
<th>状態</th>
<th>主眼</th>
<th>根拠（原文節）</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>#46</strong></td>
<td>提案公開</td>
<td>計測QA・同期・モーション除去・BIDS/Motion-BIDS</td>
<td><a href="technical_proposal_46.html#qa">#qa</a> / <a href="technical_proposal_46.html#sync">#sync</a> / <a href="technical_proposal_46.html#bids">#bids</a></td>
</tr>
<tr>
<td><strong>#47</strong></td>
<td>提案受理</td>
<td>BIDS標準化、ASR/ZapLine、wPLI/STE、LSL同期</td>
<td><a href="technical_proposal_47.html#bids">#bids</a> / <a href="technical_proposal_47.html#preprocessing">#preprocessing</a> / <a href="technical_proposal_47.html#connectivity">#connectivity</a> / <a href="technical_proposal_47.html#multimodal">#multimodal</a></td>
</tr>
<tr>
<td><strong>#48</strong></td>
<td>審査中提案</td>
<td>OPM-MEG、転移学習、Team Flow因果、IIT実装拡張</td>
<td><a href="technical_proposal_48.html#measurement">#measurement</a> / <a href="technical_proposal_48.html#teamflow">#teamflow</a> / <a href="technical_proposal_48.html#iit-implementation">#iit-implementation</a></td>
</tr>
<tr>
<td><strong>#56</strong></td>
<td>提案公開</td>
<td>反実仮想の識別不能性に対する介入設計（PCI + do演算）</td>
<td><a href="technical_proposal_56.html#problem-statement">#problem-statement</a> / <a href="technical_proposal_56.html#proposal">#proposal</a></td>
</tr>
<tr>
<td><strong>#58</strong></td>
<td>提案公開</td>
<td>NESS散逸・反実仮想識別可能性・IIT近似計算</td>
<td><a href="technical_proposal_58.html#thermo">#thermo</a> / <a href="technical_proposal_58.html#counterfactual">#counterfactual</a> / <a href="technical_proposal_58.html#iit">#iit</a></td>
</tr>
<tr>
<td><strong>#61</strong></td>
<td>実装方針反映（提案文書）</td>
<td>Unfolding論点、熱力学コスト2層化、SCM厳密化、多モデル推論</td>
<td><a href="technical_proposal_61.html#causal-structure">#causal-structure</a> / <a href="technical_proposal_61.html#thermodynamics">#thermodynamics</a> / <a href="technical_proposal_61.html#scm-identifiability">#scm-identifiability</a> / <a href="technical_proposal_61.html#multi-model-inference">#multi-model-inference</a></td>
</tr>
<tr>
<td><strong>#62</strong></td>
<td>#58応答として実装計画化</td>
<td>NESS・同値類警告・IIT近似（ヒューリスティクス）</td>
<td><a href="technical_proposal_62.html#thermodynamics">#thermodynamics</a> / <a href="technical_proposal_62.html#identifiability">#identifiability</a> / <a href="technical_proposal_62.html#complexity">#complexity</a></td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="integrated-streams">
<h2 class="section-title">統合本文（技術ストリーム別）</h2>

<div class="stage-list">
<div class="stage-item">
<div class="stage-number">A</div>
<div class="stage-body">
<h4>計測品質・同期・標準化ストリーム</h4>
<p>
計測品質の定量化・同期誤差（遅延/ジッタ/ドリフト）補正・BIDS準拠を再現可能性の最低条件として固定し、Issue #46/#47 共通の計測品質・同期・標準化ストリームとして扱います。
</p>
<div class="tag-list">
<span class="tag">QA</span><span class="tag">LSL</span><span class="tag">BIDS</span><span class="tag">Motion-BIDS</span>
</div>
<p><strong>根拠:</strong> <a href="technical_proposal_46.html#qa">#46: 計測QA</a> / <a href="technical_proposal_46.html#sync">#46: 同期補正</a> / <a href="technical_proposal_47.html#bids">#47: BIDS標準化</a></p>
</div>
</div>

<div class="stage-item">
<div class="stage-number">B</div>
<div class="stage-body">
<h4>信号前処理・接続性解析ストリーム</h4>
<p>
ASR/ZapLine 系の適応的デノイジングと、体積伝導に頑健な接続性指標（wPLI/STE）を組み合わせ、比較可能な解析パイプラインを構成します。
</p>
<div class="tag-list">
<span class="tag">ASR</span><span class="tag">ZapLine-plus</span><span class="tag">wPLI</span><span class="tag">STE</span>
</div>
<p><strong>根拠:</strong> <a href="technical_proposal_47.html#preprocessing">#47: 前処理</a> / <a href="technical_proposal_47.html#connectivity">#47: 接続性</a></p>
</div>
</div>

<div class="stage-item">
<div class="stage-number">C</div>
<div class="stage-body">
<h4>WBE同一性検証（因果介入）ストリーム</h4>
<p>
Issue #56/#58/#61/#62 の統合論点です。観測一致だけでなく、介入に対する分岐構造一致を検証し、識別可能性の限界を明示します。
</p>
<div class="tag-list">
<span class="tag">Counterfactual</span><span class="tag">do-calculus</span><span class="tag">SCM</span><span class="tag">Identifiability</span>
</div>
<p><strong>根拠:</strong> <a href="technical_proposal_56.html#proposal">#56: 介入提案</a> / <a href="technical_proposal_58.html#counterfactual">#58: 識別可能性</a> / <a href="technical_proposal_61.html#scm-identifiability">#61: 厳密化</a> / <a href="technical_proposal_62.html#identifiability">#62: 同値類警告</a></p>
</div>
</div>

<div class="stage-item">
<div class="stage-number">D</div>
<div class="stage-body">
<h4>熱力学・計算量制約ストリーム</h4>
<p>
「論理コストだけで十分」という誤解を避け、非平衡散逸（NESS）と IIT 近似計算の制約を実装要件として分離します。
</p>
<div class="tag-list">
<span class="tag">NESS</span><span class="tag">EPR</span><span class="tag">Metabolic Flux</span><span class="tag">IIT Approximation</span>
</div>
<p><strong>根拠:</strong> <a href="technical_proposal_58.html#thermo">#58: 散逸制約</a> / <a href="technical_proposal_61.html#thermodynamics">#61: 2層コスト</a> / <a href="technical_proposal_62.html#complexity">#62: 計算量対応</a></p>
</div>
</div>
</div>
</section>

<section class="section" id="full-index">
<h2 class="section-title">原本（全文）インデックス</h2>
<table class="data-table">
<thead>
<tr>
<th>提案</th>
<th>Issue</th>
<th>更新日</th>
<th>リンク</th>
</tr>
</thead>
<tbody>
<tr><td>計測品質・同期・BIDS統合強化</td><td>#46</td><td>2026-02-01</td><td><a href="technical_proposal_46.html">Open</a></td></tr>
<tr><td>標準化と計算論的拡張</td><td>#47</td><td>2026-01-25</td><td><a href="technical_proposal_47.html">Open</a></td></tr>
<tr><td>神経工学的・計算論的枠組み拡張</td><td>#48</td><td>2026-01-25</td><td><a href="technical_proposal_48.html">Open</a></td></tr>
<tr><td>識別可能性と因果介入</td><td>#56</td><td>2026-01-30</td><td><a href="technical_proposal_56.html">Open</a></td></tr>
<tr><td>熱力学・因果整合性</td><td>#58</td><td>2026-02-01</td><td><a href="technical_proposal_58.html">Open</a></td></tr>
<tr><td>因果モデリング論理ギャップ対応</td><td>#61</td><td>2026-02-01</td><td><a href="technical_proposal_61.html">Open</a></td></tr>
<tr><td>#58批判への補強提案</td><td>#62（#58応答）</td><td>2026-02-01</td><td><a href="technical_proposal_62.html">Open</a></td></tr>
</tbody>
</table>

<div class="cta-box">
<h4>Issue対応の確認</h4>
<p>Issueごとの対応状況は `issue.html` に集約しています。</p>
<a href="issue.html">Issue対応ページを見る →</a>
</div>
</section>

<section class="section" id="evidence-gaps">
<h2 class="section-title">エビデンスギャップ（未解決課題）</h2>
<p>
各提案ストリームについて、文献的裏付けが不足している領域を明示します。
</p>
<div class="key-points">
<h4>Stream A: 計測品質</h4>
<ul>
<li><strong>ASR のパラメータ選択根拠：</strong>ASR（Artifact Subspace Reconstruction）の閾値設定は経験的であり、WBE用途での最適パラメータの理論的根拠は未確立。</li>
<li><strong>OPM-MEGとの統合：</strong>OPM-MEG（Optically Pumped Magnetometer）は動き耐性を改善するが、EEGとのマルチモーダル統合プロトコルは標準化されていない（Boto et al., 2018）。</li>
</ul>
</div>
<div class="key-points">
<h4>Stream C: WBE同一性検証</h4>
<ul>
<li><strong>do-calculusの実装可能性：</strong>Pearl のdo-calculusは理論的に強力だが、神経データに対する観測変数の選択と介入変数の特定が実験設計上の最大のボトルネック。</li>
<li><strong>SCMのサイクル問題：</strong>脳の再帰的接続ではDAG仮定が成り立たず、cyclic SCM（動的因果モデルとの接続）の理論的整備が必要。</li>
</ul>
</div>
<div class="key-points">
<h4>Stream D: 熱力学</h4>
<ul>
<li><strong>NESS測定の実現性：</strong>非平衡定常状態のエントロピー生成速度を神経系で直接測定する手法は確立されていない。代理指標（代謝率、ATP消費量等）との対応関係の検証が必要。</li>
</ul>
</div>
</section>

<section class="section" id="references">
<h2 class="section-title">参考文献（横断）</h2>
<ol>
<li>Chang, C.-Y., et al. (2018). ASR evaluation. <a href="https://doi.org/10.1109/EMBC.2018.8512547" target="_blank">doi:10.1109/EMBC.2018.8512547</a></li>
<li>de Cheveigne, A. (2020). ZapLine. <a href="https://doi.org/10.1016/j.neuroimage.2019.116356" target="_blank">doi:10.1016/j.neuroimage.2019.116356</a></li>
<li>Vinck, M., et al. (2011). wPLI. <a href="https://doi.org/10.1016/j.neuroimage.2011.01.055" target="_blank">doi:10.1016/j.neuroimage.2011.01.055</a></li>
<li>Staniek, M., &amp; Lehnertz, K. (2008). Symbolic Transfer Entropy. <a href="https://doi.org/10.1103/PhysRevLett.100.158101" target="_blank">doi:10.1103/PhysRevLett.100.158101</a></li>
<li>Correa, J. D., Lee, S., &amp; Bareinboim, E. (2021). Nested Counterfactual Identification. <a href="https://arxiv.org/abs/2107.03190" target="_blank">arXiv:2107.03190</a></li>
<li>Seifert, U. (2012). Stochastic thermodynamics. <a href="https://doi.org/10.1088/0034-4885/75/12/126001" target="_blank">doi:10.1088/0034-4885/75/12/126001</a></li>
<li>Kitazono, J., Kanai, R., &amp; Oizumi, M. (2018). Efficient MIP search in IIT. <a href="https://doi.org/10.3390/e20030173" target="_blank">doi:10.3390/e20030173</a></li>
<li>Kothe, C., et al. (2025). Lab Streaming Layer. <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">doi:10.1162/IMAG.a.136</a></li>
<li>Boto, E., et al. (2018). Moving magnetoencephalography towards real-world applications with wearable OPM-MEG. <a href="https://doi.org/10.1038/nature26147" target="_blank">doi:10.1038/nature26147</a></li>
<li>Pearl, J. (2009). <em>Causality: Models, Reasoning, and Inference</em> (2nd ed.). Cambridge University Press.</li>
<li>Friston, K. J., Harrison, L., &amp; Penny, W. (2003). Dynamic causal modelling. <a href="https://doi.org/10.1016/S1053-8119(03)00202-7" target="_blank">doi:10.1016/S1053-8119(03)00202-7</a></li>
</ol>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>Related</h4>
<ul>
<li><a href="verification.html">検証基盤（Verification）→</a></li>
<li><a href="tech_roadmap.html">技術ロードマップ（学習）→</a></li>
<li><a href="issue.html">Issue対応状況（集約）→</a></li>
<li><a href="index.html">Start（トップ）→</a></li>
</ul>
</div>

<div class="note-box">
<strong>Rule of Thumb</strong>
<p>
提案は「主張」ではなく、<strong>検証条件</strong>・<strong>反証条件</strong>・<strong>根拠リンク</strong>の3点セットで管理します。
</p>
</div>

</aside>
</main>
