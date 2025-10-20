# Elsevier MCP サーバー 使用方法

## 概要

Elsevier API（Scopus、ScienceDirect）を使用して学術文献を検索するためのMCPサーバーです。

## セットアップ

### 1. APIキーの設定

プロジェクトルートに`.env`ファイルを作成（またはターミナルで環境変数を設定）：

```bash
export ELSEVIER_API_KEY="35258dba524c120ebbbc8cb0856e3707"
export ELSEVIER_INSTTOKEN=""  # オプション：機関トークンがあれば設定
```

または、`.env`ファイルを作成：

```bash
ELSEVIER_API_KEY=35258dba524c120ebbbc8cb0856e3707
ELSEVIER_INSTTOKEN=
```

### 2. 依存パッケージのインストール

```bash
pip install requests
```

## 使用方法

### コマンドライン検索

#### Scopus検索

```bash
cd /Users/yasufumi/Documents/GitHub/eegflow

# 環境変数を設定
export ELSEVIER_API_KEY="35258dba524c120ebbbc8cb0856e3707"

# 検索実行
python3 scripts/elsevier_mcp_server.py search "EEG source localization spatial resolution"
```

#### 抽象取得

```bash
python3 scripts/elsevier_mcp_server.py abstract 85123456789
```

### 使用例

#### 例1: EEGソース推定の精度に関する文献検索

```bash
python3 scripts/elsevier_mcp_server.py search "EEG source localization accuracy beamformer LORETA"
```

#### 例2: 記憶エングラム研究の最新動向

```bash
python3 scripts/elsevier_mcp_server.py search "memory engram optogenetics Tonegawa 2023"
```

#### 例3: 脳-コンピュータインターフェースの電極技術

```bash
python3 scripts/elsevier_mcp_server.py search "brain machine interface electrode array Neuralink"
```

#### 例4: 全脳シミュレーションの計算資源

```bash
python3 scripts/elsevier_mcp_server.py search "whole brain simulation computational cost exascale"
```

## 検索のヒント

### 効果的な検索クエリの作成

#### AND演算子（複数キーワードの組み合わせ）

```bash
python3 scripts/elsevier_mcp_server.py search "EEG AND source localization AND accuracy"
```

#### OR演算子（いずれかのキーワード）

```bash
python3 scripts/elsevier_mcp_server.py search "brain computer interface OR brain machine interface"
```

#### 年次指定

```bash
python3 scripts/elsevier_mcp_server.py search "memory engram AND PUBYEAR > 2020"
```

#### 著者名指定

```bash
python3 scripts/elsevier_mcp_server.py search "AUTHOR-NAME(Tonegawa) AND memory"
```

### 論理的ギャップ補強のための検索例

#### ギャップ1: EEG空間分解能の実測精度

```bash
# 高密度EEGの空間分解能
python3 scripts/elsevier_mcp_server.py search "high density EEG 128 channels spatial resolution validation"

# ソース推定アルゴリズムの比較
python3 scripts/elsevier_mcp_server.py search "EEG source localization beamformer sLORETA accuracy comparison"

# 個人頭部モデルの効果
python3 scripts/elsevier_mcp_server.py search "EEG forward model individual MRI source localization"
```

#### ギャップ2: 脳梁BMIの技術仕様

```bash
# 最新のBMI電極技術
python3 scripts/elsevier_mcp_server.py search "brain machine interface electrode density Neuralink Utah array"

# 脳梁への電極埋め込み
python3 scripts/elsevier_mcp_server.py search "corpus callosum electrode recording interhemispheric"

# 軸索再生技術
python3 scripts/elsevier_mcp_server.py search "axonal regeneration central nervous system iPS cells"
```

#### ギャップ3: 記憶転送メカニズム

```bash
# 記憶エングラムの書き込み
python3 scripts/elsevier_mcp_server.py search "artificial memory creation optogenetics hippocampus"

# 記憶のデコーディング
python3 scripts/elsevier_mcp_server.py search "episodic memory decoding fMRI scene reconstruction"

# 分散記憶の統合
python3 scripts/elsevier_mcp_server.py search "distributed memory representation multiple brain regions"
```

#### ギャップ4: 全脳シミュレーション計算資源

```bash
# Human Brain Projectの計算資源
python3 scripts/elsevier_mcp_server.py search "Human Brain Project computational resources exascale"

# ニューロンシミュレーションのスケーリング
python3 scripts/elsevier_mcp_server.py search "whole brain simulation NEURON computational cost"

# Blue Brain Projectの実績
python3 scripts/elsevier_mcp_server.py search "Blue Brain Project neocortical microcircuitry simulation"
```

#### ギャップ5: 被験者外汎化

```bash
# クロスサブジェクトBCI
python3 scripts/elsevier_mcp_server.py search "cross-subject EEG classification transfer learning"

# MOABBベンチマーク
python3 scripts/elsevier_mcp_server.py search "MOABB benchmark EEG motor imagery generalization"

# ドメイン適応
python3 scripts/elsevier_mcp_server.py search "EEG domain adaptation deep learning cross-subject"
```

## 検索結果の解釈

検索結果には以下の情報が含まれます：

- **Title**: 論文タイトル
- **Authors**: 著者名
- **Journal**: 掲載ジャーナル名と出版日
- **Cited by**: 被引用回数（影響度の指標）
- **DOI**: デジタルオブジェクト識別子（論文の一意識別子）
- **Scopus ID**: Scopusデータベース内のID

### 高品質な文献の選定基準

1. **被引用回数が多い**（Cited by > 50）
2. **最近の出版**（2020年以降）
3. **高インパクトジャーナル**（Nature, Science, Cell, PNAS等）
4. **査読済み**（Scopusは基本的に査読済み論文のみ）

## トラブルシューティング

### APIキーエラー

```
ERROR: ELSEVIER_API_KEY is not set.
```

→ 環境変数が設定されていません。`export ELSEVIER_API_KEY="..."`を実行してください。

### API制限エラー

```
Error: 429 Too Many Requests
```

→ APIのレート制限に達しました。しばらく待ってから再試行してください。

Elsevierの無料APIには以下の制限があります：
- 週あたり5,000リクエスト
- 毎秒2リクエスト

### 検索結果がない

```
Total results: 0
```

→ 検索クエリを見直してください：
- キーワードを変更（類義語を試す）
- AND条件を減らす（OR条件を増やす）
- 年次制限を緩和

## 高度な使用方法

### JSON-RPCモード（対話的検索）

```bash
# サーバーを起動
export ELSEVIER_API_KEY="35258dba524c120ebbbc8cb0856e3707"
python3 scripts/elsevier_mcp_server.py

# JSON形式でコマンドを送信
{"type": "search_scopus", "params": {"query": "EEG brain computer interface", "count": 5}}
```

### スクリプトからの使用

```python
import os
from scripts.elsevier_mcp_server import ElsevierMCPServer

api_key = "35258dba524c120ebbbc8cb0856e3707"
server = ElsevierMCPServer(api_key)

# 検索実行
results = server.search_scopus("memory engram optogenetics", count=10)
formatted = server.format_scopus_results(results)
print(formatted)
```

## 参考リンク

- [Elsevier Developer Portal](https://dev.elsevier.com/)
- [Scopus Search API Documentation](https://dev.elsevier.com/documentation/ScopusSearchAPI.wadl)
- [ScienceDirect Search API Documentation](https://dev.elsevier.com/documentation/ScienceDirectSearchAPI.wadl)

---

**最終更新**: 2025年10月19日

