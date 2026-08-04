---
type: method
status: active
created: 2026-06-12
updated: 2026-08-04
tags: [method, ux-research, longitudinal, adoption]
sources: [saeidehbakhshi-usability-metrics-static-product]
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
- [[wiki/concepts/ux-research/measurement-under-adaptation|Measurement Under Adaptation]]
- [[wiki/concepts/ux-research/steerability|Steerability]]

## On Adaptive Products, Trajectory Is the Finding

> [!important] Added 2026-08-04 — a stronger reason to run this method
> This page positions longitudinal work as the way to see adoption, habit, and novelty decay. [[wiki/sources/saeidehbakhshi-usability-metrics-static-product|Bakhshi (2026)]] gives a harder argument: on a personalised product, **trajectory is not extra insight, it is the only place the finding exists.**
>
> *"The product changes as the same person uses it."* A snapshot on an adaptive surface measures a product state that will not recur. The direction of change — is the experience broadening or narrowing? — is structurally invisible to a single session, and it is the question that matters.
>
> **The specific thing to instrument across waves:** log **what the participant was shown** separately from **what they did**, and track exposure diversity. Bakhshi's circularity argument is that a system infers a preference, shows more of it, and reads the resulting repetition as confirmation — *"the system shapes the behavior and it later uses that same behavior as evidence of what the user wants."* Without the exposure log, that narrowing is indistinguishable from genuine preference, and it shows up in the data as healthy engagement.
>
> **Also worth testing across waves:** whether a user's correction to the personalisation *persists*. A "show me less of this" that reverts by the next wave is a placebo control, and only a longitudinal design can detect it. See [[wiki/concepts/ux-research/steerability|Steerability]].
>
> **Unaddressed by the source, and a real planning problem:** how often trajectory must be sampled to detect direction rather than noise. Bakhshi gives no guidance and it is the variable that decides affordability.

## Source Evidence

- [[wiki/sources/saeidehbakhshi-usability-metrics-static-product|Bakhshi (2026): Usability Metrics Assume the Product Stays Still]] — the trajectory dimension, the circularity argument, and the exposure/behaviour split. Conceptual critique, no data.
