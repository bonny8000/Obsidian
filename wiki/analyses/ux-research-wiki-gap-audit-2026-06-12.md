---
type: analysis
status: active
created: 2026-06-12
updated: 2026-06-12
tags: [analysis, ux-research, vault-audit]
sources:
  - maps/llm-ready-source-index
  - maps/ai-ux-research-methods
  - maps/research-methods-knowledge-base
  - maps/ux-metrics-framework
confidence: 0.86
---

# Analysis: UX Research Wiki Gap Audit - 2026-06-12

## Research Question

Is this vault already more complete than the reference UX research wiki schema, and what should be added to make it work like a dedicated UX research knowledge base?

## Evidence Base

- Current vault structure includes `raw/`, `wiki/sources/`, `wiki/concepts/`, `wiki/maps/`, scripts, dashboard, logs, projects, decisions, playbooks, and queries.
- Source backfill tracks 68 source pages, 50 marked `llm_ready: true`, 19 deep, 44 standard, and 5 light.
- UX research concepts already exist under `wiki/concepts/ux-research/`.
- The reference schema emphasizes an operating manual, immutable raw files, index/log, overview, source records, method records, comparison tables, and analyses.

## Synthesis

The current vault is broader and more technically mature than the reference screenshot because it already has a source graph, concept graph, maps, scripts, linting, Git audit, and LLM-readiness fields. It was less complete as a dedicated UX research wiki because it lacked first-class method pages, comparison matrices, analysis memos, a top-level catalog, and a full `CLAUDE.md` schema.

This pass closes that structural gap by adding `wiki/methods/`, `wiki/comparisons/`, `wiki/analyses/`, `wiki/overview.md`, root `index.md`, root `log.md`, and a more explicit `CLAUDE.md`.

## Implications

- The vault can now support a UX research workflow: question -> method -> source evidence -> comparison -> analysis memo.
- LLM ideation can be more grounded because source readiness and method selection are explicit.
- Future ingest should not only summarize sources; it should update relevant method pages, comparison tables, and analysis memos.

## Risks And Counterpoints

- Starter method pages are seeded from existing source notes and concepts; they should be deepened with richer examples and templates.
- Not all source pages are `coverage: full`; some are safe for ideation but not decision evidence.
- The method library is currently focused on the strongest existing evidence areas: usability, interviews, metrics, MaxDiff, thematic analysis, and AI-assisted synthesis.

## Next Research Actions

- Expand methods for diary studies, field studies, concept testing, card sorting, tree testing, benchmark studies, and longitudinal research.
- Add example study plans and reusable interview/discussion guide templates.
- Promote partial source notes by revisiting raw captures and extracting examples, caveats, and method-specific guidance.
- Add project-specific analysis memos when the vault is used for an actual product decision.

