---
type: method
status: active
created: 2026-06-12
updated: 2026-06-12
tags: [method, ux-research, wizard-of-oz, agent-experience, ax]
sources: []
confidence: 0.6
method_family: evaluative
best_for: testing agent interaction designs before the agent capability exists
avoid_when: response latency or output quality of the real system is itself the research question
outputs: interaction transcripts, intervention and trust observations, design requirements for the real system
---

# Method: Wizard of Oz Testing

## Purpose

Test how people interact with an "intelligent" system whose intelligence is secretly a human operator — answering interaction-design questions about agents, proactive features, and conversational flows before any model is built.

## Use When

- The agent capability is months away but the interaction design decision is now.
- Questions concern proactivity tolerance, trust formation, turn-taking, or repair behavior — see [[concepts/agent-experience/proactivity-design|Proactivity Design]] and [[concepts/agent-experience/error-recovery|Error Recovery]].
- Comparing interaction patterns (e.g., suggest-vs-act-and-report) cheaply.

## Avoid When

- The real system's latency, error profile, or output quality is the variable under study — a human wizard fakes these poorly.
- Sessions cannot be run consistently enough for the wizard's behavior to be a controlled stimulus.

## Inputs

- A wizard playbook: allowed responses, scripted proactive moments, scripted errors, repair rules.
- The interface shell participants believe is the product.
- A deception-and-debrief protocol cleared with research ethics — see [[concepts/ux-research/research-ethics|Research Ethics]].

## Procedure

1. Script the wizard tightly, including deliberate planted failures to observe recovery behavior.
2. Pilot until the wizard can respond within believable latency.
3. Run tasks; observe reliance, verification, interruption reactions, and repair attempts.
4. Debrief honestly about the deception; capture reactions to the reveal.
5. Translate observations into requirements and evals for the real system.

## Outputs

- Annotated interaction transcripts.
- Observations of trust, reliance, and recovery behavior under controlled failures.
- Interaction requirements and test cases for the production agent.

## Quality Bar

- Wizard behavior consistent across participants; deviations logged.
- Planted failures pre-scripted, not improvised.
- Findings framed as interaction evidence, never as evidence about model feasibility.

## LLM Assistance

- **Safe uses:** drafting wizard playbooks, analyzing transcripts for reliance patterns. An LLM can also serve as a semi-automated wizard for low-stakes pilots.
- **Risky uses:** letting an unscripted LLM wizard improvise mid-study, breaking stimulus control.
- **Verification required:** claims tied to transcript evidence.

## Related

- [[methods/usability-testing|Usability Testing]]
- [[concepts/agent-experience/agent-evaluation-ux|Agent Evaluation UX]]
