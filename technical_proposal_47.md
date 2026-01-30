---
layout: default
title: "戦略的技術拡張提案書：2025-2026年の神経科学研究における計算論的枠組みと標準化"
description: "BIDS標準化、次世代信号処理(ASR/ZapLine)、ネットワーク神経科学(wPLI/STE)、LSL同期に関する技術的拡張提案"
article_type: "Technical Proposal"
subtitle: "Issue #47: eegflow.jp 戦略的技術拡張提案書"
author: "eegflow Project Contributor"
last_updated: "2026-01-25"
note: "Proposal (Accepted)"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Abstract</h2>
<p>
本報告書は、eegflow.jp における技術的拡張提案を行うものである。
2025-2026年の神経科学研究におけるパラダイムシフトを踏まえ、BIDSによるデータ構造の標準化、ASRやZapLineを用いた次世代信号前処理、ネットワーク神経科学（wPLI, STE）、およびLab Streaming Layer (LSL) によるマルチモーダル同期の実装を推奨する。
これにより、eegflow.jp を単なる情報サイトから、世界標準の研究を行うための技術的インフラへと進化させることを目的とする。
</p>
</div>

<section class="section" id="introduction">
<h2 class="section-title">1. 序論：神経科学研究のパラダイムシフト</h2>
<h3>1.1 背景：2025年の脳波研究における技術的転換点</h3>
<p>
2025年から2026年にかけての神経科学、とりわけ非侵襲的脳機能計測（EEG/MEG）の分野は、過去数十年に類を見ない技術的変革の只中にある。かつては実験室内の制御された環境下で、事象関連電位（ERP）のピーク振幅や潜時を単変量的に解析することが主流であったが、現在ではその様相は劇的に変化している。研究の焦点は、静的な「活動の強さ」から、脳領域間の動的な「情報の流れ（コネクティビティ）」へと移行し、解析手法は線形信号処理から深層学習（Deep Learning）やリーマン幾何学を用いた非線形・多変量解析へと高度化している。
</p>
<p>
加えて、計測環境自体も実験室を飛び出し、VR（仮想現実）空間や実社会環境（Real-world settings）での計測、いわゆるMobile Brain/Body Imaging（MoBI）が一般化しつつある。このような環境下では、従来のノイズ除去手法は通用せず、また、視線追跡装置やモーションキャプチャシステムといった異種デバイスとの厳密な時間同期が必須となる。
</p>

<h3>1.2 本報告書の目的と提案の範囲</h3>
<p>
本報告書は、eegflow.jpという既存の脳波研究情報プラットフォームに対し、現役の研究者の視点から、そのコンテンツ価値を飛躍的に高めるための技術的提案を行うものである。現状のウェブサイトが提供する基礎的な情報に加え、最先端の研究現場で真に求められている「計算論的詳細」「標準化プロトコル」「数理的背景」を補完することを目的とする。
</p>

<h3>1.3 理論的枠組み：Active InferenceとIITの統合における課題</h3>
<p>
eegflow.jpが提唱する「意識のアップロード」の理論的基盤において、Laukkonen et al. (2025) の「反事実的等価性（Counterfactual Equivalence）」をアイデンティティの証明として用いる点には、IIT 4.0（統合情報理論）の観点から論理的な飛躍が指摘されている。
</p>
<ul>
<li><strong>課題:</strong> 生成モデルの分岐構造が一致するだけでは、現象的意識の必要条件である「因果構造（Causal Structure）」の保存、すなわちIITにおける「内在的存在（Intrinsic Existence）」が保証されない。</li>
<li><strong>解決策の提案:</strong> アイデンティティの検証指標として、単なる入出力の等価性ではなく、<strong>Effective Information (EI)</strong> などの因果的指標を導入し、物理的なMarkov Blanketにおけるレイテンシ（<10ms）や帯域幅の制約を厳密に定義することを提案する。</li>
</ul>

