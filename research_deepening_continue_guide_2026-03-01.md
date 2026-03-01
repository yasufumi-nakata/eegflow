---
layout: default
title: "Continue運用ガイド: リサーチクエスチョン深掘り"
description: "continue 指示時に、各問いを網羅的に深掘りするための実行ガイド。"
article_type: "Operations"
subtitle: "60問いの反復調査フロー"
author: Mind Uploading Research Project
last_updated: "2026-03-01"
note: "for iterative deep research"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<section class="section" id="purpose">
<h2 class="section-title">目的</h2>
<p>
このガイドは、ユーザーから <code>continue</code> と指示されたときに、
全リサーチクエスチョンを漏れなく深掘りするための手順を固定するものです。
</p>
</section>

<section class="section" id="assets">
<h2 class="section-title">使用ファイル</h2>
<ul>
<li><code>research_harvest_50.md</code>: 元の問い定義（U0-U15）</li>
<li><code>research_deepening_2026-03-01.md</code>: 平易な追補説明</li>
<li><code>research_deepening_round2_2026-03-01.md</code>: U0/U1/U3 の深掘り追補（Round 2）</li>
<li><code>research_deepening_round3_2026-03-01.md</code>: U4/U7 の深掘り追補（Round 3）</li>
<li><code>research_deepening_round4_2026-03-01.md</code>: U8 の深掘り追補（Round 4）</li>
<li><code>research_deepening_round5_2026-03-01.md</code>: U10/U11/U12 の深掘り追補（Round 5）</li>
<li><code>research_deepening_round6_2026-03-01.md</code>: U13/U14/U15 の深掘り追補（Round 6）</li>
<li><code>research_deepening_round7_2026-03-01.md</code>: U8/U13/U14/U15 の参照精査（Round 7）</li>
<li><code>research_deepening_round8_2026-03-01.md</code>: U8/U13/U14/U15 の参照置換を本体反映（Round 8）</li>
<li><code>research_deepening_round9_2026-03-01.md</code>: U0/U1/U3/U4/U7/U10/U11/U12 の参照置換を本体反映（Round 9）</li>
<li><code>research_deepening_round10_2026-03-01.md</code>: 全60問いの最小コア文献セット（Round 10）</li>
<li><code>research_deepening_round11_2026-03-01.md</code>: U3/U7/U11/U12 の問い別エビデンス追補（Round 11）</li>
<li><code>research_deepening_round12_2026-03-01.md</code>: U0/U1/U4/U8/U10/U13/U14/U15 の問い別エビデンス追補（Round 12）</li>
<li><code>research_deepening_round13_2026-03-01.md</code>: 補助文献品質点検と法制度リンク監査（Round 13）</li>
<li><code>research_deepening_round14_2026-03-01.md</code>: 補助文献 preprint 置換（Round 14）</li>
<li><code>research_deepening_round15_2026-03-01.md</code>: 法制度リンク差分監査（Round 15）</li>
<li><code>research_deepening_round16_2026-03-01.md</code>: 補助文献の実験/規制/運用タグ再分類（Round 16）</li>
<li><code>research_deepening_round17_2026-03-01.md</code>: 参照二層化と3ステップ読了順（Round 17）</li>
<li><code>research_deepening_round18_2026-03-01.md</code>: 読了時間目安と更新監査フラグ（Round 18）</li>
<li><code>research_deepening_round19_2026-03-01.md</code>: U12 規制トラック整合（Round 19）</li>
<li><code>research_deepening_round20_2026-03-01.md</code>: Regulation 法域ラベルと監査優先キュー（Round 20）</li>
<li><code>research_deepening_round21_2026-03-01.md</code>: Highキュー法制度リンク差分監査（Round 21）</li>
<li><code>research_deepening_round22_2026-03-01.md</code>: 本文更新テンプレ固定と改訂履歴リンク補完（Round 22）</li>
<li><code>automation/rq_deepening_backlog_2026-03-01.csv</code>: 全60問いの実行バックログ</li>
<li><code>automation/rq_deepening_backlog_2026-03-01_enriched.csv</code>: 上記 + 一次情報リンク + 根拠確度</li>
<li><code>automation/rq_deepening_progress_round2_2026-03-01.csv</code>: Round 2 進捗管理（U0/U1/U3）</li>
<li><code>automation/rq_deepening_progress_round3_2026-03-01.csv</code>: Round 3 進捗管理（U4/U7）</li>
<li><code>automation/rq_deepening_progress_round4_2026-03-01.csv</code>: Round 4 進捗管理（U8）</li>
<li><code>automation/rq_deepening_progress_round5_2026-03-01.csv</code>: Round 5 進捗管理（U10/U11/U12）</li>
<li><code>automation/rq_deepening_progress_round6_2026-03-01.csv</code>: Round 6 進捗管理（U13/U14/U15）</li>
<li><code>automation/rq_deepening_consistency_audit_2026-03-01.md</code>: 全60問いの整合性監査（coverage missing=0）</li>
<li><code>automation/rq_deepening_coverage_summary_2026-03-01.csv</code>: U別カバレッジ集計</li>
<li><code>automation/rq_reference_relevance_audit_2026-03-01.md</code>: 引用関連性の機械点検（要目視確認）</li>
<li><code>automation/rq_reference_manual_triage_round7_2026-03-01.csv</code>: 高ノイズ比率ユニットの手動トリアージ</li>
<li><code>automation/rq_reference_replacement_applied_round8_2026-03-01.csv</code>: Round 8 の置換適用ログ</li>
<li><code>automation/rq_reference_replacement_applied_round9_2026-03-01.csv</code>: Round 9 の置換適用ログ</li>
<li><code>automation/rq_core_reference_minset_round10_2026-03-01.csv</code>: Round 10 のRQ別最小コア文献セット</li>
<li><code>automation/rq_question_specific_enrichment_round11_2026-03-01.csv</code>: Round 11 の問い別エビデンス追補（22問い）</li>
<li><code>automation/rq_question_specific_enrichment_round12_2026-03-01.csv</code>: Round 12 の問い別エビデンス追補（38問い）</li>
<li><code>automation/rq_supplementary_quality_audit_round13_2026-03-01.csv</code>: Round 13 の補助文献品質点検（60問い）</li>
<li><code>automation/rq_legal_link_freshness_round13_2026-03-01.csv</code>: Round 13 の法制度リンク更新日監査（5件）</li>
<li><code>automation/rq_supplementary_replacement_round14_2026-03-01.csv</code>: Round 14 の補助文献置換ログ（16件）</li>
<li><code>automation/rq_supplementary_quality_audit_round14_2026-03-01.csv</code>: Round 14 の置換後品質点検（60問い）</li>
<li><code>automation/rq_legal_link_freshness_round15_2026-03-01.csv</code>: Round 15 の法制度リンク差分監査（5件）</li>
<li><code>automation/rq_supplementary_thematic_tags_round16_2026-03-01.csv</code>: Round 16 の補助文献タグ再分類（60問い）</li>
<li><code>automation/rq_supplementary_thematic_tag_summary_round16_2026-03-01.csv</code>: Round 16 のタグ集計</li>
<li><code>automation/rq_reference_layering_round17_2026-03-01.csv</code>: Round 17 の参照二層化（60問い）</li>
<li><code>automation/rq_minimal_reading_path_round17_2026-03-01.csv</code>: Round 17 のRQ別3ステップ読了順（60問い）</li>
<li><code>automation/rq_reading_path_summary_round17_2026-03-01.csv</code>: Round 17 の読了順集計</li>
<li><code>automation/rq_reading_path_timed_round18_2026-03-01.csv</code>: Round 18 の時間目安付き読了順（60問い）</li>
<li><code>automation/rq_reading_path_timed_summary_round18_2026-03-01.csv</code>: Round 18 の時間目安集計</li>
<li><code>automation/rq_u12_regulation_alignment_round19_2026-03-01.csv</code>: Round 19 の U12 補助文献再配列ログ（6件）</li>
<li><code>automation/rq_supplementary_thematic_tags_round19_2026-03-01.csv</code>: Round 19 の補助文献タグ再計算（60問い）</li>
<li><code>automation/rq_supplementary_thematic_tag_summary_round19_2026-03-01.csv</code>: Round 19 のタグ集計</li>
<li><code>automation/rq_reference_layering_round19_2026-03-01.csv</code>: Round 19 の参照二層化（60問い）</li>
<li><code>automation/rq_minimal_reading_path_round19_2026-03-01.csv</code>: Round 19 のRQ別3ステップ読了順（60問い）</li>
<li><code>automation/rq_reading_path_summary_round19_2026-03-01.csv</code>: Round 19 の読了順集計</li>
<li><code>automation/rq_reading_path_timed_round19_2026-03-01.csv</code>: Round 19 の時間目安付き読了順（60問い）</li>
<li><code>automation/rq_reading_path_timed_summary_round19_2026-03-01.csv</code>: Round 19 の時間目安集計</li>
<li><code>automation/rq_regulation_jurisdiction_labels_round20_2026-03-01.csv</code>: Round 20 の法域ラベル（U12/U15, 10問い）</li>
<li><code>automation/rq_regulation_update_priority_queue_round20_2026-03-01.csv</code>: Round 20 の更新監査優先キュー（U12/U15, 10問い）</li>
<li><code>automation/rq_regulation_link_diff_round21_2026-03-01.csv</code>: Round 21 のURL単位差分監査（5URL, 差分2件）</li>
<li><code>automation/rq_regulation_priority_queue_status_round21_2026-03-01.csv</code>: Round 21 のRQ単位判定（10問い, 差分判定10件）</li>
<li><code>automation/rq_regulation_content_update_template_round22_2026-03-01.csv</code>: Round 22 のRQ本文更新テンプレ（10問い）</li>
<li><code>automation/rq_regulation_revision_history_links_round22_2026-03-01.csv</code>: Round 22 の制度文書改訂履歴リンク補完（10件）</li>
</ul>
</section>

