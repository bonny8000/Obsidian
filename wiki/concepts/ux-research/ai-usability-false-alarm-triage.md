---
type: concept
status: active
created: 2026-06-10
updated: 2026-06-10
tags: [ux-research, ai, usability-testing, validity, hallucination]
sources:
  - sources/measuringu-ai-real-ui-problems-hallucinations
  - sources/measuringu-ai-usability-problem-analysis-video
confidence: 0.84
---

# AI Usability False-Alarm Triage

## Summary

AI usability false-alarm triage is the practice of classifying AI-generated usability issues as genuine findings, false alarms, or hallucinations before they are treated as research evidence.

## Why It Matters

AI usability review can increase candidate issue coverage, but candidate issues are not findings. MeasuringU's 2026 video review follow-up found that among eleven AI-only issues, one was a genuine find, seven were false alarms, and three were hallucinations. That makes triage a required quality gate rather than a cleanup task.

## Key Claims

- AI-only usability issues need evidence review before they enter a report.
- False alarms differ from hallucinations: a false alarm can be based on something real but interpreted as the wrong problem, while a hallucination reports something that did not happen.
- Literal task interpretation can create systematic false alarms when AI ignores pragmatic evidence of task success.
- Multiple AI runs can help identify consistency, but consistency does not remove the need to check the original video, transcript, or interaction log.
- The useful role for AI is candidate issue generation or junior-researcher assistance, not final expert judgment.

## Related Concepts

- [[concepts/ux-research/ai-usability-analysis|AI Usability Analysis]]
- [[concepts/ux-research/reliability-vs-validity|Reliability vs Validity]]
- [[concepts/ux-research/evaluator-effect|Evaluator Effect]]
- [[concepts/ux-research/validity-and-decision-relevance|Validity and Decision Relevance]]
- [[concepts/ux-research/ai-evals|AI Evals in Research]]

## Sources

- [[sources/measuringu-ai-real-ui-problems-hallucinations|MeasuringU: Does AI Find Real UI Problems or Just Hallucinations?]]
- [[sources/measuringu-ai-usability-problem-analysis-video|MeasuringU: AI Reliability for Finding UI Problems]]

## Open Questions

- What minimum evidence checklist should the wiki use before accepting an AI-generated usability issue?
- Should AI-only issues be tracked as hypotheses until a human researcher verifies video evidence?
