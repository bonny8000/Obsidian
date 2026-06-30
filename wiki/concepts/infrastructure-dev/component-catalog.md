---
type: concept
status: active
created: 2026-06-29
updated: 2026-06-29
tags: [component-catalog, design-systems, generative-ui, a2ui, agent-readable, design-to-code, machine-contract]
sources:
  - sources/christinevallaure-a2ui-generative-ui
confidence: 0.78
---

# Component Catalog

## Summary

A component catalog is the machine-readable *subset* of a design system that an AI agent is allowed to build from — the authorized menu of components, properties, and slots an agent may name when it assembles a screen. It is the middle layer in Vallaure's three-layer model for generative UI: "the system you think in" (the full design system), "the contract you expose" (the catalog), "the code that runs" (the runtime). A catalog can hold more than primitives like Button/Text — it can expose complex branded components (HotelSelector, FlightCard) and complete pre-built experiences.

## Why It Matters

In [[concepts/agent-experience/a2ui-protocol|A2UI]]-style generative UI, the catalog is the agent's *only* palette and its security boundary: "the model can only name components that exist in the catalog," which blocks invented widgets and made-up props. That makes the catalog the quality ceiling for every generated screen — "the quality of every screen a user ever sees is set by what a designer put in it." It reframes previously-invisible craft (states, semantic tokens, contractual naming, accessibility) as the load-bearing input, and turns *coverage* (which requests have no right component?) into a first-class design activity, because the dominant failure mode is the quiet downgrade.

## Key Claims

- The catalog is the machine-readable subset of a design system exposed to an agent — distinct from the full human design system and from the runtime code ([[sources/christinevallaure-a2ui-generative-ui|Vallaure, 2026]]).
- Validation against the catalog is the security boundary: the agent can only name catalog components, before and after generation.
- The main failure mode is the **quiet downgrade**: when the catalog lacks the right piece, the agent substitutes the closest (often wrong) component, falls back to generic baselines, or drops to chat — and the validator catches technical, not design, errors.
- Catalogs today live as hand-authored code "just past Figma's edge," because Figma cleanly expresses only ~1/3 of CSS — so a human stays "in the seam, on purpose."
- Catalog quality (explicit states, semantic tokens, contractual names, props/slots) is the quality ceiling for every generated screen.

## Related Concepts

- [[concepts/agent-experience/a2ui-protocol|A2UI Protocol]] — the protocol that consumes a catalog to render screens.
- [[concepts/ux-research/generative-ui|Generative UI]] — the catalog is what constrains generative UI to stay on-brand.
- [[concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]] — the catalog is the agent-facing contract of an AI-native design system.
- [[concepts/infrastructure-dev/design-system-implementation|Design System Implementation]] — implementation quality becomes the catalog's quality.
- [[concepts/infrastructure-dev/hypertokens|Hypertokens]] — bundled tokens feed clean catalog components.
- [[concepts/infrastructure-dev/design-to-code-workflow|Design-to-Code Workflow]] · [[concepts/infrastructure-dev/color-token-architecture|Color Token Architecture]]
- [[concepts/ux-research/designing-for-agency|Designing for Agency]] — catalog gaps shape graceful degradation and user agency.

## Conflicts & Caveats

> [!warning] Single-author framing, no evidence
> The catalog model comes from a single educational explainer (A2UI at v0.9), not a spec or study. There is no evidence that constrained-catalog generative UI ships better UX than static design or chat. The "~1/3 of CSS" coverage figure and the failure-mode taxonomy are the author's framing, not measured results. Catalog ownership (design vs engineering vs a shared design-systems function) and coverage governance are unresolved.

## Sources

- [[sources/christinevallaure-a2ui-generative-ui|Christine Vallaure (2026): A2UI Under the Hood — Designing for Radically Adaptive UI]]

## Open Questions

- How is catalog coverage governed and tested so quiet downgrades are caught before users see them?
- Who owns the catalog and its validation rules in practice?
- What tooling lets a designer "think on a canvas" and emit clean catalog code?
