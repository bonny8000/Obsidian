#!/usr/bin/env python3
"""Regenerate wiki/maps/research-agenda.md from Open questions sections.
Run from vault root: python3 scripts/harvest_questions.py
(Keeps the manually written 'Recurring themes' section if present.)"""
import os, re, collections, datetime
WIKI='wiki/concepts'
rows=[]
for dp,_,fns in os.walk(WIKI):
    for fn in fns:
        if not fn.endswith('.md'): continue
        p=os.path.join(dp,fn)
        s=open(p,encoding='utf-8').read()
        m=re.search(r'#+\s*(?:❓\s*)?Open [Qq]uestions?\s*\n(.*?)(?=\n#|\Z)',s,re.S)
        if m:
            rel=p.replace('wiki/','').replace('.md','').replace('\\','/')
            for q in m.group(1).strip().split('\n'):
                q=q.strip('- ').strip()
                if len(q)>15: rows.append((rel,q))
openr=[(r,q) for r,q in rows if not q.startswith('[Answered')]
target='wiki/maps/research-agenda.md'
themes=''
if os.path.exists(target):
    old=open(target,encoding='utf-8').read()
    m=re.search(r'(## Recurring themes.*?)(?=\n## [A-Z])',old,re.S)
    if m: themes=m.group(1)
today=datetime.date.today().isoformat()
by=collections.defaultdict(list)
for r,q in openr: by[r.split('/')[1] if r.count('/')>=2 else 'other'].append((r,q))
names={'ux-research':'UX Research','ai-agents':'AI Agents','product-management':'Product Management','robotics-spatial':'Robotics & Spatial AI','infrastructure-dev':'Infrastructure & Dev','other':'Other'}
out=[f"---\ntype: map\nstatus: active\ncreated: 2026-06-10\nupdated: {today}\ntags: [map, research-agenda, open-questions]\nsources: []\nconfidence: 0.9\n---\n\n# Research Agenda — Open Questions Across the Wiki\n\nAuto-harvested ({len(openr)} open, {len(rows)-len(openr)} answered). Regenerate: `python3 scripts/harvest_questions.py`.\n", themes]
for c,label in names.items():
    qs=by.get(c,[])
    if not qs: continue
    out.append(f"\n## {label} ({len(qs)})\n")
    for r,q in sorted(qs): out.append(f"- {q} — [[{r}|{r.split('/')[-1]}]]")
open(target,'w',encoding='utf-8').write('\n'.join(o for o in out if o)+'\n')
print('open:',len(openr))
