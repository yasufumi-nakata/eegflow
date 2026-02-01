# Automation

This folder contains an automated flow that fetches open GitHub issues, asks an AI CLI to resolve them, commits changes, and closes the issues.

## Files
- `resolve-issues.sh`: main automation script
- `server.js`: HTTP trigger for running the script
- `.env.example`: configuration template (copy to `.env`)
- `logs/`: runtime logs (ignored by git)
- `EegflowResolver.app/`: optional app bundle (ignored by git)

## Setup
1. Copy `.env.example` to `.env`.
2. Set `AI_CMD` to the command that reads the prompt from STDIN (e.g. `gemini --yolo`). If `AI_CMD` is empty and `gemini` is available, the script defaults to `automation/run-gemini.sh`.
3. Optionally set `AI_WORKDIR` if the AI tool must run outside the repo root.
4. Ensure `gh` and `jq` are installed and authenticated.
5. Optional safety settings in `.env`:
   - `RUN_TIMEOUT_SECONDS` / `RUN_TIMEOUT_GRACE_SECONDS` to prevent hung runs.
   - `QUEUE_ON_BUSY=true` to queue one follow-up run instead of skipping when a run is already in progress.
   - `AUTO_STASH_DIRTY=true` to stash pre-existing changes once at startup and restore them at the end.

The script sets `AI_PROMPT_FILE` to the prompt file path if your command prefers reading from a file. `run-gemini.sh` also accepts `GEMINI_FLAGS` to pass extra flags.
By default the script stops if there are tracked, uncommitted changes. Set `ALLOW_DIRTY=true` to bypass that check. Pre-existing untracked files are excluded from auto-commits.

## Run
- Dry run:
  - `bash resolve-issues.sh --dry-run`
- Normal run:
  - `bash resolve-issues.sh`
- Start the server:
  - `node server.js`
  - Call `http://localhost:3000/resolve`
