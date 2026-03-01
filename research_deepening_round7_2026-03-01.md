---
layout: default
title: "Research Deepening Round 7 (2026-03-01): U8/U13/U14/U15 参照精査"
description: "高ノイズ比率ユニットの参考文献を手動トリアージし、RQ直結のコア文献セットを固定。"
article_type: "Evidence Addendum"
subtitle: "手動トリアージ（維持・要置換・要確認） + RQ別推奨文献"
author: Mind Uploading Research Project
last_updated: "2026-03-01"
note: "Round 7 (manual reference triage)"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Round 7 の狙い</h2>
<p>
自動監査でノイズ比率が高かった U8/U13/U14/U15 について、
文献タイトルとRQ適合を人手で点検しました。
本ラウンドは「機械監査の結果を鵜呑みにしない」ための確認工程です。
</p>
<p>
判定は <strong>維持</strong> / <strong>要置換</strong> / <strong>要確認</strong> の3区分で、
要置換には置換候補を明示しています。
</p>
</div>

<section class="section" id="u8-triage">
<h2 class="section-title">U8: 閉ループ安定性（手動トリアージ）</h2>
<table class="data-table">
<thead><tr><th>疑義文献</th><th>判定</th><th>理由（平易）</th><th>置換候補</th></tr></thead>
<tbody>
<tr><td>A Fixed-Time Stable Adaptation Law for Safety-Critical Control...</td><td>要確認</td><td>安全制御としては有用ですが、BCI特有の遅延/ドリフトへ直結する根拠が弱めです。</td><td>10.1038/s41591-024-03196-z（aDBS 実運用）</td></tr>
<tr><td>Towards Neurohaptics: BCI for Decoding Intuitive Sense of Touch</td><td>要置換</td><td>触覚デコードの紹介で、閉ループ安定性KPIへの接続が弱いです。</td><td>10.1093/brain/awad429（在宅aDBSと比例制御）</td></tr>
<tr><td>Zero-calibration cVEP BCI using word prediction</td><td>要置換</td><td>スペラー用途で、U8の安全制約・異常検知と直接対応しません。</td><td>10.1038/s41531-025-01124-7（慢性aDBS運用）</td></tr>
<tr><td>Brain-controlled devices: the perception-action closed loop</td><td>維持</td><td>古いが「閉ループ」の概念整理としては有効です。</td><td>補助文献として維持（主根拠は最新臨床へ移行）</td></tr>
<tr><td>EDAPT: Calibration-Free BCIs with Continual Online Adaptation</td><td>維持</td><td>ドリフト・較正コストへの直接的な技術提案です。</td><td>10.1038/s41531-024-00772-5（実地運用データ）を併記</td></tr>
<tr><td>Dynamic Neural Communication...</td><td>要置換</td><td>テーマが広く、U8の安定性評価軸に対して焦点が散ります。</td><td>10.1038/s41551-025-01438-0（遠隔最適化型aDBS）</td></tr>
<tr><td>Calibration-free online test-time adaptation for EEG MI decoding</td><td>維持</td><td>オンライン適応の具体手法としてRQ2/RQ6に関連します。</td><td>10.1001/jamaneurol.2025.2781（長期個別最適化）を追加</td></tr>
<tr><td>Enhancing Our Lives with Immersive Virtual Reality</td><td>要置換</td><td>VR一般論で、閉ループ神経制御の安全性根拠としては弱いです。</td><td>10.1080/17434440.2024.2438309（閉ループDBS実装課題）</td></tr>
</tbody>
</table>

