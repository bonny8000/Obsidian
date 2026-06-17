---
type: playbook
status: active
created: 2026-06-16
updated: 2026-06-16
tags: [playbook, ux-research, statistics, sample-size, quant-uxr]
sources:
  - sources/measuringu-statistics-30-participants
  - sources/sauro-lewis-quantifying-ux-2016
confidence: 0.9
---

# Small-N UX Statistics Checklist

## Use This When

A stakeholder asks whether a UX statistic is valid because the study has fewer than 30 participants.

## Checklist

1. State the decision.
   - What product, design, or research decision will this number support?
   - Is the decision directional, threshold-based, or a high-stakes launch decision?

2. Classify the metric.
   - Binary: task completion, yes/no, conversion.
   - Rating scale: SUS, SEQ, SUPR-Q, UX-Lite, satisfaction.
   - Time: task time, duration, latency.
   - Other: count, ordinal, open-ended coded data.

3. Classify the statistical task.
   - Estimate one value.
   - Compare to a benchmark.
   - Compare two or more alternatives.
   - Track a metric over time.

4. Choose the method before judging n.
   - Rating scales: t interval or t test with correct degrees of freedom.
   - Binary outcomes: adjusted-Wald for confidence intervals; planned binary comparison method for tests.
   - Time data: log-transform for confidence intervals when skew is expected.
   - Formative discovery: use problem-discovery logic, not the n >= 30 rule.

5. Report the limitation honestly.
   - Small n can be statistically analyzable.
   - Small n often has wide intervals.
   - Small n often cannot detect subtle or moderate effects.
   - The decision may need a bigger sample even when the method is valid.

6. Write the recommendation.
   - If the interval is narrow enough for the decision, say so.
   - If the interval is too wide, recommend more data or a lower-stakes interpretation.
   - If power is weak, state what size of effect the study could realistically detect.

## Stakeholder Response Pattern

"The issue is not whether statistics require 30 users. The issue is whether this sample, with this data type and method, gives enough precision or power for the decision."

## Common Failure Modes

- Treating n >= 30 as a universal quality bar.
- Treating n < 30 as automatically invalid.
- Reporting only point estimates for completion rates.
- Using standard Wald intervals for small binary samples.
- Applying summative statistical rules to formative problem discovery.
- Hiding low power behind technically valid small-sample methods.

## Related Notes

- [[sources/measuringu-statistics-30-participants|MeasuringU: Do Statistics Really Require 30 Participants?]]
- [[concepts/ux-research/sample-size-for-usability-studies|Sample Size for Usability Studies]]
- [[concepts/ux-research/adjusted-wald-confidence-interval|Adjusted-Wald Confidence Interval]]
- [[concepts/ux-research/ux-statistics-decision-map|UX Statistics Decision Map]]
- [[methods/surveys-and-standardized-metrics|Surveys and Standardized Metrics]]
