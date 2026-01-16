# eegflow/03_causal_modeling.py
#
# ソースレベルの脳活動データを用いて、脳領域間の有効結合性を推定し、
# 生成モデル(Generative Model)を構築することを目指します。
# Issue #34で言及されている Active Inference の実装に向けた重要なステップです。
#
# このスクリプトの目的 (概念実証):
# 1. ソース推定された時系列データ(STC)を読み込む。
# 2. 事前に定義された関心領域(ROI)に時系列をまとめる(Parcellation)。
# 3. 動的因果モデリング(DCM)やその他の因果推論アプローチの適用方法について概説する。
#
# Active Inferenceへの接続:
# DCMによって同定された生成モデルは、Fristonの自由エネルギー原理(FEP)における
# 「世界のモデル」に相当します。このモデルを用いて、エージェントが予測誤差を
# 最小化するように行動選択(Active Inference)するシミュレーションに繋げることが、
# 本プロジェクトの長期的目標です。
#
# 使用ライブラリ:
# - mne-python
# - nilearn
# - (将来的には) SPM (MATLAB) のPythonラッパー (例: `pyspm`) や、
#   PyMC/NumPyroを用いたカスタムDCM実装が考えられる。

import mne
import mne_bids
import os.path as op
import numpy as np

# --- Configuration ---
BIDS_ROOT = 'bids_dataset'
DERIVATIVES_ROOT = op.join(BIDS_ROOT, 'derivatives', 'eegflow')
FREESURFER_SUBJECTS_DIR = op.join(DERIVATIVES_ROOT, 'freesurfer')

# 解析対象の指定
SUBJECT_ID = '01'
METHOD = 'dSPM' # 02_source_imaging.pyで指定した手法
# ---

def extract_roi_time_series(subject, method):
    """
    ソース推定結果(STC)と皮質アトラスを用いて、ROIごとの時系列を抽出する。
    """
    # 1. ソース推定結果の読み込み
    stc_path = mne_bids.BIDSPath(
        subject=subject, session='01', task='rest', root=DERIVATIVES_ROOT,
        check=False, suffix=f'desc-{method}_stc', extension='.stc'
    )
    try:
        stc = mne.read_source_estimate(stc_path.fpath)
    except FileNotFoundError:
        print(f"エラー: ソース推定ファイルが見つかりません。{stc_path.fpath}", file=sys.stderr)
        print("02_source_imaging.py を実行しましたか？")
        return None

    # 2. 皮質アトラス(Parcellation)の取得
    #    ここではFreeSurferにデフォルトで含まれる'aparc'アトラスを使用
    parc = 'aparc'
    labels = mne.read_labels_from_annot(
        f"sub-{subject}", parc=parc, subjects_dir=FREESURFER_SUBJECTS_DIR
    )
    
    # ラベルから 'unknown' を除去
    labels = [label for label in labels if 'unknown' not in label.name]

    # 3. ROI時系列の抽出
    label_ts = mne.extract_label_time_course(
        stc, labels, stc.src, mode='mean_flip', allow_empty=True
    )
    
    label_names = [label.name for label in labels]
    print(f"抽出されたROIの数: {len(label_names)}")
    print(f"抽出された時系列データの形状: {label_ts.shape}")

    return label_ts, label_names


def conceptual_dcm_workflow():
    """
    DCMを適用するための概念的なワークフローを示す。
    """
    print("\n--- 動的因果モデリング (DCM) の概念的ワークフロー ---")
    print("DCMは、観測された脳活動データ(Y)を、状態方程式(f)と観測方程式(g)で説明するモデルです。")
    print("Y = g(x) + ε  (観測方程式)")
    print("dx/dt = f(x, u, θ) + ω  (状態方程式)\n")
    print("目的: データYから、モデルパラメータθ(結合強度など)の事後確率を推定する。")
    
    # 1. モデル空間の定義
    print("\n[ステップ1: モデル空間の定義]")
    print("どの領域が、どの領域に、どのように結合しているか、という仮説を複数立てます。")
    print("例: モデルA「V1→V5」、モデルB「V1↔V5」")

    # 2. モデル推定
    print("\n[ステップ2: モデル推定]")
    print("各モデルについて、ベイズ推定(変分ベイズなど)を用いてモデルエビデンスを計算します。")
    print("SPMのDCMはMATLABベースですが、Pythonから呼び出す方法や、Pythonでの再実装も研究されています。")

    # 3. モデル比較
    print("\n[ステップ3: モデル比較]")
    print("ベイズ的モデル比較(BMS)を用いて、データをもっともよく説明するモデルを選択します。")
    print("これにより、「V1からV5への一方的な結合が優勢である」といった結論が得られます。")
    
    # 4. Active Inferenceへの展開
    print("\n[ステップ4: Active Inferenceへの展開]")
    print("同定された生成モデル f(x, u, θ) は、エージェントの「内部世界モデル」となります。")
    print("このモデルを持つエージェントが、将来の予測誤差(自由エネルギー)を最小化するために、")
    print("どのような行動(u)や知覚(g)を選択するかをシミュレーションするのがActive Inferenceです。")
    print("--------------------------------------------------")


if __name__ == "__main__":
    import sys
    print("="*80)
    print("因果モデリングと生成モデル (概念実証)")
    print("="*80)
    
    if not op.exists(op.join(BIDS_ROOT, 'derivatives')):
         print(f"エラー: BIDS derivatives ディレクトリが見つかりません。", file=sys.stderr)
         print("スクリプト '02_source_imaging.py' を実行してください。", file=sys.stderr)
         sys.exit(1)

    # ROI時系列を抽出
    label_ts, label_names = extract_roi_time_series(subject=SUBJECT_ID, method=METHOD)
    
    if label_ts is not None:
        # DCMの概念的ワークフローを説明
        conceptual_dcm_workflow()