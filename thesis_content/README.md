このディレクトリは、`ymrl/thesis-template` に上書きする原稿一式です。

ビルド時（GitHub Actions）は以下を行います：
- テンプレを `thesis/` にクローン
- 本ディレクトリの `main.tex`, `00_abstract.tex`, `01.tex` などを `thesis/` に `rsync` でコピー
- テンプレ同梱 `Makefile` で `make` を実行し `main.pdf` を生成

ローカルで確認する場合：
```bash
cd thesis_content
docker run --rm -v "$PWD:/workdir" -w /workdir paperist/texlive-ja:latest sh -lc "mkdir -p /tmp/thesis && cp -r . /tmp/thesis && cd /tmp/thesis && make || (platex -kanji=utf8 main && pbibtex -kanji=utf8 main && platex -kanji=utf8 main && platex -kanji=utf8 main && dvipdfmx -p a4 main) && cp main.pdf /workdir/"
open main.pdf
```


