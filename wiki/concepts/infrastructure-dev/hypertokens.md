---
type: concept
status: active
created: 2026-06-29
updated: 2026-06-29
tags: [design-tokens, hypertokens, design-systems, composite-tokens, dtcg, design-to-code, agent-readable, token-efficiency]
sources:
  - sources/christinevallaure-hypertokens
confidence: 0.7
---

# Hypertokens

## Summary

A hypertoken is a named bundle of style properties — defined once, upstream of every design tool — that compiles automatically into each platform's copy (CSS class, Figma text style, Swift struct, etc.). It occupies a new tier in the design-system hierarchy: **Raw values → Tokens (single decisions) → Hypertokens (bundled decisions) → Components (structure, behavior, accessibility)**. Hypertokens carry only style bundles (typography, surfaces, spacing, motion); behavioral logic, structure, and accessibility stay in the component layer. The term was coined by Jake Albaugh (Figma) at Config 2026 and written up by Christine Vallaure; as of June 2026 it is a forward-looking abstraction, not a shipped primitive.

## Why It Matters

Design decisions naturally travel in groups (a typography style is font-family + size + weight + line-height + letter-spacing *together*), yet today each bundle exists as separate hand-copied versions per tool that drift out of sync. Hypertokens name and source-of-truth those bundles so the drift disappears. The sharper argument is the agent era: an agent "builds exactly what it finds and guesses the rest," so handing it `Surface.brand` instead of fifteen raw values means less reconstruction, less code, and lower token usage. This makes hypertokens a candidate infrastructure layer for [[concepts/infrastructure-dev/ai-native-design-system|AI-native design systems]].

## Key Claims

- A hypertoken is "a named bundle of style properties, defined once, that every tool's copy is built from" — one upstream source compiling to many platform outputs ([[sources/christinevallaure-hypertokens|Vallaure, 2026]]).
- It sits between tokens and components and holds bundled *style* decisions only, not behavior or structure.
- It generalizes the W3C/DTCG composite-token types (typography, shadow, border, gradient, transition, strokeStyle) from a fixed predefined list to "any recurring fragment your own system has" — open-ended, user-defined composites.
- Semantic names like `Surface.brand` are a token-efficiency play: less for an agent to reverse-engineer than raw hex/px values.
- Jake Albaugh's Config 2026 JSON pipeline compiled one source into aliased variables, component/icon libraries, Code Connect docs, base CSS, and Svelte components, reportedly yielding "less total code and lower AI usage for a better outcome."

## Related Concepts

- [[concepts/infrastructure-dev/color-token-architecture|Color Token Architecture]] — hypertokens add a bundled-decision tier above semantic tokens.
- [[concepts/infrastructure-dev/component-catalog|Component Catalog]] — the agent-facing menu hypertokens help populate cleanly.
- [[concepts/infrastructure-dev/design-to-code-workflow|Design-to-Code Workflow]] — one source compiling to many targets reduces reconstruction.
- [[concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]] — hypertokens are a proposed AI-native design-system primitive.
- [[concepts/infrastructure-dev/token-efficiency|Token Efficiency]] — semantic bundles reduce agent processing.
- [[concepts/infrastructure-dev/deterministic-ui|Deterministic UI]] — single source of truth compiling to reproducible output.
- [[concepts/infrastructure-dev/figma-code-connect|Figma Code Connect]] — a downstream target the pipeline emits.
- [[concepts/infrastructure-dev/design-md|design.md]] · [[concepts/infrastructure-dev/scaffold-design-system|Scaffold Design System]]

## Conflicts & Caveats

> [!warning] Forward-looking, single-demo
> Hypertokens are an exploration, not a shipped feature — there is no hypertoken primitive in Figma or any tool as of June 2026. The "less code / lower AI usage" outcome is a one-demo anecdote, not a measured benchmark. The concept may be absorbed into the W3C DTCG composite-token spec, and open-ended user-defined composites work against the fixed predefined types that make composites portable across tools.

## Sources

- [[sources/christinevallaure-hypertokens|Christine Vallaure (2026): Hypertokens — the bundled-decision layer between tokens and components]]

## Open Questions

- Does grouping tokens measurably improve agent output quality / reduce tokens at scale, or only in Albaugh's demo?
- Will W3C DTCG extend composite tokens toward open-ended bundles, making "hypertoken" a vocabulary rather than a new mechanism?
- Where exactly is the boundary between a hypertoken (style bundle, no logic) and a component (structure + behavior + a11y)?
