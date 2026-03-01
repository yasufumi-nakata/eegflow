---
layout: default
title: "Research Deepening Round 12 (2026-03-01): 問い別エビデンス追補（残ユニット）"
description: "U0/U1/U4/U8/U10/U13/U14/U15 の38問いを問い単位で補完。"
article_type: "Evidence Addendum"
subtitle: "Round 11 に続く全体カバレッジ完成ラウンド"
author: Mind Uploading Research Project
last_updated: "2026-03-01"
note: "Round 12 (question-specific enrichment for remaining units)"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Round 12 の狙い</h2>
<p>
Round 11 で U3/U7/U11/U12 の問い別化を実施しました。
Round 12 では残りの U0/U1/U4/U8/U10/U13/U14/U15 を同じ方式で展開し、
全60問いを「問い単位で必須2本を持つ」状態へ揃えました。
</p>
</div>

<section class="section" id="deliverables">
<h2 class="section-title">成果物</h2>
<ul>
<li><a href="automation/rq_question_specific_enrichment_round12_2026-03-01.csv" target="_blank">rq_question_specific_enrichment_round12_2026-03-01.csv</a>（38問い）</li>
</ul>
</section>

<section class="section" id="coverage">
<h2 class="section-title">適用カバレッジ</h2>
<table class="data-table">
<thead><tr><th>U</th><th>対象RQ数</th><th>問い別化の焦点</th></tr></thead><tbody>
<tr><td>U0</td><td>4</td><td>同一性判定の条件分解と閾値化</td></tr>
<tr><td>U1</td><td>4</td><td>逆問題の不確実性・頑健性・較正</td></tr>
<tr><td>U4</td><td>4</td><td>因果識別条件と反証条件の固定</td></tr>
<tr><td>U8</td><td>6</td><td>遅延/ドリフト/安全KPIの運用化</td></tr>
<tr><td>U10</td><td>4</td><td>情報熱力学と実測設計の接続</td></tr>
<tr><td>U13</td><td>6</td><td>模倣性能と因果保存の分離</td></tr>
<tr><td>U14</td><td>6</td><td>追試運用の固定項目と監査</td></tr>
<tr><td>U15</td><td>4</td><td>制度要求と技術KPIの接続</td></tr>
<tr><td><strong>合計</strong></td><td><strong>38</strong></td><td><strong>全行で必須2本を割当済み</strong></td></tr>
</tbody></table>
</section>

