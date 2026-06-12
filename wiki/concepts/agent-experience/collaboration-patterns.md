---
type: concept
status: active
created: 2026-06-12
updated: 2026-06-12
tags: [agent-experience, collaboration, delegation, ax]
sources:
  - sources/andru-saksena-adobe-haic-2025
  - sources/google-io-2026-agentic-gemini
  - sources/horvitz-1999-mixed-initiative
confidence: 0.7
---

# Collaboration Patterns

## Summary

Human–agent collaboration patterns are recurring division-of-labor structures between user and agent: who plans, who executes, who reviews, and how control transfers between them during a task.

## Why It Matters

Choosing the wrong pattern for a task is a structural UX failure no amount of UI polish fixes. A pattern catalog gives designers a vocabulary for matching agent autonomy to task stakes and user expertise.

## Key Claims

- Core patterns include: assistant (user drives, agent executes steps), reviewer (agent drives, user approves), co-creator (interleaved turns on a shared artifact), delegate (agent owns the task end-to-end and reports), and supervisor (user monitors a fleet of agent tasks).
- The same product often needs multiple patterns across one journey; the design problem is making the current pattern and its handoff points legible.
- Shared artifacts (a document, a board, a diff) coordinate collaboration better than pure conversation because state is visible to both parties.
- Pattern choice should follow stakes × reversibility × user expertise, not a single global autonomy setting.
- Transitions are the dangerous moments: control handoffs need explicit confirmation of who owns what next.
- The field-defining move is Horvitz's: reject the direct-manipulation-versus-agents binary and design the coupling, with control transferable at any moment — see [[sources/horvitz-1999-mixed-initiative|Horvitz 1999]].

## Related Concepts

- [[concepts/agent-experience/proactivity-design|Proactivity Design]]
- [[concepts/agent-experience/initiative-and-interruption|Initiative and Interruption]]
- [[concepts/ux-research/haic-modalities-taxonomy|HAIC Modalities Taxonomy]]
- [[concepts/ux-research/designing-for-agency|Designing for Agency]]
- [[concepts/ai-agents/orchestrator-of-agents|Orchestrator of Agents]]
- [[concepts/ai-agents/conversational-canvas|Conversational Canvas]]

## Conflicts & Caveats

- Pattern names are not standardized across the industry; this taxonomy is a working synthesis. Its foundation — coupling automation with direct manipulation rather than choosing between them — is grounded in Horvitz (1999).

## Sources

- [[sources/horvitz-1999-mixed-initiative|Horvitz (1999): Mixed-Initiative User Interfaces]]
- [[sources/andru-saksena-adobe-haic-2025|Adobe HAIC Framework]]
- [[sources/google-io-2026-agentic-gemini|Google I/O 2026: Agentic Gemini]]

## Open Questions

- Which pattern do users actually prefer for consequential domains (finance, account changes) versus what they claim in interviews?
