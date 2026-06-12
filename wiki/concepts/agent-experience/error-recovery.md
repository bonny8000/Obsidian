---
type: concept
status: active
created: 2026-06-12
updated: 2026-06-12
tags: [agent-experience, error-handling, repair, ax]
sources:
  - sources/amershi-2019-human-ai-guidelines
  - sources/lee-see-2004-trust-in-automation
confidence: 0.75
---

# Error Recovery

## Summary

Error recovery in agent experience covers how an agent and its interface handle failure: detecting it, admitting it, undoing damage, and repairing the interaction so the user keeps working instead of abandoning the agent.

## Why It Matters

Agents fail probabilistically and will keep failing; the differentiator is not error rate alone but how cheap an error is to detect and reverse. Recovery quality is the strongest determinant of whether trust survives the first failures.

## Key Claims

- Reversibility is the master lever: preview-before-commit, dry runs, undo, and versioned changes turn high-stakes delegation into low-stakes experimentation.
- Agents should fail loudly and specifically ("I couldn't verify the invoice date") rather than silently producing a plausible wrong answer.
- Conversational repair is a skill surface: the agent should accept correction gracefully, update, and confirm what changed — without over-apologizing or over-correcting.
- Blame asymmetry exists: users forgive errors they catch early and can fix in one step; they punish errors discovered late downstream.
- Error states deserve as much design effort as happy paths; most agent products design only the demo path.
- Amershi et al.'s G7-G11 effectively specify this concept: an AI service must be cheap to invoke, cheap to dismiss, cheap to correct, must scope down when uncertain, and must explain its behavior — see [[sources/amershi-2019-human-ai-guidelines|Amershi et al. 2019]].

## Related Concepts

- [[concepts/agent-experience/trust-calibration|Trust Calibration]]
- [[concepts/agent-experience/agent-transparency|Agent Transparency]]
- [[concepts/ux-research/ai-usability-false-alarm-triage|AI Usability False Alarm Triage]]
- [[concepts/ux-research/human-in-the-loop|Human in the Loop]]

## Conflicts & Caveats

- Now grounded in Amershi et al.'s when-wrong guidelines (G7-G11: cheap invocation, dismissal, correction; scope when uncertain; explain why) and Lee & See's finding that trust dynamics hinge on failure handling. Undo-granularity claims remain hypotheses.

## Sources

- [[sources/amershi-2019-human-ai-guidelines|Amershi et al. (2019): Human-AI Guidelines]]
- [[sources/lee-see-2004-trust-in-automation|Lee & See (2004): Trust in Automation]]

## Open Questions

- What undo granularity do users expect for multi-step agent actions — per step, per task, or per session?
