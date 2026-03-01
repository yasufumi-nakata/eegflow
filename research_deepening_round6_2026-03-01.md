---
layout: default
title: "Research Deepening Round 6 (2026-03-01): U13/U14/U15"
description: "U13（模倣分離）・U14（追試可能性）・U15（制度統合）の深掘り。"
article_type: "Evidence Addendum"
subtitle: "模倣対策・再現性運用・制度連携の実装寄り整理"
author: Mind Uploading Research Project
last_updated: "2026-03-01"
note: "Round 6 (U13/U14/U15)"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Round 6 の狙い</h2>
<p>
今回の対象は、最終段の3領域です。
U13では「高精度な模倣」と「因果保存」の分離、
U14では「第三者追試が回る運用」、
U15では「技術KPIと制度KPIの接続」を、実行可能な単位で固定します。
</p>
</div>

<section class="section" id="u13">
<h2 class="section-title">U13: 模倣分離（Round 6）</h2>
<table class="data-table">
<thead><tr><th>RQ</th><th>今回の深掘り（平易）</th><th>追加一次情報</th><th>今回実行する変更</th><th>外部依存タスク</th></tr></thead>
<tbody>
<tr>
<td>1</td>
<td>brain-to-textは「意味が合う」だけでは不十分で、内部過程が保存されているかを別に見る必要があります。</td>
<td>
<a href="https://doi.org/10.1038/s41593-023-01304-9" target="_blank">Semantic reconstruction of continuous language from non-invasive brain recordings (Nature Neuroscience, 2023)</a><br>
<a href="https://doi.org/10.1016/j.celrep.2024.114924" target="_blank">A brain-to-text framework for decoding natural tonal sentences (Cell Reports, 2024)</a>
</td>
<td>U13 RQ1に「意味一致指標」と「因果一致指標」を分離して記録する欄を追加します。</td>
<td>担当: ML評価チーム。前提: 介入付きデコード課題の設計。完了条件: 二指標での公開比較レポート。</td>
</tr>
<tr>
<td>2</td>
<td>LLMの幻覚検査を使うと、神経デコード出力の「見かけの整合」をチェックできますが、因果保存の代替にはなりません。</td>
<td>
<a href="https://arxiv.org/abs/2506.22486" target="_blank">Hallucination Detection with Small Language Models (arXiv, 2025)</a><br>
<a href="https://doi.org/10.1609/aaai.v39i27.35124" target="_blank">Representation Learning: A Causal Perspective (AAAI, 2025)</a>
</td>
<td>U13 RQ2に「幻覚率」と「因果整合率」を同時監査する欄を追加します。</td>
<td>担当: ML評価チーム。前提: 幻覚判定器の導入。完了条件: 二軸監査の自動レポート化。</td>
</tr>
<tr>
<td>3</td>
<td>同じ出力でも内部機構が違う問題には、表現分解と因果視点の評価が有効です。</td>
<td>
<a href="https://doi.org/10.1038/s42256-020-00257-z" target="_blank">Shortcut learning in deep neural networks (Nature Machine Intelligence, 2020)</a><br>
<a href="https://doi.org/10.1609/aaai.v39i27.35124" target="_blank">Causal perspective on representation learning (AAAI, 2025)</a>
</td>
<td>U13 RQ3に「shortcut兆候」チェック欄を追加します。</td>
<td>担当: 解析WG。前提: 介入/反事実評価基盤。完了条件: 同一出力・異機構ケースの検出率公開。</td>
</tr>
<tr>
<td>4</td>
<td>模倣性能の上限を抑えるには、因果評価を最終判定に組み込む必要があります。</td>
<td>
<a href="https://doi.org/10.1609/aaai.v39i17.33998" target="_blank">Learning Strategy Representation for Imitation Learning in Multi-Agent Games (AAAI, 2025)</a><br>
<a href="https://doi.org/10.1016/j.knosys.2025.113565" target="_blank">Causal representation learning in offline visual reinforcement learning (KBS, 2025)</a>
</td>
<td>U13 RQ4に「模倣スコア単独では合格不可」の判定ルールを追加します。</td>
<td>担当: 評価設計WG。前提: 因果評価KPI合意。完了条件: 統一判定規約v1公開。</td>
</tr>
<tr>
<td>5</td>
<td>知覚と想起で同一デコーダを使う場合、劣化の分岐点を取る比較実験が可能になってきています。</td>
<td>
<a href="https://doi.org/10.1109/EMBC58623.2025.11251641" target="_blank">Decoding Visual Imagination and Perception from EEG via Topomap Sequences (EMBC, 2025)</a><br>
<a href="https://doi.org/10.1109/EMBC53108.2024.10782730" target="_blank">Decoding Visual Perception from EEG Using Explainable Graph Neural Network (EMBC, 2024)</a>
</td>
<td>U13 RQ5に「知覚条件」「想起条件」の分離比較欄を追加します。</td>
<td>担当: 実験チーム。前提: 同一被験者での二条件計測。完了条件: 劣化分岐点レポート公開。</td>
</tr>
<tr>
<td>6</td>
<td>プロンプト誘導・データリーク・shortcut学習は、対照条件を固定しないと分離検出できません。</td>
<td>
<a href="https://arxiv.org/abs/2506.22486" target="_blank">Hallucination Detection with Small Language Models (2025)</a><br>
<a href="https://doi.org/10.1038/s42256-020-00257-z" target="_blank">Shortcut learning (2020)</a>
</td>
<td>U13 RQ6に「リーク検出率」「対照実験一致率」の欄を追加します。</td>
<td>担当: ML評価チーム。前提: 対照実験計画承認。完了条件: リーク分離検出の再現結果公開。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="u14">
<h2 class="section-title">U14: 追試可能性（Round 6）</h2>
<table class="data-table">
<thead><tr><th>RQ</th><th>今回の深掘り（平易）</th><th>追加一次情報</th><th>今回実行する変更</th><th>外部依存タスク</th></tr></thead>
<tbody>
<tr>
<td>1</td>
<td>データ/コード/環境の固定粒度を上げるほど再現性は上がりますが、運用コストも上がります。</td>
<td>
<a href="https://doi.org/10.1016/j.jneumeth.2023.109931" target="_blank">Methodical advances in reproducibility research (J Neurosci Methods, 2023)</a><br>
<a href="https://doi.org/10.1038/s41597-024-03559-8" target="_blank">Motion-BIDS extension for reproducible motion data (Scientific Data, 2024)</a>
</td>
<td>U14 RQ1に「固定する最小項目（データ/コード/環境）」チェック欄を追加します。</td>
<td>担当: 再現性WG。前提: コンテナ運用合意。完了条件: 最小固定セットの運用承認。</td>
</tr>
<tr>
<td>2</td>
<td>探索研究と検証研究を運用で分離するには、事前登録と報告テンプレを分ける必要があります。</td>
<td>
<a href="https://doi.org/10.7554/eLife.85980" target="_blank">Enhancing precision in human neuroscience (eLife, 2023)</a><br>
<a href="https://doi.org/10.1001/jama.2025.13350" target="_blank">TARGET Statement (JAMA, 2025)</a>
</td>
<td>U14 RQ2に「探索」「検証」の報告テンプレ分離欄を追加します。</td>
<td>担当: 運用WG。前提: 事前登録運用の合意。完了条件: 二系統テンプレの正式運用。</td>
</tr>
<tr>
<td>3</td>
<td>leaderboard監査では、データリークと過適合を分けて計測する必要があります。</td>
<td>
<a href="https://doi.org/10.1038/s41597-023-02614-0" target="_blank">A comparison of neuroelectrophysiology databases (Scientific Data, 2023)</a><br>
<a href="https://doi.org/10.1002/epi4.12704" target="_blank">EEG datasets for seizure detection/prediction: review (Epilepsia Open, 2023)</a>
</td>
<td>U14 RQ3に「リーク検出率」「外部テスト乖離率」を追加します。</td>
<td>担当: ベンチ運用WG。前提: 外部評価データ確保。完了条件: 定期監査レポート公開。</td>
</tr>
<tr>
<td>4</td>
<td>Model Card / Dataset Cardを評価契約に統合すると、再解析時の説明責任が上がります。</td>
<td>
<a href="https://bids-specification.readthedocs.io/en/stable/" target="_blank">BIDS Specification 1.10.1</a><br>
<a href="https://zenodo.org/records/18201723" target="_blank">BEP036 draft (metadata拡張, 2025)</a>
</td>
<td>U14 RQ4に「Model Card/Dataset Card提出有無」欄を追加します。</td>
<td>担当: データ公開WG。前提: 提出テンプレ承認。完了条件: 全公開案件で提出100%。</td>
</tr>
<tr>
<td>5</td>
<td>再現失敗を否定例として蓄積しないと、同じ失敗が繰り返されます。</td>
<td>
<a href="https://doi.org/10.1016/j.jneumeth.2023.109931" target="_blank">Reproducibility method paper (2023)</a><br>
<a href="https://doi.org/10.7554/eLife.85980" target="_blank">Precision neuroscience and reporting discipline (2023)</a>
</td>
<td>U14 RQ5に「否定例レジストリID」欄を追加します。</td>
<td>担当: 再現性WG。前提: 失敗公開ポリシー。完了条件: 失敗レジストリ定期更新。</td>
</tr>
<tr>
<td>6</td>
<td>コンテナ固定は再現性に有効ですが、計算資源・時間コストの上限を先に決める必要があります。</td>
<td>
<a href="https://arxiv.org/abs/2311.04912" target="_blank">ezBIDS for curation/validation workflow (arXiv, 2023)</a><br>
<a href="https://doi.org/10.1038/s41597-024-03559-8" target="_blank">Motion-BIDS practical extension (2024)</a>
</td>
<td>U14 RQ6に「再現コスト上限（時間/計算）」欄を追加します。</td>
<td>担当: インフラWG。前提: 予算上限設定。完了条件: コスト上限付き再現運用承認。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="u15">
<h2 class="section-title">U15: 制度統合（Round 6）</h2>
<table class="data-table">
<thead><tr><th>RQ</th><th>今回の深掘り（平易）</th><th>追加一次情報</th><th>今回実行する変更</th><th>外部依存タスク</th></tr></thead>
<tbody>
<tr>
<td>1</td>
<td>神経データは通常の個人データより機微性が高く、法概念を明示して扱う必要があります。</td>
<td>
<a href="https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng" target="_blank">EU AI Act (Regulation (EU) 2024/1689)</a><br>
<a href="https://doi.org/10.1016/S1474-4422(25)00124-3" target="_blank">Neurorights in neurology (Lancet Neurology, 2025)</a>
</td>
<td>U15 RQ1に「法概念マッピング（個人/生体/神経）」欄を追加します。</td>
<td>担当: 法務WG。前提: 法域別定義整理。完了条件: 法概念対照表の承認。</td>
</tr>
<tr>
<td>2</td>
<td>neurorightsは理念だけでなく、監査項目（ログ・説明責任・停止条件）に落とす必要があります。</td>
<td>
<a href="https://doi.org/10.1093/jhuman/huae042" target="_blank">Establishing Neurorights: New Rights versus Derived Rights (Journal of Human Rights Practice, 2024)</a><br>
<a href="https://doi.org/10.6028/NIST.AI.600-1" target="_blank">NIST AI RMF: Generative AI Profile (2024)</a>
</td>
<td>U15 RQ2に「neurorights監査チェックリスト」欄を追加します。</td>
<td>担当: 監査WG。前提: チェック項目合意。完了条件: 監査票v1公開。</td>
</tr>
<tr>
<td>3</td>
<td>法域差を跨ぐ最小共通運用は、EU法・国際原則・条約の共通部分を先に固定するのが現実的です。</td>
<td>
<a href="https://oecd.ai/en/ai-principles" target="_blank">OECD AI Principles</a><br>
<a href="https://book.coe.int/en/texts-of-council-of-europe-treaties/12225-council-of-europe-framework-convention-on-artificial-intelligence-and-human-rights-democracy-and-the-rule-of-law-cets-no-225.html" target="_blank">Council of Europe Framework Convention on AI (CETS No.225, 2024)</a>
</td>
<td>U15 RQ3に「共通要件（最低運用）」欄を追加します。</td>
<td>担当: ガバナンス委員会。前提: 法域比較レビュー。完了条件: 最小共通運用仕様の承認。</td>
</tr>
<tr>
<td>4</td>
<td>停止条件・更新条件は、制度文書と技術KPIをひも付けて初めて運用できます。</td>
<td>
<a href="https://www.iso.org/standard/42001" target="_blank">ISO/IEC 42001 AI management systems (2023)</a><br>
<a href="https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng" target="_blank">EU AI Act (2024)</a>
</td>
<td>U15 RQ4に「停止トリガーKPI」「更新トリガーKPI」を追加します。</td>
<td>担当: ガバナンス委員会。前提: KPI閾値の合意。完了条件: 停止/更新運用の承認。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="summary">
<h2 class="section-title">Round 6 要約</h2>
<ul>
<li>U13は、模倣精度を因果評価で抑制する設計が中核です。</li>
<li>U14は、追試を回すための運用項目（固定粒度・失敗公開・コスト上限）が中核です。</li>
<li>U15は、法制度文書と技術KPIの接続設計が中核です。</li>
</ul>
</section>

</article>
</main>
