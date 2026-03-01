---
layout: default
title: "50-Worker Research Harvest: 未解決問題を分解した文献地図"
description: "50分解クエスチョンで収集した先行研究を、解決済み領域と未解決領域に切り分けて公開。"
article_type: "Evidence Bank"
subtitle: "U0-U15 の分解、現状評価、先行研究（大量引用）"
author: Mind Uploading Research Project
last_updated: "2026-03-01"
note: "Compiled from 50 worker tasks (curated for relevance)"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>要旨</h2>
<p>本ページは、1つの大きな問いを50個の調査タスクへ分解して集めた先行研究を、未解決問題（U0-U15）に再配置したエビデンスバンクです。単なる提案ではなく、URL付き引用をベースに『今どこまで解けているか』と『何が未解決か』を分離して示します。</p>
</div>

<section class="section" id="stats">
<h2 class="section-title">収集と選別の統計</h2>
<ul>
<li><strong>Worker tasks:</strong> 50</li>
<li><strong>Raw citations:</strong> 499</li>
<li><strong>Curated citations:</strong> 302</li>
<li><strong>Dropped as noise/low-relevance:</strong> 97</li>
<li><strong>Unique citation keys:</strong> 292</li>
</ul>
</section>

<section class="section" id="quality-gate">
<h2 class="section-title">品質ゲート（混入防止）</h2>
<ol>
<li>U別キーワード一致 + 神経科学アンカー語を満たす文献のみ採用</li>
<li>無関係領域（宇宙論・腫瘍画像など）の混入を自動除外</li>
<li>重複（DOI/URL/タイトル）を統合し、スコア上位のみ残す</li>
<li>各Uに対して「解かれている範囲」と「未解決」を明示</li>
</ol>
</section>

<section class="section" id="recent-intake-2026-02">
<h2 class="section-title">最新追加入力（Issue #261–#263）</h2>
<p>
2026年2月23日に受領した内容追加Issue（#261–#263）に基づき、一次参照URLをエビデンスバンクへ登録しました。ここでは「受理済みリンク」と「学術統合前（要査読確認）」を分離して管理します。
</p>
<ol>
<li><strong>[Media]</strong> <a href="https://nazology.kusuguru.co.jp/archives/189938" target="_blank">AIに意識を宿すには「正しいコード」だけでは足りないかもしれない</a>（Issue #261）<br><span class="small">status=source_logged / 学術一次文献へのトレースを継続</span></li>
<li><strong>[Review]</strong> <a href="https://www.sciencedirect.com/science/article/pii/S0149763425005251?via%3Dihub" target="_blank">On biological and artificial consciousness: A case for biological computationalism</a>（Issue #262）<br><span class="small">status=source_logged / レビュー本文の精読要約は次回更新で実施</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2512.01591" target="_blank">Scaling and context steer LLMs along the same computational path as the human brain</a>（Issue #262）<br><span class="small">status=source_logged / WBE同一性検証への接続可能性を評価予定</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2305.19798" target="_blank">Primal-Attention: Self-attention through Asymmetric Kernel SVD in Primal Representation</a>（Issue #263）<br><span class="small">status=source_logged / 直接関連性（U0-U15）の再スクリーニング対象</span></li>
</ol>
<div class="note-box">
<strong>運用メモ</strong>
<p>
本節は「入力受理ログ」です。採否判定（Uマップ反映、引用優先度、ノイズ除外）は品質ゲート手順に従い、後続の定期更新で確定します。
</p>
</div>
</section>

<section class="section" id="u-overview">
<h2 class="section-title">U別の現状マップ</h2>
<table class="data-table">
<thead><tr><th>ID</th><th>問題名</th><th>現状</th><th>引用数</th><th>未解決の中心</th></tr></thead><tbody>
<tr><td>U0</td><td>操作的同一性</td><td>部分解決</td><td>23</td><td>介入実験を含む同一性評価ベンチは未標準化。</td></tr>
<tr><td>U1</td><td>逆問題同定可能性</td><td>部分解決</td><td>26</td><td>被験者間・装置間の不確実性を横断した一般化誤差境界が不足。</td></tr>
<tr><td>U3</td><td>生物学的境界</td><td>部分解決</td><td>26</td><td>どの粒度まで含めれば『同等な主体』と見なせるかの閾値が未確定。</td></tr>
<tr><td>U4</td><td>因果同値</td><td>部分解決</td><td>26</td><td>高次元時系列での因果識別可能性がデータ条件に強く依存。</td></tr>
<tr><td>U7</td><td>マルチモーダル整合</td><td>部分解決</td><td>26</td><td>同期誤差の許容域をタスク別に定義した共通規約が不足。</td></tr>
<tr><td>U8</td><td>閉ループ安定性</td><td>部分解決</td><td>26</td><td>長期運用でのドリフト耐性と再現性評価が不足。</td></tr>
<tr><td>U10</td><td>熱力学的一貫性</td><td>探索段階</td><td>26</td><td>神経回路実装における実効下限の実測研究が限定的。</td></tr>
<tr><td>U11</td><td>意識指標近似の妥当性</td><td>部分解決</td><td>26</td><td>理論間を同条件で比較する公開ベンチが不足。</td></tr>
<tr><td>U12</td><td>分岐本人性</td><td>探索段階</td><td>19</td><td>技術システムに直結する運用規約（監査・責任追跡）が未整備。</td></tr>
<tr><td>U13</td><td>模倣分離</td><td>部分解決</td><td>26</td><td>模倣と因果保存を同時評価する統一ベンチが不足。</td></tr>
<tr><td>U14</td><td>追試可能性</td><td>部分解決</td><td>26</td><td>神経科学×機械学習を跨ぐ共通監査規約が不十分。</td></tr>
<tr><td>U15</td><td>制度統合</td><td>探索段階</td><td>26</td><td>技術指標と法的停止基準を結びつけた実装規格が不足。</td></tr>
</tbody></table>
</section>

<section class="section" id="definitions">
<h2 class="section-title">未解決問題の厳密定義（U0-U15）</h2>
<table class="data-table">
<thead><tr><th>ID</th><th>厳密定義</th></tr></thead><tbody>
<tr><td>U0</td><td>介入集合 I と時間窓 T を固定したとき、生体系とモデル系の条件付き分布差 D(P_bio, P_model | I, T) をしきい値以下で規定できるか。</td></tr>
<tr><td>U1</td><td>観測 y から潜在源 x を推定する際、事後分布 p(x|y) の集中度・同定誤差境界・条件数を同時に報告できるか。</td></tr>
<tr><td>U3</td><td>主体モデルに含める最小構成要素（ニューロン、グリア、neuromodulator、身体・環境ループ）を、予測性能低下で境界決定できるか。</td></tr>
<tr><td>U4</td><td>観測一致ではなく介入分岐（counterfactual / do-intervention）で、生体系とモデル系の因果機構一致を判定できるか。</td></tr>
<tr><td>U7</td><td>EEG/fMRI/行動/生理の時刻系・空間系・前処理ログを監査可能に固定し、再解析で同一結論へ到達できるか。</td></tr>
<tr><td>U8</td><td>遅延・ジッタ・ノイズ・ドリフト下で、閉ループ神経制御が安全制約を破らず安定に動作するか。</td></tr>
<tr><td>U10</td><td>情報処理の不可逆性・散逸・エネルギー下限を神経計算モデルへ写像し、測定可能な反証条件を置けるか。</td></tr>
<tr><td>U11</td><td>IIT/PCI/GWT等の指標が、どの条件で一致し、どの条件で乖離するかをデータ駆動で比較可能にする。</td></tr>
<tr><td>U12</td><td>複製・分岐後に発生する複数主体の同一性・責任・権利帰属を、技術評価と整合する形式で規定できるか。</td></tr>
<tr><td>U13</td><td>高性能模倣（言語/行動出力）と、内部因果構造保存を識別する評価軸を実験的に分離できるか。</td></tr>
<tr><td>U14</td><td>第三者が同一データ・同一手順・同一評価契約で同等結論に到達できる公開運用を常時維持できるか。</td></tr>
<tr><td>U15</td><td>技術評価KPIと法/倫理KPIを連動させ、停止基準と公開基準を運用レベルで定義できるか。</td></tr>
</tbody></table>
</section>

<section class="section" id="issue-rq-audit-20260224">
<h2 class="section-title">Issue反映とRQ監査（2026-02-24）</h2>
<p>GitHub Issue #264/#265 を取り込み、各Uセクションのリサーチクエスチョン件数と多様性を点検しました。重複が出やすい領域（U3/U7/U8/U12/U13/U14）は、評価軸を分離してクエスチョンを増補しています。</p>

<h3>Issue取り込み（完了）</h3>
<table class="data-table">
<thead><tr><th>Issue</th><th>入力ソース</th><th>反映先</th><th>状態</th></tr></thead><tbody>
<tr><td>#264</td><td>Neuron URL (PII: S0896-6273(25)00843-8)</td><td>U3 主要先行研究（DOI: 10.1016/j.neuron.2025.10.036）</td><td>反映済み</td></tr>
<tr><td>#265</td><td>Neuroscience News URL</td><td>U13 主要先行研究（一次研究 DOI: 10.1126/sciadv.adw1464 を併記）</td><td>反映済み</td></tr>
</tbody></table>

<h3>RQ件数と多様性評価</h3>
<table class="data-table">
<thead><tr><th>U</th><th>更新前RQ数</th><th>更新後RQ数</th><th>多様性評価</th></tr></thead><tbody>
<tr><td>U0</td><td>4</td><td>4</td><td>高（定義・閾値・分岐を分離）</td></tr>
<tr><td>U1</td><td>4</td><td>4</td><td>中（推定不確実性中心）</td></tr>
<tr><td>U3</td><td>4</td><td>6</td><td>中（構造/体液/免疫へ軸拡張）</td></tr>
<tr><td>U4</td><td>4</td><td>4</td><td>高（識別・介入・反証を分離）</td></tr>
<tr><td>U7</td><td>4</td><td>6</td><td>中（同期・QC・欠損耐性へ拡張）</td></tr>
<tr><td>U8</td><td>4</td><td>6</td><td>高（安定性・安全性・運用回復を分離）</td></tr>
<tr><td>U10</td><td>4</td><td>4</td><td>高（理論・観測・コストを分離）</td></tr>
<tr><td>U11</td><td>4</td><td>4</td><td>高（理論比較・計算量・失敗条件を分離）</td></tr>
<tr><td>U12</td><td>4</td><td>6</td><td>高（法的帰属・同意運用を追加）</td></tr>
<tr><td>U13</td><td>4</td><td>6</td><td>中（復元精度・リーク検出軸を追加）</td></tr>
<tr><td>U14</td><td>4</td><td>6</td><td>中（否定例公開・再現コスト軸を追加）</td></tr>
<tr><td>U15</td><td>4</td><td>4</td><td>高（法概念・監査・停止基準を分離）</td></tr>
<tr><td><strong>合計</strong></td><td><strong>48</strong></td><td><strong>60</strong></td><td>重複クラスタを分散済み</td></tr>
</tbody></table>

<div class="note-box">
<strong>重複処理ルール（今回適用）</strong>
<ul>
<li>同一テーマでも「測定」「因果」「運用」の評価軸を分離して別クエスチョン化。</li>
<li>文献は一次研究を優先し、ニュース記事は一次研究リンク付きの補助参照として保持。</li>
<li>低関連・重複傾向の文献を差し替え、各Uの文献件数は維持。</li>
</ul>
</div>
</section>

<section class="section" id="literature-refresh-20260224b">
<h2 class="section-title">追加文献探索（2026-02-24 第2便）</h2>
<p>2024-2026の一次文献を再探索し、関連性が高い DOI を各Uの根拠例へ追補しました。今回の追補は「理論更新」「実装更新」「監査規約更新」の3軸で選定しています。</p>
<table class="data-table">
<thead><tr><th>U</th><th>追補DOI</th><th>要点</th></tr></thead><tbody>
<tr><td>U1</td><td><a href="https://doi.org/10.1109/JSEN.2024.3502917" target="_blank">10.1109/JSEN.2024.3502917</a></td><td>M/EEG逆問題の2025レビュー</td></tr>
<tr><td>U4</td><td><a href="https://doi.org/10.1109/TBME.2024.3423803" target="_blank">10.1109/TBME.2024.3423803</a></td><td>発達過程の動的有効結合を因果モデル化</td></tr>
<tr><td>U7</td><td><a href="https://doi.org/10.1038/s41597-024-03559-8" target="_blank">10.1038/s41597-024-03559-8</a></td><td>Motion-BIDSによる再現可能な運動データ整理</td></tr>
<tr><td>U8</td><td><a href="https://doi.org/10.1088/1741-2552/adbb20" target="_blank">10.1088/1741-2552/adbb20</a></td><td>閉ループBCI実験基盤のモジュール化</td></tr>
<tr><td>U10</td><td><a href="https://doi.org/10.1016/j.tics.2024.03.009" target="_blank">10.1016/j.tics.2024.03.009</a></td><td>心的過程と熱力学の接続レビュー</td></tr>
<tr><td>U11</td><td><a href="https://doi.org/10.1038/s41586-025-08888-1" target="_blank">10.1038/s41586-025-08888-1</a></td><td>GNWとIITの敵対的検証</td></tr>
<tr><td>U12</td><td><a href="https://doi.org/10.20318/universitas.2025.9574" target="_blank">10.20318/universitas.2025.9574</a></td><td>神経権利の欧州・中南米比較規制</td></tr>
<tr><td>U13</td><td><a href="https://doi.org/10.1088/1741-2552/adfab1" target="_blank">10.1088/1741-2552/adfab1</a></td><td>LLM併用のbrain-to-text最新報告</td></tr>
<tr><td>U14</td><td><a href="https://doi.org/10.1098/rsos.242057" target="_blank">10.1098/rsos.242057</a></td><td>再現性向上介入のスコーピングレビュー</td></tr>
<tr><td>U15</td><td><a href="https://doi.org/10.1007/s11673-025-10440-9" target="_blank">10.1007/s11673-025-10440-9</a></td><td>神経技術の責任ある倫理ガバナンス戦略</td></tr>
</tbody></table>
</section>

