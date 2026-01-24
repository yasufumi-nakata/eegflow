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

const PORT = Number(process.env.PORT) || 3000;
const RAW_SCRIPT_PATH = process.env.RESOLVE_SCRIPT;
const SCRIPT_PATH = RAW_SCRIPT_PATH
    ? (path.isAbsolute(RAW_SCRIPT_PATH)
        ? RAW_SCRIPT_PATH
        : path.join(__dirname, RAW_SCRIPT_PATH))
    : path.join(__dirname, 'resolve-issues.sh');

let isRunning = false;

// 実行ロジックを関数化
const runAutomation = (trigger) => {
    if (isRunning) {
        console.log(`[${new Date().toISOString()}] Automation already running; skipping ${trigger} run.`);
        return false;
    }
    console.log(`[${new Date().toISOString()}] Starting ${trigger} automation task...`);

    if (!fs.existsSync(SCRIPT_PATH)) {
        console.error('resolve-issues.sh が見つかりません。');
        return false;
    }

    isRunning = true;
    const child = spawn('bash', [SCRIPT_PATH], {
        cwd: __dirname,
        env: process.env,
        stdio: 'inherit',
    });
    child.on('error', (error) => {
        isRunning = false;
        console.error(`Exec error: ${error}`);
    });
    child.on('close', (code) => {
        isRunning = false;
        console.log(`[${new Date().toISOString()}] Automation task finished with code ${code}.`);
    });
    return true;
};

// 毎日11:00と17:00に実行
cron.schedule('0 11 * * *', () => runAutomation('scheduled-11'));
cron.schedule('0 17 * * *', () => runAutomation('scheduled-17'));
console.log('Cron jobs scheduled: runs daily at 11:00 and 17:00');

const server = http.createServer((req, res) => {
    if (req.url === '/resolve' && req.method === 'GET') {
        console.log(`[${new Date().toISOString()}] Received manual resolve request`);
        
        const started = runAutomation('manual');

        res.writeHead(started ? 200 : 409, { 'Content-Type': 'text/plain; charset=utf-8' });
        res.end(started ? '自動実行スクリプトをトリガーしました。\n' : '既に実行中です。\n');
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
