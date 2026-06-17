---
type: source
status: active
created: 2026-06-12
tags: [source, ux-research, quant-uxr, statistics, sample-size, confidence-intervals]
sources:
  - raw/web/measuringu-statistics-30-participants-2026-06-12
  - raw/web/measuringu-statistics-30-participants-2026-06-16-detailed
updated: 2026-06-16
ingest_level: detailed
coverage: detailed
llm_ready: true
raw_preserved: true
confidence: 0.9
---

# MeasuringU: Do Statistics Really Require 30 Participants?

## Citation

Lewis, Jim; Sauro, Jeff. "Do Statistics Really Require 30 Participants?" MeasuringU, 2026-06-09.

URL: https://measuringu.com/do-statistics-really-require-30-participants/

Raw source cards:

- `raw/web/measuringu-statistics-30-participants-2026-06-12.md`
- `raw/web/measuringu-statistics-30-participants-2026-06-16-detailed.md`

## Summary

This MeasuringU article explains why the common n >= 30 rule has real statistical roots but is often misapplied in UX research. The number 30 appears because t and z values converge around that range and because many sampling distributions become approximately normal near that range. But the article argues that 30 is not a universal threshold for valid statistics.

The main recommendation is to choose sample size based on the analysis, data type, variability, desired confidence or power, and effect size. Small samples can be statistically valid when the right methods are used, but they usually have wider uncertainty and lower sensitivity.

## Detailed Evidence Map

The article gives three reasons the n >= 30 rule feels plausible:

- Around 30 observations, t values and z values become similar enough that introductory statistics can simplify many calculations.
- Normal approximations to binomial data become less fragile as n grows, especially when proportions are not near 0 or 1.
- The Central Limit Theorem often makes sampling distributions of means more normal as sample size increases.

It then separates those approximations from UX decision practice:

- t-based methods were built for small continuous samples where the population standard deviation is unknown.
- UX raw data is often non-normal, but inferential procedures depend on sampling distributions and method choice, not only raw histograms.
- For binary data, the problem is not small n by itself; the problem is using standard Wald intervals when adjusted methods are available.
- Small samples usually limit precision and power, so reporting uncertainty is more important than defending a threshold.

## Decision Routing

| Research output | Data type | Better small-n route |
|---|---|---|
| SUS, SEQ, SUPR-Q, UX-Lite mean | Rating scale / continuous-like | t interval or t test with correct degrees of freedom |
| Task completion rate | Binary | Adjusted-Wald confidence interval |
| Two completion rates | Binary comparison | N - 1 two-proportion method or another appropriate small-sample comparison |
| Task time | Right-skewed continuous | Log-transform for confidence intervals, then transform back |
| Any small sample | Estimate or comparison | Show interval width, detectable effect size, and power limits |

## Key Claims

- The n >= 30 rule is based on real statistical approximations, but it should not become a general-purpose UX research rule.
- UX raw data is often non-normal: completion rates are binary, times are skewed, and rating scales are bounded.
- The Central Limit Theorem applies to sampling distributions of means, not directly to raw data.
- The t-distribution was designed for small samples and does not require n >= 30 to be valid.
- Standard Wald confidence intervals can be badly inaccurate for small-sample binary data.
- Adjusted-Wald and related adjusted methods are better choices for small-sample binary UX metrics.
- For rating-scale data, use the t-distribution with the correct degrees of freedom.
- For time data, consider log-transforming skewed task times before computing confidence intervals.
- Small samples shift the concern from validity of the method to precision, sensitivity, power, and detectable effect size.
- A sample of 30 is rarely exactly right for a specific UX research decision.

## Useful Examples

- For SUS, SEQ, and similar rating scales, use t-based intervals or tests rather than treating n < 30 as invalid.
- For task completion or yes/no metrics, avoid naive Wald intervals and prefer adjusted methods.
- For task time, log-transform skewed raw data when estimating intervals.

## Constraints / Caveats

- This source is a methods article, not a replacement for a project-specific power or precision calculation.
- It supports small-sample analysis with appropriate methods, not underpowered claims with no uncertainty.
- The article is about summative/statistical analysis and should not be confused with the formative "magic number 5" problem-discovery rule.

## Design Implications

- Research plans should specify data type, analysis method, desired precision, confidence, power, and minimum effect size before choosing sample size.
- Reports should explain uncertainty rather than defending sample size with folklore.
- UX dashboards should avoid naked point estimates for small-n completion rates.
- The wiki's UX metrics guidance should separate formative discovery sample logic from summative measurement sample logic.

## Tensions

- Small samples can be statistically valid but still too imprecise for subtle product decisions.
- Stakeholders may use n >= 30 as a quality shortcut, while researchers need to explain the actual analysis requirement.
- Rigid sample-size rules are easy to communicate; decision-specific statistics are more accurate but require more explanation.

## Open Questions

- Should this vault add a lightweight sample-size planning playbook for Bonny's UX research projects?
- Which common Bonny research outputs need confidence intervals or power planning?
- Should `wiki/playbooks/` include a small-n UX statistics decision checklist?

## Concepts Linked

- [[concepts/ux-research/sample-size-for-usability-studies|Sample Size for Usability Studies]]
- [[concepts/ux-research/adjusted-wald-confidence-interval|Adjusted-Wald Confidence Interval]]
- [[concepts/ux-research/ux-statistics-decision-map|UX Statistics Decision Map]]
- [[concepts/ux-research/quant-uxr-rigor|Quant UXR Rigor]]
- [[concepts/ux-research/ux-performance-benchmarking|UX Performance Benchmarking]]
- [[playbooks/small-n-ux-statistics-checklist|Small-N UX Statistics Checklist]]

## LLM Use

- **Use for:** explaining small-n UX statistics, planning sample sizes, reviewing whether analysis choices match data types.
- **Do not use for:** declaring a specific project sample size adequate without project-specific assumptions.
- **Best prompt pattern:** Ask the LLM to identify the data type, analysis goal, expected effect size, and uncertainty requirement before proposing a sample size.

## Detailed Prompt Pattern

Ask:

1. What decision will this metric support?
2. Is the outcome rating-scale, binary, time, or another distribution?
3. Are we estimating one value, comparing to a benchmark, or comparing alternatives?
4. What interval width, power, or minimum detectable effect is needed?
5. Which method matches the data type: t, adjusted-Wald, N - 1 two-proportion, log-time interval, or another planned analysis?
6. What caveat should appear in the report if n is small?

## Reliability Notes

- Primary MeasuringU methods article by Jim Lewis and Jeff Sauro.
- High usefulness for UX statistics decisions, but still should be paired with source-specific formulas or calculators for final sample-size planning.

## Backfill Status

- Created directly in LLM-ready format on 2026-06-12.
- Detailed raw/source pass added on 2026-06-16.
