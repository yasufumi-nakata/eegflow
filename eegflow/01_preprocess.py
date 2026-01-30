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
import json
import numpy as np

# New modules
try:
    from . import quality
    from . import signal_processing
except ImportError:
    # Fallback if running as script
    import quality
    import signal_processing

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

    # --- Initial Quality Checks (Proposal Section 2) ---
    print("\n--- Step 1: Initial Quality Assurance ---")
    
    # 2.1 Impedance Check (if data available)
    # Note: BDF/BrainVision sometimes stores impedance in separate file, 
    # here we check if it's in raw.info (rare) or skip.
    # Placeholder for demonstration
    # impedances = {'Fz': 5000, 'Cz': 12000} # Mock
    # quality.check_impedance_balance(impedances)
    
    # 2.2 SNR Estimation
    snr = quality.estimate_snr(raw)
    print(f"Estimated SNR (Delta): {snr.get('Delta', 'N/A')} dB")

    # 2.3 HMD Interference
    has_interference, hmd_details = quality.detect_hmd_interference(raw, refresh_rate=90.0)
    if has_interference:
        print(f"Potential HMD Interference detected. Suggesting Notch at {hmd_details['suggested_notch']} Hz")


    # 2. 基本的な前処理
    # チャンネル位置情報の設定
    raw.set_montage('standard_1005', on_missing='warn')

    # フィルタリング (1.0 Hz High-pass)
    # High-pass is needed for ICA and ASR
    raw.filter(l_freq=1.0, h_freq=None, fir_design='firwin', verbose=False)

    # ノッチフィルタ (Line noise + HMD noise)
    notch_freqs = [60.0]
    if has_interference:
        notch_freqs.append(hmd_details['suggested_notch'])
    
    raw.notch_filter(freqs=notch_freqs, fir_design='firwin', verbose=False)

    # リファレンス再設定 (Average reference)
    raw.set_eeg_reference('average', projection=True, verbose=False)

    # --- Advanced Artifact Removal (Proposal Section 4) ---
    print("\n--- Step 2: Advanced Artifact Removal ---")

    # 4.1 Artifact Subspace Reconstruction (ASR)
    # Low-pass filter is usually done before ASR or handled within
    # Issue #57: Use Riemannian geometry for better artifact rejection and data-driven thresholding
    raw_asr = signal_processing.apply_asr(raw, sfreq=raw.info['sfreq'], cutoff=20.0, method='riemann')
    
    # Low-pass after ASR (optional, but good for clean data)
    raw_asr.filter(l_freq=None, h_freq=40.0, verbose=False)


    # 3. ICAによるアーチファクト除去
    print("\n--- Step 3: ICA & ICLabel ---")
    ica = mne.preprocessing.ICA(n_components=20, random_state=42)
    ica.fit(raw_asr, tstep=1.0, reject_by_annotation=True)

    # 4.3 ICA Automatic Classification (ICLabel)
    # This replaces manual EOG finding or augments it
    ic_labels = signal_processing.apply_iclabel_classification(raw_asr, ica)
    
    # Exclude components classified as 'eye' or 'muscle' with high probability
    exclude_idx = []
    if ic_labels:
        for i, label in enumerate(ic_labels['labels']):
            prob = ic_labels['y_pred_proba'][i]
            if label in ['eye', 'muscle'] and prob > 0.8:
                exclude_idx.append(i)
        
        ica.exclude.extend(exclude_idx)
        print(f"ICLabel: Automatically excluded {len(exclude_idx)} components.")
    else:
        # Fallback to legacy EOG detection
        try:
            eog_indices, eog_scores = ica.find_bads_eog(raw_asr)
            ica.exclude.extend(eog_indices)
        except Exception:
            pass

    # ICAを適用
    ica.apply(raw_asr)

    # --- Specialized Analysis (Proposal Section 5) ---
    print("\n--- Step 4: Specialized VR Analysis ---")
    
    # 5.1 Barycenter Frequency (VR Sickness Biomarker)
    barycenter = signal_processing.calculate_barycenter_frequency(raw_asr)
    print(f"Spectral Barycenter (4-13Hz): {barycenter:.2f} Hz")


    # 4. 前処理済みデータの保存
    # BIDS派生データとしての保存パスを構築
    output_path = bids_path.copy().update(
        root=DERIVATIVES_ROOT,
        check=False,
        suffix='proc-clean_eeg' # BIDS-Appの規約に準拠
    )
    if not op.exists(output_path.directory):
        output_path.directory.mkdir(parents=True)

    raw_asr.save(output_path.fpath, overwrite=True)
    print(f"前処理済みデータを保存しました: {output_path.fpath}")

    # 5. 品質管理レポートの生成
    report = mne.Report(title=f"Preprocessing Report for sub-{subject}")
    report.add_raw(raw_asr, title="Cleaned Data", psd=True)
    report.add_ica(ica, title="ICA Components", inst=raw) # Use original raw for ICA viz
    report_path = output_path.copy().update(suffix='report', extension='.html')
    report.save(report_path.fpath, overwrite=True)
    print(f"品質管理レポートを生成しました: {report_path.fpath}")

    # 6. QCメトリクスの保存 (JSON) - Issue #34/M8 Update
    # Issue #45: 神経修飾系（Brainstem amine systems）の活動プロキシ
    # （瞳孔径、心拍変動など）をメタデータ要件として追加。
    qc_metrics = {
        "subject": subject,
        "session": session,
        "task": task,
        "processing_stage": "01_preprocess",
        "n_channels": len(raw_asr.ch_names),
        "sfreq": raw_asr.info['sfreq'],
        "duration_sec": raw_asr.times[-1],
        "ica_excluded_components": [int(x) for x in ica.exclude],
        "snr_estimates": snr,
        "hmd_interference_detected": has_interference,
        "barycenter_freq": barycenter,
        "neuromodulation_proxies": {
            "pupil_diameter": None, # To be implemented (Issue #45)
            "heart_rate_variability": None # To be implemented (Issue #45)
        },
        "filter_params": {
            "l_freq": 1.0,
            "h_freq": 40.0,
            "notch": notch_freqs
        }
    }
    
    qc_path = output_path.copy().update(suffix='qc', extension='.json')
    with open(qc_path.fpath, 'w') as f:
        json.dump(qc_metrics, f, indent=2)
    print(f"QCメトリクスを保存しました: {qc_path.fpath}")

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