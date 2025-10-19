#!/usr/bin/env bash
set -Eeuo pipefail

# This wrapper ensures required env vars are present and then starts an Elsevier MCP server.
#
# Configuration options (set in your shell env or a .env/.env.local in repo root):
# - ELSEVIER_API_KEY     (required) Elsevier API key
# - ELSEVIER_INSTTOKEN   (optional) Institution token if your access requires it
# - ELSEVIER_API_HOST    (optional) Override API host for the server, if supported by your server
# - ELSEVIER_MCP_COMMAND (optional) Explicit server command to run (e.g. "python -m mcp_elsevier")

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

# Load env files if present (bash-friendly KEY=VALUE lines)
if [ -f .env ]; then set -a; . ./.env; set +a; fi
if [ -f .env.local ]; then set -a; . ./.env.local; set +a; fi

if [ -z "${ELSEVIER_API_KEY:-}" ]; then
  echo "ERROR: ELSEVIER_API_KEY is not set. Add it to your environment or .env/.env.local." >&2
  exit 1
fi

# If an explicit command is provided, use it as-is.
if [ -n "${ELSEVIER_MCP_COMMAND:-}" ]; then
  exec bash -lc "$ELSEVIER_MCP_COMMAND"
fi

# Try common server binaries. Update these if your installed server uses a different name.
if command -v mcp-server-elsevier >/dev/null 2>&1; then
  exec mcp-server-elsevier
elif command -v elsevier-mcp >/dev/null 2>&1; then
  exec elsevier-mcp
elif command -v mcp-elsevier >/dev/null 2>&1; then
  exec mcp-elsevier
elif command -v python >/dev/null 2>&1 && python -c "import importlib,sys; sys.exit(0 if importlib.util.find_spec('mcp_elsevier') else 1)" 2>/dev/null; then
  exec python -m mcp_elsevier
elif command -v npx >/dev/null 2>&1; then
  # Fallback to an npm package name example; adjust to your actual package if different.
  exec npx -y @modelcontextprotocol/server-elsevier
else
  cat >&2 <<'EOM'
ERROR: Could not find an Elsevier MCP server binary.
Install one and ensure it is on PATH, or set ELSEVIER_MCP_COMMAND.

Examples (adjust to the actual package you use):
  # Python
  pip install mcp-server-elsevier
  # then this wrapper will auto-detect 'mcp-server-elsevier'

  # Node.js
  npm i -g @modelcontextprotocol/server-elsevier
  # then this wrapper will auto-detect 'mcp-elsevier' or use npx fallback
EOM
  exit 127
fi

