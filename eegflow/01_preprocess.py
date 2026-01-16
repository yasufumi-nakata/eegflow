# eegflow/01_preprocess.py
#
# BIDS準拠のEEGデータに対して、標準的な前処理パイプラインを適用します。
# Issue #34の指摘に基づき、再現可能な解析パイプラインの雛形として作成。
#
# このスクリプトの目的:
# 1. BIDSパス構造を利用して、対象の被験者データを発見する。
# 2. MNE-Pythonを用いて、フィルタリング、リファレンス設定、ICAによるアーチファクト除去を行う。
# 3. 前処理済みのデータをBIDS派生データ(derivatives)として保存する。
# 4. 品質の悪いデータを特定・除外するためのレポートを生成する。
#
# 使用ライブラリ:
# - mne-python
# - mne-bids

import mne
import mne_bids
import os.path as op

# --- Configuration ---
BIDS_ROOT = 'bids_dataset'
DERIVATIVES_ROOT = op.join(BIDS_ROOT, 'derivatives', 'eegflow')

# 解析対象の指定
SUBJECT_ID = '01'
SESSION_ID = '01'
TASK_ID = 'rest'
# ---

def preprocess_subject(subject, session, task):
    """
    指定された被験者・セッション・タスクのEEGデータを前処理する。
    """
    # 1. BIDSデータの読み込み
    bids_path = mne_bids.BIDSPath(
        subject=subject,
        session=session,
        task=task,
        suffix='eeg',
        extension='.bdf', # データセットに合わせた拡張子
        root=BIDS_ROOT
    )

    print(f"BIDS Path: {bids_path}")
    try:
        raw = mne_bids.read_raw_bids(bids_path, verbose=False)
    except FileNotFoundError:
        print(f"エラー: データファイルが見つかりません。{bids_path.fpath}", file=sys.stderr)
        print("00_fetch_data.py を実行して、データをダウンロードしましたか？")
        return

    # 2. 基本的な前処理
    # チャンネル位置情報の設定
    raw.set_montage('standard_1005', on_missing='warn')

    # フィルタリング (1.0 Hz High-pass, 40.0 Hz Low-pass)
    raw.filter(l_freq=1.0, h_freq=40.0, fir_design='firwin', verbose=False)

    # ノッチフィルタ (50Hzまたは60Hzの電源ラインノイズを除去)
    raw.notch_filter(freqs=60.0, fir_design='firwin', verbose=False)

    # リファレンス再設定 (Average reference)
    raw.set_eeg_reference('average', projection=True, verbose=False)

    # 3. ICAによるアーチファクト除去
    ica = mne.preprocessing.ICA(n_components=20, random_state=42)
    ica.fit(raw, tstep=1.0, reject_by_annotation=True)

    # EOG/ECGアーチファクトを自動検出
    # データにEOG/ECGチャンネルがない場合は、手動で成分を選択する必要がある
    try:
        eog_indices, eog_scores = ica.find_bads_eog(raw)
        ica.exclude.extend(eog_indices)
        print(f"ICA: EOG成分を{len(eog_indices)}個検出しました。")
    except Exception as e:
        print(f"警告: EOG成分の自動検出に失敗しました。 {e}")
        # ここで `ica.plot_sources(raw)` を呼び出して手動選択を促すことができる

    # ICAを適用
    ica.apply(raw)

    # 4. 前処理済みデータの保存
    # BIDS派生データとしての保存パスを構築
    output_path = bids_path.copy().update(
        root=DERIVATIVES_ROOT,
        check=False,
        suffix='proc-clean_eeg' # BIDS-Appの規約に準拠
    )
    if not op.exists(output_path.directory):
        output_path.directory.mkdir(parents=True)

    raw.save(output_path.fpath, overwrite=True)
    print(f"前処理済みデータを保存しました: {output_path.fpath}")

    # 5. 品質管理レポートの生成
    report = mne.Report(title=f"Preprocessing Report for sub-{subject}")
    report.add_raw(raw, title="Raw Data", psd=True)
    report.add_ica(ica, title="ICA Components", inst=raw)
    report_path = output_path.copy().update(suffix='report', extension='.html')
    report.save(report_path.fpath, overwrite=True)
    print(f"品質管理レポートを生成しました: {report_path.fpath}")

if __name__ == '__main__':
    # 実際には、ループで複数の被験者を処理することが多い
    # for subject in ['01', '02', ...]:
    #     preprocess_subject(subject, ...)
    import sys

    print("="*80)
    print("EEG 前処理パイプライン (雛形)")
    print("="*80)
    print(f"対象被験者: sub-{SUBJECT_ID}")
    print(f"BIDS Root: {BIDS_ROOT}")
    print(f"Derivatives: {DERIVATIVES_ROOT}")
    print("-" * 80)

    if not op.exists(BIDS_ROOT):
         print(f"エラー: BIDSルートディレクトリ '{BIDS_ROOT}' が見つかりません。", file=sys.stderr)
         print("スクリプト '00_fetch_data.py' を実行してデータをダウンロードしてください。", file=sys.stderr)
         sys.exit(1)

    preprocess_subject(subject=SUBJECT_ID, session=SESSION_ID, task=TASK_ID)