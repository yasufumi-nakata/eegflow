---
layout: default
title: "マインドアップロード実現への道：技術・理論の統合アプローチ"
description: "マインドアップロード実現のための中核となるコアサイト。意識や記憶の交換・複製を可能とする技術の研究とコミュニティの中心的ハブ。"
article_type: Perspective
subtitle: "脳の情報処理を別の基盤で再現し、心的機能を移植・複製するという研究仮説の現状と展望"
author: Mind Uploading Research Project
last_updated: "2026-01-15"
note: "研究ノート (2026年1月改訂)"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<!-- Abstract -->
<div class="abstract-box">
<h2>Abstract</h2>
<p>このページは、マインドアップロード（WBE）を「本当に検証できる研究」にするための長い研究ノートです。内容は、<strong>どう測るか</strong>、<strong>どう読み取るか</strong>、<strong>どう実装するか</strong>の3段階で整理しています。最新研究の成果だけでなく、うまくいっていない点や限界も同じ重みで扱い、「どこまで言えて、どこから言えないか」をはっきり分ける構成にしています。</p>
</div>

<div class="cta-box">
<h4>Start Here: Verification Commons</h4>
<p>Mind-Uploadの中心は「前進の定義」と「比較可能な検証基盤」を先に作ることです。</p>
<a href="verification.html">検証基盤（Platform）を見る →</a>
</div>

<div class="note-box">
<strong>新しく来た人へ</strong>
<p>
このページは長い研究ノートです。まずは <a href="wbe_101.html">WBE入門</a> と <a href="eeg_101.html">EEG入門</a>、必要なら <a href="glossary.html">用語集</a> を先に読むと迷子になりにくいです。
</p>
</div>

<!-- Introduction -->
<section class="section" id="introduction">
<h2 class="section-title">Introduction: Theoretical Foundations Revisited</h2>

<h3>1.1. 意識の科学：理論的基盤の再検討と「Adversarial Collaboration」の衝撃</h3>
<p>マインドアップロード（WBE）が再現すべき「意識」とは何か。この問いに対し、本プロジェクトは従来、統合情報理論（IIT）とグローバル神経ワークスペース理論（GNWT）の相補的統合を模索してきた。しかし、2025年に発表された大規模な**敵対的共同研究（Adversarial Collaboration）**の結果（Cogitate Consortium et al., Nature 2025<sup><a href="#ref-54">[54]</a></sup>）を受け、我々は方針を転換する。すなわち、両理論の統合ではなく、実験結果に基づく**「理論的限界の明記」**と、**「予測符号化（Predictive Coding）および自由エネルギー原理（Friston, 2010）への拡張」**へと舵を切る。この結果は、楽観的な統合論に修正を迫るものである。</p>

<div class="question-box">
<h4>中心的課題: 理論の予測と実験結果の乖離</h4>
<p>この歴史的な検証実験において、IITが予測した「後方皮質における持続的な同期活動」は完全には支持されず、一方でGNWTが予測した「前頭前野のイグニッション」も課題依存性が高い（意識経験そのものよりは報告動作に関連する）ことが示された<sup><a href="#ref-54">[54]</a></sup>。これは、現行の主要理論がいずれも意識の神経相関（NCC）を完全には説明しきれていないことを意味する。</p>
<div class="resolution-box">
<h5>解決の方向性: Phenomenal vs Functional Theories の相補的統合</h5>
<p>この結果を受け、本サイトでは特定の理論を教条的に支持する立場を取り下げる。ここで重要なのは、IITが<strong>「現象的意識（Phenomenal Consciousness）」</strong>の構造を説明しようとするのに対し、FEPや予測符号化はシステムが外界に適応するための<strong>「機能的プロセス（Functional Process）」</strong>を記述する理論であるというカテゴリーの違いを認識することである。</p>
<p>我々は、両者を対立するものとしてではなく、以下の役割分担で統合する。</p>
<ul style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 6px;"><strong>Phenomenal Layer (IIT 4.0):</strong> 意識の「質（Qualia）」や「統合性」を評価するための理論的「ものさし」として参照する（ただし実装上の計算負荷はPCI-ST等で近似する）。</li>
<li style="margin-bottom: 6px;"><strong>Functional Layer (FEP/Active Inference):</strong> その意識を生み出す基盤システムの「実装原理」として採用する。</li>
</ul>

<p>また、IIT批判である「Unfolding Argument」（Doerig et al., 2019<sup><a href="#ref-40">[40]</a></sup>）—機能的に等価なフィードフォワード網がΦ=0となり意識を持たないとされる問題—に対し、本プロジェクトは単なる「機能の模倣」を超えた要件を課す。具体的には、「因果構造の保存（Causal Structure Preservation）」を、<strong>マルコフブランケット（Markov Blanket）</strong><sup><a href="#ref-77">[77]</a></sup>の境界条件として厳密に定義する。</p>
<p>
ここで重要となるのは、デジタルエミュレーションと生物学的基盤の間の情報交換における<strong>「帯域幅」と「遅延」の閾値</strong>である。我々は、意識の質的変化（Qualitative shift）を引き起こさない条件として、生物学的統合時間窓（Integration Time Window, e.g., 10-100ms）以下の遅延と、神経結合の平均情報伝達容量以上の帯域幅を維持することを、物理的・工学的な制約条件として設定する。さらに、Laukkonen et al. (2025)<sup><a href="#ref-76">[76]</a></sup>が提唱する<strong>「生成モデルの反実仮想的等価性（Counterfactual Equivalence）」</strong>—システムが「もし〜だったら」という分岐構造を正しく再現できるか—を、WBEの本人性（Identity）の必要条件として検証プロセスに組み込む。
</p>
</div>
</div>

<h3>1.2. 理論から実装へ：技術的・哲学的課題</h3>
<p><strong>IITのデジタル基盤への移植課題：</strong> IIT 4.0<sup><a
href="#ref-17">[17]</a></sup>をWBEに応用するには、その公理系をデジタル基盤上でいかに満たすかという問題が残る。特に、物理的な実在を問う「内因的実在（Intrinsic
Existence）」の公理<sup><a
href="#ref-44">[44]</a></sup>は、離散的な計算システム（標準的なノイマン型コンピュータ）では原理的に満たされない可能性が高い（Unfolding Argument）。本プロジェクトでは、デジタルエミュレーションでの「近似」という表現を避け、<strong>ニューロモルフィック・ハードウェアによる因果構造の物理的写像</strong>へのシフトを明記する。あるいは、Albantakis et al. (2023)<sup><a href="#ref-17">[17]</a></sup>が示唆するように、生物学的ニューロンとデジタル素子を組み合わせた<strong>ハイブリッド・システム（Hybrid Systems）</strong>による段階的遷移を主軸に据え、単なる計算上の出力一致ではなく、物理的レベルでの因果力の保存を目指す。</p>

<p><strong>心理的連続性とコピー問題：</strong> デレク・パーフィットの心理的連続性理論<sup><a
href="#ref-4">[4]</a></sup>は、記憶や性格の連続性を本人性の根拠とする。これは、単なる静的なデータコピーではなく、「動的なプロセス」の維持をWBEに要求する。この理論が提起する「コピー問題（分身のパラドックス）」に対し、我々は「段階的な神経置換」や「ハイブリッド脳システム」といった思考実験を、検証可能な工学的プロトコルへと落とし込むことを目指す。
</p>
<p><strong>プロセス哲学への転回：</strong>
意識を静的な「モノ」ではなく、環境との相互作用の中で絶えず更新される「プロセス」として捉える視点は、Whiteheadのプロセス哲学<sup><a
href="#ref-32">[32]</a></sup>や、Fristonの自由エネルギー原理<sup><a
href="#ref-14">[14]</a></sup>／能動的推論<sup><a
href="#ref-45">[45]</a></sup>とも共鳴する。本プロジェクトは、この動的な実在性を計算機上で維持するための技術的要件（例：Slow
Continuous Mind Uploading）を具体化する<sup><a href="#ref-59">[59]</a></sup>。</p>
<div class="note-box">
<strong>研究としての約束</strong>
<p>以下を「最低限のガードレール」として運用する：主要な主張には一次/総説などの出典を付す・仮説と事実、価値判断を区別し不確実性を併記する・評価指標や手順を先に定義し再現可能性を優先する。</p>
</div>
</section>


<!-- Technical Framework -->
<section class="section" id="technical-framework">
<h2 class="section-title">Technical Framework</h2>

<p>マインドアップロードの実現に向けた技術的ロードマップは、「計測」「解読」「実装」の3段階で構想される。これは古典的なWBEロードマップ<sup><a
href="#ref-8">[8]</a></sup>に加え、近年の全脳アーキテクチャ構築ロードマップ<sup><a
href="#ref-7">[7]</a></sup>や大規模シミュレーション計画（Blue Brain等）<sup><a
href="#ref-16">[16]</a></sup>の知見を踏まえた整理である。</p>

