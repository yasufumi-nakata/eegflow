# EEGFlow

マインドアップロード（全脳エミュレーション）に向けたVR×EEG研究の技術的ロードマップと研究計画を体系的にまとめたプロジェクトです。

## 概要

本プロジェクトは、脳-コンピュータインターフェース（BCI）とEEG（脳波）計測技術を中心に、マインドアップロードの実現に向けた5年計画のロードマップを提示します。MECE原則（相互排他的かつ網羅的）に基づき、以下の3つの軸で完全分解しています：

- **脳を測る（Measure）**: 高密度EEG、fMRI、MEGなどの計測技術
- **脳を理解する（Understand）**: デコーディング、シミュレーション、因果推論
- **脳を動かす（Control）**: BCI、ニューロフィードバック、非侵襲刺激

## コンテンツ

### 📄 ドキュメント

- **[index.html](index.html)**: メインのロードマップドキュメント
  - 全体構造とMECE軸での完全分解
  - 計測・理解・制御の各フェーズの詳細
  - 代表的査読研究（APA形式、60件以上）
  - Phase 1-6のフェーズ別ロードマップ（30-50年）
  - 技術的制約の詳細評価（EEG空間分解能、脳梁BMI、記憶転送）
  - 技術スタック・KPI・リスク管理
  - 渡辺正峰方式（シームレス移行アプローチ）の解説
  - 哲学的・倫理的課題（ELSI）
  - **最新文献**: 2023-2024年の最新研究を含む

- **[ELSEVIER_MCP_USAGE.md](ELSEVIER_MCP_USAGE.md)**: Elsevier MCP サーバー使用方法
  - 文献検索のための詳細なガイド
  - Scopus API の使用例
  - 検索クエリの作成方法

### 🛠 スクリプト

- **[scripts/mcp-elsevier.sh](scripts/mcp-elsevier.sh)**: Elsevier MCP サーバー起動用ラッパースクリプト
- **[scripts/elsevier_mcp_server.py](scripts/elsevier_mcp_server.py)**: Elsevier API 文献検索サーバー
  - Scopus/ScienceDirectデータベースの検索
  - 標準ライブラリのみで動作
  - コマンドライン・対話モード対応

### 📁 その他

- **[archive/](archive/)**: 開発過程のドキュメント（参考資料）
  - CRITICAL_GAPS.md: 特定した8つの論理的ギャップ
  - TECHNICAL_CONSTRAINTS.md: 技術的制約の詳細分析
  - SUMMARY_OF_UPDATES.md: 修正内容の完全な記録
  - ELSEVIER_SEARCH_RESULTS.md: 文献検索結果

## 主な特徴

### 1. 体系的なロードマップ

6段階・30-50年のフェーズで構成：

- **Phase 1（Year 1）**: 基盤整備とパイロット検証
- **Phase 2（Year 2-3）**: 大規模データ獲得と深層モデル開発
- **Phase 3（Year 4-5）**: 統合システムと社会実装
- **Phase 3.5（Year 6-10）**: 中規模侵襲実験【新設】
- **Phase 4（Year 11-20）**: 技術統合と初期実証
- **Phase 5（Year 21-30）**: スケールアップと臨床応用
- **Phase 6（Year 31-50）**: 全脳エミュレーション実現

### 2. KPI駆動のアプローチ

各フェーズで明確なKPIを設定：
- **EEG空間分解能**: 浅部15mm、中深度25mm（現実的な物理限界を反映）
- **被験者外AUC**: ≥0.75
- **SSVEP綴り速度**: ≥40 char/min
- **BIDS準拠率**: 100%
- **計算資源**: Phase 3.5で100 TeraFLOPS → Phase 6で1 ExaFLOPS

### 3. 技術スタック

**計測・前処理**
- EEGLAB / MNE-Python
- Lab Streaming Layer (LSL)
- BIDS-EEG

**解析・モデル**
- Braindecode / PyTorch
- MOABB
- HuggingFace Transformers

**制御・BCI**
- PsychoPy / OpenSesame
- OpenViBE / BCI2000

### 4. 豊富な参考文献

60件以上の査読論文をAPA形式で引用、各技術の学術的裏付けを明示しています。
- **最新研究**: 2023-2024年の最新文献を含む
- **技術的制約**: EEG空間分解能、BMI電極技術、記憶エングラムの実証研究

