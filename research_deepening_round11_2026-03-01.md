---
layout: default
title: "Research Deepening Round 11 (2026-03-01): 問い別エビデンス追補"
description: "U3/U7/U11/U12 の22問いを対象に、問い単位で必須文献を再割当。"
article_type: "Evidence Addendum"
subtitle: "問いごとに読む順番を固定する補完ラウンド"
author: Mind Uploading Research Project
last_updated: "2026-03-01"
note: "Round 11 (question-specific enrichment for U3/U7/U11/U12)"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Round 11 の狙い</h2>
<p>
Round 10 では全60問いに最小コア文献を付与しました。
Round 11 では、優先対象だった U3/U7/U11/U12 について、問いごとに参照を分けて再配置しました。
これにより「同じU内でも、問いごとにどの一次情報を先に読むか」が明確になります。
</p>
</div>

<section class="section" id="deliverables">
<h2 class="section-title">成果物</h2>
<ul>
<li><a href="automation/rq_question_specific_enrichment_round11_2026-03-01.csv" target="_blank">rq_question_specific_enrichment_round11_2026-03-01.csv</a>（22問い）</li>
</ul>
</section>

<section class="section" id="coverage">
<h2 class="section-title">適用カバレッジ</h2>
<table class="data-table">
<thead><tr><th>U</th><th>対象RQ数</th><th>一次情報の再割当</th></tr></thead><tbody>
<tr><td>U3</td><td>6</td><td>グリア/代謝/リンパ/免疫で問い別化</td></tr>
<tr><td>U7</td><td>6</td><td>同期/前処理/QC/欠損耐性で問い別化</td></tr>
<tr><td>U11</td><td>4</td><td>理論比較/計算量/失敗条件で問い別化</td></tr>
<tr><td>U12</td><td>6</td><td>ID/継承/裁定/撤回監査で問い別化</td></tr>
<tr><td><strong>合計</strong></td><td><strong>22</strong></td><td><strong>全行で必須2本を割当済み</strong></td></tr>
</tbody></table>
</section>