<h3>U8 RQ別コア文献（推奨）</h3>
<table class="data-table">
<thead><tr><th>RQ</th><th>推奨コア文献</th><th>理由</th></tr></thead>
<tbody>
<tr><td>RQ1</td><td>10.1038/s41591-024-03196-z / 10.1093/brain/awad429</td><td>遅延・制御を実運用で評価しているためです。</td></tr>
<tr><td>RQ2</td><td>10.1038/s41531-025-01124-7 / 10.1038/s41531-024-00772-5</td><td>オンライン較正と慢性運用の実データがあるためです。</td></tr>
<tr><td>RQ3</td><td>10.1001/jamaneurol.2025.2781 / 10.1038/s41582-025-01131-5</td><td>個体差と長期変動を扱うためです。</td></tr>
<tr><td>RQ4</td><td>10.1038/s41551-025-01438-0 / 10.1080/17434440.2024.2438309</td><td>異常検知・フェイルセーフ設計に直結するためです。</td></tr>
<tr><td>RQ5</td><td>10.1101/2024.08.26.24312580 / 10.1038/s41591-024-03196-z</td><td>運用KPI（誤作動/回復時間）へ接続しやすいためです。</td></tr>
<tr><td>RQ6</td><td>10.1001/jamaneurol.2025.2781 / 10.1038/s41531-025-01124-7</td><td>再学習頻度と長期劣化の評価に使えるためです。</td></tr>
</tbody>
</table>
</section>

<section class="section" id="u13-triage">
<h2 class="section-title">U13: 模倣分離（手動トリアージ）</h2>
<table class="data-table">
<thead><tr><th>疑義文献</th><th>判定</th><th>理由（平易）</th><th>置換候補</th></tr></thead>
<tbody>
<tr><td>ConsistencyAI benchmark (demographic factual consistency)</td><td>要確認</td><td>整合性評価としては有用ですが、神経デコード直結性は限定的です。</td><td>10.1126/sciadv.adw1464（mind captioning）</td></tr>
<tr><td>A survey on LLM based autonomous agents</td><td>要置換</td><td>自律エージェント総説で、U13の因果保存評価から離れます。</td><td>10.1038/s41593-023-01304-9（semantic reconstruction）</td></tr>
<tr><td>Explainability for LLMs: A Survey</td><td>要置換</td><td>一般XAIで、brain-to-textの因果同定には距離があります。</td><td>10.1016/j.celrep.2024.114924（brain-to-text）</td></tr>
<tr><td>fMRI-LM foundation model</td><td>要確認</td><td>関連性はあるものの、基盤モデル提案で評価契約への接続が未確定です。</td><td>10.1038/s42256-020-00257-z（shortcut検査）</td></tr>
<tr><td>Decoding fMRI Data into Captions using Prefix LM</td><td>維持</td><td>fMRIから言語復元を扱い、RQ1に近いです。</td><td>10.1038/s41593-023-01304-9 を併記</td></tr>
<tr><td>Towards Diverse and Efficient Audio Captioning via Diffusion Models</td><td>要置換</td><td>一般音声キャプションで、神経由来データではありません。</td><td>10.1126/sciadv.adw1464（神経→記述文）</td></tr>
<tr><td>End-to-End Framework for Invasive Brain Signal Decoding with LLMs</td><td>維持</td><td>神経信号とLLM接続を直接扱っているためです。</td><td>10.1609/aaai.v39i27.35124（因果評価）を併記</td></tr>
<tr><td>LLMVA-GEBC (video event boundary captioning)</td><td>要置換</td><td>映像キャプション競技色が強く、U13の本旨から外れます。</td><td>10.1038/s42256-020-00257-z（shortcut学習）</td></tr>
</tbody>
</table>

