---
type: map
status: active
created: 2026-05-27
updated: 2026-08-04
tags: [map, ux-research, metrics, quant-ux, bayesian, screening]
sources:
  - sources/measuringu-statistics-30-participants
  - sources/measuringu-credible-vs-confidence-intervals
  - sources/measuringu-bayes-priors-uxr
  - sources/measuringu-tac10-screening
  - sources/measuringu-banner-tables
  - sources/measuringu-synthetic-users-review
  - sources/saeidehbakhshi-usability-metrics-static-product
confidence: 0.86
---

# UX Metrics Framework

> Rebuilt 2026-06-10 after corruption ([[logs/2026-06-10-corruption-recovery|recovery log]]). Original synthesis lost; re-grown from surviving concept pages.

## What To Measure

- [[concepts/ux-research/ux-metrics|UX Metrics]]: umbrella for performance, behavioral, attitudinal, and product-level UX metrics.
- [[concepts/ux-research/self-reported-ux-metrics|Self-Reported UX Metrics]]: SUS, SEQ, satisfaction, and related scales.
- [[concepts/ux-research/heart-framework|HEART Framework]]: happiness, engagement, adoption, retention, task success.
- [[concepts/ux-research/maxdiff-prioritization|MaxDiff Prioritization]]: forced trade-off measurement.

## How To Compare And Decide

- [[sources/measuringu-statistics-30-participants|MeasuringU's n >= 30 article]] clarifies that sample size should follow data type, analysis goal, uncertainty, power, and effect size rather than a universal threshold.
- [[playbooks/small-n-ux-statistics-checklist|Small-N UX Statistics Checklist]] turns that article into a practical stakeholder-response checklist.
- [[concepts/ux-research/ux-performance-benchmarking|UX Performance Benchmarking]] handles comparisons against goals and norms.
- [[concepts/ux-research/quant-uxr-rigor|Quant UXR Rigor]], [[concepts/ux-research/reliability-vs-validity|Reliability vs Validity]], and [[concepts/ux-research/validity-and-decision-relevance|Validity and Decision Relevance]] frame whether a metric is decision-worthy.

## Small-Sample Statistics

- [[concepts/ux-research/ux-statistics-decision-map|UX Statistics Decision Map]]: route question to method.
- [[concepts/ux-research/adjusted-wald-confidence-interval|Adjusted-Wald Confidence Interval]]: completion-rate intervals (frequentist).
- [[concepts/ux-research/bayesian-credible-interval|Bayesian Credible Interval]]: completion-rate intervals (Bayesian) — near-identical numbers under non-informative priors, different interpretation.
- [[concepts/ux-research/bayesian-priors-in-uxr|Bayesian Priors in UXR]]: prior choice can flip a small-sample conclusion; disclose and sensitivity-test.
- [[concepts/ux-research/sample-size-for-usability-studies|Sample Size for Usability Studies]]: sample-size planning by goal.
- [[concepts/ux-research/problem-discovery-model|Problem Discovery Model]]: formative discovery sample logic.
- [[concepts/ux-research/standardized-usability-questionnaires|Standardized Usability Questionnaires]]: rating-scale measurement foundation.

## Survey Quality and Reporting

- [[concepts/ux-research/survey-data-quality-screening|Survey Data Quality Screening]]: layered checklist (speeders, attention checks, straightlining, open-ended review, pattern checks, bot detection).
- [[concepts/ux-research/tac-10-tech-savviness|TAC-10 Tech Savviness]]: instrument that doubles as a Guttman-pattern data-quality canary.
- [[concepts/ux-research/banner-table|Banner Table]]: standard market-research segmentation deliverable, underused in UX.
- [[concepts/ux-research/synthetic-survey-data|Synthetic Survey Data]]: when (and not) to use LLM-generated responses; updated with the Lewis & Sauro 12-paper review.

## Core Sources

- [[sources/measuringu-statistics-30-participants|Do Statistics Really Require 30 Participants? (MeasuringU, 2026)]]
- [[sources/measuringu-credible-vs-confidence-intervals|Credible vs. Confidence Intervals (MeasuringU, 2026)]]
- [[sources/measuringu-bayes-priors-uxr|Bayes' Law in UX Research — The Power and Perils of Priors (MeasuringU, 2026)]]
- [[sources/measuringu-tac10-screening|Using the TAC-10 for Screening and Data Cleaning (MeasuringU, 2026)]]
- [[sources/measuringu-banner-tables|How to Use Banner Tables to Present Survey Results (MeasuringU, 2026)]]
- [[sources/measuringu-synthetic-users-review|A Review of Experiments with Synthetic Users (MeasuringU, 2026)]]
- [[sources/sauro-lewis-quantifying-ux-2016|Quantifying the User Experience (Sauro & Lewis, 2016)]]
- [[sources/tullis-albert-measuring-ux-2013|Measuring the User Experience (Tullis & Albert, 2013)]]
- [[sources/chapman-rodden-quant-uxr-2023|Quantitative User Experience Research (Chapman & Rodden, 2023)]]

## When The Product Will Not Hold Still (added 2026-08-04)

Everything above assumes a stable object of measurement. On personalised and adaptive products that assumption fails twice — across users, and within a user over time — and the failure is a **validity** problem, so a larger sample does not fix it.

- [[wiki/concepts/ux-research/measurement-under-adaptation|Measurement Under Adaptation]]: the two violations, why effort is ambiguous rather than good, the circularity problem, and the four-dimension alternative (Goal / Interaction / Outcome / Trajectory).
- [[wiki/concepts/ux-research/steerability|Steerability]]: usability's missing partner — can the user redirect a model the system has built of them, and **does the correction persist?** No instrument exists; this is the most buildable open measurement problem in the vault.
- **The cheap discipline:** report the conditions with every figure — *whose goal, which product state, what outcome, what stage of use.* No new instrument required.
- **Affected pages:** [[concepts/ux-research/ux-performance-benchmarking|UX Performance Benchmarking]] (comparability becomes unwarranted without a declared product state) · [[wiki/concepts/ux-research/ai-ux-measurement-constructs|AI UX Measurement Constructs]] (a validated instrument still measures a moving referent) · [[methods/benchmark-studies|Benchmark Studies]] · [[methods/usability-testing|Usability Testing]] · [[methods/longitudinal-research|Longitudinal Research]].
- **Source:** [[wiki/sources/saeidehbakhshi-usability-metrics-static-product|Bakhshi (2026)]] — conceptual critique, **no data.** Sound as a validity argument; not evidence about effect sizes.

## Tensions And Open Questions

- **Does any page in this framework currently report measurement conditions?** As of 2026-08-04, no. That is a backfill item.
- What instrument would measure steerability, and does correction-persistence predict anything users care about?
- How often must trajectory be sampled to detect direction rather than noise? Bakhshi does not say, and it is the variable that decides affordability.
- How should reports explain valid small-n statistics without implying high precision?
- Standardized questionnaires versus product-analytics frameworks: when does each earn its keep?
- Small-sample inferential stats versus "just ship and A/B": where is the boundary for Bonny's projects?
- Should the vault include calculators for adjusted-Wald, t intervals, and sample-size planning?
