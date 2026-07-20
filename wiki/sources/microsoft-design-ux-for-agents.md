---
type: source
status: active
created: 2026-07-20
updated: 2026-07-20
tags: [source, agent-experience, microsoft]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.9
---

# Microsoft: UX Design for Agents

> [!info] Metadata
> - **Author:** Ruokan He, Jen Fox, Amanda Snellinger (Microsoft Design)
> - **Date:** 2025/2026
> - **Type:** article
> - **Raw File:** [[raw/web/microsoft-ux-design-agents.md]]

## Citation

Microsoft Design (He, Fox, Snellinger). "Microsoft principles and guidelines for building agentic experiences." Microsoft Design Blog.

## Summary

This article establishes Microsoft Design's framework for Agent UX, structured around three dimensions: Space (environment), Time (past/present/future), and Core (trust and transparency). It defines agents as autonomous systems that collaborate with users and go beyond text chat, emphasizing multimodal, dynamic, and sometimes invisible interactions.

## Key Claims

- **Agent (Space):** Agents should connect people rather than replace them ("Connecting not collapsing"), and they should be easily accessible across devices but occasionally operate invisibly in the background. Active multimodal capabilities must be clearly visible.
- **Agent (Time):** 
  - *Past:* Agents use rich memory and context beyond simple states to inform current actions.
  - *Now:* Agents should "nudge more than notify"—using dynamic cues, contextual awareness, and gradual complexity rather than static formal notifications.
  - *Future:* Agents must adapt to user behavior, feedback, and accessibility needs over time.
- **Agent (Core):**
  - *Embrace Uncertainty:* A level of uncertainty is expected; reasoning and certainty levels must be visible to establish appropriate trust and avoid overreliance.
  - *Foundational Elements:* Transparency (about data, skills, connections), control (customizable settings, clear on/off), and consistency (using familiar UI) are non-negotiable. Background agents must have user-facing mechanisms to view and control their actions.

## Useful Examples

- **Nudging vs Notifying:** Instead of a static notification, an agent might proactively start a chat or generate a cue based on the user's private vs. public environment.
- **Background to Foreground:** An agent may run invisibly as a background process, but it must have a log/dashboard where its actions are visible and controllable.

## Constraints / Caveats

- The principles are high-level and generalized; specific UI patterns (e.g., exact dashboards for background agents) are not detailed.
- Some capabilities mentioned (like advanced memory systems) are noted as being "under development."

## Design Implications

- **Design for Invisibility:** Allow agents to do work in the background without constantly interrupting the user, but provide clear audit trails.
- **Multimodal by Default:** Plan for voice, vision, and gesture inputs, ensuring it's obvious to the user when these sensors are active.
- **Dynamic Interaction:** Move away from hardcoded dialog boxes and notifications toward context-aware, gradual interaction flows.

## Tensions

- **Invisibility vs. Transparency:** Operating "invisibly" in the background creates a tension with the requirement for full transparency and control. This must be solved through dedicated management surfaces (logs/dashboards).
- **Embracing Uncertainty vs. Consistency:** Finding the balance between an agent's expected non-deterministic nature and the user's need for familiar, consistent UX elements.

## Open Questions

- What specific UI patterns best support "nudging more than notifying" without becoming annoying?
- How should background agent actions be summarized in a dashboard to avoid information overload while maintaining trust?

## Concepts Linked

- [[concepts/agent-experience/microsoft-agent-ux-principles|Microsoft Agent UX Principles]]
- [[concepts/agent-experience/trust-calibration|Trust Calibration]]
- [[concepts/agent-experience/agent-transparency|Agent Transparency]]
- [[concepts/agent-experience/initiative-and-interruption|Initiative and Interruption]]

## LLM Use

- **Use for:** Grounding Agent UX discussions in Microsoft's official three-dimensional framework (Space, Time, Core).
- **Do not use for:** Detailed implementation specifics or technical architecture.
- **Best prompt pattern:** Ask the LLM to map a proposed agent interaction against the Microsoft Space/Time/Core dimensions to ensure it respects human-centric boundaries.

## Reliability Notes

> [!warning] Caveats
> This is a high-level framework published by Microsoft Design, representing best practices and aspirations rather than empirical academic studies, though it claims to be backed by deep user research.
