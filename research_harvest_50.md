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
Round 1〜84 で実施した深掘り結果を本体運用へ統合しました。ここでは「どのUがどこまで深掘り済みか」を一覧化し、詳細は各Round文書へリンクします。
</p>
<table class="data-table">
<thead><tr><th>U</th><th>RQ総数</th><th>深掘り完了</th><th>主要反映ラウンド</th></tr></thead><tbody>
<tr><td>U0</td><td>4</td><td>4</td><td>Round 2, 9, 12, 13, 16, 17, 18</td></tr>
<tr><td>U1</td><td>4</td><td>4</td><td>Round 2, 9, 12, 13, 16, 17, 18</td></tr>
<tr><td>U3</td><td>6</td><td>6</td><td>Round 2, 9, 11, 13, 16, 17, 18</td></tr>
<tr><td>U4</td><td>4</td><td>4</td><td>Round 3, 9, 12, 13, 16, 17, 18</td></tr>
<tr><td>U7</td><td>6</td><td>6</td><td>Round 3, 9, 11, 13, 14, 16, 17, 18</td></tr>
<tr><td>U8</td><td>6</td><td>6</td><td>Round 4, 8, 12, 13, 16, 17, 18</td></tr>
<tr><td>U10</td><td>4</td><td>4</td><td>Round 5, 9, 12, 13, 14, 16, 17, 18</td></tr>
<tr><td>U11</td><td>4</td><td>4</td><td>Round 5, 9, 11, 13, 16, 17, 18</td></tr>
<tr><td>U12</td><td>6</td><td>6</td><td>Round 5, 9, 11, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84</td></tr>
<tr><td>U13</td><td>6</td><td>6</td><td>Round 6, 8, 12, 13, 16, 17, 18</td></tr>
<tr><td>U14</td><td>6</td><td>6</td><td>Round 6, 8, 12, 13, 14, 16, 17, 18</td></tr>
<tr><td>U15</td><td>4</td><td>4</td><td>Round 6, 8, 12, 13, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84</td></tr>
<tr><td><strong>合計</strong></td><td><strong>60</strong></td><td><strong>60</strong></td><td><strong>Round 1-84</strong></td></tr>
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
<li><a href="research_deepening_round9_2026-03-01.html">Round 9: U0/U1/U3/U4/U7/U10/U11/U12 参照置換の本体反映</a></li>
<li><a href="research_deepening_round10_2026-03-01.html">Round 10: 全60問いの必須2本＋補助1本（最小コアセット）</a></li>
<li><a href="research_deepening_round11_2026-03-01.html">Round 11: U3/U7/U11/U12 の問い別エビデンス追補</a></li>
<li><a href="research_deepening_round12_2026-03-01.html">Round 12: U0/U1/U4/U8/U10/U13/U14/U15 の問い別エビデンス追補</a></li>
<li><a href="research_deepening_round13_2026-03-01.html">Round 13: 補助文献品質点検と法制度リンク監査</a></li>
<li><a href="research_deepening_round14_2026-03-01.html">Round 14: 補助文献 preprint 置換（16件）</a></li>
<li><a href="research_deepening_round15_2026-03-01.html">Round 15: 法制度リンク差分監査（Round 13 比較）</a></li>
<li><a href="research_deepening_round16_2026-03-01.html">Round 16: 補助文献の実験/規制/運用タグ再分類</a></li>
<li><a href="research_deepening_round17_2026-03-01.html">Round 17: 参照二層化と3ステップ読了順</a></li>
<li><a href="research_deepening_round18_2026-03-01.html">Round 18: 読了時間目安と更新監査フラグ</a></li>
<li><a href="research_deepening_round19_2026-03-01.html">Round 19: U12 規制トラック整合</a></li>
<li><a href="research_deepening_round20_2026-03-01.html">Round 20: Regulation 法域ラベルと監査優先キュー</a></li>
<li><a href="research_deepening_round21_2026-03-01.html">Round 21: Highキュー法制度リンク差分監査</a></li>
<li><a href="research_deepening_round22_2026-03-01.html">Round 22: 本文更新テンプレ固定と改訂履歴リンク補完</a></li>
<li><a href="research_deepening_round23_2026-03-01.html">Round 23: U12/U15 本文への正規化差分実反映</a></li>
<li><a href="research_deepening_round24_2026-03-01.html">Round 24: 正規化後基準の差分監査（実体更新分離）</a></li>
<li><a href="research_deepening_round25_2026-03-01.html">Round 25: 問い別監査メモと次回監視スケジュール</a></li>
<li><a href="research_deepening_round26_2026-03-01.html">Round 26: access_path_change の再確認と問い別判定</a></li>
<li><a href="research_deepening_round27_2026-03-01.html">Round 27: 問い別本文更新テンプレと監査キーワード辞書</a></li>
<li><a href="research_deepening_round28_2026-03-01.html">Round 28: 外部依存タスク分離と適用準備度の固定</a></li>
<li><a href="research_deepening_round29_2026-03-01.html">Round 29: 再監視Runbookと差分トリガー行列の固定</a></li>
<li><a href="research_deepening_round30_2026-03-01.html">Round 30: 判定ログ様式と証跡パケット仕様の固定</a></li>
<li><a href="research_deepening_round31_2026-03-01.html">Round 31: 実行チェックリストと例外ハンドリング規則の固定</a></li>
<li><a href="research_deepening_round32_2026-03-01.html">Round 32: 監査品質スコアとフォローアップ行動行列の固定</a></li>
<li><a href="research_deepening_round33_2026-03-01.html">Round 33: 再監視バッチ計画と再検証受入基準の固定</a></li>
<li><a href="research_deepening_round34_2026-03-01.html">Round 34: 平易要約テンプレートと差分レジャー仕様の固定</a></li>
<li><a href="research_deepening_round35_2026-03-01.html">Round 35: 判定理由一貫性チェック表と最終報告テンプレートの固定</a></li>
<li><a href="research_deepening_round36_2026-03-01.html">Round 36: 複数ソース照合マップとエスカレーション規則の固定</a></li>
<li><a href="research_deepening_round37_2026-03-01.html">Round 37: 判定衝突解消行列と外部依存ハンドオフSLAの固定</a></li>
<li><a href="research_deepening_round38_2026-03-01.html">Round 38: 残余リスク登録表と検証証跡インデックスの固定</a></li>
<li><a href="research_deepening_round39_2026-03-01.html">Round 39: 証跡鮮度スコアと判定クローズ条件の固定</a></li>
<li><a href="research_deepening_round40_2026-03-01.html">Round 40: 監査バンドルマニフェストとreopenウォッチリストの固定</a></li>
<li><a href="research_deepening_round41_2026-03-01.html">Round 41: ハンドオフ完了証跡と未解決キュー管理の固定</a></li>
<li><a href="research_deepening_round42_2026-03-01.html">Round 42: 未解決キュー解消経路と追加証跡依頼ボードの固定</a></li>
<li><a href="research_deepening_round43_2026-03-01.html">Round 43: 受入条件ゲート判定ログと状態遷移台帳の固定</a></li>
<li><a href="research_deepening_round44_2026-03-01.html">Round 44: highレーン2回目判定とクローズ候補登録の固定</a></li>
<li><a href="research_deepening_round45_2026-03-01.html">Round 45: 最終報告転記ログとクローズ確定登録の固定</a></li>
<li><a href="research_deepening_round46_2026-03-01.html">Round 46: reopen優先監視ログと再開判定登録の固定</a></li>
<li><a href="research_deepening_round47_2026-03-01.html">Round 47: trigger変動ドリフト行列と再開エスカレーションキューの固定</a></li>
<li><a href="research_deepening_round48_2026-03-01.html">Round 48: 閾値再評価ログと再開判定監査の固定</a></li>
<li><a href="research_deepening_round49_2026-03-01.html">Round 49: 監視窓実行ログとraise判定ゲートの固定</a></li>
<li><a href="research_deepening_round50_2026-03-01.html">Round 50: 再開準備度スコアと監視ハンドオフチェックポイントの固定</a></li>
<li><a href="research_deepening_round51_2026-03-01.html">Round 51: 再開候補スクリーニングと監視継続コミットメントの固定</a></li>
<li><a href="research_deepening_round52_2026-03-01.html">Round 52: raise候補レビューと監視サイクル確約の固定</a></li>
<li><a href="research_deepening_round53_2026-03-01.html">Round 53: high先行実行順とraise移行証跡の固定</a></li>
<li><a href="research_deepening_round54_2026-03-01.html">Round 54: preflight固定とraise反映チェックポイント整備</a></li>
<li><a href="research_deepening_round55_2026-03-01.html">Round 55: 実行ログ雛形とkeep_watch繰越台帳の固定</a></li>
<li><a href="research_deepening_round56_2026-03-01.html">Round 56: raise判定トレース台帳と次サイクル引継ぎ固定</a></li>
<li><a href="research_deepening_round57_2026-03-01.html">Round 57: 証跡完全性チェックと公開反映ゲート固定</a></li>
<li><a href="research_deepening_round58_2026-03-01.html">Round 58: 公開適用キューとpending解消確認表の固定</a></li>
<li><a href="research_deepening_round59_2026-03-01.html">Round 59: 公開コミット台帳と保留繰越バックログ固定</a></li>
<li><a href="research_deepening_round60_2026-03-01.html">Round 60: 公開結果マトリクスと未解消エスカレーション登録固定</a></li>
<li><a href="research_deepening_round61_2026-03-01.html">Round 61: 公開実行チェックとエスカレーション解消計画固定</a></li>
<li><a href="research_deepening_round62_2026-03-01.html">Round 62: クローズ証明と再開ガード固定</a></li>
<li><a href="research_deepening_round63_2026-03-01.html">Round 63: クローズ維持スケジュールと再開候補トリアージ固定</a></li>
<li><a href="research_deepening_round64_2026-03-01.html">Round 64: クローズ一貫性監査と再開兆候監視固定</a></li>
<li><a href="research_deepening_round65_2026-03-01.html">Round 65: クローズドリフト対応と再開ハンドオフ固定</a></li>
<li><a href="research_deepening_round66_2026-03-01.html">Round 66: 再開再検証パケットと再クローズ判定ゲート固定</a></li>
<li><a href="research_deepening_round67_2026-03-01.html">Round 67: 再クローズ認証台帳と再開クールダウン監視固定</a></li>
<li><a href="research_deepening_round68_2026-03-01.html">Round 68: 安定状態チェックポイントと再開再入ゲート固定</a></li>
<li><a href="research_deepening_round69_2026-03-01.html">Round 69: 再入候補トリアージと再検証再接続ブリッジ固定</a></li>
<li><a href="research_deepening_round70_2026-03-01.html">Round 70: 再入実行パケットと再安定化復帰ゲート固定</a></li>
<li><a href="research_deepening_round71_2026-03-01.html">Round 71: 再安定化確認台帳と再クローズ復帰監視固定</a></li>
<li><a href="research_deepening_round72_2026-03-01.html">Round 72: 再入再接続チェックポイントと再開再入ゲート更新固定</a></li>
<li><a href="research_deepening_round73_2026-03-01.html">Round 73: 再入更新伝播台帳と再入実行再接続ゲート固定</a></li>
<li><a href="research_deepening_round74_2026-03-01.html">Round 74: 再接続実行チェックと再入候補再同期ゲート固定</a></li>
<li><a href="research_deepening_round75_2026-03-01.html">Round 75: 再同期実行台帳と再同期監視ゲート固定</a></li>
<li><a href="research_deepening_round76_2026-03-01.html">Round 76: 再同期更新台帳と再入監視再起動ゲート固定</a></li>
<li><a href="research_deepening_round77_2026-03-01.html">Round 77: 監視再起動台帳と再接続再開ゲート固定</a></li>
<li><a href="research_deepening_round78_2026-03-01.html">Round 78: 再開反映台帳と監視再連結ゲート固定</a></li>
<li><a href="research_deepening_round79_2026-03-01.html">Round 79: 再連結更新台帳と監視再同期再開ゲート固定</a></li>
<li><a href="research_deepening_round80_2026-03-01.html">Round 80: 再接続フィードバック台帳と監視再同期再点検ゲート固定</a></li>
<li><a href="research_deepening_round81_2026-03-01.html">Round 81: 再点検結果台帳と監視再同期維持ゲート固定</a></li>
<li><a href="research_deepening_round82_2026-03-01.html">Round 82: 再同期維持確認台帳と再接続再監視ゲート固定</a></li>
<li><a href="research_deepening_round83_2026-03-01.html">Round 83: 再監視実行台帳と再接続再評価ゲート固定</a></li>
<li><a href="research_deepening_round84_2026-03-01.html">Round 84: 再評価結果台帳と監視再同期再接続ゲート固定</a></li>
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
<p class="small">
Round 9 の実置換ログ（置換前後件数と反映先）は
<a href="automation/rq_reference_replacement_applied_round9_2026-03-01.csv" target="_blank">rq_reference_replacement_applied_round9_2026-03-01.csv</a>
に記録しています。
</p>
<p class="small">
Round 10 のRQ別最小コア文献セット（全60問い）は
<a href="automation/rq_core_reference_minset_round10_2026-03-01.csv" target="_blank">rq_core_reference_minset_round10_2026-03-01.csv</a>
に記録しています。
</p>
<p class="small">
Round 11 の問い別エビデンス追補（U3/U7/U11/U12, 22問い）は
<a href="automation/rq_question_specific_enrichment_round11_2026-03-01.csv" target="_blank">rq_question_specific_enrichment_round11_2026-03-01.csv</a>
に記録しています。
</p>
<p class="small">
Round 12 の問い別エビデンス追補（U0/U1/U4/U8/U10/U13/U14/U15, 38問い）は
<a href="automation/rq_question_specific_enrichment_round12_2026-03-01.csv" target="_blank">rq_question_specific_enrichment_round12_2026-03-01.csv</a>
に記録しています。
</p>
<p class="small">
Round 13 の補助文献品質点検（全60問い）は
<a href="automation/rq_supplementary_quality_audit_round13_2026-03-01.csv" target="_blank">rq_supplementary_quality_audit_round13_2026-03-01.csv</a>
に記録しています。
</p>
<p class="small">
Round 13 の法制度リンク更新日監査（5件）は
<a href="automation/rq_legal_link_freshness_round13_2026-03-01.csv" target="_blank">rq_legal_link_freshness_round13_2026-03-01.csv</a>
に記録しています。
</p>
<p class="small">
Round 14 の補助文献置換ログ（16件）は
<a href="automation/rq_supplementary_replacement_round14_2026-03-01.csv" target="_blank">rq_supplementary_replacement_round14_2026-03-01.csv</a>
に記録しています。
</p>
<p class="small">
Round 14 の置換後品質点検（全60問い）は
<a href="automation/rq_supplementary_quality_audit_round14_2026-03-01.csv" target="_blank">rq_supplementary_quality_audit_round14_2026-03-01.csv</a>
に記録しています。
</p>
<p class="small">
Round 15 の法制度リンク差分監査（Round 13 比較）は
<a href="automation/rq_legal_link_freshness_round15_2026-03-01.csv" target="_blank">rq_legal_link_freshness_round15_2026-03-01.csv</a>
に記録しています。
</p>
<p class="small">
Round 16 の補助文献タグ再分類（60問い）は
<a href="automation/rq_supplementary_thematic_tags_round16_2026-03-01.csv" target="_blank">rq_supplementary_thematic_tags_round16_2026-03-01.csv</a>
に記録しています。
</p>
<p class="small">
Round 16 のタグ集計は
<a href="automation/rq_supplementary_thematic_tag_summary_round16_2026-03-01.csv" target="_blank">rq_supplementary_thematic_tag_summary_round16_2026-03-01.csv</a>
に記録しています。
</p>
<p class="small">
Round 17 の参照二層化（必須/補助, 60問い）は
<a href="automation/rq_reference_layering_round17_2026-03-01.csv" target="_blank">rq_reference_layering_round17_2026-03-01.csv</a>
に記録しています。
</p>
<p class="small">
Round 17 のRQ別3ステップ読了順（60問い）は
<a href="automation/rq_minimal_reading_path_round17_2026-03-01.csv" target="_blank">rq_minimal_reading_path_round17_2026-03-01.csv</a>
に記録しています（集計:
<a href="automation/rq_reading_path_summary_round17_2026-03-01.csv" target="_blank">rq_reading_path_summary_round17_2026-03-01.csv</a>）。
</p>
<p class="small">
Round 18 の時間目安付き読了順（60問い）は
<a href="automation/rq_reading_path_timed_round18_2026-03-01.csv" target="_blank">rq_reading_path_timed_round18_2026-03-01.csv</a>
に記録しています（集計:
<a href="automation/rq_reading_path_timed_summary_round18_2026-03-01.csv" target="_blank">rq_reading_path_timed_summary_round18_2026-03-01.csv</a>）。
</p>
<p class="small">
Round 19 の U12 補助文献再配列ログ（6件）は
<a href="automation/rq_u12_regulation_alignment_round19_2026-03-01.csv" target="_blank">rq_u12_regulation_alignment_round19_2026-03-01.csv</a>
に記録しています。
</p>
<p class="small">
Round 19 の再計算結果（タグ/二層化/読了順/時間目安）は
<a href="automation/rq_supplementary_thematic_tags_round19_2026-03-01.csv" target="_blank">rq_supplementary_thematic_tags_round19_2026-03-01.csv</a>、
<a href="automation/rq_reference_layering_round19_2026-03-01.csv" target="_blank">rq_reference_layering_round19_2026-03-01.csv</a>、
<a href="automation/rq_minimal_reading_path_round19_2026-03-01.csv" target="_blank">rq_minimal_reading_path_round19_2026-03-01.csv</a>、
<a href="automation/rq_reading_path_timed_round19_2026-03-01.csv" target="_blank">rq_reading_path_timed_round19_2026-03-01.csv</a>
に記録しています。
</p>
<p class="small">
Round 20 の法域ラベル（U12/U15, 10問い）は
<a href="automation/rq_regulation_jurisdiction_labels_round20_2026-03-01.csv" target="_blank">rq_regulation_jurisdiction_labels_round20_2026-03-01.csv</a>
に記録しています。
</p>
<p class="small">
Round 20 の更新監査優先キュー（U12/U15, 10問い）は
<a href="automation/rq_regulation_update_priority_queue_round20_2026-03-01.csv" target="_blank">rq_regulation_update_priority_queue_round20_2026-03-01.csv</a>
に記録しています。
</p>
<p class="small">
Round 21 の highキュー法制度リンク差分監査（U12/U15, 10問い）は
<a href="automation/rq_regulation_link_diff_round21_2026-03-01.csv" target="_blank">rq_regulation_link_diff_round21_2026-03-01.csv</a>（URL単位）と
<a href="automation/rq_regulation_priority_queue_status_round21_2026-03-01.csv" target="_blank">rq_regulation_priority_queue_status_round21_2026-03-01.csv</a>（RQ単位）
に記録しています（URL差分2件、共有URL伝播でRQ判定10件）。
</p>
<p class="small">
Round 22 の本文更新テンプレ固定と改訂履歴リンク補完は
<a href="automation/rq_regulation_content_update_template_round22_2026-03-01.csv" target="_blank">rq_regulation_content_update_template_round22_2026-03-01.csv</a>（RQ本文更新テンプレ）と
<a href="automation/rq_regulation_revision_history_links_round22_2026-03-01.csv" target="_blank">rq_regulation_revision_history_links_round22_2026-03-01.csv</a>（制度文書の改訂履歴リンク）
に記録しています。
</p>
<p class="small">
Round 23 の U12/U15 本文への正規化差分実反映は
<a href="automation/rq_regulation_link_normalization_applied_round23_2026-03-01.csv" target="_blank">rq_regulation_link_normalization_applied_round23_2026-03-01.csv</a>（適用ログ）と
<a href="automation/rq_regulation_audit_trail_insertion_round23_2026-03-01.csv" target="_blank">rq_regulation_audit_trail_insertion_round23_2026-03-01.csv</a>（監査導線追加ログ）
に記録しています。
</p>
<p class="small">
Round 24 の正規化後基準差分監査（実体更新分離）は
<a href="automation/rq_regulation_link_diff_round24_2026-03-01.csv" target="_blank">rq_regulation_link_diff_round24_2026-03-01.csv</a>（URL単位）と
<a href="automation/rq_regulation_priority_queue_status_round24_2026-03-01.csv" target="_blank">rq_regulation_priority_queue_status_round24_2026-03-01.csv</a>（RQ単位）
に記録しています（実体更新0件、アクセス経路変動1件）。
</p>
<p class="small">
Round 25 の問い別監査メモと次回監視スケジュールは
<a href="automation/rq_regulation_rq_specific_audit_memo_round25_2026-03-01.csv" target="_blank">rq_regulation_rq_specific_audit_memo_round25_2026-03-01.csv</a>（RQ別メモ）と
<a href="automation/rq_regulation_monitor_schedule_round25_2026-03-01.csv" target="_blank">rq_regulation_monitor_schedule_round25_2026-03-01.csv</a>（次回監視予定日付き）
に記録しています。
</p>
<p class="small">
Round 26 の access_path_change 再確認と問い別判定は
<a href="automation/rq_regulation_access_recheck_round26_2026-03-01.csv" target="_blank">rq_regulation_access_recheck_round26_2026-03-01.csv</a>（URL再確認）、
<a href="automation/rq_regulation_question_decision_round26_2026-03-01.csv" target="_blank">rq_regulation_question_decision_round26_2026-03-01.csv</a>（問い別判定）、
<a href="automation/rq_regulation_monitor_schedule_round26_2026-03-01.csv" target="_blank">rq_regulation_monitor_schedule_round26_2026-03-01.csv</a>（更新後スケジュール）
に記録しています。
</p>
<p class="small">
Round 27 の問い別本文更新テンプレと監査キーワード辞書は
<a href="automation/rq_regulation_update_text_template_round27_2026-03-01.csv" target="_blank">rq_regulation_update_text_template_round27_2026-03-01.csv</a>（更新文テンプレ）と
<a href="automation/rq_regulation_source_checkpoint_phrase_bank_round27_2026-03-01.csv" target="_blank">rq_regulation_source_checkpoint_phrase_bank_round27_2026-03-01.csv</a>（監査キーワード辞書）
に記録しています。
</p>
<p class="small">
Round 28 の外部依存タスク分離と本文適用準備度の固定は
<a href="automation/rq_regulation_external_dependency_tasks_round28_2026-03-01.csv" target="_blank">rq_regulation_external_dependency_tasks_round28_2026-03-01.csv</a>（外部依存タスク分離）と
<a href="automation/rq_regulation_apply_readiness_round28_2026-03-01.csv" target="_blank">rq_regulation_apply_readiness_round28_2026-03-01.csv</a>（本文適用準備度）
に記録しています。
</p>
<p class="small">
Round 29 の再監視Runbookと差分トリガー行列の固定は
<a href="automation/rq_regulation_monitor_execution_runbook_round29_2026-03-01.csv" target="_blank">rq_regulation_monitor_execution_runbook_round29_2026-03-01.csv</a>（問い別再監視Runbook）と
<a href="automation/rq_regulation_diff_trigger_matrix_round29_2026-03-01.csv" target="_blank">rq_regulation_diff_trigger_matrix_round29_2026-03-01.csv</a>（問い別差分トリガー行列）
に記録しています。
</p>
<p class="small">
Round 30 の判定ログ様式と証跡パケット仕様の固定は
<a href="automation/rq_regulation_decision_log_template_round30_2026-03-01.csv" target="_blank">rq_regulation_decision_log_template_round30_2026-03-01.csv</a>（問い別判定ログ様式）と
<a href="automation/rq_regulation_evidence_packet_spec_round30_2026-03-01.csv" target="_blank">rq_regulation_evidence_packet_spec_round30_2026-03-01.csv</a>（問い別証跡パケット仕様）
に記録しています。
</p>
<p class="small">
Round 31 の実行チェックリストと例外ハンドリング規則の固定は
<a href="automation/rq_regulation_monitor_checklist_round31_2026-03-01.csv" target="_blank">rq_regulation_monitor_checklist_round31_2026-03-01.csv</a>（問い別実行チェックリスト）と
<a href="automation/rq_regulation_exception_handling_playbook_round31_2026-03-01.csv" target="_blank">rq_regulation_exception_handling_playbook_round31_2026-03-01.csv</a>（問い別例外ハンドリング規則）
に記録しています。
</p>
<p class="small">
Round 32 の監査品質スコアとフォローアップ行動行列の固定は
<a href="automation/rq_regulation_audit_quality_scoring_round32_2026-03-01.csv" target="_blank">rq_regulation_audit_quality_scoring_round32_2026-03-01.csv</a>（問い別監査品質スコア）と
<a href="automation/rq_regulation_followup_action_matrix_round32_2026-03-01.csv" target="_blank">rq_regulation_followup_action_matrix_round32_2026-03-01.csv</a>（問い別フォローアップ行動行列）
に記録しています。
</p>
<p class="small">
Round 33 の再監視バッチ計画と再検証受入基準の固定は
<a href="automation/rq_regulation_monitor_batch_plan_round33_2026-03-01.csv" target="_blank">rq_regulation_monitor_batch_plan_round33_2026-03-01.csv</a>（問い別再監視バッチ計画）と
<a href="automation/rq_regulation_revalidation_acceptance_round33_2026-03-01.csv" target="_blank">rq_regulation_revalidation_acceptance_round33_2026-03-01.csv</a>（問い別再検証受入基準）
に記録しています。
</p>
<p class="small">
Round 34 の平易要約テンプレートと差分レジャー仕様の固定は
<a href="automation/rq_regulation_monitor_plain_summary_template_round34_2026-03-01.csv" target="_blank">rq_regulation_monitor_plain_summary_template_round34_2026-03-01.csv</a>（問い別平易要約テンプレート）と
<a href="automation/rq_regulation_text_diff_ledger_spec_round34_2026-03-01.csv" target="_blank">rq_regulation_text_diff_ledger_spec_round34_2026-03-01.csv</a>（問い別差分レジャー仕様）
に記録しています。
</p>
<p class="small">
Round 35 の判定理由一貫性チェック表と最終報告テンプレートの固定は
<a href="automation/rq_regulation_reason_consistency_check_round35_2026-03-01.csv" target="_blank">rq_regulation_reason_consistency_check_round35_2026-03-01.csv</a>（問い別判定理由一貫性チェック表）と
<a href="automation/rq_regulation_final_report_template_round35_2026-03-01.csv" target="_blank">rq_regulation_final_report_template_round35_2026-03-01.csv</a>（問い別最終報告テンプレート）
に記録しています。
</p>
<p class="small">
Round 36 の複数ソース照合マップとエスカレーション規則の固定は
<a href="automation/rq_regulation_cross_source_evidence_map_round36_2026-03-01.csv" target="_blank">rq_regulation_cross_source_evidence_map_round36_2026-03-01.csv</a>（問い別複数ソース照合マップ）と
<a href="automation/rq_regulation_escalation_trigger_rules_round36_2026-03-01.csv" target="_blank">rq_regulation_escalation_trigger_rules_round36_2026-03-01.csv</a>（問い別エスカレーション規則）
に記録しています。
</p>
<p class="small">
Round 37 の判定衝突解消行列と外部依存ハンドオフSLAの固定は
<a href="automation/rq_regulation_conflict_resolution_matrix_round37_2026-03-01.csv" target="_blank">rq_regulation_conflict_resolution_matrix_round37_2026-03-01.csv</a>（問い別判定衝突解消行列）と
<a href="automation/rq_regulation_external_handoff_sla_round37_2026-03-01.csv" target="_blank">rq_regulation_external_handoff_sla_round37_2026-03-01.csv</a>（問い別外部依存ハンドオフSLA）
に記録しています。
</p>
<p class="small">
Round 38 の残余リスク登録表と検証証跡インデックスの固定は
<a href="automation/rq_regulation_residual_risk_register_round38_2026-03-01.csv" target="_blank">rq_regulation_residual_risk_register_round38_2026-03-01.csv</a>（問い別残余リスク登録表）と
<a href="automation/rq_regulation_verification_artifact_index_round38_2026-03-01.csv" target="_blank">rq_regulation_verification_artifact_index_round38_2026-03-01.csv</a>（問い別検証証跡インデックス）
に記録しています。
</p>
<p class="small">
Round 39 の証跡鮮度スコアと判定クローズ条件の固定は
<a href="automation/rq_regulation_evidence_freshness_score_round39_2026-03-01.csv" target="_blank">rq_regulation_evidence_freshness_score_round39_2026-03-01.csv</a>（問い別証跡鮮度スコア）と
<a href="automation/rq_regulation_decision_closure_checklist_round39_2026-03-01.csv" target="_blank">rq_regulation_decision_closure_checklist_round39_2026-03-01.csv</a>（問い別判定クローズ条件）
に記録しています。
</p>
<p class="small">
Round 40 の監査バンドルマニフェストとreopenウォッチリストの固定は
<a href="automation/rq_regulation_audit_bundle_manifest_round40_2026-03-01.csv" target="_blank">rq_regulation_audit_bundle_manifest_round40_2026-03-01.csv</a>（問い別監査バンドルマニフェスト）と
<a href="automation/rq_regulation_reopen_watchlist_round40_2026-03-01.csv" target="_blank">rq_regulation_reopen_watchlist_round40_2026-03-01.csv</a>（問い別reopenウォッチリスト）
に記録しています。
</p>
<p class="small">
Round 41 のハンドオフ完了証跡と未解決キュー管理の固定は
<a href="automation/rq_regulation_handoff_completion_certificate_round41_2026-03-01.csv" target="_blank">rq_regulation_handoff_completion_certificate_round41_2026-03-01.csv</a>（問い別ハンドオフ完了証跡）と
<a href="automation/rq_regulation_unresolved_issue_queue_round41_2026-03-01.csv" target="_blank">rq_regulation_unresolved_issue_queue_round41_2026-03-01.csv</a>（問い別未解決キュー）
に記録しています。
</p>
<p class="small">
Round 42 の未解決キュー解消経路と追加証跡依頼ボードの固定は
<a href="automation/rq_regulation_resolution_path_round42_2026-03-01.csv" target="_blank">rq_regulation_resolution_path_round42_2026-03-01.csv</a>（問い別解消経路）と
<a href="automation/rq_regulation_evidence_request_board_round42_2026-03-01.csv" target="_blank">rq_regulation_evidence_request_board_round42_2026-03-01.csv</a>（問い別追加証跡依頼ボード）
に記録しています。
</p>
<p class="small">
Round 43 の受入条件ゲート判定ログと状態遷移台帳の固定は
<a href="automation/rq_regulation_acceptance_gate_check_round43_2026-03-01.csv" target="_blank">rq_regulation_acceptance_gate_check_round43_2026-03-01.csv</a>（問い別受入条件ゲート判定）と
<a href="automation/rq_regulation_state_transition_ledger_round43_2026-03-01.csv" target="_blank">rq_regulation_state_transition_ledger_round43_2026-03-01.csv</a>（問い別状態遷移台帳）
に記録しています。
</p>
<p class="small">
Round 44 のhighレーン2回目判定とクローズ候補登録の固定は
<a href="automation/rq_regulation_high_lane_second_pass_round44_2026-03-01.csv" target="_blank">rq_regulation_high_lane_second_pass_round44_2026-03-01.csv</a>（問い別2回目判定ログ）と
<a href="automation/rq_regulation_close_candidate_register_round44_2026-03-01.csv" target="_blank">rq_regulation_close_candidate_register_round44_2026-03-01.csv</a>（問い別クローズ候補登録）
に記録しています。
</p>
<p class="small">
Round 45 の最終報告転記ログとクローズ確定登録の固定は
<a href="automation/rq_regulation_final_report_reflection_log_round45_2026-03-01.csv" target="_blank">rq_regulation_final_report_reflection_log_round45_2026-03-01.csv</a>（問い別最終報告転記ログ）と
<a href="automation/rq_regulation_closure_confirmation_register_round45_2026-03-01.csv" target="_blank">rq_regulation_closure_confirmation_register_round45_2026-03-01.csv</a>（問い別クローズ確定登録）
に記録しています。
</p>
<p class="small">
Round 46 のreopen優先監視ログと再開判定登録の固定は
<a href="automation/rq_regulation_reopen_priority_monitor_round46_2026-03-01.csv" target="_blank">rq_regulation_reopen_priority_monitor_round46_2026-03-01.csv</a>（問い別reopen優先監視ログ）と
<a href="automation/rq_regulation_reopen_decision_register_round46_2026-03-01.csv" target="_blank">rq_regulation_reopen_decision_register_round46_2026-03-01.csv</a>（問い別再開判定登録）
に記録しています。
</p>
<p class="small">
Round 47 のtrigger変動ドリフト行列と再開エスカレーションキューの固定は
<a href="automation/rq_regulation_trigger_drift_matrix_round47_2026-03-01.csv" target="_blank">rq_regulation_trigger_drift_matrix_round47_2026-03-01.csv</a>（問い別trigger変動ドリフト行列）と
<a href="automation/rq_regulation_reopen_escalation_queue_round47_2026-03-01.csv" target="_blank">rq_regulation_reopen_escalation_queue_round47_2026-03-01.csv</a>（問い別再開エスカレーションキュー）
に記録しています。
</p>
<p class="small">
Round 48 の閾値再評価ログと再開判定監査の固定は
<a href="automation/rq_regulation_threshold_recheck_round48_2026-03-01.csv" target="_blank">rq_regulation_threshold_recheck_round48_2026-03-01.csv</a>（問い別閾値再評価ログ）と
<a href="automation/rq_regulation_reopen_decision_audit_round48_2026-03-01.csv" target="_blank">rq_regulation_reopen_decision_audit_round48_2026-03-01.csv</a>（問い別再開判定監査）
に記録しています。
</p>
<p class="small">
Round 49 の監視窓実行ログとraise判定ゲートの固定は
<a href="automation/rq_regulation_watch_window_execution_round49_2026-03-01.csv" target="_blank">rq_regulation_watch_window_execution_round49_2026-03-01.csv</a>（問い別監視窓実行ログ）と
<a href="automation/rq_regulation_raise_gate_criteria_round49_2026-03-01.csv" target="_blank">rq_regulation_raise_gate_criteria_round49_2026-03-01.csv</a>（問い別raise判定ゲート）
に記録しています。
</p>
<p class="small">
Round 50 の再開準備度スコアと監視ハンドオフチェックポイントの固定は
<a href="automation/rq_regulation_reopen_readiness_score_round50_2026-03-01.csv" target="_blank">rq_regulation_reopen_readiness_score_round50_2026-03-01.csv</a>（問い別再開準備度スコア）と
<a href="automation/rq_regulation_watch_handoff_checkpoint_round50_2026-03-01.csv" target="_blank">rq_regulation_watch_handoff_checkpoint_round50_2026-03-01.csv</a>（問い別監視ハンドオフチェックポイント）
に記録しています。
</p>
<p class="small">
Round 51 の再開候補スクリーニングと監視継続コミットメントの固定は
<a href="automation/rq_regulation_reopen_candidate_screening_round51_2026-03-01.csv" target="_blank">rq_regulation_reopen_candidate_screening_round51_2026-03-01.csv</a>（問い別再開候補スクリーニング）と
<a href="automation/rq_regulation_monitor_continuity_commitment_round51_2026-03-01.csv" target="_blank">rq_regulation_monitor_continuity_commitment_round51_2026-03-01.csv</a>（問い別監視継続コミットメント）
に記録しています。
</p>
<p class="small">
Round 52 のraise候補レビューと監視サイクル確約の固定は
<a href="automation/rq_regulation_raise_candidate_review_round52_2026-03-01.csv" target="_blank">rq_regulation_raise_candidate_review_round52_2026-03-01.csv</a>（問い別raise候補レビュー）と
<a href="automation/rq_regulation_watch_cycle_commitment_round52_2026-03-01.csv" target="_blank">rq_regulation_watch_cycle_commitment_round52_2026-03-01.csv</a>（問い別監視サイクル確約）
に記録しています。
</p>
<p class="small">
Round 53 のhigh先行実行順とraise移行証跡の固定は
<a href="automation/rq_regulation_high_lane_execution_round53_2026-03-01.csv" target="_blank">rq_regulation_high_lane_execution_round53_2026-03-01.csv</a>（問い別high先行実行順）と
<a href="automation/rq_regulation_raise_transition_packet_round53_2026-03-01.csv" target="_blank">rq_regulation_raise_transition_packet_round53_2026-03-01.csv</a>（問い別raise移行証跡パケット）
に記録しています。
</p>
<p class="small">
Round 54 のpreflight固定とraise反映チェックポイント整備は
<a href="automation/rq_regulation_high_lane_preflight_round54_2026-03-01.csv" target="_blank">rq_regulation_high_lane_preflight_round54_2026-03-01.csv</a>（問い別preflight固定）と
<a href="automation/rq_regulation_raise_apply_checkpoint_round54_2026-03-01.csv" target="_blank">rq_regulation_raise_apply_checkpoint_round54_2026-03-01.csv</a>（問い別raise反映チェックポイント）
に記録しています。
</p>
<p class="small">
Round 55 の実行ログ雛形とkeep_watch繰越台帳の固定は
<a href="automation/rq_regulation_window_execution_log_round55_2026-03-01.csv" target="_blank">rq_regulation_window_execution_log_round55_2026-03-01.csv</a>（問い別実行ログ雛形）と
<a href="automation/rq_regulation_keep_watch_rollover_round55_2026-03-01.csv" target="_blank">rq_regulation_keep_watch_rollover_round55_2026-03-01.csv</a>（問い別keep_watch繰越台帳）
に記録しています。
</p>
<p class="small">
Round 56 のraise判定トレース台帳と次サイクル引継ぎ固定は
<a href="automation/rq_regulation_raise_decision_trace_round56_2026-03-01.csv" target="_blank">rq_regulation_raise_decision_trace_round56_2026-03-01.csv</a>（問い別raise判定トレース台帳）と
<a href="automation/rq_regulation_cycle_handoff_manifest_round56_2026-03-01.csv" target="_blank">rq_regulation_cycle_handoff_manifest_round56_2026-03-01.csv</a>（問い別次サイクル引継ぎマニフェスト）
に記録しています。
</p>
<p class="small">
Round 57 の証跡完全性チェックと公開反映ゲート固定は
<a href="automation/rq_regulation_evidence_completeness_round57_2026-03-01.csv" target="_blank">rq_regulation_evidence_completeness_round57_2026-03-01.csv</a>（問い別証跡完全性チェック）と
<a href="automation/rq_regulation_publish_gate_round57_2026-03-01.csv" target="_blank">rq_regulation_publish_gate_round57_2026-03-01.csv</a>（問い別公開反映ゲート）
に記録しています。
</p>
<p class="small">
Round 58 の公開適用キューとpending解消確認表の固定は
<a href="automation/rq_regulation_publish_apply_queue_round58_2026-03-01.csv" target="_blank">rq_regulation_publish_apply_queue_round58_2026-03-01.csv</a>（問い別公開適用キュー）と
<a href="automation/rq_regulation_pending_review_resolution_round58_2026-03-01.csv" target="_blank">rq_regulation_pending_review_resolution_round58_2026-03-01.csv</a>（問い別pending解消確認表）
に記録しています。
</p>
<p class="small">
Round 59 の公開コミット台帳と保留繰越バックログ固定は
<a href="automation/rq_regulation_publish_commit_ledger_round59_2026-03-01.csv" target="_blank">rq_regulation_publish_commit_ledger_round59_2026-03-01.csv</a>（問い別公開コミット台帳）と
<a href="automation/rq_regulation_pending_carryover_backlog_round59_2026-03-01.csv" target="_blank">rq_regulation_pending_carryover_backlog_round59_2026-03-01.csv</a>（問い別保留繰越バックログ）
に記録しています。
</p>
<p class="small">
Round 60 の公開結果マトリクスと未解消エスカレーション登録固定は
<a href="automation/rq_regulation_publish_outcome_matrix_round60_2026-03-01.csv" target="_blank">rq_regulation_publish_outcome_matrix_round60_2026-03-01.csv</a>（問い別公開結果マトリクス）と
<a href="automation/rq_regulation_unresolved_escalation_register_round60_2026-03-01.csv" target="_blank">rq_regulation_unresolved_escalation_register_round60_2026-03-01.csv</a>（問い別未解消エスカレーション登録）
に記録しています。
</p>
<p class="small">
Round 61 の公開実行チェックとエスカレーション解消計画固定は
<a href="automation/rq_regulation_outcome_execution_check_round61_2026-03-01.csv" target="_blank">rq_regulation_outcome_execution_check_round61_2026-03-01.csv</a>（問い別公開実行チェック表）と
<a href="automation/rq_regulation_escalation_closure_plan_round61_2026-03-01.csv" target="_blank">rq_regulation_escalation_closure_plan_round61_2026-03-01.csv</a>（問い別エスカレーション解消計画）
に記録しています。
</p>
<p class="small">
Round 62 のクローズ証明と再開ガード固定は
<a href="automation/rq_regulation_closure_certification_round62_2026-03-01.csv" target="_blank">rq_regulation_closure_certification_round62_2026-03-01.csv</a>（問い別クローズ証明チェック）と
<a href="automation/rq_regulation_reopen_guard_round62_2026-03-01.csv" target="_blank">rq_regulation_reopen_guard_round62_2026-03-01.csv</a>（問い別再開ガード条件）
に記録しています。
</p>
<p class="small">
Round 63 のクローズ維持スケジュールと再開候補トリアージ固定は
<a href="automation/rq_regulation_closure_maintenance_schedule_round63_2026-03-01.csv" target="_blank">rq_regulation_closure_maintenance_schedule_round63_2026-03-01.csv</a>（問い別クローズ維持スケジュール）と
<a href="automation/rq_regulation_reopen_candidate_triage_round63_2026-03-01.csv" target="_blank">rq_regulation_reopen_candidate_triage_round63_2026-03-01.csv</a>（問い別再開候補トリアージ）
に記録しています。
</p>
<p class="small">
Round 64 のクローズ一貫性監査と再開兆候監視固定は
<a href="automation/rq_regulation_closure_consistency_audit_round64_2026-03-01.csv" target="_blank">rq_regulation_closure_consistency_audit_round64_2026-03-01.csv</a>（問い別クローズ一貫性監査）と
<a href="automation/rq_regulation_reopen_watch_signal_round64_2026-03-01.csv" target="_blank">rq_regulation_reopen_watch_signal_round64_2026-03-01.csv</a>（問い別再開兆候監視）
に記録しています。
</p>
<p class="small">
Round 65 のクローズドリフト対応と再開ハンドオフ固定は
<a href="automation/rq_regulation_closure_drift_response_round65_2026-03-01.csv" target="_blank">rq_regulation_closure_drift_response_round65_2026-03-01.csv</a>（問い別クローズドリフト対応行列）と
<a href="automation/rq_regulation_reopen_escalation_handoff_round65_2026-03-01.csv" target="_blank">rq_regulation_reopen_escalation_handoff_round65_2026-03-01.csv</a>（問い別再開エスカレーション引継ぎ）
に記録しています。
</p>
<p class="small">
Round 66 の再開再検証パケットと再クローズ判定ゲート固定は
<a href="automation/rq_regulation_reopen_revalidation_packet_round66_2026-03-01.csv" target="_blank">rq_regulation_reopen_revalidation_packet_round66_2026-03-01.csv</a>（問い別再開再検証パケット）と
<a href="automation/rq_regulation_reclose_decision_gate_round66_2026-03-01.csv" target="_blank">rq_regulation_reclose_decision_gate_round66_2026-03-01.csv</a>（問い別再クローズ判定ゲート）
に記録しています。
</p>
<p class="small">
Round 67 の再クローズ認証台帳と再開クールダウン監視固定は
<a href="automation/rq_regulation_reclose_certification_ledger_round67_2026-03-01.csv" target="_blank">rq_regulation_reclose_certification_ledger_round67_2026-03-01.csv</a>（問い別再クローズ認証台帳）と
<a href="automation/rq_regulation_reopen_cooldown_watch_round67_2026-03-01.csv" target="_blank">rq_regulation_reopen_cooldown_watch_round67_2026-03-01.csv</a>（問い別再開クールダウン監視）
に記録しています。
</p>
<p class="small">
Round 68 の安定状態チェックポイントと再開再入ゲート固定は
<a href="automation/rq_regulation_stable_state_checkpoint_round68_2026-03-01.csv" target="_blank">rq_regulation_stable_state_checkpoint_round68_2026-03-01.csv</a>（問い別安定状態チェックポイント）と
<a href="automation/rq_regulation_reopen_reentry_gate_round68_2026-03-01.csv" target="_blank">rq_regulation_reopen_reentry_gate_round68_2026-03-01.csv</a>（問い別再開再入ゲート）
に記録しています。
</p>
<p class="small">
Round 69 の再入候補トリアージと再検証再接続ブリッジ固定は
<a href="automation/rq_regulation_reentry_candidate_triage_round69_2026-03-01.csv" target="_blank">rq_regulation_reentry_candidate_triage_round69_2026-03-01.csv</a>（問い別再入候補トリアージ）と
<a href="automation/rq_regulation_revalidation_reconnect_bridge_round69_2026-03-01.csv" target="_blank">rq_regulation_revalidation_reconnect_bridge_round69_2026-03-01.csv</a>（問い別再検証再接続ブリッジ）
に記録しています。
</p>
<p class="small">
Round 70 の再入実行パケットと再安定化復帰ゲート固定は
<a href="automation/rq_regulation_reentry_execution_packet_round70_2026-03-01.csv" target="_blank">rq_regulation_reentry_execution_packet_round70_2026-03-01.csv</a>（問い別再入実行パケット）と
<a href="automation/rq_regulation_restabilization_return_gate_round70_2026-03-01.csv" target="_blank">rq_regulation_restabilization_return_gate_round70_2026-03-01.csv</a>（問い別再安定化復帰ゲート）
に記録しています。
</p>
<p class="small">
Round 71 の再安定化確認台帳と再クローズ復帰監視固定は
<a href="automation/rq_regulation_restabilization_confirmation_ledger_round71_2026-03-01.csv" target="_blank">rq_regulation_restabilization_confirmation_ledger_round71_2026-03-01.csv</a>（問い別再安定化確認台帳）と
<a href="automation/rq_regulation_reclose_return_watch_round71_2026-03-01.csv" target="_blank">rq_regulation_reclose_return_watch_round71_2026-03-01.csv</a>（問い別再クローズ復帰監視）
に記録しています。
</p>
<p class="small">
Round 72 の再入再接続チェックポイントと再開再入ゲート更新固定は
<a href="automation/rq_regulation_reentry_reconnect_checkpoint_round72_2026-03-01.csv" target="_blank">rq_regulation_reentry_reconnect_checkpoint_round72_2026-03-01.csv</a>（問い別再入再接続チェックポイント）と
<a href="automation/rq_regulation_reopen_reentry_gate_refresh_round72_2026-03-01.csv" target="_blank">rq_regulation_reopen_reentry_gate_refresh_round72_2026-03-01.csv</a>（問い別再開再入ゲート更新）
に記録しています。
</p>
<p class="small">
Round 73 の再入更新伝播台帳と再入実行再接続ゲート固定は
<a href="automation/rq_regulation_reentry_update_propagation_ledger_round73_2026-03-01.csv" target="_blank">rq_regulation_reentry_update_propagation_ledger_round73_2026-03-01.csv</a>（問い別再入更新伝播台帳）と
<a href="automation/rq_regulation_reentry_execution_relink_gate_round73_2026-03-01.csv" target="_blank">rq_regulation_reentry_execution_relink_gate_round73_2026-03-01.csv</a>（問い別再入実行再接続ゲート）
に記録しています。
</p>
<p class="small">
Round 74 の再接続実行チェックと再入候補再同期ゲート固定は
<a href="automation/rq_regulation_reentry_relink_execution_check_round74_2026-03-01.csv" target="_blank">rq_regulation_reentry_relink_execution_check_round74_2026-03-01.csv</a>（問い別再接続実行チェック）と
<a href="automation/rq_regulation_reentry_candidate_resync_gate_round74_2026-03-01.csv" target="_blank">rq_regulation_reentry_candidate_resync_gate_round74_2026-03-01.csv</a>（問い別再入候補再同期ゲート）
に記録しています。
</p>
<p class="small">
Round 75 の再同期実行台帳と再同期監視ゲート固定は
<a href="automation/rq_regulation_reentry_resync_execution_ledger_round75_2026-03-01.csv" target="_blank">rq_regulation_reentry_resync_execution_ledger_round75_2026-03-01.csv</a>（問い別再同期実行台帳）と
<a href="automation/rq_regulation_reentry_watch_resync_gate_round75_2026-03-01.csv" target="_blank">rq_regulation_reentry_watch_resync_gate_round75_2026-03-01.csv</a>（問い別再同期監視ゲート）
に記録しています。
</p>
<p class="small">
Round 76 の再同期更新台帳と再入監視再起動ゲート固定は
<a href="automation/rq_regulation_reentry_resync_update_ledger_round76_2026-03-01.csv" target="_blank">rq_regulation_reentry_resync_update_ledger_round76_2026-03-01.csv</a>（問い別再同期更新台帳）と
<a href="automation/rq_regulation_reentry_watch_restart_gate_round76_2026-03-01.csv" target="_blank">rq_regulation_reentry_watch_restart_gate_round76_2026-03-01.csv</a>（問い別再入監視再起動ゲート）
に記録しています。
</p>
<p class="small">
Round 77 の監視再起動台帳と再接続再開ゲート固定は
<a href="automation/rq_regulation_reentry_watch_restart_ledger_round77_2026-03-01.csv" target="_blank">rq_regulation_reentry_watch_restart_ledger_round77_2026-03-01.csv</a>（問い別監視再起動台帳）と
<a href="automation/rq_regulation_reentry_reconnect_resume_gate_round77_2026-03-01.csv" target="_blank">rq_regulation_reentry_reconnect_resume_gate_round77_2026-03-01.csv</a>（問い別再接続再開ゲート）
に記録しています。
</p>
<p class="small">
Round 78 の再開反映台帳と監視再連結ゲート固定は
<a href="automation/rq_regulation_reconnect_resume_update_ledger_round78_2026-03-01.csv" target="_blank">rq_regulation_reconnect_resume_update_ledger_round78_2026-03-01.csv</a>（問い別再開反映台帳）と
<a href="automation/rq_regulation_reentry_watch_relink_gate_round78_2026-03-01.csv" target="_blank">rq_regulation_reentry_watch_relink_gate_round78_2026-03-01.csv</a>（問い別監視再連結ゲート）
に記録しています。
</p>
<p class="small">
Round 79 の再連結更新台帳と監視再同期再開ゲート固定は
<a href="automation/rq_regulation_reentry_relink_update_ledger_round79_2026-03-01.csv" target="_blank">rq_regulation_reentry_relink_update_ledger_round79_2026-03-01.csv</a>（問い別再連結更新台帳）と
<a href="automation/rq_regulation_reentry_watch_resync_resume_gate_round79_2026-03-01.csv" target="_blank">rq_regulation_reentry_watch_resync_resume_gate_round79_2026-03-01.csv</a>（問い別監視再同期再開ゲート）
に記録しています。
</p>
<p class="small">
Round 80 の再接続フィードバック台帳と監視再同期再点検ゲート固定は
<a href="automation/rq_regulation_reentry_reconnect_feedback_ledger_round80_2026-03-01.csv" target="_blank">rq_regulation_reentry_reconnect_feedback_ledger_round80_2026-03-01.csv</a>（問い別再接続フィードバック台帳）と
<a href="automation/rq_regulation_reentry_watch_resync_recheck_gate_round80_2026-03-01.csv" target="_blank">rq_regulation_reentry_watch_resync_recheck_gate_round80_2026-03-01.csv</a>（問い別監視再同期再点検ゲート）
に記録しています。
</p>
<p class="small">
Round 81 の再点検結果台帳と監視再同期維持ゲート固定は
<a href="automation/rq_regulation_reentry_recheck_outcome_ledger_round81_2026-03-01.csv" target="_blank">rq_regulation_reentry_recheck_outcome_ledger_round81_2026-03-01.csv</a>（問い別再点検結果台帳）と
<a href="automation/rq_regulation_reentry_watch_resync_stability_gate_round81_2026-03-01.csv" target="_blank">rq_regulation_reentry_watch_resync_stability_gate_round81_2026-03-01.csv</a>（問い別監視再同期維持ゲート）
に記録しています。
</p>
<p class="small">
Round 82 の再同期維持確認台帳と再接続再監視ゲート固定は
<a href="automation/rq_regulation_reentry_resync_stability_confirmation_ledger_round82_2026-03-01.csv" target="_blank">rq_regulation_reentry_resync_stability_confirmation_ledger_round82_2026-03-01.csv</a>（問い別再同期維持確認台帳）と
<a href="automation/rq_regulation_reentry_reconnect_remonitor_gate_round82_2026-03-01.csv" target="_blank">rq_regulation_reentry_reconnect_remonitor_gate_round82_2026-03-01.csv</a>（問い別再接続再監視ゲート）
に記録しています。
</p>
<p class="small">
Round 83 の再監視実行台帳と再接続再評価ゲート固定は
<a href="automation/rq_regulation_reentry_remonitor_execution_ledger_round83_2026-03-01.csv" target="_blank">rq_regulation_reentry_remonitor_execution_ledger_round83_2026-03-01.csv</a>（問い別再監視実行台帳）と
<a href="automation/rq_regulation_reentry_reconnect_reevaluation_gate_round83_2026-03-01.csv" target="_blank">rq_regulation_reentry_reconnect_reevaluation_gate_round83_2026-03-01.csv</a>（問い別再接続再評価ゲート）
に記録しています。
</p>
<p class="small">
Round 84 の再評価結果台帳と監視再同期再接続ゲート固定は
<a href="automation/rq_regulation_reentry_reevaluation_outcome_ledger_round84_2026-03-01.csv" target="_blank">rq_regulation_reentry_reevaluation_outcome_ledger_round84_2026-03-01.csv</a>（問い別再評価結果台帳）と
<a href="automation/rq_regulation_reentry_watch_resync_reconnect_gate_round84_2026-03-01.csv" target="_blank">rq_regulation_reentry_watch_resync_reconnect_gate_round84_2026-03-01.csv</a>（問い別監視再同期再接続ゲート）
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
<h3>主要先行研究（再精査 12 件）</h3>
<ol>
<li><strong>[Cambridge]</strong> <a href="https://doi.org/10.1017/9781009486309.002" target="_blank">The Right to Personal Identity</a> (2026)</li>
<li><strong>[OSF]</strong> <a href="https://doi.org/10.31219/osf.io/sr7cf" target="_blank">Nondestructive Mind Uploading and the Stream of Consciousness</a> (2023)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2510.15745" target="_blank">State of Brain Emulation Report 2025</a> (2025)</li>
<li><strong>[Oxford]</strong> <a href="https://doi.org/10.1093/acprof:oso/9780198754855.003.0013" target="_blank">Enhancement, Mind-Uploading, and Personal Identity</a> (2016)</li>
<li><strong>[Cambridge]</strong> <a href="https://doi.org/10.1017/9781009367059.009" target="_blank">Personal Ontology and Life after Death, Part 2: Mind Uploading</a> (2024)</li>
<li><strong>[Synthese]</strong> <a href="https://doi.org/10.1007/s11229-024-04744-3" target="_blank">I am no abstract object</a> (2024)</li>
<li><strong>[SSRN]</strong> <a href="https://doi.org/10.2139/ssrn.2596460" target="_blank">The Fallacy of Favoring Gradual Replacement Mind Uploading Over Scan-and-Copy</a> (2015)</li>
<li><strong>[OSF]</strong> <a href="https://doi.org/10.31219/osf.io/zw3v4" target="_blank">The Fallacy of Favoring Gradual Replacement Mind Uploading Over Scan-and-Copy</a> (2023)</li>
<li><strong>[MIT Press]</strong> <a href="https://doi.org/10.7551/mitpress/10366.003.0009" target="_blank">Continuity: Kinks Not Breaks</a> (2017)</li>
<li><strong>[MIT Press]</strong> <a href="https://doi.org/10.7551/mitpress/10058.003.0005" target="_blank">Whole Brain Emulation</a> (2015)</li>
<li><strong>[Patterns]</strong> <a href="https://doi.org/10.1016/j.patter.2023.100861" target="_blank">No legal personhood for AI</a> (2023)</li>
<li><strong>[Minds and Machines]</strong> <a href="https://doi.org/10.1007/s11023-014-9352-8" target="_blank">Uploading and Branching Identity</a> (2014)</li>
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
<h3>主要先行研究（再精査 14 件）</h3>
<ol>
<li><strong>[IEEE Sensors Journal]</strong> <a href="https://doi.org/10.1109/JSEN.2024.3502917" target="_blank">Inverse Problem for M/EEG Source Localization: A Review</a> (2025)</li>
<li><strong>[SampTA]</strong> <a href="https://doi.org/10.1109/SAMPTA64769.2025.11133512" target="_blank">Revisiting CHAMPAGNE: Sparse Bayesian Learning as Reweighted Sparse Coding</a> (2025)</li>
<li><strong>[Springer]</strong> <a href="https://doi.org/10.1007/978-3-319-14947-9_4" target="_blank">Sparse Bayesian (Champagne) Algorithm</a> (2015)</li>
<li><strong>[PubMed]</strong> <a href="https://pubmed.ncbi.nlm.nih.gov/38545514/" target="_blank">SESAMEEG: probabilistic source localization</a> (PMID:38545514, 2024)</li>
<li><strong>[PubMed]</strong> <a href="https://pubmed.ncbi.nlm.nih.gov/38532791/" target="_blank">Global sensitivity of EEG source analysis to tissue conductivity uncertainties</a> (PMID:38532791, 2024)</li>
<li><strong>[PubMed]</strong> <a href="https://pubmed.ncbi.nlm.nih.gov/41308490/" target="_blank">Global sensitivity of MEG source analysis to tissue conductivity uncertainties</a> (PMID:41308490, 2025)</li>
<li><strong>[PubMed]</strong> <a href="https://pubmed.ncbi.nlm.nih.gov/39423516/" target="_blank">Standardized Kalman filtering for dynamical source localization</a> (PMID:39423516, 2024)</li>
<li><strong>[Physiological Measurement]</strong> <a href="https://doi.org/10.1088/2057-1976/aca20b" target="_blank">Neural SDE as uncertainty quantification for EEG source localization</a> (2023)</li>
<li><strong>[PubMed]</strong> <a href="https://pubmed.ncbi.nlm.nih.gov/41411682/" target="_blank">Potential of EEG and EEG/MEG skull conductivity estimation</a> (PMID:41411682, 2026)</li>
<li><strong>[Springer]</strong> <a href="https://doi.org/10.1007/978-3-030-74918-7_4" target="_blank">Source Models</a> (2022)</li>
<li><strong>[Springer]</strong> <a href="https://doi.org/10.1007/978-3-030-74918-7" target="_blank">EEG/MEG Source Reconstruction</a> (2022)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/1810.04410v2" target="_blank">Fast Approximation of EEG Forward Problem and Application to Tissue Conductivity Estimation</a> (2018)</li>
<li><strong>[SIAM]</strong> <a href="https://doi.org/10.1137/1.9781611977844.ch7" target="_blank">Parameter Identifiability and Influence</a> (2024)</li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W2903531101" target="_blank">Improving EEG Source Localization Through Spatio-Temporal Sparse Bayesian Learning</a> (2018)</li>
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
<h3>主要先行研究（再精査 15 件）</h3>
<ol>
<li><strong>[Nature]</strong> <a href="https://www.nature.com/articles/s41586-023-06808-9" target="_blank">Drosophila central brain connectome update</a> (2024)</li>
<li><strong>[PubMed]</strong> <a href="https://pubmed.ncbi.nlm.nih.gov/39902809/" target="_blank">Astrocyte-related intervention and behavior improvement</a> (PMID:39902809, 2025)</li>
<li><strong>[PubMed]</strong> <a href="https://pubmed.ncbi.nlm.nih.gov/40280131/" target="_blank">Neuron-astrocyte coupling mediates depressive-like behaviors</a> (PMID:40280131, 2025)</li>
<li><strong>[PubMed]</strong> <a href="https://pubmed.ncbi.nlm.nih.gov/39163862/" target="_blank">Acetate and cognitive performance under sleep disruption</a> (PMID:39163862, 2024)</li>
<li><strong>[PubMed]</strong> <a href="https://pubmed.ncbi.nlm.nih.gov/39172838/" target="_blank">Restoring glucose metabolism rescues cognition</a> (PMID:39172838, 2024)</li>
<li><strong>[PubMed]</strong> <a href="https://pubmed.ncbi.nlm.nih.gov/38448582/" target="_blank">Neuron-astrocyte program decline in ageing and schizophrenia</a> (PMID:38448582, 2024)</li>
<li><strong>[PubMed]</strong> <a href="https://pubmed.ncbi.nlm.nih.gov/39048816/" target="_blank">Single-cell multiregion dissection of Alzheimer's disease</a> (PMID:39048816, 2024)</li>
<li><strong>[PubMed]</strong> <a href="https://pubmed.ncbi.nlm.nih.gov/38418876/" target="_blank">Gamma stimulation promotes glymphatic clearance</a> (PMID:38418876, 2024)</li>
<li><strong>[PubMed]</strong> <a href="https://pubmed.ncbi.nlm.nih.gov/40120575/" target="_blank">Meningeal lymphatics-microglia axis regulates synaptic physiology</a> (PMID:40120575, 2025)</li>
<li><strong>[Biomedicines]</strong> <a href="https://doi.org/10.3390/biomedicines14020409" target="_blank">Mapping the Brain's Glymphatic System</a> (2026)</li>
<li><strong>[PubMed]</strong> <a href="https://pubmed.ncbi.nlm.nih.gov/38762094/" target="_blank">Neuroinflammation-related long-term dysfunction evidence</a> (PMID:38762094, 2024)</li>
<li><strong>[PubMed]</strong> <a href="https://pubmed.ncbi.nlm.nih.gov/39888279/" target="_blank">Microglia-derived IL-6 and depression-like behavior</a> (PMID:39888279, 2025)</li>
<li><strong>[PubMed]</strong> <a href="https://pubmed.ncbi.nlm.nih.gov/40311620/" target="_blank">Neural-activity-regulated glia-mediated brain lymphatic development</a> (PMID:40311620, 2025)</li>
<li><strong>[Neuron]</strong> <a href="https://doi.org/10.1016/j.neuron.2025.10.036" target="_blank">Resolving the mysteries of brain clearance and immune surveillance</a> (2025)</li>
<li><strong>[Neuroglia]</strong> <a href="https://doi.org/10.3390/neuroglia5010001" target="_blank">Contribution of small extracellular vesicles from glial cells to pain processing</a> (2024)</li>
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
<h3>主要先行研究（再精査 14 件）</h3>
<ol>
<li><strong>[Nature Reviews Neuroscience]</strong> <a href="https://doi.org/10.1038/s41583-024-00881-3" target="_blank">Structural constraints in effective connectivity analyses</a> (2025)</li>
<li><strong>[NeuroImage]</strong> <a href="https://doi.org/10.1016/j.neuroimage.2024.120954" target="_blank">Fast dynamic causal modeling regression for fMRI</a> (2024)</li>
<li><strong>[IEEE TMI]</strong> <a href="https://doi.org/10.1109/TMI.2024.3381670" target="_blank">MCAN: Causal adversarial networks for dynamic effective connectivity</a> (2024)</li>
<li><strong>[JAMA Network Open]</strong> <a href="https://doi.org/10.1001/jamanetworkopen.2024.9220" target="_blank">Personalized hippocampal network-targeted stimulation trial</a> (2024)</li>
<li><strong>[PubMed]</strong> <a href="https://pubmed.ncbi.nlm.nih.gov/38826672/" target="_blank">Dynamic causal modeling in multisensory speech perception</a> (PMID:38826672, 2024)</li>
<li><strong>[IEEE TNSRE]</strong> <a href="https://doi.org/10.1109/TNSRE.2021.3123964" target="_blank">Systematic review of DCM in psychiatric disorders</a> (2021)</li>
<li><strong>[Springer]</strong> <a href="https://doi.org/10.1007/978-1-4614-7320-6_57-1" target="_blank">Dynamic Causal Modeling with Neural Population Models</a> (2013)</li>
<li><strong>[bioRxiv]</strong> <a href="https://doi.org/10.1101/2021.06.01.446526" target="_blank">Test-retest reliability of regression dynamic causal modeling</a> (2021)</li>
<li><strong>[IEEE TBME]</strong> <a href="https://doi.org/10.1109/TBME.2024.3423803" target="_blank">A Deep Dynamic Causal Learning Model</a> (2024)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2010.09429v2" target="_blank">Neural Additive VAR for Causal Discovery in Time Series</a> (2020)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2209.03427v1" target="_blank">Causal discovery for time series with latent confounders</a> (2022)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2306.08946v2" target="_blank">Bootstrap aggregation and confidence measures for time-series causal discovery</a> (2023)</li>
<li><strong>[CRAN]</strong> <a href="https://doi.org/10.32614/cran.package.cfid" target="_blank">cfid: Identification of Counterfactual Queries in Causal Models</a> (2021)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2308.08307v1" target="_blank">Integrating cognitive map learning and active inference for planning in ambiguous environments</a> (2023)</li>
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
<h3>主要先行研究（再精査 16 件）</h3>
<ol>
<li><strong>[Imaging Neuroscience]</strong> <a href="https://doi.org/10.1162/imag.a.136" target="_blank">The lab streaming layer for synchronized multimodal recording</a> (2025)</li>
<li><strong>[Scientific Data]</strong> <a href="https://doi.org/10.1038/s41597-024-03559-8" target="_blank">Motion-BIDS extension for reproducible motion data</a> (2024)</li>
<li><strong>[BIDS]</strong> <a href="https://bids-specification.readthedocs.io/en/stable/" target="_blank">BIDS Specification 1.10.1</a> (2025更新版)</li>
<li><strong>[Zenodo]</strong> <a href="https://zenodo.org/records/18201723" target="_blank">BEP036 draft metadata extension</a> (2025)</li>
<li><strong>[Computer Methods and Programs in Biomedicine]</strong> <a href="https://doi.org/10.1016/j.cmpb.2024.108298" target="_blank">Haemosync: synchronisation algorithm for multimodal hemodynamic signals</a> (2024)</li>
<li><strong>[PubMed]</strong> <a href="https://pubmed.ncbi.nlm.nih.gov/34214093/" target="_blank">Simultaneous EEG-fMRI quality and safety study</a> (PMID:34214093)</li>
<li><strong>[IEEE TBME]</strong> <a href="https://doi.org/10.1109/TBME.2024.3383142" target="_blank">Evaluation of EEG-fMRI artifact correction methods</a> (2024)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2411.05812" target="_blank">Low-rank plus sparse decomposition for simultaneous EEG-fMRI denoising</a> (2024)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2311.04912" target="_blank">ezBIDS for multimodal BIDS curation and validation</a> (2023)</li>
<li><strong>[Scientific Data]</strong> <a href="https://doi.org/10.1038/s41597-024-03029-1" target="_blank">Multimodal single-neuron, iEEG and fMRI dataset during movie watching</a> (2024)</li>
<li><strong>[Frontiers in Neuroergonomics]</strong> <a href="https://doi.org/10.3389/fnrgo.2024.1411305" target="_blank">BIDS multimodal dataset with EEG and motion</a> (2024)</li>
<li><strong>[Reviews in the Neurosciences]</strong> <a href="https://doi.org/10.1515/revneuro-2023-0098" target="_blank">Single versus multimodal EEG and fMRI along AD continuum</a> (2024)</li>
<li><strong>[Sleep]</strong> <a href="https://doi.org/10.1093/sleep/zsad241" target="_blank">Artifact subspace reconstruction for EEG studies</a> (2023)</li>
<li><strong>[Frontiers in Human Neuroscience]</strong> <a href="https://doi.org/10.3389/fnhum.2019.00141" target="_blank">A Riemannian modification of artifact subspace reconstruction</a> (2019)</li>
<li><strong>[IEEE BIBM]</strong> <a href="https://doi.org/10.1109/bibm58861.2023.10385390" target="_blank">IMU-integrated artifact subspace reconstruction for wearable EEG</a> (2023)</li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W4390079365" target="_blank">Two common issues in synchronized multimodal EEG recordings: jitter and latency</a> (2023)</li>
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
<h3>主要先行研究（再精査 14 件）</h3>
<ol>
<li><strong>[Entropy]</strong> <a href="https://doi.org/10.3390/e26090779" target="_blank">Information Thermodynamics: From Physics to Neuroscience</a> (2024)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2502.03603" target="_blank">Dynamical Landauer principle and thermodynamic cost of entropy production</a> (2025)</li>
<li><strong>[Physical Review E]</strong> <a href="https://doi.org/10.1103/PhysRevE.107.024121" target="_blank">Entropy production correlates with consciousness levels</a> (2023)</li>
<li><strong>[Trends in Cognitive Sciences]</strong> <a href="https://doi.org/10.1016/j.tics.2024.03.009" target="_blank">The Thermodynamics of Mind</a> (2024)</li>
<li><strong>[Neuroscience and Biobehavioral Reviews]</strong> <a href="https://doi.org/10.1016/j.neubiorev.2023.105070" target="_blank">A primer on entropy in neuroscience</a> (2023)</li>
<li><strong>[Springer]</strong> <a href="https://doi.org/10.1007/978-3-319-93458-7_2" target="_blank">Conditional Erasure and the Landauer Limit</a> (2018)</li>
<li><strong>[MDPI Books]</strong> <a href="https://doi.org/10.3390/books978-3-7258-4142-4" target="_blank">The Landauer Principle and Its Implementations in Physics, Chemistry and Biology</a> (2025)</li>
<li><strong>[Cambridge]</strong> <a href="https://doi.org/10.1017/9781316650394.024" target="_blank">Information and Thermodynamics</a> (book chapter)</li>
<li><strong>[Elsevier]</strong> <a href="https://doi.org/10.1016/b978-0-444-59557-7.00011-4" target="_blank">Thermodynamics and Biological Systems</a> (2014)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2003.07436v1" target="_blank">Landauer Principle and General Relativity</a> (2020)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2409.17599v1" target="_blank">Information thermodynamics: from physics to neuroscience</a> (2024)</li>
<li><strong>[JPCL supporting information]</strong> <a href="https://doi.org/10.1021/acs.jpclett.4c03156.s001" target="_blank">Deriving the Landauer Principle from the Quantum Shannon Entropy</a> (supporting material)</li>
<li><strong>[CRC Press]</strong> <a href="https://doi.org/10.1201/b10962-10" target="_blank">Chemical Thermodynamics, Information, and Horizons</a> (2011)</li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W3023669232" target="_blank">Nonequilibrium Thermodynamics in Cell Biology</a> (2020)</li>
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
<h3>主要先行研究（再精査 14 件）</h3>
<ol>
<li><strong>[Nature]</strong> <a href="https://doi.org/10.1038/s41586-025-08888-1" target="_blank">Adversarial testing of global neuronal workspace and integrated information theories</a> (2025)</li>
<li><strong>[PLOS ONE]</strong> <a href="https://doi.org/10.1371/journal.pone.0268577" target="_blank">Adversarial collaboration protocol for consciousness theory testing</a> (2023)</li>
<li><strong>[Neuroscience of Consciousness]</strong> <a href="https://doi.org/10.1093/nc/niad016" target="_blank">Compatibility between PCI and global neuronal workspace theory</a> (2023)</li>
<li><strong>[Entropy]</strong> <a href="https://doi.org/10.3390/e25020334" target="_blank">System Integrated Information</a> (2023)</li>
<li><strong>[Journal of NeuroEngineering and Rehabilitation]</strong> <a href="https://doi.org/10.1186/s12984-024-01455-1" target="_blank">PCI in rTMS treatment responsiveness study</a> (2024)</li>
<li><strong>[Neuron]</strong> <a href="https://doi.org/10.1016/j.neuron.2024.03.002" target="_blank">Anesthesia and neurobiology of consciousness</a> (2024)</li>
<li><strong>[OSF]</strong> <a href="https://doi.org/10.31234/osf.io/rdq52" target="_blank">Structured Adversarial Collaboration Process</a> (2024)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2212.14787v1" target="_blank">Integrated Information Theory (IIT) 4.0</a> (2022)</li>
<li><strong>[OSF]</strong> <a href="https://doi.org/10.31234/osf.io/gauqm_v1" target="_blank">Does IIT make experimental predictions about consciousness?</a> (2025)</li>
<li><strong>[OSF]</strong> <a href="https://doi.org/10.31234/osf.io/kxywt" target="_blank">Separating weak IIT into IIT-inspired and aspirational-IIT approaches</a> (2023)</li>
<li><strong>[bioRxiv]</strong> <a href="https://doi.org/10.1101/2020.01.08.898775" target="_blank">Reliability of the perturbational complexity index using TMS-EEG</a> (2020)</li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W4382048961" target="_blank">An adversarial collaboration to critically evaluate theories of consciousness</a> (2023)</li>
<li><strong>[Oxford]</strong> <a href="https://doi.org/10.1093/acprof:oso/9780198520917.003.0012" target="_blank">The global neuronal workspace</a> (2006)</li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W3092295352" target="_blank">The predictive global neuronal workspace: an active inference model</a> (2020)</li>
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
<h3>主要先行研究（再精査 14 件）</h3>
<ol>
<li><strong>[Minds and Machines]</strong> <a href="https://doi.org/10.1007/s11023-014-9352-8" target="_blank">Uploading and Branching Identity</a> (2014)</li>
<li><strong>[Oxford]</strong> <a href="https://doi.org/10.1093/acprof:oso/9780198754855.003.0013" target="_blank">Enhancement, Mind-Uploading, and Personal Identity</a> (2016)</li>
<li><strong>[Cambridge]</strong> <a href="https://doi.org/10.1017/9781009486309.002" target="_blank">The Right to Personal Identity</a> (2026)</li>
<li><strong>[Patterns]</strong> <a href="https://linkinghub.elsevier.com/retrieve/pii/S2666389923002453" target="_blank">No legal personhood for AI (DOI: 10.1016/j.patter.2023.100861)</a> (2023)</li>
<li><strong>[EU Law]</strong> <a href="https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng" target="_blank">EU AI Act (Regulation (EU) 2024/1689)</a> (2024)</li>
<li><strong>[Council of Europe]</strong> <a href="https://book.coe.int/en/texts-of-council-of-europe-treaties/12225-council-of-europe-framework-convention-on-artificial-intelligence-and-human-rights-democracy-and-the-rule-of-law-cets-no-225.html" target="_blank">Framework Convention on AI (CETS No.225)</a> (2024)</li>
<li><strong>[Bioethics]</strong> <a href="https://doi.org/10.1111/bioe.70045" target="_blank">Digitizing Dignity: Digital Twins and Human Dignity</a> (2025)</li>
<li><strong>[AI and Society]</strong> <a href="https://doi.org/10.1007/s00146-025-02796-8" target="_blank">What makes a digital human twin more than a simulation?</a> (2025)</li>
<li><strong>[ISO]</strong> <a href="https://www.iso.org/standard/42001" target="_blank">ISO/IEC 42001 AI management systems</a> (2023)</li>
<li><strong>[OECD]</strong> <a href="https://oecd.ai/en/ai-principles/" target="_blank">OECD AI Principles</a> (運用中)</li>
<li><strong>[NIST]</strong> <a href="https://doi.org/10.6028/NIST.AI.600-1" target="_blank">NIST AI RMF: Generative AI Profile</a> (2024)</li>
<li><strong>[Science and Innovation]</strong> <a href="https://doi.org/10.52340/scai.2025.02.13" target="_blank">Digital Identity and Legal Personhood</a> (2025)</li>
<li><strong>[Legal Research and Analysis]</strong> <a href="https://doi.org/10.69971/lra.3.1.2025.42" target="_blank">Legal Personhood and Identity of Human Digital Twins</a> (2025)</li>
<li><strong>[Palgrave]</strong> <a href="https://doi.org/10.1007/978-1-137-01616-4_15" target="_blank">Defining Identity IV: Personhood</a> (2014)</li>
</ol>
<h3>監査導線（Round 23 追加）</h3>
<ul>
<li>EU AI Act 手続き履歴: <a href="https://eur-lex.europa.eu/legal-content/EN/HIS/?uri=CELEX:32024R1689" target="_blank">EUR-Lex Procedure timeline</a></li>
<li>EU 手続番号ページ: <a href="https://eur-lex.europa.eu/procedure/EN/2021_106" target="_blank">Procedure 2021_106</a></li>
<li>CoE 条約詳細（CETS 225）: <a href="https://www.coe.int/en/web/conventions/full-list?module=treaty-detail&treatynum=225" target="_blank">Treaty Office detail</a></li>
<li>CoE 最近の更新: <a href="https://www.coe.int/en/web/conventions/recent-changes" target="_blank">Treaty Office recent changes</a></li>
</ul>
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
<li><strong>[OECD]</strong> <a href="https://oecd.ai/en/ai-principles/" target="_blank">OECD AI Principles</a> (運用中)</li>
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
<h3>監査導線（Round 23 追加）</h3>
<ul>
<li>EU AI Act 手続き履歴: <a href="https://eur-lex.europa.eu/legal-content/EN/HIS/?uri=CELEX:32024R1689" target="_blank">EUR-Lex Procedure timeline</a></li>
<li>NIST AI RMF 開発履歴: <a href="https://www.nist.gov/itl/ai-risk-management-framework/ai-rmf-development" target="_blank">NIST AI RMF Development</a></li>
<li>OECD 法的本文: <a href="https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449" target="_blank">OECD-LEGAL-0449</a></li>
<li>OECD 2024 改訂公表: <a href="https://www.oecd.org/en/about/news/press-releases/2024/05/oecd-updates-ai-principles-to-stay-abreast-of-rapid-technological-developments.html" target="_blank">OECD press release (2024 update)</a></li>
</ul>
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
