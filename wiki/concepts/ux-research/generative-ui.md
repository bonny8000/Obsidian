---
type: concept
status: active
created: 2026-06-01
updated: 2026-06-29
tags: [ai, ux-design, dynamic-ui]
sources:
  - google-io-2026-agentic-gemini
  - sources/christinevallaure-a2ui-generative-ui
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

## Sources
- [[sources/christinevallaure-a2ui-generative-ui|Christine Vallaure (2026): A2UI Under the Hood — Designing for Radically Adaptive UI]]
