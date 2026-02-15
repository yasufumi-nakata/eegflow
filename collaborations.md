---
layout: default
title: "協業候補：研究機関・企業・助成制度の優先度付きアクションプラン"
description: "mind-upload.comの検証基盤（Verification Commons）に接続可能な研究機関・プロジェクト・企業・助成制度を、優先度付きで整理したアクションプラン。"
article_type: Action Plan
subtitle: "L0達成を最短で実現するための外部連携先と具体的なアクション"
author: Mind Uploading Research Project
last_updated: "2026-02-15"
note: "随時更新"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>このページの目的</h2>
<p>
本ページは、mind-upload.com の検証基盤（Verification Commons）を<strong>L0（再現可能な解析）から段階的に構築</strong>するため、接続可能な研究機関・プロジェクト・企業・助成制度を優先度付きで整理したアクションプランです。Issue #256 に基づき、単独では実現不可能な規模の研究課題を、適切な連携先との協力によって最短ルートで達成するための指針を示します。
</p>
</div>

<div class="key-points">
<h4>協業の原則</h4>
<ul>
<li><strong>L0優先：</strong>再現可能な解析の達成を最優先とし、既存データセットの再解析から開始する</li>
<li><strong>標準準拠：</strong>BIDS、EEG-BIDS、OpenNeuro 等の国際標準に準拠した成果物を目指す</li>
<li><strong>相互利益：</strong>一方的な利用ではなく、双方に価値をもたらす協力関係を構築する</li>
<li><strong>透明性：</strong>協力内容、成果物、制約事項を公開し、コミュニティ全体の利益とする</li>
</ul>
</div>

<section class="section" id="top-10">
<h2 class="section-title">優先協業パートナー Top 10</h2>
<p>
L0 達成から長期ビジョンまでを段階的に実現するため、協業パートナーを優先順位付けしました。各パートナーとの協力により、Mind-Upload プロジェクトの検証基盤が強化されます。
</p>

<table class="data-table">
<thead>
<tr>
<th>優先度</th>
<th>パートナー</th>
<th>目標（Goal）</th>
<th>成果物（最小スコープ）</th>
<th>最初のステップ</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td><strong>BIDS / EEG-BIDS Community</strong></td>
<td>データ標準の国際標準との整合性確保</td>
<td>BIDS Derivatives 拡張仕様書（EEG QC ログ・同期ログ）、コミュニティフィードバック反映</td>
<td>EEG-BIDS メーリングリストに参加し、拡張提案を Discussion として投稿</td>
</tr>
<tr>
<td>2</td>
<td><strong>OpenNeuro</strong></td>
<td>DOI 付きデータデポジットと再現性基盤の確立</td>
<td>DOI 付きデータセット1件、BIDS 検証レポート、再現性ガイドライン</td>
<td>既存サンプルデータを BIDS 変換し、datalad 経由でアップロード準備</td>
</tr>
<tr>
<td>3</td>
<td><strong>MOABB / NeuroTechX</strong></td>
<td>L0/L1 ベンチマークを既存 BCI ベンチマークと互換化</td>
<td>MOABB 互換ベンチマーク、既存 BCI データセットとの比較結果、統合ドキュメント</td>
<td>MOABB リポジトリのイシュー・PR 構造を調査し、統合仕様をドラフト</td>
</tr>
<tr>
<td>4</td>
<td><strong>MNE-Python</strong></td>
<td>BIDS→前処理→メトリクス→出力のパイプライン統合</td>
<td>Docker コンテナ、MNE-Python 拡張モジュール、チュートリアル</td>
<td>MNE-BIDS チュートリアルに沿ったパイプラインを自前データで動作確認</td>
</tr>
<tr>
<td>5</td>
<td><strong>LSL Community</strong></td>
<td>同期監査ログテンプレートの標準化</td>
<td>LSL 同期ログ標準、監査証跡テンプレート、統合ガイド</td>
<td>LSL ドキュメントを読み、既存プロトコルと差分を整理して提案書作成</td>
</tr>
<tr>
<td>6</td>
<td><strong>INCF (+ Japan Node)</strong></td>
<td>Working Groups を通じた標準化コンセンサスの加速</td>
<td>INCF Working Group 参加、標準化提案書、日本コミュニティ形成</td>
<td>INCF Japan Node にコンタクトし、関連 WG の日程・参加方法を確認</td>
</tr>
<tr>
<td>7</td>
<td><strong>COGITATE (ARC-COGITATE)</strong></td>
<td>公開済みデータの再解析パッケージ開発</td>
<td>COGITATE データ再解析パッケージ、検証プロトコル、論文</td>
<td>COGITATE 公開データの BIDS 互換性を検証し、再解析スコープを定義</td>
</tr>
<tr>
<td>8</td>
<td><strong>AMED Brain/MINDS 2.0</strong></td>
<td>日本の「デジタル脳」研究インフラとの接続</td>
<td>データ相互運用性プロトコル、共同研究提案、インフラ統合</td>
<td>Brain/MINDS 公募・ワークショップ情報を追跡し、接点を特定</td>
</tr>
<tr>
<td>9</td>
<td><strong>Moonshot Goal 1 Projects</strong></td>
<td>BMI 標準の横断的適用と共同ベンチマーク</td>
<td>BMI 標準化提案、共同研究、横断的ベンチマーク</td>
<td>Moonshot Goal 1 採択プロジェクト一覧を取得し、標準化ワーキングの有無を確認</td>
</tr>
<tr>
<td>10</td>
<td><strong>MinD in a Device + 東京大学・渡邉研究室</strong></td>
<td>WBE 実装に関する地域的議論の実現</td>
<td>WBE 実装プロトコル、共同研究、地域コミュニティ形成</td>
<td>MinD in a Device のイベント・勉強会に参加し、渡邉正峰氏と接点を確保</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="research-projects">
<h2 class="section-title">研究機関・プロジェクト比較表</h2>
<p>
Mind-Upload プロジェクトと協力可能な研究機関、データリポジトリ、標準化プロジェクトの包括的なリストです。分野・焦点と協力の可能性を整理しています。
</p>

