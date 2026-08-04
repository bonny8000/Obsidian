---
type: method
status: active
created: 2026-06-12
updated: 2026-08-04
tags: [method, ux-research, benchmarking, quantitative]
sources:
  - sources/tullis-albert-measuring-ux-2013
  - sources/sauro-lewis-quantifying-ux-2016
  - sources/saeidehbakhshi-usability-metrics-static-product
confidence: 0.7
method_family: evaluative
best_for: tracking UX quality across releases or against competitors with standardized metrics
avoid_when: the team needs diagnosis of causes rather than measurement of levels
outputs: metric baselines, release deltas with confidence intervals, competitive comparisons
---

# Method: Benchmark Studies

## Purpose

Measure UX quality with standardized tasks and metrics, repeated over time or across competitors, so the team can answer "are we getting better" with numbers instead of anecdotes.

## Use When

- Leadership needs trend evidence: release-over-release or year-over-year.
- Competitive comparison on shared core tasks is decision-relevant.
- A redesign needs a before/after measurement plan.

## Avoid When

- The team needs to know why problems happen — benchmarks measure, they rarely explain.
- Tasks or product surfaces change so much between waves that comparison breaks.
- Sample sizes cannot support the precision the decision requires — see [[concepts/ux-research/sample-size-for-usability-studies|Sample Size for Usability Studies]].

## Inputs

- A locked task set covering core journeys, stable across waves.
- Metric set: task success, time, errors, plus a standardized questionnaire — see [[concepts/ux-research/standardized-usability-questionnaires|Standardized Usability Questionnaires]].
- Sampling plan and confidence-interval method — see [[concepts/ux-research/adjusted-wald-confidence-interval|Adjusted Wald Confidence Interval]].

## Procedure

1. Lock tasks, metrics, success criteria, and analysis plan before wave one.
2. Run wave one as the baseline; document every protocol decision for replication.
3. Repeat at fixed cadence with consistent sampling.
4. Report deltas with confidence intervals; refuse to over-read movements inside the interval.
5. Pair significant metric drops with qualitative follow-up to diagnose.

## Outputs

- Metric dashboard with baselines and wave deltas.
- Competitive position per core task where applicable.
- A prioritized list of where the numbers say to dig qualitatively.

## Quality Bar

- Protocol identical across waves; any forced change documented as a comparability break.
- Intervals always reported; point estimates never reported alone.
- Benchmark surfaces aligned to decisions, not vanity coverage.

## LLM Assistance

- **Safe uses:** report drafting, anomaly flagging across waves.
- **Risky uses:** explaining metric movement without supporting qualitative data.
- **Verification required:** statistics reproduced from raw data, not LLM arithmetic.

## Related

- [[methods/usability-testing|Usability Testing]]
- [[concepts/ux-research/ux-performance-benchmarking|UX Performance Benchmarking]]
- [[concepts/ux-research/ux-metrics|UX Metrics]]
- [[wiki/concepts/ux-research/measurement-under-adaptation|Measurement Under Adaptation]] — the condition under which this method's comparability claim fails.
- [[wiki/concepts/ux-research/steerability|Steerability]]

## Avoid When (addition, 2026-08-04)

> [!warning] Do not benchmark a personalising product without pinning the product state
> This method's entire value is comparability — across releases, against competitors, over time. [[wiki/sources/saeidehbakhshi-usability-metrics-static-product|Bakhshi (2026)]] argues that on an adaptive or personalised surface that comparability is **unwarranted rather than merely noisy**, because the object of measurement is not the same twice: *"the score is conditional on the user, their history, the state of the system, and the stage of use."*
>
> This is a validity problem, so a larger sample does not fix it. The score stays precise while its referent moves.
>
> **Minimum requirement if you benchmark anyway:** declare the product state and the participants' stage of use as part of the benchmark definition, and treat any wave-over-wave comparison across a change in personalisation logic as a *new* benchmark rather than a continuation of the old one.

## Additional Source Evidence

- [[wiki/sources/saeidehbakhshi-usability-metrics-static-product|Bakhshi (2026): Usability Metrics Assume the Product Stays Still]] — the conditionality argument. Conceptual critique, no data.
