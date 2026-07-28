---
type: source
status: active
created: 2026-07-28
updated: 2026-07-28
tags: [design-system, ai-native-design-system, llm-safe, design-tokens, stylex, lint-rules, ci-enforcement, dark-mode, agentic-engineering]
source_path: raw/web/polar-orbit-llm-safe-design-system-2026-07-28.md
source_url: https://polar.sh/blog/orbit-llm-safe-design-system
authors: []
sources: []
ingest_level: deep
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.78
---

# Polar (2026): Building an LLM-Safe Design System (Orbit)

## Citation

*Building an LLM safe design system*, **Polar** engineering blog, 2026-06-16. Author not named on the page.

**Source type:** First-party engineering post describing an in-progress internal system, with code examples and no quantitative results.
**Raw capture:** [[raw/web/polar-orbit-llm-safe-design-system-2026-07-28|polar-orbit-llm-safe-design-system-2026-07-28]]

## Summary

The clearest small-scale statement of **constraint-by-construction** applied to design systems. The premise: documentation fails when an LLM generates code without sustained context awareness, so a design system must make off-brand decisions *uncompilable* rather than discouraged. Polar's **Orbit** replaces Tailwind with StyleX and exposes a single polymorphic `<Box />` that accepts only typed design tokens. Raw `<div>` / `<section>` / `<nav>` are banned by an ESLint rule; dark mode is baked into each color token via CSS `light-dark()`; CI is treated as a contract.

The load-bearing sentence: **"The LLM is free to write anything it wants. We just make sure the only things that pass CI are things we'd be happy to ship."**

## Key Claims

- **Documentation is the wrong enforcement layer for LLMs.** Conventions in prose are not retained across generation; the constraint has to live in the type system and the gate.
- **Tokens should name the decision, not the value.** `background-card`, not `bg-gray-100`; spacing as roles on a scale (`xs`…`xl`), not pixel counts. **"A design system is not a pile of values. It's a set of decisions."**
- **Strings are the vulnerability.** The post notes that "strings are complex to write lint-rules for" — arbitrary `className` values are exactly the path of least resistance LLM training data favors, so they are removed from the syntax.
- **Escape hatches void the guarantee.** Every ESLint disable is treated as a crack, and as a deficiency in the design system rather than a legitimate exception.
- **Ban the untyped surface, keep the semantics.** Prohibiting raw layout elements would cost DOM semantics, so `<Box as="nav">` restores them polymorphically.
- **Theme correctness by token, not by variant.** `light-dark()` inside the token definition removes the class of bug where a component is right in light mode and broken in dark.
- **CI as contract:** "If a PR is green, it is safe to merge." Compliance is enforced at the gate, not in human review.
- **The reported effect is on review, not on output volume:** reviews shifted from policing style drift to discussing behavior and layout, because "more of that is now correct by construction."

## Useful Examples

The full component-usage shape, which is the artifact worth copying:

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

Token definitions typed at the source, with theme resolution inside the value:

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

**The four mechanisms, as a checklist:**

| Mechanism | What it forecloses |
|---|---|
| Typed props derived from token definitions | Arbitrary values are unrepresentable |
| `polar/no-raw-html-layout` ESLint rule | Untyped styling surfaces (`<div className="…">`) |
| `light-dark()` inside the token | Forgotten dark-mode variants |
| ESLint rules as CI contract | Style drift surviving to `main` via review fatigue |

**The failure modes it was built against** — the concrete LLM output problems named: `p-4` in one place and `p-5` in another; arbitrary choice among `bg-gray-100` / `bg-zinc-100`; omitted dark-mode variants.

## Constraints / Caveats

- **No measurement of any kind.** The reported benefit ("reviews discuss behavior instead of grays") is a qualitative observation by the team that built it. No before/after, no error-rate comparison, no LLM-output evaluation.
- **Explicitly early-stage**, with acknowledged uncertainty about which decisions will prove correct.
- **The closed token set is sometimes too restrictive**; the team adds tokens weekly and is watching for the point where constraint turns counterproductive. That threshold is unknown.
- **Migration is incomplete** — much of the codebase is still Tailwind, so the system has not been tested as the only styling path.
- **No named author**, which slightly weakens attributability.
- **Small-company scale.** Polar is a small product org; the maintenance economics of a hand-curated closed token set at large scale are untested here.
- **StyleX is a hard dependency.** The pattern (typed tokens + banned raw elements + CI gate) is portable, but this implementation is not framework-neutral.