<h3>U13 RQ別コア文献（推奨）</h3>
<table class="data-table">
<thead><tr><th>RQ</th><th>推奨コア文献</th><th>理由</th></tr></thead>
<tbody>
<tr><td>RQ1</td><td>10.1038/s41593-023-01304-9 / 10.1016/j.celrep.2024.114924</td><td>意味復元の一次研究として直接対応するためです。</td></tr>
<tr><td>RQ2</td><td>arXiv:2506.22486 / 10.1609/aaai.v39i27.35124</td><td>幻覚検出と因果表現評価を結びやすいためです。</td></tr>
<tr><td>RQ3</td><td>10.1038/s42256-020-00257-z / 10.1609/aaai.v39i27.35124</td><td>同一出力・異機構（shortcut）を検出しやすいためです。</td></tr>
<tr><td>RQ4</td><td>10.1609/aaai.v39i17.33998 / 10.1016/j.knosys.2025.113565</td><td>模倣性能と因果制約の分離評価に有効なためです。</td></tr>
<tr><td>RQ5</td><td>10.1109/EMBC58623.2025.11251641 / 10.1109/EMBC53108.2024.10782730</td><td>知覚/想起比較を同一系列で設計しやすいためです。</td></tr>
<tr><td>RQ6</td><td>arXiv:2506.22486 / 10.1038/s42256-020-00257-z</td><td>リーク・shortcutの分離検出に使えるためです。</td></tr>
</tbody>
</table>
</section>

<section class="section" id="u14-triage">
<h2 class="section-title">U14: 追試可能性（手動トリアージ）</h2>
<table class="data-table">
<thead><tr><th>疑義文献</th><th>判定</th><th>理由（平易）</th><th>置換候補</th></tr></thead>
<tbody>
<tr><td>Revisiting gender bias research in bibliometrics (SoDA Cards)</td><td>要置換</td><td>カード概念は近いですが、神経再現性運用への直接性が弱いです。</td><td>10.1016/j.jneumeth.2023.109931</td></tr>
<tr><td>Cards Against AI (humor prediction)</td><td>要置換</td><td>タスクが異なり、追試可能性の中核論点に接続しません。</td><td>10.1038/s41597-024-03559-8</td></tr>
<tr><td>Pulsar Science with the SKA Observatory</td><td>要置換</td><td>分野が異なり、U14の評価契約と関係が薄いです。</td><td>BIDS 1.10.1 仕様書</td></tr>
<tr><td>Technological Competence for VR in neuroscience</td><td>要確認</td><td>神経研究運用には関係しますが、再現性監査の主文献としては弱めです。</td><td>arXiv:2311.04912（ezBIDS）</td></tr>
<tr><td>Preregistration template for cognitive models</td><td>維持</td><td>RQ2（探索/検証分離）に直接有効です。</td><td>10.7554/eLife.85980 を併記</td></tr>
<tr><td>A colouring protocol for generalized Russian cards problem</td><td>要置換</td><td>数学的には興味深いですが、再現性実務の根拠にはなりません。</td><td>10.1038/s41597-023-02614-0</td></tr>
<tr><td>Behavior Score Cards</td><td>要置換</td><td>用語一致のみで、U14の技術監査文脈に合致しません。</td><td>10.1002/epi4.12704</td></tr>
<tr><td>Reproductive Health Safety Cards</td><td>要置換</td><td>領域が異なり、再現性運用指標への接続が困難です。</td><td>10.1001/jama.2025.13350</td></tr>
</tbody>
</table>

<h3>U14 RQ別コア文献（推奨）</h3>
<table class="data-table">
<thead><tr><th>RQ</th><th>推奨コア文献</th><th>理由</th></tr></thead>
<tbody>
<tr><td>RQ1</td><td>10.1016/j.jneumeth.2023.109931 / 10.1038/s41597-024-03559-8</td><td>固定粒度と実データ再現の両面を扱うためです。</td></tr>
<tr><td>RQ2</td><td>10.7554/eLife.85980 / 10.1001/jama.2025.13350</td><td>探索/検証分離の運用テンプレが明確なためです。</td></tr>
<tr><td>RQ3</td><td>10.1038/s41597-023-02614-0 / 10.1002/epi4.12704</td><td>データベース品質とリーク/過適合監査に使えるためです。</td></tr>
<tr><td>RQ4</td><td>BIDS 1.10.1 / BEP036 draft (Zenodo 18201723)</td><td>Card相当のメタデータ運用に接続しやすいためです。</td></tr>
<tr><td>RQ5</td><td>10.1016/j.jneumeth.2023.109931 / 10.7554/eLife.85980</td><td>否定例公開の必要性を方法論側で支えるためです。</td></tr>
<tr><td>RQ6</td><td>arXiv:2311.04912 / 10.1038/s41597-024-03559-8</td><td>コンテナ/検証ワークフローと運用コストを同時に見られるためです。</td></tr>
</tbody>
</table>
</section>

