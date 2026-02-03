#!/bin/bash
set -euo pipefail

if ! command -v codex >/dev/null 2>&1; then
  echo "Error: codex command not found in PATH." >&2
  exit 1
fi

CODEX_FLAGS=${CODEX_FLAGS:-"--full-auto -m gpt-5.2-codex -c model_reasoning_effort=\"xhigh\""}
read -r -a CODEX_ARGS <<< "$CODEX_FLAGS"

run_codex() {
  codex exec "${CODEX_ARGS[@]}" "$@"
}

# Prefer the prompt file when provided to avoid shell arg limits.
if [[ -n "${AI_PROMPT_FILE:-}" ]]; then
  if [[ ! -f "$AI_PROMPT_FILE" ]]; then
    echo "Error: AI_PROMPT_FILE does not exist: $AI_PROMPT_FILE" >&2
    exit 1
  fi
  run_codex - < "$AI_PROMPT_FILE"
  exit 0
fi

if [[ -t 0 ]]; then
  echo "Error: AI_PROMPT_FILE is not set and no stdin prompt was provided." >&2
  exit 1
fi

run_codex