## Design Implications

- **Move design-system conformance from documentation into types and CI.** If an agent can express an off-system value, it eventually will.
- **Name tokens for intent** so the vocabulary itself encodes the decision. An agent choosing `background-card` cannot pick the wrong gray, because grays are not in the vocabulary.
- **Delete the untyped escape route rather than documenting against it** — but replace what it provided (here, DOM semantics via `as`).
- **Put theme resolution in the token**, so no generated component can be theme-incomplete.
- **Treat every lint-disable as a design-system bug report.** The exception is signal that the token set is missing something, not that the rule is wrong.
- **Expect the constraint set to need active curation.** Weekly token additions are the running cost of this approach.
- **The reviewable surface is the real deliverable.** The measurable benefit claimed is not faster generation but review attention relocated from style to behavior.

## Tensions

- **Sharpens [[wiki/concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]] from a legibility argument into a constraint argument.** Atlassian's four pillars ask whether AI *can understand and build with* the system. Polar asks whether the system can make wrong output *fail*. These are complementary but differently ambitious: legibility is necessary, foreclosure is what actually holds.
- **Against [[wiki/concepts/infrastructure-dev/design-md|DESIGN.md]] / context-file approaches:** the whole premise is that documentation-as-context does not survive generation. A DESIGN.md tells the model what to do; a type error stops it. This source would treat a context file as necessary-but-insufficient.
- **Converges with [[wiki/sources/naver-d2-ai-hackathon-nstake|NStake]] and [[wiki/sources/socar-self-healing-agents|SOCAR]] from a completely different domain.** Three independent teams — design systems, internal finance tooling, production browser automation — all conclude that safeguards must be structural rather than instructed. That convergence is the strongest signal in the 2026-07-28 cluster.
- **Cost tension.** Closed vocabularies buy consistency and charge maintenance. Polar pays weekly; SOCAR pays baseline-schema upkeep; NStake pays rule authoring. Every constraint architecture in this cluster has the same bill.
- **Against creative latitude.** A system that forecloses arbitrary values also forecloses the one-off exception a designer legitimately wants. The source acknowledges this only as "sometimes too restrictive."

## Open Questions

- Does constrained-vocabulary generation measurably improve LLM output quality, or does it only make failures visible earlier? No source in this wiki measures it.
- Where is the token-count threshold at which a closed set stops being safer than an open one (autocomplete noise, wrong-token selection)?
- What is the right *process* for a legitimate exception — token addition, scoped disable, or component escape?
- How does this interact with generative-UI approaches ([[wiki/concepts/agent-experience/a2ui-protocol|A2UI]]) where the catalog is the palette? Is a typed token set the same idea one layer down?

## Concepts Linked from This Source

- [[wiki/concepts/infrastructure-dev/llm-safe-design-system|LLM-Safe Design System]]
- [[wiki/concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]]
- [[wiki/concepts/infrastructure-dev/deterministic-ai-workflows|Deterministic AI Workflows]]
- [[wiki/concepts/infrastructure-dev/color-token-architecture|Color Token Architecture]]
- [[wiki/concepts/infrastructure-dev/design-system-implementation|Design System Implementation]]
- [[wiki/concepts/infrastructure-dev/component-catalog|Component Catalog]]
- [[wiki/concepts/infrastructure-dev/hypertokens|Hypertokens]]
- [[wiki/concepts/infrastructure-dev/design-review-automation|Design Review Automation]]

## LLM Use

Cite for **constraint-by-construction in the front-end layer**: intent-named tokens, banning untyped surfaces, theme-in-token, CI-as-contract. It is the most concrete, most copyable implementation of the pattern in this wiki, and the code examples can be lifted directly as a design brief.

Do not cite it as evidence that the approach *works* — it has no measurement. Use it for the mechanism and pair it with the production sources in the same cluster for the argument.

## Reliability Notes

- **First-party, specific, and honest about incompleteness** (legacy Tailwind, weekly token additions, "early stage"), which is more credible than a polished retrospective would be.
- **Confidence 0.78:** the mechanism is verifiable from the code shown and the reasoning is sound; the benefit claim is unmeasured and self-reported, and there is no named author.
- No vendor incentive detected — Polar sells payments infrastructure, not design tooling.
- Ingested from an AI-generated extraction; the quoted phrases should be re-verified against the original before external citation.