<section class="section" id="deepening-integration-20260301">
<h2 class="section-title">深掘り統合反映（2026-03-01）</h2>
<p>
Round 1〜8 で実施した深掘り結果を本体運用へ統合しました。ここでは「どのUがどこまで深掘り済みか」を一覧化し、詳細は各Round文書へリンクします。
</p>
<table class="data-table">
<thead><tr><th>U</th><th>RQ総数</th><th>深掘り完了</th><th>主要反映ラウンド</th></tr></thead><tbody>
<tr><td>U0</td><td>4</td><td>4</td><td>Round 2</td></tr>
<tr><td>U1</td><td>4</td><td>4</td><td>Round 2</td></tr>
<tr><td>U3</td><td>6</td><td>6</td><td>Round 2</td></tr>
<tr><td>U4</td><td>4</td><td>4</td><td>Round 3</td></tr>
<tr><td>U7</td><td>6</td><td>6</td><td>Round 3</td></tr>
<tr><td>U8</td><td>6</td><td>6</td><td>Round 4</td></tr>
<tr><td>U10</td><td>4</td><td>4</td><td>Round 5</td></tr>
<tr><td>U11</td><td>4</td><td>4</td><td>Round 5</td></tr>
<tr><td>U12</td><td>6</td><td>6</td><td>Round 5</td></tr>
<tr><td>U13</td><td>6</td><td>6</td><td>Round 6</td></tr>
<tr><td>U14</td><td>6</td><td>6</td><td>Round 6</td></tr>
<tr><td>U15</td><td>4</td><td>4</td><td>Round 6</td></tr>
<tr><td><strong>合計</strong></td><td><strong>60</strong></td><td><strong>60</strong></td><td><strong>Round 1-8</strong></td></tr>
</tbody></table>

<h3>詳細ドキュメント</h3>
<ul>
<li><a href="research_deepening_2026-03-01.html">Round 1: 全Uの平易化追補</a></li>
<li><a href="research_deepening_round2_2026-03-01.html">Round 2: U0/U1/U3</a></li>
<li><a href="research_deepening_round3_2026-03-01.html">Round 3: U4/U7</a></li>
<li><a href="research_deepening_round4_2026-03-01.html">Round 4: U8</a></li>
<li><a href="research_deepening_round5_2026-03-01.html">Round 5: U10/U11/U12</a></li>
<li><a href="research_deepening_round6_2026-03-01.html">Round 6: U13/U14/U15</a></li>
<li><a href="research_deepening_round7_2026-03-01.html">Round 7: U8/U13/U14/U15 参照精査</a></li>
<li><a href="research_deepening_round8_2026-03-01.html">Round 8: U8/U13/U14/U15 参照置換の本体反映</a></li>
</ul>

<h3>整合性監査（証跡）</h3>
<p class="small">
全60問いのカバレッジ監査は
<a href="automation/rq_deepening_consistency_audit_2026-03-01.md" target="_blank">rq_deepening_consistency_audit_2026-03-01.md</a>
に記録しています（missing=0）。
</p>
<p class="small">
U別カバレッジ集計は
<a href="automation/rq_deepening_coverage_summary_2026-03-01.csv" target="_blank">rq_deepening_coverage_summary_2026-03-01.csv</a>、
引用関連性の機械点検（要目視確認）は
<a href="automation/rq_reference_relevance_audit_2026-03-01.md" target="_blank">rq_reference_relevance_audit_2026-03-01.md</a>
に記録しています。
</p>
<p class="small">
U8/U13/U14/U15 の手動トリアージ（維持・要置換・要確認）は
<a href="automation/rq_reference_manual_triage_round7_2026-03-01.csv" target="_blank">rq_reference_manual_triage_round7_2026-03-01.csv</a>
に記録しています。
</p>
<p class="small">
Round 8 の実置換ログ（置換前後件数と反映先）は
<a href="automation/rq_reference_replacement_applied_round8_2026-03-01.csv" target="_blank">rq_reference_replacement_applied_round8_2026-03-01.csv</a>
に記録しています。
</p>
</section>

<section class="section" id="u0">
<h2 class="section-title">U0: 操作的同一性</h2>
<p><strong>厳密定義:</strong> 介入集合 I と時間窓 T を固定したとき、生体系とモデル系の条件付き分布差 D(P_bio, P_model | I, T) をしきい値以下で規定できるか。</p>
<h3>リサーチクエスチョン分解</h3>
<ol>
<li>同一性判定を『観測一致』と『介入応答一致』に分離したとき、どちらを必要条件・十分条件に置くか。</li>
<li>時間同期（ms単位）と状態表現（行動・神経活動・生理）の対応をどう固定するか。</li>
<li>同一性判定の閾値をタスク別にどう設定し、過学習モデルをどう除外するか。</li>
<li>分岐/複製ケースでの『同一個体』定義をどの評価軸に帰着させるか。</li>
</ol>
<h3>今、解かれているもの（文献で積み上がっている領域）</h3>
<ul>
<li>心理的連続性・情報的連続性・機能的同値を区別する議論枠組みは文献上で整理済み。</li>
<li>段階置換とscan-and-copyの比較で、手続き差が同一性の十分条件にならないという反論は蓄積済み。</li>
<li>同一性を単一の形而上学命題でなく、操作的判定問題に変換する方向性は共有されている。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.7551/mitpress/10366.003.0009" target="_blank">Continuity: Kinks Not Breaks</a>、<a href="https://doi.org/10.1093/acprof:oso/9780198754855.003.0013" target="_blank">Enhancement, Mind-Uploading, and Personal Identity</a>、<a href="https://doi.org/10.31219/osf.io/zw3v4" target="_blank">The Fallacy of Favoring Gradual Replacement Mind Uploading Over Scan-and-Copy</a>。</p>
<h3>これから研究が必要なもの（未解決）</h3>
<ul>
<li>介入実験を含む同一性評価ベンチは未標準化。</li>
<li>長期ドリフトを含む同一性維持（週〜月スケール）の定量指標が未確立。</li>
<li>分岐後主体の責任帰属と評価帰属を技術評価へ接続する規約が不足。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.7551/mitpress/10058.003.0005" target="_blank">Whole Brain Emulation</a>、<a href="https://arxiv.org/abs/2510.15745v3" target="_blank">State of Brain Emulation Report 2025</a>、<a href="https://doi.org/10.1017/9781009486309.002" target="_blank">The Right to Personal Identity</a>。</p>
<h3>主要先行研究（厳選 23 件）</h3>
<ol>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1017/9781009486309.002" target="_blank">The Right to Personal Identity</a> (2026)<br><span class="small">worker=04 / Minds, Freedoms and Rights</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.31219/osf.io/zw3v4" target="_blank">The Fallacy of Favoring Gradual Replacement Mind Uploading Over Scan-and-Copy</a> (2023)<br><span class="small">worker=03 / </span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/1504.06320v4" target="_blank">The Fallacy of Favoring Gradual Replacement Mind Uploading Over Scan-and-Copy</a> (2015-04-23T14:09:50Z)<br><span class="small">worker=02 / Mind uploading speculation and debate often concludes that a procedure described as gradual in-place replacement preserves personal identity while a procedure described as destruct</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.2139/ssrn.2596460" target="_blank">The Fallacy of Favoring Gradual Replacement Mind Uploading Over Scan-and-Copy</a> (2015)<br><span class="small">worker=03 / SSRN Electronic Journal</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2412.07853v1" target="_blank">Probing the gas that builds planets: Results from the JWST MINDS program</a> (2024-12-10T19:01:14Z)<br><span class="small">worker=04 / Infrared observations with JWST open up a new window into the chemical composition of the gas in the inner disk (<few au) where planets are built. Results from the MIRI GTO program</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1017/9781009367059.009" target="_blank">Personal Ontology and Life after Death, Part 2: Mind Uploading</a> (2024)<br><span class="small">worker=02 / Personal Ontology</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/1811.06825v3" target="_blank">Towards a Science of Mind</a> (2018-11-06T18:02:40Z)<br><span class="small">worker=02 / The ancient mind/body problem continues to be one of deepest mysteries of science and of the human spirit. Despite major advances in many fields, there is still no plausible link b</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.7551/mitpress/10366.003.0009" target="_blank">Continuity: Kinks Not Breaks</a> (2017)<br><span class="small">worker=04 / Evolving Enactivism</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1093/acprof:oso/9780198754855.003.0013" target="_blank">Enhancement, Mind-Uploading, and Personal Identity</a> (2016)<br><span class="small">worker=02 / The Ethics of Human Enhancement</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/1305.3227v2" target="_blank">A study on ideal ward continuity</a> (2013-05-11T11:33:20Z)<br><span class="small">worker=02 / In this paper, we prove that any ideal ward continuous function is uniformly continuous either on an interval or on an ideal ward compact subset of $\textbf{R}$. A characterization</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/0710.2556v1" target="_blank">Continuum of consciousness: Mind uploading and resurrection of human consciousness. Is there a place for physics, neuroscience and computers?</a> (2007-10-12T21:39:25Z)<br><span class="small">worker=02 / In this paper, I perform mental experiment to analyze hypothetical process of mind uploading. That process suggested as a way to achieve resurrection of human consciousness. Mind u</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/cs/0508065v1" target="_blank">Representing Digital Assets using MPEG-21 Digital Item Declaration</a> (2005-08-13T03:09:25Z)<br><span class="small">worker=04 / Various XML-based approaches aimed at representing compound digital assets have emerged over the last several years. Approaches that are of specific relevance to the digital librar</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1007/978-94-015-8510-1_6" target="_blank">Criteria and Other Minds</a> (1995)<br><span class="small">worker=04 / Other Minds</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.46569/20.500.12680/5m60qz836" target="_blank">Ethics of Mind Uploading: Personal Identity</a> (None)<br><span class="small">worker=02 / </span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2510.15745v3" target="_blank">State of Brain Emulation Report 2025</a> (2025-10-17T15:33:28Z)<br><span class="small">worker=01 / The State of Brain Emulation Report 2025 provides a comprehensive reassessment of the field's progress since Sandberg and Bostrom's 2008 Whole Brain Emulation roadmap. The report i</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.24917/20841043.13.1.02" target="_blank">Does whole brain emulation entail the emulation of mental disorders?</a> (2023)<br><span class="small">worker=01 / Argument: Biannual Philosophical Journal</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2011.14731v4" target="_blank">Spatiotemporal patterns of adaptation-induced slow oscillations in a whole-brain model of slow-wave sleep</a> (2020-11-30T12:18:12Z)<br><span class="small">worker=01 / During slow-wave sleep, the brain is in a self-organized regime in which slow oscillations (SOs) between up- and down-states travel across the cortex. While an isolated piece of co</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W2803174641" target="_blank">Transfer of Personality to Synthetic Human ("mind uploading") and the Social Construction of Identity</a> (2017)<br><span class="small">worker=02 / </span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W4319986951" target="_blank">Metaverse for Healthcare: A Survey on Potential Applications, Challenges and Future Directions</a> (2023)<br><span class="small">worker=01 / IEEE Access</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W4290998746" target="_blank">The Metaverse as a virtual form of data-driven smart urbanism: platformization and its underlying processes, institutional dimensions, and disruptive impacts</a> (2022)<br><span class="small">worker=01 / Computational Urban Science</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.7551/mitpress/10058.003.0005" target="_blank">Whole Brain Emulation</a> (2015)<br><span class="small">worker=01 / The Technological Singularity</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1007/978-94-009-2707-0_8" target="_blank">Whole-Brain, Neocortical, and Higher Brain Related Concepts</a> (1988)<br><span class="small">worker=01 / Philosophy and Medicine</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W2017561954" target="_blank">Artificial General Intelligence: Concept, State of the Art, and Future Prospects</a> (2014)<br><span class="small">worker=01 / Journal of Artificial General Intelligence</span></li>
</ol>
</section>

