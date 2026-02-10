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
ISSUE_LIMIT="${ISSUE_LIMIT:-${issue_limit:-50}}"
AI_CMD="${AI_CMD:-codex exec --full-auto -}"
AI_TIMEOUT_SECONDS="${AI_TIMEOUT_SECONDS:-300}"
AI_WORKDIR="${AI_WORKDIR:-$REPO_DIR}"
CO_AUTHOR="${CO_AUTHOR:-}"
ALLOW_DIRTY="${ALLOW_DIRTY:-false}"
AUTO_STASH_DIRTY="${AUTO_STASH_DIRTY:-false}"
DRY_RUN=false

AUTO_STASH_DONE=false
DIRTY_STASH_REF=""

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

append_markdown_path_list() {
    local paths="$1"
    local out_file="$2"
    if [[ -z "$paths" ]]; then
        echo "- (変更ファイルなし)" >> "$out_file"
        return
    fi
    while IFS= read -r path; do
        [[ -z "$path" ]] && continue
        printf -- '- `%s`\n' "$path" >> "$out_file"
    done <<< "$paths"
}

append_markdown_numstat_list() {
    local numstat="$1"
    local out_file="$2"
    if [[ -z "$numstat" ]]; then
        echo "- (差分統計なし)" >> "$out_file"
        return
    fi
    while IFS=$'\t' read -r added deleted path; do
        [[ -z "$path" ]] && continue
        printf -- '- `%s` (+%s / -%s)\n' "$path" "$added" "$deleted" >> "$out_file"
    done <<< "$numstat"
}

