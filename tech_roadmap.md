---
layout: default
title: "技術ロードマップ：計測→再構成→実装でWBEを理解する"
description: "マインドアップロード（WBE）を技術面から俯瞰する学習ロードマップ。計測→再構成→実装→検証の問いの木で整理。"
article_type: "Roadmap (Definition #1)"
subtitle: "「何を解けたら前進か」を問いの木に分解し、読む順番と最低限の到達点を示す"
last_updated: "2026-01-15"
note: "暫定版（随時更新）"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Summary</h2>
<p>このページは「攻略（= 学習ロードマップ）」の<strong>技術編</strong>です。マインドアップロード（Whole Brain Emulation, WBE）を“実現した”と言い張るには、①何を測り、②何を復元し、③どの基盤で実行し、④どう検証するか、を<strong>先に定義</strong>しなければ議論が散ります。ここでは最小の骨格として、<strong>計測 → 再構成 → 実装 → 検証 → 社会実装</strong>の問いの木で整理し、各ノードで「学ぶべき概念」「前進と言える条件（暫定）」「次に必要なデータ」をまとめます。</p>
</div>

<section class="section" id="howto">
<h2 class="section-title">How to Use</h2>
<p>このページは“本”ではなく、研究全体像の<strong>地図</strong>です。まず「問いの木」を通読し、次に「学習の順序」に沿って各ノードを深掘りしてください。重要な運用ルールは2つだけです：<strong>(1) 出典リンクを残す</strong>、<strong>(2) 暫定（不確実性）を明示する</strong>。</p>
</section>

<section class="section" id="definition" data-qa-group>
<h2 class="section-title">前進の定義（最初に固定する）</h2>
<p>“前進”を主張するには、<strong>何を再現できたら勝ちか</strong>（＝評価軸）と、<strong>何が起きたら負けか</strong>（＝反証条件）を先に決める必要があります。ここでは、その前提となる問いを3つに圧縮します。</p>

<details open class="qa" data-tags="meta">
<summary>
<span class="qa-id">P0</span>
<span class="qa-title">「マインドアップロード」の操作的定義は？（何を再現する？）</span>
<span class="qa-tags"><span class="tag">META</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>“mind uploading / WBE”を、このサイトでは何として扱うか？（外から見える行動だけか／内部の因果構造か／本人性や意識まで含むか）</p>
<p><strong>分岐（例）：</strong>(A) 行動・機能の再現（ブラックボックス同等） / (B) 神経ダイナミクスの再現（中身重視） / (C) 本人性・主観の継続まで含む（強い主張）</p>
<p><strong>反証可能性：</strong>定義が曖昧なまま成果を語ると、評価が“後付け”になり、進捗の比較が不可能になる</p>
<p><strong>次に必要：</strong>このページ内の「検証」ノードで、(A)(B)(C)それぞれの<strong>測れる基準</strong>と<strong>負け条件</strong>を確定する</p>
</div>
</details>

<details open class="qa" data-tags="meta">
<summary>
<span class="qa-id">P1</span>
<span class="qa-title">主張レベル（クレーム階段）をどこに置く？</span>
<span class="qa-tags"><span class="tag">META</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>研究成果を、どのレベルまで到達したら「前進」と言うか？</p>
<ul>
<li><strong>L0：</strong>データ収集と再現可能な解析（標準化・品質管理・追試可能性）</li>
<li><strong>L1：</strong>デコーディング/エンコーディング（神経→行動/刺激、または逆の予測）</li>
<li><strong>L2：</strong>生成モデル（未学習条件でも神経/行動を外挿し、介入予測ができる）</li>
<li><strong>L3：</strong>閉ループ実装（リアルタイムに環境と相互作用して安定に動く）</li>
<li><strong>L4：</strong>本人性の主張（記憶・価値観・学習の連続性を、事前登録した基準で評価）</li>
<li><strong>L5：</strong>社会実装（権利・安全・ガバナンスが技術と同時に成立）</li>
</ul>
<p><strong>反証可能性：</strong>“L1の達成”を“L4の達成”のように語る（スコープのすり替え）を防ぐ</p>
<p><strong>次に必要：</strong>各レベルの「必要データ」「必要モデル」「評価スイート」を、このページで対応づける</p>
</div>
</details>

<details open class="qa" data-tags="meta">
<summary>
<span class="qa-id">P2</span>
<span class="qa-title">最低限の成果物は何？（データ・コード・評価・監査）</span>
<span class="qa-tags"><span class="tag">META</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>“前進”を再現可能にするため、何を必ず残すべきか？</p>
<ul>
<li><strong>データ：</strong>生データ＋メタデータ（BIDS等）＋匿名化/同意ログ</li>
<li><strong>コード：</strong>固定バージョンの解析パイプライン（環境・依存関係込み）</li>
<li><strong>評価：</strong>事前登録した指標・テスト・ベースライン比較</li>
<li><strong>監査：</strong>モデル差分、再現実行ログ、失敗例（ネガティブ結果）</li>
</ul>
<p><strong>反証可能性：</strong>成果の“見せ方”だけが先行し、検証不能な主張になる</p>
<p><strong>次に必要：</strong>EEGFlowでまずL0-L2の成果物テンプレ（データ構造・評価スクリプト）を固める</p>
</div>
</details>
</section>

<section class="section" id="tree">
<h2 class="section-title">問いの木（詳細版：1ページに集約）</h2>
<p>以下に、技術面の問いを「計測→再構成→実装→検証→社会実装」に分解して、<strong>1ページに全部</strong>まとめます。各項目は折りたたみ（クリックで展開）です。</p>

<div class="node" id="measurement" data-qa-group>
<div class="node-kicker">1. Measurement</div>
<h3>計測：どの解像度が必要？</h3>
<p class="mini"><strong>中心問い：</strong>「脳の何を、どの時空間解像度で取れば、“復元すべき対象”が一意に近づくか？」</p>

<details open class="qa" data-tags="measurement">
<summary>
<span class="qa-id">M0</span>
<span class="qa-title">計測の前提：in vivo / 侵襲 / 破壊スキャンのどれを想定？</span>
<span class="qa-tags"><span class="tag">MEASUREMENT</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>安全・スケールの制約を踏まえ、どの計測路線で"何を目指すか"を固定する。</p>
<p><strong>分岐（例）：</strong>(A) 非侵襲（EEG/MEG/fMRI）でモデルを鍛える / (B) 侵襲（ECoG/深部/動物）で因果推論を強化 / (C) 破壊的・超高解像度で構造を取る（将来像）</p>
<p><strong>反証条件：</strong>目的（復元対象）が定義されないまま、計測だけ“高級化”しても同定不能になる</p>
<p><strong>次に必要：</strong>このページ内のR0（復元対象）とV0（検証基準）を先に確定する</p>
</div>
</details>

<details open class="qa" data-tags="measurement">
<summary>
<span class="qa-id">M1</span>
<span class="qa-title">観測変数：電気（EEG）/血流（fMRI）/スパイク（侵襲）で何が違う？</span>
<span class="qa-tags"><span class="tag">EEG</span><span class="tag">FMRI</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>観測が変わると「復元できる対象（構造/状態/学習則）」が変わる。どの観測で何が識別可能か？</p>
<p><strong>論点：</strong>時系列の速さ・空間分解能・因果介入のしやすさ・全脳カバレッジ・コスト</p>
<p><strong>次に必要：</strong>同一の課題・同一個体で、マルチモーダル同時計測（可能な範囲）＋位置合わせ（M5）</p>
</div>
</details>