<section class="section" id="u1">
<h2 class="section-title">U1: 逆問題同定可能性</h2>
<p><strong>厳密定義:</strong> 観測 y から潜在源 x を推定する際、事後分布 p(x|y) の集中度・同定誤差境界・条件数を同時に報告できるか。</p>
<h3>リサーチクエスチョン分解</h3>
<ol>
<li>EEG/MEG逆問題での不良設定性を、どの事前分布で制御するか。</li>
<li>頭蓋導電率・電極配置・ノイズ構造の不確実性を、推定不確実性へどう伝播させるか。</li>
<li>同じデータで異なる逆解法（MNE, beamformer, Champagne 等）が乖離した場合の判定規則をどう置くか。</li>
<li>推定値だけでなく、信頼区間/後方分布を公開基準に含めるか。</li>
</ol>
<h3>今、解かれているもの（文献で積み上がっている領域）</h3>
<ul>
<li>Bayesian EEG/MEG source imaging と sparse prior による逆問題安定化は方法論として確立。</li>
<li>頭部導電率不確実性が逆解精度を大きく左右する点は多数研究で再現。</li>
<li>Champagne系のspatio-temporal SBLは実データ評価を含む報告が蓄積。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.1007/978-3-319-14947-9_4" target="_blank">Sparse Bayesian (Champagne) Algorithm</a>、<a href="https://doi.org/10.1109/sampta64769.2025.11133512" target="_blank">Revisiting CHAMPAGNE</a>、<a href="https://doi.org/10.1109/JSEN.2024.3502917" target="_blank">Inverse Problem for M/EEG Source Localization: A Review</a>、<a href="https://arxiv.org/abs/1810.04410v2" target="_blank">Fast Approximation of EEG Forward Problem and Application to Tissue Conductivity Estimation</a>。</p>
<h3>これから研究が必要なもの（未解決）</h3>
<ul>
<li>被験者間・装置間の不確実性を横断した一般化誤差境界が不足。</li>
<li>逆問題の識別可能性をタスク依存で比較する統一ベンチが不足。</li>
<li>因果介入評価に接続できる逆問題の品質指標が未整備。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.1137/1.9781611977844.ch7" target="_blank">Parameter Identifiability and Influence</a>、<a href="https://doi.org/10.1007/978-3-030-74918-7" target="_blank">EEG/MEG Source Reconstruction</a>、<a href="https://arxiv.org/abs/2209.11233v2" target="_blank">Evaluating Latent Space Robustness and Uncertainty of EEG-ML Models</a>。</p>
<h3>主要先行研究（厳選 26 件）</h3>
<ol>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2506.20534v1" target="_blank">Revisiting CHAMPAGNE: Sparse Bayesian Learning as Reweighted Sparse Coding</a> (2025-06-25T15:24:38Z)<br><span class="small">worker=08 / This paper revisits the CHAMPAGNE algorithm within the Sparse Bayesian Learning (SBL) framework and establishes its connection to reweighted sparse coding. We demonstrate that the </span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/1810.11212v2" target="_blank">Third Generation MEEG Source Connectivity Analysis Toolbox (BC-VARETA 1.0) and Validation Benchmark</a> (2018-10-26T07:47:04Z)<br><span class="small">worker=07 / This paper presents a new toolbox for MEEG source activity and connectivity estimation: Brain Connectivity Variable Resolution Tomographic Analysis version 1.0 (BC-VARETA 1.0). It </span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1109/sampta64769.2025.11133512" target="_blank">Revisiting CHAMPAGNE: Sparse Bayesian Learning as Reweighted Sparse Coding</a> (2025)<br><span class="small">worker=08 / 2025 International Conference on Sampling Theory and Applications (SampTA)</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2405.18765v1" target="_blank">Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI</a> (2024-05-29T05:08:16Z)<br><span class="small">worker=08 / The current electroencephalogram (EEG) based deep learning models are typically designed for specific datasets and applications in brain-computer interaction (BCI), limiting the sc</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2303.09713v2" target="_blank">CHAMPAGNE: Learning Real-world Conversation from Large-Scale Web Videos</a> (2023-03-17T01:10:33Z)<br><span class="small">worker=08 / Visual information is central to conversation: body gestures and physical behaviour, for example, contribute to meaning that transcends words alone. To date, however, most neural c</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2108.06446v1" target="_blank">A fast asynchronous MCMC sampler for sparse Bayesian inference</a> (2021-08-14T02:20:49Z)<br><span class="small">worker=08 / We propose a very fast approximate Markov Chain Monte Carlo (MCMC) sampling framework that is applicable to a large class of sparse Bayesian inference problems, where the computati</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/1810.00786v2" target="_blank">Caulking the Leakage Effect in MEEG Source Connectivity Analysis</a> (2018-09-28T12:19:05Z)<br><span class="small">worker=07 / Simplistic estimation of neural connectivity in MEEG sensor space is impossible due to volume conduction. The only viable alternative is to carry out connectivity estimation in sou</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W2049372174" target="_blank">MEG/EEG Source Reconstruction, Statistical Evaluation, and Visualization with NUTMEG</a> (2011)<br><span class="small">worker=08 / Computational Intelligence and Neuroscience</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1007/978-3-319-14947-9_4" target="_blank">Sparse Bayesian (Champagne) Algorithm</a> (2015)<br><span class="small">worker=08 / Electromagnetic Brain Imaging</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1109/tpami.2023.3299568/mm1" target="_blank">Sparse Bayesian Learning for End-to-End EEG Decoding_supp1-3299568.pdf</a> (None)<br><span class="small">worker=08 / </span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2508.15406v1" target="_blank">Conditional Stability and Numerical Reconstruction of a Parabolic Inverse Source Problem Using Carleman Estimates</a> (2025-08-21T09:54:50Z)<br><span class="small">worker=06 / In this work we develop a new numerical approach for recovering a spatially dependent source component in a standard parabolic equation from partial interior measurements. We estab</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1137/1.9781611977844.ch7" target="_blank">Chapter 7: Parameter Identifiability and Influence</a> (2024)<br><span class="small">worker=07 / Uncertainty Quantification: Theory, Implementation, and Applications, Second Edition</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2310.11902v3" target="_blank">Operation and performance of MEG II detector</a> (2023-10-18T11:41:43Z)<br><span class="small">worker=10 / The MEG II experiment, located at the Paul Scherrer Institut (PSI) in Switzerland, is the successor to the MEG experiment, which completed data taking in 2013. MEG II started fully</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2306.03910v2" target="_blank">Heat Source Determining Inverse Problem for non-local in time equation</a> (2023-06-06T09:53:29Z)<br><span class="small">worker=06 / In this paper, we consider the inverse problem of determining the time-dependent source term in the general setting of Hilbert spaces and for general additional data. We prove the </span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2209.11233v2" target="_blank">Evaluating Latent Space Robustness and Uncertainty of EEG-ML Models under Realistic Distribution Shifts</a> (2022-09-22T19:26:09Z)<br><span class="small">worker=09 / The recent availability of large datasets in bio-medicine has inspired the development of representation learning methods for multiple healthcare applications. Despite advances in </span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1007/978-3-030-74918-7_4" target="_blank">Source Models</a> (2022)<br><span class="small">worker=10 / EEG/MEG Source Reconstruction</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.31234/osf.io/xwmyk" target="_blank">An open-source EEGLAB plugin for computing entropy-based measures on MEEG signals</a> (2022)<br><span class="small">worker=07 / </span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1007/978-3-030-74918-7" target="_blank">EEG/MEG Source Reconstruction</a> (2022)<br><span class="small">worker=10 / </span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2101.11935v1" target="_blank">A Machine Learning Challenge for Prognostic Modelling in Head and Neck Cancer Using Multi-modal Data</a> (2021-01-28T11:20:34Z)<br><span class="small">worker=09 / Accurate prognosis for an individual patient is a key component of precision oncology. Recent advances in machine learning have enabled the development of models using a wider rang</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/1906.04732v3" target="_blank">Convergence analysis of a Crank-Nicolson Galerkin method for an inverse source problem for parabolic equations with boundary observations</a> (2019-06-10T17:20:48Z)<br><span class="small">worker=06 / This work is devoted to an inverse problem of identifying a source term depending on both spatial and time variables in a parabolic equation from single Cauchy data on a part of th</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/1810.04410v2" target="_blank">Fast Approximation of EEG Forward Problem and Application to Tissue Conductivity Estimation</a> (2018-10-10T08:17:17Z)<br><span class="small">worker=09 / Bioelectric source analysis in the human brain from scalp electroencephalography (EEG) signals is sensitive to the conductivity of the different head tissues. Conductivity values a</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W2903531101" target="_blank">Improving EEG Source Localization Through Spatio-Temporal Sparse Bayesian Learning</a> (2018)<br><span class="small">worker=08 / </span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/1712.02997v2" target="_blank">MV-PURE Spatial Filters with Application to EEG/MEG Source Reconstruction</a> (2017-12-08T09:40:24Z)<br><span class="small">worker=10 / In this paper we propose spatial filters for a linear regression model which are based on the minimum-variance pseudo-unbiased reduced-rank estimation (MV-PURE) framework. As a sam</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1201/9781315156415-7" target="_blank">EEG inverse problem III</a> (2017)<br><span class="small">worker=06 / Brain Source Localization Using EEG Signal Analysis</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1201/9781315156415-8" target="_blank">EEG inverse problem IV</a> (2017)<br><span class="small">worker=06 / Brain Source Localization Using EEG Signal Analysis</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/1605.05081v3" target="_blank">Search for the Lepton Flavour Violating Decay $μ^{+} \to e^+ γ$ with the Full Dataset of the MEG Experiment</a> (2016-05-17T09:52:20Z)<br><span class="small">worker=10 / The final results of the search for the lepton flavour violating decay $μ^{+} \rightarrow {\rm e^{+}} γ$ based on the full dataset collected by the MEG experiment at the Paul Scher</span></li>
</ol>
</section>

<section class="section" id="u3">
<h2 class="section-title">U3: 生物学的境界</h2>
<p><strong>厳密定義:</strong> 主体モデルに含める最小構成要素（ニューロン、グリア、neuromodulator、身体・環境ループ）を、予測性能低下で境界決定できるか。</p>
<h3>リサーチクエスチョン分解</h3>
<ol>
<li>ニューロン中心モデルに対して、グリア/体液性調節を追加した際の予測改善量をどう測るか。</li>
<li>connectome完全性と機能予測性能の関係を、種横断でどう比較するか。</li>
<li>身体・環境結合を除去したモデルで失われる機能をどう定量化するか。</li>
<li>『必要最小構成』の判定を理論的主張ではなくデータでどう固定するか。</li>
<li>glymphatic/meningeal lymphatic 系を含むとき、予測精度と説明可能性はどの程度改善するか。</li>
<li>免疫監視（髄膜免疫・炎症性シグナル）を除外したモデルは、どの時点で長期予測が破綻するか。</li>
</ol>
<h3>今、解かれているもの（文献で積み上がっている領域）</h3>
<ul>
<li>C. elegans・Drosophila・マウスでconnectome再構成が進み、構造側の基盤は急速に整備。</li>
<li>astrocyte-neuron相互作用やneuromodulatory volume transmissionの機能的寄与は実験報告が増加。</li>
<li>embodied cognitionは脳単体モデルの限界を示す理論・実証が蓄積。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.1101/146035" target="_blank">The Emergent Connectome in C. elegans Embryogenesis</a>、<a href="https://doi.org/10.5220/0005190601840188" target="_blank">Towards an Electro-optical Emulation of the C. elegans Connectome</a>、<a href="https://doi.org/10.1007/978-3-031-64839-7_12" target="_blank">Astrocyte-Neuron Interactions Contributing to ALS Progression</a>、<a href="https://doi.org/10.1101/174276" target="_blank">Rhythms of the Body, Rhythms of the Brain</a>。</p>
<h3>これから研究が必要なもの（未解決）</h3>
<ul>
<li>どの粒度まで含めれば『同等な主体』と見なせるかの閾値が未確定。</li>
<li>構造データと機能ダイナミクスを統合する計算コストが依然高い。</li>
<li>神経外要素（体内環境、ホルモン、免疫）を含む可搬な評価系が不足。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.1016/j.neuron.2025.10.036" target="_blank">Resolving the mysteries of brain clearance and immune surveillance</a>、<a href="https://doi.org/10.3390/neuroglia5010001" target="_blank">Contribution of Small Extracellular Vesicles from Glial Cells to Pain Processing</a>、<a href="https://arxiv.org/abs/1801.04819v3" target="_blank">Robots as Powerful Allies for the Study of Embodied Cognition</a>。</p>
<h3>主要先行研究（厳選 26 件）</h3>
<ol>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1016/b978-0-443-22335-8.00010-3" target="_blank">Role of cellular redox in organismal biology: Lessons from C. elegans, zebrafish, Drosophila, and mouse</a> (2026)<br><span class="small">worker=13 / Fundamentals of Redox Biology</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1101/146035" target="_blank">The Emergent Connectome in <i>Caenorhabditis elegans</i> Embryogenesis</a> (2017)<br><span class="small">worker=13 / </span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1016/j.neuron.2025.10.036" target="_blank">Resolving the mysteries of brain clearance and immune surveillance.</a> (2025)<br><span class="small">issue=264 / Neuron (PMID: 41289996, PII: S0896-6273(25)00843-8)</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.5220/0005190601840188" target="_blank">Towards an Electro-optical Emulation of the C. elegans Connectome</a> (2014)<br><span class="small">worker=13 / Proceedings of the 2nd International Congress on Neurotechnology, Electronics and Informatics</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2508.14160v2" target="_blank">RynnEC: Bringing MLLMs into Embodied World</a> (2025-08-19T18:00:01Z)<br><span class="small">worker=14 / We introduce RynnEC, a video multimodal large language model designed for embodied cognition. Built upon a general-purpose vision-language foundation model, RynnEC incorporates a r</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2311.08135v2" target="_blank">Neuron-Astrocyte Associative Memory</a> (2023-11-14T13:01:50Z)<br><span class="small">worker=11 / Astrocytes, the most abundant type of glial cell, play a fundamental role in memory. Despite most hippocampal synapses being contacted by an astrocyte, there are no current theorie</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2204.10847v1" target="_blank">Controlling the spontaneous firing behavior of a neuron with astrocyte</a> (2022-04-22T17:53:34Z)<br><span class="small">worker=11 / Mounting evidence in recent years suggests that astrocytes, a sub-type of glial cells, not only serve metabolic and structural support for neurons and synapses but also play critic</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.4324/9781003106401-20" target="_blank">Dance expertise, embodied cognition, and the body in the brain</a> (2022)<br><span class="small">worker=14 / Dance Data, Cognition, and Multimodal Communication</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W3043135743" target="_blank">Reporting animal research: Explanation and elaboration for the ARRIVE guidelines 2.0</a> (2020)<br><span class="small">worker=13 / PLoS Biology</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/1801.04819v3" target="_blank">Robots as Powerful Allies for the Study of Embodied Cognition from the Bottom Up</a> (2018-01-15T14:29:14Z)<br><span class="small">worker=14 / A large body of compelling evidence has been accumulated demonstrating that embodiment - the agent's physical setup, including its shape, materials, sensors and actuators - is cons</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W2143502460" target="_blank">Modular Brain Networks</a> (2015)<br><span class="small">worker=13 / Annual Review of Psychology</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W2030479989" target="_blank">Probing the connectivity of neural circuits at single-neuron resolution using high-throughput DNA sequencing</a> (2011)<br><span class="small">worker=13 / Nature Precedings</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1101/174276" target="_blank">Rhythms of the Body, Rhythms of the Brain: Respiration, Neural Oscillations, and Embodied Cognition</a> (2017)<br><span class="small">worker=14 / </span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/1401.4158v1" target="_blank">Embodied social interaction constitutes social cognition in pairs of humans: A minimalist virtual reality experiment</a> (2014-01-16T20:42:32Z)<br><span class="small">worker=14 / Scientists have traditionally limited the mechanisms of social cognition to one brain, but recent approaches claim that interaction also realizes cognitive work. Experiments under </span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2512.02419v1" target="_blank">The brain-AI convergence: Predictive and generative world models for general-purpose computation</a> (2025-12-02T05:03:14Z)<br><span class="small">worker=12 / Recent advances in general-purpose AI systems with attention-based transformers offer a potential window into how the neocortex and cerebellum, despite their relatively uniform cir</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1007/978-3-031-64839-7_12" target="_blank">Astrocyte-Neuron Interactions Contributing to Amyotrophic Lateral Sclerosis Progression</a> (2024)<br><span class="small">worker=11 / Advances in Neurobiology</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1007/978-3-031-64839-7_9" target="_blank">Astrocyte-Neuron Interactions in Spinal Cord Injury</a> (2024)<br><span class="small">worker=11 / Advances in Neurobiology</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.3390/neuroglia5010001" target="_blank">Contribution of Small Extracellular Vesicles from Schwann Cells and Satellite Glial Cells to Pain Processing</a> (2024)<br><span class="small">worker=15 / Neuroglia</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2210.01419v1" target="_blank">Dynamic image recognition in a spiking neuron network supplied by astrocytes</a> (2022-10-04T07:18:09Z)<br><span class="small">worker=11 / Mathematical model of spiking neuron network (SNN) supplied by astrocytes is investigated. The astrocytes are specific type of brain cells which are not electrically excitable but </span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W3010093910" target="_blank">Neuron–glia interaction in the Drosophila nervous system</a> (2020)<br><span class="small">worker=15 / Developmental Neurobiology</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W2889526415" target="_blank">Norepinephrine stimulates glycogenolysis in astrocytes to fuel neurons with lactate</a> (2018)<br><span class="small">worker=12 / PLoS Computational Biology</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W4248169967" target="_blank">Enactivist Interventions</a> (2017)<br><span class="small">worker=14 / Oxford University Press eBooks</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1101/2024.04.04.588053" target="_blank">Modulation of input to the spinal cord; contribution of GABA released by interneurons and glial cells by polarization at the entry of sensory information</a> (2024)<br><span class="small">worker=15 / </span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2010.15748v4" target="_blank">Adaptive cognition implemented with a context-aware and flexible neuron for next-generation artificial intelligence</a> (2020-10-29T16:51:50Z)<br><span class="small">worker=11 / Neuromorphic computing mimics the organizational principles of the brain in its quest to replicate the brain's intellectual abilities. An impressive ability of the brain is its ada</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W605263502" target="_blank">Embodied Music Cognition and Mediation Technology</a> (2007)<br><span class="small">worker=14 / The MIT Press eBooks</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W1991785432" target="_blank">Glia-neuron crosstalk in the neuroprotective mechanisms of sex steroid hormones</a> (2005)<br><span class="small">worker=11 / Brain Research Reviews</span></li>
</ol>
</section>