<table class="data-table">
<thead>
<tr>
<th>機関・プロジェクト名</th>
<th>分野・焦点</th>
<th>協力の可能性</th>
<th>主な貢献領域</th>
<th>リンク</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>BIDS</strong></td>
<td>脳イメージングデータ標準</td>
<td>高</td>
<td>EEG-BIDS 拡張、Derivatives 仕様</td>
<td><a href="https://bids.neuroimaging.io/" target="_blank">公式サイト</a></td>
</tr>
<tr>
<td><strong>OpenNeuro</strong></td>
<td>神経科学データリポジトリ</td>
<td>高</td>
<td>DOI 付きデポジット、BIDS 検証</td>
<td><a href="https://openneuro.org/" target="_blank">OpenNeuro</a></td>
</tr>
<tr>
<td><strong>MOABB</strong></td>
<td>BCI ベンチマーク</td>
<td>高</td>
<td>L0/L1 ベンチマーク統合</td>
<td><a href="https://github.com/NeuroTechX/moabb" target="_blank">GitHub</a></td>
</tr>
<tr>
<td><strong>MNE-Python</strong></td>
<td>EEG/MEG 解析ツール</td>
<td>高</td>
<td>パイプライン統合、コンテナ化</td>
<td><a href="https://mne.tools/" target="_blank">MNE-Python</a></td>
</tr>
<tr>
<td><strong>LSL (Lab Streaming Layer)</strong></td>
<td>リアルタイムデータストリーミング</td>
<td>高</td>
<td>同期ログ標準化、監査証跡</td>
<td><a href="https://labstreaminglayer.readthedocs.io/" target="_blank">LSL</a></td>
</tr>
<tr>
<td><strong>INCF</strong></td>
<td>神経情報学、標準化</td>
<td>高</td>
<td>Working Groups、標準化プロセス</td>
<td><a href="https://www.incf.org/" target="_blank">INCF</a></td>
</tr>
<tr>
<td><strong>COGITATE Consortium</strong></td>
<td>意識研究、Adversarial Collaboration</td>
<td>中</td>
<td>データ再解析、検証プロトコル</td>
<td><a href="https://cogitate-consortium.com/" target="_blank">COGITATE</a></td>
</tr>
<tr>
<td><strong>AMED Brain/MINDS 2.0</strong></td>
<td>日本の脳科学研究</td>
<td>中</td>
<td>デジタル脳インフラ、データ相互運用</td>
<td><a href="https://brainminds.jp/" target="_blank">Brain/MINDS</a></td>
</tr>
<tr>
<td><strong>Moonshot Goal 1</strong></td>
<td>BMI、脳科学研究</td>
<td>中</td>
<td>標準化、横断的協力</td>
<td><a href="https://www.jst.go.jp/moonshot/" target="_blank">Moonshot R&D</a></td>
</tr>
<tr>
<td><strong>EBRAINS</strong></td>
<td>欧州の脳研究インフラ</td>
<td>低（長期）</td>
<td>長期ビジョン、大規模シミュレーション</td>
<td><a href="https://www.ebrains.eu/" target="_blank">EBRAINS</a></td>
</tr>
<tr>
<td><strong>TVB (The Virtual Brain)</strong></td>
<td>脳シミュレーション</td>
<td>低（長期）</td>
<td>長期ビジョン、モデル検証</td>
<td><a href="https://www.thevirtualbrain.org/" target="_blank">TVB</a></td>
</tr>
<tr>
<td><strong>Blue Brain Project</strong></td>
<td>全脳シミュレーション</td>
<td>低（長期）</td>
<td>長期ビジョン、回路レベル検証</td>
<td><a href="https://www.epfl.ch/research/domains/bluebrain/" target="_blank">Blue Brain</a></td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="researchers">
<h2 class="section-title">研究者・研究コンソーシアム</h2>
<p>
Mind-Upload プロジェクトと協力可能な研究者、研究グループのリストです。
</p>

