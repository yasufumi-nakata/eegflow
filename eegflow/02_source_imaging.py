# eegflow/02_source_imaging.py
#
# 前処理済みのEEGデータを用いて、脳波源推定(EEG Source Imaging)を行います。
# Issue #34の指摘に応え、本スクリプトは単一の解(点推定)を求めるだけでなく、
# その推定の不確実性をどう扱うか、という問題意識をコードレベルで反映します。
#
# このスクリプトの目的:
# 1. BIDS派生データ(derivatives)から前処理済みEEGを読み込む。
# 2. FreeSurferで再構成されたMRI表面モデルを用いて、順問題(Forward Model)を計算する。
# 3. 逆問題(Inverse Problem)を解き、皮質表面上の活動を推定する。
# 4. 点推定(例: MNE/dSPM/sLORETA)と、ベイズ的アプローチの導入可能性について言及する。
#
# 参照:
# - tech_roadmap.html R1, R2: ベイズ的アプローチの重要性
# - Michel & Brunet (2019). EEG Source Imaging: A Practical Review.
#
# 使用ライブラリ:
# - mne-python
# - nilearn (可視化)
# - freesurfer (MRI再構成に必要。このスクリプト実行前に行われている前提)

import mne
import mne_bids
import os.path as op

# --- Configuration ---
BIDS_ROOT = 'bids_dataset'
DERIVATIVES_ROOT = op.join(BIDS_ROOT, 'derivatives', 'eegflow')
FREESURFER_SUBJECTS_DIR = op.join(DERIVATIVES_ROOT, 'freesurfer')

# 解析対象の指定
SUBJECT_ID = '01'
SESSION_ID = '01'
TASK_ID = 'rest'
# ---

def run_source_imaging(subject, session, task):
    """
    指定された被験者のEEGデータに対してソースイメージングを行う。
    """
    # FreeSurferが実行されているか確認
    fs_subject_dir = op.join(FREESURFER_SUBJECTS_DIR, f"sub-{subject}")
    if not op.exists(fs_subject_dir):
        print(f"エラー: FreeSurferディレクトリが見つかりません: {fs_subject_dir}", file=sys.stderr)
        print("このスクリプトを実行する前に、MRIデータに対してFreeSurferの'recon-all'を実行しておく必要があります。", file=sys.stderr)
        return

    # 1. 前処理済みEEGデータの読み込み
    proc_path = mne_bids.BIDSPath(
        subject=subject, session=session, task=task,
        root=DERIVATIVES_ROOT, check=False, suffix='proc-clean_eeg', extension='.fif'
    )
    try:
        raw = mne.io.read_raw_fif(proc_path.fpath, preload=True)
    except FileNotFoundError:
        print(f"エラー: 前処理済みファイルが見つかりません。{proc_path.fpath}", file=sys.stderr)
        print("01_preprocess.py を実行しましたか？")
        return

    # 2. 順問題の計算 (Forward Model)
    #    MRI座標系とEEG座標系の位置合わせ(coregistration)が必要
    #    ここでは手動での位置合わせが完了していると仮定する
    #    `mne.gui.coregistration()`
    trans_path = proc_path.copy().update(suffix='trans', extension='.fif')
    if not op.exists(trans_path.fpath):
        print(f"警告: 位置合わせファイルが見つかりません: {trans_path.fpath}", file=sys.stderr)
        print("正確なソース推定には手動での位置合わせが不可欠です。ダミーのファイルを作成します。", file=sys.stderr)
        # ダミーの変換行列を作成 (あくまで処理を止めないため)
        trans = mne.transforms.Transform('head', 'mri')
        mne.write_trans(trans_path.fpath, trans)
    
    # 順問題の計算に必要なファイルを指定
    src = mne.setup_source_space(f"sub-{subject}", subjects_dir=FREESURFER_SUBJECTS_DIR, add_dist=False)
    bem = mne.make_bem_model(f"sub-{subject}", subjects_dir=FREESURFER_SUBJECTS_DIR)
    bem_sol = mne.make_bem_solution(bem)

    fwd = mne.make_forward_solution(
        raw.info, trans=trans_path.fpath, src=src, bem=bem_sol,
        meg=False, eeg=True, mindist=5.0
    )

    # 3. 逆問題の計算と推定
    # ノイズ共分散行列を計算 (安静時のデータや、課題前のベースライン期間を使う)
    noise_cov = mne.compute_raw_covariance(raw, tmin=0, tmax=10, method='shrunk')
    
    # 逆演算子を作成 (Inverse Operator)
    inverse_operator = mne.minimum_norm.make_inverse_operator(raw.info, fwd, noise_cov)
    
    # ソース推定を実行
    # method='dSPM'は、ノイズ正規化を行うことで深部への感度を改善した手法
    method = "dSPM"
    snr = 3.0
    lambda2 = 1.0 / snr ** 2
    stc = mne.minimum_norm.apply_inverse_raw(raw, inverse_operator, lambda2, method=method)

    # 4. 結果の保存と可視化
    stc_path = proc_path.copy().update(suffix=f'desc-{method}_stc', extension='.stc')
    stc.save(stc_path.fpath, ftype='stc')
    print(f"ソース推定結果を保存しました: {stc_path.fpath}")

    # 脳表面に活動をプロット
    brain = stc.plot(
        subjects_dir=FREESURFER_SUBJECTS_DIR,
        subject=f"sub-{subject}",
        surface="pial",
        hemi="both",
        time_viewer=True
    )
    brain.show_view(azimuth=180, elevation=70)

    # --- Issue #34 に関する考察 ---
    # 上記のdSPMによる推定は、依然として単一の解(点推定)です。
    # tech_roadmap.html (R1, R2)で議論したように、これは科学的に誤解を招く可能性があります。
    #
    # ベイズ的アプローチへの展開:
    # 1. sLORETA/eLORETA: これらも点推定ですが、ベイズ的な枠組みから解釈可能です。
    #    MNEでは `method='eLORETA'` として実装されています。
    #
    # 2. 完全なベイズ推定 (Full Bayesian Estimation):
    #    - MNEには `mne.beamformer.rap_music` のような一部のベイズ的アプローチが実装されています。
    #    - より進んだ手法として、変分ベイズ(Variational Bayes)を用いた解法があります。
    #      (例: "Variational Bayesian identification of dynamic causal models for EEG and MEG", 2008)
    #      これは、分布全体を推定するため、結果の不確実性を直接評価できます。
    #    - このような手法は、現状のMNEエコシステムだけでは完結が難しく、
    #      PyMCやNumPyroのような確率的プログラミング言語との連携が必要になります。
    #
    # EEGFlowの次のステップ:
    # - このスクリプトを拡張し、eLORETAによる推定を追加比較する。
    # - さらに、PyMC等を用いて簡易な変分ベイズソース推定を実装し、その不確実性マップを
    #   dSPM/eLORETAの結果と比較・評価する。
    # --------------------------------

if __name__ == "__main__":
    import sys
    print("="*80)
    print("EEG ソースイメージング (雛形)")
    print("="*80)
    print(f"対象被験者: sub-{SUBJECT_ID}")
    
    if not op.exists(op.join(BIDS_ROOT, 'derivatives')):
         print(f"エラー: BIDS derivatives ディレクトリが見つかりません。", file=sys.stderr)
         print("スクリプト '01_preprocess.py' を実行してください。", file=sys.stderr)
         sys.exit(1)

    run_source_imaging(subject=SUBJECT_ID, session=SESSION_ID, task=TASK_ID)