<div class="key-points">
<h4>提案の5つの柱</h4>
<ul>
<li><strong>データ標準化とBIDSエコシステム：</strong>再現性危機の克服とデータ共有義務化への対応。</li>
<li><strong>次世代信号前処理技術：</strong>ASR、ZapLine、および深層学習ベースのデノイジング。</li>
<li><strong>ネットワーク神経科学と接続性解析：</strong>体積伝導問題を克服するwPLIや因果性推定（STE）。</li>
<li><strong>マルチモーダル同期とLSL：</strong>VR・生体計測統合のための時間管理プロトコル。</li>
<li><strong>ソフトウェア・ハードウェアの最新動向：</strong>MNE-Python、EEGLAB、および国内機器（ミユキ技研等）の統合。</li>
</ul>
</div>
<p class="small">
なお、本提案は純粋に科学技術的な観点に基づき、倫理審査（IRB）や個人情報保護法、臨床診断における法的責任といった法的・倫理的側面については議論の対象外とする。
</p>
</section>

<section class="section" id="bids">
<h2 class="section-title">2. データ構造の標準化：Brain Imaging Data Structure (BIDS)</h2>
<p>
研究データの管理において、従来の「独自フォーマットと自由なフォルダ構成」は、もはや許容されない時代となりつつある。主要な学術ジャーナル（Nature Neuroscience, Scientific Data等）や公的リポジトリ（OpenNeuro）は、データのFAIR原則（Findable, Accessible, Interoperable, Reusable）への準拠を求めており、その事実上の世界標準が Brain Imaging Data Structure (BIDS) である。
</p>

<h3>2.1 BIDS階層構造と命名規則の厳格化</h3>
<p>
BIDSはファイルフォーマットではなく、データセットを構成するフォルダ階層とファイル命名の規格である。従来の <code>Subject1_Resting.edf</code> といった恣意的な命名は、自動化された解析パイプライン（BIDS Apps）の適用を阻害する。
</p>

<h4>2.1.1 推奨ディレクトリ構造</h4>
<div class="code-block">
<pre><code>dataset_root/
  dataset_description.json
  participants.tsv
  sub-01/
    ses-01/
      eeg/
        sub-01_ses-01_task-rest_eeg.eeg
        sub-01_ses-01_task-rest_eeg.vhdr
        sub-01_ses-01_task-rest_eeg.vmrk
        sub-01_ses-01_task-rest_eeg.json  &lt;-- サイドカーJSON（必須）
        sub-01_ses-01_task-rest_channels.tsv
      anat/ (MRIがある場合)</code></pre>
</div>
<p>
この構造において重要なのは、被験者（<code>sub-</code>）、セッション（<code>ses-</code>）、タスク（<code>task-</code>）といったキーバリューペアがファイル名に埋め込まれている点である。これにより、スクリプトはファイル名のみから実験条件を完全に特定可能となる。
</p>

<h3>2.2 サイドカーJSONによるメタデータ管理と完全性</h3>
<p>
脳波データ（バイナリ）には含まれないが、解析に不可欠な情報を記述する「サイドカーJSONファイル（*_eeg.json）」の重要性を強調すべきである。特に Pernet et al. (2019) の提唱する EEG-BIDS 規格への完全準拠を目指し、以下のフィールドを必須化する。
</p>
<ul>
<li><strong>EEGReference:</strong> 参照電極の配置。例えば「Cz」なのか、「Common Mode Sense (CMS) / Driven Right Leg (DRL)」なのかを明記する。</li>
<li><strong>PowerLineFrequency:</strong> 50Hz（東日本）か60Hz（西日本）かを明記。</li>
<li><strong>SoftwareFilters:</strong> 収録時に適用されたフィルタ情報。</li>
<li><strong>Hardware Specifications:</strong> 再現性の観点から、アンプのビット深度（例：24 bit）や入力インピーダンスの範囲を明記することが望ましい。</li>
</ul>