<section class="section" id="progress">
<h2 class="section-title">進捗（2026-03-01時点）</h2>
<ul>
<li>Round 1: U0-U15 を平易に再整理済み。</li>
<li>Round 2: U0/U1/U3 の全14問いを深掘りし、追加一次情報を紐づけ済み。</li>
<li>Round 3: U4/U7 の全10問いを深掘りし、追加一次情報を紐づけ済み。</li>
<li>Round 4: U8 の全6問いを深掘りし、追加一次情報を紐づけ済み。</li>
<li>Round 5: U10/U11/U12 の全14問いを深掘りし、追加一次情報を紐づけ済み。</li>
<li>Round 6: U13/U14/U15 の全16問いを深掘りし、追加一次情報を紐づけ済み。</li>
<li>Round 7: U8/U13/U14/U15 の疑義文献 32件を手動トリアージし、置換候補を固定済み。</li>
<li>Round 8: U8/U13/U14/U15 の主要先行研究リストを再精査版へ実置換（104件→60件）済み。</li>
<li>Round 9: U0/U1/U3/U4/U7/U10/U11/U12 の主要先行研究リストを再精査版へ実置換（198件→113件）済み。</li>
<li>Round 10: 全60問いへ「必須2本＋補助1本」の最小コア文献セットを割当済み。</li>
<li>Round 11: U3/U7/U11/U12 の22問いで、問い別の必須文献2本を再割当済み。</li>
<li>Round 12: U0/U1/U4/U8/U10/U13/U14/U15 の38問いで、問い別の必須文献2本を再割当済み。</li>
<li>Round 13: 全60問いの補助文献を品質点検し、法制度リンク5件の更新日監査ログを作成済み。</li>
<li>Round 14: grade B（preprint系）16件を査読/仕様系リンクへ実置換し、置換後は grade A=60件を確認済み。</li>
<li>Round 15: 法制度リンク5件の差分監査を実施し、Round 13比で差分なし（status/url/Last-Modified）を確認済み。</li>
<li>Round 16: 全60問いの補助文献へ「実験/規制/運用」タグを付与し、読み分け基準を固定済み。</li>
<li>Round 17: 全60問いで参照を必須/補助の二層に固定し、RQ別3ステップ読了順を生成済み。</li>
<li>Round 18: 全60問いの3ステップ読了順に所要時間目安を追加し、U12/U15（10問い）へ更新監査フラグを付与済み。</li>
<li>Round 19: U12 の補助文献6件を制度文書へ再配列し、タグ/二層化/読了順/時間目安を再計算済み。</li>
<li>Round 20: U12/U15 の regulation-track に法域ラベルを付与し、更新監査優先キューを作成済み。</li>
<li>Round 21: high キュー10問いの法制度リンク差分監査を再実行し、URL差分2件（DOI正規化/OECD正規化）を確認済み。</li>
<li>Round 22: 差分判定を本文更新テンプレへ固定し、制度文書の改訂履歴リンク（EU/CoE/NIST/OECD）を補完済み。</li>
<li>統合反映: research_harvest_50.md 本体へ Round 1-22 結果を統合済み。</li>
<li>整合監査: 全60問いカバレッジ監査と引用関連性点検を生成済み。</li>
<li>次回 continue の優先対象: Round 22 テンプレを使って U12/U15 本文リンクの正規化差分を実反映し、監査導線を本文末尾へ追記。</li>
</ul>
</section>

