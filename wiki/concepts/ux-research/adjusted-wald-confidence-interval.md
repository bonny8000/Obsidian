---
type: concept
status: active
created: 2026-06-10
updated: 2026-06-10
tags: [concept, statistics, quant-ux, confidence-intervals]
sources: [sauro-lewis-quantifying-ux-2016]
confidence: 0.95
---

# Adjusted-Wald Confidence Interval

## Summary

The recommended method for binomial confidence intervals (completion rates, conversion, yes/no metrics) at small sample sizes: "add two successes and two failures" (more precisely, add z²/2 ≈ 1.92 to successes and z² ≈ 3.84 to n for 95% CI), then compute the standard Wald interval on the adjusted proportion. Outperforms the classic Wald interval, which is badly miscalibrated for small n and extreme proportions.

## Why it matters

Usability tasks routinely have n = 5–20 and completion rates near 0% or 100% — exactly where the naive Wald interval fails. The adjusted-Wald gives honest uncertainty bounds for the small-sample reality of UX work.

## Key claims

- Use adjusted-Wald by default for completion-rate CIs at any n; it costs nothing at large n. (Sauro & Lewis 2016, ch. 3; conf 0.95)
- Worked example in book: 3/10 successes → adjusted proportion 3.35/10.71 = 0.313 with interval ±0.233 at 90% confidence. (conf 0.95)
- A point estimate without an interval invites overconfident decisions. (conf 0.9)

## Related concepts

- [[concepts/ux-research/sample-size-for-usability-studies|Sample Size for Usability Studies]]
- [[concepts/ux-research/ux-performance-benchmarking|UX Performance Benchmarking]]
- [[concepts/ux-research/quant-uxr-rigor|Quant UXR Rigor]]

## Sources

- [[sources/sauro-lewis-quantifying-ux-2016|Sauro & Lewis (2016)]], ch. 3.

## Open questions

- Should wiki dashboards report CIs for any metric Bonny tracks from usability sessions?
