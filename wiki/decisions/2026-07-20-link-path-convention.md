---
type: decision
status: active
created: 2026-07-20
updated: 2026-07-20
tags: [decision, vault-maintenance, linking]
sources: []
---

# Decision: Canonical Wiki-Link Path Convention

## Context & Background

The vault mixes three link styles for the same targets: vault-rooted (`[[wiki/concepts/...]]`), wiki-relative (`[[concepts/...]]`), and bare basenames. Obsidian resolves all three via shortest-path matching, so nothing is broken for a human — but external tooling (link checkers, RAG indexers, `scripts/rag_query.py`) must special-case every style, and the 2026-07-20 lint produced false positives for exactly this reason.

## Options Considered

1. **Bulk-rewrite all ~6,700 links to one style now.** Maximum consistency, but a high-risk mechanical edit across 600+ files for a problem Obsidian itself doesn't have.
2. **Declare a canonical style for all *new/edited* links; leave history alone.** Consistency converges over time at near-zero risk.
3. **Do nothing.** Tooling stays noisy forever.

## Decision Made

**Option 2.** The canonical form is the **vault-rooted path without leading slash**: `[[wiki/concepts/ux-research/cognitive-load|Cognitive Load]]`. Agents writing or editing any page use this form; existing links are normalized opportunistically when a page is touched for other reasons, never as a standalone bulk rewrite.

## Evidence & Justification

- 2026-07-20 lint: 28 of 28 residual "broken" flags were path-style artifacts, not real breakage.
- Bulk rewrites carry the same risk class as the backfill-script incident (66 damaged files) — see [[wiki/decisions/2026-07-20-script-maintenance-gates|Script Maintenance Gates]].

## Consequences & Next Steps

- AGENTS.md Naming section now states the canonical form.
- `wiki/_templates/` placeholders keep their illustrative `[[concepts/|]]` forms; linters should whitelist `_templates/`.
- Revisit option 1 only if a RAG pipeline demonstrably needs it.