<h3>2.3 チャンネル記述ファイル（channels.tsv）とインピーダンス</h3>
<p>
バイナリデータ内のチャンネルラベルだけでは不十分なケースが多い。<code>*_channels.tsv</code> ファイルでは、各チャンネルの「種類（type）」と「単位（units）」に加え、<strong>電極インピーダンス（impedance）</strong> の記録を推奨する。
</p>
<table class="data-table">
<thead>
<tr><th>name</th><th>type</th><th>units</th><th>impedance</th><th>description</th></tr>
</thead>
<tbody>
<tr><td>Fp1</td><td>EEG</td><td>microV</td><td>5 kOhm</td><td>Frontal Pole 1</td></tr>
<tr><td>EOGv</td><td>EOG</td><td>microV</td><td>n/a</td><td>Vertical Electrooculogram</td></tr>
</tbody>
</table>
<p>
この定義ファイルが存在することで、解析ソフトは適切な処理が可能となり、またインピーダンスの時系列変化（もし記録されていれば）はデータの品質評価に直結する。
</p>
</section>

<section class="section" id="preprocessing">
<h2 class="section-title">3. 次世代信号前処理技術：アーチファクト除去の数理</h2>
<p>
従来の「目視による棄却」や「単純なバンドパスフィルタ」は、高密度記録や長時間記録においては現実的ではない。2025年の標準となりつつある、信号の統計的性質を利用した適応的アルゴリズムの詳細な解説が必要である。
</p>

<h3>3.1 Artifact Subspace Reconstruction (ASR) の数理的解剖</h3>
<p>
Artifact Subspace Reconstruction (ASR) は、BIDS-PipelineやEEGLABのデフォルト前処理として採用が進んでいるが、その内部動作はブラックボックス化されがちである。研究者がパラメータ（特にcutoff parameter）を適切に設定できるよう、そのアルゴリズムの核心を解説する必要がある。
</p>

<h4>3.1.1 アルゴリズムのメカニズム</h4>
<p>
ASRは、主成分分析（PCA）を用いて、データ内の高分散成分（アーチファクト）を特定し、その成分のみを除去して信号を再構成する手法である。
</p>
<ol>
<li><strong>キャリブレーション（Calibration）:</strong> まず、データセットの中から「クリーンな」区間を自動探索し、その区間の共分散行列 $C$ を計算する。ここから信号の空間的な混合行列（Mixing Matrix） $M$ を推定する。</li>
<li><strong>スライディングウィンドウ処理:</strong> データを短いウィンドウ（例：0.5秒）に分割し、各ウィンドウでPCAを実行する。</li>
<li><strong>部分空間の再構成:</strong> あるウィンドウの主成分の分散が、キャリブレーションデータの分散と比較して閾値（Cutoff parameter $k$、通常 $k=20$）を超えている場合、その成分はアーチファクトとみなされる。</li>
<li><strong>射影と復元:</strong> アーチファクト成分を除外し、残ったクリーンな成分（$S_{clean}$）と混合行列 $M$ を用いて、元のセンサー空間に信号を逆射影する。
<p>ここで $X_{recon} = M 	ilde{S}_{clean}$ はムーア・ペンローズの擬似逆行列を表す。※数式表現は簡略化</p>
</li>
</ol>

<h4>3.1.2 運用上の注意点とデータ駆動型閾値設定</h4>
<p>
従来のASR運用（例：固定カットオフ $k=20$）は、科学的に不十分であるとの指摘がある（Anders et al., 2020）。固定閾値は、個人差や課題によるノイズプロファイルの違いを無視し、特に高周波帯域（ガンマ波）の神経信号を過剰に除去するリスクがある。
</p>
<p>
したがって、eegflow.jpでは以下の改善策を提案する。
</p>
<ul>
<li><strong>データ駆動型閾値設定:</strong> 固定値ではなく、<strong>リーマン幾何学（Riemannian Geometry）</strong> を用いたアプローチ（例：Riemannian Potato）により、個々のデータの統計的分布に基づいて外れ値を検出・補間する手法を採用すべきである。</li>
<li><strong>キャリブレーションデータの選定:</strong> ASRの性能は参照データの質に依存するため、安静時閉眼データなどの安定した区間を明示的に指定することを推奨する。</li>
</ul>

