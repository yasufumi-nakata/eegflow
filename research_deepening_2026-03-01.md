---
layout: default
title: "Research Deepening (2026-03-01): U0-U15 追補"
description: "research_harvest_50.md の各リサーチクエスチョンに対する、一次情報ベースの追補メモ。"
article_type: "Evidence Addendum"
subtitle: "平易な説明 + 追加根拠 + 未解決点"
author: Mind Uploading Research Project
last_updated: "2026-03-01"
note: "Round 1 deepening"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>このページの目的</h2>
<p>
このページは、<code>research_harvest_50.md</code> の各リサーチクエスチョンに対して、
一次情報（DOI・PubMed・公式規格）を追加し、
「いま何が言えるか」と「まだ言えないこと」を分けて整理した追補です。
</p>
<p>
断定を避けるため、<strong>未確定</strong> は未確定と明記しています。
</p>
</div>

<section class="section" id="u0">
<h2 class="section-title">U0: 操作的同一性</h2>
<table class="data-table">
<thead><tr><th>RQ</th><th>平易な説明</th><th>今回の追加情報（一次情報）</th><th>未解決</th></tr></thead>
<tbody>
<tr><td>1</td><td>「見た目が同じ」と「介入に対する反応が同じ」のどちらを重く見るか。</td><td>同一性議論は整理が進んでいますが、実験ベンチは未整備です（<a href="https://doi.org/10.1017/9781009486309.002" target="_blank">The Right to Personal Identity</a>, 2026）。</td><td>必要条件/十分条件の運用合意がありません。</td></tr>
<tr><td>2</td><td>時刻合わせと状態表現を、誰でも再現できる形で固定できるか。</td><td>心身連続性の議論はありますが、ms同期を含む技術規約には直結していません（<a href="https://doi.org/10.2139/ssrn.4560723" target="_blank">Nondestructive Mind Uploading and the Stream of Consciousness</a>, 2023）。</td><td>同期と評価軸を同時に規定する標準が不足しています。</td></tr>
<tr><td>3</td><td>「同一」と判定する閾値を、都合よく動かせない形で決められるか。</td><td>哲学側の反証は増えています（<a href="https://doi.org/10.1007/s11229-024-04744-3" target="_blank">I am no abstract object</a>, 2024）。ただし、閾値設計の実証手法は未成熟です。</td><td>過学習モデル除外の定量規則が不足しています。</td></tr>
<tr><td>4</td><td>複製が出たとき、どちらを「同一個体」と扱うか。</td><td>分岐問題の理論整理は前進していますが、技術監査へ落ちる粒度はまだ粗いです（同上 + 2026 Cambridge章）。</td><td>分岐後の責任帰属と評価帰属の接続規約が未整備です。</td></tr>
</tbody></table>
</section>

<section class="section" id="u1">
<h2 class="section-title">U1: 逆問題同定可能性</h2>
<table class="data-table">
<thead><tr><th>RQ</th><th>平易な説明</th><th>今回の追加情報（一次情報）</th><th>未解決</th></tr></thead>
<tbody>
<tr><td>1</td><td>逆問題が不安定なとき、事前分布でどこまで安定化できるか。</td><td>2025年レビューで、Bayesian化と疎性仮定の有効性が再整理されています（<a href="https://doi.org/10.1109/JSEN.2024.3502917" target="_blank">Inverse Problem for M/EEG Source Localization: A Review</a>）。</td><td>タスク横断の最適事前分布は未確定です。</td></tr>
<tr><td>2</td><td>導電率や電極ずれなどの誤差を、不確実性として最終推定に反映できるか。</td><td>不確実性伝播の数値法が更新されています（<a href="https://doi.org/10.1088/1361-6420/acf9c6" target="_blank">Inverse Problems</a>, 2023）。</td><td>被験者間・装置間を同時に扱う誤差境界は不足です。</td></tr>
<tr><td>3</td><td>解法ごとに答えが違うとき、どれを採用するか。</td><td>同一データで手法差が出ることは再確認されています（上記レビュー + <a href="https://doi.org/10.1109/SAMPTA64769.2025.11133512" target="_blank">Revisiting CHAMPAGNE</a>, 2025）。</td><td>「乖離時の裁定ルール」が標準化されていません。</td></tr>
<tr><td>4</td><td>点推定だけでなく、信頼区間まで公開すべきか。</td><td>不確実性推定を前提にしたEEG手法が増えています（<a href="https://doi.org/10.1088/2057-1976/aca20b" target="_blank">Neural SDE UQ for EEG</a>, 2023; <a href="https://doi.org/10.1088/2632-2153/aded57" target="_blank">Bayesian parameter learning</a>, 2025）。</td><td>公開最小要件（CI/後方分布の必須範囲）が未合意です。</td></tr>
</tbody></table>
</section>