<section class="section" id="u4">
<h2 class="section-title">U4: 因果同値</h2>
<p><strong>厳密定義:</strong> 観測一致ではなく介入分岐（counterfactual / do-intervention）で、生体系とモデル系の因果機構一致を判定できるか。</p>
<h3>リサーチクエスチョン分解</h3>
<ol>
<li>観測データ由来の相関を因果グラフへ持ち上げる識別条件は何か。</li>
<li>介入実験（刺激・抑制・入力撹乱）で検証可能な最小因果主張は何か。</li>
<li>active inferenceやDCMの理論予測を、反事実評価にどう接続するか。</li>
<li>同値判定の失敗条件（falsification）をどの水準で宣言するか。</li>
</ol>
<h3>今、解かれているもの（文献で積み上がっている領域）</h3>
<ul>
<li>do-calculus/SCM に基づく因果識別理論は成熟。</li>
<li>神経科学でDCMや介入実験を使った因果方向推定の実践知は存在。</li>
<li>反事実推論を含む評価設計の必要性は理論的にほぼ合意。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.1007/978-1-4614-7320-6_57-1" target="_blank">Dynamic Causal Modeling with Neural Population Models</a>、<a href="https://doi.org/10.1101/2021.06.01.446526" target="_blank">Test-retest reliability of regression dynamic causal modeling</a>、<a href="https://doi.org/10.1109/TBME.2024.3423803" target="_blank">A Deep Dynamic Causal Learning Model</a>、<a href="https://arxiv.org/abs/2010.09429v2" target="_blank">Neural Additive VAR for Causal Discovery in Time Series</a>。</p>
<h3>これから研究が必要なもの（未解決）</h3>
<ul>
<li>高次元時系列での因果識別可能性がデータ条件に強く依存。</li>
<li>観測ノイズ・遅延・未観測交絡を含む現実設定での頑健評価が不足。</li>
<li>WBE水準の介入同値判定に使える公開ベンチが未整備。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://arxiv.org/abs/2209.03427v1" target="_blank">Causal discovery for time series with latent confounders</a>、<a href="https://arxiv.org/abs/2306.08946v2" target="_blank">Bootstrap aggregation and confidence measures for time-series causal discovery</a>、<a href="https://doi.org/10.32614/cran.package.cfid" target="_blank">cfid: Identification of Counterfactual Queries in Causal Models</a>。</p>
<h3>主要先行研究（厳選 26 件）</h3>
<ol>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2507.00083v1" target="_blank">Strategic Counterfactual Modeling of Deep-Target Airstrike Systems via Intervention-Aware Spatio-Causal Graph Networks</a> (2025-06-30T04:26:10Z)<br><span class="small">worker=17 / This study addresses the lack of structured causal modeling between tactical strike behavior and strategic delay in current strategic-level simulations, particularly the structural</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2302.00860v3" target="_blank">Modeling Causal Mechanisms with Diffusion Models for Interventional and Counterfactual Queries</a> (2023-02-02T04:08:08Z)<br><span class="small">worker=16 / We consider the problem of answering observational, interventional, and counterfactual queries in a causally sufficient setting where only observational data and the causal graph a</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2209.03013v1" target="_blank">Quantitative probing: Validating causal models using quantitative domain knowledge</a> (2022-09-07T09:19:11Z)<br><span class="small">worker=17 / We present quantitative probing as a model-agnostic framework for validating causal models in the presence of quantitative domain knowledge. The method is constructed as an analogu</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2202.10166v1" target="_blank">Diffusion Causal Models for Counterfactual Estimation</a> (2022-02-21T12:23:01Z)<br><span class="small">worker=16 / We consider the task of counterfactual estimation from observational imaging data given a known causal structure. In particular, quantifying the causal effect of interventions for </span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1101/2024.11.06.622230" target="_blank">Dynamic Causal Modeling in Probabilistic Programming Languages</a> (2024)<br><span class="small">worker=17 / </span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2101.08123v1" target="_blank">Technological Competence is a Precondition for Effective Implementation of Virtual Reality Head Mounted Displays in Human Neuroscience: A Technological Review and Meta-analysis</a> (2021-01-20T13:48:11Z)<br><span class="small">worker=17 / Immersive virtual reality (VR) emerges as a promising research and clinical tool. However, several studies suggest that VR induced adverse symptoms and effects (VRISE) may undermin</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2010.09429v2" target="_blank">Neural Additive Vector Autoregression Models for Causal Discovery in Time Series</a> (2020-10-19T12:44:25Z)<br><span class="small">worker=20 / Causal structure discovery in complex dynamical systems is an important challenge for many scientific domains. Although data from (interventional) experiments is usually limited, l</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/1902.03380v3" target="_blank">When Causal Intervention Meets Adversarial Examples and Image Masking for Deep Neural Networks</a> (2019-02-09T06:44:13Z)<br><span class="small">worker=17 / Discovering and exploiting the causality in deep neural networks (DNNs) are crucial challenges for understanding and reasoning causal effects (CE) on an explainable visual model. "</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1101/2021.06.01.446526" target="_blank">Test-retest reliability of regression dynamic causal modeling</a> (2021)<br><span class="small">worker=17 / </span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1007/978-1-4614-7320-6_57-1" target="_blank">Dynamic Causal Modeling with Neural Population Models</a> (2013)<br><span class="small">worker=17 / Encyclopedia of Computational Neuroscience</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2511.05236v1" target="_blank">The Causal Round Trip: Generating Authentic Counterfactuals by Eliminating Information Loss</a> (2025-11-07T13:37:23Z)<br><span class="small">worker=16 / Judea Pearl's vision of Structural Causal Models (SCMs) as engines for counterfactual reasoning hinges on faithful abduction: the precise inference of latent exogenous noise. For d</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2306.08946v2" target="_blank">Bootstrap aggregation and confidence measures to improve time series causal discovery</a> (2023-06-15T08:37:16Z)<br><span class="small">worker=20 / Learning causal graphs from multivariate time series is a ubiquitous challenge in all application domains dealing with time-dependent systems, such as in Earth sciences, biology, o</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2303.01274v1" target="_blank">Measuring axiomatic soundness of counterfactual image models</a> (2023-03-02T13:59:07Z)<br><span class="small">worker=16 / We present a general framework for evaluating image counterfactuals. The power and flexibility of deep generative models make them valuable tools for learning mechanisms in structu</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1109/ijcnn54540.2023.10192004" target="_blank">Neural Time-Invariant Causal Discovery from Time Series Data</a> (2023)<br><span class="small">worker=20 / 2023 International Joint Conference on Neural Networks (IJCNN)</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2209.03427v1" target="_blank">Causal discovery for time series with latent confounders</a> (2022-09-07T18:57:19Z)<br><span class="small">worker=20 / Reconstructing the causal relationships behind the phenomena we observe is a fundamental challenge in all areas of science. Discovering causal relationships through experiments is </span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2208.10601v1" target="_blank">Deriving time-averaged active inference from control principles</a> (2022-08-22T21:20:04Z)<br><span class="small">worker=19 / Active inference offers a principled account of behavior as minimizing average sensory surprise over time. Applications of active inference to control problems have heretofore tend</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W2912654919" target="_blank">Global, regional, and national incidence, prevalence, and years lived with disability for 354 diseases and injuries for 195 countries and territories, 1990–2017: a systematic analysis for the Global Burden of Disease Study 2017</a> (2018)<br><span class="small">worker=17 / The Lancet</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.21203/rs.3.rs-7023047/v1" target="_blank">Causal Fairness in Black-Box AI: A Counterfactual Auditing Framework for Deep Models</a> (2025)<br><span class="small">worker=16 / </span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.2139/ssrn.4850347" target="_blank">Data Imputation with Adversarial Neural Networks for Causal Discovery from Subsampled Time Series</a> (2024)<br><span class="small">worker=20 / </span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2104.08043v1" target="_blank">Data Generating Process to Evaluate Causal Discovery Techniques for Time Series Data</a> (2021-04-16T11:38:29Z)<br><span class="small">worker=20 / Going beyond correlations, the understanding and identification of causal relationships in observational time series, an important subfield of Causal Discovery, poses a major chall</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.32614/cran.package.cfid" target="_blank">cfid: Identification of Counterfactual Queries in Causal Models</a> (2021)<br><span class="small">worker=16 / CRAN: Contributed Packages</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2010.00262v1" target="_blank">Active Inference or Control as Inference? A Unifying View</a> (2020-10-01T09:08:45Z)<br><span class="small">worker=19 / Active inference (AI) is a persuasive theoretical framework from computational neuroscience that seeks to describe action and perception as inference-based computation. However, th</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1007/978-3-031-01909-8_3" target="_blank">Time Series Causality Tools</a> (2016)<br><span class="small">worker=20 / Synthesis Lectures on Data Mining and Knowledge Discovery</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W2115123524" target="_blank">Enrichment Effects on Adult Cognitive Development</a> (2008)<br><span class="small">worker=17 / Gothic.net</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2308.08307v1" target="_blank">Integrating cognitive map learning and active inference for planning in ambiguous environments</a> (2023-08-16T12:10:23Z)<br><span class="small">worker=19 / Living organisms need to acquire both cognitive maps for learning the structure of the world and planning mechanisms able to deal with the challenges of navigating ambiguous enviro</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W4321162478" target="_blank">CUTS: Neural Causal Discovery from Irregular Time-Series Data</a> (2023)<br><span class="small">worker=20 / arXiv (Cornell University)</span></li>
</ol>
</section>

