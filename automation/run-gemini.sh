#!/bin/bash
set -euo pipefail

if ! command -v gemini >/dev/null 2>&1; then
  echo "Error: gemini command not found in PATH." >&2
  exit 1
fi

GEMINI_FLAGS=${GEMINI_FLAGS:-"--yolo"}

# Prefer the prompt file when provided to avoid shell arg limits.
if [[ -n "${AI_PROMPT_FILE:-}" ]]; then
  if [[ ! -f "$AI_PROMPT_FILE" ]]; then
    echo "Error: AI_PROMPT_FILE does not exist: $AI_PROMPT_FILE" >&2
    exit 1
  fi
  gemini $GEMINI_FLAGS < "$AI_PROMPT_FILE"
  exit 0
fi

if [[ -t 0 ]]; then
  echo "Error: AI_PROMPT_FILE is not set and no stdin prompt was provided." >&2
  exit 1
fi

gemini $GEMINI_FLAGS