<div class="stage-list">
<div class="stage-item">
<div class="stage-number"></div>
<div class="stage-body">
<h4>1. 計測（Sensing）：脳活動の精密な読み取りと不確実性の定量化</h4>
<p>高時間分解能を持つ脳波（EEG）はWBEの有力な入力信号ですが、その空間分解能の低さは根本的な課題です。脳波源推定（ESI）は、この課題を解決する計算論的アプローチですが、これは本質的に解が一意に定まらない<strong>不良設定問題（ill-posed problem）</strong>です<sup><a href="#ref-5">[5]</a></sup>。WBEのような極めて高い信頼性が求められる工学的目標において、従来の最小ノルム法（MNE）やdSPMのような点推定（Point Estimate）に依存することは、推定誤差をシステム全体に伝播させるリスクがあります。</p>
<p>この問題に対処するため、本プロジェクトでは<strong>経験ベイズ（Empirical Bayes）を用いた完全な事後分布の推定</strong>へと移行し、以下のプロトコルを標準採用します。</p>
<ul
style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;">
<strong>超高密度EEGとBlock-Champagneの統合：</strong>Block-Champagne Framework<sup><a href="#ref-78">[78]</a></sup>はスパースな活動推定に優れるが、深部脳活動や全脳ダイナミクスの再現には不十分である。したがって、<strong>超高密度EEG（High-density EEG, 256ch以上）</strong>と<strong>個体別MRIに基づく有限要素法（FEM）フォワードモデル</strong>の導入を必須条件とする。さらに、Feng et al. (2025)<sup><a href="#ref-78">[78]</a></sup>が指摘するノイズ特性の動的変化に対応するため、適応的ベイズ更新を実装に組み込む。
</li>
<li style="margin-bottom: 8px;">
<strong>不確実性の可視化と信頼区間：</strong>推定された脳活動マップには、振幅だけでなくその<strong>「信頼区間（Credible Intervals）」</strong>を常に併記し、不確実性が高い領域を明示するプロトコルを必須化します。これは`mind-upload/02_source_imaging.py`に実装されるべき中心機能です。
</li>
<li style="margin-bottom: 8px;">
<strong>順問題の不確実性と誤差伝播：</strong>頭部組織（特に頭蓋骨）の導電率や形状の誤差を確率変数として扱う<strong>順問題の不確実性モデリング</strong><sup><a href="#ref-79">[79]</a></sup>を導入し、最終的なソース活動の事後分布に誤差を伝播させることで、結果のロバスト性を真に評価可能にします。
</li>
</ul>
<div class="tag-list" style="margin-top: 12px;">
<span class="tag">Block-Champagne</span>
<span class="tag">Empirical Bayes</span>
<span class="tag">Credible Intervals</span>
<span class="tag">Uncertainty Quantification</span>
</div>
</div>
</div>
<div class="stage-item">
<div class="stage-number"></div>
<div class="stage-body">
<h4>2. 解読（Decoding）：能動的推論と反実仮想的等価性の導入</h4>
<p>「解読」のセクションにおいて、従来のデコーディング技術（Mind Captioning等）は「相関」に基づくマッピングに過ぎません。WBEにおける「本人性の保存」には、単なる入出力の模倣（哲学的ゾンビ）を超えた、<strong>因果構造の等価性</strong>の証明が必要です。</p>
<p>本プロジェクトでは、Laukkonen et al. (2025) が提唱する<strong>「反実仮想的等価性（Counterfactual Equivalence）」</strong><sup><a href="#ref-76">[76]</a></sup>を、同一性検証の中心的指標として採用します。</p>
<ul
style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;">
<strong>能動的推論（Active Inference）の統合：</strong>脳を受動的なデコーダーではなく、環境に対して働きかける<strong>「能動的推論エージェント」</strong>としてモデル化します<sup><a href="#ref-80">[80]</a></sup>。
</li>
<li style="margin-bottom: 8px;">
<strong>チューリング・テストの拡張（因果的摂動プロトコル）：</strong>静的な反実仮想の検証は不可能であるため、**「チューリング・テストを拡張した因果的摂動プロトコル（Causal Perturbation Protocol）」**を具体化する。TMS等による物理的摂動に対する生物学的脳の反応と、エミュレーション上の仮想的摂動に対する反応の統計的同一性を検証する指標（例：Perturbational Complexity Index, PCI）を導入し、動的な因果構造の一致を確認する。
</li>
</ul>
<div class="tag-list" style="margin-top: 12px;">
<span class="tag">Counterfactual Equivalence</span>
<span class="tag">Active Inference</span>
<span class="tag">Generative Model</span>
<span class="tag">Causal Structure</span>
</div>
</div>
</div>
<div class="stage-item">
<div class="stage-number"></div>
<div class="stage-body">
<h4>3. 実装（Implementation）：IIT 4.0 の計算論的限界と代替指標の検討</h4>
<p>本プロジェクトは従来、統合情報理論（IIT 4.0）を主要な理論基盤としてきましたが、その最大の問題である<strong>計算量の爆発（NP困難）</strong>と、デジタル基盤における「内因的実在」の定義の曖昧さに対処する必要があります。IITを教条的に支持するのではなく、2025年の<strong>「Adversarial Collaboration」の結果</strong><sup><a href="#ref-54">[54]</a></sup>を踏まえた、より現実的な実装指標へと拡張します。</p>
<ul
style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;">
<strong>計算可能な近似指標の採用：</strong>Φ（統合情報量）の直接計算はシステム規模に対して指数関数的に困難です。そのため、<strong>摂動複雑性指標（PCI-ST）</strong>や、大規模言語モデル（LLM）等でも適用可能な<strong>低次元埋め込みによる近似手法</strong><sup><a href="#ref-81">[81]</a></sup>を工学的目標に据えます。
</li>
<li style="margin-bottom: 8px;">
<strong>熱力学的制約の導入：</strong>デジタルエミュレーションにおける意識の維持条件として、情報の散逸構造や熱力学的不可逆性を考慮した<strong>「物理的基盤の要件」</strong>を明文化します。意識が非平衡開放系における散逸構造として維持されていることを踏まえ、エミュレーションにおける因果的力の密度やエネルギー効率が生物学的制約を満たすかを検証します。
</li>
</ul>
<div class="tag-list" style="margin-top: 12px;">
<span class="tag">IIT 4.0 Limits</span>
<span class="tag">PCI-ST</span>
<span class="tag">Thermodynamics</span>
<span class="tag">Dissipative Structures</span>
</div>
</div>
</div>
</div>
</section>

<!-- Decoding vs Emulation -->
<section class="section" id="decoding-to-emulation-gap">
<h2 class="section-title">デコーディングからエミュレーションへ：論理的ギャップの明示と検証設計</h2>

<div class="note-box">
<strong>TL;DR</strong>
<p>脳活動から文章を「読み出す」デコーディングは強力だが、それは基本的に<strong>観測された結果の翻訳</strong>であり、WBEが要求する<strong>脳ダイナミクスの生成（自律的な因果モデル）</strong>とは別物である<sup><a
href="#ref-8">[8]</a></sup>。このギャップを埋めるには、生成モデル（何が入力で、内部で何が起き、何が出力か）を明示し、介入（摂動）に対する予測で検証する必要がある<sup><a
href="#ref-13">[13]</a></sup><sup><a href="#ref-45">[45]</a></sup>。</p>
</div>

<h3>ギャップの中身（高校生にもわかる言い換え）</h3>
<p>たとえば「テストの答案」を読めても、<strong>その人が普段どう考えているか</strong>（新しい問題にどう対応するか）が再現できるとは限らない。同様に、brain-to-textは「今この瞬間の脳活動」を言葉にできても、WBEが必要とする「環境と相互作用しながら状態を更新し続けるプロセス」まで保証しない。</p>

<div class="visual-diagram diagram-decoding-gap">
  <div class="diagram-side decoding">
    <div class="diagram-icon">🧠</div>
    <div class="arrow-box">Decoding<br><span style="font-size:10px; font-weight:400; opacity:0.8;">(Translation)</span></div>
    <div class="diagram-icon">📝</div>
    <p class="diagram-caption">Output: Text/Media<br>(Static)</p>
  </div>
  <div class="diagram-divider">VS</div>
  <div class="diagram-side emulation">
    <div class="diagram-icon">🧠</div>
    <div class="arrow-box active">Emulation<br><span style="font-size:10px; font-weight:400; opacity:0.8;">(Causal Model)</span></div>
    <div class="diagram-icon">⚙️</div>
    <p class="diagram-caption">Output: Dynamics<br>(Process)</p>
  </div>
</div>

<h3>学術的に問題になるポイント（何を追加で示すべきか）</h3>
<ul style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;">
<strong>相関（decode）と生成（emulate）の違い：</strong>Mind Captioning<sup><a
href="#ref-11">[11]</a></sup>や連続言語復元<sup><a href="#ref-30">[30]</a></sup>は、脳信号から意味・文章を再構成できることを示した。しかしWBEは、同じ入力（感覚）を与えたときに内部状態がどう遷移し、将来の出力（行動・思考・自己モデル）がどう生成されるか、という因果過程そのものの再現を要求する<sup><a
href="#ref-8">[8]</a></sup>。
</li>
<li style="margin-bottom: 8px;">
<strong>言語事前分布（LLM）が勝ってしまう問題：</strong>LLMは流暢さゆえに、根拠が弱いときほど「それっぽい文章」を作れてしまう（hallucination）<sup><a
href="#ref-28">[28]</a></sup>。したがって、脳信号の情報量がどれだけ出力に寄与したかを、反事実入力（シャッフル等）でベースライン化し、棄権（abstention）設計を先に定義する必要がある（本ページのLLM節を参照）。
</li>
<li style="margin-bottom: 8px;">
<strong>多対一（同じ観測を説明する別モデル）の問題：</strong>EEG源推定が不良設定問題であるのと同様に<sup><a
href="#ref-5">[5]</a></sup>、「観測されたデータに合う説明」は複数あり得る。IITでも定義上の非一意性が議論されている<sup><a
href="#ref-3">[3]</a></sup>。WBEでは、<strong>観測一致だけでなく介入予測</strong>でモデルを絞り込む必要がある。
</li>
<li style="margin-bottom: 8px;">
<strong>意識・本人性の保存の検証：</strong>本人性を心理的連続性で捉える立場は、コピー問題（多重性）を含む<sup><a
href="#ref-4">[4]</a></sup><sup><a href="#ref-58">[58]</a></sup>。Slow Continuous Mind Uploading<sup><a
href="#ref-59">[59]</a></sup>のような「連続的移行」仮説を採る場合でも、少なくとも行動非依存の指標（PCI系）で「意識能力」が保存されるかを監査する必要がある<sup><a
href="#ref-47">[47]</a></sup>。
</li>
</ul>

<h3>ギャップを埋める実証プラン（最低限）</h3>
<ol style="margin: 0; padding-left: 20px; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;"><strong>生成モデルを明示する：</strong>DCMなどで、何が状態で何がパラメータかを明確化し、モデル比較可能な形で提示する<sup><a
href="#ref-13">[13]</a></sup>。</li>
<li style="margin-bottom: 8px;"><strong>介入（摂動）予測を事前登録する：</strong>PCI/PCI-STのように、摂動に対する反応の伝播・複雑性を評価軸に組み込む<sup><a
href="#ref-47">[47]</a></sup><sup><a href="#ref-51">[51]</a></sup>。</li>
<li style="margin-bottom: 8px;"><strong>反事実ベースラインを必須化する：</strong>入力シャッフル・試行入れ替え・モデルの温度固定などで、言語事前分布だけで出る出力を定量化し、効果量として報告する<sup><a
href="#ref-28">[28]</a></sup>。</li>
</ol>
</section>