<section class="section" id="u15-triage">
<h2 class="section-title">U15: 制度統合（手動トリアージ）</h2>
<table class="data-table">
<thead><tr><th>疑義文献</th><th>判定</th><th>理由（平易）</th><th>置換候補</th></tr></thead>
<tbody>
<tr><td>Honest Computing: data lineage and provenance</td><td>維持</td><td>監査証跡という観点で、制度KPIへ接続可能です。</td><td>EU AI Act条文と併記して運用化</td></tr>
<tr><td>Byzantine-Resilient SGD in High Dimensions</td><td>要置換</td><td>攻撃耐性最適化として有用ですが、法制度統合への直結が弱いです。</td><td>10.1016/S1474-4422(25)00124-3</td></tr>
<tr><td>Data Encoding for Byzantine-Resilient Distributed Optimization</td><td>要置換</td><td>同上。制度・監査設計の主根拠としては焦点がずれます。</td><td>10.1093/jhuman/huae042</td></tr>
<tr><td>Equal access to mental augmentation</td><td>維持</td><td>権利配分の論点としてU15 RQ2/RQ3に有効です。</td><td>OECD原則との対応表を追加</td></tr>
<tr><td>Dynamic Neural Communication...</td><td>要置換</td><td>技術解説寄りで、制度統合の根拠としては弱いです。</td><td>10.6028/NIST.AI.600-1</td></tr>
<tr><td>Privacy and Security in BCI</td><td>維持</td><td>神経データ機微性と保護要件の基礎文献です。</td><td>EU AI Actと紐付けて運用化</td></tr>
<tr><td>Towards Neurohaptics</td><td>要置換</td><td>BCI応用技術であり、制度評価KPIには直接つながりません。</td><td>CETS No.225（Council of Europe）</td></tr>
<tr><td>Privacy and Ethics in BCI Research</td><td>維持</td><td>制度側要件へ橋渡しできる基礎論点を含みます。</td><td>ISO/IEC 42001 と対照運用</td></tr>
</tbody>
</table>

<h3>U15 RQ別コア文献（推奨）</h3>
<table class="data-table">
<thead><tr><th>RQ</th><th>推奨コア文献</th><th>理由</th></tr></thead>
<tbody>
<tr><td>RQ1</td><td>EU AI Act 2024/1689 / 10.1016/S1474-4422(25)00124-3</td><td>法概念と神経データ機微性の接続に直接有効です。</td></tr>
<tr><td>RQ2</td><td>10.1093/jhuman/huae042 / 10.6028/NIST.AI.600-1</td><td>neurorights論と監査項目を対応づけやすいためです。</td></tr>
<tr><td>RQ3</td><td>OECD AI Principles / CETS No.225</td><td>法域横断の最小共通語彙を作りやすいためです。</td></tr>
<tr><td>RQ4</td><td>ISO/IEC 42001 / EU AI Act 2024/1689</td><td>停止条件・更新条件を制度運用に落としやすいためです。</td></tr>
</tbody>
</table>
</section>

<section class="section" id="summary">
<h2 class="section-title">Round 7 要約</h2>
<ul>
<li>U8/U13/U14/U15 の疑義文献 32件を手動判定し、置換候補を固定しました。</li>
<li>RQ別の推奨コア文献を定義し、次回は本体文献リストを段階置換できる状態にしました。</li>
<li>外部依存タスク: 置換後の最終採否（編集委員会レビュー）。完了条件: U別コア文献セットの承認。</li>
</ul>
</section>

</article>
</main>
