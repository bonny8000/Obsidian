---
type: method
status: active
created: 2026-06-12
updated: 2026-06-12
tags: [method, ux-research, diary-study, longitudinal]
sources: []
confidence: 0.6
method_family: generative
best_for: in-context behavior over days or weeks, triggers, experience change over time
avoid_when: you need observed behavior, a decision is due this week, or the behavior is too rare to capture
outputs: entry corpus, journey timelines, trigger inventory, experience-over-time themes
---

# Method: Diary Studies

## Purpose

Capture what people actually do and feel in their real context over time, through structured self-reports triggered by events or schedules — the behaviors no lab session can reproduce.

## Use When

- The experience unfolds over days or weeks (adoption, habit formation, recurring service touchpoints).
- Triggers and context matter: when, where, and why someone reaches for the product.
- You need a longitudinal baseline before or after a launch.

## Avoid When

- Recall and self-report bias would invalidate the question (use logs or observation).
- The target behavior happens less than a few times per study period.
- Participants cannot realistically sustain the reporting burden.

## Inputs

- A behavior or trigger definition participants can recognize unambiguously.
- Entry protocol: structured prompts, media capture rules, expected cadence.
- Incentive structure that rewards consistency, not volume.
- Participant criteria linked to [[concepts/ux-research/participant-selection-criteria|Participant Selection Criteria]].

## Procedure

1. Define the trigger ("every time you…") and the entry template (situation, action, feeling, friction).
2. Pilot the protocol with 1–2 participants; cut any prompt that takes over two minutes.
3. Run 1–4 weeks with mid-study check-ins to sustain compliance and probe interesting entries.
4. Close with exit interviews that walk through each participant's own entries.
5. Analyze across time (per participant) and across participants (per trigger or theme).

## Outputs

- Entry corpus with timestamps and context metadata.
- Per-participant journey timelines.
- Trigger and friction inventories.
- Themes of change over time (novelty decay, trust growth, workaround formation).

## Quality Bar

- Compliance rate reported honestly; thin weeks flagged, not papered over.
- Entries treated as self-report, triangulated against logs or interviews before driving decisions.
- Exit interviews grounded in the participant's actual entries, not generic questions.

## LLM Assistance

- **Safe uses:** clustering entries, building per-participant timelines, flagging entries worth probing in check-ins.
- **Risky uses:** synthesizing "typical days" that no participant actually reported; filling gaps in sparse data.
- **Verification required:** every theme must trace to specific entries.

## Related

- [[methods/longitudinal-research|Longitudinal Research]]
- [[methods/semi-structured-interviews|Semi-Structured Interviews]]
- [[concepts/agent-experience/agent-evaluation-ux|Agent Evaluation UX]] — diary protocols suit trust-trajectory questions for agents.