## 使用方法

### ドキュメントの閲覧

```bash
# ブラウザで直接開く
open index.html

# または、簡易HTTPサーバーで確認
python -m http.server 8000
# ブラウザで http://localhost:8000 にアクセス
```

### PDF（SFC論文テンプレ）自動生成（GitHub Actions）

本リポジトリは、SFC修士論文テンプレート（`ymrl/thesis-template`）をCIで取得し、`thesis_content/` の原稿を上書きしてPDFを生成します。

```text
.github/workflows/build-pdf.yml  # CIでPDF生成（artifact: thesis/main.pdf）
thesis_content/                  # テンプレに上書きする原稿（main.texほか）
```

手動実行はGitHubの「Actions」→「Run workflow」で可能です。成果物は`thesis-pdf`という名前でダウンロードできます。

### Elsevier MCPサーバーの使用

文献検索機能を使用する場合：

```bash
# 環境変数の設定
export ELSEVIER_API_KEY="your_api_key_here"
export ELSEVIER_INSTTOKEN="your_institution_token"  # オプション

# サーバーの起動
./scripts/mcp-elsevier.sh
```

または、`.env` ファイルを作成：

```bash
ELSEVIER_API_KEY=your_api_key_here
ELSEVIER_INSTTOKEN=your_institution_token  # オプション
```

## 主なトピック

### マインドアップロードのアプローチ比較

| アプローチ | 自己同一性 | 侵襲性 | 実現時期 |
|-----------|-----------|--------|---------|
| 渡辺方式（シームレス移行） | 連続性維持 | 高侵襲 | ～20年 |
| WBE（全脳エミュレーション） | コピー | 破壊的 | 数十年～世紀 |
| WBA（全脳アーキテクチャ） | 新規AI | 非侵襲 | ～2030年代 |

### EEG研究の貢献領域

1. **高密度計測**: 128ch以上のEEGによるソース推定（誤差≤10mm）
2. **多モーダル統合**: fMRI-EEG同時計測、VR-EEG同期（≤2ms）
3. **デコーディング**: 視覚・言語・運動の表象解読
4. **閉ループ制御**: tACS/tDCS位相同期、適応型BCI

### ELSI（倫理的・法的・社会的課題）

- 自己同一性（テセウスの船問題）
- 社会的不平等（アクセスの格差）
- 法的地位と権利
- ディストピアリスク（悪意ある使用）

## リソース要件

### 予算（年次）
- Phase 1: 約1,500万円
- Phase 2-3: 約2,500万円
- Phase 3-5: 約3,500万円

### 人員
- 研究員・ポスドク
- データサイエンティスト
- 倫理専門家
- プロジェクトマネージャー

### 設備
- 高密度EEGシステム（128ch以上）
- VRヘッドセット（Vive Pro Eye等）
- tACS/tDCS刺激装置
- GPUクラスタ（NVIDIA A100等）

## 関連リンク

### 主要データセット
- [TUH EEG Corpus](https://www.isip.piconepress.com/projects/tuh_eeg/)
- [PhysioNet](https://physionet.org/)
- [OpenNeuro](https://openneuro.org/)
- [BCI Competition](http://www.bbci.de/competition/)

### ツール・フレームワーク
- [EEGLAB](https://sccn.ucsd.edu/eeglab/)
- [MNE-Python](https://mne.tools/)
- [Braindecode](https://braindecode.org/)
- [MOABB](https://github.com/NeuroTechX/moabb)

### 関連組織
- [MinD in a Device](https://www.mindinadevice.com/)
- [全脳アーキテクチャ・イニシアティブ](https://wba-initiative.org/)

## ライセンス

本プロジェクトのドキュメントは教育・研究目的での利用を想定しています。引用する際は適切な出典表記をお願いします。

## 貢献

バグ報告、改善提案、追加研究の提案などは Issue または Pull Request でお願いします。

## 謝辞

本ロードマップは、神経科学、脳波研究、BCI、全脳エミュレーション分野における多数の先行研究に基づいています。詳細な参考文献は `index.html` をご参照ください。

---

**最終更新**: 2025年10月

