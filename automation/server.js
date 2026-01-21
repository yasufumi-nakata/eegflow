const http = require('http');
const { exec } = require('child_process');
const path = require('path');
const fs = require('fs');

const ENV_PATH = path.join(__dirname, '.env');

if (fs.existsSync(ENV_PATH)) {
    const lines = fs.readFileSync(ENV_PATH, 'utf8').split(/\r?\n/);
    for (const line of lines) {
        const trimmed = line.trim();
        if (!trimmed || trimmed.startsWith('#')) {
            continue;
        }
        const [key, ...rest] = trimmed.split('=');
        if (!key) {
            continue;
        }
        const value = rest.join('=').trim();
        if (!(key in process.env)) {
            process.env[key] = value;
        }
    }
}

const PORT = Number(process.env.PORT) || 3000;
const SCRIPT_PATH = process.env.RESOLVE_SCRIPT || path.join(__dirname, 'resolve-issues.sh');

const server = http.createServer((req, res) => {
    if (req.url === '/resolve' && req.method === 'GET') {
        console.log(`[${new Date().toISOString()}] Received resolve request`);

        if (!fs.existsSync(SCRIPT_PATH)) {
            res.writeHead(500, { 'Content-Type': 'text/plain; charset=utf-8' });
            res.end('resolve-issues.sh が見つかりません。\n');
            return;
        }

        // スクリプトを実行
        exec(`bash "${SCRIPT_PATH}"`, { cwd: __dirname }, (error, stdout, stderr) => {
            if (error) {
                console.error(`Exec error: ${error}`);
                return;
            }
            console.log(`Stdout: ${stdout}`);
            if (stderr) console.error(`Stderr: ${stderr}`);
        });

        res.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });
        res.end('定期実行スクリプトをバックグラウンドで開始しました。\n');
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
