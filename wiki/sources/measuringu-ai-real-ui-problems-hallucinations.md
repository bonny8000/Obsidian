---
type: source
status: active
created: 2026-06-10
tags: [source, ux-research, ai-usability-analysis, hallucination, false-alarm, evaluator-effect]
sources:
  - raw/web/measuringu-ai-real-ui-problems-hallucinations-2026-05-26
updated: 2026-06-12
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.88
---

# MeasuringU: Does AI Find Real UI Problems or Just Hallucinations?

## Citation

Lewis, Jim; Sauro, Jeff; Schiavone, Will; Plabst, Lucas. "Does AI Find Real UI Problems or Just Hallucinations?" MeasuringU, 2026-05-26.

URL: https://measuringu.com/does-ai-find-real-ui-problems-or-just-hallucinations/

Raw source card: `raw/web/measuringu-ai-real-ui-problems-hallucinations-2026-05-26.md`

## Summary

This article tests whether AI-only usability problems from a video review are genuine human misses, false alarms, or hallucinations. It extends the earlier MeasuringU reliability article by adding a validity-oriented classification layer.

The useful takeaway for the wiki is that AI usability analysis can add signal, but the AI-only issue list should be triaged before it is treated as research evidence.

## Extracted Data

| Measure | Reported value |
| --- | --- |
| Human researchers | 4 |
| AI systems | ChatGPT-5.4 Thinking and Gemini 3 Flash Thinking |
| Runs per AI | 4 |
| Human-identified usability problems | 9 |
| Combined AI-identified problems | 14 |
| AI-only problems | 11 |
| AI-only genuine finds | 1 of 11 |
| AI-only false alarms | 7 of 11 |
| AI-only hallucinations | 3 of 11 |

## Key Claims

- AI-only usability problems should be classified before they enter a findings list.
- In this study, roughly nine out of ten AI-only problems needed correction or dismissal.
- False alarms were more common than hallucinations; they came from real observations interpreted as the wrong usability claim.
- Human oversight is still necessary because hallucinations cannot be detected without checking the original video evidence.
- Multiple AI runs may help flag consistency patterns, but consistency is not validity.

## Concepts Linked

- [[concepts/ux-research/ai-usability-analysis|AI Usability Analysis]]
- [[concepts/ux-research/ai-usability-false-alarm-triage|AI Usability False-Alarm Triage]]
- [[concepts/ux-research/reliability-vs-validity|Reliability vs Validity]]
- [[concepts/ux-research/evaluator-effect|Evaluator Effect]]
- [[concepts/ux-research/validity-and-decision-relevance|Validity and Decision Relevance]]

## Useful Examples

- Current example source: use examples, tables, cases, or named artifacts already present elsewhere in this note; otherwise return to `raw/web/measuringu-ai-real-ui-problems-hallucinations-2026-05-26`, `raw/web/measuringu-ai-real-ui-problems-hallucinations-2026-05-26.md` before asking an LLM for concrete examples.

## Constraints / Caveats

- Coverage is `substantial` and ingest level is `standard`; do not treat this source as fully digested unless `coverage: full`.
- Claims should be checked against `raw/web/measuringu-ai-real-ui-problems-hallucinations-2026-05-26`, `raw/web/measuringu-ai-real-ui-problems-hallucinations-2026-05-26.md` when used for recommendations, metrics, or external-facing work.

## Reliability Notes

- Claims should be checked against `raw/web/measuringu-ai-real-ui-problems-hallucinations-2026-05-26`, `raw/web/measuringu-ai-real-ui-problems-hallucinations-2026-05-26.md` when used for recommendations, metrics, or external-facing work.

Primary source for a small MeasuringU study. The article is useful evidence for building review rubrics, but it should not be generalized as a population estimate because it uses one video, one prompt setup, and two LLM families.

## Design Implications

- Use this source to shape research design, UX evidence, method selection, and evaluation prompts.
- Connect it with [[concepts/ux-research/ai-usability-analysis]], [[concepts/ux-research/ai-usability-false-alarm-triage]], [[concepts/ux-research/reliability-vs-validity]], [[concepts/ux-research/evaluator-effect]] before turning it into a project recommendation.

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
