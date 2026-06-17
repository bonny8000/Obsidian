---
type: raw_web_capture
status: active
created: 2026-06-16
retrieved: 2026-06-16
url: https://measuringu.com/do-statistics-really-require-30-participants/
publisher: MeasuringU
authors:
  - Jim Lewis
  - Jeff Sauro
published: 2026-06-09
title: Do Statistics Really Require 30 Participants?
tags: [raw, web, ux-research, statistics, sample-size, quant-uxr]
copyright_mode: paraphrased_evidence_card
extractor: Defuddle CLI --md
related_source: wiki/sources/measuringu-statistics-30-participants
confidence: 0.95
---

# Source Card: MeasuringU - Do Statistics Really Require 30 Participants?

URL: https://measuringu.com/do-statistics-really-require-30-participants/

This detailed raw card preserves the article's metadata, argument structure, extracted claims, practical rules, and graph implications. It intentionally does not reproduce the full article text.

## Retrieval Notes

- Defuddle local extraction succeeded on 2026-06-16 with proxy variables cleared.
- Web verification also confirmed the public article page, title, authors, publication date, headings, and main body on 2026-06-16.
- Earlier compact raw card: `raw/web/measuringu-statistics-30-participants-2026-06-12.md`.
- This card is a deeper pass for analysis and graph wiring.

## Core Thesis

The article argues that the familiar rule requiring at least 30 participants has legitimate statistical origins, but it becomes misleading when applied as a universal UX research threshold. The better rule is to choose sample size and analysis method from the research decision, data type, expected variability, desired confidence or power, and minimum effect size.

## Argument Structure

### Why n >= 30 became persuasive

- Introductory statistics often teaches z-based procedures first, but z procedures require knowing the population standard deviation.
- Applied UX work rarely has that population value, so the t-distribution is the relevant tool for continuous measures.
- Around n = 30, t values and z values are close enough that many tables and teaching shortcuts converge.
- For binary proportions, the binomial distribution can be approximated by a normal distribution under some conditions, but small samples and extreme proportions make that approximation fragile.
- UX raw data is commonly non-normal: completion is binary, task time is right-skewed, and rating scales are bounded or clustered.

### Why n < 30 can still be statistically valid

- The t-distribution was created for small samples and accounts for degrees of freedom.
- The Central Limit Theorem concerns the sampling distribution of means, not the shape of the raw data.
- MeasuringU's bootstrap examples indicate common UX metrics can have near-normal sampling distributions before n = 30, depending on metric type.
- Standard Wald intervals are a poor choice for small-sample binary outcomes, but adjusted methods can repair the problem.
- The question is often not "is statistics allowed?" but "how much uncertainty and power can this sample support?"

### Practical conclusion

- A fixed sample-size threshold is a communication shortcut, not a decision rule.
- Small samples can support valid inference with appropriate methods, but they usually produce wider intervals and lower sensitivity.
- A sample of 30 is rarely the exact right number; it may be too small for subtle effects, too large for some high-cost decisions, or simply unrelated to the decision's precision target.

## Figure-Level Evidence

- Figure 1 supports the historical reason for the n = 30 rule: t values approach z values as degrees of freedom increase.
- Figure 2 reinforces that raw UX metrics often fail normality assumptions.
- Figure 3 distinguishes raw-data non-normality from sampling-distribution behavior and shows several UX metric means approaching normality across smaller sample sizes.
- Figure 4 links the t-test to William Gossett and small-sample industrial measurement, reinforcing that small-n analysis is part of the method's origin.

## Method Routing Table

| UX data type | Typical metric | Small-n risk | Better method |
|---|---|---|---|
| Rating scale | SUS, SEQ, SUPR-Q, UX-Lite | Treating n < 30 as invalid, or using z methods without population SD | t-distribution with correct degrees of freedom |
| Binary outcome | Task completion, yes/no, conversion | Standard Wald intervals understate uncertainty | Adjusted-Wald confidence intervals; N - 1 two-proportion test for comparisons |
| Time measure | Task time, duration | Right skew and long-tail slow sessions | Log-transform for confidence intervals, then transform back |
| Any small sample | Any estimate or comparison | Low precision and low power | Report interval width, detectable effect size, and decision limits |

## Extracted Claims

- n >= 30 is partly rooted in t-to-z convergence and normal approximation logic.
- The threshold is often misapplied as a universal validity requirement.
- The t-distribution does not need n >= 30; it was designed for small samples.
- UX researchers should distinguish raw-data distribution from sampling distribution.
- Standard Wald intervals can be badly miscalibrated for small binary samples.
- Adjusted-Wald style procedures allow more honest uncertainty estimates for small completion-rate samples.
- Non-normal UX data does not automatically invalidate t-tests, intervals, or ANOVA-style procedures.
- Small samples mainly constrain precision, sensitivity, and power.
- Sample-size planning should start from the decision and analysis plan.

## Graph Implications

- Strengthens [[wiki/concepts/ux-research/sample-size-for-usability-studies]] by separating formative discovery logic from summative measurement logic.
- Strengthens [[wiki/concepts/ux-research/adjusted-wald-confidence-interval]] as the preferred small-n binary-metric interval.
- Strengthens [[wiki/concepts/ux-research/ux-statistics-decision-map]] with a concrete route from data type to method.
- Supports a new checklist-style playbook for responding to stakeholder claims that statistics require 30 users.
- Should be linked from [[wiki/maps/ux-metrics-framework]] and [[wiki/methods/surveys-and-standardized-metrics]].

## Research Use

Use this source when:

- A stakeholder challenges a small sample only because n is below 30.
- A UX report needs to justify t-based rating-scale analysis with small n.
- A completion-rate metric needs uncertainty bounds from a small usability sample.
- A team needs to explain why validity and precision are different concerns.

Do not use this source to:

- Declare any small sample adequate without checking interval width, power, and effect size.
- Treat qualitative formative discovery sample logic as the same problem as summative statistical inference.
- Hide weak power behind the claim that small samples are statistically allowed.

## Follow-Up Links Mentioned by the Article

- Magic number 5 for discovery studies.
- Degrees of freedom and t-distribution explanation.
- MeasuringU article on whether UX data is normally distributed.
- MeasuringU 2005 work on small-sample binomial confidence intervals.
- Adjusted-Wald / Agresti-Coull interval logic.
- N - 1 two-proportion test for binary comparisons.
- UX-Lite sample-size planning articles.
- Effect-size planning articles.