<h3>3.2 スペクトル-空間フィルタリング：ZapLine-plus</h3>
<p>
電源ノイズ（ハムノイズ）の除去には、従来ノッチフィルタが用いられてきたが、これは特定の周波数帯域の信号成分を完全に削除してしまうため、ガンマ帯域の研究においては致命的となる場合がある。これに対し、ZapLine およびその改良版である ZapLine-plus は、ノイズの空間分布（トポグラフィ）を利用して、信号成分を温存しつつノイズのみを分離する。
</p>

<h4>3.2.1 ZapLineの基本原理</h4>
<p>
ZapLineは、データを「ノイズ周波数成分」と「それ以外」にフィルタバンクで分離し、ノイズ周波数成分に対してのみ空間フィルタ（DSS: Denoising Source Separation）を適用する。これにより、電源ノイズと空間的に相関のない脳波成分は保持される。
</p>

<h4>3.2.2 ZapLine-plusによる適応的処理</h4>
<p>
2025年の研究トレンドにおいては、モバイル計測の増加に伴い、センサーの位置ズレや環境変化によって電源ノイズの空間分布や正確な周波数が時間的に変動することが課題となっている。ZapLine-plusは以下の機能でこれを解決する。
</p>
<ul>
<li><strong>適応的チャンキング:</strong> ノイズの空間分布が安定している区間（チャンク）ごとにデータを分割処理する。</li>
<li><strong>周波数追従:</strong> 50Hzぴったりではなく、49.9Hz〜50.1Hzのように変動するノイズピークをチャンクごとに検出する。</li>
<li><strong>成分数の自動決定:</strong> 除去すべき空間成分の数を、外れ値検出アルゴリズムを用いて自動決定する。</li>
</ul>

<h3>3.3 深層学習に基づくデノイジング</h3>
<p>
最新のトレンドとして、NERV (Neural EEG Reconstruction for Various artifacts) などの深層学習モデルの導入が進んでいる。これらは、大量のEEGデータセット（TUH EEG Corpus等）で事前学習されたモデルを用い、EOGやEMGを分離する。
特筆すべきは、生成モデルの品質評価指標としての <strong>CAT (Class-Aware Time-domain) score</strong> の導入である。従来のSNR（信号対雑音比）だけでは、生成された信号が「もっともらしいが偽の脳波」であるかを見抜けないため、下流タスク（分類精度など）への影響を評価する新たな指標が必要とされている。
</p>
</section>

<section class="section" id="connectivity">
<h2 class="section-title">4. ネットワーク神経科学：コネクティビティ解析の落とし穴と解決策</h2>
<p>
脳波解析の関心は、局所的な活動から脳領域間のネットワークへと移行している。しかし、頭皮上脳波におけるコネクティビティ解析には「体積伝導（Volume Conduction）」という物理的な制約がつきまとう。eegflow.jpでは、この問題を回避するための堅牢な指標を推奨する必要がある。
</p>

<h3>4.1 位相同期の堅牢性：Weighted Phase Lag Index (wPLI)</h3>
<p>
従来のコヒーレンス（Coherence）やPhase Locking Value (PLV)は、体積伝導の影響（ゼロ位相ラグの相関）を強く受けるため、頭皮上EEGでの使用は推奨されない。これに対し、<strong>Weighted Phase Lag Index (wPLI)</strong> が現在のゴールドスタンダードとなっている。
</p>

<h4>4.1.1 wPLIの定義と優位性</h4>
<p>
PLIは位相差の符号のみを利用するが、wPLIはクロススペクトルの虚部の大きさで重み付けを行う。
</p>
<ul>
<li><strong>ゼロ位相ラグの抑制:</strong> 体積伝導由来の信号は、瞬時に複数の電極に伝わるため、位相差が0（または $\pi$）になり、クロススペクトルは実軸上に分布する。wPLIは虚部（$\Im$）で重み付けするため、実軸付近のノイズ成分の寄与を極小化できる。</li>
<li><strong>ノイズ耐性:</strong> 振幅の小さい成分（ノイズである可能性が高い）の影響を低減できるため、従来のPLIよりも統計的検出力が高い。</li>
</ul>

