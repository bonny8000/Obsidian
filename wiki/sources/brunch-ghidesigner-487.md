---
type: source
status: active
created: 2026-05-18
tags: [source, llm-wiki, design]
sources:
  - raw/web/brunch-ghidesigner-487.md
updated: 2026-06-12
ingest_level: deep
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.8
---

# AI Designer LLM Wiki Article

## Citation

Yoo Hoon-sik professor. "AI Designer LLM Wiki." Brunch, retrieved 2026-05-18.

URL: https://brunch.co.kr/@ghidesigner/487

Raw source card: `raw/web/brunch-ghidesigner-487.md`

## Summary

The article explains the LLM Wiki idea for designers. It presents a workflow where an AI agent compiles raw sources into a persistent Markdown wiki that can be viewed and navigated in Obsidian.

## Key Claims

- The LLM Wiki pattern is meant to reduce the loss of useful knowledge between isolated AI chat sessions.
- The recommended architecture includes immutable raw sources, an AI-maintained wiki layer, and a schema/instruction layer.
- The main operations are ingesting sources, querying the compiled wiki, and linting the knowledge base.
- Obsidian is useful because it reads local Markdown files and provides graph-based navigation.

## Concepts Linked

- [[concepts/infrastructure-dev/llm-wiki|LLM Wiki]]
- [[concepts/product-management/compounding-knowledge|Compounding Knowledge]]
- [[concepts/ai-agents/ai-maintained-wiki|AI-Maintained Wiki]]
- [[concepts/infrastructure-dev/knowledge-linting|Knowledge Linting]]

## Useful Examples

- Current example source: use examples, tables, cases, or named artifacts already present elsewhere in this note; otherwise return to `raw/web/brunch-ghidesigner-487.md` before asking an LLM for concrete examples.

## Constraints / Caveats

- Coverage is `substantial` and ingest level is `deep`; do not treat this source as fully digested unless `coverage: full`.
- Claims should be checked against `raw/web/brunch-ghidesigner-487.md` when used for recommendations, metrics, or external-facing work.

## Reliability Notes

This page is a paraphrased source summary. Verify specific historical claims or tool recommendations against primary sources before treating them as final.

## Design Implications

- Use this source to shape product strategy, roadmap framing, operating model, and prioritization prompts.
- Connect it with [[concepts/infrastructure-dev/llm-wiki]], [[concepts/product-management/compounding-knowledge]], [[concepts/ai-agents/ai-maintained-wiki]], [[concepts/infrastructure-dev/knowledge-linting]] before turning it into a project recommendation.

## Tensions

- Backfill note: source-specific tensions were not separately extracted in the earlier ingest. Compare this source with related concepts and maps before treating its framing as settled.

## Open Questions

- What evidence, examples, or counterexamples should be extracted from the raw source before marking this as `coverage: full`?
- Which linked concept would change most if this source were contradicted?

## LLM Use

- **Use for:** product strategy, roadmap framing, operating model, and prioritization prompts.
- **Do not use for:** unsupported exact claims beyond the source note's `substantial` coverage.
- **Best prompt pattern:** Ask the LLM to combine this source with its linked concepts, then verify any specific claim against the raw source before final use.

## Backfill Status

- Retrofitted on 2026-06-12 by `scripts/backfill_llm_ready.py` from the existing source note.
- This standardizes the note for LLM use; it does not by itself mean the raw source has been fully re-read.
