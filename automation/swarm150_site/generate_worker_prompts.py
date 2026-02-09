#!/usr/bin/env python3
from pathlib import Path
import csv

ROOT = Path('/Users/yasufumi/Documents/GitHub/eegflow/automation/swarm150_site')
PROMPTS = ROOT / 'prompts'
PROMPTS.mkdir(parents=True, exist_ok=True)

pages = [
    'index.md',
    'verification.md',
    'datasets.md',
    'hands_on.md',
    'faq.md',
    'issue.md',
    'wbe_101.md',
    'eeg_101.md',
    'glossary.md',
    'casework.md',
    'idea.md',
    'proposals.md',
    'technical_proposal_46.md',
    'technical_proposal_48.md',
    'technical_proposal_61.md',
]

lenses = [
    '初心者が最短で理解できる導入改善',
    '主張の検証可能性（達成条件/反証条件）の明確化',
    '曖昧語の削減と定義の明確化',
    '冗長表現の削減と可読性向上',
    '次に読むべきページへの導線強化',
    '実務的な次アクションの具体化',
    '外部依存事項の切り分けの明確化',
    '誤解されやすい点の先回り説明',
    '段落構造の整理（1段落1メッセージ）',
    'トーン統一（過度な断定を避けた敬体）',
]

assert len(pages) * len(lenses) == 150

meta_rows = []
worker_id = 1
for page in pages:
    for lens in lenses:
        prompt = f'''あなたはWebコンテンツ改善ワーカー {worker_id}/150 です。

対象リポジトリ: /Users/yasufumi/Documents/GitHub/eegflow
対象ファイル: {page}
改善観点: {lens}

タスク:
1. 対象ファイルを読み、改善余地がある箇所を1つだけ選んでください。
2. 実際に差し替え可能な短い文章改善案を1件だけ作ってください。

必須出力形式（JSONのみ。前後の説明文は禁止）:
{{
  "worker_id": {worker_id},
  "file": "{page}",
  "lens": "{lens}",
  "section_hint": "どの節かを短く",
  "problem": "問題点を1文で",
  "before_excerpt": "対象箇所の短い抜粋（40〜160字）",
  "after_text": "置換後の文案（80〜220字）",
  "reason": "改善理由を1〜2文で",
  "priority": "high"
}}

制約:
- 事実関係が不明な新情報を追加しないでください。
- 既存ページの方針（検証可能性・再現性重視）を保ってください。
- HTMLタグは書かず、本文テキストのみ提案してください。
- JSON以外の文字は出力しないでください。
'''
        (PROMPTS / f'worker{worker_id}.txt').write_text(prompt, encoding='utf-8')
        meta_rows.append((worker_id, page, lens))
        worker_id += 1

merge_prompt = '''あなたは統合ワーカーです。
下記の worker 出力 JSON を統合し、ページごとに「採用候補トップ3」をまとめてください。

出力形式（Markdown）:
# Swarm Summary
## by page
### <page>
- 採用候補1: ...
- 採用候補2: ...
- 採用候補3: ...

## global priorities
- 全体で優先度が高い改善を10件
'''
(PROMPTS / 'merge.txt').write_text(merge_prompt, encoding='utf-8')

with (ROOT / 'worker_matrix.csv').open('w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['worker_id', 'file', 'lens'])
    w.writerows(meta_rows)

print('generated', len(meta_rows), 'worker prompts')