build_issue_resolution_comment() {
    local issue_num="$1"
    local issue_title="$2"
    local commit_sha="$3"
    local changed_files="$4"
    local diff_numstat="$5"
    local out_file="$6"

    cat > "$out_file" <<EOF
自動対応を完了しました。

### 修正案
- Issue #${issue_num}「${issue_title}」の要件を満たすため、関連箇所を確認し、影響範囲を最小化して修正する方針で対応しました。
- 変更内容と差分統計を以下に記録します。

### 修正内容
- コミット: \`${commit_sha}\`
- 変更ファイル:
EOF

    append_markdown_path_list "$changed_files" "$out_file"

    cat >> "$out_file" <<'EOF'

### 差分統計
EOF

    append_markdown_numstat_list "$diff_numstat" "$out_file"

    cat >> "$out_file" <<'EOF'

実行環境に関する情報はこのIssueには記載していません。
EOF
}

run_with_timeout() {
    local seconds="$1"
    shift
    if command -v gtimeout >/dev/null 2>&1; then
        gtimeout "$seconds" "$@"
        return $?
    elif command -v timeout >/dev/null 2>&1; then
        timeout "$seconds" "$@"
        return $?
    else
        "$@" &
        local cmd_pid=$!
        local watcher_pid
        (
            sleep "$seconds"
            if kill -0 "$cmd_pid" 2>/dev/null; then
                kill -TERM "$cmd_pid" 2>/dev/null || true
                sleep 5
                kill -KILL "$cmd_pid" 2>/dev/null || true
            fi
        ) &
        watcher_pid=$!

        local had_errexit=0
        if [[ $- == *e* ]]; then
            had_errexit=1
        fi
        set +e
        wait "$cmd_pid"
        local exit_code=$?
        if [[ $had_errexit -eq 1 ]]; then
            set -e
        fi

        kill -TERM "$watcher_pid" 2>/dev/null || true
        wait "$watcher_pid" 2>/dev/null || true
        return "$exit_code"
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

stash_dirty_worktree() {
    local status
    status=$(git -C "$REPO_DIR" status --porcelain)
    if [[ -z "$status" ]]; then
        return 0
    fi
    local stash_msg
    stash_msg="automation-auto-stash $(date '+%Y%m%d-%H%M%S')"
    log "作業ツリーが汚れているため一時退避します: ${stash_msg}"
    if ! git -C "$REPO_DIR" stash push -u -m "$stash_msg" >/dev/null; then
        error_exit "スタッシュに失敗しました。別のGitプロセスや権限、ディスク容量を確認してください。"
    fi
    DIRTY_STASH_REF=$(git -C "$REPO_DIR" stash list | grep -m 1 "$stash_msg" | cut -d: -f1 || true)
    if [[ -z "$DIRTY_STASH_REF" ]]; then
        log "WARN: 一時退避したスタッシュが特定できませんでした。"
    fi
}

stash_failed_issue() {
    local issue_num="$1"
    local status
    status=$(git -C "$REPO_DIR" status --porcelain)
    if [[ -z "$status" ]]; then
        return 0
    fi
    local stash_msg
    stash_msg="automation-failed-issue-${issue_num} $(date '+%Y%m%d-%H%M%S')"
    log "WARN: Issue #${issue_num} の変更を一時退避します: ${stash_msg}"
    if ! git -C "$REPO_DIR" stash push -u -m "$stash_msg" >/dev/null; then
        error_exit "Issue #${issue_num} の変更のスタッシュに失敗しました。作業ツリーを確認してください。"
    fi
}

restore_stash() {
    if [[ -z "$DIRTY_STASH_REF" ]]; then
        return 0
    fi
    log "一時退避した変更を戻します: ${DIRTY_STASH_REF}"
    if git -C "$REPO_DIR" stash show -p "$DIRTY_STASH_REF" | git -C "$REPO_DIR" apply --check --index >/dev/null 2>&1; then
        if git -C "$REPO_DIR" stash apply --index "$DIRTY_STASH_REF" >/dev/null; then
            git -C "$REPO_DIR" stash drop "$DIRTY_STASH_REF" >/dev/null || log "WARN: スタッシュの削除に失敗しました: ${DIRTY_STASH_REF}"
            log "スタッシュを復元しました。"
        else
            log "WARN: スタッシュの適用に失敗しました。手動で確認してください: ${DIRTY_STASH_REF}"
        fi
    else
        log "WARN: 競合が見込まれるためスタッシュを保持しました: ${DIRTY_STASH_REF}"
    fi
    DIRTY_STASH_REF=""
}

ensure_clean_tracked() {
    if [[ "$ALLOW_DIRTY" == "true" ]]; then
        return
    fi
    if git -C "$REPO_DIR" diff --quiet && git -C "$REPO_DIR" diff --staged --quiet; then
        if [[ "$AUTO_STASH_DONE" == "false" ]]; then
            AUTO_STASH_DONE=true
        fi
        return
    fi
    if [[ "$AUTO_STASH_DIRTY" == "true" && "$AUTO_STASH_DONE" == "false" ]]; then
        stash_dirty_worktree
        AUTO_STASH_DONE=true
        return
    fi
    error_exit "作業ツリーに未コミットの変更があります。ALLOW_DIRTY=true で続行できます。"
}

checkout_target_branch() {
    local current_branch
    current_branch=$(git -C "$REPO_DIR" rev-parse --abbrev-ref HEAD)
    if [[ "$current_branch" == "$TARGET_BRANCH" ]]; then
        return
    fi
    log "対象ブランチへ切り替えます: ${TARGET_BRANCH}"
    if git -C "$REPO_DIR" show-ref --verify --quiet "refs/heads/${TARGET_BRANCH}"; then
        git -C "$REPO_DIR" checkout "$TARGET_BRANCH"
        return
    fi
    if git -C "$REPO_DIR" show-ref --verify --quiet "refs/remotes/origin/${TARGET_BRANCH}"; then
        git -C "$REPO_DIR" checkout -b "$TARGET_BRANCH" "origin/${TARGET_BRANCH}"
        return
    fi
    error_exit "対象ブランチが見つかりません: ${TARGET_BRANCH}"
}

cleanup_prompt() {
    if [[ -n "${PROMPT_FILE:-}" && -f "$PROMPT_FILE" ]]; then
        rm -f "$PROMPT_FILE"
    fi
    PROMPT_FILE=""
}

cleanup_all() {
    cleanup_prompt
    restore_stash
}

trap cleanup_all EXIT INT TERM

# 初期化
mkdir -p "$LOG_DIR"
log "=== Issue自動解決スクリプト開始 ==="

require_cmd git
require_cmd gh
require_cmd jq

if [[ ! -d "$REPO_DIR/.git" ]]; then
    error_exit "REPO_DIR が Git リポジトリではありません: $REPO_DIR"
fi

if [[ "$DRY_RUN" == false ]]; then
    AI_CMD_BIN=$(printf '%s\n' "$AI_CMD" | awk '{print $1}')
    if [[ -z "$AI_CMD_BIN" ]]; then
        error_exit "AI_CMD が空です。.env で設定してください。"
    fi
    require_cmd "$AI_CMD_BIN"
fi

# 最新のコードを取得
log "リポジトリを更新中..."
if [[ "$DRY_RUN" == false ]]; then
    ensure_clean_tracked
    checkout_target_branch
    git -C "$REPO_DIR" pull origin "$TARGET_BRANCH" 2>&1 | tee -a "$LOG_FILE" || log "WARN: git pull に失敗しました（続行）"
fi

# オープンIssueを取得
log "オープンIssueを取得中..."
ISSUES=$(gh issue list --repo "$REPO" --state open --json number,title,body --limit "$ISSUE_LIMIT" 2>>"$LOG_FILE") || error_exit "Issueの取得に失敗しました"

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
    ISSUE_BODY=$(echo "$issue" | jq -r '.body // ""')
    
    log "--- Issue #${ISSUE_NUM} を処理中: ${ISSUE_TITLE} ---"

    if [[ "$DRY_RUN" == false ]]; then
        ensure_clean_tracked
    fi

    UNTRACKED_BEFORE=""
    if [[ "$DRY_RUN" == false ]]; then
        UNTRACKED_BEFORE=$(git -C "$REPO_DIR" ls-files --others --exclude-standard)
    fi
    
    # AIに渡すプロンプトを構築
    PROMPT="あなたはeegflowプロジェクトの開発者です。以下のGitHub Issueを解決してください。

## Issue #${ISSUE_NUM}: ${ISSUE_TITLE}

${ISSUE_BODY}

---

リポジトリの構造を確認し、適切なファイルを修正してください。
修正が完了したら、変更内容の要約と実施した確認手順を教えてください。
実行環境（OS情報、ユーザー名、絶対パス、秘密情報）はGitHubへ記載しないでください。"

    if [[ "$DRY_RUN" == true ]]; then
        log "[DRY-RUN] Issue #${ISSUE_NUM} のプロンプトを生成しました"
        log "[DRY-RUN] プロンプト文字数: ${#PROMPT}"
        continue
    fi
    
    # プロンプトを一時ファイルに保存（実行後に削除）
    PROMPT_FILE=$(mktemp "${TMPDIR:-/tmp}/eegflow_prompt_${ISSUE_NUM}_XXXXXX.txt")
    printf '%s' "$PROMPT" > "$PROMPT_FILE"
    
    log "Issue #${ISSUE_NUM} を解決中..."
    if ! run_ai < "$PROMPT_FILE" >>"$LOG_FILE" 2>&1; then
        log "ERROR: Issue #${ISSUE_NUM} の解決に失敗しました"
        stash_failed_issue "$ISSUE_NUM"
        rm -f "$PROMPT_FILE"
        PROMPT_FILE=""
        continue
    fi
    rm -f "$PROMPT_FILE"
    PROMPT_FILE=""
    
    log "AI処理完了"
    
    # 変更があれば検出
    if git -C "$REPO_DIR" diff --quiet && git -C "$REPO_DIR" diff --staged --quiet; then
        log "Issue #${ISSUE_NUM}: ファイルの変更がありませんでした"
        continue
    fi
    
    # 変更をコミット
    log "変更をコミット中..."
    git -C "$REPO_DIR" add -A
    if [[ -n "$UNTRACKED_BEFORE" ]]; then
        while IFS= read -r path; do
            [[ -z "$path" ]] && continue
            git -C "$REPO_DIR" reset -q -- "$path"
        done <<< "$UNTRACKED_BEFORE"
    fi
    STAGED_FILES=$(git -C "$REPO_DIR" diff --cached --name-only)
    STAGED_NUMSTAT=$(git -C "$REPO_DIR" diff --cached --numstat)
    if [[ -z "$STAGED_FILES" ]]; then
        log "Issue #${ISSUE_NUM}: コミット対象の変更がありませんでした"
        git -C "$REPO_DIR" reset -q
        continue
    fi
    COMMIT_MSG="Fixes #${ISSUE_NUM}: ${ISSUE_TITLE}

自動生成による修正
"
    if [[ -n "$CO_AUTHOR" ]]; then
        COMMIT_MSG="${COMMIT_MSG}"$'\n\n'"Co-authored-by: ${CO_AUTHOR}"
    fi
    git -C "$REPO_DIR" commit -m "$COMMIT_MSG"
    COMMIT_SHA=$(git -C "$REPO_DIR" rev-parse --short HEAD)
    
    # プッシュ
    log "変更をプッシュ中..."
    git -C "$REPO_DIR" push origin "$TARGET_BRANCH"
    
    # Issueをクローズ
    log "Issue #${ISSUE_NUM} をクローズ中..."
    CLOSE_COMMENT_FILE=$(mktemp "${TMPDIR:-/tmp}/issue_close_${ISSUE_NUM}_XXXXXX.md")
    build_issue_resolution_comment "$ISSUE_NUM" "$ISSUE_TITLE" "$COMMIT_SHA" "$STAGED_FILES" "$STAGED_NUMSTAT" "$CLOSE_COMMENT_FILE"
    if gh issue comment "$ISSUE_NUM" --repo "$REPO" --body-file "$CLOSE_COMMENT_FILE" >>"$LOG_FILE" 2>&1; then
        gh issue close "$ISSUE_NUM" --repo "$REPO" >>"$LOG_FILE" 2>&1 || log "WARN: Issueのクローズに失敗しました"
    else
        log "ERROR: Issue #${ISSUE_NUM} の修正内容コメント投稿に失敗したため、クローズをスキップしました"
    fi
    rm -f "$CLOSE_COMMENT_FILE"
    
    log "Issue #${ISSUE_NUM} の処理が完了しました"
done

log "=== Issue自動解決スクリプト終了 ==="