<section class="section" id="u3">
<h2 class="section-title">U3: 生物学的境界</h2>
<table class="data-table">
<thead><tr><th>RQ</th><th>平易な説明</th><th>今回の追加情報（一次情報）</th><th>未解決</th></tr></thead>
<tbody>
<tr><td>1</td><td>グリアや体液性調節を足したとき、予測がどれだけ良くなるか。</td><td>アストロサイト介入で行動改善が報告されています（<a href="https://pubmed.ncbi.nlm.nih.gov/39902809/" target="_blank">Glia, 2025, PMID:39902809</a>）。</td><td>効果量をWBE向け評価軸へ変換する規約が不足です。</td></tr>
<tr><td>2</td><td>配線の完全さと機能予測の関係を、種をまたいで比べられるか。</td><td>ショウジョウバエ中央脳の大規模構造地図が更新されています（<a href="https://www.nature.com/articles/s41586-023-06808-9" target="_blank">Nature</a>, 2024）。</td><td>構造→機能の比較指標が種横断で統一されていません。</td></tr>
<tr><td>3</td><td>身体・環境ループを除くと、何が落ちるか。</td><td>Embodied系の実験・理論蓄積は続いていますが、WBE評価契約への直結は限定的です（既存文献群 + BIDS運用研究）。</td><td>除去実験の標準タスク設計が不足しています。</td></tr>
<tr><td>4</td><td>「最低限これがあれば主体を再現した」と、データで言えるか。</td><td>構造マップは急速に整備されていますが、必要最小構成の閾値は未確定です（Nature connectome更新）。</td><td>閾値決定に使う反証可能プロトコルが不足です。</td></tr>
<tr><td>5</td><td>glymphatic/meningeal系を入れる価値があるか。</td><td>2026年レビューで系統図は整理されています（<a href="https://doi.org/10.3390/biomedicines14020409" target="_blank">Mapping the Brain’s Glymphatic System</a>）。</td><td>予測改善量の定量は未確定です（レビュー中心）。</td></tr>
<tr><td>6</td><td>免疫監視を外すと、いつ長期予測が壊れるか。</td><td>神経炎症・グリア制御の知見は増加しています（例: <a href="https://pubmed.ncbi.nlm.nih.gov/38762094/" target="_blank">Exp Neurol, 2024, PMID:38762094</a>）。</td><td>WBE文脈での長期破綻閾値は未測定です。</td></tr>
</tbody></table>
</section>

<section class="section" id="u4">
<h2 class="section-title">U4: 因果同値</h2>
<table class="data-table">
<thead><tr><th>RQ</th><th>平易な説明</th><th>今回の追加情報（一次情報）</th><th>未解決</th></tr></thead>
<tbody>
<tr><td>1</td><td>相関データから因果グラフへ進める条件は何か。</td><td>高次元脳時系列向けの動的DAG推定法が提示されています（<a href="https://doi.org/10.1016/j.neuroimage.2024.120684" target="_blank">NeuroImage, 2024</a>）。</td><td>未観測交絡への頑健性は限定的です。</td></tr>
<tr><td>2</td><td>どこまで介入したら「因果が同じ」と言えるか。</td><td>構造情報を使った有向接続モデリングの整理が進んでいます（<a href="https://doi.org/10.1038/s41583-024-00881-3" target="_blank">Nat Rev Neurosci, 2025</a>）。</td><td>介入設計と失敗基準の公開規約が不足です。</td></tr>
<tr><td>3</td><td>active inference / DCMの予測を、反事実評価に接続できるか。</td><td>DCMは実応用が継続的に増えています（<a href="https://pubmed.ncbi.nlm.nih.gov/38826672/" target="_blank">PMID:38826672</a>）。</td><td>反事実評価との橋渡し指標が未統一です。</td></tr>
<tr><td>4</td><td>どの条件で「同値ではない」と明確に言うか。</td><td>既存レビューは課題領域の偏りを示しています（<a href="https://doi.org/10.1109/TNSRE.2021.3123964" target="_blank">DCM Systematic Review</a>）。</td><td>falsificationを段階化した実運用基準が不足です。</td></tr>
</tbody></table>
</section>