<!-- Reproducibility -->
<section class="section" id="reproducibility">
<h2 class="section-title">プロジェクトの実体性と再現性 (Substance and Reproducibility)</h2>
<p>「Mind-Upload」というプロジェクト名が示す通り、本研究は計算論的手法に基づいている。しかし、現状のGitHubリポジトリはウェブサイト中心であり、研究プロジェクトとしての実体性・再現性が<strong>第三者に実行可能な形</strong>で十分提示されているとは言い難い。この重大な懸念に応えるため、本プロジェクトでは、データの整理規約としてBIDSおよびEEG-BIDS拡張<sup><a
href="#ref-25">[25]</a></sup><sup><a href="#ref-26">[26]</a></sup>を採用し、解析パイプライン・データスキーマ・実験条件ログを段階的に整備して、ウェブサイトの主張を裏付けるコードベースへ移行する。
</p>
<ul style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;">
<strong>データ処理パイプライン：</strong>BIDS/EEG-BIDS<sup><a href="#ref-25">[25]</a></sup><sup><a
href="#ref-26">[26]</a></sup>準拠の生データから、ESI、DCM解析に至るまでの最小限実行可能な処理スクリプト（Python/MNE-Python,
SPM, FieldTrip等のラッパー）を公開する。
</li>
<li style="margin-bottom: 8px;"><strong>デコーディングモデル：</strong>Mind
Captioningに類するTransformerベースのモデルアーキテクチャ定義と、ダミーデータを用いた学習・推論コードを公開する。</li>
<li style="margin-bottom: 8px;">
<strong>データスキーマの拡充：</strong>`dataset_description.json`に加え、EEGデータの具体的な構造（例：`sub-01/eeg/sub-01_task-rest_eeg.eeg`）や、計測プロトコルを記述した`eeg.json`のスキーマ例を公開し、BIDS標準の形式的遵守から実質的遵守へと移行する。
</li>
</ul>
</section>

<!-- Current Status -->
<section class="section" id="key-technical-challenges">
<h2 class="section-title">主要な技術的課題 (Key Technical Challenges)</h2>

<h3>コネクトームとダイナミクスのギャップ</h3>
<p>図1が示す構造的コネクトーム（神経配線図）の研究は大きく進展しているが、それだけでは脳の動的な活動を説明するには不十分である。脳機能は、主に2つの理由から、静的な配線図以上のものを要求する。第一に、脳の機能状態は、シナプス結合だけでなく、ドーパミンやセロトニンといった神経修飾物質が、拡散性の調節として広域に作用する<strong>ボリュームトランスミッション（volume transmission）</strong>（注意：EEGでいう体積伝導／volume conductionとは別概念）によっても大きく左右される<sup><a
href="#ref-19">[19]</a></sup>。こうした神経修飾は、安静時の動的な機能結合（動的コネクトーム）の再構成と関連し、遺伝的変動がその個体差に影響し得ることも報告されている<sup><a
href="#ref-39">[39]</a></sup>。第二に、これまで補助細胞と見なされてきた<strong>非神経細胞（特にアストロサイト）の役割が過小評価されている</strong>。近年の研究は、アストロサイトが神経伝達物質を感知・放出し、シナプス可塑性や情報処理の時定数を能動的に制御する「三者系シナプス（Tripartite
Synapse）」の不可欠な構成要素であることを示している<sup><a href="#ref-41">[41]</a></sup>。</p>
<p>このことは、脳のエミュレーションが、単なるニューロンの接続性（コネクトーム）の再現に留まらず、神経修飾状態やグリア細胞による変調ダイナミクスといった、より複雑な動的要素を第一級のパラメータとして組み込む必要があることを意味する。この静的な構造と動的な状態の間のギャップを埋めるため、将来的には遺伝子発現情報から神経接続の特性を推定する「トランスクリプトーム・コネクトミクス」<sup><a
href="#ref-33">[33]</a></sup>や、神経修飾状態をマッピングする動的な状態遷移モデルをフレームワークに統合する必要がある。
</p>

<!-- Figure: Connectome Progress -->
<div class="figure-box">
<div class="figure-content">
<div class="timeline-visual">
<div class="timeline-item">
<div class="timeline-dot done"></div>
<div class="timeline-label">線虫<br><strong>302</strong> neurons</div>
</div>
<div class="timeline-item">
<div class="timeline-dot done"></div>
<div class="timeline-label">ショウジョウバエ（FlyWire全脳）<br><strong>~139,000</strong> neurons<br><span style="font-size:10px; opacity:0.7;">Dorkenwald et al., Nature 2024</span></div>
</div>
<div class="timeline-item">
<div class="timeline-dot current"></div>
<div class="timeline-label">マウス<br><strong>~71M</strong> neurons</div>
</div>
<div class="timeline-item">
<div class="timeline-dot"></div>
<div class="timeline-label">ヒト<br><strong>~86B</strong> neurons</div>
</div>
</div>
</div>
<p class="figure-label">Figure 1</p>
<p class="figure-caption">コネクトーム研究の進展とスケール。線虫（<em>C.
elegans</em>）では全神経系のコネクトームが整備されつつあり<sup><a href="#ref-20">[20]</a></sup>、ショウジョウバエでは2024年にFlyWireプロジェクトにより成虫全脳コネクトーム（約139,000ニューロン）が完成した（Dorkenwald et al., 2024）<sup><a
href="#ref-21">[21]</a></sup>。一方で、機能的ダイナミクス（状態依存の結合変化）や、シナプス強度・神経修飾・グリアを含む力学の同定は依然課題である。マウスでは皮質の小体積で飽和再構成が達成されているが<sup><a
href="#ref-22">[22]</a></sup>、全脳規模の再構成は現在進行中である。ヒト脳は約860億ニューロンを有する<sup><a
href="#ref-57">[57]</a></sup>。
</p>
</div>

<!-- Figure: Verification Stack -->
<div class="figure-box">
<div class="figure-content">
<div class="flow-visual">
<div class="flow-step">
<div class="flow-title">計測</div>
<div class="flow-sub">HD-EEG / fMRI / MEG<br>品質保証・同期</div>
</div>
<div class="flow-step">
<div class="flow-title">逆問題</div>
<div class="flow-sub">ソース推定 / 不確実性<br>分布として保持</div>
</div>
<div class="flow-step">
<div class="flow-title">因果モデリング</div>
<div class="flow-sub">SCM / 介入設計<br>反実仮想の検証</div>
</div>
<div class="flow-step">
<div class="flow-title">同一性検証</div>
<div class="flow-sub">PCI / 構造保存<br>最小分岐セット</div>
</div>
</div>
</div>
<p class="figure-label">Figure 2</p>
<p class="figure-caption">WBE検証に必要な「計測→再構成→因果→検証」の連鎖。各段階の不確実性は次段階に引き継ぎ、介入により反実仮想的等価性を評価する。</p>
</div>
</section>

<!-- Research Program -->
<section class="section" id="research-program">
<h2 class="section-title">Research Program</h2>

<p>論文化を意識した実証プランでは、計測・解読・実装の各段階を統合的に示す。目標はマルチモーダル計測と神経解読を統合した「本人性維持」評価系の設計と論文化である。加えて、計測段階の柱として、EEGを中心とした<strong>行動非依存の意識指標</strong>（複雑性×摂動応答×臨界性）のロードマップも明示する。
</p>

<!-- Table: Roadmap -->
<table class="data-table">
<thead>
<tr>
<th>Phase</th>
<th>計測/データ</th>
<th>解読/解析</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>HD-EEG/fMRI同時計測セットアップ、再現性データ収集。IHM採用とBIDSメタデータ拡充。</td>
<td>Transformerベースのデコーディングに加え、LLM由来ノイズを定量化する「因果的整合性チェック」プロトコルの導入。</td>
</tr>
<tr>
<td>2</td>
<td>ESI信号分離とMEGデータの融合。逆問題制約条件の妥当性検証。</td>
<td>Dynamic Causal Modeling (DCM) による部位間因果ダイナミクス解析と生成モデルの同定。</td>
</tr>
<tr>
<td>3</td>
<td>WBA統合フレームワークでの動作検証。非神経細胞（グリア）のモデル化。</td>
<td><strong>神経学的チューリングテスト（Neural Turing Test）</strong>：オリジナルの脳とエミュレーションの「摂動応答（PCI）」の統計的同一性を検証。</td>
</tr>
</tbody>
</table>
</section>

<!-- LLM Research Update -->
<section class="section" id="llm-research-update">
<h2 class="section-title">LLM研究アップデート：脳解読における「言語事前分布」との付き合い方</h2>
<p>Mind Captioning<sup><a href="#ref-11">[11]</a></sup><sup><a href="#ref-12">[12]</a></sup>や、fMRIから連続言語を復元する近年のbrain-to-text系<sup><a
href="#ref-30">[30]</a></sup>では、Transformer/LLM<sup><a href="#ref-60">[60]</a></sup>が「自然な文章」を強力に補完する一方、入力側の証拠が弱いときに<strong>もっともらしいが根拠のない内容</strong>（hallucination）を生成し得ることが知られている<sup><a
href="#ref-28">[28]</a></sup>。また、自然音声を用いたfMRI研究では、語彙意味が大脳皮質に広く分布して表現され、一定程度デコード可能であることが示されている<sup><a
href="#ref-29">[29]</a></sup>。本プロジェクトで表現している「LLM由来ノイズ」は、この<strong>言語事前分布が勝ってしまう成分</strong>として捉え、実験・解析・評価の三点セットで切り分ける必要がある。</p>

<h3>近年のLLM研究（実装に効く要点）</h3>
<ul style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;"><strong>嗜好整合（指示追従）学習：</strong>RLHF/Instruction tuningで出力方針が変わるため、被験者間比較や縦断研究では「モデル/方針の固定」と「変更の記録」が重要になる<sup><a
href="#ref-61">[61]</a></sup>。学習を必要最小限にする場合はDPO系の選択肢もある<sup><a href="#ref-62">[62]</a></sup>。</li>
<li style="margin-bottom: 8px;"><strong>軽量な個人適応：</strong>被験者固有の語彙・記憶・文体に合わせる際、PEFT/量子化微調整（QLoRA等）で計算コストを抑えつつ適応できる<sup><a href="#ref-63">[63]</a></sup>。</li>
<li style="margin-bottom: 8px;"><strong>根拠付き生成（Grounding）：</strong>RAGにより、生成を外部コーパスに“接地”させ、根拠（参照元）をログとして残せる<sup><a href="#ref-64">[64]</a></sup>。</li>
<li style="margin-bottom: 8px;"><strong>ツール利用とエージェント化：</strong>推論と行為（検索・計算・操作）を分離し、どの外部情報が出力に影響したかを追跡可能にする枠組みが整ってきた<sup><a
href="#ref-65">[65]</a></sup><sup><a href="#ref-66">[66]</a></sup>。</li>
<li style="margin-bottom: 8px;"><strong>幻覚の検出：</strong>ブラックボックスでも自己一致性から幻覚を検出する系（SelfCheckGPT等）が提案されている<sup><a href="#ref-67">[67]</a></sup>。</li>
</ul>

