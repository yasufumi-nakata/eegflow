---
layout: default
title: "Research Deepening Round 4 (2026-03-01): U8"
description: "U8（閉ループ安定性）の6問いを一次情報で深掘り。"
article_type: "Evidence Addendum"
subtitle: "遅延・ドリフト・安全KPIの実装寄り整理"
author: Mind Uploading Research Project
last_updated: "2026-03-01"
note: "Round 4 (U8)"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Round 4 の狙い</h2>
<p>
U8（閉ループ安定性）は、実験から運用へ進むときの安全の中核です。
この追補では、U8の6問いに対して、
一次情報を追加し、実行可能な変更と外部依存を分けて整理します。
</p>
</div>

<section class="section" id="u8">
<h2 class="section-title">U8: 閉ループ安定性（Round 4）</h2>
<table class="data-table">
<thead><tr><th>RQ</th><th>今回の深掘り（平易）</th><th>追加一次情報</th><th>今回実行する変更</th><th>外部依存タスク</th></tr></thead>
<tbody>
<tr>
<td>1</td>
<td>遅延許容域は理論だけでなく、実運用のDBSデータで具体化できる段階です。</td>
<td>
<a href="https://doi.org/10.1038/s41591-024-03196-z" target="_blank">Chronic adaptive DBS vs conventional DBS (Nat Med, 2024)</a><br>
<a href="https://doi.org/10.1093/brain/awad429" target="_blank">At-home adaptive dual-target DBS with proportional control (Brain, 2024)</a>
</td>
<td>U8 RQ1に「遅延上限(ms)」と「安定マージン」を必須欄として追加します。</td>
<td>担当: 臨床/安全チーム。前提: 安全審査承認。完了条件: 遅延超過時の安全停止手順の承認。</td>
</tr>
<tr>
<td>2</td>
<td>オンライン較正とドリフト対策は、長期運用報告で実用知見が増えています。</td>
<td>
<a href="https://doi.org/10.1038/s41531-025-01124-7" target="_blank">Chronic adaptive DBS: clinical outcomes and programming strategies (npj Parkinson’s, 2025)</a><br>
<a href="https://doi.org/10.1038/s41531-024-00772-5" target="_blank">ADAPT-PD sensing data and methodology (npj Parkinson’s, 2024)</a>
</td>
<td>U8 RQ2に「再較正頻度」「ドリフト検出閾値」を追加します。</td>
<td>担当: 運用チーム。前提: 長期ログ収集基盤。完了条件: 再較正プロトコルv1公開。</td>
</tr>
<tr>
<td>3</td>
<td>個体差・日内変動は大きく、単一セッション性能での評価は不十分です。</td>
<td>
<a href="https://doi.org/10.1001/jamaneurol.2025.2781" target="_blank">Long-Term Personalized Adaptive DBS (JAMA Neurol, 2025)</a><br>
<a href="https://doi.org/10.1038/s41582-025-01131-5" target="_blank">From adaptive DBS to adaptive circuit targeting (Nat Rev Neurol, 2025)</a>
</td>
<td>U8 RQ3に「日内変動係数」「個体内分散」を追加します。</td>
<td>担当: 解析WG。前提: 連続計測合意。完了条件: 個体差を含む安定性評価公開。</td>
</tr>
<tr>
<td>4</td>
<td>異常検知とフェイルセーフは、臨床報告を運用契約へ翻訳する作業が残っています。</td>
<td>
<a href="https://doi.org/10.1080/17434440.2024.2438309" target="_blank">Closed-loop DBS systems for neuropsychiatric disorders (2024)</a><br>
<a href="https://doi.org/10.1038/s41551-025-01438-0" target="_blank">Movement-responsive DBS with remotely optimized decoder (Nat Biomed Eng, 2026)</a>
</td>
<td>U8 RQ4に「異常検知再現率」「フェイルセーフ発動時間」を追加します。</td>
<td>担当: 安全委員会。前提: 失敗時責任分界の整理。完了条件: フェイルセーフ監査手順の承認。</td>
</tr>
<tr>
<td>5</td>
<td>ヒューマンオーバーライドのKPIは、誤作動率と回復時間を対で管理するのが実務的です。</td>
<td>
<a href="https://doi.org/10.1101/2024.08.26.24312580" target="_blank">Adaptive DBS in Parkinson's disease: Delphi consensus (2024 preprint)</a><br>
<a href="https://doi.org/10.1038/s41591-024-03196-z" target="_blank">Blinded randomized feasibility trial (Nat Med, 2024)</a>
</td>
<td>U8 RQ5に「オーバーライド発生率」「回復時間中央値」を追加します。</td>
<td>担当: 臨床運用チーム。前提: 現場運用手順合意。完了条件: KPIの定期報告開始。</td>
</tr>
<tr>
<td>6</td>
<td>再学習頻度は「性能低下を抑える頻度」と「安全余裕を保つ頻度」の最小公倍数で決める必要があります。</td>
<td>
<a href="https://doi.org/10.1001/jamaneurol.2025.2781" target="_blank">Long-term personalized adaptive DBS (2025)</a><br>
<a href="https://doi.org/10.1038/s41531-025-01124-7" target="_blank">Programming strategies in chronic adaptive DBS (2025)</a>
</td>
<td>U8 RQ6に「劣化速度」「再学習間隔候補」を追加し、トレードオフ評価欄を作成します。</td>
<td>担当: 解析/安全WG。前提: 長期フォローアップ体制。完了条件: 最適化方針の事前登録。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="summary">
<h2 class="section-title">Round 4 要約</h2>
<ul>
<li>U8は、臨床エビデンスが増えており、KPI定義を実運用へ落とせる段階です。</li>
<li>特に遅延上限、再較正頻度、フェイルセーフ発動時間は最優先で数値化すべきです。</li>
<li>次の continue では U10/U11 を同形式で深掘りします。</li>
</ul>
</section>

</article>
</main>