<table class="data-table">
<thead>
<tr>
<th>研究者・コンソーシアム</th>
<th>所属・役職</th>
<th>専門分野</th>
<th>協力の可能性</th>
<th>リンク</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>渡邉正峰</strong><br>(Masataka Watanabe)</td>
<td>東京大学 准教授</td>
<td>WBE、意識研究、認知科学</td>
<td>高</td>
<td><a href="https://mindinadevice.org/" target="_blank">MinD in a Device</a></td>
</tr>
<tr>
<td><strong>COGITATE Consortium</strong></td>
<td>複数機関（国際）</td>
<td>意識研究、Adversarial Collaboration</td>
<td>中</td>
<td><a href="https://cogitate-consortium.com/" target="_blank">COGITATE</a></td>
</tr>
<tr>
<td><strong>Alexandre Barachant</strong></td>
<td>MOABB 共同開発者</td>
<td>BCI、機械学習、信号処理</td>
<td>高</td>
<td><a href="https://github.com/alexandrebarachant" target="_blank">GitHub</a></td>
</tr>
<tr>
<td><strong>Vinay Jayaram</strong></td>
<td>MOABB 共同開発者</td>
<td>BCI、ベンチマーク、NeuroTechX</td>
<td>高</td>
<td><a href="https://github.com/vinay-jayaram" target="_blank">GitHub</a></td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>研究者への連絡について</strong>
<p>
研究者への直接的な連絡は、事前に GitHub Issues で議論し、プロジェクトの目的と協力内容を明確にした上で行うことを推奨します。各研究者の研究負荷と優先順位を尊重し、相互利益のある協力関係を構築することが重要です。
</p>
</div>
</section>

<section class="section" id="companies">
<h2 class="section-title">企業・組織一覧</h2>
<p>
Mind-Upload プロジェクトと協力可能な企業、非営利組織、コミュニティのリストです。
</p>

