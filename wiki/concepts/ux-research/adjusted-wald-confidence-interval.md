---
type: concept
status: active
created: 2026-06-10
updated: 2026-06-17
tags: [concept, statistics, quant-ux, confidence-intervals, bayesian-comparison]
sources:
  - sources/sauro-lewis-quantifying-ux-2016
  - sources/measuringu-statistics-30-participants
  - sources/measuringu-credible-vs-confidence-intervals
confidence: 0.95
---

# Adjusted-Wald Confidence Interval

## Summary

Adjusted-Wald is a small-sample method for binomial confidence intervals, useful for completion rates, conversion, yes/no outcomes, and other binary UX metrics. The practical 95% shortcut is close to adding two successes and two failures before computing a Wald-style interval on the adjusted proportion.

More generally, for confidence level z:

- adjusted n = n + z^2
- adjusted successes = x + z^2 / 2
- adjusted proportion = adjusted successes / adjusted n

Then compute the interval around the adjusted proportion.

## Why It Matters

Usability studies often have small samples and binary outcomes. A naive Wald interval can look precise when the actual uncertainty is much wider, especially near 0% or 100% completion. Adjusted-Wald gives a more honest uncertainty estimate without forcing the team to collect 30 participants by default.

## Key Claims

- The n >= 30 rule should not force binary UX metrics into naive Wald intervals.
- Standard Wald intervals can badly understate uncertainty for small-sample binary data.
- Adjusted methods work better for completion-rate confidence intervals when n is small.
- A point estimate without an interval invites overconfident product decisions.
- Small-n binary analysis is possible, but it must surface interval width and decision risk.

## Use When

- Reporting task completion from a usability study.
- Reporting pass/fail, yes/no, conversion, or binary success outcomes.
- A stakeholder asks whether a completion rate from n < 30 can be statistically summarized.
- Comparing the uncertainty of several small-sample binary metrics.

## Avoid When

- The outcome is a rating scale or continuous metric; use t-based methods instead.
- The study needs a hypothesis test between two proportions; use a planned comparison method such as N - 1 two-proportion.
- The interval is too wide for the decision; the method is valid, but the sample may still be insufficient.

## Related Concepts

- [[concepts/ux-research/bayesian-credible-interval|Bayesian Credible Interval]] — Bayesian counterpart; near-identical numbers under non-informative priors, different interpretation.
- [[concepts/ux-research/bayesian-priors-in-uxr|Bayesian Priors in UXR]] — when priors diverge, so do the conclusions.
- [[concepts/ux-research/sample-size-for-usability-studies|Sample Size for Usability Studies]]
- [[concepts/ux-research/ux-statistics-decision-map|UX Statistics Decision Map]]
- [[concepts/ux-research/ux-performance-benchmarking|UX Performance Benchmarking]]
- [[concepts/ux-research/quant-uxr-rigor|Quant UXR Rigor]]

## Practical interpretation

The technically correct interpretation — "if we ran many tests with 20 users and computed confidence intervals each time, on average, 95 out of 100 intervals will contain the unknown population completion rate" — is hard to land with stakeholders. Defensible stakeholder phrasings ([[sources/measuringu-credible-vs-confidence-intervals|Sauro & Lewis, 2026]]):

- **Likely range:** "X% to Y% is the most likely range for the unknown completion rate."
- **Plausible range:** "Given this data, values inside are plausible while those outside are implausible."

Avoid saying "95% probability the true value is in this range" with a confidence interval — that's a Bayesian credible interval statement. If you need that interpretation, compute a credible interval instead (the numbers are usually very close under non-informative priors).

## Sources

- [[sources/measuringu-statistics-30-participants|MeasuringU: Do Statistics Really Require 30 Participants?]]
- [[sources/measuringu-credible-vs-confidence-intervals|MeasuringU: Credible vs. Confidence Intervals — Different Meanings but Similar Decisions]] (Sauro & Lewis, 2026)
- [[sources/sauro-lewis-quantifying-ux-2016|Sauro & Lewis (2016)]], ch. 3.

## Open Questions

- Should wiki dashboards report adjusted-Wald intervals for every binary metric from usability sessions?
- Should the vault add a calculator artifact for adjusted-Wald and N - 1 two-proportion tests?
