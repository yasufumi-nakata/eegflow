---
layout: default
title: "FAQ：よくある質問（と、よくある事故）"
description: "Mind-Uploadを読んでいて出やすい疑問に、短く正確に答えます。"
article_type: FAQ
subtitle: "派手な結論より、検証できる前進を"
author: Mind Uploading Research Project
last_updated: "2026-02-10"
note: "Human-first"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>How To Read</h2>
<p>
ここは「よくある勘違い」を先に避けるためのページです。主張が大きいほど、(1)言葉の定義、(2)評価の物差し、(3)間違いと判定する条件、(4)再現手順の順で確認します。
</p>
</div>

<section class="section" id="q0">
<h2 class="section-title">Q. Mind-Uploadは結局、何をするサイト？</h2>
<p>
A. マインドアップロード/WBEを「検証可能な研究プログラム」に寄せるための<strong>検証基盤（Verification Commons）</strong>を作るサイトです。
データ（入力）、評価（出力）、ルール（達成条件/反証条件）、運用（継続）を先に固定します。
</p>
<div class="cta-box">
<h4>Start</h4>
<p>全体像はここから。</p>
<a href="verification.html">検証基盤を見る →</a>
</div>
</section>

<section class="section" id="q1">
<h2 class="section-title">Q. EEGで“思考”は読める？</h2>
<p>
A. 「何をどこまで」と定義しない限り答えられません。EEGはノイズと個体差が大きく、言語モデルも尤もらしい文を補完するため、EEG由来情報とモデル補完を反事実テストで分離する手順を先に固定します。
</p>
<p>
Mind-Uploadの立場は、「派手な読み出し」を否定するのではなく、<strong>検証可能な主張に落とす</strong>ことです（失敗例まで含む）。
</p>
</section>

<section class="section" id="q2">
<h2 class="section-title">Q. decode（デコーディング）と emulate（エミュレーション）の違いは？</h2>
<p>
A. decodeは“観測を翻訳する”ことで、emulateは“内部状態が時間発展し、介入に反応し、出力を生成する”ことです。
WBEに近づくには、後者を評価できるベンチマーク（介入・反事実・閉ループ）へ寄せる必要があります。
</p>
<p><a href="wbe_101.html">入門（WBE 101）</a>と<a href="glossary.html">用語集</a>が近道です。</p>
</section>

<section class="section" id="q3">
<h2 class="section-title">Q. じゃあ、何を作れば“前進”になる？</h2>
<p>
A. まずは L0〜L2 が現実的です。つまり「再現できる解析」「比較できるベンチ」「介入予測で検証できるモデル」です。
Mind-Uploadでは、これを“サイトとして運用できる形”に落とします（テンプレ・ログ・ルール）。
</p>
<div class="key-points">
<h4>具体的な成果物</h4>
<ul>
<li><strong>入力：</strong>BIDS/EEG-BIDS + メタデータ + QCログ</li>
<li><strong>手順：</strong>固定パイプライン + 実行ログ + 失敗例</li>
<li><strong>出力：</strong>指標（スコア） + ベースライン差分 + 反証条件の結果</li>
</ul>
</div>
</section>

<section class="section" id="q4">
<h2 class="section-title">Q. なぜ“標準化”がそんなに大事？</h2>
<p>
A. 標準がないと、同じことを言っているようで違う入力・違う手順・違う指標を比較してしまい、進捗が見えなくなります。
PDBやBIDS+OpenNeuroなどの事例は、分野が違っても「前進を測れる」状態を作った点が共通しています。
</p>
<p><a href="casework.html">ケースワーク集</a>に、設計の型をまとめています。</p>
</section>

<section class="section" id="q5">
<h2 class="section-title">Q. “ベンチマークの罠”って何？</h2>
<p>
A. 指標に勝つことが、現実の目的達成とズレる現象です（Goodhartの罠）。
例えば、データリークや過学習でスコアだけ上がる、実装コストが高すぎて実運用されない、などがあります。
Mind-Uploadでは、失敗例・リーク検査・モデルカードを含めて運用設計します。
</p>
</section>

<section class="section" id="q6">
<h2 class="section-title">Q. 意識の「ハードプロブレム」に対するスタンスは？</h2>
<p>
A. Mind-Uploadは、ハードプロブレム（Chalmers, 1995）について特定の哲学的立場を前提にしません。
機能主義的アプローチを実装基盤として採用しますが、それが現象的意識の十分条件であるとは主張しません。
代わりに、<strong>検証可能な操作的指標</strong>（PCI-ST、反事実テスト、介入応答一致等）を評価基準とし、
哲学的帰結は結果の解釈段階で議論する立場を取ります。
</p>
<div class="note-box">
<strong>透明性</strong>
<p>
これは重大な制約です。機能的等価性が確認されても、現象的意識の同一性は保証されません。
この限界を明示した上で、測定可能な前進を積み上げます。
</p>
</div>
</section>