<section class="section" id="u7">
<h2 class="section-title">U7: マルチモーダル整合</h2>
<p><strong>厳密定義:</strong> EEG/fMRI/行動/生理の時刻系・空間系・前処理ログを監査可能に固定し、再解析で同一結論へ到達できるか。</p>
<h3>リサーチクエスチョン分解</h3>
<ol>
<li>BIDS拡張で同期・QC・刺激ログをどこまで必須化するか。</li>
<li>LSL等の時刻同期誤差を検証可能な指標に落とせるか。</li>
<li>アーチファクト除去（ASR, ZapLine等）の設定差が結果へ与える影響をどう監査するか。</li>
<li>モダリティ間アライメント失敗時の再計測/除外基準をどう固定するか。</li>
<li>前処理差分をCIで自動比較する場合、どの再現率低下をリリースブロック閾値にするか。</li>
<li>モダリティ欠損（EEG欠損・fMRI欠損）条件でも同等結論を保てる最小観測セットは何か。</li>
</ol>
<h3>今、解かれているもの（文献で積み上がっている領域）</h3>
<ul>
<li>BIDS/EEG-BIDSによりデータ配置と基本メタデータ仕様は共有可能になった。</li>
<li>LSLと同期ログの実装実践はコミュニティで広く利用されている。</li>
<li>EEG品質管理の標準的前処理（ASR等）に関する知見は蓄積。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.1162/imag.a.136" target="_blank">The lab streaming layer for synchronized multimodal recording</a>、<a href="https://doi.org/10.1038/s41597-024-03559-8" target="_blank">Motion-BIDS</a>、<a href="https://doi.org/10.1101/2024.02.13.580071" target="_blank">The Lab Streaming Layer for Synchronized Multimodal Recording</a>、<a href="https://doi.org/10.1093/sleep/zsad241" target="_blank">Artifact subspace reconstruction in EEG studies</a>、<a href="https://doi.org/10.3389/fnhum.2019.00141" target="_blank">Riemannian Modification of Artifact Subspace Reconstruction</a>。</p>
<h3>これから研究が必要なもの（未解決）</h3>
<ul>
<li>同期誤差の許容域をタスク別に定義した共通規約が不足。</li>
<li>異なる前処理パイプライン間での出力差分監査が不十分。</li>
<li>失敗例まで含めた公開QCログ運用が限定的。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://api.openalex.org/W4390079365" target="_blank">Two common issues in synchronized multimodal recordings with EEG: Jitter and latency</a>、<a href="https://doi.org/10.1109/bibm58861.2023.10385390" target="_blank">IMU-integrated Artifact Subspace Reconstruction for Wearable EEG Devices</a>、<a href="https://arxiv.org/abs/2403.09707v1" target="_blank">Understanding data analysis aspects of TMS-EEG in clinical study</a>。</p>
<h3>主要先行研究（厳選 26 件）</h3>
<ol>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1162/imag.a.136" target="_blank">The lab streaming layer for synchronized multimodal recording</a> (2025)<br><span class="small">worker=22 / Imaging Neuroscience</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2407.04727v2" target="_blank">Dynamical Embedding of Single Channel Electroencephalogram for Artifact Subspace Reconstruction</a> (2024-06-28T06:26:29Z)<br><span class="small">worker=24 / This study introduces a novel framework to apply Artifact Subspace Reconstruction (ASR) algorithm on single-channel Electroencephalogram (EEG) data. ASR, renowned for its automated</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2204.13444v1" target="_blank">Mobile EEG artifact correction on limited hardware using artifact subspace recon- struction</a> (2022-04-28T12:23:19Z)<br><span class="small">worker=24 / Biological data like electroencephalography (EEG) are typically contaminated by unwanted signals, called artifacts. Therefore, many applications dealing with biological data with l</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2008.13369v1" target="_blank">Introducing Representations of Facial Affect in Automated Multimodal Deception Detection</a> (2020-08-31T05:12:57Z)<br><span class="small">worker=22 / Automated deception detection systems can enhance health, justice, and security in society by helping humans detect deceivers in high-stakes situations across medical and legal dom</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2508.05993v3" target="_blank">Efficient Multimodal Streaming Recommendation via Expandable Side Mixture-of-Experts</a> (2025-08-08T04:00:05Z)<br><span class="small">worker=22 / Streaming recommender systems (SRSs) are widely deployed in real-world applications, where user interests shift and new items arrive over time. As a result, effectively capturing u</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2410.16284v2" target="_blank">A 3D Framework for Improving Low-Latency Multi-Channel Live Streaming</a> (2024-10-05T02:21:57Z)<br><span class="small">worker=22 / The advent of 5G has driven the demand for high-quality, low-latency live streaming. However, challenges such as managing the increased data volume, ensuring synchronization across</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W4390079365" target="_blank">Two common issues in synchronized multimodal recordings with EEG: Jitter and latency</a> (2023)<br><span class="small">worker=22 / Neuroscience Research</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2511.21760v2" target="_blank">fMRI-LM: Towards a Universal Foundation Model for Language-Aligned fMRI Understanding</a> (2025-11-24T20:26:59Z)<br><span class="small">worker=23 / Recent advances in multimodal large language models (LLMs) have enabled unified reasoning across images, audio, and video, but extending such capability to brain imaging remains la</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2503.14504v2" target="_blank">Aligning Multimodal LLM with Human Preference: A Survey</a> (2025-03-18T17:59:56Z)<br><span class="small">worker=23 / Large language models (LLMs) can handle a wide variety of general tasks with simple prompts, without the need for task-specific training. Multimodal Large Language Models (MLLMs), </span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2403.09707v1" target="_blank">Understanding data analysis aspects of TMS-EEG in clinical study: a mini review and a case study with open dataset</a> (2024-03-09T18:13:35Z)<br><span class="small">worker=24 / Concurrency of transcranial magnetic stimulation with electroencephalography (TMS-EEG) technique is a powerful and challenging methodology for basic research and clinical applicati</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1101/2024.02.13.580071" target="_blank">The Lab Streaming Layer for Synchronized Multimodal Recording</a> (2024)<br><span class="small">worker=22 / </span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1109/bibm58861.2023.10385390" target="_blank">IMU-integrated Artifact Subspace Reconstruction for Wearable EEG Devices</a> (2023)<br><span class="small">worker=24 / 2023 IEEE International Conference on Bioinformatics and Biomedicine (BIBM)</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1093/sleep/zsad241" target="_blank">Artifact subspace reconstruction: a candidate for a dream solution for EEG studies, sleep or awake</a> (2023)<br><span class="small">worker=24 / SLEEP</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2112.00989v2" target="_blank">Embedding Decomposition for Artifacts Removal in EEG Signals</a> (2021-12-02T05:30:38Z)<br><span class="small">worker=24 / Electroencephalogram (EEG) recordings are often contaminated with artifacts. Various methods have been developed to eliminate or weaken the influence of artifacts. However, most of</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/1906.07354v1" target="_blank">Bayesian fusion and multimodal DCM for EEG and fMRI</a> (2019-06-18T02:59:47Z)<br><span class="small">worker=23 / This paper asks whether integrating multimodal EEG and fMRI data offers a better characterisation of functional brain architectures than either modality alone. This evaluation rest</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.3389/fnhum.2019.00141" target="_blank">A Riemannian Modification of Artifact Subspace Reconstruction for EEG Artifact Handling</a> (2019)<br><span class="small">worker=24 / Frontiers in Human Neuroscience</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/1801.09232v1" target="_blank">Multimodal Functional and Structural Brain Connectivity Analysis in Autism: A Preliminary Integrated Approach with EEG, fMRI and DTI</a> (2018-01-28T14:04:50Z)<br><span class="small">worker=23 / This paper proposes a novel approach of integrating different neuroimaging techniques to characterize an autistic brain. Different techniques like EEG, fMRI and DTI have traditiona</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W2153791616" target="_blank">Whatever next? Predictive brains, situated agents, and the future of cognitive science</a> (2013)<br><span class="small">worker=22 / Behavioral and Brain Sciences</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1109/ddecs.2010.5491745" target="_blank">Receiver synchronization in video streaming with short latency over asynchronous networks</a> (2010)<br><span class="small">worker=22 / 13th IEEE Symposium on Design and Diagnostics of Electronic Circuits and Systems</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W3080791240" target="_blank">Multimodal-Multisensory Experiments</a> (2020)<br><span class="small">worker=22 / Preprints.org</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.11138/fneur/2015.30.1.009" target="_blank">Integration of multimodal neuroimaging methods: a rationale for clinical applications of simultaneous EEG-fMRI</a> (2015)<br><span class="small">worker=23 / Functional Neurology</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1201/b17605-13" target="_blank">Perspectives of M-EEG and fMRI Data Fusion</a> (2014)<br><span class="small">worker=23 / EEG/ERP Analysis</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.3389/conf.fnins.2010.06.00015" target="_blank">Multimodal integration: constraining MEG localization with EEG and fMRI</a> (2010)<br><span class="small">worker=23 / Frontiers in Neuroscience</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2509.02568v1" target="_blank">EEG-MSAF: An Interpretable Microstate Framework uncovers Default-Mode Decoherence in Early Neurodegeneration</a> (2025-08-18T15:54:29Z)<br><span class="small">worker=21 / Dementia (DEM) is a growing global health challenge, underscoring the need for early and accurate diagnosis. Electroencephalography (EEG) provides a non-invasive window into brain </span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2310.12417v1" target="_blank">Metadata for Scientific Experiment Reporting: A Case Study in Metal-Organic Frameworks</a> (2023-10-19T02:11:44Z)<br><span class="small">worker=21 / Research methods and procedures are core aspects of the research process. Metadata focused on these components is critical to supporting the FAIR principles, particularly reproduci</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W4296131700" target="_blank">No need for extensive artifact rejection for ICA - A multi-study evaluation on stationary and mobile EEG datasets</a> (2022)<br><span class="small">worker=24 / </span></li>
</ol>
</section>

