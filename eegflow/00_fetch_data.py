# eegflow/00_fetch_data.py
#
#
# このスクリプトは、再現可能な解析の基盤となる公開データセットを取得します。
# Issue #34の指摘に基づき、プロジェクトの再現性を担保するための第一歩です。
#
# 推奨データセット:
# OpenNeuro: ds003645 "A multi-modal parcellation of the human cerebral cortex"
# https://openneuro.org/datasets/ds003645
# このデータセットには、安静時fMRI、課題fMRI、拡散MRI、および高密度EEG(128ch)が含まれており、
# 個別化頭部モデル(IHM)の作成からマルチモーダルな解析まで、本プロジェクトの目的に合致しています。
#
# 使用方法:
# 1. openneuro-pyをインストール: `pip install openneuro-py`
# 2. コマンドラインから実行:
#    `openneuro-py download --dataset=ds003645 --target_dir=./bids_dataset`
#
# このスクリプトは、手動でのダウンロードステップを明記し、パイプラインの透明性を確保します。

import os
import subprocess
import sys

# --- Configuration ---
# BIDS準拠のデータセットID (OpenNeuro)
DATASET_ID = "ds003645"
# データセットを保存するディレクトリ
TARGET_DIR = "bids_dataset"
# ---

def check_openneuro_cli():
    """openneuro-pyがインストールされているか確認する"""
    try:
        subprocess.run(["openneuro-py", "--version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def download_dataset():
    """
    OpenNeuroから指定されたデータセットをダウンロードするコマンドを生成・実行する。
    """
    if not check_openneuro_cli():
        print("エラー: 'openneuro-py' が見つかりません。", file=sys.stderr)
        print("次のコマンドでインストールしてください: pip install openneuro-py", file=sys.stderr)
        sys.exit(1)

    # ターゲットディレクトリが存在しない場合は作成
    if not os.path.exists(TARGET_DIR):
        print(f"'{TARGET_DIR}'ディレクトリを作成します...")
        os.makedirs(TARGET_DIR)

    # openneuro-pyのダウンロードコマンドを構築
    command = [
        "openneuro-py",
        "download",
        f"--dataset={DATASET_ID}",
        f"--target_dir={TARGET_DIR}",
        # "--include=sub-01/eeg/*", # 特定のサブジェクトやモダリティのみ取得する場合
    ]

    print("="*80)
    print("再現性のためのデータセット取得")
    print(f"データセット: {DATASET_ID}")
    print(f"保存先:       {TARGET_DIR}")
    print(f"実行コマンド: {' '.join(command)}")
    print("="*80)
    print("\n上記のコマンドをターミナルで実行して、データセットをダウンロードしてください。")
    print("注意: データセットのサイズが大きいため、時間とディスク容量が必要です。")

    # ここではコマンドの実行は行わず、ユーザーに実行を促す
    # 自動実行する場合は、以下のコメントを解除
    #
    # print("ダウンロードを開始します...")
    # try:
    #     process = subprocess.run(command, check=True, text=True)
    #     print("ダウンロードが完了しました。")
    # except subprocess.CalledProcessError as e:
    #     print(f"エラー: ダウンロードに失敗しました。\n{e}", file=sys.stderr)
    #     sys.exit(1)

if __name__ == "__main__":
    download_dataset()
