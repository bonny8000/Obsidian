---
type: method
status: active
created: 2026-06-12
updated: 2026-06-12
tags: [method, ux-research, survey, metrics, quant-uxr]
sources:
  - sources/sauro-lewis-quantifying-ux-2016
  - sources/tullis-albert-measuring-ux-2013
  - sources/carl-pearson-quant-uxr-self-study-resources
  - sources/chapman-rodden-quant-uxr-2023
confidence: 0.86
method_family: quantitative
best_for: attitudes, self-reported experience, tracking, benchmarking
avoid_when: behavior must be observed directly or sample quality is weak
outputs: metric scores, confidence intervals, benchmarks, segments, decision thresholds
---

# Method: Surveys and Standardized Metrics

## Purpose

Surveys and standardized UX metrics quantify self-reported experience, attitudes, expectations, satisfaction, perceived usability, and other constructs that can be tracked or compared.

## Use When

- The team needs a repeatable metric.
- A decision depends on relative differences across variants, segments, or time.
- The construct can be asked clearly and interpreted consistently.

## Avoid When

- Participants cannot accurately self-report the behavior of interest.
- The sample source is biased or too small for the decision.
- The team wants a survey to replace direct usability observation.

## Inputs

- Construct definition.
- Sampling frame and recruitment criteria.
- Standardized questionnaire or carefully tested custom items.
- Analysis plan, including confidence intervals where needed.

## Procedure

1. Define what the metric should decide.
2. Choose or design items aligned with the construct.
3. Pilot for wording and comprehension.
4. Collect responses with sample-quality checks.
5. Analyze effect size, uncertainty, and practical significance.

## Outputs

- Metric score and distribution.
- Confidence interval or uncertainty estimate.
- Benchmark or baseline comparison.
- Decision recommendation tied to threshold or trend.

## Quality Bar

- Do not overstate precision.
- Keep measurement validity separate from dashboard aesthetics.
- Explain what the metric can and cannot decide.

## LLM Assistance

- **Safe uses:** drafting candidate items, checking wording ambiguity, summarizing open-ends.
- **Risky uses:** inventing statistical conclusions, ignoring sampling limits, treating synthetic responses as real.
- **Verification required:** formulas, sample size assumptions, and item wording.

## Related Concepts

- [[concepts/ux-research/standardized-usability-questionnaires|Standardized Usability Questionnaires]]
- [[concepts/ux-research/self-reported-ux-metrics|Self-Reported UX Metrics]]
- [[concepts/ux-research/adjusted-wald-confidence-interval|Adjusted Wald Confidence Interval]]
- [[concepts/ux-research/ux-statistics-decision-map|UX Statistics Decision Map]]

## Source Evidence

- [[sources/sauro-lewis-quantifying-ux-2016|Sauro and Lewis - Quantifying UX]]
- [[sources/tullis-albert-measuring-ux-2013|Tullis and Albert - Measuring UX]]
- [[sources/carl-pearson-quant-uxr-self-study-resources|Quant UXR Self-Study Resources]]
- [[sources/chapman-rodden-quant-uxr-2023|Chapman and Rodden - Quant UXR]]

