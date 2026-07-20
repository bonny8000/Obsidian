---
type: source
status: active
created: 2026-05-18
tags: [source, ux-research, ai-usability-analysis, reliability]
sources:
  - raw/web/measuringu-ai-usability-problem-analysis-video.md
updated: 2026-06-12
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.86
---

# MeasuringU: AI Reliability for Finding UI Problems

## Citation

Lewis, Jim; Sauro, Jeff; Schiavone, Will; Plabst, Lucas. "How Reliable Is AI at Finding UI Problems?" MeasuringU, 2026-04-28.

URL: https://measuringu.com/ai-usability-problem-analysis-of-a-video/

Raw source card: `raw/web/measuringu-ai-usability-problem-analysis-video.md`

## Summary

This article evaluates whether AI systems produce consistent usability-problem lists when analyzing the same usability-test video multiple times. It is useful for grounding [[concepts/ux-research/ai-usability-analysis|AI Usability Analysis]] in reliability measurement instead of assuming generated insights are stable.

## Key Claims

- AI usability analysis should be evaluated for repeatability.
- Reliability and validity are different; stable outputs are not automatically accurate outputs.
- For the tested video/prompt, Gemini had higher internal reliability than ChatGPT, while cross-model reliability was low.
- UX researchers should avoid treating AI problem lists as stable findings without validation.

## Concepts Linked

- [[concepts/ux-research/ai-usability-analysis|AI Usability Analysis]]
- [[concepts/ux-research/ux-research-automation|UX Research Automation]]
- [[concepts/ux-research/reliability-vs-validity|Reliability vs Validity]]
- [[concepts/ux-research/any-2-agreement|Any-2 Agreement]]
- [[concepts/ux-research/evaluator-effect|Evaluator Effect]]

## Useful Examples

- Current example source: use examples, tables, cases, or named artifacts already present elsewhere in this note; otherwise return to `raw/web/measuringu-ai-usability-problem-analysis-video.md` before asking an LLM for concrete examples.

## Constraints / Caveats

- Coverage is `substantial` and ingest level is `standard`; do not treat this source as fully digested unless `coverage: full`.
- Claims should be checked against `raw/web/measuringu-ai-usability-problem-analysis-video.md` when used for recommendations, metrics, or external-facing work.

## Reliability Notes

Primary source for a small study. The experiment uses one video and one prompt, so conclusions should not be generalized without more data.

## Design Implications

- Use this source to shape research design, UX evidence, method selection, and evaluation prompts.
- Connect it with [[concepts/ux-research/ai-usability-analysis]], [[concepts/ux-research/ux-research-automation]], [[concepts/ux-research/reliability-vs-validity]], [[concepts/ux-research/any-2-agreement]] before turning it into a project recommendation.

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