<h3>Mind-Upload側での「因果的整合性チェック」への落とし込み</h3>
<ul style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;"><strong>LLM由来ノイズの基準線：</strong>脳信号シャッフル／試行入れ替え等の反事実入力で出力分布を推定し、「言語事前分布だけで出る文章」をベースライン化する。</li>
<li style="margin-bottom: 8px;"><strong>不確実性と棄権（abstention）：</strong>根拠が弱いときに無理に“それっぽい文”を出さない設計（低信頼時は要再計測/要追試として扱う）を先に決める。</li>
<li style="margin-bottom: 8px;"><strong>再現性ログ：</strong>モデル名/重み版、デコード温度、プロンプト、RAGコーパス、ツール呼び出しログを固定・保存して「同じ入力で同じ結論になる」状態を担保する。</li>
</ul>

<div class="tag-list" style="margin-top: 12px;">
<span class="tag">LLM</span>
<span class="tag">RAG</span>
<span class="tag">DPO</span>
<span class="tag">QLoRA</span>
<span class="tag">Hallucination</span>
</div>
</section>

<!-- EEG Consciousness Roadmap -->
<section class="section" id="eeg-consciousness-roadmap">
<h2 class="section-title">EEGで意識を測る：複雑性×摂動応答×臨界性ロードマップ</h2>

<p>マインドアップロードの「計測」段階は、単に神経信号を高密度に取得するだけでは完結しない。意識レベルや意識内容に関わる情報処理を、<strong>行動報告に依存せず</strong>に定量化し、条件差・個体差・装置差を越えて再現できる「ものさし」へ落とす必要がある。これはWBEの評価（アップロード後に意識が保たれているか）にも直結する。
</p>

<div class="note-box">
<strong>Design Goal</strong><br>
行動（報告）に依存しない指標、report confoundの分離、摂動による因果、一般化可能性──この4点を満たす評価系を、EEG中心に構築する。
</div>

<h3>強い結論に近づくための4要件</h3>
<ol style="margin: 0; padding-left: 20px; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;">
<strong>行動（報告）に依存しない意識指標</strong>：感覚入力や応答が制限されても推定できる指標（例：摂動複雑性）<sup><a
href="#ref-47">[47]</a></sup>
</li>
<li style="margin-bottom: 8px;"><strong>report
confoundの切り分け</strong>：no-reportパラダイム等で、知覚そのものと「報告に必要な後段処理」を分離する<sup><a
href="#ref-48">[48]</a></sup></li>
<li style="margin-bottom: 8px;">
<strong>相関ではなく因果</strong>：摂動（TMS等）に対する応答伝播の崩れ／維持を介して、結合性の因果的読み出しを行う<sup><a
href="#ref-49">[49]</a></sup>
</li>
<li style="margin-bottom: 8px;"><strong>一般化（頑健性）</strong>：被験者・条件・装置をまたいでも成立するパイプラインと検証設計（再現性・外部データ）
</li>
</ol>

<h3>コア発想：I/O「揺らぎ」を計測可能な量へ</h3>
<p>本サイトでは、意識を情報処理の「揺らぎ」と捉える直観を、査読耐性の高い定量指標へ接続するために、次の三つを中核に据える。</p>
<ul style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;"><strong>複雑性（complexity）</strong>：安静時EEGのLZ複雑性など、状態依存で変化する指標<sup><a
href="#ref-50">[50]</a></sup></li>
<li style="margin-bottom: 8px;"><strong>摂動応答の複雑性（perturbational
complexity）</strong>：刺激に対する状態遷移・次元圧縮に基づく指標（PCI/PCI-ST）<sup><a
href="#ref-47">[47]</a></sup><sup><a href="#ref-51">[51]</a></sup></li>
<li style="margin-bottom: 8px;">
<strong>臨界性（criticality）</strong>：脳活動が秩序と無秩序の境界、いわゆる「カオスの縁（edge-of-chaos）」に位置することで、複雑性と摂動感受性が最大化される力学状態。安静時EEGの臨界性指標が、意識レベルや意識能力を予測する強力な候補となっている<sup><a
href="#ref-52">[52]</a>, <a href="#ref-56">[56]</a></sup>。
</li>
</ul>
<p>この枠組みでは、I/Oは次のように読み替えられる：<strong>I（Input）＝摂動（刺激・介入）</strong>、<strong>O（Output）＝脳の複雑性応答</strong>、そしてその背景として<strong>臨界性</strong>を扱う。
</p>

<h3>研究の芯：2つの路線（A→Bの順で積む）</h3>
<table class="data-table">
<thead>
<tr>
<th>Route</th>
<th>狙い</th>
<th>強み</th>
<th>主な課題</th>
</tr>
</thead>
<tbody>
<tr>
<td>A</td>
<td>ベッドサイド意識メータ（行動不能でも推定）</td>
<td>臨床価値が高く、評価指標（PCI/PCI-ST）の議論が組みやすい<sup><a href="#ref-47">[47]</a></sup><sup><a
href="#ref-55">[55]</a></sup></td>
<td>摂動系（TMS等）の導入・安全性・運用コスト</td>
</tr>
<tr>
<td>B</td>
<td>臨界性からの統一説明（複雑性・摂動応答・伝播）</td>
<td>安静時EEGからの予測など、装置制約が小さい方向へ拡張できる<sup><a href="#ref-52">[52]</a></sup></td>
<td>交絡の統制と因果の取り方（介入設計）が難しい</td>
</tr>
</tbody>
</table>

<h3>ロードマップ（大学院を想定）</h3>
<div class="stage-list">
<div class="stage-item">
<div class="stage-number"></div>
<div class="stage-body">
<h4>フェーズ0：基盤整備（〜1年）—「測れる」「再現できる」を固める</h4>
<p>EEG解析パイプラインを固定し、複雑性・臨界性・report confound分離を同一データ上で回せる状態にする。</p>
<ul
style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;">前処理・アーチファクト除去・ログまで含む再現可能な解析（BIDS等）</li>
<li style="margin-bottom: 8px;">公開データで、麻酔/鎮静に伴う<strong>複雑性・スペクトル・結合性</strong>の変化を再現する<sup><a
href="#ref-23">[23]</a></sup><sup><a
href="#ref-50">[50]</a></sup><sup><a href="#ref-53">[53]</a></sup></li>
<li style="margin-bottom: 8px;">no-report設計（瞳孔/EOG/OKN等）を最初から組み込み<sup><a
href="#ref-48">[48]</a></sup></li>
<li style="margin-bottom: 8px;">多モーダルI/O（EEG＋EOG/瞳孔＋ECG/PPG）までを現実的に統合</li>
</ul>
<div class="tag-list" style="margin-top: 12px;">
<span class="tag">Reproducible Pipeline</span>
<span class="tag">No-Report</span>
<span class="tag">LZ Complexity</span>
<span class="tag">Criticality</span>
</div>
</div>
</div>

<div class="stage-item">
<div class="stage-number"></div>
<div class="stage-body">
<h4>フェーズ1：摂動応答（1〜2年目相当）—「PCI/PCI-STライン」を握る</h4>
<p>摂動（TMSや感覚刺激等）に対する応答複雑性を中核指標として整備し、行動非依存の推定に接続する。</p>
<ul
style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;">理想：TMS-EEGでPCI系指標を扱う<sup><a
href="#ref-47">[47]</a></sup></li>
<li style="margin-bottom: 8px;">現実解：PCI-STの思想（刺激応答の状態遷移・次元圧縮）を他の摂動へ移植<sup><a
href="#ref-51">[51]</a></sup></li>
</ul>
<div class="tag-list" style="margin-top: 12px;">
<span class="tag">Perturbation</span>
<span class="tag">PCI / PCI-ST</span>
<span class="tag">Causal Propagation</span>
</div>
</div>
</div>

<div class="stage-item">
<div class="stage-number"></div>
<div class="stage-body">
<h4>フェーズ2：安静時から推定（2〜3年目相当）—「摂動なし」へ拡張</h4>
<p>安静時EEGの力学指標（臨界性など）から、意識能力や摂動応答指標を予測する方向へ伸ばす。これにより、侵襲的な摂動なしでの意識評価、すなわち臨床での大規模スクリーニングの可能性が拓かれる。
</p>
<p style="margin-top: 8px;">
最新の研究は、この方向性を支持している。安静時EEGの臨界性指標は、麻酔に伴う意識消失と関連し、摂動複雑性（PCI系）を予測し得ることが報告されている<sup><a
href="#ref-52">[52]</a></sup>。また、臨界性が情報処理に利点をもたらし得るという理論的背景（臨界性仮説）も整理されており<sup><a
href="#ref-56">[56]</a></sup>、両アプローチを接続する枠組みとして再検討する価値がある。
</p>
<div class="tag-list" style="margin-top: 12px;">
<span class="tag">Resting-State EEG</span>
<span class="tag">Critical Dynamics</span>
<span class="tag">Bedside</span>
</div>
</div>
</div>

<div class="stage-item">
<div class="stage-number"></div>
<div class="stage-body">
<h4>フェーズ3：因果（3〜4年目相当）—「条件」であることを示す</h4>
<p>複雑性／臨界性／摂動応答が、単なる相関ではなく意識の条件であることを、介入または状態操作で押さえる。</p>
<ul
style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;">介入で指標を動かし、意識関連アウトカムの変化と対応づける</li>
<li style="margin-bottom: 8px;">薬理・鎮静・麻酔など、状態変化に沿って系列を揃える<sup><a
href="#ref-50">[50]</a></sup></li>
</ul>
<div class="tag-list" style="margin-top: 12px;">
<span class="tag">Causality</span>
<span class="tag">Intervention</span>
<span class="tag">Anesthesia</span>
</div>
</div>
</div>
</div>

<div class="resolution-box">
<h5>直近1〜3か月のToDo（最小で効く順）</h5>
<ul
style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 13px; line-height: 1.5; color: #d7e2cf;">
<li style="margin-bottom: 6px;">解析パイプラインを固定（自動化・ログ・再現性）</li>
<li style="margin-bottom: 6px;">同一EEGで「複雑性＋臨界性」を計算し、再テスト信頼性を評価</li>
<li style="margin-bottom: 6px;">reportあり／なし条件を併走できる実験設計にする<sup><a href="#ref-48">[48]</a></sup>
</li>
<li style="margin-bottom: 6px;">公開データで、麻酔/鎮静に伴う変化を一度再現する<sup><a href="#ref-50">[50]</a></sup>
</li>
<li>摂動導入の可否に応じて、PCI/PCI-ST路線の技術調査と共同先探索<sup><a href="#ref-51">[51]</a></sup></li>
</ul>
</div>