<section class="section" id="question-map">
<h2 class="section-title">問い別マップ（要約）</h2>
<table class="data-table">
<thead><tr><th>U-RQ</th><th>要点（平易）</th><th>必須1</th><th>必須2</th><th>今回実行する変更</th><th>外部依存タスク</th></tr></thead><tbody>
<tr><td>U3-1</td><td>グリア追加の効果は「ある/ない」ではなく、課題ごとの効果量で管理する段階に来ています。</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/39902809/" target="_blank">PubMed</a></td><td><a href="https://pubmed.ncbi.nlm.nih.gov/40280131/" target="_blank">PubMed</a></td><td>U3に「ΔR2/ΔAUC」を必須効果量として追記します。</td><td>担当: 実験チーム。前提: グリア操作系の再現手順。完了条件: 効果量付き比較公開。</td></tr>
<tr><td>U3-2</td><td>構造地図の高解像度化は進展中ですが、種横断の機能比較スケールは未統一です。</td><td><a href="https://www.nature.com/articles/s41586-023-06808-9" target="_blank">Nature</a></td><td><a href="https://pubmed.ncbi.nlm.nih.gov/40703192/" target="_blank">PubMed</a></td><td>種横断比較の最小共通指標（予測性能/汎化誤差）案を作成します。</td><td>担当: 比較神経班。前提: 種間データ整備。完了条件: 共通指標での比較表公開。</td></tr>
<tr><td>U3-3</td><td>身体・環境ループを削ると、代謝・行動安定性の説明力が落ちる例が増えています。</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/39163862/" target="_blank">PubMed</a></td><td><a href="https://pubmed.ncbi.nlm.nih.gov/39172838/" target="_blank">PubMed</a></td><td>U3に代謝指標（グルコース/乳酸関連）を補助指標として追加します。</td><td>担当: 実験チーム。前提: 代謝計測環境。完了条件: 行動指標との相関評価。</td></tr>
<tr><td>U3-4</td><td>「必要最小構成」は単一理論で決めず、アブレーションで性能低下を見て決める形が現実的です。</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/38448582/" target="_blank">PubMed</a></td><td><a href="https://pubmed.ncbi.nlm.nih.gov/39048816/" target="_blank">PubMed</a></td><td>U3アブレーション計画に「除外時性能低下の下限」を追加します。</td><td>担当: 実験設計班。前提: 多領域データ取得。完了条件: 下限値の事前登録。</td></tr>
<tr><td>U3-5</td><td>glymphatic/meningeal系は、認知機能やAβクリアランスに関連する実験が増えています。</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/38418876/" target="_blank">PubMed</a></td><td><a href="https://pubmed.ncbi.nlm.nih.gov/40120575/" target="_blank">PubMed</a></td><td>U3 RQ5にリンパ系関連の有無を記録する監査列を追加します。</td><td>担当: 実験チーム。前提: リンパ系計測導入。完了条件: 有無比較の効果量公開。</td></tr>
<tr><td>U3-6</td><td>免疫・炎症シグナルを無視すると、長期予測が崩れる可能性を示す報告が増えています。</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/38762094/" target="_blank">PubMed</a></td><td><a href="https://pubmed.ncbi.nlm.nih.gov/39888279/" target="_blank">PubMed</a></td><td>U3 RQ6に「免疫除外モデルの破綻時点」計測欄を追加します。</td><td>担当: 実験チーム。前提: 長期追跡プロトコル承認。完了条件: 週〜月スケール破綻点レポート。</td></tr>
<tr><td>U7-1</td><td>BIDSの必須項目は拡張されていますが、WBE用途で「必須」にする範囲はまだ決め切れていません。</td><td><a href="https://bids-specification.readthedocs.io/en/stable/" target="_blank">Spec</a></td><td><a href="https://zenodo.org/records/18201723" target="_blank">Zenodo</a></td><td>U7にBIDS必須メタデータの最小セット（同期/QC/刺激ログ）表を追加します。</td><td>担当: データ標準化WG。前提: BIDS運用ルール合意。完了条件: validator通過率の定期公開。</td></tr>
<tr><td>U7-2</td><td>同期誤差は「ある/ない」ではなく、アルゴリズムで測って比較する段階です。</td><td><a href="https://doi.org/10.1016/j.cmpb.2024.108298" target="_blank">DOI</a></td><td><a href="https://pubmed.ncbi.nlm.nih.gov/34214093/" target="_blank">PubMed</a></td><td>U7 RQ2に「時刻ずれ(ms)」「ジッタ分散」の自動計算欄を追加します。</td><td>担当: 計測運用チーム。前提: 同期基準信号の統一。完了条件: セッション間比較レポート。</td></tr>
<tr><td>U7-3</td><td>アーチファクト除去は手法差で結果が動くため、設定監査が必須です。</td><td><a href="https://doi.org/10.1109/TBME.2024.3383142" target="_blank">DOI</a></td><td><a href="https://arxiv.org/abs/2411.05812" target="_blank">link</a></td><td>U7 RQ3に「前処理設定差分ログ」を必須監査項目として追加します。</td><td>担当: 解析WG。前提: 前処理テンプレ統一。完了条件: 設定差分での再現率評価公開。</td></tr>
<tr><td>U7-4</td><td>アライメント失敗時は、再計測か除外かの基準を先に決めないと運用がぶれます。</td><td><a href="https://arxiv.org/abs/2311.04912" target="_blank">link</a></td><td><a href="https://doi.org/10.1038/s41597-024-03029-1" target="_blank">DOI</a></td><td>U7 RQ4に「再計測条件」「除外条件」の二段階判定欄を追加します。</td><td>担当: 計測運用チーム。前提: 欠測時運用手順の承認。完了条件: 再計測/除外判定一致率の公開。</td></tr>
<tr><td>U7-5</td><td>CIで前処理差分を回すなら、どの低下率で停止するかを数値で固定する必要があります。</td><td><a href="https://bids-specification.readthedocs.io/en/stable/" target="_blank">Spec</a></td><td><a href="https://doi.org/10.1109/TBME.2024.3383142" target="_blank">DOI</a></td><td>U7 RQ5に「リリースブロック閾値（再現率低下%）」を設定する欄を追加します。</td><td>担当: CI運用チーム。前提: ベースライン実験固定。完了条件: 失敗時自動ブロック動作確認。</td></tr>
<tr><td>U7-6</td><td>モダリティ欠損下でも結論が保てるかは、公開データで最小観測セットを検証する必要があります。</td><td><a href="https://doi.org/10.3389/fnrgo.2024.1411305" target="_blank">DOI</a></td><td><a href="https://doi.org/10.1515/revneuro-2023-0098" target="_blank">DOI</a></td><td>U7 RQ6に欠損シミュレーション列（EEG欠損/fMRI欠損）を追加します。</td><td>担当: 解析WG。前提: 欠損実験計画。完了条件: 最小観測セットでの結論維持率公開。</td></tr>
<tr><td>U11-1</td><td>理論比較は「同じ入力で比べる」ことが本質で、理論ごとに別データだと結論比較ができません。</td><td><a href="https://doi.org/10.1038/s41586-025-08888-1" target="_blank">DOI</a></td><td><a href="https://doi.org/10.1371/journal.pone.0268577" target="_blank">DOI</a></td><td>U11 RQ1に「共通入力仕様」の必須チェック欄を追加します。</td><td>担当: 意識研究WG。前提: 事前登録合意。完了条件: 同条件比較結果の公開。</td></tr>
<tr><td>U11-2</td><td>PCI/IITは計算コストが重く、近似計算を使うと適用範囲の明示が必要です。</td><td><a href="https://doi.org/10.1093/nc/niad016" target="_blank">DOI</a></td><td><a href="https://doi.org/10.3390/e25020334" target="_blank">DOI</a></td><td>U11 RQ2に「計算時間」「近似条件」「適用外条件」を記録する欄を追加します。</td><td>担当: 解析WG。前提: 計算資源制約の合意。完了条件: 近似の妥当域を示したレポート。</td></tr>
<tr><td>U11-3</td><td>理論の対立点は、1つの実験計画に落として先に固定しないと、後で都合よく解釈されます。</td><td><a href="https://doi.org/10.1038/s41586-025-08888-1" target="_blank">DOI</a></td><td><a href="https://doi.org/10.1371/journal.pone.0268577" target="_blank">DOI</a></td><td>U11 RQ3に「対立予測の事前固定」欄を追加します。</td><td>担当: 実験設計WG。前提: 理論代表者間の合意。完了条件: 事前登録済み比較実験の実施。</td></tr>
<tr><td>U11-4</td><td>臨床運用では、指標が外れたときの失敗条件（偽陽性/偽陰性）を先に明記する必要があります。</td><td><a href="https://doi.org/10.1186/s12984-024-01455-1" target="_blank">DOI</a></td><td><a href="https://doi.org/10.1016/j.neuron.2024.03.002" target="_blank">DOI</a></td><td>U11 RQ4に「偽陽性率/偽陰性率」の最小報告欄を追加します。</td><td>担当: 臨床研究WG。前提: 臨床評価プロトコル承認。完了条件: 失敗条件を含む運用手順公開。</td></tr>
<tr><td>U12-1</td><td>分岐後主体IDは、技術IDだけでなく、法的責任追跡と結びつける必要があります。</td><td><a href="https://doi.org/10.1016/j.patter.2023.100861" target="_blank">DOI</a></td><td><a href="https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng" target="_blank">EU Law</a></td><td>U12 RQ1に「ID衝突時の責任追跡ルール」欄を追加します。</td><td>担当: 法務/ガバナンスWG。前提: 管轄法域整理。完了条件: 追跡ルールの承認。</td></tr>
<tr><td>U12-2</td><td>責任・権利・同意の継承時点は、法的イベントとして明示しないと運用で破綻します。</td><td><a href="https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng" target="_blank">EU Law</a></td><td><a href="https://book.coe.int/en/texts-of-council-of-europe-treaties/12225-council-of-europe-framework-convention-on-artificial-intelligence-and-human-rights-democracy-and-the-rule-of-law-cets-no-225.html" target="_blank">CoE</a></td><td>U12 RQ2に「継承時点タイムスタンプ」を必須欄として追加します。</td><td>担当: 法務WG。前提: 継承イベント定義。完了条件: 法務監査で追跡可能な台帳整備。</td></tr>
<tr><td>U12-3</td><td>心理的連続性と法的個体がずれるケースは、先に紛争解決ルールを持つ必要があります。</td><td><a href="https://doi.org/10.1111/bioe.70045" target="_blank">DOI</a></td><td><a href="https://doi.org/10.1007/s00146-025-02796-8" target="_blank">DOI</a></td><td>U12 RQ3に「基準不一致時の裁定ルート」欄を追加します。</td><td>担当: 倫理・法務WG。前提: 紛争解決手順の合意。完了条件: 裁定手順の公開。</td></tr>
<tr><td>U12-4</td><td>技術性能と人格帰属は別軸なので、評価レポートを分けて管理する方が実務的です。</td><td><a href="https://doi.org/10.1016/j.patter.2023.100861" target="_blank">DOI</a></td><td><a href="https://www.iso.org/standard/42001" target="_blank">ISO</a></td><td>U12 RQ4に「性能KPI」「帰属KPI」の二系統欄を追加します。</td><td>担当: ガバナンス委員会。前提: KPI体系の承認。完了条件: 二系統監査の運用開始。</td></tr>
<tr><td>U12-5</td><td>記憶編集・再同期が起きるなら、法的主体IDの再編条件を先に定める必要があります。</td><td><a href="https://doi.org/10.1007/s00146-025-02796-8" target="_blank">DOI</a></td><td><a href="https://oecd.ai/en/ai-principles" target="_blank">OECD</a></td><td>U12 RQ5に「再編トリガー条件」「再編後の監査ID」欄を追加します。</td><td>担当: 法務/運用WG。前提: ID再編ポリシー草案。完了条件: 再編監査ログの検証完了。</td></tr>
<tr><td>U12-6</td><td>同意撤回時の権限剥奪は、技術実装（鍵管理・監査）と制度要件を同時に満たす必要があります。</td><td><a href="https://doi.org/10.6028/NIST.AI.600-1" target="_blank">DOI</a></td><td><a href="https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng" target="_blank">EU Law</a></td><td>U12 RQ6に「撤回反映遅延」「権限残留率」の監査欄を追加します。</td><td>担当: セキュリティ/法務WG。前提: 鍵管理設計。完了条件: 撤回時監査で0件残留を確認。</td></tr>
</tbody></table>
</section>

<section class="section" id="notes">
<h2 class="section-title">注記</h2>
<ul>
<li>今回の追加は、既存一次情報を問い単位へ再配置したものです（新規の主張追加ではありません）。</li>
<li>外部依存タスクはCSVに分離し、担当・前提・完了条件を保持しています。</li>
</ul>
</section>

</article>
</main>
