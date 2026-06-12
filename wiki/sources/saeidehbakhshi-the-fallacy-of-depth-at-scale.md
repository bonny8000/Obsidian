---
type: source
status: active
created: 2026-06-01
tags: [source, ux-research, ai, qualitative-research]
updated: 2026-06-12
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.90
---

# The Fallacy of Depth at Scale

## Citation

- **Author:** Saeideh Bakhshi
- **Date Added:** 2026-06-01
- **Location:** `raw/2026-06-01-the-fallacy-of-depth-at-scale.md`
- **URL:** [saeidehbakhshi.substack.com](https://saeidehbakhshi.substack.com/p/the-fallacy-of-depth-at-scale?triedRedirect=true)
- **Source Type:** Substack Article

## Summary

The article argues that AI-moderated interviews are a new research affordance, not a substitute for traditional methods. The "depth at scale" framing collapses distinct methodological properties. AI-moderated research provides follow-up to volunteered language at scale, but fails to address sample bias, behavioral observation, or valid prevalence measurement. Methods should be chosen based on their core primitives (surveys for prevalence, depth interviews for mechanism, open text for hypothesis generation, and AI interviews for probed discovery at scale).

## Key Claims

- **Scale does not fix bias:** More responses just give more of the same sample skew (nonresponse, fluency bias). Instrument bias holds at any size.
- **AI moderation adds one real capability:** Probed language/follow-up at machine scale.
- **AI interviews miss the unsaid:** They cannot measure observed behavior, introspectively inaccessible reasons, or capture data from silently disengaged users.
- **Errors do not average out:** Sample problems (who produces data) and instrument problems (what happens to data) are structural, not statistical.

## Concepts Linked

- [[concepts/ux-research/ai-moderated-interviews|AI-Moderated Interviews]]
- [[concepts/ux-research/ux-research-automation|UX Research Automation]]
- [[concepts/ux-research/reliability-vs-validity|Reliability vs Validity]]

## Useful Examples

- Current example source: use examples, tables, cases, or named artifacts already present elsewhere in this note; otherwise return to `raw/2026-06-01-the-fallacy-of-depth-at-scale.md` before asking an LLM for concrete examples.

## Constraints / Caveats

- Coverage is `substantial` and ingest level is `standard`; do not treat this source as fully digested unless `coverage: full`.
- Claims should be checked against `raw/2026-06-01-the-fallacy-of-depth-at-scale.md` when used for recommendations, metrics, or external-facing work.

## Reliability Notes

- Coverage is `substantial` and ingest level is `deep`; do not treat this source as fully digested unless `coverage: full`.
- Claims should be checked against `raw/2026-06-01-the-fallacy-of-depth-at-scale.md` when used for recommendations, metrics, or external-facing work.

- Coverage is `substantial` and ingest level is `standard`; do not treat this source as fully digested unless `coverage: full`.

> [!warning] Caveats
> Reliability was not assessed in the earlier note. Treat this source as a prompt for exploration until raw evidence is checked.

## Design Implications

- Use this source to shape research design, UX evidence, method selection, and evaluation prompts.
- Connect it with [[concepts/ux-research/ai-moderated-interviews]], [[concepts/ux-research/ux-research-automation]], [[concepts/ux-research/reliability-vs-validity]] before turning it into a project recommendation.

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
