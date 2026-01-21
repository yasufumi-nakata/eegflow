#!/usr/bin/env bash
# resolve-issues.sh - GitHub IssueをAI CLIツールで自動解決するスクリプト
#
# 使用方法:
#   ./resolve-issues.sh           # 通常実行
#   ./resolve-issues.sh --dry-run # ドライラン（変更なし）
#
# 必要な環境:
#   - gh (GitHub CLI) がインストール済みで認証済み
#   - jq がインストール済み
#   - AI_CMD に対応するCLI/スクリプトが用意済み

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEFAULT_REPO_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

# .env を読み込み（存在する場合）
ENV_FILE="${ENV_FILE:-${SCRIPT_DIR}/.env}"
if [[ -f "$ENV_FILE" ]]; then
    set -a
    # shellcheck disable=SC1090
    . "$ENV_FILE"
    set +a
fi

# 設定（.env で上書き可能）
REPO="${REPO:-yasufumi-nakata/eegflow}"
REPO_DIR="${REPO_DIR:-$DEFAULT_REPO_DIR}"
AUTOMATION_DIR="${AUTOMATION_DIR:-$SCRIPT_DIR}"
LOG_DIR="${LOG_DIR:-${AUTOMATION_DIR}/logs}"
LOG_FILE="${LOG_FILE:-${LOG_DIR}/resolve-issues-$(date +%Y%m%d-%H%M%S).log}"
TARGET_BRANCH="${TARGET_BRANCH:-main}"
ISSUE_LIMIT="${ISSUE_LIMIT:-50}"
AI_CMD="${AI_CMD:-}"
AI_TIMEOUT_SECONDS="${AI_TIMEOUT_SECONDS:-300}"
AI_WORKDIR="${AI_WORKDIR:-$REPO_DIR}"
CO_AUTHOR="${CO_AUTHOR:-}"
DRY_RUN=false

# 引数処理
if [[ "${1:-}" == "--dry-run" ]]; then
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

require_cmd() {
    local cmd="$1"
    command -v "$cmd" >/dev/null 2>&1 || error_exit "必要なコマンドが見つかりません: $cmd"
}

run_with_timeout() {
    local seconds="$1"
    shift
    if command -v gtimeout >/dev/null 2>&1; then
        gtimeout "$seconds" "$@"
    elif command -v timeout >/dev/null 2>&1; then
        timeout "$seconds" "$@"
    else
        "$@"
    fi
}

run_ai() {
    if [[ -z "$AI_CMD" ]]; then
        log "ERROR: AI_CMD が未設定です。.env で設定してください。"
        return 1
    fi
    if [[ ! -d "$AI_WORKDIR" ]]; then
        log "ERROR: AI_WORKDIR が存在しません: $AI_WORKDIR"
        return 1
    fi
    export AI_PROMPT_FILE="$PROMPT_FILE"
    (cd "$AI_WORKDIR" && run_with_timeout "$AI_TIMEOUT_SECONDS" sh -c "$AI_CMD")
}

# 初期化
mkdir -p "$LOG_DIR"
log "=== Issue自動解決スクリプト開始 ==="

require_cmd git
require_cmd gh
require_cmd jq

if [[ ! -d "$REPO_DIR/.git" ]]; then
    error_exit "REPO_DIR が Git リポジトリではありません: $REPO_DIR"
fi

# 最新のコードを取得
log "リポジトリを更新中..."
if [[ "$DRY_RUN" == false ]]; then
    git -C "$REPO_DIR" pull origin "$TARGET_BRANCH" 2>&1 | tee -a "$LOG_FILE" || log "WARN: git pull に失敗しました（続行）"
fi

# オープンIssueを取得
log "オープンIssueを取得中..."
ISSUES=$(gh issue list --repo "$REPO" --state open --json number,title,body --limit "$ISSUE_LIMIT" 2>&1) || error_exit "Issueの取得に失敗しました"

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
    
    # プロンプトを一時ファイルに保存
    PROMPT_FILE="${LOG_DIR}/prompt_${ISSUE_NUM}.txt"
    echo "$PROMPT" > "$PROMPT_FILE"
    
    log "AI_CMD で Issue #${ISSUE_NUM} を解決中..."
    if ! printf '%s' "$PROMPT" | run_ai 2>&1 | tee -a "$LOG_FILE"; then
        log "ERROR: Issue #${ISSUE_NUM} の解決に失敗しました"
        continue
    fi
    
    log "AI処理完了"
    
    # 変更があれば検出
    if git -C "$REPO_DIR" diff --quiet && git -C "$REPO_DIR" diff --staged --quiet; then
        log "Issue #${ISSUE_NUM}: ファイルの変更がありませんでした"
        continue
    fi
    
    # 変更をコミット
    log "変更をコミット中..."
    git -C "$REPO_DIR" add -A
    COMMIT_MSG="Fixes #${ISSUE_NUM}: ${ISSUE_TITLE}

自動生成による修正
"
    if [[ -n "$CO_AUTHOR" ]]; then
        COMMIT_MSG="${COMMIT_MSG}"$'\n\n'"Co-authored-by: ${CO_AUTHOR}"
    fi
    git -C "$REPO_DIR" commit -m "$COMMIT_MSG"
    
    # プッシュ
    log "変更をプッシュ中..."
    git -C "$REPO_DIR" push origin "$TARGET_BRANCH"
    
    # Issueをクローズ
    log "Issue #${ISSUE_NUM} をクローズ中..."
    gh issue close "$ISSUE_NUM" --repo "$REPO" --comment "このIssueは自動解決システムにより対応されました。" || log "WARN: Issueのクローズに失敗しました"
    
    log "Issue #${ISSUE_NUM} の処理が完了しました"
done

log "=== Issue自動解決スクリプト終了 ==="
