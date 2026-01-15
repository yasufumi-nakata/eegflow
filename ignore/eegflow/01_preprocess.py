# EEGFlow: 01_preprocess.py
#
# このスクリプトは、BIDS (Brain Imaging Data Structure) 形式のEEGデータを
# MNE-Python を用いて前処理するための最小限のパイプラインを示します。
#
# This script demonstrates a minimal preprocessing pipeline for BIDS-formatted
# EEG data using MNE-Python.
#
# GitHub Issue #21で指摘された「コードベースの欠如」という批判に応え、
# プロジェクトの実体性と再現性を示すために作成されました。
#
# Created to address the "lack of codebase" critique in GitHub Issue #21
# and to demonstrate the project's substance and commitment to reproducibility.

import mne
from mne_bids import BIDSPath, read_raw_bids

# --- 1. BIDSデータセットのパスを設定 ---
# --- 1. Set up BIDS dataset paths ---
# BIDSのルートディレクトリ、被験者ID、タスク名などを指定します。
# Specify the BIDS root directory, subject ID, task name, etc.
bids_root = 'path/to/your/bids_dataset'
subject = '01'
session = '01'
task = 'rest'
run = '01'

# BIDSPathオブジェクトを作成
# Create a BIDSPath object
bids_path = BIDSPath(subject=subject, session=session, task=task, run=run,
                     root=bids_root, suffix='eeg', extension='.vhdr')


# --- 2. 生データの読み込み ---
# --- 2. Load raw data ---
# BIDSパスから生データを読み込みます。
# Load raw data from the BIDS path.
# try-exceptブロックは、実際のデータがない場合にエラーを防ぐためのものです。
# The try-except block is to prevent errors when no actual data is present.
try:
    raw = read_raw_bids(bids_path=bids_path, verbose=False)
    raw.load_data()
except Exception as e:
    print(f"ダミーデータを作成します。Could not load real data: {e}")
    print("Creating dummy data instead.")
    # ダミーデータを作成
    # Create dummy data
    sfreq = 250
    ch_names = ['Fp1', 'Fp2', 'Fz', 'Cz', 'Pz', 'O1', 'O2', 'M1']
    info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types='eeg')
    data = mne.filter.create_filter(None, sfreq, l_freq=1, h_freq=40)
    n_times = sfreq * 10 # 10 seconds
    dummy_data = data[:, :n_times] * 1e-6
    raw = mne.io.RawArray(dummy_data, info)


# --- 3. 前処理 ---
# --- 3. Preprocessing ---

# 3.1. チャンネルの種類の再設定 (必要に応じて)
# 3.1. Re-setting channel types (if necessary)
# EOGやECGチャンネルを正しく設定します。
# Set EOG or ECG channels correctly.
# raw.set_channel_types({'HEOG': 'eog', 'VEOG': 'eog', 'ECG': 'ecg'})

# 3.2. バンドパスフィルタ
# 3.2. Band-pass filtering
# 一般的な周波数帯域 (例: 1-40 Hz) でフィルタリングします。
# Filter the data in a common frequency band (e.g., 1-40 Hz).
raw.filter(l_freq=1., h_freq=40., fir_design='firwin')

# 3.3. ノッチフィルタ
# 3.3. Notch filtering
# 電源ラインのノイズ (50Hz or 60Hz) を除去します。
# Remove power line noise (50Hz or 60Hz).
raw.notch_filter(freqs=60.0)

# 3.4. リファレンスの再設定
# 3.4. Re-referencing
# 例えば、平均リファレンスに設定します。
# For example, set to average reference.
raw.set_eeg_reference('average', projection=True)
print("Applied average reference.")

# 3.5. ICA (独立成分分析) によるアーティファクト除去
# 3.5. Artifact removal with ICA (Independent Component Analysis)
# 瞬き (EOG) や心拍 (ECG) などのアーティファクトを特定し、除去します。
# Identify and remove artifacts like blinks (EOG) and heartbeats (ECG).
ica = mne.preprocessing.ICA(n_components=8, random_state=97, max_iter=800)
ica.fit(raw)

# アーティファクト成分を特定 (この例では自動検出)
# Identify artifact components (here using automated detection)
# eog_indices, eog_scores = ica.find_bads_eog(raw)
# ica.exclude = eog_indices
# print(f"ICA: Found {len(eog_indices)} EOG components to exclude.")

# ICAを適用
# Apply ICA
# ica.apply(raw)


# --- 4. エポック化 ---
# --- 4. Epoching ---
# 連続データを特定のイベントに関連するエポックに分割します。
# Segment the continuous data into epochs related to specific events.
# events = mne.find_events(raw, stim_channel='Stim')
# event_id = {'stimulus': 1}
# tmin, tmax = -0.2, 0.5  # seconds
# epochs = mne.Epochs(raw, events, event_id, tmin, tmax, preload=True)

print("Preprocessing steps outlined.")


# --- 5. 前処理済みデータの保存 ---
# --- 5. Save preprocessed data ---
# 結果を -epo.fif 形式で保存するのが一般的です。
# It is common practice to save the result in -epo.fif format.
# output_path = bids_path.copy().update(suffix='epo', extension='.fif', check=False)
# epochs.save(output_path, overwrite=True)
# print(f"Preprocessed data saved to: {output_path}")

print("\nEEGFlow - 01_preprocess.py script finished.")
print("This script provides a conceptual pipeline. It should be adapted for a specific dataset and research question.")
