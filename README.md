# EEGFlow
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

マインドアップロード実現のための中核となるコアサイト。

## 目的

このサイトは、マインドアップロードの実現に向けた技術・研究・コミュニティの中心的ハブとなることを目指しています。

ここでいうマインドアップロードとは、**意識や記憶の交換・複製を可能とする技術**を指します。

## 今後の展望

本プロジェクトは、最終的にサイトの更新や運用プロセスを完全に自動化することを目指しています。現在は手動で行っているタスクも、順次自動化ツールやCI/CDパイプラインへ移行する予定です。

## 貢献方法

- [issue.md](issue.md) を参照
- [Issueを立てる](https://github.com/yasufumi-nakata/eegflow/issues)

## LLM向けプロンプトの利用

- LLMに調査や分析を依頼する際の科学者スタイルのプロンプト例は [.agent/agent.md](.agent/agent.md) にまとめています。
- AI運用時は、実行可能な作業だけを提案・実施する「握れるボール原則」を必ず遵守してください（[.agent/agent.md](.agent/agent.md) の該当節）。

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
