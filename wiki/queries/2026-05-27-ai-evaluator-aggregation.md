---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.80
---

# Should AI runs be treated like multiple evaluators and aggregated?

## Short Answer
Yes, with caution. Running the same AI prompt multiple times and aggregating overlapping issues is analogous to aggregating multiple human evaluators, and it can improve problem discovery recall. However, low cross-model reliability means that aggregating across different AI systems may artificially inflate the list without improving validity. Within the same model, multiple runs can be aggregated using any-2 logic to surface more stable findings.

## Evidence
- [[concepts/ux-research/evaluator-effect|Evaluator Effect]] — "AI systems may show within-system and between-system evaluator effects. Reliability metrics help distinguish acceptable variability from unstable output."
- [[concepts/ux-research/any-2-agreement|Any-2 Agreement]] — "Any-2 agreement can compare AI runs with each other." This is the operational mechanism for treating AI runs as evaluators.
- [[sources/measuringu-ai-usability-problem-analysis-video|MeasuringU: AI Reliability for Finding UI Problems]] — "Cross-model reliability was low." Aggregating across models adds noise. "For the tested video/prompt, Gemini had higher internal reliability." Within-model aggregation is more defensible.
- [[concepts/ux-research/reliability-vs-validity|Reliability vs Validity]] — "Consistent results are not automatically accurate results." Aggregation improves recall but cannot substitute for validity checking.

## Follow-up Sources Needed
- Research on optimal number of AI runs for stable problem discovery using within-model aggregation.