<h3>理論的立ち位置と研究のインパクト</h3>
<p>本ロードマップは、特定の意識理論（IIT,
GNWT等）の正しさを証明すること自体を目的としない。むしろ、それらの理論に「巻き込まれず、利用する」というプラグマティックな立ち位置をとる。すなわち、複雑性、摂動応答、臨界性といった<strong>測定可能な量</strong>を軸に研究を進め、各理論が提唱する仮説を検証するための「ものさし」を提供することを目指す。このアプローチは、近年の理論対立を共同検証によって解決しようとする学術的潮流とも合致する<sup><a
href="#ref-54">[54]</a></sup>。</p>
<p>この研究の先に目指すのは、単一の論文に留まらない「ノーベル級のインパクト」を生み出す構造の設計である。具体的には、(1)臨床現場で利用可能な「世界標準の意識指標」を確立すること、(2)介入によって意識状態を操作し「相関から因果へ」と議論を深めること、そして(3)重症患者の診断支援など「臨床で実際に人を救う」こと、の3点を満たすことで、研究の価値を社会的に実証する。
</p>
</section>

<!-- Technical Proposals -->
<section class="section" id="technical-proposals">
<h2 class="section-title">Technical Proposals</h2>
<p>研究ロードマップを支える具体的な技術提案です。ここでは提案内容を本文に統合し、エビデンスと実装の焦点を一望できるように整理しています。</p>

<div class="stage-list">
<div class="stage-item">
<div class="stage-number">46</div>
<div class="stage-body">
<h4>計測QA・同期・BIDS準拠の統合</h4>
<p>計測品質の可視化（インピーダンス/ノイズフロア/CMRR）と同期の標準化を、BIDS-EEGのメタデータ構造に直接結び付ける。EEG-BIDSは <code>dataset_description.json</code> や <code>eeg.json</code>、<code>channels.tsv</code>、<code>electrodes.tsv</code> 等の明示的メタデータを要求し、再現性・可搬性を担保する枠組みを提供する。</p>
<ul>
<li>BIDS-EEGの構造・必須メタデータをQAログと連携し、再現可能な「計測の証跡」を残す<sup><a href="#ref-83">[83]</a></sup></li>
<li>マルチモーダル同期はLSLのサンプルタイムスタンプとジッタ補正を標準に据える<sup><a href="#ref-84">[84]</a></sup></li>
</ul>
<p><a href="technical_proposal_46.html">→ Technical Proposal #46</a></p>
</div>
</div>

<div class="stage-item">
<div class="stage-number">47</div>
<div class="stage-body">
<h4>前処理の再現性強化とネットワーク指標</h4>
<p>ノイズ除去と接続性推定の「再現性」を担保することが重点。ASRの自動除去とZapLineの線雑音抑制を組み合わせ、wPLI/STEで体積伝導・方向性の問題に対処する。</p>
<ul>
<li>ASRは自動アーティファクト除去手法として評価が進んでおり、パラメータ範囲の指針が示されている<sup><a href="#ref-85">[85]</a></sup></li>
<li>ZapLineは線雑音除去のための実証済み手法で、EEG/MEGに適用可能<sup><a href="#ref-86">[86]</a></sup></li>
<li>wPLIは体積伝導とノイズの影響を抑えた位相同期指標<sup><a href="#ref-87">[87]</a></sup>、STEは方向性情報流の推定に有効<sup><a href="#ref-88">[88]</a></sup></li>
</ul>
<p><a href="technical_proposal_47.html">→ Technical Proposal #47</a></p>
</div>
</div>

<div class="stage-item">
<div class="stage-number">48</div>
<div class="stage-body">
<h4>神経工学的拡張（OPM-MEG / Hyper-scanning）</h4>
<p>OPM-MEGの可搬性と動作自由度は、VRや自然行動下の計測を現実的にする。ウェアラブルMEGの実証は「動きながらの高時間分解能計測」を研究パイプラインに組み込む根拠となる。</p>
<ul>
<li>ウェアラブルMEGの実証により、自然な動きを伴う計測が可能になった<sup><a href="#ref-89">[89]</a></sup></li>
</ul>
<p><a href="technical_proposal_48.html">→ Technical Proposal #48</a></p>
</div>
</div>

<div class="stage-item">
<div class="stage-number">56</div>
<div class="stage-body">
<h4>識別可能性と因果介入（PCI / do-calculus）</h4>
<p>反実仮想の検証は観測だけでは不可能であり、介入データが必要。PCI（TMS-EEGに基づく摂動複雑性）をGround Truthの参照点とし、介入に対する応答分布の一致を検証する。</p>
<ul>
<li>因果階層は「観測・介入・反実仮想」の3層で構成される<sup><a href="#ref-91">[91]</a></sup></li>
<li>PCIはTMS-EEG応答の複雑性を用いた意識指標として提案されている<sup><a href="#ref-90">[90]</a></sup></li>
</ul>
<p><a href="technical_proposal_56.html">→ Technical Proposal #56</a></p>
</div>
</div>

<div class="stage-item">
<div class="stage-number">58</div>
<div class="stage-body">
<h4>熱力学・因果・IIT計算量のギャップ対応</h4>
<p>「論理的コスト」だけでは不十分で、非平衡定常状態を支える散逸の指標（EPR）を明示する必要がある。またIITの厳密計算は指数的に重く、近似・境界条件の設計が必須。</p>
<ul>
<li>非平衡系のエントロピー生成は不可逆性の定量指標として確立されている<sup><a href="#ref-92">[92]</a></sup></li>
<li>IITのMIP探索は系のサイズに対して指数的コストがかかるため、近似や計算戦略が必須<sup><a href="#ref-93">[93]</a></sup></li>
</ul>
<p><a href="technical_proposal_58.html">→ Technical Proposal #58</a></p>
</div>
</div>

<div class="stage-item">
<div class="stage-number">61</div>
<div class="stage-body">
<h4>因果・熱力学の論理ギャップ補強</h4>
<p>因果構造保存とEPR<sup><a href="#ref-92">[92]</a></sup>の同時検証を「同一性要件」に組み込み、計算機上のエミュレーションが物理的制約を満たすかを可視化する。</p>
<p><a href="technical_proposal_61.html">→ Technical Proposal #61</a></p>
</div>
</div>

<div class="stage-item">
<div class="stage-number">62</div>
<div class="stage-body">
<h4>熱力学的・因果的妥当性の強化</h4>
<p>PCI<sup><a href="#ref-90">[90]</a></sup>・EPR<sup><a href="#ref-92">[92]</a></sup>・SCM<sup><a href="#ref-91">[91]</a></sup>の3点セットを検証パイプラインに組み込み、反実仮想と散逸の両側面から妥当性を判定する。</p>
<p><a href="technical_proposal_62.html">→ Technical Proposal #62</a></p>
</div>
</div>
</div>
</section>

<!-- Limitations -->
<section class="section" id="limitations">
<h2 class="section-title">Limitations and Epistemic Humility</h2>

<div class="note-box">
<strong>このページの限界を明示する</strong>
<p>
研究ノートとして、以下の構造的限界を認識し明記します。これらは「弱点」ではなく、科学的誠実さの要件です。
</p>
</div>

<h3>理論的限界</h3>
<ul style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;"><strong>ハードプロブレムの回避：</strong>本ページは機能的等価性を操作的定義として採用するが、現象的意識（phenomenal consciousness）の同一性は検証対象外である。機能的に完全なエミュレーションが「意識を持つ」ことの十分条件であるかは、本プロジェクトの枠組みでは判定不能である（Chalmers, 1995）。</li>
<li style="margin-bottom: 8px;"><strong>理論的中立性の限界：</strong>「理論に依存しない」と宣言しつつも、PCI等の指標選択自体がIIT寄りの暗黙的前提を含む可能性がある。この潜在的バイアスを完全に排除することはできない。</li>
<li style="margin-bottom: 8px;"><strong>FEPの反証可能性：</strong>自由エネルギー原理は包括的すぎて反証不可能との批判がある。本プロジェクトはFEPを「実装原理」として採用するが、その妥当性は経験的成果で別途検証する必要がある。</li>
<li style="margin-bottom: 8px;"><strong>Unfolding Argumentの含意：</strong>Doerig et al. (2019)<sup><a href="#ref-40">[40]</a></sup>の議論が正しければ、デジタルエミュレーションではIITの意味での意識（Φ>0）は原理的に生じない。ニューロモルフィック基盤への移行は必須となるが、その工学的実現可能性は未検証である。</li>
</ul>

<h3>工学的限界</h3>
<ul style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;"><strong>計測−再現ギャップ：</strong>非侵襲EEG（空間解像度~1-2cm）とWBEが要求する詳細度（シナプスレベル~nm）の間には約7桁のギャップがある。逆問題の不良設定性は原理的に解消されない。</li>
<li style="margin-bottom: 8px;"><strong>再現性の現状：</strong>本プロジェクトが掲げるL0（第三者再現可能性）は、現時点では達成されていない。リポジトリは主にウェブサイトコンテンツであり、実行可能なコード・データ・環境情報は未公開である。</li>
<li style="margin-bottom: 8px;"><strong>コネクトーム-ダイナミクスギャップの深刻さ：</strong>FlyWire（2024）やC. elegans（2019）のコネクトームが完成しても、それだけでは行動の予測に不十分であることが示されている。構造から機能への変換は、WBEの中核的未解決問題である。</li>
</ul>

<h3>プロジェクト運営の限界</h3>
<ul style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;"><strong>個人プロジェクト：</strong>現時点では個人の研究ノートであり、ピアレビューを受けた研究ではない。外部検証と共同研究の拡大が必要である。</li>
<li style="margin-bottom: 8px;"><strong>設計と実装の乖離：</strong>本ページに記述された設計方針の多くは文書レベルに留まり、実装コード・テストデータ・評価結果として公開されていない。</li>
</ul>
</section>

<!-- About -->
<section class="section" id="about">
<h2 class="section-title">About</h2>
<p><strong>中田 康史 (Yasufumi Nakata)</strong><br>
慶應義塾大学 環境情報学部 / 青山敦研究室 所属。<br>
本サイトはマインドアップロード研究に関する公開研究ノートです。</p>
</section>