<section class="section" id="q7">
<h2 class="section-title">Q. コピー問題（分身のパラドックス）をどう扱う？</h2>
<p>
A. 「スキャン＆コピー」方式では、コピー直後にオリジナルとコピーが独立に分岐するため、
どちらが「本人」かは原理的に決定できません（パーフィットの心理的連続性理論）。
Mind-Uploadでは、<strong>Slow Continuous Mind Uploading</strong>（段階的移行）を主軸に据え、
分断を伴わないプロセスの連続性を工学的要件として設計します。
ただし、この戦略も「どの時点で移行が完了したか」の判定基準を事前に固定する必要があり、
これはクレーム階段 L4 の課題として扱います。
</p>
</section>

<section class="section" id="q8">
<h2 class="section-title">Q. IITとGNWTの実験的検証はどうなった？</h2>
<p>
A. 2025年のCogitate Consortium（敵対的共同研究）が、IITとGNWTの予測を大規模に検証しました。
結果は<strong>双方とも完全には支持されなかった</strong>：IITの後方皮質持続活動は部分的支持のみ、
GNWTの前頭前野イグニッションは報告動作と分離困難でした。
Mind-Uploadではこの結果を受け、特定理論への固執を避け、PCI等の理論非依存な経験的指標を中心に据えています。
</p>
</section>

<section class="section" id="q9">
<h2 class="section-title">Q. 倫理的課題はどう扱っている？</h2>
<p>
A. WBEは固有の倫理的課題を伴います：(1) エミュレートされた存在の法的地位と権利、
(2) 同意の撤回可能性（停止する権利）、(3) 複製による多重人格の倫理、
(4) アクセス格差と社会的公正。Mind-Uploadでは、技術的検証と並行して、
<strong>倫理的レビュー委員会の設計</strong>をクレーム階段 L5（社会実装）の前提条件として位置づけています。
現時点では技術的基盤（L0-L2）に集中していますが、L3以降の計画には倫理ガバナンスの設計を含みます。
</p>
</section>

<section class="section" id="q10">
<h2 class="section-title">Q. 他のWBEプロジェクトとの違いは？</h2>
<p>
A. 主な既存プロジェクトとの位置づけ：
</p>
<ul>
<li><strong>Blue Brain / Human Brain Project：</strong>大規模シミュレーション重視。Mind-Uploadは検証基盤設計を先行させる点が異なる。</li>
<li><strong>全脳アーキテクチャ・イニシアティブ（WBAI）：</strong>構成論的・ロードマップ重視。Mind-Uploadはベンチマークと反証条件を先に固定する点が補完的。</li>
<li><strong>OpenWorm：</strong>C. elegans全コネクトーム実装。Mind-Uploadはヒト脳の非侵襲計測（EEG）からのアプローチ。</li>
</ul>
<p>
Mind-Uploadの差別化点は、<strong>「検証基盤（Verification Commons）を先に作る」</strong>という戦略です。
</p>
</section>

<section class="section" id="references">
<h2 class="section-title">参考文献（FAQ）</h2>
<ol>
<li>Tang, J., et al. (2023). Semantic reconstruction from non-invasive brain recordings. <a href="https://doi.org/10.1038/s41593-023-01304-9" target="_blank">doi:10.1038/s41593-023-01304-9</a></li>
<li>Ji, Z., et al. (2023). Survey of Hallucination in NLG. <a href="https://doi.org/10.1145/3571730" target="_blank">doi:10.1145/3571730</a></li>
<li>Correa, J. D., Lee, S., &amp; Bareinboim, E. (2021). Nested Counterfactual Identification. <a href="https://arxiv.org/abs/2107.03190" target="_blank">arXiv:2107.03190</a></li>
<li>Gorgolewski, K. J., et al. (2016). BIDS. <a href="https://doi.org/10.1038/sdata.2016.44" target="_blank">doi:10.1038/sdata.2016.44</a></li>
<li>Pernet, C. R., et al. (2019). EEG-BIDS. <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">doi:10.1038/s41597-019-0104-8</a></li>
<li>Casali, A. G., et al. (2013). PCI. <a href="https://doi.org/10.1126/scitranslmed.3006294" target="_blank">doi:10.1126/scitranslmed.3006294</a></li>
<li>Chalmers, D. J. (1995). Facing up to the problem of consciousness. <em>Journal of Consciousness Studies</em>, 2(3), 200-219.</li>
<li>Parfit, D. (1984). <em>Reasons and Persons</em>. Oxford University Press.</li>
</ol>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>Shortcuts</h4>
<ul>
<li><a href="index.html">Start →</a></li>
<li><a href="verification.html">Verification →</a></li>
<li><a href="wbe_101.html">WBE 101 →</a></li>
<li><a href="eeg_101.html">EEG 101 →</a></li>
<li><a href="datasets.html">Datasets →</a></li>
<li><a href="glossary.html">Glossary →</a></li>
</ul>
</div>

</aside>
</main>
