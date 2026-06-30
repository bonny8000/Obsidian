#!/usr/bin/env python3
"""LLM-Wiki lint: run from vault root -> writes wiki/logs/lint-report.md
Checks: pipe-stripped links, broken link targets, empty/stub files,
missing frontmatter, orphaned concepts, lost-content stubs."""
import os, re, sys, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(ROOT, 'wiki')
today = datetime.date.today().isoformat()

pages = {}   # rel path (no .md) -> abs path
texts = {}
for dp, dns, fns in os.walk(WIKI):
    for fn in fns:
        if fn.endswith('.md'):
            p = os.path.join(dp, fn)
            rel = os.path.relpath(p, WIKI).replace('\\', '/')[:-3]
            pages[rel] = p
            try:
                texts[rel] = open(p, encoding='utf-8').read()
            except Exception as e:
                texts[rel] = ''

issues = {k: [] for k in ['pipe_stripped', 'broken_links', 'empty', 'no_frontmatter', 'orphans', 'lost_content']}

link_pat = re.compile(r'\[\[([^\]\|#]+)(?:#[^\]\|]*)?(?:\|[^\]]*)?\]\]')
stripped_pat = re.compile(r'\[\[[a-z0-9][a-z0-9_/-]*[a-z0-9][A-Z][^\]\[\|]*\]\]')
basenames = {r.split('/')[-1]: r for r in pages}
linked = set()

for rel, s in texts.items():
    if rel == 'logs/lint-report' or rel.startswith('_templates/'):
        continue  # skip generated report + template scaffolds (intentional [[concepts/]] placeholders)
    if len(s.strip()) < 40:
        issues['empty'].append(rel)
    if not s.lstrip('﻿').startswith('---'):
        issues['no_frontmatter'].append(rel)
    if ('lost-content' in s or 'Rebuilt stub' in s or 'Answer lost' in s) and not rel.startswith('logs/'):
        issues['lost_content'].append(rel)  # logs/ legitimately mention these terms; they are not content stubs
    for m in stripped_pat.finditer(s):
        issues['pipe_stripped'].append(f'{rel}: {m.group(0)[:60]}')
    for m in link_pat.finditer(s):
        t = m.group(1).strip()
        if t.startswith('raw/') or t.startswith('http') or '.' in t.split('/')[-1]:
            continue
        key = t[5:] if t.startswith('wiki/') else t
        if key in pages or key.split('/')[-1] in basenames:
            linked.add(key if key in pages else basenames[key.split('/')[-1]])
        else:
            issues['broken_links'].append(f'{rel} -> [[{t}]]')

for rel in pages:
    if rel.startswith('concepts/') and rel not in linked:
        issues['orphans'].append(rel)

out = [f"""---
type: log
status: active
created: {today}
updated: {today}
tags: [log, lint]
sources: []
confidence: 1.0
---

# Lint Report - {today}
"""]
labels = {'pipe_stripped': 'Pipe-stripped links', 'broken_links': 'Broken link targets',
          'empty': 'Empty/near-empty pages', 'no_frontmatter': 'Missing frontmatter',
          'orphans': 'Orphaned concepts (no inbound links)', 'lost_content': 'Lost-content stubs awaiting re-ingest'}
for k, label in labels.items():
    v = sorted(set(issues[k]))
    out.append(f"\n## {label}: {len(v)}\n")
    for item in v[:50]:
        out.append(f"- `{item}`")
    if len(v) > 50:
        out.append(f"- ... and {len(v)-50} more")

report = '\n'.join(out) + '\n'
open(os.path.join(WIKI, 'logs', 'lint-report.md'), 'w', encoding='utf-8', newline='\n').write(report)
print(f"pages: {len(pages)}")
for k in labels: print(f"{k}: {len(set(issues[k]))}")
