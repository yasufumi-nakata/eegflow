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
<h4>設計完了（実装コード未公開）</h4>
<ul>
<li><strong>Issue #10:</strong> MUとLLMシミュレーションの判別基準（予測不可能性・自己更新性・因果反応性）の3軸ベンチマーク — <em>設計文書は完了。再現可能な実装コード・テストデータ・評価結果は未公開。</em></li>
<li><strong>Issue #12:</strong> Boundary Problem に対するグリア・代謝指標を含むハイブリッド計測プロトコル — <em>概念設計は完了。プロトコル詳細・必要機材リスト・パイロットデータは未整備。</em></li>
<li><strong>Issue #34:</strong> M8品質管理 (QC) メトリクスのJSONログ出力機能 — <em>スキーマ設計は完了。実装コードはリポジトリに未反映。</em></li>
<li><strong>Issue #43:</strong> R2経験的ベイズによるソース推定と不確実性定量化（信頼区間） — <em>理論的枠組みは文書化済み。<code>02_source_imaging.py</code>の実装コードは未公開。</em></li>
</ul>
</div>
<div class="note-box">
<strong>透明性に関する注記</strong>
<p>
上記のIssueは、サイト内の文書レベルでは対応が完了していますが、第三者が再現・検証できる形（実行可能コード、テストデータ、評価結果）での公開には至っていません。本プロジェクトが掲げる再現性の基準（L0: 第三者による再現可能性）を満たすためには、これらの実装の公開が必要です。
</p>
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

<!-- Verification Audit -->
<section class="section" id="verification-audit">
<h2 class="section-title">Verification Audit（180件の検証監査）</h2>
<p>
2026年2月に実施した全サイトコンテンツの体系的検証監査の結果です。4カテゴリ・180件のGitHub Issueとして登録し、サイト修正を通じて対応しています。
</p>

<table class="data-table">
<thead>
<tr>
<th>カテゴリ</th>
<th>Issue範囲</th>
<th>件数</th>
<th>対応状況</th>
<th>主な修正内容</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>LIT（文献検証）</strong></td>
<td>#71–#110</td>
<td>40件</td>
<td>文書修正済み</td>
<td>DOI検証、重複参照の除去（ref-68/69/72/75）、FlyWire 2024追加、未検証引用の明示</td>
</tr>
<tr>
<td><strong>THEO（理論的ギャップ）</strong></td>
<td>#111–#145</td>
<td>35件</td>
<td>文書修正済み</td>
<td>ハードプロブレムの立場明示、Unfolding Argument対応、FEP批判の認知、哲学的前提の表化</td>
</tr>
<tr>
<td><strong>IMPL（実装ギャップ）</strong></td>
<td>#146–#195</td>
<td>50件</td>
<td>文書修正済み</td>
<td>実装ステータス透明性報告、L0未達成の明示、エビデンスギャップ分析、Deployment節追加</td>
</tr>
<tr>
<td><strong>METH（方法論・最新研究）</strong></td>
<td>#196–#250</td>
<td>55件</td>
<td>文書修正済み</td>
<td>コネクトーム進捗更新、代替アプローチ比較表、倫理FAQ追加、用語集拡充（13用語追加）</td>
</tr>
</tbody>
</table>

<div class="key-points">
<h4>主要な修正（サイト横断）</h4>
<ul>
<li><strong>perspective.md：</strong>重複参照4件除去、Limitations節追加、FlyWireコネクトーム更新、Chalmers 1995追加</li>
<li><strong>idea.md：</strong>Limitations and Open Questions節追加、Weber 2025にDOIリンク付与、参考文献5件追加</li>
<li><strong>verification.md：</strong>実装ステータス透明性報告表追加、科学的ギャップ分析節追加、MOABB/FAIR参照追加</li>
<li><strong>glossary.md：</strong>意識理論セクション（IIT/GNWT/FEP/PCI/マルコフブランケット等8用語）と実装基盤セクション（5用語）を追加</li>
<li><strong>faq.md：</strong>ハードプロブレム、コピー問題、Cogitate結果、倫理、他プロジェクト比較の5問を追加</li>
<li><strong>wbe_101.md：</strong>哲学的前提の比較表、代替アプローチ比較表を追加</li>
<li><strong>proposals.md：</strong>エビデンスギャップ節追加（ASR/OPM-MEG/do-calculus/NESS課題の明示）</li>
<li><strong>tech_roadmap.md：</strong>I8/I9構造バグ修正、Deployment & Governance節（D0-D3）追加</li>
</ul>
</div>

<div class="note-box">
<strong>透明性に関する注記</strong>
<p>
上記の修正はすべて「文書レベル」です。実行可能コード、テストデータ、評価結果としての公開（L0達成）は別途必要であり、本監査ではその乖離を明示することを優先しました。
</p>
</div>
</section>

<!-- Technical Critique Response -->
<section class="section" id="technical-critique">
<h2 class="section-title">Technical Critique対応（#64–#70）</h2>
<p>
2026年2月に提出された7件の技術的・科学的批判（Issues #64–#70）への対応です。共通テーマをまとめて各ファイルに反映しています。
</p>

<table class="data-table">
<thead>
<tr>
<th>テーマ</th>
<th>対応Issue</th>
<th>修正内容</th>
<th>反映先</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>IIT 4.0計算量・Unfolding Argument</strong></td>
<td>#64, #65, #68, #69</td>
<td>哲学的ゾンビリスクの明示、ニューロモルフィック必要性の強調、階層的粗視化の導入</td>
<td><a href="perspective.html#decoding-to-emulation-gap">perspective</a></td>
</tr>
<tr>
<td><strong>EEG空間解像度の限界</strong></td>
<td>#64, #66, #67, #70</td>
<td>情報理論的限界の明示（7桁ギャップ）、WBEでの現実的役割の再定義</td>
<td><a href="eeg_101.html#information-theoretic-limits">eeg_101</a></td>
</tr>
<tr>
<td><strong>反実仮想的等価性の不十分さ</strong></td>
<td>#65, #66, #69, #70</td>
<td>EI・Causal Density・STEの3指標追加、Pearlの因果梯子による評価枠組み</td>
<td><a href="perspective.html#decoding-to-emulation-gap">perspective</a> / <a href="verification.html#verification-rigor">verification</a></td>
</tr>
<tr>
<td><strong>NESS熱力学的接地</strong></td>
<td>#68</td>
<td>Landauer限界を超えるEPR要件、Fisher Informationとの結合</td>
<td><a href="perspective.html#decoding-to-emulation-gap">perspective</a></td>
</tr>
<tr>
<td><strong>DCM/ベイズ法の限界</strong></td>
<td>#64, #65, #67, #70</td>
<td>BMR・Causal Fingerprinting・適応的前処理（Riemannian Potato）の導入</td>
<td><a href="proposals.html#integrated-streams">proposals</a></td>
</tr>
<tr>
<td><strong>ESI不確実性定量化</strong></td>
<td>#67, #69, #70</td>
<td>信頼区間義務化、適応的ASR/ZapLine-plus、順問題誤差伝播</td>
<td><a href="eeg_101.html#esi-uncertainty">eeg_101</a> / <a href="verification.html#verification-rigor">verification</a></td>
</tr>
</tbody>
</table>
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
