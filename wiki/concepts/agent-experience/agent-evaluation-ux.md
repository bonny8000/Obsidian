---
type: concept
status: active
created: 2026-06-12
updated: 2026-06-12
tags: [agent-experience, evaluation, metrics, ux-research, ax]
sources:
  - sources/theaxlabs-contaminated-memory-performance
  - sources/lee-see-2004-trust-in-automation
  - sources/amershi-2019-human-ai-guidelines
confidence: 0.7
---

# Agent Evaluation UX

## Summary

Agent evaluation UX is the research and metrics practice for judging whether an agent experience works: combining task-outcome evals with human-centered measures like appropriate reliance, intervention rate, and trust trajectory over repeated use.

## Why It Matters

Model-quality evals answer "is the output correct"; they do not answer "does the human–agent system produce better outcomes than the human alone." UX research owns that second question, and standard usability metrics only partially cover it.

## Key Claims

- Single-session usability testing under-measures agents; trust calibration, reliance patterns, and proactivity tolerance only show up longitudinally.
- Useful agent-specific measures include: intervention/correction rate, verification effort, delegation breadth over time, false-positive tolerance for proactive touches, and recovery cost per error.
- Wizard-of-Oz protocols remain the fastest way to test agent interaction designs before the agent capability exists — see [[methods/wizard-of-oz-testing|Wizard of Oz Testing]].
- Eval suites and UX research should share artifacts: failure cases found in usability sessions become regression evals; eval failures become stimuli for design iteration.
- Memory-bearing agents need evaluation of memory quality itself, since contamination degrades experience invisibly.
- Lee & See's misuse/disuse taxonomy converts directly into measurable outcomes: unreviewed-error rate (misuse) and redundant-verification rate (disuse) bracket appropriate reliance — see [[sources/lee-see-2004-trust-in-automation|Lee & See 2004]].

## Related Concepts

- [[concepts/ux-research/ai-evals|AI Evals]]
- [[concepts/ai-agents/product-evals|Product Evals]]
- [[concepts/agent-experience/trust-calibration|Trust Calibration]]
- [[concepts/ux-research/ux-metrics|UX Metrics]]
- [[methods/usability-testing|Usability Testing]]
- [[methods/longitudinal-research|Longitudinal Research]]

## Conflicts & Caveats

- Metric definitions above are a working set, not an industry standard. Reliance-side metrics (intervention rate, verification effort) are grounded in Lee & See's appropriate-reliance frame; Amershi et al.'s guidelines double as heuristic-evaluation criteria.

## Sources

- [[sources/lee-see-2004-trust-in-automation|Lee & See (2004): Trust in Automation]]
- [[sources/amershi-2019-human-ai-guidelines|Amershi et al. (2019): Human-AI Guidelines]]
- [[sources/theaxlabs-contaminated-memory-performance|AX LABS: Contaminated Memory]]

## Open Questions

- What is a practical minimum longitudinal protocol (length, touchpoints, sample) for measuring trust trajectory in an agent product?
