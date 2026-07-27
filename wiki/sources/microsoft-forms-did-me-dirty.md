---
type: source
status: active
created: 2026-07-27
updated: 2026-07-27
tags: [source, ux-research, survey, ranking, data-quality]
sources:
  - raw/web/2026-07-27-microsoft-forms-did-me-dirty.md
confidence: 0.8
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
---

# Microsoft Forms Did Me Dirty

## Citation

Trevor Calabro, “Microsoft Forms Did Me Dirty,” Substack, retrieved 2026-07-27. [Original article](https://trevorcalabro.substack.com/p/microsoft-forms-did-me-dirty)

## Source Type

Practitioner case report on validating third-party ranking analysis.

## Location

`raw/web/2026-07-27-microsoft-forms-did-me-dirty.md`

## Summary

The author found a questionable winner in a 32-person force-ranking exercise, exported the raw responses, and compared Microsoft Forms’ default output with Borda, pairwise, and Schulze aggregation. The source is a useful reminder that research tooling can hide analytic assumptions.

## Key Claims

- Default ranking output should be treated as an analysis to validate, not as raw fact.
- Independent aggregation can reveal sensitivity to the scoring method.
- Raw response export is a practical audit control for survey and prioritization tools.

## Useful Examples

- Recompute a force-ranking result with more than one defensible aggregation method.
- Document the method used before presenting a “winner” to stakeholders.

## Constraints / Caveats

The case does not establish that Microsoft Forms is broadly unreliable or that one alternative method is universally correct.

## Design Implications

Research tooling should expose scoring assumptions, preserve raw responses, and make alternative analyses easy to compare.

## Tensions

Convenient default analytics reduce effort, while transparent and auditable analysis requires more methodological work.

## Open Questions

- Which aggregation method best fits the decision and respondent task?
- How often do product teams inspect the scoring model behind survey dashboards?

## Concepts Linked

- [[concepts/ux-research/research-data-validation|Research Data Validation]]
- [[concepts/ux-research/ranking-and-prioritization|Ranking and Prioritization]]

## LLM Use

Use this source to prompt an audit of ranking, survey, and prioritization outputs. Ask the model to state the aggregation rule, reproduce it from raw data, and compare plausible alternatives.

## Reliability Notes

The source is a firsthand account with a concrete dataset size and named methods. The underlying responses and calculations were not independently inspected in this ingest.

## Backfill Status

New source page created from the 2026-07-27 raw capture.
