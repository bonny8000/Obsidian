# Source Card: MeasuringU - Do Statistics Really Require 30 Participants?

URL: https://measuringu.com/do-statistics-really-require-30-participants/

Retrieved: 2026-06-12

Source type: UX research statistics article

Publisher: MeasuringU

Authors: Jim Lewis, PhD; Jeff Sauro, PhD

Published: 2026-06-09

Title: Do Statistics Really Require 30 Participants?

Extractor notes:

- Defuddle succeeded locally on 2026-06-12.
- Web verification confirmed the title, authors, date, and article body on 2026-06-12.
- This raw card records metadata, extracted claims, and an AI-written summary rather than reproducing the full article text.

## Summary

The article explains that the common rule requiring at least 30 participants has real statistical roots but is often misapplied. The number 30 matters because t and z values converge around that range and because many sampling distributions become approximately normal around that range. But the article argues that this should not become a universal UX research sample-size rule.

For continuous UX measures, the t-distribution was designed for small samples. For binary UX outcomes such as task completion, standard Wald intervals can be inaccurate at small sample sizes, but adjusted methods such as adjusted-Wald can perform well. For skewed time data, log transformation can help. The better practice is to select sample size from the analysis, desired confidence or power, data type, variability, and minimum effect size.

## Extracted Claims

- The n >= 30 rule comes from real concerns about small-sample inference and the normal approximation, but it is too rigid as a universal rule.
- UX data is often non-normal: completion rates are binary, task times are skewed, and rating scales can be bounded or clustered.
- The Central Limit Theorem concerns the distribution of sample means, not the raw data distribution.
- For some common UX metrics, sampling distributions can approach normality before n = 30.
- The t-distribution exists specifically to handle small samples when the population standard deviation is unknown.
- Standard Wald intervals can badly understate uncertainty for binary data at small sample sizes.
- Adjusted-Wald and related adjusted procedures can make small-sample binary confidence intervals more accurate.
- Small samples can be statistically valid but will have lower precision and power.
- Sample size should be derived from the decision and analysis plan, not from a fixed folklore threshold.

## Practical Rules Extracted

- Rating scales: use t-distribution with the correct degrees of freedom.
- Binary data: use adjusted methods such as adjusted-Wald for confidence intervals and appropriate small-sample proportion tests.
- Time data: consider log-transforming skewed task times for confidence intervals.
- For small samples, focus on uncertainty, sensitivity, power, and effect size rather than treating the analysis as invalid.