<section class="section" id="u7">
<h2 class="section-title">U7: マルチモーダル整合</h2>
<table class="data-table">
<thead><tr><th>RQ</th><th>平易な説明</th><th>今回の追加情報（一次情報）</th><th>未解決</th></tr></thead>
<tbody>
<tr><td>1</td><td>BIDSで同期・QC・刺激ログをどこまで必須にするか。</td><td>BIDS 1.10.1でモダリティ仕様と必須項目が拡張・明確化されています（<a href="https://bids-specification.readthedocs.io/en/stable/" target="_blank">BIDS Spec 1.10.1</a>）。</td><td>WBE向け必須メタデータ最小集合は未合意です。</td></tr>
<tr><td>2</td><td>LSLなどの同期誤差を、再現可能な数値で示せるか。</td><td>同時EEG-fMRIの安全性・品質評価の実測研究があります（<a href="https://pubmed.ncbi.nlm.nih.gov/34214093/" target="_blank">PMID:34214093</a>）。</td><td>タスク別の許容誤差閾値が不足しています。</td></tr>
<tr><td>3</td><td>前処理設定差（ASR等）が結果をどれだけ動かすか監査できるか。</td><td>同時記録向けアーチファクト除去法が更新されています（<a href="https://arxiv.org/abs/2411.05812" target="_blank">LR+SD for EEG-fMRI</a>）。</td><td>設定差監査の共通テンプレートが不足です。</td></tr>
<tr><td>4</td><td>アライメント失敗時に再計測/除外をどう決めるか。</td><td>BIDS運用側で検証ツールは増えています（<a href="https://arxiv.org/abs/2311.04912" target="_blank">ezBIDS</a>）。</td><td>「失敗時の意思決定規則」の標準化が未完です。</td></tr>
<tr><td>5</td><td>前処理差分CIで、どの低下をリリース停止にするか。</td><td>OpenNeuro上で標準化と検証が進んでいます（BIDS/OpenNeuro運用情報）。</td><td>リリースブロック閾値の業界標準は未形成です。</td></tr>
<tr><td>6</td><td>モダリティ欠損でも同じ結論を保てる最小観測セットは何か。</td><td>BIDS化されたマルチモーダルデータセット公開が増えています（<a href="https://doi.org/10.3389/fnrgo.2024.1411305" target="_blank">Frontiers dataset, 2024</a>）。</td><td>欠損頑健性の横断ベンチが不足です。</td></tr>
</tbody></table>
</section>

<section class="section" id="u8">
<h2 class="section-title">U8: 閉ループ安定性</h2>
<table class="data-table">
<thead><tr><th>RQ</th><th>平易な説明</th><th>今回の追加情報（一次情報）</th><th>未解決</th></tr></thead>
<tbody>
<tr><td>1</td><td>閉ループ制御が破綻しない遅延範囲を決められるか。</td><td>PDでのaDBS臨床試験が進み、制御戦略の実地データが増えています（<a href="https://doi.org/10.1038/s41591-024-03196-z" target="_blank">Nat Med, 2024</a>）。</td><td>遅延許容域の一般式は未確立です。</td></tr>
<tr><td>2</td><td>ドリフトに合わせてオンライン較正できるか。</td><td>長期運用とプログラミング手順の報告が増えています（<a href="https://doi.org/10.1038/s41531-025-01124-7" target="_blank">npj Parkinson’s, 2025</a>）。</td><td>疾患横断で使える較正標準は未整備です。</td></tr>
<tr><td>3</td><td>個体差・日内変動をまたいで安定といえるか。</td><td>在宅運用データを含む報告があります（<a href="https://doi.org/10.1093/brain/awad429" target="_blank">Brain, 2024</a>）。</td><td>評価指標の共通化が不足です。</td></tr>
<tr><td>4</td><td>異常検知・フェイルセーフを契約化できるか。</td><td>神経デコーダを遠隔最適化する報告が出ています（<a href="https://doi.org/10.1038/s41551-025-01438-0" target="_blank">Nat Biomed Eng, 2026 issue</a>）。</td><td>失敗時停止ルールの法規格連動が弱いです。</td></tr>
<tr><td>5</td><td>人手介入（オーバーライド）を入れたときKPIをどう置くか。</td><td>臨床現場でのaDBS運用原則が整理され始めています（<a href="https://pubmed.ncbi.nlm.nih.gov/39252901/" target="_blank">Delphi consensus, PMID:39252901</a>）。</td><td>誤作動率/回復時間の標準KPIは未合意です。</td></tr>
<tr><td>6</td><td>再学習頻度を安全余裕と性能で最適化できるか。</td><td>慢性運用の初期実データが増えています（<a href="https://www.nature.com/articles/s41531-026-01269-z" target="_blank">ADAPT-START pre-proof, 2026-02-25</a>）。</td><td>長期最適化の一般解は未確立です。</td></tr>
</tbody></table>
</section>

