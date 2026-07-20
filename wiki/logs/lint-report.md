---
type: log
status: active
created: 2026-07-12
updated: 2026-07-20
tags: [log, lint]
sources: []
confidence: 1.0
---

# Lint Report - 2026-07-20

Full-vault health check after the restructure. 6,651 wiki-links scanned across 160 sources, 305 concepts, 15 maps, 73 queries.

## Backfill boilerplate duplication: 66 → 0 (fixed)

`scripts/backfill_llm_ready.py` had written identical coverage/claims boilerplate into both `Constraints / Caveats` and `Reliability Notes` (2-3 copies per file). 20 of those files also claimed ``ingest level is `deep` `` in the body while frontmatter said `standard`. All 66 cleaned; ingest-level text now matches frontmatter everywhere. Real Reliability content (warning callouts, prose) preserved.

## Broken link targets: 8 → 0 (fixed)

Created the three concept pages that the 2026-07-20 cognitive-science ingest linked but never wrote:
- `wiki/concepts/ux-research/cognitive-load` (was referenced by 6 pages)
- `wiki/concepts/ux-research/mental-models`
- `wiki/concepts/ux-research/heuristics-and-biases`

Remaining unresolved link-like strings are intentional placeholders in `wiki/_templates/` (`[[concepts/...]]`, `[[sources/...]]`, `[[decisions/...]]`) and folder references in `wiki/maps/llm-wiki-architecture.md` — not treated as defects.

## Index defects: 3 → 0 (fixed)

- Mojibake "??rebuilt" → "— rebuilt" (2 lines in root `index.md`).
- Duplicate `measuringu-statistics-30-participants` entry removed from Recent Ingests.

## Contract drift: 1 → 0 (fixed)

- `wiki/drafts/` existed on disk but was missing from the AGENTS.md directory contract; documented as the Safe Ingest staging area.

## Flagged for Bonny (not changed)

- `test.txt` junk file at vault root.
- Two orphaned raw captures in outer `D:\Obsidian\raw\` (`ai-in-quantitative-research.md`, `what-LLM-can-and-cannot-find.md`) sit outside the vault; likely staging leftovers — move into `LLM-Wiki/raw/web/` and ingest, or delete.
- `D:\Obsidian` root has a broken/empty `.git` folder (git says "not a repository") plus its own `.obsidian`; consider removing the stray `.git` to avoid confusion with the real repo inside `LLM-Wiki`.
- Untracked scripts in the vault repo: `scripts/obsidian-safe.py`, `scripts/rag_query.py` — commit or ignore.
- Stale full copy of the old vault remains at `C:\Users\bonny_chen\LLM-Wiki`; it still receives edits from tooling and risks split-brain. Archive or delete after confirming nothing unique remains.

## Lost-content stubs awaiting re-ingest: 4 (carried over from 2026-07-12)

- `sources/andru-saksena-adobe-haic-2025`
- `sources/cooper-about-face-4-2014`
- `sources/garrett-elements-ux-2011`
- `sources/gerhard-norton-vr-usability-2022`