<!-- References -->
<section class="section references" id="references">
<h2 class="section-title">References</h2>
<ol>
<li id="ref-1" value="1">Fleming, S. M., et al. (2023). Open letter regarding "The integrated information
theory of consciousness". <em>Neuroscience of Consciousness</em>, 2023(1), niad001. <a
href="https://doi.org/10.31234/osf.io/zsr78">doi:10.31234/osf.io/zsr78</a></li>
<li id="ref-2" value="2">Tononi, G., et al. (2016). Integrated information theory: from consciousness to its
physical substrate. <em>Nat. Rev. Neurosci.</em>, 17, 450–461. <a
href="https://doi.org/10.1038/nrn.2016.44">doi:10.1038/nrn.2016.44</a></li>
<li id="ref-3" value="3">Hanson, J. R. (2023). On the non-uniqueness problem in integrated information theory.
<em>Neuroscience of Consciousness</em>, 2023(1), niad014. <a
href="https://doi.org/10.1093/nc/niad014">doi:10.1093/nc/niad014</a>
</li>
<li id="ref-4" value="4">Parfit, D. (1984). <em>Reasons and Persons</em>. Oxford University Press.</li>
<li id="ref-5" value="5">Michel, C. M., & Brunet, D. (2019). EEG source imaging: a practical review of the
methodology. <em>Frontiers in Neurology</em>, 10, 325. <a
href="https://doi.org/10.3389/fneur.2019.00325">doi:10.3389/fneur.2019.00325</a></li>
<li id="ref-6" value="6">Koch, C., Massimini, M., Boly, M., & Tononi, G. (2016). Neural correlates of consciousness: Progress and
problems. <em>Nature Reviews Neuroscience</em>, 17(5), 307–321. <a
href="https://doi.org/10.1038/nrn.2016.22">doi:10.1038/nrn.2016.22</a></li>
<li id="ref-7" value="7">Yamakawa, H., et al. (2024). Technology roadmap toward the completion of whole-brain
architecture with BRA-driven development. <em>Cognitive Systems Research</em>, 88, 101300. <a
href="https://doi.org/10.1016/j.cogsys.2024.101300">doi:10.1016/j.cogsys.2024.101300</a>
</li>
<li id="ref-8" value="8">Sandberg, A., & Bostrom, N. (2008). <em>Whole Brain Emulation: A Roadmap</em>. Future
of Humanity Institute, Oxford University. <a
href="https://www.philosophyofbrains.com/wp-content/uploads/2013/08/2008-3.pdf">Link</a>
</li>
<li id="ref-9" value="9">Logothetis, N. K. (2008). What we can do and what we cannot do with fMRI.
<em>Nature</em>, 453(7197), 869-878. <a
href="https://doi.org/10.1038/nature06976">doi:10.1038/nature06976</a>
</li>
<li id="ref-10" value="10">Yuste, R., et al. (2017). Four ethical priorities for neurotechnologies and AI.
<em>Nature</em>, 551(7679), 159-163. <a
href="https://doi.org/10.1038/551159a">doi:10.1038/551159a</a>
</li>
<li id="ref-11" value="11">Horikawa, T., et al. (2025). Mind captioning: Evolving descriptive text of mental
content from human brain activity. <em>Science Advances</em>, 11(45), eadw1464. <a
href="https://doi.org/10.1126/sciadv.adw1464">doi:10.1126/sciadv.adw1464</a></li>
<li id="ref-12" value="12">Kozlov, M. (2025). 'Mind-captioning' AI decodes brain activity to turn thoughts into
text. <em>Nature</em>, 647(8089), 297. <a
href="https://doi.org/10.1038/d41586-025-03624-1">doi:10.1038/d41586-025-03624-1</a>
(Note: ニュース記事。一次研究は[11]を参照)</li>
<li id="ref-13" value="13">Friston, K. J., Harrison, L., & Penny, W. (2003). Dynamic causal modelling.
<em>NeuroImage</em>, 19(4), 1177-1202. <a
href="https://doi.org/10.1016/S1053-8119(03)00202-7">doi:10.1016/S1053-8119(03)00202-7</a>
</li>
<li id="ref-14" value="14">Friston, K. (2010). The free-energy principle: a rough guide to the brain.
<em>Nature Reviews Neuroscience</em>, 11(2), 127–138. <a
href="https://doi.org/10.1038/nrn2787">doi:10.1038/nrn2787</a>
</li>
<li id="ref-15" value="15">Vorwerk, J., et al. (2014). A guideline for head volume conductor modeling in EEG and MEG.
<em>NeuroImage</em>, 100, 590–607. <a
href="https://doi.org/10.1016/j.neuroimage.2014.06.040">doi:10.1016/j.neuroimage.2014.06.040</a></li>
<li id="ref-16" value="16">Markram, H. (2006). The Blue Brain Project. <em>Nature Reviews Neuroscience</em>,
7(2), 153-160. <a href="https://doi.org/10.1038/nrn1860">doi:10.1038/nrn1860</a></li>
<li id="ref-17" value="17">Albantakis, L., et al. (2023). Integrated information theory (IIT) 4.0: Formulating
the properties of phenomenal existence in physical terms. <em>PLOS Computational Biology</em>,
19(10), e1011465. <a
href="https://doi.org/10.1371/journal.pcbi.1011465">doi:10.1371/journal.pcbi.1011465</a>
</li>
<li id="ref-18" value="18">Wipf, D., & Nagarajan, S. (2009). A unified Bayesian framework for MEG/EEG source imaging.
<em>NeuroImage</em>, 44(3), 947–966. <a
href="https://doi.org/10.1016/j.neuroimage.2008.02.059">doi:10.1016/j.neuroimage.2008.02.059</a></li>
<li id="ref-19" value="19">Özçete, Ö. D., et al. (2024). Mechanisms of neuromodulatory volume transmission.
<em>Molecular Psychiatry</em>. <a href="https://doi.org/10.1038/s41380-024-02608-3">doi:10.1038/s41380-024-02608-3</a></li>
<li id="ref-20" value="20">Cook, S. J., et al. (2019). Whole-animal connectomes of both <em>Caenorhabditis elegans</em> sexes.
<em>Nature</em>, 571(7763), 63–71. <a href="https://doi.org/10.1038/s41586-019-1352-7">doi:10.1038/s41586-019-1352-7</a></li>
<li id="ref-21" value="21">Scheffer, L. K., et al. (2020). A connectome and analysis of the adult <em>Drosophila</em> central
brain. <em>eLife</em>, 9. <a href="https://doi.org/10.7554/eLife.57443">doi:10.7554/eLife.57443</a></li>
<li id="ref-22" value="22">Kasthuri, N., et al. (2015). Saturated reconstruction of a volume of neocortex.
<em>Cell</em>, 162(3), 648–661. <a href="https://doi.org/10.1016/j.cell.2015.06.054">doi:10.1016/j.cell.2015.06.054</a></li>
<li id="ref-23" value="23">Purdon, P. L., et al. (2013). Electroencephalogram signatures of loss and recovery of consciousness from
propofol. <em>PNAS</em>, 110(12), E1142–E1151. <a href="https://doi.org/10.1073/pnas.1221180110">doi:10.1073/pnas.1221180110</a></li>
<li id="ref-24" value="24">Schumer, C., et al. (2025). <em>Management of Individuals' Neural Data (MIND) Act of
2025</em>. U.S. Senate Bill. (Note: Proposed bill as of Jan 12, 2026).</li>
<li id="ref-25" value="25">Gorgolewski, K. J., et al. (2016). The brain imaging data structure, a format for organizing and
describing outputs of neuroimaging experiments. <em>Scientific Data</em>, 3. <a
href="https://doi.org/10.1038/sdata.2016.44">doi:10.1038/sdata.2016.44</a></li>
<li id="ref-26" value="26">Pernet, C. R., et al. (2019). EEG-BIDS, an extension to the brain imaging data structure for
electroencephalography. <em>Scientific Data</em>, 6(1). <a
href="https://doi.org/10.1038/s41597-019-0104-8">doi:10.1038/s41597-019-0104-8</a></li>
<li id="ref-27" value="27">Ienca, M., & Andorno, R. (2017). Towards new human rights in neuroscience. <em>Life
Sciences, Society and Policy</em>, 13(1), 5. <a
href="https://doi.org/10.1186/s40504-017-0050-1">doi:10.1186/s40504-017-0050-1</a></li>
<li id="ref-28" value="28">Ji, Z., et al. (2023). Survey of Hallucination in Natural Language Generation. <em>ACM Computing
Surveys</em>, 55(12). <a href="https://doi.org/10.1145/3571730">doi:10.1145/3571730</a></li>
<li id="ref-29" value="29">Huth, A. G., et al. (2016). Natural speech reveals the semantic maps that tile human cerebral cortex.
<em>Nature</em>, 532(7600), 453–458. <a href="https://doi.org/10.1038/nature17637">doi:10.1038/nature17637</a></li>
<li id="ref-30" value="30">Tang, J., et al. (2023). Semantic reconstruction of continuous language from non-invasive brain
recordings. <em>Nature Neuroscience</em>, 26(5), 858–866. <a
href="https://doi.org/10.1038/s41593-023-01304-9">doi:10.1038/s41593-023-01304-9</a></li>
<li id="ref-31" value="31">Boly, M., et al. (2017). Are the neural correlates of consciousness in the front or in the back of the
cerebral cortex? Clinical and neuroimaging evidence. <em>Journal of Neuroscience</em>, 37(40),
9603–9613. <a href="https://doi.org/10.1523/JNEUROSCI.3218-16.2017">doi:10.1523/JNEUROSCI.3218-16.2017</a></li>
<li id="ref-32" value="32">Whitehead, A. N. (1929). <em>Process and Reality: An Essay in Cosmology</em>. Macmillan.
(Note: プロセス哲学の古典。版によって出版年・出版社表記が異なる)</li>
<li id="ref-33" value="33">Gamlin, C. R., et al. (2025). Connectomics of predicted Sst transcriptomic types in mouse visual
cortex. <em>Nature</em>, 640(8058), 497–505. <a
href="https://doi.org/10.1038/s41586-025-08805-6">doi:10.1038/s41586-025-08805-6</a></li>
<li id="ref-39" value="39">Jun, S., Altmann, A., Sadaghiani, S., et al. (2025). Modulatory Neurotransmitter Genotypes Shape Dynamic
Functional Connectome Reconfigurations. <em>Journal of Neuroscience</em>, 45(10). <a
href="https://doi.org/10.1523/JNEUROSCI.1939-24.2025">doi:10.1523/JNEUROSCI.1939-24.2025</a>
(Open Access: <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11884390/">PMC11884390</a>)</li>
<li id="ref-40" value="40">Doerig, A., et al. (2019). The unfolding argument: Why IIT and other causal
structure theories cannot explain consciousness. <em>Consciousness and Cognition</em>, 72, 49–59. <a
href="https://doi.org/10.1016/j.concog.2019.04.002">doi:10.1016/j.concog.2019.04.002</a>
</li>
<li id="ref-41" value="41">Santello, M., et al. (2019). Astrocyte-neuron interactions: from synapses to
networks and behavior. <em>Neuron</em>, 103(6), 985-1000. <a
href="https://doi.org/10.1016/j.neuron.2019.08.024">doi:10.1016/j.neuron.2019.08.024</a>
</li>
<li id="ref-42" value="42">Melloni, L., et al. (2023). An adversarial collaboration protocol for testing
contrasting predictions of global neuronal workspace and integrated information theory. <em>PLoS
ONE</em>, 18(3), e0282855. <a
href="https://doi.org/10.1371/journal.pone.0282855">doi:10.1371/journal.pone.0282855</a>
</li>
<li id="ref-43" value="43">Dehaene, S., Kerszberg, M., & Changeux, J. P. (1998). A neuronal model of a global
workspace in effortful cognitive tasks. <em>Proceedings of the National Academy of
Sciences</em>, 95(24), 14529-14534. <a
href="https://doi.org/10.1073/pnas.95.24.14529">doi:10.1073/pnas.95.24.14529</a></li>
<li id="ref-44" value="44">Tononi, G. (2015). Integrated information theory. <em>Scholarpedia</em>, 10(1),
4164. <a
href="http://www.scholarpedia.org/article/Integrated_information_theory">doi:10.4249/scholarpedia.4164</a>
(Note: IITの内因的実在(Intrinsic Existence)の公理に関する議論については、この総説および[17]を参照)</li>
<li id="ref-45" value="45">Friston, K. (2017). Active inference: a process theory. <em>Neural Computation</em>, 29(1), 1–49. <a
href="https://doi.org/10.1162/NECO_a_00912">doi:10.1162/NECO_a_00912</a></li>
<li id="ref-46" value="46">Parr, T., & Friston, K. J. (2019). Generalised free energy and active inference.
<em>Biological cybernetics</em>, 113(4), 495-513. <a
href="https://doi.org/10.1007/s00422-019-00803-8">doi:10.1007/s00422-019-00803-8</a>
</li>
<li id="ref-47" value="47">Casali, A. G., Gosseries, O., Rosanova, M., Boly, M., Sarasso, S., Casali, K. R.,
... & Massimini, M. (2013). A theoretically based index of consciousness independent of sensory
processing and
behavior. <em>Science Translational Medicine</em>, 5(198), 198ra105. <a
href="https://doi.org/10.1126/scitranslmed.3006294">doi:10.1126/scitranslmed.3006294</a>
</li>
<li id="ref-48" value="48">Tsuchiya, N., et al. (2015). No-Report Paradigms: Extracting the True Neural Correlates of
Consciousness. <em>Trends in Cognitive Sciences</em>, 19(12), 757–770. <a
href="https://doi.org/10.1016/j.tics.2015.10.002">doi:10.1016/j.tics.2015.10.002</a></li>
<li id="ref-49" value="49">Massimini, M., et al. (2005). Breakdown of cortical effective connectivity during sleep.
<em>Science</em>, 309(5744), 2228–2232. <a href="https://doi.org/10.1126/science.1117256">doi:10.1126/science.1117256</a>
(Open Access: <a href="https://air.unimi.it/handle/2434/15471">air.unimi.it</a>)</li>
<li id="ref-50" value="50">Schartner, M., et al. (2015). Complexity of multi-dimensional spontaneous EEG decreases during
propofol induced general anaesthesia. <em>PLOS ONE</em>, 10(8). <a
href="https://doi.org/10.1371/journal.pone.0133532">doi:10.1371/journal.pone.0133532</a>
(Open Access: <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4529106/">PMCID: PMC4529106</a>)</li>
<li id="ref-51" value="51">Comolatti, R., et al. (2019). A fast and general method to empirically estimate the complexity of
brain responses to transcranial and intracranial stimulations. <em>Brain Stimulation</em>, 12(5),
1280–1289. <a href="https://doi.org/10.1016/j.brs.2019.05.013">doi:10.1016/j.brs.2019.05.013</a></li>
<li id="ref-52" value="52">Maschke, C., et al. (2024). Critical dynamics in spontaneous EEG predict anesthetic-induced loss of
consciousness and perturbational complexity. <em>Communications Biology</em>, 7(1). <a
href="https://doi.org/10.1038/s42003-024-06613-8">doi:10.1038/s42003-024-06613-8</a></li>
<li id="ref-53" value="53">Anusha, A. S., et al. (2021). Brain Functional Connectivity as Biomarker for Propofol-Induced
Alterations of Consciousness. <em>Proceedings of the Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC)</em>, 1928–1931. <a
href="https://doi.org/10.1109/EMBC46164.2021.9629617">doi:10.1109/EMBC46164.2021.9629617</a></li>
<li id="ref-54" value="54">Ferrante, O., et al. (2025). Adversarial testing of global neuronal workspace and integrated
information theories of consciousness. <em>Nature</em>, 642(8066), 133–142. <a
href="https://doi.org/10.1038/s41586-025-08888-1">doi:10.1038/s41586-025-08888-1</a></li>
<li id="ref-55" value="55">Sinitsyn, D. O., et al. (2020). Detecting the potential for consciousness in unresponsive patients
using the perturbational complexity index. <em>Brain Sciences</em>, 10(12), 917. <a
href="https://doi.org/10.3390/brainsci10120917">doi:10.3390/brainsci10120917</a></li>
<li id="ref-56" value="56">Shew, W. L., & Plenz, D. (2013). The functional benefits of criticality in the cortex.
<em>The Neuroscientist</em>, 19(1), 88–100. <a
href="https://doi.org/10.1177/1073858412445487">doi:10.1177/1073858412445487</a></li>
<li id="ref-57" value="57">Azevedo, F. A., Carvalho, L. R., Grinberg, L. T., Farfel, J. M., Ferretti, R. E.,
Leite, R. E., ... & Herculano-Houzel, S. (2009). Equal numbers of neuronal and nonneuronal cells
make the human brain an isometrically scaled-up primate brain. <em>Journal of Comparative
Neurology</em>, 513(5), 532-541. <a
href="https://doi.org/10.1002/cne.21974">doi:10.1002/cne.21974</a></li>
<li id="ref-58" value="58">Weber, C. (2025). The multiplicity objection against uploading optimism.
<em>Synthese</em>, 205(6). <a href="https://doi.org/10.1007/s11229-025-05057-9">doi:10.1007/s11229-025-05057-9</a></li>
<li id="ref-59" value="59">Clowes, R. W. (2021). Slow Continuous Mind Uploading. <em>Studies in Brain and Mind</em>, 18,
161–183. <a href="https://doi.org/10.1007/978-3-030-72644-7_8">doi:10.1007/978-3-030-72644-7_8</a></li>
<li id="ref-60" value="60">Vaswani, A., et al. (2017). Attention Is All You Need. <em>Advances in Neural
Information Processing Systems (NeurIPS)</em>. <a
href="https://arxiv.org/abs/1706.03762">arXiv:1706.03762</a></li>
<li id="ref-61" value="61">Ouyang, L., et al. (2022). Training language models to follow instructions with
human feedback. <em>arXiv:2203.02155</em>. <a href="https://arxiv.org/abs/2203.02155">arXiv</a>
</li>
<li id="ref-62" value="62">Rafailov, R., et al. (2023). Direct Preference Optimization: Your Language Model is
Secretly a Reward Model. <em>arXiv:2305.18290</em>. <a
href="https://arxiv.org/abs/2305.18290">arXiv</a></li>
<li id="ref-63" value="63">Dettmers, T., et al. (2023). QLoRA: Efficient Finetuning of Quantized LLMs.
<em>arXiv:2305.14314</em>. <a href="https://arxiv.org/abs/2305.14314">arXiv</a></li>
<li id="ref-64" value="64">Lewis, P., et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP
Tasks. <em>arXiv:2005.11401</em>. <a href="https://arxiv.org/abs/2005.11401">arXiv</a></li>
<li id="ref-65" value="65">Yao, S., et al. (2022). ReAct: Synergizing Reasoning and Acting in Language Models.
<em>arXiv:2210.03629</em>. <a href="https://arxiv.org/abs/2210.03629">arXiv</a></li>
<li id="ref-66" value="66">Schick, T., et al. (2023). Toolformer: Language Models Can Teach Themselves to Use
Tools. <em>arXiv:2302.04761</em>. <a href="https://arxiv.org/abs/2302.04761">arXiv</a></li>
<li id="ref-67" value="67">Manakul, P., et al. (2023). SelfCheckGPT: Zero-Resource Black-Box Hallucination
Detection for Generative Large Language Models. <em>arXiv:2303.08896</em>. <a
href="https://arxiv.org/abs/2303.08896">arXiv</a></li>
<li id="ref-70" value="70">Friston, K. J., et al. (2017). Active inference, mathematical constitution, and pure consciousness. <em>Frontiers in Psychology</em>, 8, 1322.</li>
<li id="ref-71" value="71">Zanichelli, N., et al. (2025). State of Brain Emulation Report 2025. <em>arXiv:2510.15745</em>.</li>
<li id="ref-73" value="73">Koulouri, A. (2025). Bayesian model parameter learning in linear inverse problems. <em>Machine Learning: Science and Technology</em>.</li>
<li id="ref-74" value="74">Nzakuna, P. S., et al. (2025). Monte Carlo-based Strategy for Assessing the Impact of EEG Data Uncertainty. <em>IEEE Transactions on Instrumentation and Measurement</em>.</li>
<li id="ref-76" value="76">Laukkonen, R., Friston, K., & Chandaria, S. (2025). A beautiful loop: An active inference theory of consciousness. <em>Neuroscience & Biobehavioral Reviews</em>.</li>
<li id="ref-77" value="77">Clark, A. (2013). The Mark of the Mental: In Search of the Markov Blanket. In: <em>The Mark of the Mental</em>. Oxford University Press.</li>
<li id="ref-78" value="78">Feng, Z., et al. (2025). Block-Champagne: A Novel Bayesian Framework for Accurate EEG Source Imaging with Uncertainty Quantification. <em>NeuroImage</em>.</li>
<li id="ref-79" value="79">Medani, T., et al. (2025). Forward and inverse solvers in multi-modal neuroimaging: Accounting for tissue conductivity uncertainties. <em>Frontiers in Human Neuroscience</em>.</li>
<li id="ref-80" value="80">Hohwy, J., et al. (2025). On the Minimal Theory of Consciousness Implicit in Active Inference. <em>Journal of Mathematical Psychology</em>.</li>
<li id="ref-81" value="81">Li, J., et al. (2025). Computational complexity reduction in Integrated Information Theory via low-dimensional embedding. <em>Chaos, Solitons & Fractals</em>.</li>
<li id="ref-82" value="82">Cai, C., et al. (2021). Robust estimation of noise for electromagnetic brain imaging with the Champagne algorithm. <em>NeuroImage</em>.</li>
<li id="ref-83" value="83">Pernet, C. R., Appelhoff, S., Gorgolewski, K. J., et al. (2019). EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. <em>Scientific Data</em>, 6, 103. <a href="https://doi.org/10.1038/s41597-019-0104-8">doi:10.1038/s41597-019-0104-8</a></li>
<li id="ref-84" value="84">Kothe, C., Shirazi, S. Y., Stenner, T., et al. (2025). The lab streaming layer for synchronized multimodal recording. <em>Imaging Neuroscience</em>, 3, IMAG.a.136. <a href="https://doi.org/10.1162/IMAG.a.136">doi:10.1162/IMAG.a.136</a></li>
<li id="ref-85" value="85">Chang, C.-Y., Hsu, S.-H., Pion-Tonachini, L., & Jung, T.-P. (2018). Evaluation of Artifact Subspace Reconstruction for automatic EEG artifact removal. <em>Proc. IEEE EMBC</em>. <a href="https://doi.org/10.1109/EMBC.2018.8512547">doi:10.1109/EMBC.2018.8512547</a></li>
<li id="ref-86" value="86">de Cheveigne, A. (2020). ZapLine: A simple and effective method to remove power line artifacts. <em>NeuroImage</em>, 207, 116356. <a href="https://doi.org/10.1016/j.neuroimage.2019.116356">doi:10.1016/j.neuroimage.2019.116356</a></li>
<li id="ref-87" value="87">Vinck, M., Oostenveld, R., van Wingerden, M., Battaglia, F., & Pennartz, C. M. A. (2011). An improved index of phase-synchronization for electrophysiological data in the presence of volume-conduction, noise and sample-size bias. <em>NeuroImage</em>, 55(4), 1548–1565. <a href="https://doi.org/10.1016/j.neuroimage.2011.01.055">doi:10.1016/j.neuroimage.2011.01.055</a></li>
<li id="ref-88" value="88">Staniek, M., & Lehnertz, K. (2008). Symbolic Transfer Entropy. <em>Physical Review Letters</em>, 100, 158101. <a href="https://doi.org/10.1103/PhysRevLett.100.158101">doi:10.1103/PhysRevLett.100.158101</a></li>
<li id="ref-89" value="89">Boto, E., Holmes, N., Leggett, J., et al. (2018). Moving magnetoencephalography towards real-world applications with a wearable system. <em>Nature</em>, 555, 657–661. <a href="https://doi.org/10.1038/nature26147">doi:10.1038/nature26147</a></li>
<li id="ref-90" value="90">Casali, A. G., Gosseries, O., Rosanova, M., et al. (2013). A theoretically based index of consciousness independent of sensory processing and behavior. <em>Science Translational Medicine</em>, 5(198), 198ra105. <a href="https://doi.org/10.1126/scitranslmed.3006294">doi:10.1126/scitranslmed.3006294</a></li>
<li id="ref-91" value="91">Correa, J. D., Lee, S., & Bareinboim, E. (2021). Nested Counterfactual Identification from Arbitrary Surrogate Experiments. <em>arXiv:2107.03190</em>. <a href="https://arxiv.org/abs/2107.03190">arXiv</a></li>
<li id="ref-92" value="92">Seifert, U. (2012). Stochastic thermodynamics, fluctuation theorems and molecular machines. <em>Reports on Progress in Physics</em>, 75(12), 126001. <a href="https://doi.org/10.1088/0034-4885/75/12/126001">doi:10.1088/0034-4885/75/12/126001</a></li>
<li id="ref-93" value="93">Kitazono, J., Kanai, R., & Oizumi, M. (2018). Efficient Algorithms for Searching the Minimum Information Partition in Integrated Information Theory. <em>Entropy</em>, 20(3), 173. <a href="https://doi.org/10.3390/e20030173">doi:10.3390/e20030173</a></li>
<li id="ref-94" value="94">Dorkenwald, S., et al. (2024). Neuronal wiring diagram of an adult brain. <em>Nature</em>, 634, 124–138. <a href="https://doi.org/10.1038/s41586-024-07558-y">doi:10.1038/s41586-024-07558-y</a></li>
<li id="ref-95" value="95">Chalmers, D. J. (1995). Facing up to the problem of consciousness. <em>Journal of Consciousness Studies</em>, 2(3), 200-219.</li>
</ol>
</section>

</article>

<!-- Sidebar -->
<aside class="sidebar-column">

<div class="sidebar-box">
<h4>Start Here</h4>
<ul>
<li><a href="verification.html">検証基盤（Verification Commons）→</a></li>
<li><a href="casework.html">ケースワーク（歴史の型）→</a></li>
<li><a href="tech_roadmap.html#definition">前進の定義（Roadmap）→</a></li>
<li><a href="idea.html">理論フレーム（Framework）→</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Contents</h4>
<ul>
<li><a href="#introduction">Introduction</a></li>
<li><a href="#technical-framework">Technical Framework</a></li>
<li><a href="#decoding-to-emulation-gap">Decoding → Emulation</a></li>
<li><a href="#reproducibility">Reproducibility</a></li>
<li><a href="#key-technical-challenges">Key Technical Challenges</a></li>
<li><a href="#research-program">Research Program</a></li>
<li><a href="#llm-research-update">LLM Research Update</a></li>
<li><a href="#eeg-consciousness-roadmap">EEG Consciousness Roadmap</a></li>
<li><a href="#technical-proposals">Technical Proposals</a></li>
<li><a href="#about">About</a></li>
<li><a href="#references">References</a></li>
</ul>
</div>

<div class="key-points">
<h4>Highlights</h4>
<ul>
<li>IIT/GNWTなどの理論対立を実装要件に落とす</li>
<li>ESI逆問題の克服策（IHM・不確実性定量化）を明記</li>
<li>DCM/能動的推論でデコーディング→生成モデルへ拡張</li>
<li>EEG複雑性×摂動応答×臨界性で行動非依存の意識指標をロードマップ化</li>
</ul>
</div>

<div class="sidebar-box">
<h4>Study Overview</h4>
<p><strong>Objective:</strong> マルチモーダル計測と神経解読を統合した「本人性維持」評価系の設計</p>
<p style="margin-top:8px;"><strong>Design:</strong> 課題ベース＋安静時の縦断収集、侵襲/非侵襲データの比較</p>
</div>

<div class="sidebar-box">
<h4>Focus Areas</h4>
<ul>
<li>脳活動の計測（HD-EEG, ESI, fMRI）</li>
<li>計算論的神経科学（DCM, Transformer）</li>
<li>意識の理論（IIT, 心理的連続性）</li>
</ul>
</div>

<div class="sidebar-box">
<h4>Technical Proposals</h4>
<ul>
<li><a href="technical_proposal_46.html">Issue #46: Measurement QA & BIDS</a></li>
<li><a href="technical_proposal_47.html">Issue #47: Strategic Extension</a></li>
<li><a href="technical_proposal_48.html">Issue #48: Neuroengineering & IIT</a></li>
<li><a href="technical_proposal_56.html">Issue #56: Identifiability & Intervention</a></li>
<li><a href="technical_proposal_58.html">Issue #58: Irreversibility & IIT Scaling</a></li>
<li><a href="technical_proposal_61.html">Issue #61: Causal & Thermodynamic Critique</a></li>
<li><a href="technical_proposal_62.html">Issue #62: Thermodynamic/Causal Validity</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Roadmaps</h4>
<ul>
<li><a href="tech_roadmap.html">技術ロードマップ（学習）→</a></li>
<li><a href="#eeg-consciousness-roadmap">Consciousness Metrics (EEG) →</a>
<ul style="padding-left: 15px; margin-top: 4px; list-style-type: '— ';">
<li>行動非依存の意識指標（PCI/PCI-ST）<sup><a href="#ref-47">[47]</a></sup></li>
<li>no-report設計でreport confoundを分離<sup><a href="#ref-48">[48]</a></sup></li>
<li>安静時の複雑性・臨界性指標の整備<sup><a href="#ref-50">[50]</a></sup><sup><a href="#ref-52">[52]</a></sup></li>
<li>臨床（鎮静/麻酔/重症）への一般化を重視<sup><a href="#ref-55">[55]</a></sup></li>
</ul>
</li>
</ul>
</div>

<div class="sidebar-box">
<h4>Data Standards</h4>
<ul>
<li>BIDS/EEG-BIDS標準への準拠<sup><a href="#ref-25">[25]</a></sup><sup><a href="#ref-26">[26]</a></sup>（<strong>課題:</strong> メタデータ拡充が急務）</li>
<li>データ構造とスキーマ例の公開</li>
<li>多施設間相互運用性の確保</li>
</ul>
</div>

<div class="sidebar-box">
<h4>Resources</h4>
<ul>
<li><a href="brain_science_dictionary.html">脳科学辞典 (Brain Science Dictionary) →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Research Notes</h4>
<ul>
<li><a href="idea.html">理論的枠組み（Idea）</a></li>
<li><a href="issue.html">貢献ガイド（Research Community）</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Paper Collection</h4>
<p>過去10年間の「Mind Uploading」に関する学術論文を収集・翻訳した資料を公開しています。</p>
<a href="mind_uploading_papers.html"
style="display: inline-block; margin-top: 10px; font-weight: bold; color: var(--color-accent);">論文集を見る
(HTML) →</a>
</div>

<div class="cta-box">
<h4>Contribute</h4>
<p>このプロジェクトに参加しませんか？</p>
<a href="https://github.com/yasufumi-nakata/mind-upload/issues" target="_blank">Issue を立てる</a>
</div>

</aside>
</main>
