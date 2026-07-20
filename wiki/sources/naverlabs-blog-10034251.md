---
type: source
status: active
created: 2026-05-18
tags: [source, naver-labs, hri, elevator-robotics]
sources:
  - raw/web/naverlabs-blog-10034251.md
updated: 2026-06-12
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.85
---

# NAVER LABS: Robot Elevator Boarding Acceptance

## Citation

NAVER LABS. "로봇이 타기엔 너무 붐비나요? - 엘리베이터 속 인간과 로봇의 공존을 위한 탑승 수용성 연구." NAVER LABS Blog, 2026-05-07.

URL: https://www.naverlabs.com/blogDetail?seq=10034251

Raw source card: `raw/web/naverlabs-blog-10034251.md`

## Summary

This article summarizes research on when people accept or reject a delivery robot entering an elevator. It introduces [[concepts/robotics-spatial/robot-boarding-area|Robot Boarding Area]] and highlights that robot boarding decisions must account for social comfort, not only physical clearance.

## Key Claims

- Elevator robots need a decision model for whether to board, not only how to board.
- People judge robot boarding acceptability using both crowding level and whether a practical entry space remains available.
- In crowded settings, giving up and waiting can produce a better user experience than forcing entry.

## Concepts Linked

- [[concepts/robotics-spatial/human-robot-interaction|Human-Robot Interaction]]
- [[concepts/robotics-spatial/robot-boarding-area|Robot Boarding Area]]
- [[concepts/robotics-spatial/socially-aware-navigation|Socially Aware Navigation]]
- [[concepts/robotics-spatial/physical-ai|Physical AI]]

## Useful Examples

- Current example source: use examples, tables, cases, or named artifacts already present elsewhere in this note; otherwise return to `raw/web/naverlabs-blog-10034251.md` before asking an LLM for concrete examples.

## Constraints / Caveats

- Coverage is `substantial` and ingest level is `standard`; do not treat this source as fully digested unless `coverage: full`.
- Claims should be checked against `raw/web/naverlabs-blog-10034251.md` when used for recommendations, metrics, or external-facing work.

## Reliability Notes

Primary organizational source from NAVER LABS. The underlying ACM CHI 2026 paper should be collected later for formal method and evidence details.

## Design Implications

- Use this source to shape research design, UX evidence, method selection, and evaluation prompts.
- Connect it with [[concepts/robotics-spatial/robot-boarding-area]], [[concepts/robotics-spatial/human-robot-interaction]], [[concepts/robotics-spatial/socially-aware-navigation]], [[concepts/robotics-spatial/physical-ai]] before turning it into a project recommendation.

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
