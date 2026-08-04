---
type: concept
status: active
created: 2026-05-18
updated: 2026-08-04
tags: [design-system, implementation, engineering]
sources:
  - sources/bucketplace-pretendard-jp-2026-04-17
  - sources/brunch-ghidesigner-482
  - sources/pxd-color-token-design-2026
  - sources/christinevallaure-agentic-ai-design-systems
  - sources/christinevallaure-a2ui-generative-ui
  - sources/boongranii-cursor-pointer-debate
confidence: 0.78
---

# Design System Implementation

## Summary

Design system implementation is the engineering work that makes design tokens, typography, components, assets, and platform behavior match the intended product design across real devices and locales.

## Why It Matters

Design systems fail when the implementation only matches the design in the default case. Multilingual typography shows how a design-system rule can be technically "applied" but visually wrong because glyph fallback changes the rendered result.

## Key Claims

- Design-system implementation must verify rendered output, not only code-level configuration.
- Typography tokens need platform and language-specific validation.
- AI design-to-code workflows should respect design-system implementation constraints.
- Color-token structure affects long-term maintainability: scale tokens are fast but context-light, semantic tokens encode role and state, and hybrid structures balance flexibility with operational consistency.
- **Implementation completeness becomes the quality ceiling for generated UI.** When an agent assembles screens from a [[concepts/infrastructure-dev/component-catalog|catalog]], "the quality of every screen a user ever sees is set by what a designer put in it" — missing states, weak tokens, or off-spec names cap the result ([[sources/christinevallaure-a2ui-generative-ui|Vallaure, 2026]]).
- **The full state matrix must exist or the agent under-builds.** Hover/focus/active/disabled/error/empty/loading/skeleton states need to be present (via variants, booleans, instance swap), or generated UI silently omits them — "if your Star component only has a default story, the agent thinks that is the only state it has" ([[sources/christinevallaure-agentic-ai-design-systems|Vallaure, 2026]]).

## Related Concepts

- [[concepts/infrastructure-dev/multilingual-app-typography|Multilingual App Typography]]
- [[concepts/infrastructure-dev/localization-ux|Localization UX]]
- [[concepts/infrastructure-dev/color-token-architecture|Color Token Architecture]]
- [[concepts/ai-agents/vibe-design|Vibe Design]]
- [[concepts/infrastructure-dev/design-automation|Design Automation]]
- [[concepts/infrastructure-dev/component-catalog|Component Catalog]] · [[concepts/infrastructure-dev/figma-code-connect|Figma Code Connect]]

## Sources

- [[sources/bucketplace-pretendard-jp-2026-04-17|Bucketplace: Pretendard JP in Multi-Country Android App]]
- [[sources/brunch-ghidesigner-482|Vibe Design and Coding with Claude Design and Claude Code]]
- [[sources/pxd-color-token-design-2026|pxd: Color Token Design Patterns]]
- [[sources/christinevallaure-agentic-ai-design-systems|Vallaure (2026): Agentic AI, Design Systems & Figma]]
- [[sources/christinevallaure-a2ui-generative-ui|Vallaure (2026): A2UI Under the Hood]]

## Open Questions

- [Answered → [[queries/2026-05-27-design-system-typography-regression-qa|Query Page]]] How should design-system QA catch script-specific typography regressions?
- **Which of this system's defaults are undocumented, and who would notice if one changed?**

## Defaults Are Decisions Inherited by People Who Never See Them

> [!important] Added 2026-08-04 — a small case with a general lesson
> Tailwind CSS v4 changed one preflight default: `cursor: pointer` → `cursor: default` on buttons, to align with native OS behaviour and the W3C spec. Downstream, shadcn/ui users filed the same complaint repeatedly — issues **#7501, #7223, #6843, #7279** — that they *"can't tell it's clickable because the cursor doesn't change"* ([[wiki/sources/boongranii-cursor-pointer-debate|Boongranii, 2026]]).
>
> **The lesson is not about cursors.** A design-system default is a decision made once, by someone with context, and then inherited by many people who never see the decision or its reasoning. When it changes, the consequence propagates silently to every consumer, and the rationale is not where the consequence lands.
>
> **Two practices this argues for:**
>
> 1. **Document defaults with rationale, not just values.** The value tells a consumer what happens; the rationale tells them whether their situation is the one the default was chosen for. In this case the default was chosen for specification conformance, and the affected consumers had weak-affordance UI where conformance was the wrong criterion.
> 2. **Treat a preflight/base-layer change as a breaking change.** It is not scoped to a component and it cannot be opted out of per call site.
>
> The underlying disagreement — a formal specification versus a twenty-year learned user convention — has no resolution from either authority. The design-system obligation is to **pick one and record which, and why**. See [[wiki/concepts/ux-research/perceived-affordance|Perceived Affordance]].
>
> Carry the accessibility correction too: `cursor: pointer` reaches pointer users only, and the affordance problem it patches (a card whose interactivity is unannounced) is *worse* for touch and keyboard users. Fix the affordance and set the cursor.

## Additional Sources

- [[wiki/sources/boongranii-cursor-pointer-debate|Boongranii (2026): Should Clickable Elements Use cursor: pointer?]] — the Tailwind v4 default change and its downstream consequences.

