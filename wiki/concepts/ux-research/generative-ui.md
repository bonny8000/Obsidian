---
type: concept
status: active
created: 2026-06-01
updated: 2026-08-04
tags: [ai, ux-design, dynamic-ui]
sources:
  - google-io-2026-agentic-gemini
  - sources/christinevallaure-a2ui-generative-ui
  - sources/google-search-io-2026-agents
confidence: 0.90
---

# Generative UI

## Summary
Generative UI refers to user interfaces that are created or adapted in real-time by an AI model to match the specific context, intent, and capabilities of the user. Unlike static UI, Generative UI is probabilistic and ephemeral.

## Key Primitives
- **Just-in-Time Layouts:** Creating a custom view for a specific query (e.g., a custom comparison table for travel options).
- **Component Synthesis:** Combining existing UI primitives into new configurations on the fly.
- **Contextual Adaptation:** Changing the interface complexity based on the user's expertise or current environment.

## Why it matters
It marks the end of "one-size-fits-all" interface design. Generative UI allows for an infinite number of interface variations, providing each user with the most efficient tool for their immediate task, which is a core pillar of [[concepts/ux-research/ax-ai-experience|AX (AI Experience)]].

## Key Claims
- **Constrained generative UI is the safer form.** Vallaure's A2UI ("the interface is built fresh in the moment, for the exact person or the exact thing they asked for") restricts the agent to a designer-authored [[concepts/infrastructure-dev/component-catalog|component catalog]], preventing generic "div soup" while keeping the adaptivity ([[sources/christinevallaure-a2ui-generative-ui|Vallaure, 2026]]).
- The catalog is both the agent's palette and its security boundary — "the model can only name components that exist in the catalog."
- The dominant failure mode is the **quiet downgrade**: an incomplete catalog silently substitutes the wrong component or drops to chat.

## Related Concepts
- [[concepts/ux-research/ax-ai-experience|AX (AI Experience)]]
- [[concepts/infrastructure-dev/figma-make|Figma Make]]
- [[concepts/infrastructure-dev/deterministic-ui|Deterministic UI]]
- [[concepts/agent-experience/a2ui-protocol|A2UI Protocol]] — a constrained, catalog-bounded form of generative UI.
- [[concepts/infrastructure-dev/component-catalog|Component Catalog]] — what bounds generative UI to stay on-brand.

## Status Change: Generative UI Is Now a Mass Default

> [!important] Re-baselined 2026-08-04
> This page has treated generative UI as an emerging pattern and a considered design choice. At I/O 2026 ([[wiki/sources/google-search-io-2026-agents|Reid, 2026-05-19]]) Google announced it **free to all Search users** from summer 2026 — powered by Antigravity and Gemini 3.5 Flash, assembling *"custom layouts, assembling components in real-time"* with interactive visuals, tables, graphs, and simulations.
>
> **Two consequences.**
>
> **1. The argumentative burden has flipped.** Any design case in this vault that treats generated interfaces as novel is now arguing against the default behaviour of the world's largest interface. Note the strategy visible in Google's own rollout gating: **generated surfaces are free; delegated action (Information Agents, agentic booking, dashboards) is paid.** Google is treating generative UI as what Search *is*, not as a premium feature.
>
> **2. It shipped with no evaluation.** The announcement contains no accuracy figures, no failure rates, and no comparison against a page of links — and no measurement exists of whether users retain or verify differently from a generated surface. That question now applies to roughly a billion people and nobody has asked it.
>
> Caveat: this is a first-party product announcement. Announced ≠ shipped, and this vault has not verified the summer-2026 rollout.

## Sources
- [[sources/christinevallaure-a2ui-generative-ui|Christine Vallaure (2026): A2UI Under the Hood — Designing for Radically Adaptive UI]]
- [[wiki/sources/google-search-io-2026-agents|Google (2026): Search at I/O 2026]] — generative UI free to all Search users; the free/paid split.

## Related (added 2026-08-04)
- [[wiki/concepts/product-management/geo-generative-engine-optimization|GEO]] — what "being cited" means when the answer is an assembled layout is now unsettled.
- [[wiki/concepts/infrastructure-dev/ai-crawler-governance|AI Crawler Governance]] — the publisher side of a surface that substitutes for the visit.
- [[wiki/concepts/agent-experience/system-state-signaling|System State Signaling]]
