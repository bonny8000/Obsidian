---
type: source
status: active
created: 2026-06-10
updated: 2026-06-10
tags: [source, ux-research, ai-usability-analysis, hallucination, false-alarm, evaluator-effect]
sources:
  - raw/web/measuringu-ai-real-ui-problems-hallucinations-2026-05-26
confidence: 0.88
---

# MeasuringU: Does AI Find Real UI Problems or Just Hallucinations?

## Citation

Lewis, Jim; Sauro, Jeff; Schiavone, Will; Plabst, Lucas. "Does AI Find Real UI Problems or Just Hallucinations?" MeasuringU, 2026-05-26.

URL: https://measuringu.com/does-ai-find-real-ui-problems-or-just-hallucinations/

Raw source card: `raw/web/measuringu-ai-real-ui-problems-hallucinations-2026-05-26.md`

## Summary

This article tests whether AI-only usability problems from a video review are genuine human misses, false alarms, or hallucinations. It extends the earlier MeasuringU reliability article by adding a validity-oriented classification layer.

The useful takeaway for the wiki is that AI usability analysis can add signal, but the AI-only issue list should be triaged before it is treated as research evidence.

## Extracted Data

| Measure | Reported value |
| --- | --- |
| Human researchers | 4 |
| AI systems | ChatGPT-5.4 Thinking and Gemini 3 Flash Thinking |
| Runs per AI | 4 |
| Human-identified usability problems | 9 |
| Combined AI-identified problems | 14 |
| AI-only problems | 11 |
| AI-only genuine finds | 1 of 11 |
| AI-only false alarms | 7 of 11 |
| AI-only hallucinations | 3 of 11 |

## Extracted Claims

- AI-only usability problems should be classified before they enter a findings list.
- In this study, roughly nine out of ten AI-only problems needed correction or dismissal.
- False alarms were more common than hallucinations; they came from real observations interpreted as the wrong usability claim.
- Human oversight is still necessary because hallucinations cannot be detected without checking the original video evidence.
- Multiple AI runs may help flag consistency patterns, but consistency is not validity.

## Linked Concepts

- [[concepts/ux-research/ai-usability-analysis|AI Usability Analysis]]
- [[concepts/ux-research/ai-usability-false-alarm-triage|AI Usability False-Alarm Triage]]
- [[concepts/ux-research/reliability-vs-validity|Reliability vs Validity]]
- [[concepts/ux-research/evaluator-effect|Evaluator Effect]]
- [[concepts/ux-research/validity-and-decision-relevance|Validity and Decision Relevance]]

## Reliability Notes

Primary source for a small MeasuringU study. The article is useful evidence for building review rubrics, but it should not be generalized as a population estimate because it uses one video, one prompt setup, and two LLM families.
