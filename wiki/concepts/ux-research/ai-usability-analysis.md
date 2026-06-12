---
type: concept
status: active
created: 2026-05-18
updated: 2026-06-10
tags: [ux-research, ai, usability-testing]
sources:
  - sources/measuringu-ai-usability-problem-analysis-video
  - sources/measuringu-ai-real-ui-problems-hallucinations
  - sources/toss-tech-research-platform-ai
confidence: 0.87
---

# AI Usability Analysis

## Summary

AI usability analysis uses AI systems to inspect usability-test material, such as videos, transcripts, screen recordings, or task logs, and identify potential UX problems.

## Why It Matters

Usability analysis is valuable but labor-intensive. AI may reduce some analysis effort, but the MeasuringU source shows that repeatability and validation must be measured before relying on generated findings.

## Key Claims

- AI-generated usability problems should be evaluated for reliability.
- Consistency does not prove correctness.
- AI-only issue lists should be triaged into genuine findings, false alarms, and hallucinations before reporting.
- In MeasuringU's 2026 follow-up, one of eleven AI-only issues was a genuine find, seven were false alarms, and three were hallucinations.
- AI analysis is best treated as assistance or triage until validated against human expert analysis and participant evidence.
- **Huribot (Toss)** is a production example: an AI usability assistant trained on proprietary user data that enables designers to detect issues like dark patterns and misleading graphics during early iteration — positioned explicitly as a "check" tool supplementing, not replacing, formal UT. (See [[concepts/ux-research/huribot|Huribot]].)

## Related Concepts

- [[concepts/ux-research/ux-research-automation|UX Research Automation]]
- [[concepts/ux-research/ai-usability-false-alarm-triage|AI Usability False-Alarm Triage]]
- [[concepts/ux-research/reliability-vs-validity|Reliability vs Validity]]
- [[concepts/ux-research/any-2-agreement|Any-2 Agreement]]
- [[concepts/ux-research/evaluator-effect|Evaluator Effect]]
- [[concepts/ux-research/validity-and-decision-relevance|Validity and Decision Relevance]]
- [[concepts/ux-research/genai-in-qualitative-research|GenAI in Qualitative Research]]
- [[concepts/ux-research/huribot|Huribot]]
- [[concepts/ux-research/automated-ut-setup|Automated UT Setup]]

## Sources

- [[sources/measuringu-ai-usability-problem-analysis-video|MeasuringU: AI Reliability for Finding UI Problems]]
- [[sources/measuringu-ai-real-ui-problems-hallucinations|MeasuringU: Does AI Find Real UI Problems or Just Hallucinations?]]
- [[sources/toss-tech-research-platform-ai|Toss Tech: Huribot Story #1]]

## Open Questions

- [Answered → [[queries/2026-05-27-ai-usability-validation-benchmark|Query Page]]] What validation benchmark should Bonny use before trusting AI-generated UX findings?