<h3>4.2 因果性の推定：Symbolic Transfer Entropy (STE)</h3>
<p>
wPLIは無向グラフ（AとBがつながっている）しか評価できないが、情報の「流れ」や「因果性」（AがBを駆動している）を知るためには、Transfer Entropy (TE) が用いられる。特にEEGのような非定常・非線形信号に対しては、<strong>Symbolic Transfer Entropy (STE)</strong> が有効である。
</p>

<h4>4.2.1 記号化によるロバスト性の確保</h4>
<p>
STEでは、連続的な電圧値をそのまま使うのではなく、順列パターン（Permutation patterns）などのシンボル列に変換する。
</p>
<ul>
<li><strong>Embedding Dimension ($m$):</strong> 埋め込み次元。従来の $m=3$ では複雑な脳波ダイナミクスを捉えきれないことが示されており、近年の研究では $m=5 \sim 7$ への最適化が推奨されている。</li>
<li><strong>Delay Time ($	au$):</strong> 遅れ時間。信号の自己相関が最初に低下する点などを基準に設定する。</li>
</ul>
<p>
STEを用いることで、例えば「前頭葉から後頭葉へのトップダウン信号」と「視覚野からのボトムアップ信号」を区別して定量化することが可能となる。
</p>
</section>

<section class="section" id="source-localization">
<h2 class="section-title">5. ソースローカリゼーション（脳源推定）の最前線</h2>
<p>
頭皮上の電位分布から脳内電源を推定する「逆問題」は、数学的に不良設定問題であるが、制約条件の工夫により推定精度は向上している。古典的なLORETA法に加え、以下の最新手法を紹介すべきである。
</p>

<h3>5.1 スパース性と深層学習の導入</h3>
<ul>
<li><strong>スパース制約:</strong> 脳活動は空間的に局在している（focal）ことが多いという仮定に基づき、L1ノルム正則化などを導入して、ボケの少ない解を得る手法。DESIRE study などの最新研究では、ノイズレベルに応じて正則化パラメータを自動調整する手法が提案されており、てんかん焦点の同定などでLORETAを上回る精度を示している。</li>
<li><strong>Deep Learning Beamformer:</strong> ALCMV (Accelerated Linear Constrained Minimum Variance) や AORI といったアルゴリズムは、共分散行列の計算を再帰的に行い、次元削減を組み合わせることで、計算コストを大幅に削減（約66%減）している。これにより、BCIなどのリアルタイムアプリケーションでも高精度な線源推定が可能になりつつある。</li>
</ul>

<h3>5.2 比較：LORETA vs BrainLoc</h3>
<p>
国内でも利用者の多い BrainLoc について、LORETAとの比較視点を提供することは有益である。
</p>
<ul>
<li><strong>LORETA:</strong> 分布定数モデル。脳全体に滑らかに広がる活動の推定に適する。機能的結合の解析によく用いられる。</li>
<li><strong>BrainLoc:</strong> 双極子（Dipole）モデルに基づくアプローチも含み、特にMRI/CT画像との統合による解剖学的な位置特定（てんかん原性域や腫瘍位置との関係など）に強みを持つ。移動双極子モデルにより、時間的に移動する信号源を追跡可能。</li>
</ul>
</section>

<section class="section" id="multimodal">
<h2 class="section-title">6. マルチモーダル統合と同期計測：Lab Streaming Layer (LSL)</h2>
<p>
VR、アイトラッキング、モーションキャプチャを組み合わせた実験系では、各デバイスが独自のクロックで動作するため、データの同期が最大の課題となる。従来のハードウェアトリガー（パラレルポート）に代わり、ネットワークベースの同期プロトコル <strong>Lab Streaming Layer (LSL)</strong> の理解が必須となる。
</p>

