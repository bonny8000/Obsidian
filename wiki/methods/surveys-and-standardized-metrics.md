---
type: method
status: active
created: 2026-06-12
updated: 2026-07-02
tags: [method, ux-research, survey, metrics, quant-uxr]
sources:
  - sources/sauro-lewis-quantifying-ux-2016
  - sources/tullis-albert-measuring-ux-2013
  - sources/carl-pearson-quant-uxr-self-study-resources
  - sources/chapman-rodden-quant-uxr-2023
  - sources/measuringu-statistics-30-participants
  - sources/arxiv-2606.30660-value-sensitive-conversational-ai
confidence: 0.9
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
- A standardized measure such as SUS, SEQ, SUPR-Q, or UX-Lite matches the decision.
- Participants may benefit from an audio-first or conversational modality, and the study can separately measure access, comprehension, completion, and response quality.

## Avoid When

- Participants cannot accurately self-report the behavior of interest.
- The sample source is biased or too small for the decision.
- The team wants a survey to replace direct usability observation.
- The only argument for the sample size is a generic n >= 30 rule.
- A human-like agent would be deployed without clear AI disclosure, privacy checks, skip/stop controls, or a plan to distinguish completion from valid data.

## Inputs

- Construct definition.
- Sampling frame and recruitment criteria.
- Standardized questionnaire or carefully tested custom items.
- Analysis plan, including confidence intervals where needed.
- Precision, power, or minimum detectable effect target for the decision.

## Procedure

1. Define what the metric should decide.
2. Choose or design items aligned with the construct.
3. Pilot for wording and comprehension.
4. Choose the analysis method before collecting data.
5. Collect responses with sample-quality checks.
6. Analyze effect size, uncertainty, and practical significance.
7. Explain the decision limit, especially when n is small.
8. If using voice or conversational AI, co-design language and pacing, disclose the agent, preserve skip/stop controls, and measure comprehension and response validity in addition to completion.

## Small-N Analysis Guidance

| Metric | Small-n issue | Better route |
|---|---|---|
| SUS, SEQ, SUPR-Q, UX-Lite | Stakeholders may assume n < 30 invalidates the result | Use t-based intervals or tests with correct degrees of freedom |
| Task completion | Naive Wald intervals can understate uncertainty | Use adjusted-Wald intervals |
| Task time | Raw times are usually right-skewed | Log-transform for interval estimation, then transform back |
| Any metric | Low power and wide intervals | Report interval width, sensitivity, and decision caveat |

## Outputs

- Metric score and distribution.
- Confidence interval or uncertainty estimate.
- Benchmark or baseline comparison.
- Decision recommendation tied to threshold or trend.
- Caveat about precision and power when the sample is small.

## Quality Bar

- Avoid treating n >= 30 as a universal rule.
- Choose sample size from analysis goal, data type, uncertainty, power, and effect size.
- Do not overstate precision.
- Keep measurement validity separate from dashboard aesthetics.
- Explain what the metric can and cannot decide.
- Treat delivery modality as part of the instrument. Higher completion does not establish truthfulness, validity, or informed consent.

## LLM Assistance

- **Safe uses:** drafting candidate items, checking wording ambiguity, summarizing open-ends, identifying whether a metric is binary/rating/time.
- **Risky uses:** inventing statistical conclusions, ignoring sampling limits, treating synthetic responses as real.
- **Verification required:** formulas, sample-size assumptions, confidence intervals, power, and item wording.

## Related Concepts

- [[concepts/ux-research/standardized-usability-questionnaires|Standardized Usability Questionnaires]]
- [[concepts/ux-research/self-reported-ux-metrics|Self-Reported UX Metrics]]
- [[concepts/ux-research/adjusted-wald-confidence-interval|Adjusted-Wald Confidence Interval]]
- [[concepts/ux-research/ux-statistics-decision-map|UX Statistics Decision Map]]
- [[concepts/ux-research/sample-size-for-usability-studies|Sample Size for Usability Studies]]
- [[playbooks/small-n-ux-statistics-checklist|Small-N UX Statistics Checklist]]
- [[concepts/ux-research/value-sensitive-conversational-surveys|Value-Sensitive Conversational Surveys]]

## Source Evidence

- [[sources/measuringu-statistics-30-participants|MeasuringU - Do Statistics Really Require 30 Participants?]]
- [[sources/sauro-lewis-quantifying-ux-2016|Sauro and Lewis - Quantifying UX]]
- [[sources/tullis-albert-measuring-ux-2013|Tullis and Albert - Measuring UX]]
- [[sources/carl-pearson-quant-uxr-self-study-resources|Quant UXR Self-Study Resources]]
- [[sources/chapman-rodden-quant-uxr-2023|Chapman and Rodden - Quant UXR]]
- [[sources/arxiv-2606.30660-value-sensitive-conversational-ai|Maurya (2026) - Value-Sensitive Conversational AI for Low-Literacy Surveys]]
