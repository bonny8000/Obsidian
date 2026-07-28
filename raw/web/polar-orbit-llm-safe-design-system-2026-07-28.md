---
source_url: https://polar.sh/blog/orbit-llm-safe-design-system
captured: 2026-07-28
title: "Building an LLM safe design system"
authors: []
published: 2026-06-16
publisher: Polar
language: en
---

# Building an LLM-Safe Design System (Orbit) — Polar

**Published:** 2026-06-16 · **Captured:** 2026-07-28
**Capture note:** AI-written summary with short quoted phrases for attribution. Full text not reproduced. Author not named on the page.

## Summary

Polar's engineering post on **Orbit**, their design system built so that AI-generated code *cannot* be off-brand. The premise: documentation fails when LLMs generate code without sustained context awareness, so design decisions must become **mandatory vocabulary** rather than optional guidance. Wrong decisions are made **uncompilable**, and CI is the gate.

## The problem

LLMs produce syntactically valid but inconsistent styling. Handed Tailwind utilities they emit `p-4` in one place and `p-5` in another, pick arbitrarily among `bg-gray-100` / `bg-zinc-100`, and omit dark-mode variants. The post notes that **"strings are complex to write lint-rules for"** and that any escape hatch undermines the constraints built around it.

## Architecture

Orbit replaces Tailwind with **StyleX** (Meta's compile-time styling library) and exposes a single polymorphic **`<Box />`** component that accepts **only typed design tokens** as props.

### Token convention: intent, not value

Tokens are named for the decision, not the value — `background-card` rather than `bg-gray-100`. Spacing tokens are roles on a scale (`xs`, `s`, `m`, `l`, `xl`), not pixel counts. The post's framing: **"A design system is not a pile of values. It's a set of decisions."**

```jsx
<Box
  flexDirection="column"
  gap="l"
  padding="m"
  backgroundColor="background-card"
  borderRadius="m"
>
  <Text variant="heading-xs" color="text-primary">
    Card title
  </Text>
</Box>
```

Tokens are strictly typed at definition:

```javascript
export const spacing = stylex.defineVars({
  m: '12px',
  l: '16px',
  xl: '24px',
})

export const backgroundColors = stylex.defineVars({
  'background-card': 'light-dark(hsl(240, 2.90%, 72.50%), hsl(233, 4%, 9.5%))',
})
```

## Four constraint mechanisms

1. **Typed props.** `Box` prop types derive directly from token definitions, so arbitrary values are unrepresentable.
2. **Raw HTML layout elements banned.** Bare `<div>`, `<section>`, `<nav>` are prohibited by an ESLint rule (`polar/no-raw-html-layout`). Semantics are preserved through polymorphism: `<Box as="nav" alignItems="center" columnGap="m">…</Box>`. This keeps DOM semantics while removing untyped styling surfaces.
3. **Dark mode baked into the token.** Colors use CSS's native `light-dark()` function, so there are no separate dark variants to forget — preventing "a component that looks right in light mode and broken in dark mode."
4. **CI enforcement as contract.** ESLint rules are treated as contracts rather than suggestions: **"If a PR is green, it is safe to merge."** Design compliance is enforced at the gate, not in review.

## How this constrains LLM output

Rather than asking the model to remember conventions, the system makes wrong decisions fail to compile. An LLM writing Orbit code chooses from a predefined vocabulary; autocomplete surfaces valid tokens and typos become type errors. The post's formulation: **"The LLM is free to write anything it wants. We just make sure the only things that pass CI are things we'd be happy to ship."** Raw elements and arbitrary `className` strings are removed from the available syntax, closing the paths of least resistance that LLM training data would otherwise favor.

## Reported results

Qualitative and early: reviews shifted from policing style drift (wrong grays, forgotten dark mode, arbitrary values) toward discussing behavior and layout, because **"more of that is now correct by construction."** No quantitative measurement is given.

## Caveats and limitations

- **Token scope gaps.** The closed token sets are sometimes too restrictive; the team adds tokens weekly and watches whether constraints turn counterproductive.
- **Legacy code.** Much of the existing codebase is still Tailwind; migration is incremental.
- **Escape hatches.** Every ESLint disable is treated as a crack in the guarantee and as a design-system deficiency.
- **Early stage.** The system is under active development with acknowledged uncertainty about which decisions will prove right.
