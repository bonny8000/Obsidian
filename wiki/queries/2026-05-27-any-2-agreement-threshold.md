---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.78
---

# What agreement threshold is acceptable for AI-assisted UX triage?

## Short Answer
The wiki does not contain a numeric threshold, but the available evidence suggests the bar should be set relative to human evaluator norms: if human any-2 agreement for the same task is around 40–60%, an AI system matching or exceeding that range may be acceptable for triage. For triage (not formal reporting), consistency matters more than completeness, so within-system reliability above ~50% any-2 is a reasonable starting gate.

## Evidence
- [[concepts/ux-research/any-2-agreement|Any-2 Agreement]] — "Any-2 agreement can compare AI runs with each other or compare different AI systems. It helps quantify repeatability of problem lists. It does not by itself establish whether the problems are valid or important."
- [[concepts/ux-research/evaluator-effect|Evaluator Effect]] — "Usability problem discovery naturally varies across evaluators. AI systems may show within-system and between-system evaluator effects."
- [[concepts/ux-research/reliability-vs-validity|Reliability vs Validity]] — "Reliability is a prerequisite for trust, but it is not the same as accuracy."
- [[sources/measuringu-ai-usability-problem-analysis-video|MeasuringU: AI Reliability for Finding UI Problems]] — The study found cross-model reliability was low; within-model reliability varied by system. Gemini showed higher internal reliability than ChatGPT in the tested setting.

## Follow-up Sources Needed
- Published human evaluator any-2 agreement norms for usability heuristic evaluation and think-aloud analysis.
- Additional MeasuringU or similar studies with numeric any-2 thresholds for AI-assisted analysis.