<section class="section" id="u8">
<h2 class="section-title">U8: 閉ループ安定性</h2>
<p><strong>厳密定義:</strong> 遅延・ジッタ・ノイズ・ドリフト下で、閉ループ神経制御が安全制約を破らず安定に動作するか。</p>
<h3>リサーチクエスチョン分解</h3>
<ol>
<li>閉ループBCIの遅延許容域を制御理論的にどう同定するか。</li>
<li>オンライン較正と概念ドリフト対策をどう組み込むか。</li>
<li>個体差と日内変動をまたぐ安定性をどの指標で評価するか。</li>
<li>異常検知とフェイルセーフを評価契約へどう組み込むか。</li>
<li>ヒューマンオーバーライドを導入したとき、誤作動率と回復時間をどうKPI化するか。</li>
<li>週〜月スケール運用での再学習頻度を、性能劣化と安全余裕のトレードオフでどう最適化するか。</li>
</ol>
<h3>今、解かれているもの（文献で積み上がっている領域）</h3>
<ul>
<li>閉ループBCIにおける遅延・適応制御の重要性は多数報告で一貫。</li>
<li>オンライン再学習や適応フィルタにより短期安定性を改善できることは確認済み。</li>
<li>リアルタイム神経フィードバック系の基本アーキテクチャは確立。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.31224/4555" target="_blank">Closed-Loop Mu-Rhythm BCI for Neuroadaptive Control</a>、<a href="https://doi.org/10.1088/1741-2552/adbb20" target="_blank">Dareplane: a modular open-source software platform for BCI research</a>、<a href="https://doi.org/10.1016/j.bspc.2022.104183" target="_blank">Self-adaptive multiple-kernel ELM for MI-BCI</a>、<a href="https://arxiv.org/abs/2508.10474v1" target="_blank">EDAPT: Calibration-Free BCIs with Continual Online Adaptation</a>。</p>
<h3>これから研究が必要なもの（未解決）</h3>
<ul>
<li>長期運用でのドリフト耐性と再現性評価が不足。</li>
<li>安全制約違反を事前検出する統一検証手順が不足。</li>
<li>閉ループ破綻時の責任境界と運用基準が未整備。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://arxiv.org/abs/2011.12362v1" target="_blank">Fixed-Time Stable Adaptation Law for Safety-Critical Control</a>、<a href="https://arxiv.org/abs/2508.08153v2" target="_blank">Robust Adaptive Discrete-Time Control Barrier Certificate</a>、<a href="https://doi.org/10.1109/bci60775.2024.10480468" target="_blank">Calibration-free online test-time adaptation for EEG MI decoding</a>。</p>
<h3>主要先行研究（再精査 14 件）</h3>
<ol>
<li><strong>[Nature Medicine]</strong> <a href="https://doi.org/10.1038/s41591-024-03196-z" target="_blank">Chronic adaptive DBS versus conventional DBS in Parkinson's disease</a> (2024)</li>
<li><strong>[Brain]</strong> <a href="https://doi.org/10.1093/brain/awad429" target="_blank">At-home adaptive dual-target DBS with proportional control</a> (2024)</li>
<li><strong>[npj Parkinson's Disease]</strong> <a href="https://doi.org/10.1038/s41531-025-01124-7" target="_blank">Clinical outcomes and programming strategies in chronic adaptive DBS</a> (2025)</li>
<li><strong>[npj Parkinson's Disease]</strong> <a href="https://doi.org/10.1038/s41531-024-00772-5" target="_blank">ADAPT-PD sensing data and methodology</a> (2024)</li>
<li><strong>[JAMA Neurology]</strong> <a href="https://doi.org/10.1001/jamaneurol.2025.2781" target="_blank">Long-term personalized adaptive DBS</a> (2025)</li>
<li><strong>[Nature Reviews Neurology]</strong> <a href="https://doi.org/10.1038/s41582-025-01131-5" target="_blank">From adaptive DBS to adaptive circuit targeting</a> (2025)</li>
<li><strong>[Nature Biomedical Engineering]</strong> <a href="https://doi.org/10.1038/s41551-025-01438-0" target="_blank">Movement-responsive DBS with remotely optimized decoder</a> (2026 issue)</li>
<li><strong>[Expert Review of Medical Devices]</strong> <a href="https://doi.org/10.1080/17434440.2024.2438309" target="_blank">Closed-loop DBS systems for neuropsychiatric disorders</a> (2024)</li>
<li><strong>[medRxiv]</strong> <a href="https://doi.org/10.1101/2024.08.26.24312580" target="_blank">Adaptive DBS in Parkinson's disease: Delphi consensus</a> (2024 preprint)</li>
<li><strong>[IEEE BCI]</strong> <a href="https://doi.org/10.1109/bci60775.2024.10480468" target="_blank">Calibration-free online test-time adaptation for EEG motor imagery decoding</a> (2024)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2508.10474v1" target="_blank">EDAPT: Calibration-Free BCIs with Continual Online Adaptation</a> (2025)</li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.31224/4555" target="_blank">Closed-Loop Mu-Rhythm BCI for Neuroadaptive Control</a> (2025)</li>
<li><strong>[Biomedical Signal Processing and Control]</strong> <a href="https://doi.org/10.1016/j.bspc.2022.104183" target="_blank">Self-adaptive multiple-kernel ELM for MI-BCI</a> (2023)</li>
<li><strong>[IEEE BCI Workshop]</strong> <a href="https://doi.org/10.1109/iww-bci.2016.7457451" target="_blank">Brain-controlled devices: the perception-action closed loop</a> (2016)</li>
</ol>
</section>

<section class="section" id="u10">
<h2 class="section-title">U10: 熱力学的一貫性</h2>
<p><strong>厳密定義:</strong> 情報処理の不可逆性・散逸・エネルギー下限を神経計算モデルへ写像し、測定可能な反証条件を置けるか。</p>
<h3>リサーチクエスチョン分解</h3>
<ol>
<li>Landauer下限を神経計算でどう適用/解釈するか。</li>
<li>非平衡熱力学指標と神経情報処理効率の対応をどう定義するか。</li>
<li>理論式を実データ（神経活動・代謝）へ落とし込む観測設計をどう作るか。</li>
<li>WBE計算コスト評価に熱力学制約をどう統合するか。</li>
</ol>
<h3>今、解かれているもの（文献で積み上がっている領域）</h3>
<ul>
<li>Landauer原理・情報熱力学の理論枠組み自体は確立。</li>
<li>神経科学へ情報熱力学を接続するレビュー/視点論文が増加。</li>
<li>計算効率とエネルギー制約を同時評価する問題設定は明確化。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://arxiv.org/abs/2003.07436v1" target="_blank">Landauer Principle and General Relativity</a>、<a href="https://doi.org/10.3390/e26090779" target="_blank">Information Thermodynamics: From Physics to Neuroscience</a>、<a href="https://doi.org/10.1016/j.tics.2024.03.009" target="_blank">The Thermodynamics of Mind</a>、<a href="https://doi.org/10.1017/9781316650394.024" target="_blank">Information and Thermodynamics</a>。</p>
<h3>これから研究が必要なもの（未解決）</h3>
<ul>
<li>神経回路実装における実効下限の実測研究が限定的。</li>
<li>熱散逸推定の標準化された計測パイプラインが不足。</li>
<li>WBEスケール推定で使える合意済みコストモデルが未成立。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.1007/978-3-319-93458-7_2" target="_blank">Conditional Erasure and the Landauer Limit</a>、<a href="https://doi.org/10.3390/books978-3-7258-4142-4" target="_blank">The Landauer Principle and Its Implementations in Physics, Chemistry and Biology</a>、<a href="https://doi.org/10.1016/b978-0-444-59557-7.00011-4" target="_blank">Thermodynamics and Biological Systems</a>。</p>
<h3>主要先行研究（厳選 26 件）</h3>
<ol>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2003.07436v1" target="_blank">Landauer Principle and General Relativity</a> (2020-03-16T20:41:26Z)<br><span class="small">worker=30 / We endeavour to illustrate the physical relevance of the Landauer principle applying it to different important issues concerning the theory of gravitation. We shall first analyze, </span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2411.07897v1" target="_blank">Modified Landauer principle according to Tsallis entropy</a> (2024-11-12T16:08:29Z)<br><span class="small">worker=30 / The Landauer principle establishes a lower bound in the amount of energy that should be dissipated in the erasure of one bit of information. The specific value of this dissipated e</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2409.17599v1" target="_blank">Information thermodynamics: from physics to neuroscience</a> (2024-09-26T07:28:13Z)<br><span class="small">worker=29 / This paper provides a perspective on applying the concepts of information thermodynamics, developed recently in non-equilibrium statistical physics, to problems in theoretical neur</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.3390/books978-3-7258-4142-4" target="_blank">The Landauer Principle and Its Implementations in Physics, Chemistry and Biology</a> (2025)<br><span class="small">worker=30 / </span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1007/978-3-319-93458-7_2" target="_blank">Conditional Erasure and the Landauer Limit</a> (2018)<br><span class="small">worker=30 / Energy Limits in Computation</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/1512.07839v4" target="_blank">Implementing a Bayes Filter in a Neural Circuit: The Case of Unknown Stimulus Dynamics</a> (2015-12-22T14:52:14Z)<br><span class="small">worker=30 / In order to interact intelligently with objects in the world, animals must first transform neural population responses into estimates of the dynamic, unknown stimuli which caused t</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/1212.0031v3" target="_blank">Encoding binary neural codes in networks of threshold-linear neurons</a> (2012-11-30T22:43:11Z)<br><span class="small">worker=30 / Networks of neurons in the brain encode preferred patterns of neural activity via their synaptic connections. Despite receiving considerable attention, the precise relationship bet</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1021/acs.jpclett.4c03156.s001" target="_blank">Deriving the Landauer Principle From the Quantum Shannon Entropy</a> (None)<br><span class="small">worker=30 / </span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.3390/e26090779" target="_blank">Information Thermodynamics: From Physics to Neuroscience</a> (2024)<br><span class="small">worker=29 / Entropy</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2101.08123v1" target="_blank">Technological Competence is a Precondition for Effective Implementation of Virtual Reality Head Mounted Displays in Human Neuroscience: A Technological Review and Meta-analysis</a> (2021-01-20T13:48:11Z)<br><span class="small">worker=29 / Immersive virtual reality (VR) emerges as a promising research and clinical tool. However, several studies suggest that VR induced adverse symptoms and effects (VRISE) may undermin</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2002.07664v1" target="_blank">Nonequilibrium thermodynamics: emergent and fundamental</a> (2020-02-16T20:20:17Z)<br><span class="small">worker=32 / How can we derive the evolution equations of dissipative systems? What is the relation between the different approaches? How much do we understand the fundamental aspects of a seco</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/1612.02496v1" target="_blank">Thermodynamics of low-dimensional trapped Fermi gases</a> (2016-12-08T00:41:00Z)<br><span class="small">worker=29 / The effects of low dimensionality on the thermodynamics of a Fermi gas trapped by isotropic power law potentials are analyzed. Particular attention is given to different characteri</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W2153791616" target="_blank">Whatever next? Predictive brains, situated agents, and the future of cognitive science</a> (2013)<br><span class="small">worker=30 / Behavioral and Brain Sciences</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W2132262459" target="_blank">CHARMM: The biomolecular simulation program</a> (2009)<br><span class="small">worker=30 / Journal of Computational Chemistry</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1017/9781316650394.024" target="_blank">Information and Thermodynamics</a> (None)<br><span class="small">worker=29 / Perspectives on Statistical Thermodynamics</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W4385772954" target="_blank">Phase-Field DeepONet: Physics-informed deep operator neural network for fast simulations of pattern formation governed by gradient flows of free-energy functionals</a> (2023)<br><span class="small">worker=32 / Computer Methods in Applied Mechanics and Engineering</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1016/b978-0-444-59557-7.00011-4" target="_blank">Thermodynamics and Biological Systems</a> (2014)<br><span class="small">worker=32 / Nonequilibrium Thermodynamics</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/1103.5671v1" target="_blank">Thermodynamic derivation and use of a nonequilibrium canonical ensemble</a> (2011-03-29T14:59:26Z)<br><span class="small">worker=32 / A thermodynamic expression for the analog of the canonical ensemble for nonequilibrium systems is described based on a purely information theoretical interpretation of entropy. As </span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1201/b10962-10" target="_blank">Chemical Thermodynamics, Information, and Horizons</a> (2011)<br><span class="small">worker=29 / Chemical Thermodynamics and Information Theory with Applications</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/1002.1845v1" target="_blank">Lie groups in nonequilibrium thermodynamics: Geometric structure behind viscoplasticity</a> (2010-02-09T13:09:54Z)<br><span class="small">worker=32 / Poisson brackets provide the mathematical structure required to identify the reversible contribution to dynamic phenomena in nonequilibrium thermodynamics. This mathematical struct</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1016/b978-044453079-0/50013-4" target="_blank">THERMODYNAMICS AND BIOLOGICAL SYSTEMS</a> (2007)<br><span class="small">worker=32 / Nonequilibrium Thermodynamics</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1016/b978-044450886-7/50012-6" target="_blank">Thermodynamics and biological systems</a> (2002)<br><span class="small">worker=32 / Nonequilibrium Thermodynamics</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W4233135949" target="_blank">Probabilistic latent semantic indexing</a> (1999)<br><span class="small">worker=30 / </span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W3023669232" target="_blank">Nonequilibrium Thermodynamics in Cell Biology: Extending Equilibrium Formalism to Cover Living Systems</a> (2020)<br><span class="small">worker=32 / Annual Review of Biophysics</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W2610895655" target="_blank">Nonequilibrium thermodynamics of restricted Boltzmann machines</a> (2017)<br><span class="small">worker=32 / Physical review. E</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W2133483674" target="_blank">Brain activity and cognition: a connection from thermodynamics and information theory</a> (2015)<br><span class="small">worker=29 / Frontiers in Psychology</span></li>
</ol>
</section>

<section class="section" id="u11">
<h2 class="section-title">U11: 意識指標近似の妥当性</h2>
<p><strong>厳密定義:</strong> IIT/PCI/GWT等の指標が、どの条件で一致し、どの条件で乖離するかをデータ駆動で比較可能にする。</p>
<h3>リサーチクエスチョン分解</h3>
<ol>
<li>理論間で比較可能な入出力仕様をどう定義するか。</li>
<li>PCIやIIT近似計算の計算量制約をどう扱うか。</li>
<li>理論予測の対立点を単一実験計画へどう落とすか。</li>
<li>意識指標を臨床/研究で運用する際の失敗条件をどう明示するか。</li>
</ol>
<h3>今、解かれているもの（文献で積み上がっている領域）</h3>
<ul>
<li>IIT 4.0、GWT、PCI系の理論・実証双方で比較対象が明確化。</li>
<li>adversarial collaboration型の理論比較アプローチが提案され、対立点の明示が進展。</li>
<li>PCIは臨床・意識状態研究で一定の有用性が示されている。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.1093/nc/niad016" target="_blank">PCI と GWT の整合可能性検討</a>、<a href="https://doi.org/10.31234/osf.io/rdq52" target="_blank">Structured Adversarial Collaboration Process</a>、<a href="https://doi.org/10.1038/s41586-025-08888-1" target="_blank">Adversarial testing of global neuronal workspace and integrated information theories of consciousness</a>、<a href="https://arxiv.org/abs/2212.14787v1" target="_blank">Integrated Information Theory (IIT) 4.0</a>。</p>
<h3>これから研究が必要なもの（未解決）</h3>
<ul>
<li>理論間を同条件で比較する公開ベンチが不足。</li>
<li>IIT計算量問題を回避した近似指標の妥当域が未確定。</li>
<li>複数理論を統合した実務的判定規約が未整備。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.31234/osf.io/gauqm_v1" target="_blank">IIT の実験予測可能性に関する検討</a>、<a href="https://doi.org/10.31234/osf.io/kxywt" target="_blank">弱い IIT の分解と評価</a>、<a href="https://doi.org/10.1101/2020.01.08.898775" target="_blank">PCI の再現性評価（TMS-EEG）</a>。</p>
<h3>主要先行研究（厳選 26 件）</h3>
<ol>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2508.00190v1" target="_blank">On the utility of toy models for theories of consciousness</a> (2025-07-31T22:13:28Z)<br><span class="small">worker=36 / Toy models are highly idealized and deliberately simplified models that retain only the essential features of a system in order to explore specific theoretical questions. Long used</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2509.00555v1" target="_blank">Integrated information and predictive processing theories of consciousness: An adversarial collaborative review</a> (2025-08-30T16:41:13Z)<br><span class="small">worker=36 / As neuroscientific theories of consciousness continue to proliferate, the need to assess their similarities and differences -- as well as their predictive and explanatory power -- </span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1093/nc/niad016" target="_blank">About the compatibility between the perturbational complexity index and the global neuronal workspace theory of consciousness</a> (2023)<br><span class="small">worker=35 / Neuroscience of Consciousness</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.31234/osf.io/gauqm_v1" target="_blank">Does Integrated Information Theory (IIT) make experimental predictions about consciousness?</a> (2025)<br><span class="small">worker=33 / </span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.3390/e24020270" target="_blank">From Shorter to Longer Timescales: Converging Integrated Information Theory (IIT) with the Temporo-Spatial Theory of Consciousness (TTC)</a> (2022)<br><span class="small">worker=33 / Entropy</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2105.02314v1" target="_blank">Consciousness and the Collapse of the Wave Function</a> (2021-05-05T20:39:54Z)<br><span class="small">worker=35 / Does consciousness collapse the quantum wave function? This idea was taken seriously by John von Neumann and Eugene Wigner but is now widely dismissed. We develop the idea by combi</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/1405.0126v1" target="_blank">Is Consciousness Computable? Quantifying Integrated Information Using Algorithmic Information Theory</a> (2014-05-01T10:28:05Z)<br><span class="small">worker=33 / In this article we review Tononi's (2008) theory of consciousness as integrated information. We argue that previous formalizations of integrated information (e.g. Griffith, 2014) d</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2408.15982v2" target="_blank">From Neuronal Packets to Thoughtseeds: A Hierarchical Model of Embodied Cognition in the Global Workspace</a> (2024-08-28T17:51:16Z)<br><span class="small">worker=34 / The emergence of cognition requires a framework that bridges evolutionary principles with neurocomputational mechanisms. This paper introduces the novel "thoughtseed" framework, pr</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1123/science.adj4235" target="_blank"><em>Science</em>Adviser: Consciousness “adversarial collaboration” yields first results</a> (2023)<br><span class="small">worker=36 / AAAS Articles DO Group</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2212.14787v1" target="_blank">Integrated information theory (IIT) 4.0: Formulating the properties of phenomenal existence in physical terms</a> (2022-12-30T15:53:14Z)<br><span class="small">worker=33 / This paper presents Integrated Information Theory (IIT) 4.0. IIT aims to account for the properties of experience in physical (operational) terms. It identifies the essential prope</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.31234/osf.io/rdq52" target="_blank">Accelerating Research on Consciousness: The Structured Adversarial Collaboration Process</a> (2024)<br><span class="small">worker=36 / </span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1111/ejn.16299/v1/review2" target="_blank">Review for "Dissociations between spontaneous electroencephalographic features and the perturbational complexity index in the minimally conscious state"</a> (2023)<br><span class="small">worker=35 / </span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.31234/osf.io/93ufe" target="_blank">Where is the ‘posterior hot zone’? Open Review of Cogitate et al (2023): “An Adversarial Collaboration to Critically Evaluate Theories of Consciousness”</a> (2023)<br><span class="small">worker=36 / </span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2002.07716v2" target="_blank">Synaptic clock as a neural substrate of consciousness</a> (2020-02-18T16:43:58Z)<br><span class="small">worker=35 / In this theoretical work the temporal aspect of consciousness is analyzed. We start from the notion that while conscious experience seems to change constantly, yet for any of its c</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1101/2020.01.08.898775" target="_blank">Assessing the Intra- and Inter-Subject Reliability of the Perturbational Complexity Index (PCI) of Consciousness for Three Brain Regions Using TMS-EEG</a> (2020)<br><span class="small">worker=35 / </span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/1108.4296v1" target="_blank">On the evolution of phenomenal consciousness</a> (2011-08-22T12:54:54Z)<br><span class="small">worker=35 / A number of concepts are included in the term 'consciousness'. We choose to concentrate here on phenomenal consciousness, the process through which we are able to experience aspect</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1093/acprof:oso/9780198520917.003.0012" target="_blank">The global neuronal workspace</a> (2006)<br><span class="small">worker=34 / Consciousness</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/physics/0409140v2" target="_blank">Complex-Dynamic Origin of Consciousness and the Critical Choice of Sustainability Transition</a> (2004-09-27T10:43:59Z)<br><span class="small">worker=35 / A quite general interaction process of a multi-component system is analysed by the extended effective potential method liberated from usual limitations of perturbation theory or in</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/q-bio/0401018v2" target="_blank">Consciousness, cognition, and context: extending the global neuronal workspace model</a> (2004-01-14T18:22:44Z)<br><span class="small">worker=34 / We adapt an information theory analysis of interacting cognitive biological and social modules to the problem of the global neuronal workspace, the current standard neuroscience pi</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2508.13171v1" target="_blank">Cognitive Workspace: Active Memory Management for LLMs -- An Empirical Study of Functional Infinite Context</a> (2025-08-08T16:32:47Z)<br><span class="small">worker=34 / Large Language Models (LLMs) face fundamental limitations in context management despite recent advances extending context windows to millions of tokens. We propose Cognitive Worksp</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.31234/osf.io/kxywt" target="_blank">Separating weak integrated information theory (IIT) into IIT-inspired and aspirational-IIT approaches</a> (2023)<br><span class="small">worker=33 / </span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W4382048961" target="_blank">An adversarial collaboration to critically evaluate theories of consciousness</a> (2023)<br><span class="small">worker=36 / </span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W4382362322" target="_blank">An adversarial collaboration to critically evaluate theories of consciousness</a> (2023)<br><span class="small">worker=36 / </span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W3092295352" target="_blank">The predictive global neuronal workspace: A formal active inference model of visual consciousness</a> (2020)<br><span class="small">worker=34 / Progress in Neurobiology</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/1902.06002v3" target="_blank">Group Testing: An Information Theory Perspective</a> (2019-02-15T23:04:24Z)<br><span class="small">worker=33 / The group testing problem concerns discovering a small number of defective items within a large population by performing tests on pools of items. A test is positive if the pool con</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W2951753437" target="_blank">Integrating the global neuronal workspace into the framework of predictive processing: Towards a working hypothesis</a> (2019)<br><span class="small">worker=34 / Consciousness and Cognition</span></li>
</ol>
</section>

<section class="section" id="u12">
<h2 class="section-title">U12: 分岐本人性</h2>
<p><strong>厳密定義:</strong> 複製・分岐後に発生する複数主体の同一性・責任・権利帰属を、技術評価と整合する形式で規定できるか。</p>
<h3>リサーチクエスチョン分解</h3>
<ol>
<li>分岐後主体の識別子を何に基づいて付与するか。</li>
<li>責任・権利・同意の継承ルールをどの時点で分岐させるか。</li>
<li>心理的連続性基準と法的個体基準の不一致をどう扱うか。</li>
<li>技術評価（性能）と人格評価（帰属）をどう接続するか。</li>
<li>分岐主体間で記憶編集・再同期が起きた場合、法的主体IDを再編する基準は何か。</li>
<li>同意撤回が発生したとき、複数分岐主体への権限剥奪を技術的にどう実装・監査するか。</li>
</ol>
<h3>今、解かれているもの（文献で積み上がっている領域）</h3>
<ul>
<li>哲学的には分岐問題（duplications, fission）に関する論点整理が進んでいる。</li>
<li>心理的連続性 vs 数的同一性の対立構造は明確。</li>
<li>法制度側でデジタル人格・データ主体性の議論が拡大。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.1007/s11023-014-9352-8" target="_blank">Uploading and Branching Identity</a>、<a href="https://doi.org/10.1093/acprof:oso/9780198754855.003.0013" target="_blank">Enhancement, Mind-Uploading, and Personal Identity</a>、<a href="https://doi.org/10.20318/universitas.2025.9574" target="_blank">Neurotecnologías y neuroderechos</a>、<a href="https://doi.org/10.1017/9781009486309.002" target="_blank">The Right to Personal Identity</a>。</p>
<h3>これから研究が必要なもの（未解決）</h3>
<ul>
<li>技術システムに直結する運用規約（監査・責任追跡）が未整備。</li>
<li>分岐後の評価KPI（福祉・責任・所有）を定義する実務設計が不足。</li>
<li>国際法域をまたぐ整合ルールが未確定。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.52340/scai.2025.02.13" target="_blank">Digital Identity and Legal Personhood</a>、<a href="https://doi.org/10.69971/lra.3.1.2025.42" target="_blank">Legal Personhood and Identity of Human Digital Twins</a>、<a href="https://doi.org/10.1007/978-1-137-01616-4_15" target="_blank">Defining Identity IV: Personhood</a>。</p>
<h3>主要先行研究（厳選 19 件）</h3>
<ol>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2401.15284v6" target="_blank">Beyond principlism: Practical strategies for ethical AI use in research practices</a> (2024-01-27T03:53:25Z)<br><span class="small">worker=37 / The rapid adoption of generative artificial intelligence (AI) in scientific research, particularly large language models (LLMs), has outpaced the development of ethical guidelines,</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2112.07025v1" target="_blank">A Hippocratic Oath for mathematicians? Mapping the landscape of ethics in mathematics</a> (2021-12-13T21:24:20Z)<br><span class="small">worker=37 / While the consequences of mathematically-based software, algorithms and strategies have become ever wider and better appreciated, ethical reflection on mathematics has remained pri</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2111.11712v1" target="_blank">The Ethics of Biosurveillance</a> (2021-11-23T08:06:50Z)<br><span class="small">worker=37 / Governments must keep agricultural systems free of pests that threaten agricultural production and international trade. Biosecurity surveillance already makes use of a wide range o</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1093/acprof:oso/9780198754855.003.0013" target="_blank">Enhancement, Mind-Uploading, and Personal Identity</a> (2016)<br><span class="small">worker=37 / The Ethics of Human Enhancement</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W4388540663" target="_blank">Climate change, mental health, and reproductive decision-making: A systematic review</a> (2023)<br><span class="small">worker=37 / PLOS Climate</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/1504.06320v4" target="_blank">The Fallacy of Favoring Gradual Replacement Mind Uploading Over Scan-and-Copy</a> (2015-04-23T14:09:50Z)<br><span class="small">worker=37 / Mind uploading speculation and debate often concludes that a procedure described as gradual in-place replacement preserves personal identity while a procedure described as destruct</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1007/s11023-014-9352-8" target="_blank">Uploading and Branching Identity</a> (2014)<br><span class="small">worker=37 / Minds and Machines</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.46569/20.500.12680/5m60qz836" target="_blank">Ethics of Mind Uploading: Personal Identity</a> (None)<br><span class="small">worker=37 / </span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1017/9781009486309.002" target="_blank">The Right to Personal Identity</a> (2026)<br><span class="small">worker=39 / Minds, Freedoms and Rights</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W2416648430" target="_blank">How do older people describe their sensory experiences of the natural world? A systematic review of the qualitative evidence</a> (2016)<br><span class="small">worker=37 / BMC Geriatrics</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W1501447279" target="_blank">What Is Digital Labour? What Is Digital Work? What’s their Difference? And Why Do These Questions Matter for Understanding Social Media?</a> (2013)<br><span class="small">worker=37 / tripleC Communication Capitalism & Critique Open Access Journal for a Global Sustainable Information Society</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2310.05276v1" target="_blank">Enhancing Pre-Trained Language Models with Sentence Position Embeddings for Rhetorical Roles Recognition in Legal Opinions</a> (2023-10-08T20:33:55Z)<br><span class="small">worker=38 / The legal domain is a vast and complex field that involves a considerable amount of text analysis, including laws, legal arguments, and legal opinions. Legal practitioners must ana</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2511.14964v1" target="_blank">How Should the Law Treat Future AI Systems? Fictional Legal Personhood versus Legal Identity</a> (2025-11-18T23:08:28Z)<br><span class="small">worker=38 / The law draws a sharp distinction between objects and persons, and between two kinds of persons, the ''fictional'' kind (i.e. corporations), and the ''non-fictional'' kind (individ</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.52340/scai.2025.02.13" target="_blank">Digital Identity and Legal Personhood: Regulating AI and Virtual Entities in the Digital Age</a> (2025)<br><span class="small">worker=38 / Science And Innovation</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.69971/lra.3.1.2025.42" target="_blank">Legal Personhood and Identity of Human Digital Twins</a> (2025)<br><span class="small">worker=38 / Legal Research & Analysis</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2011.02412v1" target="_blank">Identity and Personhood in Digital Democracy: Evaluating Inclusion, Equality, Security, and Privacy in Pseudonym Parties and Other Proofs of Personhood</a> (2020-11-04T17:08:54Z)<br><span class="small">worker=38 / Digital identity seems like a prerequisite for digital democracy: how can we ensure "one person, one vote" online without identifying voters? But digital identity solutions - ID ch</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/1810.02724v1" target="_blank">Human Indignity: From Legal AI Personhood to Selfish Memes</a> (2018-10-02T20:01:43Z)<br><span class="small">worker=38 / It is possible to rely on current corporate law to grant legal personhood to Artificially Intelligent (AI) agents. In this paper, after introducing pathways to AI personhood, we an</span></li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W4324309277" target="_blank">2023 Alzheimer's disease facts and figures</a> (2023)<br><span class="small">worker=38 / Alzheimer s & Dementia</span></li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.1007/978-1-137-01616-4_15" target="_blank">Defining Identity IV: Personhood</a> (2014)<br><span class="small">worker=38 / Word Meaning and Legal Interpretation</span></li>
</ol>
</section>

<section class="section" id="u13">
<h2 class="section-title">U13: 模倣分離</h2>
<p><strong>厳密定義:</strong> 高性能模倣（言語/行動出力）と、内部因果構造保存を識別する評価軸を実験的に分離できるか。</p>
<h3>リサーチクエスチョン分解</h3>
<ol>
<li>brain-to-text成功を『意味復元』と『因果再現』へ分解できるか。</li>
<li>LLMの幻覚・整合性検査を神経デコード評価へどう接続するか。</li>
<li>同一出力でも内部機構が異なるケースをどう検出するか。</li>
<li>模倣性能の上限を因果評価でどこまで抑制できるか。</li>
<li>視覚知覚と視覚想起で同一デコーダを使ったとき、意味復元精度の劣化パターンはどこで分岐するか。</li>
<li>プロンプト誘導・データリーク・shortcut学習を分離検出する対照実験をどう設計するか。</li>
</ol>
<h3>今、解かれているもの（文献で積み上がっている領域）</h3>
<ul>
<li>非侵襲脳活動からのsemantic decoding/brain-to-textは急速に進展。</li>
<li>LLM幻覚検出・自己整合性評価の方法論は拡張中。</li>
<li>『出力一致だけでは内部同一性を保証しない』点は広く共有。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.1126/sciadv.adw1464" target="_blank">Mind captioning</a>、<a href="https://doi.org/10.1088/1741-2552/adfab1" target="_blank">Brain-to-text decoding with context-aware neural representations and large language models</a>、<a href="https://doi.org/10.1101/2022.09.29.509744" target="_blank">Semantic reconstruction of continuous language from non-invasive brain recordings</a>、<a href="https://doi.org/10.1002/brx2.37" target="_blank">Advancements and implications of semantic reconstruction</a>。</p>
<h3>これから研究が必要なもの（未解決）</h3>
<ul>
<li>模倣と因果保存を同時評価する統一ベンチが不足。</li>
<li>神経デコードでのデータリーク・shortcut学習検出が不十分。</li>
<li>介入実験を含む因果評価の標準手順が未整備。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.18653/v1/2025.emnlp-industry.139" target="_blank">Zero-knowledge LLM hallucination detection and mitigation</a>、<a href="https://doi.org/10.18653/v1/2025.findings-emnlp.527" target="_blank">Factuality Hallucination Type Detection via Belief State</a>、<a href="https://doi.org/10.1101/2024.03.19.585656" target="_blank">Decoding Continuous Character-based Language from Non-invasive Brain Recordings</a>。</p>
<h3>主要先行研究（再精査 14 件）</h3>
<ol>
<li><strong>[Science Advances]</strong> <a href="https://doi.org/10.1126/sciadv.adw1464" target="_blank">Mind captioning: Evolving descriptive text of mental content from human brain activity</a> (2025)</li>
<li><strong>[Nature Neuroscience]</strong> <a href="https://doi.org/10.1038/s41593-023-01304-9" target="_blank">Semantic reconstruction of continuous language from non-invasive brain recordings</a> (2023)</li>
<li><strong>[Cell Reports]</strong> <a href="https://doi.org/10.1016/j.celrep.2024.114924" target="_blank">A brain-to-text framework for decoding natural tonal sentences</a> (2024)</li>
<li><strong>[Journal of Neural Engineering]</strong> <a href="https://doi.org/10.1088/1741-2552/adfab1" target="_blank">Brain-to-text decoding with context-aware neural representations and large language models</a> (2025)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2506.22486" target="_blank">Hallucination Detection with Small Language Models</a> (2025)</li>
<li><strong>[EMNLP Industry]</strong> <a href="https://doi.org/10.18653/v1/2025.emnlp-industry.139" target="_blank">Zero-knowledge LLM hallucination detection and mitigation</a> (2025)</li>
<li><strong>[Findings of EMNLP]</strong> <a href="https://doi.org/10.18653/v1/2025.findings-emnlp.527" target="_blank">Factuality hallucination type detection via belief state</a> (2025)</li>
<li><strong>[AAAI]</strong> <a href="https://doi.org/10.1609/aaai.v39i27.35124" target="_blank">Representation Learning: A Causal Perspective</a> (2025)</li>
<li><strong>[AAAI]</strong> <a href="https://doi.org/10.1609/aaai.v39i17.33998" target="_blank">Learning strategy representation for imitation learning in multi-agent games</a> (2025)</li>
<li><strong>[Knowledge-Based Systems]</strong> <a href="https://doi.org/10.1016/j.knosys.2025.113565" target="_blank">Causal representation learning in offline visual reinforcement learning</a> (2025)</li>
<li><strong>[Nature Machine Intelligence]</strong> <a href="https://doi.org/10.1038/s42256-020-00257-z" target="_blank">Shortcut learning in deep neural networks</a> (2020)</li>
<li><strong>[IEEE EMBC]</strong> <a href="https://doi.org/10.1109/EMBC58623.2025.11251641" target="_blank">Decoding visual imagination and perception from EEG via topomap sequences</a> (2025)</li>
<li><strong>[IEEE EMBC]</strong> <a href="https://doi.org/10.1109/EMBC53108.2024.10782730" target="_blank">Decoding visual perception from EEG using explainable graph neural networks</a> (2024)</li>
<li><strong>[bioRxiv]</strong> <a href="https://doi.org/10.1101/2024.03.19.585656" target="_blank">Decoding continuous character-based language from non-invasive brain recordings</a> (2024)</li>
</ol>
</section>

<section class="section" id="u14">
<h2 class="section-title">U14: 追試可能性</h2>
<p><strong>厳密定義:</strong> 第三者が同一データ・同一手順・同一評価契約で同等結論に到達できる公開運用を常時維持できるか。</p>
<h3>リサーチクエスチョン分解</h3>
<ol>
<li>データ/コード/評価環境の固定粒度をどこまで要求するか。</li>
<li>探索研究と検証研究を運用上どう分離するか。</li>
<li>leaderboardでのリーク・過適合・報告バイアスをどう監査するか。</li>
<li>Model Card / Dataset Card を評価契約へどう統合するか。</li>
<li>再現失敗ケースを否定例レジストリとして公開し、再試行サイクルをどう運用するか。</li>
<li>コンテナ固定（OS・依存ライブラリ・乱数種）を必須化した場合、再現コスト増分をどこまで許容するか。</li>
</ol>
<h3>今、解かれているもの（文献で積み上がっている領域）</h3>
<ul>
<li>再現性危機を受け、preregistration・open science実践は拡大。</li>
<li>Model Card / Dataset Card の実務フレームは利用可能。</li>
<li>ベンチ運用の落とし穴（リーク、データ重複）に関する知見は豊富。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.1098/rsos.210155" target="_blank">Preregistration template for cognitive models</a>、<a href="https://doi.org/10.31219/osf.io/xsfam" target="_blank">Preregistration and increased transparency will benefit science</a>、<a href="https://doi.org/10.1038/s41746-022-00592-y" target="_blank">Methodological failures in medical imaging ML and recommendations</a>。</p>
<h3>これから研究が必要なもの（未解決）</h3>
<ul>
<li>神経科学×機械学習を跨ぐ共通監査規約が不十分。</li>
<li>失敗例を継続公開する文化・実装が限定的。</li>
<li>長期運用での評価劣化を追跡する仕組みが不足。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.1093/oso/9780190881481.003.0007" target="_blank">The Reproducibility Crisis</a>、<a href="https://doi.org/10.1098/rsos.242057" target="_blank">Open science interventions to improve reproducibility and replicability of research</a>、<a href="https://doi.org/10.31234/osf.io/dzsh4" target="_blank">Barriers and solutions for early career researchers in tackling reproducibility</a>、<a href="https://doi.org/10.37473/dac/10.1002/jrsm.1540" target="_blank">PreregRS guides preregistration for research syntheses</a>。</p>
<h3>主要先行研究（再精査 16 件）</h3>
<ol>
<li><strong>[Royal Society Open Science]</strong> <a href="https://doi.org/10.1098/rsos.210155" target="_blank">Preregistration template for the application of cognitive models</a> (2021)</li>
<li><strong>[OSF]</strong> <a href="https://doi.org/10.31219/osf.io/xsfam" target="_blank">Preregistration and increased transparency will benefit science</a> (2017)</li>
<li><strong>[npj Digital Medicine]</strong> <a href="https://doi.org/10.1038/s41746-022-00592-y" target="_blank">Methodological failures in medical imaging ML and recommendations</a> (2022)</li>
<li><strong>[Book Chapter]</strong> <a href="https://doi.org/10.1093/oso/9780190881481.003.0007" target="_blank">The Reproducibility Crisis</a> (2019)</li>
<li><strong>[Royal Society Open Science]</strong> <a href="https://doi.org/10.1098/rsos.242057" target="_blank">Open science interventions to improve reproducibility and replicability</a> (2024)</li>
<li><strong>[OSF]</strong> <a href="https://doi.org/10.31234/osf.io/dzsh4" target="_blank">Barriers and solutions for early career researchers in reproducibility</a> (2018)</li>
<li><strong>[PreregRS]</strong> <a href="https://doi.org/10.37473/dac/10.1002/jrsm.1540" target="_blank">PreregRS guides preregistration for research syntheses</a> (2022)</li>
<li><strong>[Journal of Neuroscience Methods]</strong> <a href="https://doi.org/10.1016/j.jneumeth.2023.109931" target="_blank">Methodical advances in reproducibility research</a> (2023)</li>
<li><strong>[Scientific Data]</strong> <a href="https://doi.org/10.1038/s41597-024-03559-8" target="_blank">Motion-BIDS extension for reproducible motion data</a> (2024)</li>
<li><strong>[Scientific Data]</strong> <a href="https://doi.org/10.1038/s41597-023-02614-0" target="_blank">A comparison of neuroelectrophysiology databases</a> (2023)</li>
<li><strong>[Epilepsia Open]</strong> <a href="https://doi.org/10.1002/epi4.12704" target="_blank">EEG datasets for seizure detection and prediction: a review</a> (2023)</li>
<li><strong>[eLife]</strong> <a href="https://doi.org/10.7554/eLife.85980" target="_blank">Enhancing precision in human neuroscience</a> (2023)</li>
<li><strong>[JAMA]</strong> <a href="https://doi.org/10.1001/jama.2025.13350" target="_blank">TARGET statement for transparent reporting</a> (2025)</li>
<li><strong>[BIDS]</strong> <a href="https://bids-specification.readthedocs.io/en/stable/" target="_blank">BIDS Specification 1.10.1</a> (2025更新版)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2311.04912" target="_blank">ezBIDS for curation and validation workflow</a> (2023)</li>
<li><strong>[Zenodo]</strong> <a href="https://zenodo.org/records/18201723" target="_blank">BEP036 draft metadata extension</a> (2025)</li>
</ol>
</section>

<section class="section" id="u15">
<h2 class="section-title">U15: 制度統合</h2>
<p><strong>厳密定義:</strong> 技術評価KPIと法/倫理KPIを連動させ、停止基準と公開基準を運用レベルで定義できるか。</p>
<h3>リサーチクエスチョン分解</h3>
<ol>
<li>神経データの機微性をどの法概念で扱うか（個人情報・生体情報・人格情報）。</li>
<li>neurorightsを技術監査項目へどう写像するか。</li>
<li>法域差（EU/US/JP等）を跨ぐ最小共通運用をどう定義するか。</li>
<li>技術進展に応じた停止条件・更新条件をどうガバナンス化するか。</li>
</ol>
<h3>今、解かれているもの（文献で積み上がっている領域）</h3>
<ul>
<li>neurorights・神経データ保護に関する政策議論と法案提案は拡大。</li>
<li>BCIプライバシー・安全性のリスク領域は比較的明確化。</li>
<li>AIガバナンス枠組みを神経技術へ接続する試みが増加。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.1007/978-3-030-72254-8_19" target="_blank">Privacy and Security in Brain-Computer Interfaces</a>、<a href="https://doi.org/10.1201/9781351231954-34" target="_blank">Privacy and Ethics in Brain-Computer Interface Research</a>、<a href="https://doi.org/10.1007/s11673-025-10440-9" target="_blank">Ethical Governance Strategies for the Responsible Innovation of Neurotechnologies</a>、<a href="https://doi.org/10.2196/56665" target="_blank">Ethics and Governance of Neurotechnology in Africa</a>。</p>
<h3>これから研究が必要なもの（未解決）</h3>
<ul>
<li>技術指標と法的停止基準を結びつけた実装規格が不足。</li>
<li>国際相互運用可能な監査テンプレートが未整備。</li>
<li>研究用途と商用用途の境界で運用ルールが分断。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.1017/9781009207898.029" target="_blank">Responsible AI Healthcare and Neurotechnology Governance</a>、<a href="https://doi.org/10.4337/9781786438515.00015" target="_blank">Social values and privacy law and policy</a>、<a href="https://api.openalex.org/W4200185524" target="_blank">On Neurorights</a>。</p>
<h3>主要先行研究（再精査 16 件）</h3>
<ol>
<li><strong>[EU Law]</strong> <a href="https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng" target="_blank">EU AI Act (Regulation (EU) 2024/1689)</a> (2024)</li>
<li><strong>[Lancet Neurology]</strong> <a href="https://doi.org/10.1016/S1474-4422(25)00124-3" target="_blank">Neurorights in neurology</a> (2025)</li>
<li><strong>[Journal of Human Rights Practice]</strong> <a href="https://doi.org/10.1093/jhuman/huae042" target="_blank">Establishing Neurorights: New Rights versus Derived Rights</a> (2024)</li>
<li><strong>[NIST]</strong> <a href="https://doi.org/10.6028/NIST.AI.600-1" target="_blank">NIST AI RMF: Generative AI Profile</a> (2024)</li>
<li><strong>[OECD]</strong> <a href="https://oecd.ai/en/ai-principles" target="_blank">OECD AI Principles</a> (運用中)</li>
<li><strong>[Council of Europe]</strong> <a href="https://book.coe.int/en/texts-of-council-of-europe-treaties/12225-council-of-europe-framework-convention-on-artificial-intelligence-and-human-rights-democracy-and-the-rule-of-law-cets-no-225.html" target="_blank">Framework Convention on AI (CETS No.225)</a> (2024)</li>
<li><strong>[ISO]</strong> <a href="https://www.iso.org/standard/42001" target="_blank">ISO/IEC 42001 AI management systems</a> (2023)</li>
<li><strong>[AISC]</strong> <a href="https://doi.org/10.1007/978-3-030-72254-8_19" target="_blank">Privacy and Security in Brain-Computer Interfaces</a> (2021)</li>
<li><strong>[Handbook Chapter]</strong> <a href="https://doi.org/10.1201/9781351231954-34" target="_blank">Privacy and Ethics in Brain-Computer Interface Research</a> (2018)</li>
<li><strong>[Bioethics]</strong> <a href="https://doi.org/10.1007/s11673-025-10440-9" target="_blank">Ethical Governance Strategies for Responsible Neurotechnology</a> (2025)</li>
<li><strong>[JMIR Neurotechnology]</strong> <a href="https://doi.org/10.2196/56665" target="_blank">Ethics and Governance of Neurotechnology in Africa: Lessons from AI</a> (2024)</li>
<li><strong>[Cambridge Handbook]</strong> <a href="https://doi.org/10.1017/9781009207898.029" target="_blank">Responsible AI Healthcare and Neurotechnology Governance</a> (2022)</li>
<li><strong>[Research Handbook]</strong> <a href="https://doi.org/10.4337/9781786438515.00015" target="_blank">Social values and privacy law and policy</a> (2022)</li>
<li><strong>[Frontiers]</strong> <a href="https://api.openalex.org/W4200185524" target="_blank">On Neurorights</a> (2021)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2407.14390v1" target="_blank">Honest Computing: demonstrable data lineage and provenance</a> (2024)</li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W4379053109" target="_blank">Equal access to mental augmentation</a> (2023)</li>
</ol>
</section>

</article>
<aside class="sidebar-column">
<div class="sidebar-box">
<h4>関連ページ</h4>
<ul>
<li><a href="verification.html">Verification Commons →</a></li>
<li><a href="tech_roadmap.html#unsolved">Roadmap: Unsolved Questions →</a></li>
<li><a href="mind_uploading_papers.html">Paper Archive →</a></li>
<li><a href="proposals.html">Technical Proposals →</a></li>
</ul>
</div>
<div class="note-box">
<strong>運用方針</strong>
<p>このページは『実体のある引用と未解決定義』を更新する場所です。実行不能な主提案ではなく、検証可能な差分と証跡を残します。</p>
</div>
</aside>
</main>
