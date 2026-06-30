---
type: concept
status: draft
created: 2026-05-21
updated: 2026-06-29
tags: [concept, design-philosophy, frontend]
sources:
  - sources/hsol-ai-portfolio-6
  - sources/pxd-color-token-design-2026
  - sources/christinevallaure-hypertokens
  - sources/christinevallaure-a2ui-generative-ui
confidence: 0.9
---

# Deterministic UI

## Summary
A design philosophy where the user interface (UI) is a pure, predictable function of the underlying data state. In the [[sources/hsol-ai-portfolio-6|AI Portfolio]] example, the website's layout and content are automatically generated from the Obsidian vault's data graph.

## Why it Matters
It reduces manual design work and ensures that the presentation layer is always in sync with the source of truth. It allows for "hands-free" portfolio maintenance.

## Key Claims
- If the data (markdown files and their links) changes, the UI updates deterministically.
- Designers focus on the "ObjectView" logic rather than individual page layouts.
- Semantic color tokens are another deterministic pattern: UI color resolves from role, state, and theme rules rather than from one-off screen decisions.
- [[concepts/infrastructure-dev/hypertokens|Hypertokens]] extend this to bundled style decisions: one upstream source of truth compiles deterministically to each tool's copy (CSS, Figma, Swift), removing per-tool drift ([[sources/christinevallaure-hypertokens|Vallaure, 2026]]).
- Catalog validation in [[concepts/agent-experience/a2ui-protocol|A2UI]] pulls open-ended generative UI back toward deterministic guarantees — the agent can only assemble from approved catalog components ([[sources/christinevallaure-a2ui-generative-ui|Vallaure, 2026]]).

## Related Concepts
- [[concepts/infrastructure-dev/objectview|ObjectView]]
- [[concepts/infrastructure-dev/design-automation|Design Automation]]
- [[concepts/infrastructure-dev/color-token-architecture|Color Token Architecture]]
- [[concepts/infrastructure-dev/hypertokens|Hypertokens]]
- [[concepts/agent-experience/a2ui-protocol|A2UI Protocol]]

## Sources
- [[sources/hsol-ai-portfolio-6|AI Portfolio Making (6): A Data Model for a Person]]
- [[sources/pxd-color-token-design-2026|pxd: Color Token Design Patterns]]
- [[sources/christinevallaure-hypertokens|Vallaure (2026): Hypertokens]]
- [[sources/christinevallaure-a2ui-generative-ui|Vallaure (2026): A2UI Under the Hood]]
