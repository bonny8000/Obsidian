---
type: source
status: active
created: 2026-06-08
tags: [ux-research, researchops, recruiting, screening, participant-selection]
sources:
  - raw/web/linkedin-user-selection-criteria-2026-05-14.md
updated: 2026-06-12
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.7
---

# LinkedIn: Is This User Really Our User?

## Citation

UX 리서치에 관심 있는 사람. (2026-05-14). *이 사용자, 진짜 우리 유저?* LinkedIn public post. Retrieved 2026-06-08 from the provided LinkedIn URL.

## Source Type

LinkedIn public social post summarizing participant recruiting guidance.

## Location

- Raw source card: `raw/web/linkedin-user-selection-criteria-2026-05-14.md`
- Original URL: https://www.linkedin.com/posts/%EC%9D%B4-%EC%82%AC%EC%9A%A9%EC%9E%90-%EC%A7%84%EC%A7%9C-%EC%9A%B0%EB%A6%AC-%EC%9C%A0%EC%A0%80-ugcPost-7460553832729796608-dOjl/

## Summary

The post argues that demographic filters are not enough for UX research recruiting. A stronger screener separates three axes: inclusion criteria based on actual behavior, exclusion criteria for people who would distort results despite qualifying on paper, and diversity criteria that prevent one segment from dominating the sample.

## Key Claims

- Screening should ask about actual behavior and experience, not only demographic identity.
- Exclusion criteria are a separate design decision; they filter people who pass inclusion but would reduce evidence quality.
- Diversity should be planned as a matrix across behavior and relevant demographic or contextual dimensions.
- Bad recruiting can quietly distort analysis and downstream product decisions.
- The post references NN/g guidance from May 2026; that primary source should be ingested before treating this as a formal standard.

## Concepts Linked

- [[concepts/ux-research/participant-selection-criteria|Participant Selection Criteria]]
- [[concepts/ux-research/ai-recruitment|AI Recruitment]]
- [[concepts/ux-research/research-operations|Research Operations]]
- [[concepts/ux-research/research-methods-foundations|Research Methods Foundations]]

## Useful Examples

- Current example source: use examples, tables, cases, or named artifacts already present elsewhere in this note; otherwise return to `raw/web/linkedin-user-selection-criteria-2026-05-14.md` before asking an LLM for concrete examples.

## Constraints / Caveats

- Coverage is `substantial` and ingest level is `standard`; do not treat this source as fully digested unless `coverage: full`.
- Claims should be checked against `raw/web/linkedin-user-selection-criteria-2026-05-14.md` when used for recommendations, metrics, or external-facing work.

## Reliability Notes

- This is a secondary social summary, not the primary NN/g article it references.
- Confidence is capped until the original NN/g guidance is ingested and checked.

## Design Implications

- Use this source to shape research design, UX evidence, method selection, and evaluation prompts.
- Connect it with [[concepts/ux-research/participant-selection-criteria]], [[concepts/ux-research/ai-recruitment]], [[concepts/ux-research/research-operations]], [[concepts/ux-research/research-methods-foundations]] before turning it into a project recommendation.

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