<section class="section" id="u10">
<h2 class="section-title">U10: 熱力学的一貫性</h2>
<table class="data-table">
<thead><tr><th>RQ</th><th>平易な説明</th><th>今回の追加情報（一次情報）</th><th>未解決</th></tr></thead>
<tbody>
<tr><td>1</td><td>Landauer下限を神経計算でどう読むか。</td><td>情報熱力学を神経推論に接続する整理が公開されています（<a href="https://doi.org/10.3390/e26090779" target="_blank">Entropy, 2024</a>）。</td><td>WBEスケールへの外挿は未確定です。</td></tr>
<tr><td>2</td><td>非平衡指標と情報処理効率を対応づけられるか。</td><td>脳状態とエントロピー生成の相関研究があります（<a href="https://doi.org/10.1103/PhysRevE.107.024121" target="_blank">Phys Rev E, 2023</a>）。</td><td>因果方向（効率↔散逸）の確定は未達です。</td></tr>
<tr><td>3</td><td>理論式を観測可能な実験設計へ落とせるか。</td><td>概念整理は進みましたが、実測系はまだ限定的です（Entropy 2024 perspective）。</td><td>標準計測プロトコルが不足しています。</td></tr>
<tr><td>4</td><td>計算コスト評価に熱制約を組み込めるか。</td><td>理論側（Landauer拡張等）は進展しています（<a href="https://arxiv.org/abs/2502.03603" target="_blank">Dynamical Landauer principle, 2025</a>）。</td><td>実装評価KPIに落ちる共通モデルは未成立です。</td></tr>
</tbody></table>
</section>

<section class="section" id="u11">
<h2 class="section-title">U11: 意識指標近似の妥当性</h2>
<table class="data-table">
<thead><tr><th>RQ</th><th>平易な説明</th><th>今回の追加情報（一次情報）</th><th>未解決</th></tr></thead>
<tbody>
<tr><td>1</td><td>理論比較の入出力仕様を共通化できるか。</td><td>大規模敵対的共同研究の本体結果が公開されました（<a href="https://www.nature.com/articles/s41586-025-08888-1" target="_blank">Nature, 2025</a>）。</td><td>完全な共通仕様はまだ固定されていません。</td></tr>
<tr><td>2</td><td>PCI/IIT計算量制約を実運用でどう扱うか。</td><td>PCI運用の限界と互換性議論が進んでいます（<a href="https://doi.org/10.1093/nc/niad016" target="_blank">Neuroscience of Consciousness, 2023</a>）。</td><td>計算近似の妥当域が未確定です。</td></tr>
<tr><td>3</td><td>理論対立点を単一プロトコルで検証できるか。</td><td>事前登録型の対立検証プロトコルが公開済みです（<a href="https://doi.org/10.1371/journal.pone.0268577" target="_blank">PLOS ONE, 2023</a>）。</td><td>理論追加時の拡張規則は未整備です。</td></tr>
<tr><td>4</td><td>臨床/研究で誤判定時の失敗条件を明示できるか。</td><td>PCIが行動回復より先に容量検出する報告があります（<a href="https://doi.org/10.1016/j.brs.2023.01.731" target="_blank">Brain Stimulation, 2023</a>）。</td><td>誤検知・偽陰性の運用閾値が未統一です。</td></tr>
</tbody></table>
</section>