<table class="data-table">
<thead>
<tr>
<th>企業・組織名</th>
<th>分野・焦点</th>
<th>協力の可能性</th>
<th>主な協力内容</th>
<th>リンク</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Neuralink</strong></td>
<td>BMI、侵襲的脳インターフェース</td>
<td>低（長期）</td>
<td>技術的知見、データ形式標準化</td>
<td><a href="https://neuralink.com/" target="_blank">Neuralink</a></td>
</tr>
<tr>
<td><strong>Synchron</strong></td>
<td>ステントロード、非侵襲的 BMI</td>
<td>低（長期）</td>
<td>技術的知見、データ形式</td>
<td><a href="https://synchron.com/" target="_blank">Synchron</a></td>
</tr>
<tr>
<td><strong>OpenBCI</strong></td>
<td>オープンソース BCI ハードウェア</td>
<td>中</td>
<td>データ形式標準化、コミュニティ連携</td>
<td><a href="https://openbci.com/" target="_blank">OpenBCI</a></td>
</tr>
<tr>
<td><strong>MinD in a Device</strong></td>
<td>WBE 研究、意識研究</td>
<td>高</td>
<td>WBE 実装プロトコル、地域コミュニティ</td>
<td><a href="https://mindinadevice.org/" target="_blank">MinD in a Device</a></td>
</tr>
<tr>
<td><strong>Carboncopies Foundation</strong></td>
<td>WBE 研究支援、意識研究</td>
<td>中</td>
<td>コミュニティ連携、研究支援</td>
<td><a href="https://www.carboncopies.org/" target="_blank">Carboncopies</a></td>
</tr>
<tr>
<td><strong>Brain Preservation Foundation</strong></td>
<td>脳保存技術、WBE 研究</td>
<td>低（長期）</td>
<td>技術的知見、研究支援</td>
<td><a href="https://www.brainpreservation.org/" target="_blank">BPF</a></td>
</tr>
<tr>
<td><strong>INCF</strong></td>
<td>神経情報学、標準化</td>
<td>高</td>
<td>標準化プロセス、Working Groups 参加</td>
<td><a href="https://www.incf.org/" target="_blank">INCF</a></td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="funding">
<h2 class="section-title">助成制度・資金源</h2>
<p>
Mind-Upload プロジェクトの研究開発を支援可能な資金源のリストです。
</p>

<table class="data-table">
<thead>
<tr>
<th>資金源名</th>
<th>対象分野</th>
<th>協力の可能性</th>
<th>申請条件・備考</th>
<th>リンク</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>AMED Brain/MINDS 2.0</strong></td>
<td>脳科学研究、デジタル脳</td>
<td>中</td>
<td>日本の研究機関が主導、インフラ統合</td>
<td><a href="https://brainminds.jp/" target="_blank">Brain/MINDS</a></td>
</tr>
<tr>
<td><strong>Moonshot R&D</strong></td>
<td>BMI、脳科学研究</td>
<td>中</td>
<td>日本の研究機関、BMI 標準化</td>
<td><a href="https://www.jst.go.jp/moonshot/" target="_blank">Moonshot R&D</a></td>
</tr>
<tr>
<td><strong>JSPS / KAKEN</strong></td>
<td>基礎研究、学術研究</td>
<td>中</td>
<td>日本の研究機関が申請主体</td>
<td><a href="https://www.jsps.go.jp/" target="_blank">JSPS</a></td>
</tr>
<tr>
<td><strong>NIH BRAIN Initiative</strong></td>
<td>脳科学研究、神経技術</td>
<td>低</td>
<td>米国の研究機関が主導</td>
<td><a href="https://braininitiative.nih.gov/" target="_blank">BRAIN Initiative</a></td>
</tr>
<tr>
<td><strong>Templeton World Charity Foundation</strong></td>
<td>意識研究、哲学的研究</td>
<td>低</td>
<td>意識研究、哲学的側面の強調</td>
<td><a href="https://www.templetonworldcharity.org/" target="_blank">Templeton</a></td>
</tr>
<tr>
<td><strong>Center for Open Science (OSF)</strong></td>
<td>オープンサイエンス、再現性</td>
<td>高</td>
<td>再現性向上、オープンサイエンス推進</td>
<td><a href="https://www.cos.io/" target="_blank">COS</a></td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>資金申請について</strong>
<p>
資金申請は、プロジェクトの目的と成果物を明確にし、既存の検証基盤（L0 達成状況）を基盤として申請することを推奨します。各資金源の申請条件と優先順位を確認し、適切な研究機関との連携を検討してください。
</p>
</div>
</section>

