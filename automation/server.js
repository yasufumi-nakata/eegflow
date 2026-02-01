const http = require('http');
const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');
const cron = require('node-cron');

const ENV_PATH = path.join(__dirname, '.env');

const parseEnvValue = (value) => {
    const trimmed = value.trim();
    if (
        (trimmed.startsWith('"') && trimmed.endsWith('"')) ||
        (trimmed.startsWith("'") && trimmed.endsWith("'"))
    ) {
        return trimmed.slice(1, -1);
    }
    return trimmed;
};

if (fs.existsSync(ENV_PATH)) {
    const lines = fs.readFileSync(ENV_PATH, 'utf8').split(/\r?\n/);
    for (const line of lines) {
        const trimmed = line.trim();
        if (!trimmed || trimmed.startsWith('#')) {
            continue;
        }
        const [rawKey, ...rest] = trimmed.split('=');
        const key = rawKey.replace(/^export\s+/, '').trim();
        if (!key) {
            continue;
        }
        const value = parseEnvValue(rest.join('='));
        if (!(key in process.env)) {
            process.env[key] = value;
        }
    }
}

const toNumberOrDefault = (value, fallback) => {
    const num = Number(value);
    return Number.isFinite(num) ? num : fallback;
};

const PORT = toNumberOrDefault(process.env.PORT, 3000);
const RUN_TIMEOUT_SECONDS = toNumberOrDefault(process.env.RUN_TIMEOUT_SECONDS, 3600);
const RUN_TIMEOUT_GRACE_SECONDS = toNumberOrDefault(process.env.RUN_TIMEOUT_GRACE_SECONDS, 30);
const QUEUE_ON_BUSY = String(process.env.QUEUE_ON_BUSY ?? 'true').toLowerCase() !== 'false';
const RAW_SCRIPT_PATH = process.env.RESOLVE_SCRIPT;
const SCRIPT_PATH = RAW_SCRIPT_PATH
    ? (path.isAbsolute(RAW_SCRIPT_PATH)
        ? RAW_SCRIPT_PATH
        : path.join(__dirname, RAW_SCRIPT_PATH))
    : path.join(__dirname, 'resolve-issues.sh');

let isRunning = false;
let pendingTriggers = new Set();

// 実行ロジックを関数化
const runAutomation = (trigger) => {
    if (isRunning) {
        if (QUEUE_ON_BUSY) {
            pendingTriggers.add(trigger);
            console.log(`[${new Date().toISOString()}] Automation already running; queued ${trigger} run.`);
            return 'queued';
        }
        console.log(`[${new Date().toISOString()}] Automation already running; skipping ${trigger} run.`);
        return 'skipped';
    }
    console.log(`[${new Date().toISOString()}] Starting ${trigger} automation task...`);

    if (!fs.existsSync(SCRIPT_PATH)) {
        console.error('resolve-issues.sh が見つかりません。');
        return 'skipped';
    }

    isRunning = true;
    const child = spawn('bash', [SCRIPT_PATH], {
        cwd: __dirname,
        env: process.env,
        stdio: 'inherit',
    });
    let timeoutId = null;
    let killTimer = null;
    if (RUN_TIMEOUT_SECONDS > 0) {
        timeoutId = setTimeout(() => {
            console.error(`[${new Date().toISOString()}] Automation timed out after ${RUN_TIMEOUT_SECONDS}s; sending SIGTERM.`);
            child.kill('SIGTERM');
            if (RUN_TIMEOUT_GRACE_SECONDS > 0) {
                killTimer = setTimeout(() => {
                    console.error(`[${new Date().toISOString()}] Automation still running; sending SIGKILL.`);
                    child.kill('SIGKILL');
                }, RUN_TIMEOUT_GRACE_SECONDS * 1000);
            }
        }, RUN_TIMEOUT_SECONDS * 1000);
    }
    child.on('error', (error) => {
        isRunning = false;
        if (timeoutId) {
            clearTimeout(timeoutId);
        }
        if (killTimer) {
            clearTimeout(killTimer);
        }
        console.error(`Exec error: ${error}`);
    });
    child.on('close', (code, signal) => {
        isRunning = false;
        if (timeoutId) {
            clearTimeout(timeoutId);
        }
        if (killTimer) {
            clearTimeout(killTimer);
        }
        const status = signal ? `signal ${signal}` : `code ${code}`;
        console.log(`[${new Date().toISOString()}] Automation task finished with ${status}.`);
        if (QUEUE_ON_BUSY && pendingTriggers.size > 0) {
            const queued = Array.from(pendingTriggers).join(',');
            pendingTriggers = new Set();
            console.log(`[${new Date().toISOString()}] Starting queued automation run (${queued}).`);
            runAutomation(`queued:${queued}`);
        }
    });
    return 'started';
};

// 毎日11:00と17:00に実行
cron.schedule('0 11 * * *', () => runAutomation('scheduled-11'));
cron.schedule('0 17 * * *', () => runAutomation('scheduled-17'));
console.log('Cron jobs scheduled: runs daily at 11:00 and 17:00');

const server = http.createServer((req, res) => {
    if (req.url === '/resolve' && req.method === 'GET') {
        console.log(`[${new Date().toISOString()}] Received manual resolve request`);
        
        const status = runAutomation('manual');

        if (status === 'started') {
            res.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });
            res.end('自動実行スクリプトをトリガーしました。\n');
        } else if (status === 'queued') {
            res.writeHead(202, { 'Content-Type': 'text/plain; charset=utf-8' });
            res.end('実行中のため、次回の実行としてキューに入れました。\n');
        } else {
            res.writeHead(409, { 'Content-Type': 'text/plain; charset=utf-8' });
            res.end('既に実行中です。\n');
        }
    } else {
        res.writeHead(404);
        res.end();
    }
});

server.listen(PORT, () => {
    console.log(`Automation server is running on http://localhost:${PORT}`);
    console.log(`Endpoint: http://localhost:${PORT}/resolve`);
    console.log('---');
    console.log('このターミナルを開いたままにしておくと、定時実行が正常に動作します。');
});
