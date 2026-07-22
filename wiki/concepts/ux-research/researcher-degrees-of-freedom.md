---
type: concept
status: active
created: 2026-07-20
updated: 2026-07-20
tags: [ux-research, quantitative-research, validity, ai-analysis]
sources:
  - sources/saeidehbakhshi-ai-in-quantitative-research
confidence: 0.8
---
# Researcher Degrees of Freedom

## Summary

Researcher degrees of freedom are the many unlogged analytical choices — outcomes, time windows, segments, exclusions, transformations, model specifications — that let a "clean" result emerge from a large hidden search. The concept predates AI, but AI multiplies the speed and scale at which those choices can be exercised, while returning a single polished chart whose confidence interval describes only the selected analysis, not the search that produced it.

## Key Claims

- A system that scans five outcomes × four windows × eight segments × several exclusions and returns one chart has silently exercised massive selection; the reported uncertainty ignores it. *(Bakhshi 2026)*
- Verification is representation-hungry: analysts needed prose, code, charts, and tables together to audit AI-assisted analyses — no single view was a sufficient audit trail. *(Bakhshi 2026, citing Microsoft CHI study)*
- A person reviewing the final slide is "technically in the loop" without having seen the choices that determined the result. *(Bakhshi 2026)*
- Countermeasures: keep exploration distinct from confirmation; use holdouts, replication, preregistration, and preserve the analytical path visibly in the workflow. *(Bakhshi 2026)*

## Why It Matters (for UX)

AI-assisted analytics tools sold to UX/product teams optimize for the clean chart. Without a visible analytical path, teams will increasingly act on artifacts of search rather than findings. This concept supplies the vocabulary for review rituals and tool requirements (show the tested alternatives, not just the winner).

## Related Concepts

- [[wiki/concepts/ux-research/evidence-engineering|Evidence Engineering]]
- [[wiki/concepts/ux-research/reliability-vs-validity|Reliability vs Validity]]
- [[wiki/concepts/ux-research/human-in-the-loop|Human-in-the-Loop]]
- [[wiki/concepts/ux-research/heuristics-and-biases|Heuristics and Biases]]

## Sources

- [[wiki/sources/saeidehbakhshi-ai-in-quantitative-research|Bakhshi: AI in Quantitative Research (2026)]]

## Open Questions

- What is the minimum "analytical path" record a fast-moving team will actually maintain — and can agent tooling produce it automatically?
