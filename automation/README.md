# Automation

This folder contains an automated flow that fetches open GitHub issues, asks an AI CLI to resolve them, commits changes, posts a fix proposal/change summary comment, and closes the issues.

## Files
- `resolve-issues.sh`: main automation script
- `server.js`: HTTP trigger for running the script
- `.env.example`: configuration template (copy to `.env`)
- `logs/`: runtime logs (ignored by git)
- `EegflowResolver.app/`: optional app bundle (ignored by git)
- `swarm150_site/out/worker_suggestions.jsonl`: 150-worker提案の集約結果（`worker*.md` 個別ファイルは冗長のため廃止）

## Setup
1. Copy `.env.example` to `.env`.
2. Optional: set `AI_CMD` to your local AI runner command that reads the prompt from STDIN (e.g. `your-ai-cli --non-interactive`). If omitted, `resolve-issues.sh` uses `codex exec --full-auto -`.
3. Optionally set `AI_WORKDIR` if the AI tool must run outside the repo root.
4. Ensure `gh` and `jq` are installed and authenticated.
5. Keep execution-environment values only in local `.env` (git-ignored), not in tracked files.
6. Optional safety settings in `.env`:
   - `RUN_TIMEOUT_SECONDS` / `RUN_TIMEOUT_GRACE_SECONDS` to prevent hung runs.
   - `QUEUE_ON_BUSY=true` to queue one follow-up run instead of skipping when a run is already in progress.
   - `AUTO_STASH_DIRTY=true` to stash pre-existing changes once at startup and restore them at the end.
   - `SCHEDULE_MINUTE=0` to run once per hour at minute 0 (`server.js`).

The script sets `AI_PROMPT_FILE` to the prompt file path if your command prefers reading from a file.
By default the script stops if there are tracked, uncommitted changes. Set `ALLOW_DIRTY=true` to bypass that check. Pre-existing untracked files are excluded from auto-commits.

## Run
- Dry run:
  - `bash resolve-issues.sh --dry-run`
- Normal run:
  - `bash resolve-issues.sh`
- Start the server:
  - `node server.js`
  - Call `http://localhost:3000/resolve`
  - The server also runs automatically once per hour.
