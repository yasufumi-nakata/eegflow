---
layout: default
title: "技術提案書：計測品質・同期・モーション除去・BIDS準拠の統合強化"
description: "Mind-Uploadを研究基盤へ引き上げるための計測QA・同期・解析・標準化の実装提案"
article_type: "Technical Proposal"
subtitle: "Issue #46: Comprehensive Platform Proposal"
author: "mind-upload Project Contributor"
last_updated: "2026-02-10"
note: "Proposal (Draft)"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Abstract</h2>
<p>
本提案は、mind-uploadを実験プロトタイプから再現可能な研究基盤へ引き上げるため、計測品質・同期・アーティファクト除去・BIDS準拠の4軸で整理した技術的拡張案を提示する。
</p>
</div>

<section class="section" id="qa">
<h2 class="section-title">1. 計測QA：ハードウェア品質の可視化</h2>
<ul>
<li><strong>インピーダンス/CMRRの自動監視:</strong> 電極インピーダンスのミスマッチを定量化し、
CMRR劣化を早期警告する。</li>
<li><strong>ノイズフロア測定:</strong> 入力短絡またはファントムヘッドを用いた定期的な基準測定を実装する。</li>
<li><strong>VR干渉チェック:</strong> HMD由来のノイズ帯域を検出し、設定プロファイル化する。</li>
</ul>
</section>

<section class="section" id="sync">
<h2 class="section-title">2. 同期・ジッタ・ドリフト補正</h2>
<ul>
<li><strong>CLETキャリブレーション:</strong> フォトダイオードによりEnd-to-End遅延を測定し、
解析時に補正する。</li>
<li><strong>ジッタ評価:</strong> 平均遅延だけでなく分散（ジッタ）を計測・ログ化する。</li>
<li><strong>クロックドリフト補正:</strong> LSL time_correction を用いた線形補正を標準化する。</li>
</ul>
</section>

<section class="section" id="artifact">
<h2 class="section-title">3. モーションアーティファクト除去</h2>
<ul>
<li><strong>ASR統合:</strong> VR計測のキャリブレーションフェーズを義務化し、ASRパラメータを可視化する。</li>
<li><strong>ICLabel連携:</strong> ICA成分の自動分類で除去の再現性を高める。</li>
<li><strong>センサーフュージョン:</strong> HMDのIMUや視線データを参照信号として適応フィルタリングする。</li>
</ul>
</section>

<section class="section" id="pipelines">
<h2 class="section-title">4. ドメイン特化パイプライン</h2>
<ul>
<li><strong>VR酔い解析:</strong> 低周波指標・スペクトル重心の推移を可視化する。</li>
<li><strong>SSVEP:</strong> CCA/TRCAなど多変量手法を標準化し、短時間窓での識別精度を向上させる。</li>
</ul>
</section>

<section class="section" id="bids">
<h2 class="section-title">5. BIDS / Motion-BIDS 準拠</h2>
<ul>
<li><strong>BIDS-EEG:</strong> メタデータの強制記録（アンプ設定・電極配置・参照方式）。</li>
<li><strong>Motion-BIDS:</strong> VR座標系と神経データの整合を保証する座標系記述を導入する。</li>
</ul>
</section>

<section class="section" id="impact">
<h2 class="section-title">6. 実装への影響</h2>
<ol>
<li><strong>mind-upload/01_preprocess.py:</strong> QA指標とASR/ICLabelの統合を追加。</li>
<li><strong>データ出力:</strong> BIDS-EEGおよびMotion-BIDS対応のメタデータ生成。</li>
<li><strong>同期ツール:</strong> CLET/LSL補正の標準化とログ出力。</li>
</ol>
</section>

</article>
</main>
