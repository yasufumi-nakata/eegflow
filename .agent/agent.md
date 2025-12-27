# EEGFlow プロジェクト仕様書

## ホスティング

- **GitHub Pages** でホスト
- CNAMEファイルによるカスタムドメイン設定あり

## ファイル構成

```
/
├── index.html          # メインサイト
├── CNAME              # GitHub Pagesドメイン設定
├── .gitignore         # Git除外ファイル
└── .agent/
    └── agent.md       # この仕様書
```

## 技術スタック

- 静的HTML/CSS/JavaScript
- フレームワーク不要（バニラ）
