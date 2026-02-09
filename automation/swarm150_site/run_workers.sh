#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PROMPT_DIR="$ROOT_DIR/prompts"
OUT_DIR="$ROOT_DIR/out"
LOG_DIR="$ROOT_DIR/logs"

mkdir -p "$OUT_DIR" "$LOG_DIR"

CODEX_BIN="${CODEX_BIN:-codex}"
# Default: enable web search + safe automation.
# If you prefer, edit this line (e.g. remove --search, or change approval/sandbox flags).
CODEX_COMMON_ARGS=(--search --full-auto)

WORKERS=150

run_worker () {
  local no="$1"
  "$CODEX_BIN" "${CODEX_COMMON_ARGS[@]}" exec \
    --skip-git-repo-check \
    --output-last-message "$OUT_DIR/worker${no}.md" \
    - < "$PROMPT_DIR/worker${no}.txt" \
    > "$LOG_DIR/worker${no}.log" 2>&1
}

pids=()
for no in $(seq 1 "$WORKERS"); do
  run_worker "$no" &
  pids+=("$!")
done

echo "[INFO] Waiting for workers..."
for pid in "${pids[@]}"; do
  wait "$pid"
done
echo "[INFO] Workers done."

SKIP_MERGE="${SKIP_MERGE:-0}"
if [ "$SKIP_MERGE" = "1" ]; then
  echo "[OK] SKIP_MERGE=1; skipping merge."
  exit 0
fi

{
  cat "$PROMPT_DIR/merge.txt"
  echo ""
  for no in $(seq 1 "$WORKERS"); do
    echo ""
    echo "## Worker ${no} output"
    cat "$OUT_DIR/worker${no}.md"
    echo ""
  done
} | "$CODEX_BIN" "${CODEX_COMMON_ARGS[@]}" exec \
  --skip-git-repo-check \
  --output-last-message "$OUT_DIR/final.md" \
  - > "$LOG_DIR/merge.log" 2>&1

echo "[OK] wrote: $OUT_DIR/final.md"