<section class="section" id="u12">
<h2 class="section-title">U12: 分岐本人性</h2>
<table class="data-table">
<thead><tr><th>RQ</th><th>平易な説明</th><th>今回の追加情報（一次情報）</th><th>未解決</th></tr></thead>
<tbody>
<tr><td>1</td><td>分岐後主体のIDを何で決めるか。</td><td>AI法学側では「AIに法的人格を与えない」立場が明確化されています（<a href="https://doi.org/10.1016/j.patter.2023.100861" target="_blank">Patterns, 2023</a>）。</td><td>分岐人間主体への直接適用は未確定です。</td></tr>
<tr><td>2</td><td>責任・権利・同意の継承時点をいつにするか。</td><td>EU AI Actは義務主体整理を強化しています（<a href="https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng" target="_blank">Regulation (EU) 2024/1689</a>）。</td><td>分岐本人性そのものの法条文化は未整備です。</td></tr>
<tr><td>3</td><td>心理的連続性と法的個体基準が食い違う場合の処理。</td><td>デジタルツイン倫理の議論は増えています（<a href="https://doi.org/10.1111/bioe.70045" target="_blank">Bioethics, 2025</a>）。</td><td>裁判実務に耐える判定ルールは不足です。</td></tr>
<tr><td>4</td><td>性能評価と人格帰属評価をどう接続するか。</td><td>政策側はリスク管理を先行させる設計です（EU AI Act / OECD更新）。</td><td>技術KPIと人格KPIの連結テンプレートが未整備です。</td></tr>
<tr><td>5</td><td>記憶再同期が起きたとき、法的IDをどう再編するか。</td><td>デジタルヒューマンツイン論文で課題化されています（<a href="https://doi.org/10.1007/s00146-025-02796-8" target="_blank">AI &amp; Society, 2025</a>）。</td><td>監査可能な再編手順は未確定です。</td></tr>
<tr><td>6</td><td>同意撤回時に複数分岐へ権限剥奪をどう実装するか。</td><td>現行ガバナンスは主体単位管理が中心で、分岐主体管理は想定が弱いです（EU/OECD文書）。</td><td>実装仕様（鍵管理・監査ログ）が不足です。</td></tr>
</tbody></table>
</section>

<section class="section" id="u13">
<h2 class="section-title">U13: 模倣分離</h2>
<table class="data-table">
<thead><tr><th>RQ</th><th>平易な説明</th><th>今回の追加情報（一次情報）</th><th>未解決</th></tr></thead>
<tbody>
<tr><td>1</td><td>brain-to-text成功を「意味一致」と「因果再現」に分けて測れるか。</td><td>因果表現学習を使う流れが拡大しています（<a href="https://doi.org/10.3390/e26070556" target="_blank">Diffusion-Based Causal Representation Learning, 2024</a>）。</td><td>神経デコードへの直接適用例は限定的です。</td></tr>
<tr><td>2</td><td>LLM幻覚検査を神経デコード評価へ接続できるか。</td><td>学習表現を因果視点で定義する整理が進んでいます（<a href="https://doi.org/10.1609/aaai.v39i27.35124" target="_blank">AAAI, 2025</a>）。</td><td>幻覚検出を因果保存判定へ直結する標準は未整備です。</td></tr>
<tr><td>3</td><td>出力が同じでも内部機構が違うケースを検出できるか。</td><td>戦略表現分離の実装例が示されています（<a href="https://doi.org/10.1609/aaai.v39i17.33998" target="_blank">AAAI, 2025</a>）。</td><td>神経系モデルへの移植時の妥当性は未検証です。</td></tr>
<tr><td>4</td><td>模倣性能だけ高いモデルを、因果評価で抑制できるか。</td><td>因果表現を使うと「見かけ一致」偏重を下げられる可能性が示唆されています（Entropy 2024 + AAAI 2025）。</td><td>統一ベンチが不足です。</td></tr>
<tr><td>5</td><td>知覚と想起で同じデコーダを使ったとき、劣化の分岐点を取れるか。</td><td>現時点では直接比較データが限定的で、未確定です。</td><td>同一被験者・同一課題の公開ベンチが必要です。</td></tr>
<tr><td>6</td><td>データリークやshortcut学習を対照実験で分離できるか。</td><td>因果視点での表現検査設計は進んでいますが、神経デコード特化版は少数です（AAAI系手法）。</td><td>リーク検出を含む標準プロトコルが未整備です。</td></tr>
</tbody></table>
</section>

