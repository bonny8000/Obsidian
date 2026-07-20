---
type: concept
status: active
created: 2026-07-20
updated: 2026-07-20
tags: [agent-experience, ax, framework, microsoft]
sources:
  - sources/microsoft-design-ux-for-agents
confidence: 0.8
---

# Microsoft Agent UX Principles

> [!abstract] Summary
> Microsoft Design's framework for agentic experiences structured around three dimensions: Space (how it operates in the environment), Time (how it uses past/present/future context), and Core (trust and transparency).

> [!important] Why it Matters
> As one of the major platforms deploying agents at scale, Microsoft's principles provide a structured way to evaluate whether an agent is human-centric, avoiding common pitfalls like over-notification, opacity, or user replacement.

## 📝 Key Claims

The framework is divided into Space, Time, and Core dimensions:

**1. Agent (Space) - The Environment**
- **Connecting, not collapsing:** Agents should connect people to knowledge and each other, not replace or belittle human roles.
- **Easily accessible yet occasionally invisible:** Agents should operate across modalities and seamlessly transition between foreground (proactive/reactive) and background operations, only nudging when appropriate.

**2. Agent (Time) - The Chronology**
- **Past (Reflecting on history):** Agents must leverage rich memory, connecting past events and context, moving beyond single-shot queries.
- **Now (Nudging more than notifying):** Agents should use dynamic, context-aware cues rather than static formal notifications, respecting the user's current environment.
- **Future (Adapting and evolving):** Agents must adapt to user behavior, preferences, and accessibility needs over time.

**3. Agent (Core) - The Foundation**
- **Embrace uncertainty but establish trust:** Uncertainty is a feature of agent design. To prevent overreliance, the system must expose its reasoning and level of certainty.
- **Transparency, control, and consistency:** Users must have ultimate control over the agent (on/off, settings). Background actions require visible audit trails (logs/dashboards), and interactions should use familiar UI paradigms to reduce cognitive load.

## 🔗 Related Concepts
- [[concepts/agent-experience/trust-calibration|Trust Calibration]]
- [[concepts/agent-experience/agent-transparency|Agent Transparency]]
- [[concepts/agent-experience/proactivity-design|Proactivity Design]]
- [[concepts/agent-experience/initiative-and-interruption|Initiative and Interruption]]

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> The principle of being "occasionally invisible" (operating in the background) inherently conflicts with the need for "transparency and control." Microsoft proposes solving this via dedicated dashboards, but the UX pattern for effectively monitoring background agents without babysitting them remains an unsolved industry challenge.

## 📚 Sources
- [[sources/microsoft-design-ux-for-agents|Microsoft Design: UX Design for Agents]]

## ❓ Open Questions
- What are the concrete UI patterns for "nudging more than notifying" that effectively capture attention without breaking flow?
- How much "uncertainty" can users tolerate in enterprise applications before they abandon the agent?
