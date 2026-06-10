---
type: project
status: active
created: 2026-06-10
updated: 2026-06-10
tags: [project, meta, wiki-maintenance]
sources: []
confidence: 0.9
---

# LLM Wiki Improvement Plan

## Objectives

Make the wiki (1) trustworthy — no silent data loss, (2) smarter — deeper synthesis, not just ingestion, and (3) proactive — it tells Bonny things instead of waiting to be asked.

## Current Status (audit, 2026-06-10)

The vault is in good shape structurally: 564 notes, clear directory contract (AGENTS.md), templates, maps, and a disciplined change log. But the audit found real damage:

> [!warning] Findings
> 1. **25 corrupted/empty files** (0 or 3 bytes): 9 source pages, 4 concept pages, 6 query pages, 5 ingest reports, and the `ux-metrics-framework` map. Two corruption events: 2026-05-27 (files containing only `---`) and 2026-06-01 05:06 (zeroed files). Content described in the change log (Tullis & Albert, Chapman & Rodden, Adobe HAIC, VR Usability, Garrett/Cooper ingests) is **lost** and must be rebuilt.
> 2. **124 files contain pipe-stripped wikilinks** — `[[concepts/ai-agents/agentic-ai|Agentic AI]]` instead of `[[concepts/ai-agents/agentic-ai|Agentic AI]]`. These links are broken in Obsidian's graph and navigation. Likely a tool/sync pass removed `|` characters.
> 3. **No version control.** The vault is not a git repo, which is why the corruption was silent and unrecoverable.

## Phase 0 — Repair (do first)

1. **Init git** in the vault and commit everything as a baseline before any mass edit. Add `.obsidian/workspace*` to `.gitignore`.
2. **Fix pipe-stripped links** with a script (regex: kebab-path immediately followed by a capital letter → reinsert `|`). Verify with a dry-run diff, then commit.
3. **Rebuild the 25 empty pages.** Raw material still exists for some (`raw/web/`, `raw/files/`); books (Tullis & Albert, Cooper, Garrett) need re-ingest from PDFs or summaries. Track each in a rebuild checklist.
4. **Find the corruption cause** before trusting any sync/plugin again — check Obsidian plugins, sync tools, and any script run on 2026-05-27 and 2026-06-01.

## Phase 1 — Trustworthy

- **Lint script** (`scripts/lint.py`): broken/pipe-stripped links, empty or stub files, missing frontmatter, orphans, claims without sources. Writes `wiki/logs/lint-report.md`. Run after every ingest.
- **Git commit per ingest** — the change log gets a verifiable diff behind it.

## Phase 2 — Smarter

- **Work the deep-ingest backlog**: Sauro & Lewis 2e ([[sources/sauro-lewis-quantifying-ux-2016]]) chapters → adjusted-Wald CI, sample-size models, standardized questionnaires (SUS/PSSUQ/SUPR-Q), problem-discovery model. Same for rebuilt book sources.
- **Synthesis over collection**: for each map, add a "Tensions & open questions" section that contrasts sources (e.g., MeasuringU AI-analysis skepticism vs. AI-moderated-research optimism). Concept pages already have `Open questions` — harvest them into a single **research agenda** note (`wiki/maps/research-agenda.md`) ranked by how often a question recurs.
- **Bases dashboards**: extend `dashboard.base` — stale pages (updated > 60 days), low-confidence claims (< 0.7), draft-status pages. Obsidian then shows what needs attention on open.

## Phase 3 — Proactive

- **Scheduled weekly digest** (Cowork scheduled task): what changed, what went stale, top 3 open questions, 1–2 suggested next sources based on gaps. Saved to `wiki/logs/` + shown in chat.
- **Inbox workflow**: drop anything into `raw/inbox/`; the agent proposes (not auto-applies) source pages and concept links on the next session.
- **Source watchlist**: a note listing feeds worth monitoring (MeasuringU, QuantUXBlog, arXiv HCI queries, brunch authors already in the vault); the weekly task checks them and queues candidates.
- **Resurfacing**: weekly digest includes 3 older concepts related to currently active projects, to keep past knowledge in circulation.

## Key Decisions

- [ ] UXDR: adopt git as the vault's safety layer (Phase 0.1) — record in `wiki/decisions/` once done.

## Tasks & Next Steps

- [ ] Phase 0.1 git init + baseline commit
- [ ] Phase 0.2 pipe-link repair script + dry run + apply
- [ ] Phase 0.3 rebuild checklist for 25 empty pages
- [ ] Phase 0.4 identify corruption cause
- [ ] Phase 1 lint script
- [ ] Phase 2 Sauro & Lewis deep ingest (chapters 3, 6–8 first — highest reuse for quant UXR work)
- [ ] Phase 3 schedule weekly digest task