<section class="section" id="u14">
<h2 class="section-title">U14: 追試可能性</h2>
<table class="data-table">
<thead><tr><th>RQ</th><th>平易な説明</th><th>今回の追加情報（一次情報）</th><th>未解決</th></tr></thead>
<tbody>
<tr><td>1</td><td>データ/コード/環境をどこまで固定すべきか。</td><td>種間再現性分析でも手順固定の重要性が再確認されています（<a href="https://doi.org/10.1016/j.jneumeth.2023.109931" target="_blank">J Neurosci Methods, 2023</a>）。</td><td>固定粒度の最小合意が不足です。</td></tr>
<tr><td>2</td><td>探索研究と検証研究を運用で分離できるか。</td><td>BIDS/OpenNeuro運用により、公開時の最低要件が実務化されています（<a href="https://bids-specification.readthedocs.io/en/stable/" target="_blank">BIDS 1.10.1</a>）。</td><td>探索→検証の切替条件が未統一です。</td></tr>
<tr><td>3</td><td>leaderboardのリーク/過適合を監査できるか。</td><td>標準化ツールで提出前検証は改善しています（<a href="https://arxiv.org/abs/2311.04912" target="_blank">ezBIDS, 2023</a>）。</td><td>リーク監査の強制仕様は不足しています。</td></tr>
<tr><td>4</td><td>Model Card / Dataset Cardを評価契約に入れられるか。</td><td>FAIR・メタデータ拡張の実務議論が進んでいます（<a href="https://zenodo.org/records/18201723" target="_blank">BEP036 draft, 2025</a>）。</td><td>契約条項への標準組み込みは未完です。</td></tr>
<tr><td>5</td><td>再現失敗を公開し、再試行サイクルを回せるか。</td><td>否定例の公開価値は方法論側で強調されています（J Neurosci Methods 2023）。</td><td>失敗レジストリの運用標準が不足です。</td></tr>
<tr><td>6</td><td>コンテナ固定で増えるコストをどこまで許容するか。</td><td>再現性向上と運用負荷のトレードオフは依然大きいです（BIDS実装報告群）。</td><td>許容コストの合意指標が未整備です。</td></tr>
</tbody></table>
</section>

<section class="section" id="u15">
<h2 class="section-title">U15: 制度統合</h2>
<table class="data-table">
<thead><tr><th>RQ</th><th>平易な説明</th><th>今回の追加情報（一次情報）</th><th>未解決</th></tr></thead>
<tbody>
<tr><td>1</td><td>神経データの機微性を、どの法概念で扱うか。</td><td>EU AI Actが高リスク運用と基本権保護を法制化しています（<a href="https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng" target="_blank">EU 2024/1689</a>）。</td><td>神経データ特化条項は国際的に未統一です。</td></tr>
<tr><td>2</td><td>neurorightsを監査項目へ落とせるか。</td><td>NIST AI RMFとGenAI Profileで監査観点が具体化されています（<a href="https://doi.org/10.6028/NIST.AI.600-1" target="_blank">NIST AI 600-1, 2024</a>）。</td><td>neurorights専用チェックリストは未確立です。</td></tr>
<tr><td>3</td><td>EU/US/JPをまたぐ最小共通運用を定義できるか。</td><td>OECD原則が共通語彙の土台を更新しています（<a href="https://oecd.ai/ai-principles/" target="_blank">OECD AI Principles update, 2024</a>）。</td><td>法執行レベルの相互承認は未成熟です。</td></tr>
<tr><td>4</td><td>技術進展に応じた停止条件・更新条件を制度化できるか。</td><td>管理システム規格としてISO/IEC 42001が実務枠を提示しています（<a href="https://www.iso.org/standard/42001" target="_blank">ISO/IEC 42001:2023</a>）。</td><td>停止基準を技術KPIへ直結する具体規約が不足です。</td></tr>
</tbody></table>
</section>

<section class="section" id="limits">
<h2 class="section-title">今回の限界（正直な記録）</h2>
<ul>
<li>U13（模倣分離）とU12（分岐本人性）は、神経実験より理論・法学文献の比率が高く、WBE直結の実証はまだ薄いです。</li>
<li>U10（熱力学）は概念整理が先行し、実測系の標準化は未完です。</li>
<li>U8（閉ループ安定性）は2024-2026で進展が大きい一方、適応アルゴリズムの外部再現データはまだ限られます。</li>
</ul>
</section>

</article>
</main>
