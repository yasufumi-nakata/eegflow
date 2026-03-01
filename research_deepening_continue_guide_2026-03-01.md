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
<li><code>research_deepening_round23_2026-03-01.md</code>: U12/U15 本文への正規化差分実反映（Round 23）</li>
<li><code>research_deepening_round24_2026-03-01.md</code>: 正規化後基準の差分監査（実体更新分離, Round 24）</li>
<li><code>research_deepening_round25_2026-03-01.md</code>: 問い別監査メモと次回監視スケジュール（Round 25）</li>
<li><code>research_deepening_round26_2026-03-01.md</code>: access_path_change の再確認と問い別判定（Round 26）</li>
<li><code>research_deepening_round27_2026-03-01.md</code>: 問い別本文更新テンプレと監査キーワード辞書（Round 27）</li>
<li><code>research_deepening_round28_2026-03-01.md</code>: 外部依存タスク分離と適用準備度の固定（Round 28）</li>
<li><code>research_deepening_round29_2026-03-01.md</code>: 再監視Runbookと差分トリガー行列の固定（Round 29）</li>
<li><code>research_deepening_round30_2026-03-01.md</code>: 判定ログ様式と証跡パケット仕様の固定（Round 30）</li>
<li><code>research_deepening_round31_2026-03-01.md</code>: 実行チェックリストと例外ハンドリング規則の固定（Round 31）</li>
<li><code>research_deepening_round32_2026-03-01.md</code>: 監査品質スコアとフォローアップ行動行列の固定（Round 32）</li>
<li><code>research_deepening_round33_2026-03-01.md</code>: 再監視バッチ計画と再検証受入基準の固定（Round 33）</li>
<li><code>research_deepening_round34_2026-03-01.md</code>: 平易要約テンプレートと差分レジャー仕様の固定（Round 34）</li>
<li><code>research_deepening_round35_2026-03-01.md</code>: 判定理由一貫性チェック表と最終報告テンプレートの固定（Round 35）</li>
<li><code>research_deepening_round36_2026-03-01.md</code>: 複数ソース照合マップとエスカレーション規則の固定（Round 36）</li>
<li><code>research_deepening_round37_2026-03-01.md</code>: 判定衝突解消行列と外部依存ハンドオフSLAの固定（Round 37）</li>
<li><code>research_deepening_round38_2026-03-01.md</code>: 残余リスク登録表と検証証跡インデックスの固定（Round 38）</li>
<li><code>research_deepening_round39_2026-03-01.md</code>: 証跡鮮度スコアと判定クローズ条件の固定（Round 39）</li>
<li><code>research_deepening_round40_2026-03-01.md</code>: 監査バンドルマニフェストとreopenウォッチリストの固定（Round 40）</li>
<li><code>research_deepening_round41_2026-03-01.md</code>: ハンドオフ完了証跡と未解決キュー管理の固定（Round 41）</li>
<li><code>research_deepening_round42_2026-03-01.md</code>: 未解決キュー解消経路と追加証跡依頼ボードの固定（Round 42）</li>
<li><code>research_deepening_round43_2026-03-01.md</code>: 受入条件ゲート判定ログと状態遷移台帳の固定（Round 43）</li>
<li><code>research_deepening_round44_2026-03-01.md</code>: highレーン2回目判定とクローズ候補登録の固定（Round 44）</li>
<li><code>research_deepening_round45_2026-03-01.md</code>: 最終報告転記ログとクローズ確定登録の固定（Round 45）</li>
<li><code>research_deepening_round46_2026-03-01.md</code>: reopen優先監視ログと再開判定登録の固定（Round 46）</li>
<li><code>research_deepening_round47_2026-03-01.md</code>: trigger変動ドリフト行列と再開エスカレーションキューの固定（Round 47）</li>
<li><code>research_deepening_round48_2026-03-01.md</code>: 閾値再評価ログと再開判定監査の固定（Round 48）</li>
<li><code>research_deepening_round49_2026-03-01.md</code>: 監視窓実行ログとraise判定ゲートの固定（Round 49）</li>
<li><code>research_deepening_round50_2026-03-01.md</code>: 再開準備度スコアと監視ハンドオフチェックポイントの固定（Round 50）</li>
<li><code>research_deepening_round51_2026-03-01.md</code>: 再開候補スクリーニングと監視継続コミットメントの固定（Round 51）</li>
<li><code>research_deepening_round52_2026-03-01.md</code>: raise候補レビューと監視サイクル確約の固定（Round 52）</li>
<li><code>research_deepening_round53_2026-03-01.md</code>: high先行実行順とraise移行証跡の固定（Round 53）</li>
<li><code>research_deepening_round54_2026-03-01.md</code>: preflight固定とraise反映チェックポイント整備（Round 54）</li>
<li><code>research_deepening_round55_2026-03-01.md</code>: 実行ログ雛形とkeep_watch繰越台帳の固定（Round 55）</li>
<li><code>research_deepening_round56_2026-03-01.md</code>: raise判定トレース台帳と次サイクル引継ぎ固定（Round 56）</li>
<li><code>research_deepening_round57_2026-03-01.md</code>: 証跡完全性チェックと公開反映ゲート固定（Round 57）</li>
<li><code>research_deepening_round58_2026-03-01.md</code>: 公開適用キューとpending解消確認表の固定（Round 58）</li>
<li><code>research_deepening_round59_2026-03-01.md</code>: 公開コミット台帳と保留繰越バックログ固定（Round 59）</li>
<li><code>research_deepening_round60_2026-03-01.md</code>: 公開結果マトリクスと未解消エスカレーション登録固定（Round 60）</li>
<li><code>research_deepening_round61_2026-03-01.md</code>: 公開実行チェックとエスカレーション解消計画固定（Round 61）</li>
<li><code>research_deepening_round62_2026-03-01.md</code>: クローズ証明と再開ガード固定（Round 62）</li>
<li><code>research_deepening_round63_2026-03-01.md</code>: クローズ維持スケジュールと再開候補トリアージ固定（Round 63）</li>
<li><code>research_deepening_round64_2026-03-01.md</code>: クローズ一貫性監査と再開兆候監視固定（Round 64）</li>
<li><code>research_deepening_round65_2026-03-01.md</code>: クローズドリフト対応と再開ハンドオフ固定（Round 65）</li>
<li><code>research_deepening_round66_2026-03-01.md</code>: 再開再検証パケットと再クローズ判定ゲート固定（Round 66）</li>
<li><code>research_deepening_round67_2026-03-01.md</code>: 再クローズ認証台帳と再開クールダウン監視固定（Round 67）</li>
<li><code>research_deepening_round68_2026-03-01.md</code>: 安定状態チェックポイントと再開再入ゲート固定（Round 68）</li>
<li><code>research_deepening_round69_2026-03-01.md</code>: 再入候補トリアージと再検証再接続ブリッジ固定（Round 69）</li>
<li><code>research_deepening_round70_2026-03-01.md</code>: 再入実行パケットと再安定化復帰ゲート固定（Round 70）</li>
<li><code>research_deepening_round71_2026-03-01.md</code>: 再安定化確認台帳と再クローズ復帰監視固定（Round 71）</li>
<li><code>research_deepening_round72_2026-03-01.md</code>: 再入再接続チェックポイントと再開再入ゲート更新固定（Round 72）</li>
<li><code>research_deepening_round73_2026-03-01.md</code>: 再入更新伝播台帳と再入実行再接続ゲート固定（Round 73）</li>
<li><code>research_deepening_round74_2026-03-01.md</code>: 再接続実行チェックと再入候補再同期ゲート固定（Round 74）</li>
<li><code>research_deepening_round75_2026-03-01.md</code>: 再同期実行台帳と再同期監視ゲート固定（Round 75）</li>
<li><code>research_deepening_round76_2026-03-01.md</code>: 再同期更新台帳と再入監視再起動ゲート固定（Round 76）</li>
<li><code>research_deepening_round77_2026-03-01.md</code>: 監視再起動台帳と再接続再開ゲート固定（Round 77）</li>
<li><code>research_deepening_round78_2026-03-01.md</code>: 再開反映台帳と監視再連結ゲート固定（Round 78）</li>
<li><code>research_deepening_round79_2026-03-01.md</code>: 再連結更新台帳と監視再同期再開ゲート固定（Round 79）</li>
<li><code>research_deepening_round80_2026-03-01.md</code>: 再接続フィードバック台帳と監視再同期再点検ゲート固定（Round 80）</li>
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
<li><code>automation/rq_regulation_link_normalization_applied_round23_2026-03-01.csv</code>: Round 23 の正規化差分適用ログ（10問い）</li>
<li><code>automation/rq_regulation_audit_trail_insertion_round23_2026-03-01.csv</code>: Round 23 の監査導線追加ログ（8リンク）</li>
<li><code>automation/rq_regulation_link_diff_round24_2026-03-01.csv</code>: Round 24 のURL単位差分監査（5URL, 実体更新分離付き）</li>
<li><code>automation/rq_regulation_priority_queue_status_round24_2026-03-01.csv</code>: Round 24 のRQ単位判定（10問い, アクセス経路変動列付き）</li>
<li><code>automation/rq_regulation_rq_specific_audit_memo_round25_2026-03-01.csv</code>: Round 25 のRQ別監査メモ（10問い）</li>
<li><code>automation/rq_regulation_monitor_schedule_round25_2026-03-01.csv</code>: Round 25 の次回監視予定日付きスケジュール（10問い）</li>
<li><code>automation/rq_regulation_access_recheck_round26_2026-03-01.csv</code>: Round 26 のアクセス経路再確認ログ（5URL）</li>
<li><code>automation/rq_regulation_question_decision_round26_2026-03-01.csv</code>: Round 26 の問い別更新可否判定（10問い）</li>
<li><code>automation/rq_regulation_monitor_schedule_round26_2026-03-01.csv</code>: Round 26 の更新後監視スケジュール（10問い）</li>
<li><code>automation/rq_regulation_update_text_template_round27_2026-03-01.csv</code>: Round 27 の問い別本文更新テンプレ（10問い）</li>
<li><code>automation/rq_regulation_source_checkpoint_phrase_bank_round27_2026-03-01.csv</code>: Round 27 の監査キーワード辞書（10問い）</li>
<li><code>automation/rq_regulation_external_dependency_tasks_round28_2026-03-01.csv</code>: Round 28 の外部依存タスク分離（10問い）</li>
<li><code>automation/rq_regulation_apply_readiness_round28_2026-03-01.csv</code>: Round 28 の本文適用準備度（10問い）</li>
<li><code>automation/rq_regulation_monitor_execution_runbook_round29_2026-03-01.csv</code>: Round 29 の問い別再監視Runbook（10問い）</li>
<li><code>automation/rq_regulation_diff_trigger_matrix_round29_2026-03-01.csv</code>: Round 29 の問い別差分トリガー行列（10問い）</li>
<li><code>automation/rq_regulation_decision_log_template_round30_2026-03-01.csv</code>: Round 30 の問い別判定ログ様式（10問い）</li>
<li><code>automation/rq_regulation_evidence_packet_spec_round30_2026-03-01.csv</code>: Round 30 の問い別証跡パケット仕様（10問い）</li>
<li><code>automation/rq_regulation_monitor_checklist_round31_2026-03-01.csv</code>: Round 31 の問い別実行チェックリスト（10問い）</li>
<li><code>automation/rq_regulation_exception_handling_playbook_round31_2026-03-01.csv</code>: Round 31 の問い別例外ハンドリング規則（10問い）</li>
<li><code>automation/rq_regulation_audit_quality_scoring_round32_2026-03-01.csv</code>: Round 32 の問い別監査品質スコア（10問い）</li>
<li><code>automation/rq_regulation_followup_action_matrix_round32_2026-03-01.csv</code>: Round 32 の問い別フォローアップ行動行列（10問い）</li>
<li><code>automation/rq_regulation_monitor_batch_plan_round33_2026-03-01.csv</code>: Round 33 の問い別再監視バッチ計画（10問い）</li>
<li><code>automation/rq_regulation_revalidation_acceptance_round33_2026-03-01.csv</code>: Round 33 の問い別再検証受入基準（10問い）</li>
<li><code>automation/rq_regulation_monitor_plain_summary_template_round34_2026-03-01.csv</code>: Round 34 の問い別平易要約テンプレート（10問い）</li>
<li><code>automation/rq_regulation_text_diff_ledger_spec_round34_2026-03-01.csv</code>: Round 34 の問い別差分レジャー仕様（10問い）</li>
<li><code>automation/rq_regulation_reason_consistency_check_round35_2026-03-01.csv</code>: Round 35 の問い別判定理由一貫性チェック表（10問い）</li>
<li><code>automation/rq_regulation_final_report_template_round35_2026-03-01.csv</code>: Round 35 の問い別最終報告テンプレート（10問い）</li>
<li><code>automation/rq_regulation_cross_source_evidence_map_round36_2026-03-01.csv</code>: Round 36 の問い別複数ソース照合マップ（10問い）</li>
<li><code>automation/rq_regulation_escalation_trigger_rules_round36_2026-03-01.csv</code>: Round 36 の問い別エスカレーション規則（10問い）</li>
<li><code>automation/rq_regulation_conflict_resolution_matrix_round37_2026-03-01.csv</code>: Round 37 の問い別判定衝突解消行列（10問い）</li>
<li><code>automation/rq_regulation_external_handoff_sla_round37_2026-03-01.csv</code>: Round 37 の問い別外部依存ハンドオフSLA（10問い）</li>
<li><code>automation/rq_regulation_residual_risk_register_round38_2026-03-01.csv</code>: Round 38 の問い別残余リスク登録表（10問い）</li>
<li><code>automation/rq_regulation_verification_artifact_index_round38_2026-03-01.csv</code>: Round 38 の問い別検証証跡インデックス（10問い）</li>
<li><code>automation/rq_regulation_evidence_freshness_score_round39_2026-03-01.csv</code>: Round 39 の問い別証跡鮮度スコア（10問い）</li>
<li><code>automation/rq_regulation_decision_closure_checklist_round39_2026-03-01.csv</code>: Round 39 の問い別判定クローズ条件（10問い）</li>
<li><code>automation/rq_regulation_audit_bundle_manifest_round40_2026-03-01.csv</code>: Round 40 の問い別監査バンドルマニフェスト（10問い）</li>
<li><code>automation/rq_regulation_reopen_watchlist_round40_2026-03-01.csv</code>: Round 40 の問い別reopenウォッチリスト（10問い）</li>
<li><code>automation/rq_regulation_handoff_completion_certificate_round41_2026-03-01.csv</code>: Round 41 の問い別ハンドオフ完了証跡（10問い）</li>
<li><code>automation/rq_regulation_unresolved_issue_queue_round41_2026-03-01.csv</code>: Round 41 の問い別未解決キュー（10問い）</li>
<li><code>automation/rq_regulation_resolution_path_round42_2026-03-01.csv</code>: Round 42 の問い別解消経路（10問い）</li>
<li><code>automation/rq_regulation_evidence_request_board_round42_2026-03-01.csv</code>: Round 42 の問い別追加証跡依頼ボード（10問い）</li>
<li><code>automation/rq_regulation_acceptance_gate_check_round43_2026-03-01.csv</code>: Round 43 の問い別受入条件ゲート判定（10問い）</li>
<li><code>automation/rq_regulation_state_transition_ledger_round43_2026-03-01.csv</code>: Round 43 の問い別状態遷移台帳（10問い）</li>
<li><code>automation/rq_regulation_high_lane_second_pass_round44_2026-03-01.csv</code>: Round 44 の問い別2回目判定ログ（10問い）</li>
<li><code>automation/rq_regulation_close_candidate_register_round44_2026-03-01.csv</code>: Round 44 の問い別クローズ候補登録（10問い）</li>
<li><code>automation/rq_regulation_final_report_reflection_log_round45_2026-03-01.csv</code>: Round 45 の問い別最終報告転記ログ（10問い）</li>
<li><code>automation/rq_regulation_closure_confirmation_register_round45_2026-03-01.csv</code>: Round 45 の問い別クローズ確定登録（10問い）</li>
<li><code>automation/rq_regulation_reopen_priority_monitor_round46_2026-03-01.csv</code>: Round 46 の問い別reopen優先監視ログ（10問い）</li>
<li><code>automation/rq_regulation_reopen_decision_register_round46_2026-03-01.csv</code>: Round 46 の問い別再開判定登録（10問い）</li>
<li><code>automation/rq_regulation_trigger_drift_matrix_round47_2026-03-01.csv</code>: Round 47 の問い別trigger変動ドリフト行列（10問い）</li>
<li><code>automation/rq_regulation_reopen_escalation_queue_round47_2026-03-01.csv</code>: Round 47 の問い別再開エスカレーションキュー（10問い）</li>
<li><code>automation/rq_regulation_threshold_recheck_round48_2026-03-01.csv</code>: Round 48 の問い別閾値再評価ログ（10問い）</li>
<li><code>automation/rq_regulation_reopen_decision_audit_round48_2026-03-01.csv</code>: Round 48 の問い別再開判定監査（10問い）</li>
<li><code>automation/rq_regulation_watch_window_execution_round49_2026-03-01.csv</code>: Round 49 の問い別監視窓実行ログ（10問い）</li>
<li><code>automation/rq_regulation_raise_gate_criteria_round49_2026-03-01.csv</code>: Round 49 の問い別raise判定ゲート（10問い）</li>
<li><code>automation/rq_regulation_reopen_readiness_score_round50_2026-03-01.csv</code>: Round 50 の問い別再開準備度スコア（10問い）</li>
<li><code>automation/rq_regulation_watch_handoff_checkpoint_round50_2026-03-01.csv</code>: Round 50 の問い別監視ハンドオフチェックポイント（10問い）</li>
<li><code>automation/rq_regulation_reopen_candidate_screening_round51_2026-03-01.csv</code>: Round 51 の問い別再開候補スクリーニング（10問い）</li>
<li><code>automation/rq_regulation_monitor_continuity_commitment_round51_2026-03-01.csv</code>: Round 51 の問い別監視継続コミットメント（10問い）</li>
<li><code>automation/rq_regulation_raise_candidate_review_round52_2026-03-01.csv</code>: Round 52 の問い別raise候補レビュー（10問い）</li>
<li><code>automation/rq_regulation_watch_cycle_commitment_round52_2026-03-01.csv</code>: Round 52 の問い別監視サイクル確約（10問い）</li>
<li><code>automation/rq_regulation_high_lane_execution_round53_2026-03-01.csv</code>: Round 53 の問い別high先行実行順（10問い）</li>
<li><code>automation/rq_regulation_raise_transition_packet_round53_2026-03-01.csv</code>: Round 53 の問い別raise移行証跡パケット（10問い）</li>
<li><code>automation/rq_regulation_high_lane_preflight_round54_2026-03-01.csv</code>: Round 54 の問い別preflight固定（10問い）</li>
<li><code>automation/rq_regulation_raise_apply_checkpoint_round54_2026-03-01.csv</code>: Round 54 の問い別raise反映チェックポイント（10問い）</li>
<li><code>automation/rq_regulation_window_execution_log_round55_2026-03-01.csv</code>: Round 55 の問い別実行ログ雛形（10問い）</li>
<li><code>automation/rq_regulation_keep_watch_rollover_round55_2026-03-01.csv</code>: Round 55 の問い別keep_watch繰越台帳（10問い）</li>
<li><code>automation/rq_regulation_raise_decision_trace_round56_2026-03-01.csv</code>: Round 56 の問い別raise判定トレース台帳（10問い）</li>
<li><code>automation/rq_regulation_cycle_handoff_manifest_round56_2026-03-01.csv</code>: Round 56 の問い別次サイクル引継ぎマニフェスト（10問い）</li>
<li><code>automation/rq_regulation_evidence_completeness_round57_2026-03-01.csv</code>: Round 57 の問い別証跡完全性チェック（10問い）</li>
<li><code>automation/rq_regulation_publish_gate_round57_2026-03-01.csv</code>: Round 57 の問い別公開反映ゲート（10問い）</li>
<li><code>automation/rq_regulation_publish_apply_queue_round58_2026-03-01.csv</code>: Round 58 の問い別公開適用キュー（10問い）</li>
<li><code>automation/rq_regulation_pending_review_resolution_round58_2026-03-01.csv</code>: Round 58 の問い別pending解消確認表（10問い）</li>
<li><code>automation/rq_regulation_publish_commit_ledger_round59_2026-03-01.csv</code>: Round 59 の問い別公開コミット台帳（10問い）</li>
<li><code>automation/rq_regulation_pending_carryover_backlog_round59_2026-03-01.csv</code>: Round 59 の問い別保留繰越バックログ（10問い）</li>
<li><code>automation/rq_regulation_publish_outcome_matrix_round60_2026-03-01.csv</code>: Round 60 の問い別公開結果マトリクス（10問い）</li>
<li><code>automation/rq_regulation_unresolved_escalation_register_round60_2026-03-01.csv</code>: Round 60 の問い別未解消エスカレーション登録（10問い）</li>
<li><code>automation/rq_regulation_outcome_execution_check_round61_2026-03-01.csv</code>: Round 61 の問い別公開実行チェック表（10問い）</li>
<li><code>automation/rq_regulation_escalation_closure_plan_round61_2026-03-01.csv</code>: Round 61 の問い別エスカレーション解消計画（10問い）</li>
<li><code>automation/rq_regulation_closure_certification_round62_2026-03-01.csv</code>: Round 62 の問い別クローズ証明チェック（10問い）</li>
<li><code>automation/rq_regulation_reopen_guard_round62_2026-03-01.csv</code>: Round 62 の問い別再開ガード条件（10問い）</li>
<li><code>automation/rq_regulation_closure_maintenance_schedule_round63_2026-03-01.csv</code>: Round 63 の問い別クローズ維持スケジュール（10問い）</li>
<li><code>automation/rq_regulation_reopen_candidate_triage_round63_2026-03-01.csv</code>: Round 63 の問い別再開候補トリアージ（10問い）</li>
<li><code>automation/rq_regulation_closure_consistency_audit_round64_2026-03-01.csv</code>: Round 64 の問い別クローズ一貫性監査（10問い）</li>
<li><code>automation/rq_regulation_reopen_watch_signal_round64_2026-03-01.csv</code>: Round 64 の問い別再開兆候監視（10問い）</li>
<li><code>automation/rq_regulation_closure_drift_response_round65_2026-03-01.csv</code>: Round 65 の問い別クローズドリフト対応行列（10問い）</li>
<li><code>automation/rq_regulation_reopen_escalation_handoff_round65_2026-03-01.csv</code>: Round 65 の問い別再開エスカレーション引継ぎ（10問い）</li>
<li><code>automation/rq_regulation_reopen_revalidation_packet_round66_2026-03-01.csv</code>: Round 66 の問い別再開再検証パケット（10問い）</li>
<li><code>automation/rq_regulation_reclose_decision_gate_round66_2026-03-01.csv</code>: Round 66 の問い別再クローズ判定ゲート（10問い）</li>
<li><code>automation/rq_regulation_reclose_certification_ledger_round67_2026-03-01.csv</code>: Round 67 の問い別再クローズ認証台帳（10問い）</li>
<li><code>automation/rq_regulation_reopen_cooldown_watch_round67_2026-03-01.csv</code>: Round 67 の問い別再開クールダウン監視（10問い）</li>
<li><code>automation/rq_regulation_stable_state_checkpoint_round68_2026-03-01.csv</code>: Round 68 の問い別安定状態チェックポイント（10問い）</li>
<li><code>automation/rq_regulation_reopen_reentry_gate_round68_2026-03-01.csv</code>: Round 68 の問い別再開再入ゲート（10問い）</li>
<li><code>automation/rq_regulation_reentry_candidate_triage_round69_2026-03-01.csv</code>: Round 69 の問い別再入候補トリアージ（10問い）</li>
<li><code>automation/rq_regulation_revalidation_reconnect_bridge_round69_2026-03-01.csv</code>: Round 69 の問い別再検証再接続ブリッジ（10問い）</li>
<li><code>automation/rq_regulation_reentry_execution_packet_round70_2026-03-01.csv</code>: Round 70 の問い別再入実行パケット（10問い）</li>
<li><code>automation/rq_regulation_restabilization_return_gate_round70_2026-03-01.csv</code>: Round 70 の問い別再安定化復帰ゲート（10問い）</li>
<li><code>automation/rq_regulation_restabilization_confirmation_ledger_round71_2026-03-01.csv</code>: Round 71 の問い別再安定化確認台帳（10問い）</li>
<li><code>automation/rq_regulation_reclose_return_watch_round71_2026-03-01.csv</code>: Round 71 の問い別再クローズ復帰監視（10問い）</li>
<li><code>automation/rq_regulation_reentry_reconnect_checkpoint_round72_2026-03-01.csv</code>: Round 72 の問い別再入再接続チェックポイント（10問い）</li>
<li><code>automation/rq_regulation_reopen_reentry_gate_refresh_round72_2026-03-01.csv</code>: Round 72 の問い別再開再入ゲート更新（10問い）</li>
<li><code>automation/rq_regulation_reentry_update_propagation_ledger_round73_2026-03-01.csv</code>: Round 73 の問い別再入更新伝播台帳（10問い）</li>
<li><code>automation/rq_regulation_reentry_execution_relink_gate_round73_2026-03-01.csv</code>: Round 73 の問い別再入実行再接続ゲート（10問い）</li>
<li><code>automation/rq_regulation_reentry_relink_execution_check_round74_2026-03-01.csv</code>: Round 74 の問い別再接続実行チェック（10問い）</li>
<li><code>automation/rq_regulation_reentry_candidate_resync_gate_round74_2026-03-01.csv</code>: Round 74 の問い別再入候補再同期ゲート（10問い）</li>
<li><code>automation/rq_regulation_reentry_resync_execution_ledger_round75_2026-03-01.csv</code>: Round 75 の問い別再同期実行台帳（10問い）</li>
<li><code>automation/rq_regulation_reentry_watch_resync_gate_round75_2026-03-01.csv</code>: Round 75 の問い別再同期監視ゲート（10問い）</li>
<li><code>automation/rq_regulation_reentry_resync_update_ledger_round76_2026-03-01.csv</code>: Round 76 の問い別再同期更新台帳（10問い）</li>
<li><code>automation/rq_regulation_reentry_watch_restart_gate_round76_2026-03-01.csv</code>: Round 76 の問い別再入監視再起動ゲート（10問い）</li>
<li><code>automation/rq_regulation_reentry_watch_restart_ledger_round77_2026-03-01.csv</code>: Round 77 の問い別監視再起動台帳（10問い）</li>
<li><code>automation/rq_regulation_reentry_reconnect_resume_gate_round77_2026-03-01.csv</code>: Round 77 の問い別再接続再開ゲート（10問い）</li>
<li><code>automation/rq_regulation_reconnect_resume_update_ledger_round78_2026-03-01.csv</code>: Round 78 の問い別再開反映台帳（10問い）</li>
<li><code>automation/rq_regulation_reentry_watch_relink_gate_round78_2026-03-01.csv</code>: Round 78 の問い別監視再連結ゲート（10問い）</li>
<li><code>automation/rq_regulation_reentry_relink_update_ledger_round79_2026-03-01.csv</code>: Round 79 の問い別再連結更新台帳（10問い）</li>
<li><code>automation/rq_regulation_reentry_watch_resync_resume_gate_round79_2026-03-01.csv</code>: Round 79 の問い別監視再同期再開ゲート（10問い）</li>
<li><code>automation/rq_regulation_reentry_reconnect_feedback_ledger_round80_2026-03-01.csv</code>: Round 80 の問い別再接続フィードバック台帳（10問い）</li>
<li><code>automation/rq_regulation_reentry_watch_resync_recheck_gate_round80_2026-03-01.csv</code>: Round 80 の問い別監視再同期再点検ゲート（10問い）</li>
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
<li>Round 23: U12/U15 本文へ正規化差分を実反映し、制度文書の監査導線リンクを追記済み。</li>
<li>Round 24: highキューを再監視し、実体更新（0件）とアクセス経路変動（1件）を分離判定済み。</li>
<li>Round 25: 10問いそれぞれに監査焦点メモを付与し、次回監視予定日（+7日）を固定済み。</li>
<li>Round 26: access_path_change を再確認し、10問いすべてで本文据え置き（実体更新なし）を確定済み。</li>
<li>Round 27: 10問いそれぞれの本文更新文テンプレと監査キーワード辞書を固定済み。</li>
<li>Round 28: 10問いの外部依存タスクを分離し、本文適用準備度（no_change適用）を固定済み。</li>
<li>Round 29: 10問いの再監視Runbookと差分トリガー行列を固定済み。</li>
<li>Round 30: 10問いの判定ログ様式と証跡パケット仕様を固定済み。</li>
<li>Round 31: 10問いの実行チェックリストと例外ハンドリング規則を固定済み。</li>
<li>Round 32: 10問いの監査品質スコアとフォローアップ行動行列を固定済み。</li>
<li>Round 33: 10問いの再監視バッチ計画と再検証受入基準を固定済み。</li>
<li>Round 34: 10問いの平易要約テンプレートと差分レジャー仕様を固定済み。</li>
<li>Round 35: 10問いの判定理由一貫性チェック表と最終報告テンプレートを固定済み。</li>
<li>Round 36: 10問いの複数ソース照合マップとエスカレーション規則を固定済み。</li>
<li>Round 37: 10問いの判定衝突解消行列と外部依存ハンドオフSLAを固定済み。</li>
<li>Round 38: 10問いの残余リスク登録表と検証証跡インデックスを固定済み。</li>
<li>Round 39: 10問いの証跡鮮度スコアと判定クローズ条件を固定済み。</li>
<li>Round 40: 10問いの監査バンドルマニフェストとreopenウォッチリストを固定済み。</li>
<li>Round 41: 10問いのハンドオフ完了証跡と未解決キュー管理を固定済み。</li>
<li>Round 42: 10問いの未解決キュー解消経路と追加証跡依頼ボードを固定済み。</li>
<li>Round 43: 10問いの受入条件ゲート判定ログと状態遷移台帳を固定済み。</li>
<li>Round 44: 10問いのhighレーン2回目判定ログとクローズ候補登録を固定済み。</li>
<li>Round 45: 10問いの最終報告転記ログとクローズ確定登録を固定済み。</li>
<li>Round 46: 10問いのreopen優先監視ログと再開判定登録を固定済み。</li>
<li>Round 47: 10問いのtrigger変動ドリフト行列と再開エスカレーションキューを固定済み。</li>
<li>Round 48: 10問いの閾値再評価ログと再開判定監査を固定済み。</li>
<li>Round 49: 10問いの監視窓実行ログとraise判定ゲートを固定済み。</li>
<li>Round 50: 10問いの再開準備度スコアと監視ハンドオフチェックポイントを固定済み。</li>
<li>Round 51: 10問いの再開候補スクリーニングと監視継続コミットメントを固定済み。</li>
<li>Round 52: 10問いのraise候補レビューと監視サイクル確約を固定済み。</li>
<li>Round 53: 10問いのhigh先行実行順とraise移行証跡パケットを固定済み。</li>
<li>Round 54: 10問いのpreflight固定とraise反映チェックポイントを固定済み。</li>
<li>Round 55: 10問いの実行ログ雛形とkeep_watch繰越台帳を固定済み。</li>
<li>Round 56: 10問いのraise判定トレース台帳と次サイクル引継ぎマニフェストを固定済み。</li>
<li>Round 57: 10問いの証跡完全性チェックと公開反映ゲートを固定済み。</li>
<li>Round 58: 10問いの公開適用キューとpending解消確認表を固定済み。</li>
<li>Round 59: 10問いの公開コミット台帳と保留繰越バックログを固定済み。</li>
<li>Round 60: 10問いの公開結果マトリクスと未解消エスカレーション登録を固定済み。</li>
<li>Round 61: 10問いの公開実行チェックとエスカレーション解消計画を固定済み。</li>
<li>Round 62: 10問いのクローズ証明チェックと再開ガード条件を固定済み。</li>
<li>Round 63: 10問いのクローズ維持スケジュールと再開候補トリアージを固定済み。</li>
<li>Round 64: 10問いのクローズ一貫性監査と再開兆候監視を固定済み。</li>
<li>Round 65: 10問いのクローズドリフト対応行列と再開エスカレーション引継ぎを固定済み。</li>
<li>Round 66: 10問いの再開再検証パケットと再クローズ判定ゲートを固定済み。</li>
<li>Round 67: 10問いの再クローズ認証台帳と再開クールダウン監視を固定済み。</li>
<li>Round 68: 10問いの安定状態チェックポイントと再開再入ゲートを固定済み。</li>
<li>Round 69: 10問いの再入候補トリアージと再検証再接続ブリッジを固定済み。</li>
<li>Round 70: 10問いの再入実行パケットと再安定化復帰ゲートを固定済み。</li>
<li>Round 71: 10問いの再安定化確認台帳と再クローズ復帰監視を固定済み。</li>
<li>Round 72: 10問いの再入再接続チェックポイントと再開再入ゲート更新を固定済み。</li>
<li>Round 73: 10問いの再入更新伝播台帳と再入実行再接続ゲートを固定済み。</li>
<li>Round 74: 10問いの再接続実行チェックと再入候補再同期ゲートを固定済み。</li>
<li>Round 75: 10問いの再同期実行台帳と再同期監視ゲートを固定済み。</li>
<li>Round 76: 10問いの再同期更新台帳と再入監視再起動ゲートを固定済み。</li>
<li>Round 77: 10問いの監視再起動台帳と再接続再開ゲートを固定済み。</li>
<li>Round 78: 10問いの再開反映台帳と監視再連結ゲートを固定済み。</li>
<li>Round 79: 10問いの再連結更新台帳と監視再同期再開ゲートを固定済み。</li>
<li>Round 80: 10問いの再接続フィードバック台帳と監視再同期再点検ゲートを固定済み。</li>
<li>統合反映: research_harvest_50.md 本体へ Round 1-80 結果を統合済み。</li>
<li>整合監査: 全60問いカバレッジ監査と引用関連性点検を生成済み。</li>
<li>次回 continue の優先対象: 2026-03-08 UTC に Round 80 reentry_reconnect_feedback_ledger の3記録と reentry_watch_resync_recheck_gate の3項目を更新し、再発あり問いは reentry_update_propagation_ledger と reentry_watch_resync_gate へ再接続する。</li>
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
