---
type: concept
status: active
created: 2026-06-10
updated: 2026-06-16
tags: [concept, statistics, quant-ux, playbook]
sources:
  - sources/sauro-lewis-quantifying-ux-2016
  - sources/measuringu-statistics-30-participants
confidence: 0.92
---

# UX Statistics Decision Map

## Summary

Route UX statistics by decision, data type, and design structure. Do not route decisions through a fixed n >= 30 rule. The central questions are: What decision is being made? Are we estimating, benchmarking, or comparing? Is the data binary, rating-scale, time, or another metric? Are conditions within-subjects or between-subjects?

## Route Table

| Decision | Data Type | Typical UX Metric | Preferred Route |
|---|---|---|---|
| Estimate one value | Binary | Task completion | Adjusted-Wald confidence interval |
| Estimate one value | Rating scale | SUS, SEQ, SUPR-Q, UX-Lite | t confidence interval |
| Estimate one value | Time | Task time | Log-transform, estimate interval, transform back |
| Compare to benchmark | Binary | Completion vs. target | Planned binomial or proportion method |
| Compare to benchmark | Rating scale | Mean score vs. target | One-sample t method |
| Compare two independent designs | Binary | Completion A vs. B | N - 1 two-proportion method or planned binary test |
| Compare two independent designs | Rating scale or time | Mean A vs. B | Two-sample t method, with time transformation when needed |
| Compare same users across designs | Binary | Paired completion | Paired binary method such as McNemar when appropriate |
| Compare same users across designs | Rating scale or time | Paired scores or times | Paired t method, with transformation when needed |

## Small-N Interpretation

- n < 30 does not automatically invalidate statistics.
- The t-distribution was designed for small continuous samples.
- Binary outcomes need adjusted interval methods because naive Wald intervals can be misleading.
- Time data often needs transformation because raw time distributions are skewed.
- The limiting factor is often precision and power, not mathematical permission to analyze.

## Operating Checklist

1. Name the decision the statistic must support.
2. Identify the metric type: binary, rating scale, time, count, or other.
3. Identify whether the task is estimation, benchmark comparison, or design comparison.
4. Identify whether observations are independent or paired.
5. Choose the method from the route table.
6. Report uncertainty, sensitivity, and practical decision limits.
7. Only then decide whether the sample size is enough.

## Related Concepts

- [[concepts/ux-research/adjusted-wald-confidence-interval|Adjusted-Wald Confidence Interval]]
- [[concepts/ux-research/sample-size-for-usability-studies|Sample Size for Usability Studies]]
- [[concepts/ux-research/standardized-usability-questionnaires|Standardized Usability Questionnaires]]
- [[concepts/ux-research/quant-uxr-rigor|Quant UXR Rigor]]
- [[playbooks/small-n-ux-statistics-checklist|Small-N UX Statistics Checklist]]

## Sources

- [[sources/measuringu-statistics-30-participants|MeasuringU: Do Statistics Really Require 30 Participants?]]
- [[sources/sauro-lewis-quantifying-ux-2016|Sauro & Lewis (2016)]], ch. 1, 3-10.

## Open Questions

- Build a small interactive calculator implementing this decision map?
- Add example report language for each metric type?
