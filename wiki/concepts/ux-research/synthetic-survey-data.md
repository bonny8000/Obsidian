---
type: concept
status: active
created: 2026-06-10
updated: 2026-06-17
tags: [ux-research, surveys, ai, synthetic-data, validity, llm-evaluation]
sources:
  - sources/quantuxblog
  - sources/measuringu-synthetic-users-review
confidence: 0.82
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
- **Empirical confirmation across 12 peer-reviewed studies** ([[sources/measuringu-synthetic-users-review|Lewis & Sauro, 2026]]): 9 encouraging vs 14 discouraging findings. Synthetic users match humans on surface metrics (means, directional trends) but fail on *reduced variance*, subgroup means, regression coefficients, and qualitative depth. **Only 21% of classic psychology studies replicated** with synthetic users.
- Recommended scope per the review: synthetic users have promise for "deriving insights from already-collected data," **not** for generating novel research findings or driving critical decisions. The qualitative shallow-extension trap is consistent — synthetic interviews flatten after a few follow-up turns even when the first answer looks good.

## Related Concepts

- [[concepts/ux-research/quant-uxr-rigor|Quant UXR Rigor]]
- [[concepts/ux-research/quant-uxr-learning-path|Quant UXR Learning Path]]
- [[concepts/ux-research/reliability-vs-validity|Reliability vs Validity]]
- [[concepts/ux-research/validity-and-decision-relevance|Validity and Decision Relevance]]
- [[concepts/ux-research/genai-in-qualitative-research|GenAI in Qualitative Research]]
- [[concepts/ux-research/self-reported-ux-metrics|Self-Reported UX Metrics]]
- [[concepts/ux-research/grounded-synthetic-personas|Grounded Synthetic Personas]]
- [[comparisons/ai-assisted-research-risk-matrix|AI-Assisted Research Risk Matrix]]

## Sources

- [[sources/quantuxblog|Quantitative UX Research Blog]]
- [[sources/measuringu-synthetic-users-review|MeasuringU: A Review of Experiments with Synthetic Users (Lewis & Sauro, 2026)]] — 12-paper review across psychological experiments, surveys, social research, UX interviews.

## Open Questions

- Which internal uses of synthetic survey data are acceptable as tooling tests rather than research evidence?
- What validation standard would be required before using synthetic data in any product decision?
- Which of the 14 discouraging findings from the Lewis & Sauro review hold up against frontier models (Claude 4.x, GPT-5)? When does the review need to be redone?
