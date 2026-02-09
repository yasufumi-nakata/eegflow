---
layout: default
title: "貢献ガイド"
description: "Mind-Uploadプロジェクトへの参加方法と、Issue対応状況（根拠リンク付き）"
article_type: Guide
subtitle: "Join the Research Community + Issue Tracker"
author: Mind Uploading Research Project
last_updated: "2026-02-10"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<!-- Intro -->
<div class="abstract-box">
<h2>Welcome</h2>
<p>
Mind-Uploadは、マインドアップロードを検証可能な研究へ進めるオープンコミュニティです。分野や経験を問わず、文章改善や用語整理、誤解の指摘など再現性向上に直結する作業からすぐに参加いただけます。
</p>
</div>

<div class="key-points">
<h4>はじめての人へ</h4>
<ul>
<li><strong>迷ったら：</strong><a href="index.html">Start</a> → <a href="verification.html">Verification</a> → <a href="tech_roadmap.html#definition">前進の定義</a></li>
<li><strong>用語で詰まったら：</strong><a href="glossary.html">Glossary</a> と <a href="faq.html">FAQ</a></li>
<li><strong>最初に価値が出やすい貢献：</strong>「達成条件」と「反証条件」が書けるIssue</li>
</ul>
</div>

<!-- Contribution Methods -->
<section class="section">
<h2 class="section-title">How to Contribute</h2>

<div class="stage-list">
<div class="stage-item">
<div class="stage-number">01</div>
<div class="stage-body">
<h4>Issueを立てる (Discussion)</h4>
<p>新しいアイデアの提案、バグの報告、あるいは理論に関する議論は、すべて GitHub Issues から始まります。</p>
<div class="tag-list">
<span class="tag">Bug Report</span>
<span class="tag">Feature Request</span>
<span class="tag">Question</span>
</div>
</div>
</div>

<div class="stage-item">
<div class="stage-number">02</div>
<div class="stage-body">
<h4>Pull Requestを送る (Implementation)</h4>
<p>コードの修正やドキュメントの改善は Pull Request を通じて受け付けています。フォークしてブランチを作成し、変更を提案してください。</p>
</div>
</div>
</div>

<div class="cta-box">
<h4>Start Contributing</h4>
<p>GitHub Issue を作成して、議論に参加しましょう。</p>
<a href="https://github.com/yasufumi-nakata/mind-upload/issues" target="_blank">Open an Issue</a>
</div>
</section>

<!-- Resolved Issues -->
<section class="section">
<h2 class="section-title">Resolved Milestones</h2>
<p>コミュニティの貢献により解決された主要な課題です。</p>

<div class="key-points">
<h4>Completed Tasks</h4>
<ul>
<li><strong>Issue #10:</strong> MUとLLMシミュレーションの判別基準（予測不可能性・自己更新性・因果反応性）の3軸ベンチマーク確立</li>
<li><strong>Issue #12:</strong> Boundary Problem に対するグリア・代謝指標を含むハイブリッド計測プロトコルの策定</li>
<li><strong>Issue #34:</strong> M8品質管理 (QC) メトリクスのJSONログ出力機能の実装</li>
<li><strong>Issue #43:</strong> R2経験的ベイズによるソース推定と不確実性定量化（信頼区間）の実装</li>
</ul>
</div>
</section>

<section class="section" id="technical-issue-tracker">
<h2 class="section-title">Technical Issue Tracker（本文統合済み）</h2>
<p>
以下は、Technical Proposal 系 Issue の対応状況です。判断根拠は、各 Proposal の該当節へ直接リンクしています。
</p>

<table class="data-table">
<thead>
<tr>
<th>Issue</th>
<th>対応内容（要約）</th>
<th>状態</th>
<th>根拠リンク</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>#46</strong></td>
<td>計測QA、同期補正、アーティファクト除去、BIDS/Motion-BIDSの統合方針を整理</td>
<td>提案化済み</td>
<td><a href="technical_proposal_46.html#qa">#qa</a> / <a href="technical_proposal_46.html#sync">#sync</a> / <a href="technical_proposal_46.html#bids">#bids</a></td>
</tr>
<tr>
<td><strong>#47</strong></td>
<td>BIDS標準化、ASR/ZapLine、wPLI/STE、LSL同期の実装方針を拡張</td>
<td>提案受理（文書）</td>
<td><a href="technical_proposal_47.html#bids">#bids</a> / <a href="technical_proposal_47.html#preprocessing">#preprocessing</a> / <a href="technical_proposal_47.html#connectivity">#connectivity</a></td>
</tr>
<tr>
<td><strong>#48</strong></td>
<td>OPM-MEG、転移学習、Team Flow因果、IIT実装の拡張案を提出</td>
<td>審査中提案</td>
<td><a href="technical_proposal_48.html#measurement">#measurement</a> / <a href="technical_proposal_48.html#teamflow">#teamflow</a> / <a href="technical_proposal_48.html#iit-implementation">#iit-implementation</a></td>
</tr>
<tr>
<td><strong>#56</strong></td>
<td>反実仮想の識別不能性に対して PCI と do-calculus を導入する検証設計へ変更</td>
<td>提案化済み</td>
<td><a href="technical_proposal_56.html#problem-statement">#problem-statement</a> / <a href="technical_proposal_56.html#proposal">#proposal</a></td>
</tr>
<tr>
<td><strong>#58</strong></td>
<td>NESS散逸・因果識別可能性・IIT近似計算の3課題に対する設計方針を明文化</td>
<td>提案化済み</td>
<td><a href="technical_proposal_58.html#thermo">#thermo</a> / <a href="technical_proposal_58.html#counterfactual">#counterfactual</a> / <a href="technical_proposal_58.html#iit">#iit</a></td>
</tr>
<tr>
<td><strong>#61</strong></td>
<td>Unfolding論点・熱力学コスト2層化・SCM厳密化・多モデル推論への修正を提示</td>
<td>実装方針反映（文書）</td>
<td><a href="technical_proposal_61.html#causal-structure">#causal-structure</a> / <a href="technical_proposal_61.html#thermodynamics">#thermodynamics</a> / <a href="technical_proposal_61.html#multi-model-inference">#multi-model-inference</a></td>
</tr>
<tr>
<td><strong>#62</strong></td>
<td>#58批判に対し、同値類警告とIIT近似の実装計画を追加補強</td>
<td>実装計画化（文書）</td>
<td><a href="technical_proposal_62.html#thermodynamics">#thermodynamics</a> / <a href="technical_proposal_62.html#identifiability">#identifiability</a> / <a href="technical_proposal_62.html#complexity">#complexity</a></td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>運用ルール</strong>
<p>
このトラッカーは「サイト内で確認可能な証跡」を基準に更新します。外部実装（実験・法務・機材調達等）は外部依存として分離し、本ページでは主張しません。
</p>
</div>

<div class="cta-box">
<h4>統合本文</h4>
<p>Technical Proposal 全体の統合本文は `proposals.html` に集約しています。</p>
<a href="proposals.html">統合本文を見る →</a>
</div>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>Resources</h4>
<ul>
<li><a href="https://github.com/yasufumi-nakata/mind-upload" target="_blank">GitHub Repository →</a></li>
<li><a href="idea.html">Theoretical Framework →</a></li>
<li><a href="tech_roadmap.html">Technical Roadmap →</a></li>
</ul>
</div>

<div class="note-box">
<strong>Code of Conduct</strong>
<p>
すべての参加者が快適に議論できるよう、互いに敬意を持って接してください。科学的な批判は歓迎されますが、攻撃的な言動は容認されません。
</p>
</div>

</aside>
</main>
