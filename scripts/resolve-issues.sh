#!/bin/bash
# resolve-issues.sh - GitHub IssueをAI CLIツールで自動解決するスクリプト
# 
# 使用方法:
#   ./resolve-issues.sh           # 通常実行
#   ./resolve-issues.sh --dry-run # ドライラン（変更なし）
#
# 必要な環境:
#   - gh (GitHub CLI) がインストール済みで認証済み
#   - gemini または codex CLI がインストール済み

set -e

# 設定
REPO="yasufumi-nakata/eegflow"
REPO_DIR="/Users/yasushi/Documents/GitHub/eegflow"
LOG_DIR="/Users/yasushi/Library/Logs/eegflow"
LOG_FILE="${LOG_DIR}/resolve-issues-$(date +%Y%m%d-%H%M%S).log"
DRY_RUN=false

# 引数処理
if [[ "$1" == "--dry-run" ]]; then
    DRY_RUN=true
    echo "ドライランモード: 実際の変更は行いません"
fi

# ログ関数
log() {
    local msg="[$(date '+%Y-%m-%d %H:%M:%S')] $1"
    echo "$msg"
    echo "$msg" >> "$LOG_FILE"
}

# エラーハンドリング
error_exit() {
    log "ERROR: $1"
    exit 1
}

# 初期化
mkdir -p "$LOG_DIR"
log "=== Issue自動解決スクリプト開始 ==="
cd "$REPO_DIR" || error_exit "リポジトリディレクトリに移動できません: $REPO_DIR"

# 最新のコードを取得
log "リポジトリを更新中..."
if [[ "$DRY_RUN" == false ]]; then
    git pull origin main 2>&1 | tee -a "$LOG_FILE" || log "WARN: git pull に失敗しました（続行）"
fi

# オープンIssueを取得
log "オープンIssueを取得中..."
ISSUES=$(gh issue list --repo "$REPO" --state open --json number,title,body --limit 50 2>&1) || error_exit "Issueの取得に失敗しました"

ISSUE_COUNT=$(echo "$ISSUES" | jq 'length')
log "オープンIssue数: $ISSUE_COUNT"

if [[ "$ISSUE_COUNT" -eq 0 ]]; then
    log "処理するIssueがありません。終了します。"
    exit 0
fi

# 各Issueを処理
echo "$ISSUES" | jq -c '.[]' | while read -r issue; do
    ISSUE_NUM=$(echo "$issue" | jq -r '.number')
    ISSUE_TITLE=$(echo "$issue" | jq -r '.title')
    ISSUE_BODY=$(echo "$issue" | jq -r '.body')
    
    log "--- Issue #${ISSUE_NUM} を処理中: ${ISSUE_TITLE} ---"
    
    # AIに渡すプロンプトを構築
    PROMPT="あなたはeegflowプロジェクトの開発者です。以下のGitHub Issueを解決してください。

## Issue #${ISSUE_NUM}: ${ISSUE_TITLE}

${ISSUE_BODY}

---

リポジトリの構造を確認し、適切なファイルを修正してください。
修正が完了したら、変更内容の要約を教えてください。"

    if [[ "$DRY_RUN" == true ]]; then
        log "[DRY-RUN] Issue #${ISSUE_NUM} のプロンプトを生成しました"
        log "[DRY-RUN] プロンプト文字数: ${#PROMPT}"
        continue
    fi
    
    # gemini CLIで解決を試みる
    log "gemini CLIで Issue #${ISSUE_NUM} を解決中..."
    
    # geminiをyoloモードで実行（自動承認）
    GEMINI_RESULT=$(echo "$PROMPT" | timeout 300 gemini --yolo -o text 2>&1) || {
        log "WARN: gemini での解決に失敗しました。codex を試みます..."
        
        # codexで再試行
        GEMINI_RESULT=$(timeout 300 codex exec --approval-mode full-auto "$PROMPT" 2>&1) || {
            log "ERROR: Issue #${ISSUE_NUM} の解決に失敗しました"
            continue
        }
    }
    
    log "AI処理完了"
    
    # 変更があれば検出
    if git diff --quiet && git diff --staged --quiet; then
        log "Issue #${ISSUE_NUM}: ファイルの変更がありませんでした"
        continue
    fi
    
    # 変更をコミット
    log "変更をコミット中..."
    git add -A
    git commit -m "Fixes #${ISSUE_NUM}: ${ISSUE_TITLE}

自動生成による修正

Co-authored-by: gemini-cli <noreply@google.com>"
    
    # プッシュ
    log "変更をプッシュ中..."
    git push origin main
    
    # Issueをクローズ
    log "Issue #${ISSUE_NUM} をクローズ中..."
    gh issue close "$ISSUE_NUM" --repo "$REPO" --comment "このIssueは自動解決システムにより対応されました。" || log "WARN: Issueのクローズに失敗しました"
    
    log "Issue #${ISSUE_NUM} の処理が完了しました"
done

log "=== Issue自動解決スクリプト終了 ==="
