---
type: concept
status: active
created: 2026-06-10
updated: 2026-06-12
tags: [concept, statistics, quant-ux, playbook]
sources:
  - sources/sauro-lewis-quantifying-ux-2016
  - sources/measuringu-statistics-30-participants
confidence: 0.9
---

# UX Statistics Decision Map

## Summary

Sauro & Lewis ch. 1 routes any UX research question to a method via three questions: (1) Estimating a value, comparing to a benchmark, or comparing alternatives? (2) Data discrete-binary (completion) or continuous (time, ratings)? (3) Same users or different users across conditions (within vs. between subjects)?

## Route table (compressed)

- Do not route decisions through a fixed n >= 30 rule; route through data type, analysis goal, expected variability, confidence or power, and effect size.

- Estimate precision → confidence interval ([[concepts/ux-research/adjusted-wald-confidence-interval|adjusted-Wald]] for binary; t-interval for continuous; log-transform for times).
- Compare to benchmark → one-sample test (exact binomial / one-sample t).
- Compare two designs, different users → two-sample t / N − 1 two-proportion test.
- Compare two designs, same users → paired t / McNemar.
- "How many users?" → [[concepts/ux-research/sample-size-for-usability-studies|sample size models]].

## Why it matters

This map turns the book into an operational playbook — the right page for a working session is one lookup away. Candidate for `wiki/playbooks/`.

## Related concepts

- [[concepts/ux-research/adjusted-wald-confidence-interval|Adjusted-Wald Confidence Interval]]
- [[concepts/ux-research/sample-size-for-usability-studies|Sample Size for Usability Studies]]
- [[concepts/ux-research/standardized-usability-questionnaires|Standardized Usability Questionnaires]]

## Sources

- [[sources/measuringu-statistics-30-participants|MeasuringU: Do Statistics Really Require 30 Participants?]]

- [[sources/sauro-lewis-quantifying-ux-2016|Sauro & Lewis (2016)]], ch. 1, 3–10.

## Open questions

- Build a small interactive calculator (HTML artifact) implementing the decision map?
