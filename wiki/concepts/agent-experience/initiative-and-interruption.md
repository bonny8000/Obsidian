---
type: concept
status: active
created: 2026-06-12
updated: 2026-06-12
tags: [agent-experience, mixed-initiative, attention, ax]
sources:
  - sources/andru-saksena-adobe-haic-2025
  - sources/horvitz-1999-mixed-initiative
  - sources/amershi-2019-human-ai-guidelines
confidence: 0.78
---

# Initiative and Interruption

## Summary

Where [[concepts/agent-experience/proactivity-design|Proactivity Design]] decides whether an agent should act unprompted, initiative-and-interruption design decides the tactics: who holds the floor, when the agent may take it, and how much attention each interruption may claim.

## Why It Matters

Attention is the scarcest resource in agentic products. An agent that interrupts at the wrong moment trains users to ignore or disable it; an agent that never speaks up wastes its context advantage.

## Key Claims

- Mixed-initiative interaction treats turn-taking as a negotiated resource: either party can propose, but the user can always reclaim control instantly.
- Interruption cost depends on task state; interrupting mid-flow is far more expensive than at natural boundaries (task completion, idle moments, session start).
- Interruption budget should be explicit in design: a cap on unprompted touches per session/day, spent on the highest-confidence, highest-value moments.
- Modality should scale with urgency: ambient cue < inline suggestion < notification < blocking dialog. Most agent messages deserve the lowest tier.
- Batching low-urgency items into digests preserves value while protecting flow.
- Horvitz demonstrated a graded-autonomy ladder selected by inferred confidence: do nothing, suggest, act with confirmation, act automatically — the canonical template for interruption-tier design — see [[sources/horvitz-1999-mixed-initiative|Horvitz 1999]].

## Related Concepts

- [[concepts/agent-experience/proactivity-design|Proactivity Design]]
- [[concepts/agent-experience/collaboration-patterns|Collaboration Patterns]]
- [[concepts/ux-research/progressive-user-control|Progressive User Control]]
- [[concepts/ai-agents/long-horizon-tasks|Long-Horizon Tasks]]

## Conflicts & Caveats

- Horvitz (1999) is now ingested and grounds the attention-cost and graded-autonomy claims; transfer to long-horizon autonomous agents is supported by its continued citation in 2025-26 proactive-agent literature but remains an active research question.

## Sources

- [[sources/horvitz-1999-mixed-initiative|Horvitz (1999): Mixed-Initiative User Interfaces]]
- [[sources/amershi-2019-human-ai-guidelines|Amershi et al. (2019): Human-AI Guidelines]]
- [[sources/andru-saksena-adobe-haic-2025|Adobe HAIC Framework]]

## Open Questions

- For background agents running long tasks, what events justify an interruption versus a status line the user can poll?
