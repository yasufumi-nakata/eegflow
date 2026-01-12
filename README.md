# EEGFlow

マインドアップロード実現のための中核となるコアサイト。

## 目的

このサイトは、マインドアップロードの実現に向けた技術・研究・コミュニティの中心的ハブとなることを目指しています。

ここでいうマインドアップロードとは、**意識や記憶の交換・複製を可能とする技術**を指します。

## 今後の展望

本プロジェクトは、最終的にサイトの更新や運用プロセスを完全に自動化することを目指しています。現在は手動で行っているタスクも、順次自動化ツールやCI/CDパイプラインへ移行する予定です。

## データ標準と再現性 (Data Standards and Reproducibility)

本プロジェクトは、神経科学研究における再現可能性を最重要視します。その実現のため、以下の標準とツールを導入、または導入を計画しています。

- **BIDS (Brain Imaging Data Structure)**: データとメタデータはBIDS 1.9.0標準に準拠します。これにより、データの構造的な一貫性を保ち、共有と再利用を促進します。
- **BIDS-Validator**: データセットがBIDS標準に準拠していることを検証するためのバリデーションツールをCI/CDパイプラインに統合する予定です。
- **BIDS-App準拠パイプライン**: 解析の再現性を確保するため、[EEG-BIDS-Clean](https://github.com/sappelhoff/eeg-bids-clean) のようなBIDS-App準拠の解析パイプラインの導入を計画しています。これにより、標準化された手順でデータの前処理や解析を実行できます。

## 倫理とプライバシー保護 (Ethics and Privacy)

マインドアップロード研究は、極めて機微な個人情報である神経データを扱います。本プロジェクトは、MIND Act 2025などの法的・倫理的要請に準拠するだけでなく、それを超える高いレベルでのプライバシー保護を目指します。

- **神経データの匿名化**: MRIデータに含まれる顔の形状を削除する[PyDeface](https://github.com/poldracklab/pydeface)のような匿名化アルゴリズムの導入を検討します。（EEGデータが主ですが、マルチモーダルなデータ収集を想定）
- **差分プライバシー (Differential Privacy)**: データ解析の過程で個人の情報が特定されるリスクを低減するため、差分プライバシー技術を応用した解析手法の導入を研究します。
- **同意管理**: 神経データの利用目的や範囲について、参加者が詳細かつ動的に管理できるような同意管理スキーマの設計と実装を計画しています。

## 貢献方法

- [issue.md](issue.md) を参照
- [Issueを立てる](https://github.com/yasufumi-nakata/eegflow/issues)

## LLM向けプロンプトの利用

- LLMに調査や分析を依頼する際の科学者スタイルのプロンプト例は [.agent/agent.md](.agent/agent.md) にまとめています。

## リンク

- **GitHub**: https://github.com/yasufumi-nakata/eegflow

## システム構成 (System Architecture)

本プロジェクトでは、AIエージェントを活用した半自動的なコンテンツ更新ワークフローを採用しています。

```mermaid
graph LR
    A[ユーザー] -->|Issue作成| B(Manus AI)
    B -->|Issue登録| C[GitHub Issues]
    C -->|Issue取得| D(Antigravity)
    D -->|コード修正・コミット| E[GitHub Repository]
    E -->|自動デプロイ| F[GitHub Pages]
    F -->|閲覧| A
```

### ワークフロー

1.  **Issue作成 (Manus)**: ユーザーがManus AIに対して改善提案や新機能のリクエストを伝えると、ManusがGitHub Issueを自動作成します。
2.  **Issue処理 (Antigravity)**: Antigravity（本エージェント）がオープンなIssueを取得し、コードベースを分析・修正し、コミット＆プッシュを行います。コミットメッセージに `Fixes #N` を含めることで、Issueは自動的にクローズされます。
3.  **デプロイ (GitHub Pages)**: `main` ブランチへのプッシュをトリガーに、GitHub Pagesが自動的にサイトを更新します。

## ホスティング

- GitHub Pages
