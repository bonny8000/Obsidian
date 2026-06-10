---
type: concept
status: active
created: 2026-06-10
updated: 2026-06-10
tags: [ux-research, surveys, ai, synthetic-data, validity]
sources:
  - sources/quantuxblog
confidence: 0.74
---

# Synthetic Survey Data

## Summary

Synthetic survey data is LLM-generated survey response data. In the QuantUX framing, it should not be treated as a replacement for human survey data because it does not come from motivated human respondents.

## Why It Matters

AI makes it easy to generate plausible-looking survey tables, but quant UXR depends on who answered, why they answered, how they interpreted the question, and what population the sample can represent. Synthetic responses can look like data while bypassing the human evidence the survey was meant to collect.

## Key Claims

- Surveys should be understood as motivated communication from people, not only as abstract measurements.
- LLM-generated responses cannot solve sampling problems because no human population was sampled.
- Prompt, model, and time sensitivity can make synthetic responses unreliable.
- Synthetic responses may fail construct validity when they do not reproduce human response patterns.
- Synthetic data may still be useful for testing survey tooling, analysis pipelines, or hypothetical examples, but not as evidence about users without strong validation.

## Related Concepts

- [[concepts/ux-research/quant-uxr-rigor|Quant UXR Rigor]]
- [[concepts/ux-research/quant-uxr-learning-path|Quant UXR Learning Path]]
- [[concepts/ux-research/reliability-vs-validity|Reliability vs Validity]]
- [[concepts/ux-research/validity-and-decision-relevance|Validity and Decision Relevance]]
- [[concepts/ux-research/genai-in-qualitative-research|GenAI in Qualitative Research]]
- [[concepts/ux-research/self-reported-ux-metrics|Self-Reported UX Metrics]]

## Sources

- [[sources/quantuxblog|Quantitative UX Research Blog]]

## Open Questions

- Which internal uses of synthetic survey data are acceptable as tooling tests rather than research evidence?
- What validation standard would be required before using synthetic data in any product decision?
