---
layout: default
title: "Research Deepening Round 2 (2026-03-01): U0-U3"
description: "U0/U1/U3 の各リサーチクエスチョンを、一次情報でさらに深掘りした追補。"
article_type: "Evidence Addendum"
subtitle: "平易な要点・追加根拠・今すぐ実行できる内部作業"
author: Mind Uploading Research Project
last_updated: "2026-03-01"
note: "Round 2 (U0/U1/U3)"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Round 2 の狙い</h2>
<p>
この追補では、U0/U1/U3 について、
「何が新しく分かったか」を一次情報（DOI/PubMed）で追加し、
各問いに対して次に実行できる内部作業を明示します。
</p>
</div>

<section class="section" id="u0">
<h2 class="section-title">U0: 操作的同一性（Round 2）</h2>
<table class="data-table">
<thead><tr><th>RQ</th><th>今回の深掘り（平易）</th><th>追加一次情報</th><th>今回実行する変更</th><th>外部依存タスク</th></tr></thead>
<tbody>
<tr>
<td>1</td>
<td>「観測一致だけでは足りない」という方向は強いですが、介入一致をどう必要条件化するかは未合意です。</td>
<td>
<a href="https://doi.org/10.31219/osf.io/sr7cf" target="_blank">Nondestructive Mind Uploading and the Stream of Consciousness (OSF, 2023)</a><br>
<a href="https://arxiv.org/abs/2510.15745" target="_blank">State of Brain Emulation Report 2025 (arXiv, 2025)</a>
</td>
<td>U0判定テンプレに「観測一致」「介入一致」を別項目として固定する下書きを作成します。</td>
<td>担当: 法務/倫理WG。前提: 分岐時責任の原則合意。完了条件: 判定規約v1承認。</td>
</tr>
<tr>
<td>2</td>
<td>ms同期と状態表現の固定は技術側で定義できますが、同一性判定へどう重み付けするかは理論側の未解決です。</td>
<td>
<a href="https://doi.org/10.1093/acprof:oso/9780198754855.003.0013" target="_blank">Enhancement, Mind-Uploading, and Personal Identity</a><br>
<a href="https://doi.org/10.1017/9781009367059.009" target="_blank">Personal Ontology and Life after Death, Part 2</a>
</td>
<td>同期誤差を数値で残すため、U0の評価欄に「時刻ずれ(ms)」を追加します。</td>
<td>担当: 計測チーム。前提: 同期計測手順の標準化。完了条件: 監査可能な同期ログ様式確定。</td>
</tr>
<tr>
<td>3</td>
<td>閾値設計（どこから同一とみなすか）は、哲学文献は豊富でも実験設計に直結する共通規約が不足しています。</td>
<td>
<a href="https://doi.org/10.1007/s11229-024-04744-3" target="_blank">I am no abstract object (Synthese, 2024)</a><br>
<a href="https://doi.org/10.2139/ssrn.2596460" target="_blank">The Fallacy of Favoring Gradual Replacement... (SSRN)</a>
</td>
<td>U0に ROC-AUC と閾値感度を入れた最小評価シートをCSV化します。</td>
<td>担当: 評価設計WG。前提: 最低タスクセット合意。完了条件: 閾値感度分析の再現レポート。</td>
</tr>
<tr>
<td>4</td>
<td>分岐/複製での同一性は、性能評価だけでは決まらず、責任追跡IDの運用設計が不可欠です。</td>
<td>
<a href="https://doi.org/10.1017/9781009486309.002" target="_blank">The Right to Personal Identity (2026)</a><br>
<a href="https://doi.org/10.1016/j.patter.2023.100861" target="_blank">No legal personhood for AI (Patterns, 2023)</a>
</td>
<td>U0 RQ4に ID衝突率・責任追跡率を必須指標として明記します。</td>
<td>担当: 法務/ガバナンスWG。前提: ID再編ポリシー草案。完了条件: 分岐ID監査運用の承認。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="u1">
<h2 class="section-title">U1: 逆問題同定可能性（Round 2）</h2>
<table class="data-table">
<thead><tr><th>RQ</th><th>今回の深掘り（平易）</th><th>追加一次情報</th><th>今回実行する変更</th><th>外部依存タスク</th></tr></thead>
<tbody>
<tr>
<td>1</td>
<td>「不確実性つき推定」を標準にする流れは強く、点推定のみの報告は弱くなっています。</td>
<td>
<a href="https://pubmed.ncbi.nlm.nih.gov/38545514/" target="_blank">SESAMEEG: probabilistic source localization (PMID:38545514, 2024)</a><br>
<a href="https://doi.org/10.1109/JSEN.2024.3502917" target="_blank">Inverse Problem for M/EEG Source Localization: A Review (2025)</a>
</td>
<td>U1の標準出力に「事後分布幅」を必須欄として追加します。</td>
<td>担当: 計測チーム。前提: ベイズ推定実装の統一。完了条件: 全手法で同形式の不確実性出力。</td>
</tr>
<tr>
<td>2</td>
<td>導電率不確実性の影響は、EEG/MEGの両方で直近研究が再確認しています。</td>
<td>
<a href="https://pubmed.ncbi.nlm.nih.gov/38532791/" target="_blank">Global sensitivity of EEG source analysis to tissue conductivity uncertainties (PMID:38532791, 2024)</a><br>
<a href="https://pubmed.ncbi.nlm.nih.gov/41308490/" target="_blank">Global sensitivity of MEG source analysis... (PMID:41308490, 2025)</a>
</td>
<td>導電率感度を「必須感度解析」としてU1テンプレに追記します。</td>
<td>担当: 計測/物理モデル班。前提: 頭部モデル取得。完了条件: 感度解析結果の公開。</td>
</tr>
<tr>
<td>3</td>
<td>MNE/beamformer/Champagneの乖離は依然発生し、裁定ルールなしでは結論が動きます。</td>
<td>
<a href="https://doi.org/10.1109/SAMPTA64769.2025.11133512" target="_blank">Revisiting CHAMPAGNE (2025)</a><br>
<a href="https://pubmed.ncbi.nlm.nih.gov/39423516/" target="_blank">Standardized Kalman filtering for dynamical source localization (PMID:39423516, 2024)</a>
</td>
<td>手法間乖離時の裁定（多数決ではなく誤差境界比較）ルール案を追加します。</td>
<td>担当: 解析WG。前提: 同一データ再解析。完了条件: 裁定ルール検証レポート。</td>
</tr>
<tr>
<td>4</td>
<td>信頼区間/後方分布の公開は「推奨」ではなく、再現性上ほぼ必須に近づいています。</td>
<td>
<a href="https://doi.org/10.1088/2057-1976/aca20b" target="_blank">Neural SDE as UQ for EEG source localization (2023)</a><br>
<a href="https://pubmed.ncbi.nlm.nih.gov/41411682/" target="_blank">Potential of EEG and EEG/MEG skull conductivity estimation... (PMID:41411682, 2026)</a>
</td>
<td>U1公開要件に「95%区間」「後方分布共有リンク」を追加します。</td>
<td>担当: データ公開WG。前提: 共有フォーマット合意。完了条件: 追試で同区間再現。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="u3">
<h2 class="section-title">U3: 生物学的境界（Round 2）</h2>
<table class="data-table">
<thead><tr><th>RQ</th><th>今回の深掘り（平易）</th><th>追加一次情報</th><th>今回実行する変更</th><th>外部依存タスク</th></tr></thead>
<tbody>
<tr>
<td>1</td>
<td>グリア追加の効果は「ある/ない」ではなく、課題ごとの効果量で管理する段階に来ています。</td>
<td>
<a href="https://pubmed.ncbi.nlm.nih.gov/39902809/" target="_blank">Astrocyte-related intervention and behavior improvement (PMID:39902809, 2025)</a><br>
<a href="https://pubmed.ncbi.nlm.nih.gov/40280131/" target="_blank">Neuron-astrocyte coupling mediates depressive-like behaviors (PMID:40280131, 2025)</a>
</td>
<td>U3に「ΔR2/ΔAUC」を必須効果量として追記します。</td>
<td>担当: 実験チーム。前提: グリア操作系の再現手順。完了条件: 効果量付き比較公開。</td>
</tr>
<tr>
<td>2</td>
<td>構造地図の高解像度化は進展中ですが、種横断の機能比較スケールは未統一です。</td>
<td>
<a href="https://www.nature.com/articles/s41586-023-06808-9" target="_blank">Drosophila central brain connectome update (Nature, 2024)</a><br>
<a href="https://pubmed.ncbi.nlm.nih.gov/40703192/" target="_blank">Joint estimation of source dynamics and interactions (PMID:40703192, 2025)</a>
</td>
<td>種横断比較の最小共通指標（予測性能/汎化誤差）案を作成します。</td>
<td>担当: 比較神経班。前提: 種間データ整備。完了条件: 共通指標での比較表公開。</td>
</tr>
<tr>
<td>3</td>
<td>身体・環境ループを削ると、代謝・行動安定性の説明力が落ちる例が増えています。</td>
<td>
<a href="https://pubmed.ncbi.nlm.nih.gov/39163862/" target="_blank">Acetate and cognitive performance under sleep disruption (PMID:39163862, 2024)</a><br>
<a href="https://pubmed.ncbi.nlm.nih.gov/39172838/" target="_blank">Restoring glucose metabolism rescues cognition (PMID:39172838, 2024)</a>
</td>
<td>U3に代謝指標（グルコース/乳酸関連）を補助指標として追加します。</td>
<td>担当: 実験チーム。前提: 代謝計測環境。完了条件: 行動指標との相関評価。</td>
</tr>
<tr>
<td>4</td>
<td>「必要最小構成」は単一理論で決めず、アブレーションで性能低下を見て決める形が現実的です。</td>
<td>
<a href="https://pubmed.ncbi.nlm.nih.gov/38448582/" target="_blank">Neuron-astrocyte program decline in ageing/schizophrenia (PMID:38448582, 2024)</a><br>
<a href="https://pubmed.ncbi.nlm.nih.gov/39048816/" target="_blank">Single-cell multiregion dissection of Alzheimer's disease (PMID:39048816, 2024)</a>
</td>
<td>U3アブレーション計画に「除外時性能低下の下限」を追加します。</td>
<td>担当: 実験設計班。前提: 多領域データ取得。完了条件: 下限値の事前登録。</td>
</tr>
<tr>
<td>5</td>
<td>glymphatic/meningeal系は、認知機能やAβクリアランスに関連する実験が増えています。</td>
<td>
<a href="https://pubmed.ncbi.nlm.nih.gov/38418876/" target="_blank">Gamma stimulation promotes glymphatic clearance (PMID:38418876, 2024)</a><br>
<a href="https://pubmed.ncbi.nlm.nih.gov/40120575/" target="_blank">Meningeal lymphatics-microglia axis regulates synaptic physiology (PMID:40120575, 2025)</a><br>
<a href="https://doi.org/10.3390/biomedicines14020409" target="_blank">Mapping the Brain’s Glymphatic System (2026)</a>
</td>
<td>U3 RQ5にリンパ系関連の有無を記録する監査列を追加します。</td>
<td>担当: 実験チーム。前提: リンパ系計測導入。完了条件: 有無比較の効果量公開。</td>
</tr>
<tr>
<td>6</td>
<td>免疫・炎症シグナルを無視すると、長期予測が崩れる可能性を示す報告が増えています。</td>
<td>
<a href="https://pubmed.ncbi.nlm.nih.gov/38762094/" target="_blank">Neuroinflammation-related long-term dysfunction evidence (PMID:38762094, 2024)</a><br>
<a href="https://pubmed.ncbi.nlm.nih.gov/39888279/" target="_blank">Microglia-derived IL-6 and depression-like behavior (PMID:39888279, 2025)</a><br>
<a href="https://pubmed.ncbi.nlm.nih.gov/40311620/" target="_blank">Neural-activity-regulated glia-mediated brain lymphatic development (PMID:40311620, 2025)</a>
</td>
<td>U3 RQ6に「免疫除外モデルの破綻時点」計測欄を追加します。</td>
<td>担当: 実験チーム。前提: 長期追跡プロトコル承認。完了条件: 週〜月スケール破綻点レポート。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="summary">
<h2 class="section-title">Round 2 要約</h2>
<ul>
<li>U0は理論蓄積は十分ですが、介入同値を扱う実験ベンチ規約が依然不足しています。</li>
<li>U1は不確実性推定と導電率感度の一次情報が増え、公開要件を強化できる段階です。</li>
<li>U3はグリア/リンパ系の実験知見が増加し、「含めるべき最小構成」の定量化が前進しています。</li>
</ul>
</section>

</article>
</main>
