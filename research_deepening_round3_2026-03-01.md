---
layout: default
title: "Research Deepening Round 3 (2026-03-01): U4/U7"
description: "U4（因果同値）とU7（マルチモーダル整合）のリサーチクエスチョン深掘り。"
article_type: "Evidence Addendum"
subtitle: "一次情報の追加と、実行可能な次作業の固定"
author: Mind Uploading Research Project
last_updated: "2026-03-01"
note: "Round 3 (U4/U7)"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Round 3 の狙い</h2>
<p>
U4 と U7 は、WBEの「検証可能性」に直結する領域です。
この追補では、各問いに対して一次情報を追加し、
今セッションで実行可能な変更と外部依存タスクを分離して明示します。
</p>
</div>

<section class="section" id="u4">
<h2 class="section-title">U4: 因果同値（Round 3）</h2>
<table class="data-table">
<thead><tr><th>RQ</th><th>今回の深掘り（平易）</th><th>追加一次情報</th><th>今回実行する変更</th><th>外部依存タスク</th></tr></thead>
<tbody>
<tr>
<td>1</td>
<td>相関から因果へ進むには、構造仮定と識別条件を明示しないと、同じデータから別結論が出ます。</td>
<td>
<a href="https://doi.org/10.1038/s41583-024-00881-3" target="_blank">Structural constraints in effective connectivity analyses (Nat Rev Neurosci, 2025)</a><br>
<a href="https://doi.org/10.1016/j.neuroimage.2024.120954" target="_blank">Fast dynamic causal modeling regression for fMRI (NeuroImage, 2024)</a>
</td>
<td>U4に「識別条件を明示しない主張は採択しない」監査チェックを追加します。</td>
<td>担当: 実験設計チーム。前提: 介入設計レビュー会の合意。完了条件: 因果主張テンプレの承認。</td>
</tr>
<tr>
<td>2</td>
<td>最小因果主張は、実際に介入して差分が再現されること（反復可能）が必要です。</td>
<td>
<a href="https://doi.org/10.1109/TMI.2024.3381670" target="_blank">MCAN: Causal adversarial networks for dynamic effective connectivity (IEEE TMI, 2024)</a><br>
<a href="https://doi.org/10.1001/jamanetworkopen.2024.9220" target="_blank">Personalized hippocampal network-targeted stimulation trial (JAMA Network Open, 2024)</a>
</td>
<td>U4 RQ2に「介入効果の反復再現（別セッション）」を必須欄として追加します。</td>
<td>担当: 臨床/実験チーム。前提: 介入プロトコル承認。完了条件: 反復介入レポート公開。</td>
</tr>
<tr>
<td>3</td>
<td>DCMやactive inferenceは使えますが、反事実評価へ接続する設計を最初に決めないと説明止まりになります。</td>
<td>
<a href="https://pubmed.ncbi.nlm.nih.gov/38826672/" target="_blank">Dynamic causal modeling in multisensory speech perception (PMID:38826672, 2024)</a><br>
<a href="https://doi.org/10.1109/TNSRE.2021.3123964" target="_blank">Systematic review of DCM in psychiatric disorders (IEEE TNSRE)</a>
</td>
<td>U4 RQ3に「反事実テスト項目（do介入の期待差）」の欄を追加します。</td>
<td>担当: 解析WG。前提: 反事実課題設計。完了条件: 期待差と実測差の比較結果公開。</td>
</tr>
<tr>
<td>4</td>
<td>失敗条件（falsification）を宣言しない因果同値は、運用上は検証不能です。</td>
<td>
<a href="https://doi.org/10.1016/j.neuroimage.2024.120954" target="_blank">Fast DCM regression with explicit model assumptions (NeuroImage, 2024)</a><br>
<a href="https://doi.org/10.1038/s41583-024-00881-3" target="_blank">Effective connectivity pitfalls and constraints (Nat Rev Neurosci, 2025)</a>
</td>
<td>U4 RQ4に「失敗宣言閾値（例: 因果辺再現率下限）」を数値で入れる欄を追加します。</td>
<td>担当: 検証WG。前提: 失敗時対応フロー承認。完了条件: 失敗ケース公開運用開始。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="u7">
<h2 class="section-title">U7: マルチモーダル整合（Round 3）</h2>
<table class="data-table">
<thead><tr><th>RQ</th><th>今回の深掘り（平易）</th><th>追加一次情報</th><th>今回実行する変更</th><th>外部依存タスク</th></tr></thead>
<tbody>
<tr>
<td>1</td>
<td>BIDSの必須項目は拡張されていますが、WBE用途で「必須」にする範囲はまだ決め切れていません。</td>
<td>
<a href="https://bids-specification.readthedocs.io/en/stable/" target="_blank">BIDS Specification 1.10.1</a><br>
<a href="https://zenodo.org/records/18201723" target="_blank">BEP036 (HED and events metadata extension draft, 2025)</a>
</td>
<td>U7にBIDS必須メタデータの最小セット（同期/QC/刺激ログ）表を追加します。</td>
<td>担当: データ標準化WG。前提: BIDS運用ルール合意。完了条件: validator通過率の定期公開。</td>
</tr>
<tr>
<td>2</td>
<td>同期誤差は「ある/ない」ではなく、アルゴリズムで測って比較する段階です。</td>
<td>
<a href="https://doi.org/10.1016/j.cmpb.2024.108298" target="_blank">Haemosync: synchronisation algorithm for multimodal hemodynamic signals (2024)</a><br>
<a href="https://pubmed.ncbi.nlm.nih.gov/34214093/" target="_blank">Simultaneous EEG-fMRI quality/safety study (PMID:34214093)</a>
</td>
<td>U7 RQ2に「時刻ずれ(ms)」「ジッタ分散」の自動計算欄を追加します。</td>
<td>担当: 計測運用チーム。前提: 同期基準信号の統一。完了条件: セッション間比較レポート。</td>
</tr>
<tr>
<td>3</td>
<td>アーチファクト除去は手法差で結果が動くため、設定監査が必須です。</td>
<td>
<a href="https://doi.org/10.1109/TBME.2024.3383142" target="_blank">Evaluation of EEG-fMRI artifact correction methods (IEEE TBME, 2024)</a><br>
<a href="https://arxiv.org/abs/2411.05812" target="_blank">Low-rank+sparse decomposition for simultaneous EEG-fMRI denoising (arXiv, 2024)</a>
</td>
<td>U7 RQ3に「前処理設定差分ログ」を必須監査項目として追加します。</td>
<td>担当: 解析WG。前提: 前処理テンプレ統一。完了条件: 設定差分での再現率評価公開。</td>
</tr>
<tr>
<td>4</td>
<td>アライメント失敗時は、再計測か除外かの基準を先に決めないと運用がぶれます。</td>
<td>
<a href="https://arxiv.org/abs/2311.04912" target="_blank">ezBIDS: multimodal BIDS curation and validation support (2023)</a><br>
<a href="https://doi.org/10.1038/s41597-024-03029-1" target="_blank">Multimodal single-neuron/iEEG/fMRI dataset during movie watching (Scientific Data, 2024)</a>
</td>
<td>U7 RQ4に「再計測条件」「除外条件」の二段階判定欄を追加します。</td>
<td>担当: 計測運用チーム。前提: 欠測時運用手順の承認。完了条件: 再計測/除外判定一致率の公開。</td>
</tr>
<tr>
<td>5</td>
<td>CIで前処理差分を回すなら、どの低下率で停止するかを数値で固定する必要があります。</td>
<td>
<a href="https://bids-specification.readthedocs.io/en/stable/" target="_blank">BIDS 1.10.1 (validation-oriented metadata requirements)</a><br>
<a href="https://doi.org/10.1109/TBME.2024.3383142" target="_blank">Artifact correction comparison evidence (2024)</a>
</td>
<td>U7 RQ5に「リリースブロック閾値（再現率低下%）」を設定する欄を追加します。</td>
<td>担当: CI運用チーム。前提: ベースライン実験固定。完了条件: 失敗時自動ブロック動作確認。</td>
</tr>
<tr>
<td>6</td>
<td>モダリティ欠損下でも結論が保てるかは、公開データで最小観測セットを検証する必要があります。</td>
<td>
<a href="https://doi.org/10.3389/fnrgo.2024.1411305" target="_blank">BIDS multimodal dataset with EEG+motion (Frontiers, 2024)</a><br>
<a href="https://doi.org/10.1515/revneuro-2023-0098" target="_blank">Single vs multimodal EEG/fMRI along AD continuum (2024)</a>
</td>
<td>U7 RQ6に欠損シミュレーション列（EEG欠損/fMRI欠損）を追加します。</td>
<td>担当: 解析WG。前提: 欠損実験計画。完了条件: 最小観測セットでの結論維持率公開。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="summary">
<h2 class="section-title">Round 3 要約</h2>
<ul>
<li>U4は、因果主張の識別条件と失敗条件を先に固定することが最重要です。</li>
<li>U7は、同期・前処理・欠損に対する監査項目を数値で固定する段階にあります。</li>
<li>次の continue では U8（閉ループ安定性）を同じ形式で深掘りします。</li>
</ul>
</section>

</article>
</main>
