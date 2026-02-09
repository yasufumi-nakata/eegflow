#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PROMPT_DIR="$ROOT_DIR/prompts"
OUT_DIR="$ROOT_DIR/out"
LOG_DIR="$ROOT_DIR/logs"
REPO_DIR="${REPO_DIR:-/Users/yasufumi/Documents/GitHub/eegflow}"

mkdir -p "$OUT_DIR" "$LOG_DIR"

CODEX_BIN="${CODEX_BIN:-codex}"
MODEL_NAME="${MODEL_NAME:-gpt-5-codex}"
REASONING_EFFORT="${REASONING_EFFORT:-high}"
MAX_PARALLEL="${MAX_PARALLEL:-20}"
MAX_RETRIES="${MAX_RETRIES:-2}"
SKIP_MERGE="${SKIP_MERGE:-1}"

# Override broken local defaults and pin the execution environment.
CODEX_COMMON_ARGS=(
  -C "$REPO_DIR"
  -m "$MODEL_NAME"
  -c "model_reasoning_effort=\"$REASONING_EFFORT\""
  -c "approval_policy=\"never\""
  -c "sandbox_mode=\"danger-full-access\""
)

WORKERS="${WORKERS:-150}"

run_worker () {
  local no="$1"
  "$CODEX_BIN" exec "${CODEX_COMMON_ARGS[@]}" \
    --skip-git-repo-check \
    --output-last-message "$OUT_DIR/worker${no}.md" \
    - < "$PROMPT_DIR/worker${no}.txt" \
    > "$LOG_DIR/worker${no}.log" 2>&1
}

run_with_retry () {
  local no="$1"
  local attempt=0
  while true; do
    attempt=$((attempt + 1))
    if run_worker "$no"; then
      return 0
    fi
    if [ "$attempt" -gt "$MAX_RETRIES" ]; then
      echo "[ERROR] worker${no} failed after ${MAX_RETRIES} retries" >&2
      return 1
    fi
    echo "[WARN] worker${no} failed. retry ${attempt}/${MAX_RETRIES}" >&2
    sleep 1
  done
}

active=0
pids=()

wait_one () {
  local pid="$1"
  if ! wait "$pid"; then
    :
  fi
}

drain_one () {
  local pid="${pids[0]}"
  wait_one "$pid"
  pids=("${pids[@]:1}")
  active=$((active - 1))
}

failed_workers=()
for no in $(seq 1 "$WORKERS"); do
  (
    if ! run_with_retry "$no"; then
      echo "$no" > "$LOG_DIR/worker${no}.failed"
      exit 1
    fi
  ) &
  pids+=("$!")
  active=$((active + 1))
  if [ "$active" -ge "$MAX_PARALLEL" ]; then
    drain_one
  fi
done

while [ "$active" -gt 0 ]; do
  drain_one
done

for no in $(seq 1 "$WORKERS"); do
  if [ -f "$LOG_DIR/worker${no}.failed" ]; then
    failed_workers+=("$no")
  fi
done

if [ "${#failed_workers[@]}" -gt 0 ]; then
  echo "[ERROR] failed workers: ${failed_workers[*]}" >&2
  exit 1
fi

echo "[INFO] Workers done. outputs in $OUT_DIR"

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
} | "$CODEX_BIN" exec "${CODEX_COMMON_ARGS[@]}" \
  --skip-git-repo-check \
  --output-last-message "$OUT_DIR/final.md" \
  - > "$LOG_DIR/merge.log" 2>&1

echo "[OK] wrote: $OUT_DIR/final.md"