<section class="section" id="loop">
<h2 class="section-title">continue時の反復フロー</h2>
<ol>
<li>未完了の問いを <code>rq_deepening_backlog_2026-03-01_enriched.csv</code> から抽出します。</li>
<li>各問いについて、一次情報を最低2件追加します（DOI / PubMed / 公式規格）。</li>
<li>「何が分かったか」「何が未解決か」を分離して追記します。</li>
<li>外部依存タスクは、担当者・前提・完了条件を明記して分離します。</li>
<li>差分・検証結果をコミットし、都度 push します。</li>
</ol>
</section>

<section class="section" id="done-criteria">
<h2 class="section-title">1問いの完了条件</h2>
<ul>
<li>一次情報リンクが2件以上あること</li>
<li>評価指標（metric）が定義されていること</li>
<li>このリポジトリで今すぐ実行できる次作業が1件以上あること</li>
<li>外部依存タスクが分離されていること</li>
</ul>
</section>

<section class="section" id="notes">
<h2 class="section-title">注意点</h2>
<ul>
<li>理論先行領域（U10/U12/U13）は、断定ではなく確度ラベルを維持します。</li>
<li>法制度領域（U15）は、必ず最新の公式文書日付を確認します。</li>
<li>計測領域（U1/U7/U8）は、閾値を数値で記録します。</li>
</ul>
</section>

</article>
</main>
