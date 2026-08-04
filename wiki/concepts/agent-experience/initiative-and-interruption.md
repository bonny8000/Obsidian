---
type: concept
status: active
created: 2026-06-12
updated: 2026-08-04
tags: [agent-experience, mixed-initiative, attention, ax]
sources:
  - sources/andru-saksena-adobe-haic-2025
  - sources/horvitz-1999-mixed-initiative
  - sources/amershi-2019-human-ai-guidelines
  - sources/google-search-io-2026-agents
  - sources/paxton-yao-voice-ai-thinking-state
  - sources/toyota-voice-interaction-humanoid-robots
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
- **Nudging more than notifying:** Microsoft Design advocates replacing static, formal notifications with dynamic, context-aware cues that respect the user's environment (e.g. public vs. private) — see [[concepts/agent-experience/microsoft-agent-ux-principles|Microsoft Agent UX Principles]].

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
- [[sources/microsoft-design-ux-for-agents|Microsoft Design (2025): UX Design for Agents]]

## Open Questions

- For background agents running long tasks, what events justify an interruption versus a status line the user can poll?
- **Do users notice, or care, that no interruption contract exists?** Google shipped 24/7 monitoring agents to paid tiers without describing one.
- **Is the response gap a turn-taking problem?** If so, this concept — not "loading states" — is where latency design belongs.

## Two Additions, 2026-08-04

> [!important] The pattern this concept exists for is now shipping, with no interruption contract described
> [[wiki/sources/google-search-io-2026-agents|Google's Information Agents]] (announced I/O 2026, paid tiers, summer 2026) operate *"in the background, 24/7"* over blogs, news, social posts, and live finance/shopping/sports data, then push synthesised updates. Example uses: apartment-hunting alerts, notifications about a named athlete.
>
> A standing monitor that decides *when to interrupt* is making initiative decisions continuously. The announcement says **nothing** about frequency, thresholds, snooze, why-this-fired explanations, or how a user corrects a bad monitor. The open questions on this page stop being theoretical.
>
> **What a monitoring agent needs, and Google has not described:** a frequency budget, a materiality threshold, a visible reason for each notification, and a correction path that persists (see [[wiki/concepts/ux-research/steerability|Steerability]] — a "show me less of this" that reverts next session is not control).

> [!important] The response gap is a floor-holding problem, not a progress-bar problem
> The most revealing detail in [[wiki/sources/paxton-yao-voice-ai-thinking-state|Yao (2026)]] is that NIO's NOMI assistant has a **countdown** state — not system processing at all, but a window in which *the user may still speak*. That is a turn-taking signal, and it is the state a system-centric model never enumerates.
>
> Read that way, [[wiki/sources/toyota-voice-interaction-humanoid-robots|Toyota's]] pre-emptively generated fillers (*"Um"*, *"Well"*) are the same move in speech: not progress indicators but **claims on the floor**, which is what human conversation has always used them for. Both sources reinvent turn-taking repair and neither names it.
>
> **Implication for this concept:** interruption is usually framed here as the agent breaking into the user's attention. Turn-taking is the symmetrical case — who holds the floor, and how does each party know. See [[wiki/concepts/agent-experience/response-latency-masking|Response Latency Masking]], [[wiki/concepts/agent-experience/system-state-signaling|System State Signaling]], and [[wiki/analyses/2026-08-04-the-response-gap|the 2026-08-04 memo]], where this reframe is argued at length. It is the vault's inference, not either source's claim.

## Additional Sources

- [[wiki/sources/google-search-io-2026-agents|Google (2026): Search at I/O 2026]] — Information Agents as persistent monitors; no interruption model described.
- [[wiki/sources/paxton-yao-voice-ai-thinking-state|Yao (2026): Voice AI Gave Designers a New State to Show]] — the countdown state, and ambiguous silence.
- [[wiki/sources/toyota-voice-interaction-humanoid-robots|Toyota FRC (2026): Voice Interaction with Humanoid Robots]] — fillers as floor-holding.
