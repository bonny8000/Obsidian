---
type: concept
status: active
created: 2026-05-18
updated: 2026-06-29
tags: [design-to-code, ai-coding, frontend]
sources:
  - sources/ditoday-claude-design-uiux-workflow
  - sources/brunch-ghidesigner-482
  - sources/christinevallaure-agentic-ai-design-systems
  - sources/christinevallaure-hypertokens
  - sources/christinevallaure-a2ui-generative-ui
confidence: 0.68
---

# Design-to-Code Workflow

## Summary

A design-to-code workflow turns design intent, screens, components, or prototypes into implementation-ready code while preserving design constraints.

## Why It Matters

AI can accelerate handoff, but it can also introduce mismatches. A useful workflow includes design-system context, codebase context, browser verification, and human review.

## Key Claims

- AI design artifacts can become structured inputs for coding agents.
- Browser automation and screenshot comparison can help verify implementation quality.
- The goal is a loop between design, implementation, and validation rather than a one-way handoff.
- **A six-part Figma pre-flight makes the handoff agent-readable** (three-layer variables, property/name parity, complete state matrix, slots, auto layout, [[concepts/infrastructure-dev/figma-code-connect|Code Connect]]); without it agents re-implement components and silently omit states ([[sources/christinevallaure-agentic-ai-design-systems|Vallaure, 2026]]).
- **Figma expresses only ~1/3 of CSS**, so the agent-facing [[concepts/infrastructure-dev/component-catalog|catalog]] lives as hand-authored code "just past Figma's edge" and a human "stays in the seam" of the canvas→code translation ([[sources/christinevallaure-a2ui-generative-ui|Vallaure, 2026]]).
- **Compiling one token source to many targets** ([[concepts/infrastructure-dev/hypertokens|hypertokens]]) reduces what an agent must reconstruct in the handoff ([[sources/christinevallaure-hypertokens|Vallaure, 2026]]).

## Related Concepts

- [[concepts/infrastructure-dev/design-review-automation|Design Review Automation]]
- [[concepts/ai-agents/planning-to-code-workflow|Planning-to-Code Workflow]]
- [[concepts/ai-agents/vibe-design|Vibe Design]]
- [[concepts/ai-agents/vibe-coding|Vibe Coding]]
- [[concepts/infrastructure-dev/design-system-implementation|Design System Implementation]]
- [[concepts/infrastructure-dev/figma-code-connect|Figma Code Connect]] — the reuse contract in the handoff.
- [[concepts/infrastructure-dev/component-catalog|Component Catalog]] · [[concepts/infrastructure-dev/hypertokens|Hypertokens]]

## Sources

- [[sources/ditoday-claude-design-uiux-workflow|Digital iNSIGHT: Claude Design and UI/UX Workflow]]
- [[sources/brunch-ghidesigner-482|Vibe Design and Coding with Claude Design and Claude Code]]
- [[sources/christinevallaure-agentic-ai-design-systems|Vallaure (2026): Agentic AI, Design Systems & Figma]]
- [[sources/christinevallaure-hypertokens|Vallaure (2026): Hypertokens]]
- [[sources/christinevallaure-a2ui-generative-ui|Vallaure (2026): A2UI Under the Hood]]

## Open Questions

- [Answered → [[queries/2026-05-27-design-to-code-fidelity-threshold|Query Page]]] What fidelity threshold is required before design-to-code output is useful?