<h3>6.1 LSLの動作原理とクロックドリフト補正</h3>
<p>
LSLは、単にデータをTCP/IPで送るだけでなく、高度なタイムスタンプ管理を行っている。
</p>

<h4>6.1.1 時間同期プロトコル</h4>
<p>
LSLはNetwork Time Protocol (NTP) に似たパケット交換を行い、送信側PCと受信側PCのクロック差（Offset）と往復遅延（RTT）を測定する。
重要なのは、収録中にこのクロック差が一定ではなく、温度変化やCPU負荷により徐々にズレていく（クロックドリフト）点である。
</p>

<h4>6.1.2 ジッター補正と線形回帰</h4>
<p>
LSLのインポーター（load_xdf 等）は、収録されたクロックオフセットの履歴に対して線形回帰（Linear Regression）やロバスト回帰を適用し、ドリフト成分を除去して全サンプルのタイムスタンプを再計算する。この処理により、1時間の記録でもサブミリ秒の同期精度を維持可能となる。
</p>

<h3>6.2 国内ハードウェアとの統合事例：Miyuki Giken</h3>
<p>
日本の研究環境においてシェアの高いミユキ技研の装置（Polymate Pocket等）におけるLSL対応についても触れるべきである。
</p>
<ul>
<li><strong>ハイブリッド同期:</strong> 視覚刺激の提示タイミング（Onset）など、極めて高い時間精度（&lt;1ms）が求められるイベントについては、依然として光センサやパラレルポート経由でのハードウェアトリガーを推奨する。一方で、アイトラッカーの視線座標やVRヘッドセットの回転情報など、連続的なデータストリームについてはLSLを用いて統合する「ハイブリッド構成」が、信頼性と利便性のバランスにおいて最適解となる場合が多い。</li>
</ul>

<h3>6.3 ハイパースキャニング（複数人同時計測）</h3>
<p>
社会神経科学（Social Neuroscience）の興隆に伴い、2名の被験者の脳波を同時記録するハイパースキャニングの需要が増している。
</p>
<ul>
<li><strong>シングルアンプ構成:</strong> 64chアンプを分割し、32chずつ2名に割り当てる方法。クロックが同一であるため同期ズレが原理的に発生しない最大のメリットがある。</li>
<li><strong>音声同期の重要性:</strong> 自然な会話を分析する場合、音声データもLSLストリームとして統合し、発話の開始点（Onset）にトリガーを打つことで、発話に関連した脳電位（Speech-related potentials）を解析可能にする手法が提案されている。</li>
</ul>
</section>

<section class="section" id="software">
<h2 class="section-title">7. ソフトウェアエコシステムの最新動向 (2025-2026)</h2>

<h3>7.1 MNE-Python：深層学習との融合</h3>
<p>Pythonベースの MNE-Python は、現在最も開発が活発である。</p>
<ul>
<li><strong>Deep Learning連携:</strong> PyTorchやTensorFlowとの親和性が高く、前述のNERVや各種デコーディングモデルの実装プラットフォームとして事実上の標準となっている。</li>
<li><strong>最新機能 (v1.11.0):</strong> GEDTransformer（一般化固有値分解のクラス化）による空間フィルタリングの統一、ICAのfit/apply分離、Eyelinkサポート強化など。</li>
</ul>

<h3>7.2 EEGLAB：GUIとモバイル解析の拠点</h3>
<p>MATLABベースの EEGLAB は、依然としてGUI操作を好むユーザーや、既存の資産を持つラボにとって重要である。</p>
<ul>
<li><strong>BeMoBIL Pipeline:</strong> モバイルEEGに特化したプラグイン群。歩行アーチファクト除去やBIDS対応が含まれる。</li>
<li><strong>Automagic:</strong> 前処理の完全自動化ツールボックス。大規模データセットに有効。</li>
</ul>