<details open class="qa" data-tags="measurement">
<summary>
<span class="qa-id">M2</span>
<span class="qa-title">時間解像度の下限：どの時間スケールを“保存”すべき？</span>
<span class="qa-tags"><span class="tag">RESOLUTION</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>認知・学習・意識に関係する現象を壊さないために、必要な時間分解能はどこか？</p>
<ul>
<li><strong>候補：</strong>ms（スパイク/位相）・10-100ms（結合ダイナミクス）・秒（状態遷移）・分〜日（学習/可塑性）</li>
<li><strong>反証条件：</strong>粗すぎる時間分解能で、介入応答や閉ループ制御が再現できない</li>
<li><strong>次に必要：</strong>閉ループ課題（I1）で許容遅延を測り、必要サンプリングを逆算する</li>
</ul>
</div>
</details>

<details open class="qa" data-tags="measurement">
<summary>
<span class="qa-id">M3</span>
<span class="qa-title">空間解像度の下限：どの粒度（領域/カラム/ニューロン/シナプス）を目指す？</span>
<span class="qa-tags"><span class="tag">RESOLUTION</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>“本人の心的機能”に必要な情報が、どの空間粒度に宿ると仮定するか？</p>
<p><strong>分岐（例）：</strong>(A) 領域間結合＋状態で十分 / (B) 局所回路まで必要 / (C) シナプス結合まで必要</p>
<p><strong>次に必要：</strong>仮定(A)(B)(C)ごとに、観測可能性（M1）と計算可能性（I3）を評価する</p>
</div>
</details>

<details open class="qa" data-tags="measurement">
<summary>
<span class="qa-id">M4</span>
<span class="qa-title">全脳カバレッジ：どこまで“全体”を測る必要がある？</span>
<span class="qa-tags"><span class="tag">COVERAGE</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>限られた計測で、“境界（何が主体に含まれるか）”をどう扱うか？</p>
<p><strong>次に必要：</strong>検証（V0）で「主体の境界」を操作的に置き、必要領域と不要領域を明文化する</p>
</div>
</details>

<details open class="qa" data-tags="measurement">
<summary>
<span class="qa-id">M5</span>
<span class="qa-title">マルチモーダル統合：位置合わせ（MRI/EEG/fMRI）をどう保証する？</span>
<span class="qa-tags"><span class="tag">FUSION</span><span class="tag">MRI</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>異なる計測は座標系・遅延・ノイズ構造が違う。統合の誤差が“学習したい信号”を壊していないか？</p>
<p><strong>反証条件：</strong>位置合わせ誤差で再構成（R2）が不安定になり、再現性（P2）が落ちる</p>
<p><strong>次に必要：</strong>同一データに対し複数パイプラインで一致するか（解析差分監査）</p>
</div>
</details>

<details open class="qa" data-tags="measurement">
<summary>
<span class="qa-id">M6</span>
<span class="qa-title">介入・刺激：同定可能性を上げる“実験デザイン”は？</span>
<span class="qa-tags"><span class="tag">CAUSAL</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>受動観測だけでは同定できない時、どんな介入（刺激/課題/環境変化）を入れると識別可能性が上がるか？</p>
<p><strong>次に必要：</strong>モデル（R4）側で「この介入があると識別できる」という設計逆算をする</p>
</div>
</details>

<details open class="qa" data-tags="measurement">
<summary>
<span class="qa-id">M7</span>
<span class="qa-title">縦断：日内/日間変動に対して“本人性特徴”は安定か？</span>
<span class="qa-tags"><span class="tag">LONGITUDINAL</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>同一個体でも脳状態は揺れる。どの特徴が“本人らしさ”として頑健か？</p>
<p><strong>反証条件：</strong>再現できるのが“その日の状態”に限られ、長期の同一性評価（V5）ができない</p>
<p><strong>次に必要：</strong>同一被験者の複数セッションで、事前定義の同定スコア（V1）を追跡する</p>
</div>
</details>

