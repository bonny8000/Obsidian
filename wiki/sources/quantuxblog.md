---
type: source
status: active
created: 2026-06-10
tags: [source, quant-uxr, research-rigor, synthetic-data, research-methods]
sources:
  - raw/web/quantuxblog-source-collection-2026-06-10
updated: 2026-06-12
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.76
---

# Quantitative UX Research Blog

## Citation

Chapman, Chris, and contributors. Quantitative UX Research Blog. Observed 2026-06-10.

URL: https://quantuxblog.com/

Raw source card: `raw/web/quantuxblog-source-collection-2026-06-10.md`

## Summary

Quantitative UX Research Blog is a quant UXR source collection with posts by Chris Chapman and guests. The homepage describes it as a blog about UX research and quantitative methods, including extra-chapter-like material for Chapman and Rodden's Quantitative User Experience Research.

This ingest captured the homepage inventory plus two selected posts: "Rigor in Quant UX Research" and "Synthetic Survey Data? It's Not Data."

## Key Claims

- Quant UXR rigor should be decision-centered and evidence-centered rather than defined by advanced methods, p-values, large data sets, or rigid protocols.
- Chapman's proposed rigor stack moves from learning and decisions, to data and methods, to stakeholder engagement, to higher-order strategic decisions.
- LLM-generated synthetic survey data should not replace human survey data because it lacks the motivated human response process that surveys are meant to capture.
- Empirical comparisons cited in the synthetic-survey post raise reliability and validity concerns for LLM-generated survey responses.

## Concepts Linked

- [[concepts/ux-research/quant-uxr-rigor|Quant UXR Rigor]]
- [[concepts/ux-research/synthetic-survey-data|Synthetic Survey Data]]
- [[concepts/ux-research/quant-uxr-learning-path|Quant UXR Learning Path]]
- [[concepts/ux-research/validity-and-decision-relevance|Validity and Decision Relevance]]

## Useful Examples

- Current example source: use examples, tables, cases, or named artifacts already present elsewhere in this note; otherwise return to `raw/web/quantuxblog-source-collection-2026-06-10`, `raw/web/quantuxblog-source-collection-2026-06-10.md` before asking an LLM for concrete examples.

## Constraints / Caveats

- Coverage is `substantial` and ingest level is `standard`; do not treat this source as fully digested unless `coverage: full`.
- Claims should be checked against `raw/web/quantuxblog-source-collection-2026-06-10`, `raw/web/quantuxblog-source-collection-2026-06-10.md` when used for recommendations, metrics, or external-facing work.

## Reliability Notes

- Coverage is `substantial` and ingest level is `deep`; do not treat this source as fully digested unless `coverage: full`.
- Claims should be checked against `raw/web/quantuxblog-source-collection-2026-06-10`, `raw/web/quantuxblog-source-collection-2026-06-10.md` when used for recommendations, metrics, or external-facing work.

- Coverage is `substantial` and ingest level is `standard`; do not treat this source as fully digested unless `coverage: full`.

The homepage capture used browser-readable content because the local extractor received a rate-limit response. The selected post summaries are useful for concept extraction, but deeper article-level notes should be created if these posts become central evidence.

## Design Implications

- Use this source to shape research design, UX evidence, method selection, and evaluation prompts.
- Connect it with [[concepts/ux-research/quant-uxr-rigor]], [[concepts/ux-research/synthetic-survey-data]], [[concepts/ux-research/quant-uxr-learning-path]], [[concepts/ux-research/validity-and-decision-relevance]] before turning it into a project recommendation.

## Tensions

- Backfill note: source-specific tensions were not separately extracted in the earlier ingest. Compare this source with related concepts and maps before treating its framing as settled.

## Open Questions

- What evidence, examples, or counterexamples should be extracted from the raw source before marking this as `coverage: full`?
- Which linked concept would change most if this source were contradicted?

## LLM Use

- **Use for:** research design, UX evidence, method selection, and evaluation prompts.
- **Do not use for:** unsupported exact claims beyond the source note's `substantial` coverage.
- **Best prompt pattern:** Ask the LLM to combine this source with its linked concepts, then verify any specific claim against the raw source before final use.

## Backfill Status

- Retrofitted on 2026-06-12 by `scripts/backfill_llm_ready.py` from the existing source note.
- This standardizes the note for LLM use; it does not by itself mean the raw source has been fully re-read.