<h3>7.3 FieldTrip：MEGとOPMへの対応</h3>
<p>FieldTrip は、特にMEG（脳磁図）解析において強力であるが、2025年のアップデートでは Optically Pumped Magnetometers (OPM) への対応が強化されている。</p>

<h3>7.4 商用ソフトウェア：BrainVision Analyzer 2</h3>
<p>BrainVision Analyzer 2 は、「History Tree」機能により解析プロセスの追跡可能性が担保されるため、臨床研究や企業の研究開発において強みを持つ。MATLABとの連携も強化されている。</p>
</section>

<section class="section" id="roadmap">
<h2 class="section-title">8. 結論：eegflow.jpのロードマップへの提言</h2>
<p>以上の技術的精査に基づき、eegflow.jpが今後1〜2年で実装すべきコンテンツのロードマップを以下に提案する。</p>
<ul>
<li><strong>「BIDS導入ガイド」の作成（優先度：高）:</strong> 日本語の実験環境（ミユキ技研、BrainProducts等）からBIDS形式へ変換するためのスクリプト例を提供。</li>
<li><strong>「アーチファクト除去の数理」セクションの新設:</strong> ASRやZapLineのパラメータの意味を数理的に解説する教育的コンテンツ。</li>
<li><strong>「コネクティビティ解析」のベストプラクティス:</strong> 体積伝導の危険性を啓蒙し、wPLIやSTEの使用を推奨。</li>
<li><strong>「LSLによるマルチモーダル同期」の実践チュートリアル:</strong> Unity（VR）とPython（LSL）の連携サンプル。</li>
<li><strong>VR・モバイル脳波（MoBI）特集:</strong> 実環境下でのノイズ対策やVRヘッドセットとの物理的干渉対策。</li>
</ul>
<p>
これらの情報を拡充することで、eegflow.jpは単なる情報サイトから、日本の神経科学研究者が世界標準の研究を行うための「技術的インフラ」へと進化することができるだろう。
</p>
</section>

<section class="section" id="references">
<h2 class="section-title">引用文献</h2>
<ul class="reference-list">
<li><a href="https://www.fieldtriptoolbox.org/example/other/bids/">BIDS - the brain imaging data structure - FieldTrip toolbox</a></li>
<li><a href="https://bids.neuroimaging.io/">The Brain Imaging Data Structure: BIDS</a></li>
<li><a href="https://bids-specification.readthedocs.io/en/stable/derivatives/common-data-types.html">Common data types and metadata - BIDS Specification</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10710985/">Artifact subspace reconstruction: a candidate for a dream solution for EEG studies - PMC</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC9120550/">Zapline‐plus: A Zapline extension for automatic and adaptive removal of frequency‐specific noise artifacts in M/EEG - PMC</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3462418/">Weighted Phase Lag Index and Graph Analysis - PMC</a></li>
<li><a href="https://labstreaminglayer.readthedocs.io/info/time_synchronization.html">Time Synchronization — Labstreaminglayer documentation</a></li>
<li><a href="https://mne.tools/stable/changes/v1.11.html">Version 1.11.0 (2025-11-21) - MNE-Python</a></li>
</ul>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>On this page</h4>
<ul>
<li><a href="#introduction">1. 序論</a></li>
<li><a href="#bids">2. データ標準化(BIDS)</a></li>
<li><a href="#preprocessing">3. 次世代信号前処理</a></li>
<li><a href="#connectivity">4. ネットワーク神経科学</a></li>
<li><a href="#source-localization">5. ソース推定</a></li>
<li><a href="#multimodal">6. マルチモーダル(LSL)</a></li>
<li><a href="#software">7. ソフトウェア動向</a></li>
<li><a href="#roadmap">8. 結論・ロードマップ</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Relevant Pages</h4>
<ul>
<li><a href="{{ '/index' | relative_url }}">Home</a></li>
<li><a href="{{ '/tech_roadmap' | relative_url }}">Technology Roadmap</a></li>
</ul>
</div>
</aside>
</main>