<details open class="qa" data-tags="measurement">
<summary>
<span class="qa-id">M8</span>
<span class="qa-title">品質管理：アーチファクト/欠損/ノイズをどう“定量化”して扱う？</span>
<span class="qa-tags"><span class="tag">QC</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>“良いデータ”の定義を事前に置き、除外・補完・重み付けを透明にする。</p>
<p><strong>次に必要：</strong>EEGFlowの前処理（`eegflow/01_preprocess.py`）に、QC指標とログ出力を組み込む <strong>(✅ Implemented in Issue #34)</strong></p>
</div>
</details>

<details open class="qa" data-tags="measurement">
<summary>
<span class="qa-id">M9</span>
<span class="qa-title">標準化：BIDS/メタデータで“他人が追試できる”形にするには？</span>
<span class="qa-tags"><span class="tag">BIDS</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>データが共有可能でも、メタデータが薄いと追試できない。何を最低限メタデータ化するか？</p>
<p><strong>次に必要：</strong>プロトコル（課題・機器・前処理）を機械可読で残す（P2）</p>
</div>
</details>
</div>

<div class="node" id="reconstruction" data-qa-group>
<div class="node-kicker">2. Reconstruction</div>
<h3>再構成：何を復元する？（回路 / 状態 / 学習則）</h3>
<p class="mini"><strong>中心問い：</strong>「“本人の心的機能”に必要なのは、構造（結合）・動的状態（活動）・学習則（可塑性）のどこまでか？」</p>

<details open class="qa" data-tags="reconstruction">
<summary>
<span class="qa-id">R0</span>
<span class="qa-title">復元対象の最小セットは？（構造/状態/学習則）</span>
<span class="qa-tags"><span class="tag">RECONSTRUCTION</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>どこまで復元すれば、検証（V0）で勝ちに行けるか？</p>
<p><strong>分岐（例）：</strong>(A) 構造＋状態（固定） / (B) 構造＋状態＋一部可塑性 / (C) 可塑性まで含むフル動的</p>
<p><strong>反証条件：</strong>(A)で閉ループ学習（I5）が再現不能、(B)(C)で同定不能・過学習で破綻</p>
<p><strong>次に必要：</strong>同定可能性（R7）と計算可能性（I3）を同時に評価する</p>
</div>
</details>

<details open class="qa" data-tags="reconstruction">
<summary>
<span class="qa-id">R1</span>
<span class="qa-title">逆問題：観測（M1）から何が一意に推定できる？</span>
<span class="qa-tags"><span class="tag">INVERSE</span><span class="tag">BAYES</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>EEGソース推定のような逆問題は、解が一意に定まらない“不良設定問題（ill-posed problem）”である。点推定（ひとつの解を求めること）は科学的に誤解を招く可能性があるため、本プロジェクトでは<strong>ベイズ的アプローチを原則とする</strong>。</p>
<p><strong>方針：</strong>解を事後確率分布として捉え、その不確実性自体を後段の解析（因果モデリング等）に引き継ぐ。これにより、推定の曖昧さを考慮した、より頑健な結論を目指す。</p>
<p><strong>次に必要：</strong>推定結果の不確実性（R7）と、仮定（事前分布）を変えた時の感度分析（監査ログ）</p>
</div>
</details>

<details open class="qa" data-tags="reconstruction">
<summary>
<span class="qa-id">R2</span>
<span class="qa-title">ソース推定：EEGから“どの表現”の脳活動が欲しい？</span>
<span class="qa-tags"><span class="tag">EEG</span><span class="tag">ESI</span><span class="tag">BAYES</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>EEGソース推定は「領域×時間」の表現を得やすいが、ニューロン/シナプスは直接は見えない。復元対象（R0）に合わせて表現を選ぶ。</p>
<p><strong>課題：</strong>従来は「高密度EEG(128ch)化」が推奨されてきたが、近年の研究はチャンネル数だけでは不良設定性（ill-posedness）を解決できないことを示している。特に、dSPMのような点推定法は不確実性を無視してしまう。</p>
<p><strong>階層的ベイズモデルと高解像度計測の統合：</strong>Block-Champagne Framework<sup><a href="#ref-78">[78]</a></sup>の採用に加え、<strong>超高密度EEG（High-density EEG, 256ch以上）</strong>と<strong>個体別MRIに基づく有限要素法（FEM）フォワードモデル</strong>の導入を必須化する。これにより深部脳活動の推定精度を担保する。さらに、Feng et al. (2025)<sup><a href="#ref-78">[78]</a></sup>が指摘するノイズ特性の動的変化に対応するため、<strong>適応的ベイズ更新（Adaptive Bayesian Updating）</strong>を実装し、推定された脳活動マップには必ず<strong>信頼区間（Credible Intervals）</strong>を付随させる。</p>
<p><strong>次に必要：</strong>`eegflow/02_source_imaging.py` に変分ベイズ（Variational Bayesian）アプローチを実装し、不確実性を考慮したソース再構成を行う <strong>(✅ Implemented in Issue #43)</strong></p>
</div>
</details>

<details open class="qa" data-tags="reconstruction">
<summary>
<span class="qa-id">R3</span>
<span class="qa-title">状態推定：潜在状態（latent）をどう定義し、どう検証する？</span>
<span class="qa-tags"><span class="tag">STATE</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>観測ノイズと真の状態を分離し、状態が“予測に効いている”ことを示せるか？</p>
<p><strong>反証条件：</strong>潜在状態がデータの圧縮にしかなっておらず、介入予測（R4）に寄与しない</p>
<p><strong>次に必要：</strong>未学習条件での外挿と、介入応答の予測誤差を評価する</p>
</div>
</details>

<details open class="qa" data-tags="reconstruction">
<summary>
<span class="qa-id">R4</span>
<span class="qa-title">因果：介入に対する反応を予測できるモデルは何？</span>
<span class="qa-tags"><span class="tag">CAUSAL</span><span class="tag">MULTI-SCALE</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>相関の当てはめではなく、刺激/操作に対して“どう変わるはずか”を言えるか？ デコーディング（相関）からエミュレーション（因果）への飛躍をどう埋めるか？</p>
<p><strong>方針：</strong>脳を能動的推論（Active Inference）を行う生成モデルとして定式化する。Laukkonen et al. (2025) の<strong>「反実仮想的等価性（Counterfactual Equivalence）」</strong>を指標とするが、EEG単体では解像度が不足する。</p>
<p><strong>改善策（Multi-scale）：</strong>EEGから推定されたマクロな因果構造を、ミクロな神経回路シミュレーション（Blue Brain Project等）の制約条件として用いる<strong>「マルチスケール因果モデリング」</strong>を採用する。トップダウン（EEG）とボトムアップ（回路）の統合により、シナプスレベルの可塑性を反映した頑健なモデルを目指す。</p>
<p><strong>次に必要：</strong>介入前提の評価タスク（V2）と、マルチスケール統合パイプラインの設計</p>
</div>
</details>

<details open class="qa" data-tags="reconstruction">
<summary>
<span class="qa-id">R5</span>
<span class="qa-title">可塑性：学習則を“入れる/入れない”の境界は？</span>
<span class="qa-tags"><span class="tag">PLASTICITY</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>長期の本人性（V5）を扱うなら、学習（更新）を入れざるを得ない。だが更新を入れると検証が難しくなる。</p>
<p><strong>分岐（例）：</strong>(A) 学習しない（固定モデル） / (B) 制限付きで学習（安全な更新） / (C) 学習則まで推定</p>
<p><strong>次に必要：</strong>学習を入れた時のドリフト監視（V4）と、安全策（I8）</p>
</div>
</details>

<details open class="qa" data-tags="reconstruction">
<summary>
<span class="qa-id">R6</span>
<span class="qa-title">個人化：一般モデル＋個人パラメータ？それとも完全に個人別？</span>
<span class="qa-tags"><span class="tag">PERSONALIZATION</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>“本人性”を議論するなら個人化は避けられない。一方で、個人化しすぎると過学習と再現性が壊れる。</p>
<p><strong>次に必要：</strong>個人内/個人間の性能分解（どこが個人差か）を評価指標に入れる</p>
</div>
</details>

<details open class="qa" data-tags="reconstruction">
<summary>
<span class="qa-id">R7</span>
<span class="qa-title">同定可能性：推定は“唯一解”に近づく？不確実性は？</span>
<span class="qa-tags"><span class="tag">IDENTIFIABILITY</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>同じ観測を説明する別モデルが無数にある時、どの仮定で絞り込むか？不確実性をどう表現するか？</p>
<p><strong>反証条件：</strong>小さな前処理差で結果が大きく変わり、再現（P2）できない</p>
<p><strong>次に必要：</strong>事前分布/正則化を明示し、感度分析で“頑健な結論だけ”採用する</p>
</div>
</details>

<details open class="qa" data-tags="reconstruction">
<summary>
<span class="qa-id">R8</span>
<span class="qa-title">圧縮：どの情報を捨てても“検証基準”は保てる？</span>
<span class="qa-tags"><span class="tag">COMPRESSION</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>WBEは“全部保存”が理想だが現実的でない。評価（V0）を満たす最小表現を探せるか？</p>
<p><strong>次に必要：</strong>圧縮率を変えて、評価スイートの性能がどこで崩れるかを測る</p>
</div>
</details>

<details open class="qa" data-tags="reconstruction">
<summary>
<span class="qa-id">R9</span>
<span class="qa-title">監査：モデル差分と失敗例を“残す仕組み”は？</span>
<span class="qa-tags"><span class="tag">AUDIT</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>更新のたびに結論が変わる領域だからこそ、差分・失敗・ネガティブ結果を残す必要がある。</p>
<p><strong>次に必要：</strong>モデル/データ/評価のバージョンを結びつけ、再実行で再現できる形にする（P2）</p>
</div>
</details>

<details open class="qa" data-tags="reconstruction">
<summary>
<span class="qa-id">R10</span>
<span class="qa-title">神経修飾：気分や覚醒度（Volume Transmission）をどう組み込む？</span>
<span class="qa-tags"><span class="tag">NEUROMODULATION</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>シナプス結合（Wiring Transmission）だけでは、ドーパミンやセロトニンによる全脳的な「ムード」「学習率」の変化を再現できない。</p>
<p><strong>解決策：</strong>アーキテクチャに<strong>「Neuromodulation-aware Layers（神経修飾層）」</strong>を追加する。これは、入力応答ゲイン（活性化関数の傾き）や可塑性（学習率）を動的に制御するメタパラメータとして機能する。</p>
<p><strong>次に必要：</strong>瞳孔径や心拍変動などの生理指標を、脳幹アミン系活動のプロキシとしてモデルに入力する（M1/M8）</p>
</div>
</details>
</div>

<div class="node" id="implementation" data-qa-group>
<div class="node-kicker">3. Implementation</div>
<h3>実装：どの基盤で？リアルタイム性は？</h3>
<p class="mini"><strong>中心問い：</strong>「復元したモデルを、どの計算基盤（HPC/クラウド/ニューロモーフィック/ハイブリッド）で動かすか？閉ループ（身体・環境）に入れられるか？」</p>

<details open class="qa" data-tags="implementation">
<summary>
<span class="qa-id">I0</span>
<span class="qa-title">実行基盤：汎用計算/GPU/HPC/ニューロモーフィックのどれを狙う？</span>
<span class="qa-tags"><span class="tag">IMPLEMENTATION</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>復元対象（R0）に対して、実装基盤は“十分な忠実度”と“現実的コスト”を両立できるか？</p>
<p><strong>次に必要：</strong>モデル粒度（I2）と計算量（I3）をセットで見積もる</p>
</div>
</details>

<details open class="qa" data-tags="implementation">
<summary>
<span class="qa-id">I10</span>
<span class="qa-title">時間連続性：離散時間(RNN)と連続時間(ODE)のどちらを選ぶ？</span>
<span class="qa-tags"><span class="tag">NEURAL-ODE</span><span class="tag">DYNAMICS</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>生物学的脳は連続時間で動作するが、標準的なRNN/Transformerは離散時間である。このギャップがダイナミクスの歪みを生む。</p>
<p><strong>提案：</strong>実装フレームワークとして<strong>Neural ODEs (Neural Ordinary Differential Equations)</strong> または <strong>CTRNNs</strong> を採用する。$\frac{dh(t)}{dt} = f(h(t), t, \theta)$ としてモデル化することで、任意の時間分解能でのサンプリングと、随伴変数法（Adjoint Method）によるメモリ効率の良い学習が可能になる。</p>
<p><strong>次に必要：</strong>EEG（ミリ秒）とfMRI（秒）の異なるタイムスケールを、同一の微分方程式系で統合する</p>
</div>
</details>

<details open class="qa" data-tags="implementation">
<summary>
<span class="qa-id">I1</span>
<span class="qa-title">閉ループ：リアルタイムに何msの遅延まで許される？</span>
<span class="qa-tags"><span class="tag">REALTIME</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>“本人らしさ”を評価するなら、環境との相互作用（遅延・ノイズ）が本質になる。許容遅延は課題依存。</p>
<p><strong>次に必要：</strong>評価スイート（V1）側で、遅延/ノイズ耐性を測る項目を入れる</p>
</div>
</details>

<details open class="qa" data-tags="implementation">
<summary>
<span class="qa-id">I2</span>
<span class="qa-title">モデル粒度：スパイキング/レート/抽象のどこで戦う？</span>
<span class="qa-tags"><span class="tag">GRANULARITY</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>粒度を上げるほど忠実度は上がる（仮）一方で、同定（R7）と計算（I3）が壊れる。勝てる粒度はどこか？</p>
<p><strong>次に必要：</strong>粒度ごとに「必要計測（M2/M3）」「必要計算（I3）」「通る評価（V0）」を対応づける</p>
</div>
</details>

<details open class="qa" data-tags="implementation">
<summary>
<span class="qa-id">I3</span>
<span class="qa-title">計算量：メモリ/電力/並列化のボトルネックはどこ？</span>
<span class="qa-tags"><span class="tag">SCALING</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>モデルの忠実度を上げると、計算資源が爆発する。どこで近似・圧縮（R8）するか？</p>
<p><strong>次に必要：</strong>評価スイートの性能を落とさずに圧縮できる境界を測る</p>
</div>
</details>

<details open class="qa" data-tags="implementation">
<summary>
<span class="qa-id">I4</span>
<span class="qa-title">初期化：モデルの“初期状態”をどう与える？</span>
<span class="qa-tags"><span class="tag">INITIALIZATION</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>同じ構造でも初期状態が違えば振る舞いが違う。計測（M7）のどの時点を“スタート”にする？</p>
<p><strong>反証条件：</strong>初期化の任意性で結果が揺れて、本人性評価（V5）が成立しない</p>
<p><strong>次に必要：</strong>初期化手順を固定し、初期化に対する感度（頑健性）を測る</p>
</div>
</details>

<details open class="qa" data-tags="implementation">
<summary>
<span class="qa-id">I5</span>
<span class="qa-title">学習とドリフト：学習させるなら“安全な更新”をどう設計する？</span>
<span class="qa-tags"><span class="tag">LEARNING</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>学習（R5）を許すと、本人性（V5）と安全（D2）が絡む。更新をどう監視し、どこで止めるか？</p>
<p><strong>次に必要：</strong>ドリフト指標（V4）＋キルスイッチ/隔離（I8）</p>
</div>
</details>

<details open class="qa" data-tags="implementation">
<summary>
<span class="qa-id">I6</span>
<span class="qa-title">身体性：入力/出力（センサー/運動/言語）をどこまで持たせる？</span>
<span class="qa-tags"><span class="tag">EMBODIMENT</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>閉ループ検証（I1/V1）には、環境と身体（あるいはその代替）が必要。最小の身体性は何か？</p>
<p><strong>次に必要：</strong>環境（VR/ゲーム/対話）を固定し、同一条件で追試可能な評価を設計する</p>
</div>
</details>

<details open class="qa" data-tags="implementation">
<summary>
<span class="qa-id">I7</span>
<span class="qa-title">再現性：実装差（言語/ハード）で結果が変わらない保証は？</span>
<span class="qa-tags"><span class="tag">REPRO</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>“同じモデル”でも数値誤差や並列順序で挙動が変わる。どこまで決定性を要求するか？</p>
<p><strong>次に必要：</strong>固定乱数・固定環境・差分テスト（P2）で、許容誤差内に収まるか検証する</p>
</div>
</details>

<details open class="qa" data-tags="implementation">
<summary>
<span class="qa-id">I8</span>
<span class="qa-title">安全：隔離・監視・停止（containment）をどう作る？</span>
<span class="qa-tags"><span class="tag">SAFETY</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>強い主張（P1のL4-L5）に近づくほど、安全が技術要件になる。</p>
<details open class="qa" data-tags="implementation">
<summary>
<span class="qa-id">I9</span>
<span class="qa-title">熱力学：デジタル基盤で“意識の物理的コスト”を払えるか？</span>
<span class="qa-tags"><span class="tag">THERMODYNAMICS</span><span class="tag">IIT</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>現在のノイマン型コンピュータは物理的因果力を抽象化しているため、IIT 4.0の観点ではΦ=0（Unfolding Argument）となる可能性がある。また、生物学的脳の「非平衡定常状態（NESS）」としての散逸構造をどう模倣するか？</p>
<p><strong>方針（Issue #58 Update）：</strong>物理的実装（ニューロモルフィック）への完全移行までの過渡期として、<strong>「仮想散逸プロトコル（Virtual Dissipation Protocol）」</strong>を実装する。
1. <strong>Entropy Production Rate (EPR):</strong> 時間反転対称性の破れを定量化し、不可逆なエントロピー生成をシミュレーション内で強制する。
2. <strong>Metabolic Flux:</strong> 計算の有無に関わらず、構造維持のために消費される仮想エネルギー流（Metabolic Overhead）を定義する。
これにより、デジタルエミュレーションであっても「存在し続けるためにコストを払う」散逸構造としての性質を保持させる。</p>
<p><strong>次に必要：</strong>EPR > 0 を維持しつつ、論理的計算を行うアルゴリズムの定式化</p>
</div>
</details>
</div>
</details>

<div class="node" id="verification" data-qa-group>
<div class="node-kicker">4. Verification</div>
<h3>検証：何を満たせば「同じ」と言える？</h3>
<p class="mini"><strong>中心問い：</strong>「同一性/意識/行動のうち、技術的に検証可能な基準をどう定義し、反証条件をどう置くか？」</p>

<details open class="qa" data-tags="verification">
<summary>
<span class="qa-id">V0</span>
<span class="qa-title">検証対象：同一性・意識・行動のどれを“工学的に”検証する？</span>
<span class="qa-tags"><span class="tag">VERIFICATION</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>検証できない（測れない）ものを、検証したことにはできない。何を“測れる成功条件”に落とすか？</p>
<p><strong>分岐（例）：</strong>(A) 行動・能力の同等性 / (B) 介入応答の同等性 / (C) 自伝的記憶や価値観の連続性（要注意）</p>
<p><strong>次に必要：</strong>V1で評価スイートを事前登録し、P1のクレーム階段と対応づける</p>
</div>
</details>

<details open class="qa" data-tags="verification">
<summary>
<span class="qa-id">V1</span>
<span class="qa-title">評価スイート：何を測れば“前進”と言える？（事前登録）</span>
<span class="qa-tags"><span class="tag">BENCHMARK</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>タスク・指標・ベースライン・統計・失敗条件を事前に固定する。</p>
<ul>
<li><strong>行動：</strong>未学習タスクでの一般化、反応時間/誤り、学習曲線</li>
<li><strong>神経：</strong>状態遷移、スペクトル特徴、ネットワーク指標、介入応答</li>
<li><strong>本人性（暫定）：</strong>自伝的記憶の整合、選好の安定、自己モデルの一貫性</li>
</ul>
<p><strong>次に必要：</strong>まずはL0-L2向けに“小さくても追試可能”なスイートを作る</p>
</div>
</details>

<details open class="qa" data-tags="verification">
<summary>
<span class="qa-id">V2</span>
<span class="qa-title">因果テスト：刺激/介入で“同じ反応”を出せるか？</span>
<span class="qa-tags"><span class="tag">CAUSAL</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>相関一致は“似せた”だけでも達成できる。介入に対して一致するかが強い検証になる。</p>
<p><strong>次に必要：</strong>M6（介入設計）とR4（因果モデル）を繋いだ評価項目を作る</p>
</div>
</details>

<details open class="qa" data-tags="verification">
<summary>
<span class="qa-id">V3</span>
<span class="qa-title">一般化：分布外（OOD）でも“本人らしさ”は保てる？</span>
<span class="qa-tags"><span class="tag">OOD</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>訓練と同じ条件でしか動かないなら、アップロードではなく“再生”に近い。新規状況での一貫性を測る。</p>
<p><strong>次に必要：</strong>未学習課題・環境変化・ノイズ条件での性能劣化曲線を定義する</p>
</div>
</details>

<details open class="qa" data-tags="verification">
<summary>
<span class="qa-id">V4</span>
<span class="qa-title">長期：学習・ドリフト・忘却の扱いをどう評価する？</span>
<span class="qa-tags"><span class="tag">LONGITUDINAL</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>学習させるほど、元の本人と乖離する可能性も増える。変化を“許容”する範囲を定義する。</p>
<p><strong>次に必要：</strong>セッション間の同一性指標（M7）＋更新ログ（P2）</p>
</div>
</details>

<details open class="qa" data-tags="verification">
<summary>
<span class="qa-id">V5</span>
<span class="qa-title">本人性：心理的連続性を超えた“因果的同一性”とは？</span>
<span class="qa-tags"><span class="tag">IDENTITY</span><span class="tag">LEGAL</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>記憶や性格の類似（心理的連続性）だけでは、コピーや模倣（LLM）と区別がつかない。より厳密な工学的定義が必要である。</p>
<ul>
<li><strong>新基準：因果的同一性（Causal Identity）：</strong>
パーフィットの心理説を拡張し、システムの「未来の予測能力（Active Inference の精度）」が生物学的脳と統計的に区別不能であることを同一性の条件とする。
</li>
<li><strong>指標：</strong>チューリング・テストを拡張した<strong>「因果的摂動プロトコル（Causal Perturbation Protocol）」</strong>を実行する。TMS等による物理的摂動に対する生物学的脳の反応と、エミュレーション上の仮想的摂動に対する反応の統計的同一性を検証する指標（例：Perturbational Complexity Index, PCI）を導入し、動的な因果構造の一致を確認する。</li>
<li><strong>反証条件：</strong>記憶は持っているが、新規環境に対する適応・予測パターンがオリジナルと乖離する（ゾンビ/模倣者）</li>
<li><strong>次に必要：</strong>V8の「模倣との区別」テストにおいて、予測精度をコア指標に据える</li>
</ul>                        </div>
</details>

<details open class="qa" data-tags="verification">
<summary>
<span class="qa-id">V6</span>
<span class="qa-title">意識：理論に依存した予測を、どこまで“検証可能”にできる？</span>
<span class="qa-tags"><span class="tag">CONSCIOUSNESS</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>意識は直接観測できない。理論（IIT/GNWT等）が出す“予測の差”を、計測（M）と介入（M6/V2）で検証できるか？</p>
<ul>
<li><strong>IIT 4.0の計算量問題 (Issue #58):</strong> 厳密なΦ計算はNP困難（$2^n$）であり不可能である。これに対し、<strong>近似計算（Approximate Phi, Effective Information）</strong>を採用し、全脳レベルではなく局所モジュール間の統合性を評価する現実的路線をとる。</li>
<li><strong>識別可能性の壁 (The Identifiability Wall):</strong> 反実仮想的等価性（Laukkonen et al., 2025）は、観測データだけでは一意に定まらない（Markov Equivalence Class）。したがって、特定の構造方程式（SCM）を仮定した上での「条件付き等価性」であることを常に明示し、PCI等の摂動応答を用いてSCM候補を絞り込むアプローチ（V2, V5）を必須とする。</li>
<li><strong>Unfolding Argumentへの応答:</strong> IIT批判である「Unfolding Argument」に対し、単なる機能的等価性を超えた要件を課す。具体的には、「因果構造の保存（Causal Structure Preservation）」を、<strong>マルコフブランケット（Markov Blanket）</strong>の境界条件（デジタルエミュレーションと生物学的基盤の間の情報交換における帯域幅と遅延）の保存として厳密に定義し、その計算論的閾値を検証プロセスに組み込む。</li>
</ul>
<p><strong>注意：</strong>理論はあくまで仮説生成のツールとして扱い、実装（WBE）の成否は「特定の理論に適合するか」ではなく、V2（因果）やV5（本人性）といった実証的指標で判断する。</p>
</div>
</details>

<details open class="qa" data-tags="verification">
<summary>
<span class="qa-id">V7</span>
<span class="qa-title">コピー/分岐：複数インスタンスが走ったら“本人”はどう扱う？</span>
<span class="qa-tags"><span class="tag">BRANCHING</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>工学的には複製が容易。検証の設計も、分岐を前提にしないと破綻する。</p>
<p><strong>次に必要：</strong>個体ID・版管理（P2）を、本人性評価（V5）と結びつける</p>
</div>
</details>

<details open class="qa" data-tags="verification">
<summary>
<span class="qa-id">V8</span>
<span class="qa-title">LLM/模倣との区別：外形が似ていても“中身が違う”をどう判定する？</span>
<span class="qa-tags"><span class="tag">DISAMBIGUATION</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>会話や報告は模倣されやすい。区別には、介入応答・閉ループ・内部状態の整合が必要になる。</p>
<p><strong>次に必要：</strong>V2（介入）＋I1（閉ループ）＋R4（因果）を組み合わせた“逃げ道の少ない”評価</p>
</div>
</details>

<details open class="qa" data-tags="verification">
<summary>
<span class="qa-id">V9</span>
<span class="qa-title">追試：第三者が“同じ結論”に到達できる設計になっている？</span>
<span class="qa-tags"><span class="tag">REPRO</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>研究の最短距離は“他人が追試できる”状態を作ること。本人性の議論ほど追試性が重要になる。</p>
<p><strong>次に必要：</strong>P2（成果物）を満たす範囲で、データ/コード/評価を公開可能に整える</p>
</div>
</details>

<details open class="qa" data-tags="verification">
<summary>
<span class="qa-id">V10</span>
<span class="qa-title">モデル距離：生体脳とエミュレーションの“近さ”をどう測る？</span>
<span class="qa-tags"><span class="tag">METRIC</span><span class="tag">MATH</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>パラメータ空間での単純なユークリッド距離は、モデルの機能的な振る舞いの違いを反映しないことが多い。より本質的な「振る舞いの近さ」をどう定量化するか？</p>
<p><strong>方針：</strong>情報幾何学的指標 (Information Geometric Metrics) を採用する。特に<strong>フィッシャー情報量 (Fisher Information)</strong> は、パラメータの変化が確率分布（モデルの出力）に与える影響の大きさを表すため、これを計量（Metric）として用いることで、生物学的脳とエミュレートされた生成モデルの間の機能的な距離を厳密に定義できる。</p>
<p><strong>次に必要：</strong>Fisher Information Metric (FIM) を用いたモデル間距離の計算モジュールを実装し、V2（因果テスト）の定量評価に組み込む</p>
</div>
</details>

<details open class="qa" data-tags="verification">
<summary>
<span class="qa-id">V11</span>
<span class="qa-title">トポロジー：意識の“構造”は保存されているか？</span>
<span class="qa-tags"><span class="tag">TDA</span><span class="tag">GEOMETRY</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>PCI（複雑性）などのスカラー値だけでは、意識の「質的な構造（Qualitative Structure）」が同じかどうかわからない。</p>
<p><strong>提案：</strong>検証指標として<strong>位相的データ解析（TDA）</strong>、特に<strong>パーシステント・ホモロジー（Persistent Homology）</strong>を導入する。神経活動多様体（Neural Manifold）の「穴（サイクル）」や連結成分の数（ベッティ数）を比較することで、動的なアトラクタ構造の同一性を幾何学的に保証する。</p>
<p><strong>次に必要：</strong>パーシステンス図（Persistence Diagrams）を用いて、生体脳とエミュレーションの間のトポロジー距離（Bottleneck distance等）を計測する</p>
</div>
</details>
</div>
</div>

</section>

<section class="section" id="template">
<h2 class="section-title">科学的中心問いページ用テンプレ（推奨）</h2>
<p>新しい技術提案や問いのページを作成する際は、以下のMarkdownテンプレートをコピーして使用することを推奨します。R0（復元対象）とV0（検証基準）を先に固定する思考フローを強制する構成になっています。</p>

<details>
<summary><strong>テンプレートを表示（クリックで展開）</strong></summary>
<pre style="background: #f6f8fa; padding: 16px; border-radius: 6px; white-space: pre-wrap; font-size: 0.85em; overflow-x: auto;">
## 科学的中心問いページ用テンプレ（全部入り・そのままコピペ可）

&gt; 目的：**「R0（復元対象）とV0（検証基準）を先に固定し、その上でM0（計測）とI0（同定可能性）を議論する」**順序を強制するテンプレです。
&gt; ※各セクションは“未確定なら未確定”と明記して進められる形にしてあります。

---

# 0. タイトル

* **ページ題名**：
* **一文要約（結論先出し）**：

  * 「本ページは、＿＿＿＿を＿＿＿＿の基準で復元可能にするために、必要な計測要件（時空間解像度・観測変数）を同定する。」

---

# 1. 中心問い（CQ）

* **中心問い**：

  * 「＿＿＿＿を、どの時空間解像度で取得すれば、“復元すべき対象（R0）”が一意に近づくか？」
* **問いの焦点**（どれを主戦場にするか）：

  * [ ] 観測変数の選定（何を測るか）
  * [ ] 解像度・カバレッジの下限（どの程度細かく/広く）
  * [ ] ノイズ・欠測・個体差の許容範囲
  * [ ] 因果（介入可能性）を含む同定

---

# 2. 用語・スコープ固定（曖昧さ潰し）

* **対象種**：ヒト／動物（種：＿＿＿）／シミュレーション
* **状態の範囲**：安静／課題中（課題：＿＿＿）／睡眠／薬理介入
* **時間スケール**：ミリ秒〜秒／分〜時／日〜年
* **空間スケール**：細胞／カラム／領域／全脳
* **「復元」の意味**（直観ではなく定義で）：＿＿＿＿

---

# 3. R0：復元対象（最重要・先に確定）

## 3.1 何を復元するのか（対象の定義）

* **復元対象 R0**：

  * 例）構造（結線）／ダイナミクス（状態遷移）／機能（入力→出力）／記憶・方略／主観報告を含む自己モデル など
* **R0の出力形式**（最終的に何が出てくれば“復元”と言えるか）：

  * 例）パラメータ集合、生成モデル、状態空間モデル、エージェント方策、シミュレータ など

## 3.2 同一性（同値関係）＝「成功」の定義

* **同値関係（何が同じなら成功か）**：

  * 「＿＿＿＿が一致すればR0は同一とみなす」
* **許容誤差**（どこまで違っても同一扱いか）：

  * 指標：＿＿＿＿、閾値：＿＿＿＿

## 3.3 前提（R0に暗黙に含めている仮定）

* 例）脳はマルコフ的／観測可能な潜在状態が存在／学習可能な関数クラスで表現可能 等
* **仮定一覧**：

  * A1：＿＿＿＿
  * A2：＿＿＿＿
  * A3：＿＿＿＿

---

# 4. V0：検証基準（合否テスト）

## 4.1 何をもって「復元できた」と言うか（テスト設計）

* **検証タスク**：＿＿＿＿
* **評価データ**：同一個体内／個体間一般化／条件外挿（反事実）
* **ベースライン**：＿＿＿＿（例：単純モデル、既存手法）

## 4.2 指標（定量）と合格ライン（閾値）

* **主要指標**：＿＿＿＿（例：予測精度、尤度、因果効果の一致、行動分布距離）
* **合格ライン**：＿＿＿＿（閾値 or 比率）
* **再現性要件**：n=＿＿＿、再現率＿＿＿、事前登録の有無＿＿＿

## 4.3 介入・因果を使う場合（推奨：可能なら入れる）

* **介入手段**：刺激／薬理／損傷／閉ループ制御
* **介入時の一致条件**：＿＿＿＿（“応答が一致”の定義）

---

# 5. M0：計測の前提（MEASUREMENT）

## 5.1 計測路線の前提（どれを想定するか）

* **想定**：

  * [ ] in vivo（非侵襲）
  * [ ] in vivo（侵襲）
  * [ ] 破壊スキャン（ex vivo / 将来像）
* **安全・倫理・スケール制約**：＿＿＿＿

## 5.2 観測対象（何を測るか）候補リスト

* 電気：EEG/MEG/ECoG/単一・多点
* 血流：fMRI/fNIRS
* 光学：Ca imaging 等
* 構造：MRI/DTI/EM など
* **このページで主に扱う観測量**：＿＿＿＿

## 5.3 期待する時空間解像度・カバレッジ

* **時間分解能**：＿＿＿＿
* **空間分解能**：＿＿＿＿
* **被覆範囲**：局所／広域／全脳
* **サンプリング制約（持続時間・回数）**：＿＿＿＿
* **ノイズ床・欠測**：＿＿＿＿

---

# 6. P0：推定モデル／表現（モデル仮定を明示）

* **推定したい潜在表現**：状態空間／因子モデル／生成モデル／エージェント方策／コネクトーム等
* **学習パラダイム**：教師あり／自己教師／同化（data assimilation）／シミュレータ併用
* **必要な帰納バイアス**：＿＿＿＿（例：低次元、スパース、対称性、解剖学制約）
* **計算資源・実装制約**：＿＿＿＿

---

# 7. I0：同定可能性（このページの“芯”）

## 7.1 主張（1〜2文で）

* **I0主張**：

  * 「R0を一意に近づけるには、観測量＿＿＿＿を、時間＿＿＿＿・空間＿＿＿＿以上で取得する必要がある（少なくとも＿＿＿＿が下限）。」

## 7.2 必要条件（下限：これが無いと無理）

* **必要条件（観測の最小セット）**：＿＿＿＿
* **直観／根拠**：未観測自由度が残る／多対一写像になる／ノイズで不可分になる 等
* **“同定不能”の具体例**：＿＿＿＿（同じ観測を生む別解が構成できる 等）

## 7.3 十分条件（上限：ここまで取れれば原理的に可能）

* **十分条件**：＿＿＿＿
* **現実性**：今は不可能／将来可能性／代替案

## 7.4 失敗モード（重要：先回りで列挙）

* [ ] 多対一（別R0が同じ観測を生む）
* [ ] モデルミススペ（P0が間違っている）
* [ ] 介入不足で因果が切り分けられない
* [ ] 個体差で一般化が破れる
* [ ] ノイズ床・欠測で識別不能
* **検出方法**：＿＿＿＿（どの指標で“失敗”と判定するか）

## 7.5 「一意に近づく」を測る尺度

* **一意性スコア**（候補）：事後分布の集中度／同値類サイズ／識別距離 など
* **採用する尺度**：＿＿＿＿

---

# 8. 戦略分岐（A/B/C）※例のまま使える形

&gt; 各分岐は「M0の違い」だけでなく、**V0に到達する経路**と**I0を満たす見込み**を必ずセットで書きます。

## A：非侵襲（EEG/MEG/fMRI等）でモデルを鍛える

* **狙い**：＿＿＿＿（例：大規模・長期データで汎化を稼ぐ）
* **M0**：＿＿＿＿（解像度・カバレッジ・制約）
* **P0**：＿＿＿＿（表現・学習）
* **V0への到達経路**：＿＿＿＿（どのテストに通すか）
* **I0上のボトルネック**：＿＿＿＿（何が同定不能になりやすいか）
* **この分岐で得る“判定情報”**：＿＿＿＿（次の分岐選択に効く情報）

## B：侵襲（ECoG/深部/動物）で因果推論を強化

* **狙い**：＿＿＿＿（例：介入で因果・同定を強める）
* **M0**：＿＿＿＿
* **P0**：＿＿＿＿
* **V0への到達経路**：＿＿＿＿
* **I0上の改善点**：＿＿＿＿（介入で多対一を潰す等）
* **外挿（ヒト一般化）の扱い**：＿＿＿＿

## C：破壊的・超高解像度で構造を取る（将来像）

* **狙い**：＿＿＿＿（例：十分条件側の上限を検討）
* **M0**：＿＿＿＿（取得可能な構造情報）
* **P0**：＿＿＿＿（構造→機能の写像仮定）
* **V0への到達経路**：＿＿＿＿
* **I0の結論**：＿＿＿＿（原理的に十分か／まだ不足か）

---

# 9. 反証条件・停止規則（Stop rule）

## 9.1 全体反証（ページの根本を否定する条件）

* **反証条件**：

  * 「R0（復元対象）が定義されないまま計測だけ高級化しても、同定不能が解消されない」
  * 具体的には：＿＿＿＿（同じ観測で別R0が構成できる、V0を通らない 等）

## 9.2 分岐別の停止規則（撤退ライン）

* Aの停止：＿＿＿＿
* Bの停止：＿＿＿＿
* Cの停止：＿＿＿＿
* **ピボット条件**：＿＿＿＿（A→Bへ、B→Cへ、等の判断基準）

---

# 10. 次アクション（このページ内の優先順位を固定）

* **まず確定する**：

  1. R0（復元対象・同値関係）
  2. V0（合否テスト）
  3. I0（必要条件の下限主張）
* **今週やること**：＿＿＿＿
* **次に書き足すセクション**：＿＿＿＿
* **未確定の論点（質問リスト）**：

  * Q1：＿＿＿＿
  * Q2：＿＿＿＿

---

## 付録：1ページで俯瞰する「要点サマリ」枠（任意）

* **R0**：＿＿＿＿
* **V0**：＿＿＿＿
* **M0**：＿＿＿＿
* **P0**：＿＿＿＿
* **I0結論（下限/上限）**：＿＿＿＿
* **採用する分岐**：A/B/C（理由：＿＿＿＿）
* **反証・停止**：＿＿＿＿

---
</pre>
</details>
</section>

<section class="section" id="learning">
<h2 class="section-title">学習の順序（最短で全体像）</h2>
<p>“順番”は重要です。計測に強くても、検証基準が曖昧だと前進を主張できません。逆に、検証だけが立派でも、復元対象が定義できていなければ実装が迷走します。</p>
<ol>
<li><strong>全体像：</strong>WBEロードマップ（大枠の工程・ボトルネック）</li>
<li><strong>計測：</strong>どの解像度で何が失われるか（EEG/fMRI/侵襲/コネクトーム）</li>
<li><strong>再構成：</strong>逆問題→状態推定→生成モデル→介入予測、の順で“反証可能な復元”へ</li>
<li><strong>実装：</strong>モデル粒度を固定し、実行基盤差の影響を監査可能にする</li>
<li><strong>検証：</strong>評価スイートと反証条件を先に書き、更新履歴を残す</li>
</ol>
</section>

<section class="section" id="eegflow">
<h2 class="section-title">EEGFlow の現在地（このリポジトリでやること）</h2>
<p>EEGFlow は現時点では<strong>概念実装</strong>ですが、「計測→再構成→検証」のミニマムな流れを、EEG中心に試せる形を目指しています。</p>
<ul>
<li><a href="https://github.com/yasufumi-nakata/eegflow/blob/main/eegflow/01_preprocess.py" target="_blank">01_preprocess.py</a>：前処理（アーチファクト・品質管理の雛形） <strong>[QC Implemented]</strong></li>
<li><a href="https://github.com/yasufumi-nakata/eegflow/blob/main/eegflow/02_source_imaging.py" target="_blank">02_source_imaging.py</a>：ソース推定（逆問題の入口） <strong>[Uncertainty Implemented]</strong></li>
<li><a href="https://github.com/yasufumi-nakata/eegflow/blob/main/eegflow/03_causal_modeling.py" target="_blank">03_causal_modeling.py</a>：因果/生成モデル（予測・介入へ）</li>
</ul>
<p class="mini">※「解析手順の再現性」や「データ標準（BIDS）」は、WBE以前に研究として必須の足場です。</p>
</section>

<section class="section" id="sources">
<h2 class="section-title">参考（Issue #42 関連文献）</h2>
<ol>
<li>Cea, I., et al. (2024). Only consciousness truly exists? Two problems for IIT 4.0's ontology. <em>Frontiers in Psychology</em>.</li>
<li>Doerig, A., et al. (2019). The unfolding argument: Why diagrams of information flow cannot tell us anything about consciousness. <em>Consciousness and Cognition</em>.</li>
<li>Laukkonen, R. E., et al. (2025). A beautiful loop: An active inference theory of consciousness. <em>Psychological Review</em>.</li>
<li>Markram, H., et al. (2015). Reconstruction and Simulation of Neocortical Microcircuitry. <em>Cell</em>.</li>
<li>U.S. Senate. (2025). <em>MIND Act of 2025 (S.2925)</em>.</li>
<li>Sandberg, A., &amp; Bostrom, N. (2008). <em>Whole Brain Emulation: A Roadmap</em>.</li>
<li>Yamakawa, H., et al. (2024). Technology roadmap toward the completion of whole-brain architecture...</li>
</ol>
</section>

</article>

<aside class="sidebar-column">

<div class="key-points">
<h4>このページで得るもの</h4>
<ul>
<li>問いの木（詳細版）を1ページに集約</li>
<li>前進の定義（クレーム階段）の固定</li>
<li>折りたたみ＋絞り込みで探索</li>
<li>学習の順序（迷子にならない）</li>
<li>最初に当たる一次/総説リンク</li>
</ul>
</div>

<div class="sidebar-box">
<h4>Filter</h4>
<input id="qaSearch" class="filter-input" type="text" placeholder="キーワードで絞り込み（例: EEG, 因果, 本人性）">
<p class="small" style="margin-top: 10px;">カテゴリ</p>
<div class="checkbox-grid" style="margin-top: 8px;">
<label><input type="checkbox" name="qaTag" value="meta">Meta</label>
<label><input type="checkbox" name="qaTag" value="measurement">Measurement</label>
<label><input type="checkbox" name="qaTag" value="reconstruction">Reconstruction</label>
<label><input type="checkbox" name="qaTag" value="implementation">Implementation</label>
<label><input type="checkbox" name="qaTag" value="verification">Verification</label>
<label><input type="checkbox" name="qaTag" value="deployment">Deployment</label>
</div>
<div class="controls" style="margin-top: 12px;">
<button class="btn" id="qaClear" type="button">Clear</button>
<button class="btn" id="qaExpandAll" type="button">Expand</button>
<button class="btn" id="qaCollapseAll" type="button">Collapse</button>
</div>
<p class="small" id="qaStatus" style="margin-top: 10px;">表示: -/-</p>
</div>

<div class="sidebar-box">
<h4>On this page</h4>
<ul>
<li><a href="#howto">How to Use</a></li>
<li><a href="#definition">前進の定義</a></li>
<li><a href="#tree">問いの木</a></li>
<li><a href="#measurement">計測</a></li>
<li><a href="#reconstruction">再構成</a></li>
<li><a href="#implementation">実装</a></li>
<li><a href="#verification">検証</a></li>
<li><a href="#deployment">社会実装</a></li>
<li><a href="#learning">学習の順序</a></li>
<li><a href="#eegflow">EEGFlow の現在地</a></li>
<li><a href="#sources">参考文献</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Links</h4>
<ul>
<li><a href="index.html">Home</a></li>
<li><a href="technical_proposal_47.html">Technical Proposal #47</a></li>
<li><a href="mind_uploading_papers.html">Paper Collection</a></li>
<li><a href="brain_science_dictionary.html">Brain Science Dictionary</a></li>
<li><a href="https://github.com/yasufumi-nakata/eegflow" target="_blank">GitHub Repository</a></li>
<li><a href="issue.md">Contribute Guide</a></li>
</ul>
</div>

</aside>
</main>

<footer>
<p>EEGFlow · 技術ロードマップ（暫定）</p>
</footer>

<script>
(function () {
var searchInput = document.getElementById('qaSearch');
var clearBtn = document.getElementById('qaClear');
var expandBtn = document.getElementById('qaExpandAll');
var collapseBtn = document.getElementById('qaCollapseAll');
var statusEl = document.getElementById('qaStatus');

if (!searchInput || !statusEl) return;

function toArray(nodeList) {
return Array.prototype.slice.call(nodeList || []);
}

var checkboxes = toArray(document.querySelectorAll('input[name="qaTag"]'));
var qas = toArray(document.querySelectorAll('details.qa'));
var groups = toArray(document.querySelectorAll('[data-qa-group]'));

function selectedTags() {
return checkboxes
.filter(function (cb) { return cb.checked; })
.map(function (cb) { return cb.value; });
}

function matchesTags(qaTags, selected) {
if (!selected.length) return true;
for (var i = 0; i < selected.length; i++) {
if (qaTags.indexOf(selected[i]) !== -1) return true;
}
return false;
}

function matchesText(text, query) {
if (!query) return true;
return text.indexOf(query) !== -1;
}

function applyFilters() {
var query = (searchInput.value || '').trim().toLowerCase();
var selected = selectedTags();
var visibleCount = 0;

qas.forEach(function (qa) {
var qaTags = (qa.getAttribute('data-tags') || '')
.split(/\s+/)
.filter(Boolean);
var text = (qa.textContent || '').toLowerCase();
var show = matchesTags(qaTags, selected) && matchesText(text, query);
qa.style.display = show ? '' : 'none';
if (show) visibleCount += 1;
});

groups.forEach(function (g) {
var groupQas = toArray(g.querySelectorAll('details.qa'));
var anyVisible = groupQas.some(function (qa) { return qa.style.display !== 'none'; });
g.style.display = anyVisible ? '' : 'none';
});

statusEl.textContent = '表示: ' + visibleCount + '/' + qas.length;
}

function visibleQAs() {
return qas.filter(function (qa) { return qa.style.display !== 'none'; });
}

searchInput.addEventListener('input', applyFilters);
checkboxes.forEach(function (cb) { cb.addEventListener('change', applyFilters); });

if (clearBtn) {
clearBtn.addEventListener('click', function () {
searchInput.value = '';
checkboxes.forEach(function (cb) { cb.checked = false; });
applyFilters();
searchInput.focus();
});
}

if (expandBtn) {
expandBtn.addEventListener('click', function () {
visibleQAs().forEach(function (d) { d.open = true; });
});
}

if (collapseBtn) {
collapseBtn.addEventListener('click', function () {
visibleQAs().forEach(function (d) { d.open = false; });
});
}

applyFilters();
})();
</script>
