---
type: method
status: active
created: 2026-06-12
updated: 2026-06-12
tags: [method, ux-research, usability-testing]
sources:
  - sources/measuringu-ai-real-ui-problems-hallucinations
  - sources/measuringu-ai-usability-problem-analysis-video
  - sources/tullis-albert-measuring-ux-2013
  - sources/sauro-lewis-quantifying-ux-2016
confidence: 0.86
method_family: evaluative
best_for: task friction, learnability, interface defects, usability risk
avoid_when: the product surface is undefined or the question is only about market demand
outputs: issue list, severity, evidence clips, task metrics, design recommendations
---

# Method: Usability Testing

## Purpose

Usability testing evaluates whether people can complete important tasks with a product surface, where they struggle, and whether the observed problems are severe enough to change design priorities.

## Use When

- A prototype, product flow, or interactive artifact exists.
- The team needs evidence about task success, confusion, efficiency, or perceived effort.
- The research question is about an actual experience rather than broad attitudes.

## Avoid When

- There is no concrete task or artifact to test.
- The team mainly needs segmentation, demand sizing, or pricing evidence.
- The study would rely only on AI-generated users without human validation.

## Inputs

- Research question tied to a product decision.
- Task scenarios with clear success criteria.
- Participant criteria linked to [[concepts/ux-research/participant-selection-criteria|Participant Selection Criteria]].
- Observation protocol and severity rubric.

## Procedure

1. Define tasks, success criteria, and what counts as a usability problem.
2. Recruit participants who match the decision context.
3. Observe task attempts and capture behavioral evidence before interpretation.
4. Code issues, severity, and possible causes.
5. Separate observed problems from researcher inference and LLM-suggested themes.

## Outputs

- Usability issue inventory.
- Severity-ranked recommendations.
- Task success and time-on-task where appropriate.
- Evidence clips or source-linked observations.

## Quality Bar

- Keep observations separate from interpretation.
- Track false positives when using AI assistance.
- Tie each recommendation to observed behavior, not just participant preference.

## LLM Assistance

- **Safe uses:** clustering observed issues, drafting problem statements, finding repeated patterns.
- **Risky uses:** inventing causes, ranking severity without evidence, treating hallucinated issues as real.
- **Verification required:** check AI-generated findings against raw sessions and source notes.

## Related Concepts

- [[concepts/ux-research/ai-usability-analysis|AI Usability Analysis]]
- [[concepts/ux-research/ai-usability-false-alarm-triage|AI Usability False-Alarm Triage]]
- [[concepts/ux-research/evaluator-effect|Evaluator Effect]]
- [[concepts/ux-research/sample-size-for-usability-studies|Sample Size for Usability Studies]]

## Source Evidence

- [[sources/measuringu-ai-real-ui-problems-hallucinations|MeasuringU - AI Real UI Problems and Hallucinations]]
- [[sources/measuringu-ai-usability-problem-analysis-video|MeasuringU - AI Usability Problem Analysis Video]]
- [[sources/tullis-albert-measuring-ux-2013|Tullis and Albert - Measuring UX]]
- [[sources/sauro-lewis-quantifying-ux-2016|Sauro and Lewis - Quantifying UX]]