<section class="section" id="action-short">
<h2 class="section-title">短期アクションプラン（L0 達成）</h2>
<p>
再現可能な解析を実現するため、以下を最優先で実施します。
</p>

<div class="stage-list">
<div class="stage-item">
<div class="stage-number">1</div>
<div class="stage-body">
<h4>BIDS 準拠と OpenNeuro デポジット</h4>
<p>既存の公開データセットを用いて、第三者がコード・データ・環境を揃えて同じ結果を再現できる状態を実現する。BIDS 準拠データセットの作成と OpenNeuro へのデポジットを完了する。</p>
</div>
</div>
<div class="stage-item">
<div class="stage-number">2</div>
<div class="stage-body">
<h4>BIDS Derivatives 拡張</h4>
<p>EEG QC ログ、同期ログを BIDS Derivatives として提案し、標準化プロセスに参加する。</p>
</div>
</div>
<div class="stage-item">
<div class="stage-number">3</div>
<div class="stage-body">
<h4>MNE-Python ベースのパイプライン構築</h4>
<p>BIDS→前処理→メトリクス→出力の再現可能な解析パイプラインを構築し、Docker コンテナで環境を固定化する。</p>
</div>
</div>
<div class="stage-item">
<div class="stage-number">4</div>
<div class="stage-body">
<h4>LSL 同期ログ標準の策定</h4>
<p>Lab Streaming Layer との統合プロトコルを策定し、監査証跡テンプレートを整備する。</p>
</div>
</div>
</div>

<div class="tag-list">
<span class="tag">BIDS</span><span class="tag">OpenNeuro</span><span class="tag">MNE-Python</span><span class="tag">LSL</span><span class="tag">L0</span>
</div>
</section>

<section class="section" id="action-mid">
<h2 class="section-title">中期アクションプラン（L1/L2 ベンチマーク）</h2>
<p>
L0 を基盤として、複数のデータセット・手法間で比較可能なベンチマークを確立します。
</p>

<div class="stage-list">
<div class="stage-item">
<div class="stage-number">1</div>
<div class="stage-body">
<h4>MOABB フレームワークとの統合</h4>
<p>L0/L1 ベンチマークを既存の BCI ベンチマークと互換性のある形で実装し、MOABB フレームワークへ統合する。</p>
</div>
</div>
<div class="stage-item">
<div class="stage-number">2</div>
<div class="stage-body">
<h4>COGITATE データ再解析</h4>
<p>公開済みデータの再解析パッケージを開発し、Adversarial Collaboration の知見を Mind-Upload 検証基盤に統合する。</p>
</div>
</div>
<div class="stage-item">
<div class="stage-number">3</div>
<div class="stage-body">
<h4>INCF Working Groups 参加</h4>
<p>標準化コンセンサスの加速と日本ノードとの連携による地域コミュニティ構築を行う。</p>
</div>
</div>
<div class="stage-item">
<div class="stage-number">4</div>
<div class="stage-body">
<h4>Brain/MINDS 2.0 とのインフラ統合</h4>
<p>日本の「デジタル脳」研究インフラとの接続を図り、データ相互運用性プロトコルを策定する。</p>
</div>
</div>
</div>

<div class="tag-list">
<span class="tag">MOABB</span><span class="tag">COGITATE</span><span class="tag">INCF</span><span class="tag">Brain/MINDS</span><span class="tag">L1</span><span class="tag">L2</span>
</div>
</section>

<section class="section" id="action-long">
<h2 class="section-title">長期アクションプラン</h2>
<p>
介入・摂動ベースの本人性検証と、WBE 長期ビジョンへの接続を目指します。
</p>