<section class="section" id="question-map">
<h2 class="section-title">問い別マップ（要約）</h2>
<table class="data-table">
<thead><tr><th>U-RQ</th><th>要点（平易）</th><th>必須1</th><th>必須2</th><th>今回実行する変更</th><th>外部依存タスク</th></tr></thead><tbody>
<tr><td>U0-1</td><td>「観測一致だけでは足りない」という方向は強いですが、介入一致をどう必要条件化するかは未合意です。</td><td><a href="https://doi.org/10.31219/osf.io/sr7cf" target="_blank">DOI</a></td><td><a href="https://arxiv.org/abs/2510.15745" target="_blank">arXiv</a></td><td>U0判定テンプレに「観測一致」「介入一致」を別項目として固定する下書きを作成します。</td><td>担当: 法務/倫理WG。前提: 分岐時責任の原則合意。完了条件: 判定規約v1承認。</td></tr>
<tr><td>U0-2</td><td>ms同期と状態表現の固定は技術側で定義できますが、同一性判定へどう重み付けするかは理論側の未解決です。</td><td><a href="https://doi.org/10.1093/acprof:oso/9780198754855.003.0013" target="_blank">DOI</a></td><td><a href="https://doi.org/10.1017/9781009367059.009" target="_blank">DOI</a></td><td>同期誤差を数値で残すため、U0の評価欄に「時刻ずれ(ms)」を追加します。</td><td>担当: 計測チーム。前提: 同期計測手順の標準化。完了条件: 監査可能な同期ログ様式確定。</td></tr>
<tr><td>U0-3</td><td>閾値設計（どこから同一とみなすか）は、哲学文献は豊富でも実験設計に直結する共通規約が不足しています。</td><td><a href="https://doi.org/10.1007/s11229-024-04744-3" target="_blank">DOI</a></td><td><a href="https://doi.org/10.2139/ssrn.2596460" target="_blank">DOI</a></td><td>U0に ROC-AUC と閾値感度を入れた最小評価シートをCSV化します。</td><td>担当: 評価設計WG。前提: 最低タスクセット合意。完了条件: 閾値感度分析の再現レポート。</td></tr>
<tr><td>U0-4</td><td>分岐/複製での同一性は、性能評価だけでは決まらず、責任追跡IDの運用設計が不可欠です。</td><td><a href="https://doi.org/10.1017/9781009486309.002" target="_blank">DOI</a></td><td><a href="https://doi.org/10.1016/j.patter.2023.100861" target="_blank">DOI</a></td><td>U0 RQ4に ID衝突率・責任追跡率を必須指標として明記します。</td><td>担当: 法務/ガバナンスWG。前提: ID再編ポリシー草案。完了条件: 分岐ID監査運用の承認。</td></tr>
<tr><td>U1-1</td><td>「不確実性つき推定」を標準にする流れは強く、点推定のみの報告は弱くなっています。</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/38545514/" target="_blank">PubMed</a></td><td><a href="https://doi.org/10.1109/JSEN.2024.3502917" target="_blank">DOI</a></td><td>U1の標準出力に「事後分布幅」を必須欄として追加します。</td><td>担当: 計測チーム。前提: ベイズ推定実装の統一。完了条件: 全手法で同形式の不確実性出力。</td></tr>
<tr><td>U1-2</td><td>導電率不確実性の影響は、EEG/MEGの両方で直近研究が再確認しています。</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/38532791/" target="_blank">PubMed</a></td><td><a href="https://pubmed.ncbi.nlm.nih.gov/41308490/" target="_blank">PubMed</a></td><td>導電率感度を「必須感度解析」としてU1テンプレに追記します。</td><td>担当: 計測/物理モデル班。前提: 頭部モデル取得。完了条件: 感度解析結果の公開。</td></tr>
<tr><td>U1-3</td><td>MNE/beamformer/Champagneの乖離は依然発生し、裁定ルールなしでは結論が動きます。</td><td><a href="https://doi.org/10.1109/SAMPTA64769.2025.11133512" target="_blank">DOI</a></td><td><a href="https://pubmed.ncbi.nlm.nih.gov/39423516/" target="_blank">PubMed</a></td><td>手法間乖離時の裁定（多数決ではなく誤差境界比較）ルール案を追加します。</td><td>担当: 解析WG。前提: 同一データ再解析。完了条件: 裁定ルール検証レポート。</td></tr>
<tr><td>U1-4</td><td>信頼区間/後方分布の公開は「推奨」ではなく、再現性上ほぼ必須に近づいています。</td><td><a href="https://doi.org/10.1088/2057-1976/aca20b" target="_blank">DOI</a></td><td><a href="https://pubmed.ncbi.nlm.nih.gov/41411682/" target="_blank">PubMed</a></td><td>U1公開要件に「95%区間」「後方分布共有リンク」を追加します。</td><td>担当: データ公開WG。前提: 共有フォーマット合意。完了条件: 追試で同区間再現。</td></tr>
<tr><td>U4-1</td><td>相関から因果へ進むには、構造仮定と識別条件を明示しないと、同じデータから別結論が出ます。</td><td><a href="https://doi.org/10.1038/s41583-024-00881-3" target="_blank">DOI</a></td><td><a href="https://doi.org/10.1016/j.neuroimage.2024.120954" target="_blank">DOI</a></td><td>U4に「識別条件を明示しない主張は採択しない」監査チェックを追加します。</td><td>担当: 実験設計チーム。前提: 介入設計レビュー会の合意。完了条件: 因果主張テンプレの承認。</td></tr>
<tr><td>U4-2</td><td>最小因果主張は、実際に介入して差分が再現されること（反復可能）が必要です。</td><td><a href="https://doi.org/10.1109/TMI.2024.3381670" target="_blank">DOI</a></td><td><a href="https://doi.org/10.1001/jamanetworkopen.2024.9220" target="_blank">DOI</a></td><td>U4 RQ2に「介入効果の反復再現（別セッション）」を必須欄として追加します。</td><td>担当: 臨床/実験チーム。前提: 介入プロトコル承認。完了条件: 反復介入レポート公開。</td></tr>
<tr><td>U4-3</td><td>DCMやactive inferenceは使えますが、反事実評価へ接続する設計を最初に決めないと説明止まりになります。</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/38826672/" target="_blank">PubMed</a></td><td><a href="https://doi.org/10.1109/TNSRE.2021.3123964" target="_blank">DOI</a></td><td>U4 RQ3に「反事実テスト項目（do介入の期待差）」の欄を追加します。</td><td>担当: 解析WG。前提: 反事実課題設計。完了条件: 期待差と実測差の比較結果公開。</td></tr>
<tr><td>U4-4</td><td>失敗条件（falsification）を宣言しない因果同値は、運用上は検証不能です。</td><td><a href="https://doi.org/10.1016/j.neuroimage.2024.120954" target="_blank">DOI</a></td><td><a href="https://doi.org/10.1038/s41583-024-00881-3" target="_blank">DOI</a></td><td>U4 RQ4に「失敗宣言閾値（例: 因果辺再現率下限）」を数値で入れる欄を追加します。</td><td>担当: 検証WG。前提: 失敗時対応フロー承認。完了条件: 失敗ケース公開運用開始。</td></tr>
<tr><td>U8-1</td><td>遅延許容域は理論だけでなく、実運用のDBSデータで具体化できる段階です。</td><td><a href="https://doi.org/10.1038/s41591-024-03196-z" target="_blank">DOI</a></td><td><a href="https://doi.org/10.1093/brain/awad429" target="_blank">DOI</a></td><td>U8 RQ1に「遅延上限(ms)」と「安定マージン」を必須欄として追加します。</td><td>担当: 臨床/安全チーム。前提: 安全審査承認。完了条件: 遅延超過時の安全停止手順の承認。</td></tr>
<tr><td>U8-2</td><td>オンライン較正とドリフト対策は、長期運用報告で実用知見が増えています。</td><td><a href="https://doi.org/10.1038/s41531-025-01124-7" target="_blank">DOI</a></td><td><a href="https://doi.org/10.1038/s41531-024-00772-5" target="_blank">DOI</a></td><td>U8 RQ2に「再較正頻度」「ドリフト検出閾値」を追加します。</td><td>担当: 運用チーム。前提: 長期ログ収集基盤。完了条件: 再較正プロトコルv1公開。</td></tr>
<tr><td>U8-3</td><td>個体差・日内変動は大きく、単一セッション性能での評価は不十分です。</td><td><a href="https://doi.org/10.1001/jamaneurol.2025.2781" target="_blank">DOI</a></td><td><a href="https://doi.org/10.1038/s41582-025-01131-5" target="_blank">DOI</a></td><td>U8 RQ3に「日内変動係数」「個体内分散」を追加します。</td><td>担当: 解析WG。前提: 連続計測合意。完了条件: 個体差を含む安定性評価公開。</td></tr>
<tr><td>U8-4</td><td>異常検知とフェイルセーフは、臨床報告を運用契約へ翻訳する作業が残っています。</td><td><a href="https://doi.org/10.1080/17434440.2024.2438309" target="_blank">DOI</a></td><td><a href="https://doi.org/10.1038/s41551-025-01438-0" target="_blank">DOI</a></td><td>U8 RQ4に「異常検知再現率」「フェイルセーフ発動時間」を追加します。</td><td>担当: 安全委員会。前提: 失敗時責任分界の整理。完了条件: フェイルセーフ監査手順の承認。</td></tr>
<tr><td>U8-5</td><td>ヒューマンオーバーライドのKPIは、誤作動率と回復時間を対で管理するのが実務的です。</td><td><a href="https://doi.org/10.1101/2024.08.26.24312580" target="_blank">DOI</a></td><td><a href="https://doi.org/10.1038/s41591-024-03196-z" target="_blank">DOI</a></td><td>U8 RQ5に「オーバーライド発生率」「回復時間中央値」を追加します。</td><td>担当: 臨床運用チーム。前提: 現場運用手順合意。完了条件: KPIの定期報告開始。</td></tr>
<tr><td>U8-6</td><td>再学習頻度は「性能低下を抑える頻度」と「安全余裕を保つ頻度」の最小公倍数で決める必要があります。</td><td><a href="https://doi.org/10.1001/jamaneurol.2025.2781" target="_blank">DOI</a></td><td><a href="https://doi.org/10.1038/s41531-025-01124-7" target="_blank">DOI</a></td><td>U8 RQ6に「劣化速度」「再学習間隔候補」を追加し、トレードオフ評価欄を作成します。</td><td>担当: 解析/安全WG。前提: 長期フォローアップ体制。完了条件: 最適化方針の事前登録。</td></tr>
<tr><td>U10-1</td><td>Landauer下限は「理論上の最低コスト」で、脳やWBEの実装コストそのものではありません。混同を避ける必要があります。</td><td><a href="https://doi.org/10.3390/e26090779" target="_blank">DOI</a></td><td><a href="https://arxiv.org/abs/2502.03603" target="_blank">arXiv</a></td><td>U10 RQ1に「理論下限」と「実測コスト」を分けて記録する欄を追加します。</td><td>担当: 物理実験チーム。前提: 実測系の計測条件統一。完了条件: 下限値と実測値の比較表公開。</td></tr>
<tr><td>U10-2</td><td>非平衡指標（散逸・エントロピー生成）と意識/情報処理の関係は、相関は見え始めていますが因果は未確定です。</td><td><a href="https://doi.org/10.1103/PhysRevE.107.024121" target="_blank">DOI</a></td><td><a href="https://doi.org/10.1016/j.tics.2024.03.009" target="_blank">DOI</a></td><td>U10 RQ2に「相関」と「因果推定」を分離した評価欄を追加します。</td><td>担当: 解析WG。前提: 介入データ取得。完了条件: 因果方向を含む検証レポート公開。</td></tr>
<tr><td>U10-3</td><td>理論式を実験へ落とすには、神経活動と代謝を同時に取る観測設計が必要です。</td><td><a href="https://doi.org/10.1016/j.neubiorev.2023.105070" target="_blank">DOI</a></td><td><a href="https://doi.org/10.3390/e26090779" target="_blank">DOI</a></td><td>U10 RQ3に「同時計測（神経活動+代謝）」の必須チェックを追加します。</td><td>担当: 実験チーム。前提: 同時計測環境導入。完了条件: 再現可能な観測プロトコル公開。</td></tr>
<tr><td>U10-4</td><td>WBE計算コストは、計算時間やメモリだけでなく、熱散逸コストを同時に見ないと過小評価になります。</td><td><a href="https://doi.org/10.3390/e26090779" target="_blank">DOI</a></td><td><a href="https://arxiv.org/abs/2502.03603" target="_blank">arXiv</a></td><td>U10 RQ4に「計算コスト」と「熱コスト」の二層KPIを追加します。</td><td>担当: ガバナンス/実装WG。前提: コスト台帳設計。完了条件: 二層KPIでの定期評価開始。</td></tr>
<tr><td>U13-1</td><td>brain-to-textは「意味が合う」だけでは不十分で、内部過程が保存されているかを別に見る必要があります。</td><td><a href="https://doi.org/10.1038/s41593-023-01304-9" target="_blank">DOI</a></td><td><a href="https://doi.org/10.1016/j.celrep.2024.114924" target="_blank">DOI</a></td><td>U13 RQ1に「意味一致指標」と「因果一致指標」を分離して記録する欄を追加します。</td><td>担当: ML評価チーム。前提: 介入付きデコード課題の設計。完了条件: 二指標での公開比較レポート。</td></tr>
<tr><td>U13-2</td><td>LLMの幻覚検査を使うと、神経デコード出力の「見かけの整合」をチェックできますが、因果保存の代替にはなりません。</td><td><a href="https://arxiv.org/abs/2506.22486" target="_blank">arXiv</a></td><td><a href="https://doi.org/10.1609/aaai.v39i27.35124" target="_blank">DOI</a></td><td>U13 RQ2に「幻覚率」と「因果整合率」を同時監査する欄を追加します。</td><td>担当: ML評価チーム。前提: 幻覚判定器の導入。完了条件: 二軸監査の自動レポート化。</td></tr>
<tr><td>U13-3</td><td>同じ出力でも内部機構が違う問題には、表現分解と因果視点の評価が有効です。</td><td><a href="https://doi.org/10.1038/s42256-020-00257-z" target="_blank">DOI</a></td><td><a href="https://doi.org/10.1609/aaai.v39i27.35124" target="_blank">DOI</a></td><td>U13 RQ3に「shortcut兆候」チェック欄を追加します。</td><td>担当: 解析WG。前提: 介入/反事実評価基盤。完了条件: 同一出力・異機構ケースの検出率公開。</td></tr>
<tr><td>U13-4</td><td>模倣性能の上限を抑えるには、因果評価を最終判定に組み込む必要があります。</td><td><a href="https://doi.org/10.1609/aaai.v39i17.33998" target="_blank">DOI</a></td><td><a href="https://doi.org/10.1016/j.knosys.2025.113565" target="_blank">DOI</a></td><td>U13 RQ4に「模倣スコア単独では合格不可」の判定ルールを追加します。</td><td>担当: 評価設計WG。前提: 因果評価KPI合意。完了条件: 統一判定規約v1公開。</td></tr>
<tr><td>U13-5</td><td>知覚と想起で同一デコーダを使う場合、劣化の分岐点を取る比較実験が可能になってきています。</td><td><a href="https://doi.org/10.1109/EMBC58623.2025.11251641" target="_blank">DOI</a></td><td><a href="https://doi.org/10.1109/EMBC53108.2024.10782730" target="_blank">DOI</a></td><td>U13 RQ5に「知覚条件」「想起条件」の分離比較欄を追加します。</td><td>担当: 実験チーム。前提: 同一被験者での二条件計測。完了条件: 劣化分岐点レポート公開。</td></tr>
<tr><td>U13-6</td><td>プロンプト誘導・データリーク・shortcut学習は、対照条件を固定しないと分離検出できません。</td><td><a href="https://arxiv.org/abs/2506.22486" target="_blank">arXiv</a></td><td><a href="https://doi.org/10.1038/s42256-020-00257-z" target="_blank">DOI</a></td><td>U13 RQ6に「リーク検出率」「対照実験一致率」の欄を追加します。</td><td>担当: ML評価チーム。前提: 対照実験計画承認。完了条件: リーク分離検出の再現結果公開。</td></tr>
<tr><td>U14-1</td><td>データ/コード/環境の固定粒度を上げるほど再現性は上がりますが、運用コストも上がります。</td><td><a href="https://doi.org/10.1016/j.jneumeth.2023.109931" target="_blank">DOI</a></td><td><a href="https://doi.org/10.1038/s41597-024-03559-8" target="_blank">DOI</a></td><td>U14 RQ1に「固定する最小項目（データ/コード/環境）」チェック欄を追加します。</td><td>担当: 再現性WG。前提: コンテナ運用合意。完了条件: 最小固定セットの運用承認。</td></tr>
<tr><td>U14-2</td><td>探索研究と検証研究を運用で分離するには、事前登録と報告テンプレを分ける必要があります。</td><td><a href="https://doi.org/10.7554/eLife.85980" target="_blank">DOI</a></td><td><a href="https://doi.org/10.1001/jama.2025.13350" target="_blank">DOI</a></td><td>U14 RQ2に「探索」「検証」の報告テンプレ分離欄を追加します。</td><td>担当: 運用WG。前提: 事前登録運用の合意。完了条件: 二系統テンプレの正式運用。</td></tr>
<tr><td>U14-3</td><td>leaderboard監査では、データリークと過適合を分けて計測する必要があります。</td><td><a href="https://doi.org/10.1038/s41597-023-02614-0" target="_blank">DOI</a></td><td><a href="https://doi.org/10.1002/epi4.12704" target="_blank">DOI</a></td><td>U14 RQ3に「リーク検出率」「外部テスト乖離率」を追加します。</td><td>担当: ベンチ運用WG。前提: 外部評価データ確保。完了条件: 定期監査レポート公開。</td></tr>
<tr><td>U14-4</td><td>Model Card / Dataset Cardを評価契約に統合すると、再解析時の説明責任が上がります。</td><td><a href="https://bids-specification.readthedocs.io/en/stable/" target="_blank">Spec</a></td><td><a href="https://zenodo.org/records/18201723" target="_blank">Zenodo</a></td><td>U14 RQ4に「Model Card/Dataset Card提出有無」欄を追加します。</td><td>担当: データ公開WG。前提: 提出テンプレ承認。完了条件: 全公開案件で提出100%。</td></tr>
<tr><td>U14-5</td><td>再現失敗を否定例として蓄積しないと、同じ失敗が繰り返されます。</td><td><a href="https://doi.org/10.1016/j.jneumeth.2023.109931" target="_blank">DOI</a></td><td><a href="https://doi.org/10.7554/eLife.85980" target="_blank">DOI</a></td><td>U14 RQ5に「否定例レジストリID」欄を追加します。</td><td>担当: 再現性WG。前提: 失敗公開ポリシー。完了条件: 失敗レジストリ定期更新。</td></tr>
<tr><td>U14-6</td><td>コンテナ固定は再現性に有効ですが、計算資源・時間コストの上限を先に決める必要があります。</td><td><a href="https://arxiv.org/abs/2311.04912" target="_blank">arXiv</a></td><td><a href="https://doi.org/10.1038/s41597-024-03559-8" target="_blank">DOI</a></td><td>U14 RQ6に「再現コスト上限（時間/計算）」欄を追加します。</td><td>担当: インフラWG。前提: 予算上限設定。完了条件: コスト上限付き再現運用承認。</td></tr>
<tr><td>U15-1</td><td>神経データは通常の個人データより機微性が高く、法概念を明示して扱う必要があります。</td><td><a href="https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng" target="_blank">EU Law</a></td><td><a href="https://doi.org/10.1016/S1474-4422(25)00124-3" target="_blank">DOI</a></td><td>U15 RQ1に「法概念マッピング（個人/生体/神経）」欄を追加します。</td><td>担当: 法務WG。前提: 法域別定義整理。完了条件: 法概念対照表の承認。</td></tr>
<tr><td>U15-2</td><td>neurorightsは理念だけでなく、監査項目（ログ・説明責任・停止条件）に落とす必要があります。</td><td><a href="https://doi.org/10.1093/jhuman/huae042" target="_blank">DOI</a></td><td><a href="https://doi.org/10.6028/NIST.AI.600-1" target="_blank">DOI</a></td><td>U15 RQ2に「neurorights監査チェックリスト」欄を追加します。</td><td>担当: 監査WG。前提: チェック項目合意。完了条件: 監査票v1公開。</td></tr>
<tr><td>U15-3</td><td>法域差を跨ぐ最小共通運用は、EU法・国際原則・条約の共通部分を先に固定するのが現実的です。</td><td><a href="https://oecd.ai/en/ai-principles" target="_blank">OECD</a></td><td><a href="https://book.coe.int/en/texts-of-council-of-europe-treaties/12225-council-of-europe-framework-convention-on-artificial-intelligence-and-human-rights-democracy-and-the-rule-of-law-cets-no-225.html" target="_blank">CoE</a></td><td>U15 RQ3に「共通要件（最低運用）」欄を追加します。</td><td>担当: ガバナンス委員会。前提: 法域比較レビュー。完了条件: 最小共通運用仕様の承認。</td></tr>
<tr><td>U15-4</td><td>停止条件・更新条件は、制度文書と技術KPIをひも付けて初めて運用できます。</td><td><a href="https://www.iso.org/standard/42001" target="_blank">ISO</a></td><td><a href="https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng" target="_blank">EU Law</a></td><td>U15 RQ4に「停止トリガーKPI」「更新トリガーKPI」を追加します。</td><td>担当: ガバナンス委員会。前提: KPI閾値の合意。完了条件: 停止/更新運用の承認。</td></tr>
</tbody></table>
</section>

<section class="section" id="notes">
<h2 class="section-title">注記</h2>
<ul>
<li>Round 11 + Round 12 で、全60問いの問い別エビデンス割当が完了しました。</li>
<li>各行で外部依存タスクを分離し、担当・前提・完了条件を維持しています。</li>
</ul>
</section>

</article>
</main>
