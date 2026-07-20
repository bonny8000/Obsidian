---
type: concept
status: active
created: 2026-06-01
updated: 2026-06-10
tags: [concept, ai-agents, ux-research, governance]
sources:
  - sources/hbs-working-knowledge-ai-advice-willful-blindness
  - sources/langchain-loop-engineering
confidence: 0.88
---

# Human-in-the-Loop

> Rebuilt 2026-06-10 after corruption ([[logs/2026-06-10-corruption-recovery|recovery log]]). Original claims lost; reconstructed from backlink context.

## Summary

Design pattern where automated/AI systems route judgments, approvals, or interpretations through a human before consequential action. In UX research, the human owns interpretation and meaning-making while AI handles scale (transcription, pattern surfacing, recruitment screening).

## Why it matters

Recurring spine across this wiki's clusters: agentic automation ([[concepts/ai-agents/agentic-ai|Agentic AI]], [[concepts/ux-research/huribot|Huribot]]) is only trustworthy where human checkpoints are explicit. Sources here repeatedly find AI analysis unreliable without human triage (e.g., [[concepts/ux-research/ai-usability-false-alarm-triage|AI Usability False-Alarm Triage]]).

## Key claims

- Human review is most valuable at interpretation and decision points, not mechanical steps. (conf 0.85)
- "Approve-by-default" loops degrade into rubber-stamping; checkpoint design matters. (conf 0.7, inferred)
- **Checkpoints are vulnerable to strategic avoidance (willful blindness):** Human operators will actively ignore explanations or skip review checkpoints if doing so maximizes output-based incentives (bonuses) or avoids moral discomfort, making "checkbox transparency" a major design flaw — see [[concepts/agent-experience/willful-blindness|Willful Blindness]]. (conf 0.90)
- **HITL fits across four nested loop levels:** Loop 1 (input gates before sensitive actions), Loop 2 (human-as-grader), Loop 3 (output approval before production delivery), and Loop 4 (harness-change review before deployment) — see [[concepts/ai-agents/loop-engineering|Loop Engineering]]. (conf 0.85)

## Related concepts

- [[concepts/ux-research/human-interpretation|Human Interpretation]]
- [[concepts/ux-research/ai-usability-false-alarm-triage|AI Usability False-Alarm Triage]]
- [[concepts/ai-agents/agentic-ai|Agentic AI]]

## Sources

- [[sources/hbs-working-knowledge-ai-advice-willful-blindness|Chan (2026): When AI Gives Advice, Employees Rarely Ask Why]]
- [[sources/langchain-loop-engineering|Runkle (2026): The Art of Loop Engineering]]
- See backlinks; original source list lost in corruption.

## Open questions

- Where exactly should the human checkpoint sit in an automated UT pipeline (setup, analysis, or reporting)?