<div class="stage-list">
<div class="stage-item">
<div class="stage-number">1</div>
<div class="stage-body">
<h4>反事実テスト・介入予測の操作化</h4>
<p>学習済みタスクを超えた介入・摂動ベースの本人性検証プロトコルを確立する。反事実テスト（Counterfactual Tests）と介入予測（Intervention Prediction）の検証プロトコルを設計する。</p>
</div>
</div>
<div class="stage-item">
<div class="stage-number">2</div>
<div class="stage-body">
<h4>Moonshot Goal 1 との横断的標準化</h4>
<p>BMI 分野における L0/L1 標準の横断的適用と、Moonshot Goal 1 プロジェクトとの連携を行う。</p>
</div>
</div>
<div class="stage-item">
<div class="stage-number">3</div>
<div class="stage-body">
<h4>MinD in a Device + 東京大学との WBE 実装議論</h4>
<p>渡邉正峰研究室との連携により、WBE 実装に関する地域的議論を実現し、実装プロトコルを策定する。</p>
</div>
</div>
<div class="stage-item">
<div class="stage-number">4</div>
<div class="stage-body">
<h4>長期ビジョンとの接続</h4>
<p>EBRAINS、TVB、Blue Brain Project 等の長期ビジョンと接続し、マルチスケール因果モデリングの基盤を構築する。</p>
</div>
</div>
</div>

<div class="tag-list">
<span class="tag">Counterfactual</span><span class="tag">Intervention</span><span class="tag">Moonshot</span><span class="tag">WBE</span><span class="tag">L2+</span>
</div>
</section>

<section class="section" id="contact">
<h2 class="section-title">協力の申し込み・問い合わせ</h2>
<p>
Mind-Upload プロジェクトへの協力をご希望の場合は、以下の方法でお問い合わせください。
</p>

<div class="key-points">
<h4>連絡方法</h4>
<ul>
<li><strong>GitHub Issues：</strong> <a href="https://github.com/yasufumi-nakata/mind-upload/issues" target="_blank">Issue #256</a> または新規 Issue を作成</li>
<li><strong>GitHub Discussions：</strong> 一般的な質問や議論は Discussions を利用</li>
<li><strong>Email：</strong> 機密性の高い内容や詳細な協議が必要な場合は、GitHub 経由で連絡先を交換</li>
</ul>
</div>

<div class="note-box">
<strong>協力の原則</strong>
<p>
協力は相互利益を基盤とし、透明性を重視します。協力内容、成果物、制約事項は公開し、コミュニティ全体の利益となるよう努めます。一方的な利用や、研究倫理に反する協力は受け付けません。
</p>
</div>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>Start Here</h4>
<ul>
<li><a href="verification.html">検証基盤（Verification）→</a></li>
<li><a href="tech_roadmap.html">技術ロードマップ（Roadmap）→</a></li>
<li><a href="perspective.html">理論的展望（Perspective）→</a></li>
<li><a href="wbe_101.html">WBE 入門 →</a></li>
<li><a href="eeg_101.html">EEG 入門 →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Related Pages</h4>
<ul>
<li><a href="index.html">メインページ →</a></li>
<li><a href="issue.html">貢献ガイド（Contribute）→</a></li>
<li><a href="proposals.html">技術提案（Proposals）→</a></li>
<li><a href="datasets.html">データセット（Datasets）→</a></li>
<li><a href="glossary.html">用語集（Glossary）→</a></li>
<li><a href="faq.html">FAQ →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>ページ内ナビゲーション</h4>
<ul>
<li><a href="#top-10">優先協業パートナー Top 10</a></li>
<li><a href="#research-projects">研究機関・プロジェクト</a></li>
<li><a href="#researchers">研究者</a></li>
<li><a href="#companies">企業・組織</a></li>
<li><a href="#funding">助成制度・資金源</a></li>
<li><a href="#action-short">短期アクションプラン（L0）</a></li>
<li><a href="#action-mid">中期アクションプラン（L1/L2）</a></li>
<li><a href="#action-long">長期アクションプラン</a></li>
<li><a href="#contact">問い合わせ</a></li>
</ul>
</div>

<div class="note-box">
<strong>このページについて</strong>
<p>
本ページは Issue #256 に基づき、mind-upload.com の検証基盤（Verification Commons）に接続可能な研究機関・プロジェクト・企業・助成制度を、優先度付きで整理したアクションプランです。L0 達成を最優先とし、段階的に長期ビジョンへと展開する戦略に基づいています。
</p>
</div>

</aside>

</main>
