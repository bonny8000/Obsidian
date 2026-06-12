---
type: method
status: active
created: 2026-06-12
updated: 2026-06-12
tags: [method, ux-research, longitudinal, adoption]
sources: []
confidence: 0.6
method_family: generative
best_for: adoption, habit formation, trust trajectory, retention drivers over weeks or months
avoid_when: the decision is due in days, or novelty effects are irrelevant to the question
outputs: wave-over-wave findings, attrition analysis, behavior-change narratives
---

# Method: Longitudinal Research

## Purpose

Study the same people across multiple waves to see how use, attitudes, and trust change after novelty wears off — the dimension single-session studies structurally cannot see.

## Use When

- The question is about week two, not minute two: retention, habit, delegation growth.
- Trust in an AI or agent product needs to be tracked as a trajectory — see [[concepts/agent-experience/trust-calibration|Trust Calibration]] and [[concepts/agent-experience/agent-evaluation-ux|Agent Evaluation UX]].
- A launch needs before/during/after evidence on the same cohort.

## Avoid When

- Timeline or budget cannot sustain multiple waves with the same participants.
- Cross-sectional waves with different samples would answer the question more cheaply.

## Inputs

- Cohort definition and a realistic retention plan (expect 20–40% attrition).
- Wave protocol: which measures repeat verbatim each wave, which rotate.
- Mixed instruments: usage logs where possible, plus diaries or interviews.

## Procedure

1. Fix the repeated-measure core before wave one; it cannot change mid-study.
2. Recruit with attrition headroom and incentives weighted toward completion.
3. Run waves at intervals matched to the behavior's natural rhythm.
4. Analyze within-person change first, then aggregate; report attrition bias honestly.
5. Close with exit interviews replaying each participant's own trajectory.

## Outputs

- Wave-over-wave change on the repeated core.
- Attrition analysis: who dropped out and what that skews.
- Individual trajectory narratives for the report's qualitative spine.

## Quality Bar

- Repeated measures identical across waves.
- Attrition reported as a finding, not hidden.
- Novelty-period data labeled as such, never extrapolated as steady state.

## LLM Assistance

- **Safe uses:** building per-participant trajectory summaries across waves, flagging within-person changes worth probing.
- **Risky uses:** imputing missing waves; narrating change for participants who churned.
- **Verification required:** trajectories traced to wave-level evidence.

## Related

- [[methods/diary-studies|Diary Studies]]
- [[methods/benchmark-studies|Benchmark Studies]]
