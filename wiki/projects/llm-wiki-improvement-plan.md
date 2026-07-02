---
type: project
status: active
created: 2026-06-10
updated: 2026-07-02
tags: [project, meta, wiki-maintenance, canvas, safety]
sources: []
confidence: 0.95
---

# LLM Wiki Improvement Plan

## Objectives

Make the wiki trustworthy, useful for synthesis, visually navigable, and safe for repeated AI maintenance.

## Current Status (2026-07-02)

> [!success] Foundations complete
> - Git is active as the backup/audit layer and the vault has a verified GitHub `main` history.
> - `scripts/lint.py` checks broken links, empty pages, frontmatter, orphans, and content-loss signals.
> - Raw evidence and AI-maintained wiki layers are established.
> - Source-readiness metadata and the LLM-Ready Source Index are in use.
> - The earlier pipe-link and empty-file corruption incidents were repaired or tracked.

> [!info] 2026-07-02 architecture upgrade
> - Added three Obsidian Canvas workflows: three-layer architecture, advanced modules, and safe draft/review/apply.
> - Added [[../playbooks/safe-ingest-promotion-workflow|Safe Ingest Promotion Workflow]].
> - Added [[../maps/llm-wiki-visual-workflows|LLM Wiki Visual Workflows]] as the visual navigation hub.
> - Ollama is installed but has no local models; local drafting remains optional and cannot write directly to the wiki.

> [!warning] Operational decision still open
> Obsidian currently opens `D:\Obsidian`, while the Git repository and maintained vault content are under `D:\Obsidian\LLM-Wiki`. Keep edits in the repository and confirm the intended app root before changing Obsidian configuration.

## Phase 0 — Repair and Baseline (complete)

- [x] Initialize Git and preserve a clean baseline.
- [x] Normalize Windows Git metadata and line endings.
- [x] Repair pipe-stripped links and rebuild recoverable empty pages.
- [x] Preserve raw PDFs and source cards before synthesis.

## Phase 1 — Trustworthy Operations (complete, ongoing enforcement)

- [x] Add vault lint and focused link checks.
- [x] Add source-readiness metadata and a generated-style source index.
- [x] Add draft → review → apply → validation gates.
- [x] Use Git as backup/audit rather than day-to-day note sync.
- [ ] Decide and document the intended Obsidian app root (`D:\Obsidian` vs `D:\Obsidian\LLM-Wiki`).

## Phase 2 — Smarter and More Navigable (in progress)

- [x] Add maps, Bases dashboards, and method/comparison/analysis layers.
- [x] Add Canvas architecture and workflow diagrams.
- [x] Connect web and PDF ingest to the same raw-first promotion path.
- [ ] Keep map "Tensions & Open Questions" sections current as sources accumulate.
- [ ] Reduce the remaining partial-source backlog using original PDFs or authenticated captures.
- [ ] Add a small automated check that Canvas edge targets and linked file nodes exist.

## Phase 3 — Proactive and Optional Modules

- [ ] Configure a local Ollama model only if draft quality, structured output, and review gates pass.
- [ ] Evaluate semantic RAG / GraphRAG against link-and-map retrieval before adopting it.
- [ ] Produce a scheduled weekly digest: changes, stale pages, top open questions, and resurfaced concepts.
- [ ] Add a source watchlist and a review queue without auto-publishing new claims.

## Decision Rules

- The core stays Raw → Source → Concept/Method/Map → Index/Log.
- Optional modules may draft or retrieve, but cannot bypass provenance, review, or lint.
- A Canvas improves comprehension; it does not raise evidence confidence.
- Completion metrics never substitute for validity, trust, or ethics metrics.

## Related

- [[../maps/llm-wiki-architecture|LLM Wiki Architecture]]
- [[../maps/llm-wiki-visual-workflows|LLM Wiki Visual Workflows]]
- [[../playbooks/safe-ingest-promotion-workflow|Safe Ingest Promotion Workflow]]
