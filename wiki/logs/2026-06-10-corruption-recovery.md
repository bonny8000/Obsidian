---
type: log
status: active
created: 2026-06-10
updated: 2026-06-10
tags: [log, maintenance, recovery]
sources: []
confidence: 0.95
---

# 2026-06-10 Corruption Recovery Log

Two corruption events zeroed or truncated 25 wiki files: **2026-05-27** (files reduced to `---`, 3 bytes) and **2026-06-01 ~05:06** (files zeroed, 0 bytes). No version control existed, so original content is unrecoverable locally. Git was initialized 2026-06-10 to prevent recurrence.

Suspected cause: a sync/tool layer mishandling atomic writes (the same layer was observed writing null bytes during git setup on 2026-06-10). Pipe-stripping of 590 wikilinks across 125 files (fixed by script, see git commit) may share the cause.

## Status of the 25 files

**Rebuilt from raw/ (full):** sources/bucketplace-pretendard-jp-2026-04-17, sources/manyfast-homepage, sources/medium-harizlim-ai-qualitative-research-2026, concepts/infrastructure-dev/font-subsetting, concepts/infrastructure-dev/localization-ux.

**Rebuilt from backlink context (verify):** concepts/ux-research/human-in-the-loop, concepts/product-management/fpa-central, maps/ux-metrics-framework.

**Citation stub — needs re-ingest from original work:** sources/tullis-albert-measuring-ux-2013, sources/chapman-rodden-quant-uxr-2023, sources/cooper-about-face-4-2014, sources/garrett-elements-ux-2011, sources/gerhard-norton-vr-usability-2022, sources/andru-saksena-adobe-haic-2025.

**Tombstone — regenerate on demand:** 6 query pages dated 2026-05-27 (re-ask the questions), 5 ingest reports dated 2026-05-27 (superseded; change-log entries survive).

## Next steps

- [ ] Re-ingest the 6 book/paper sources (locate PDFs or re-summarize).
- [ ] Verify the 3 context-rebuilt pages against raw sources.
- [ ] Identify the corrupting tool/plugin before trusting bulk operations (check what ran 05-27 and 06-01 05:06).
