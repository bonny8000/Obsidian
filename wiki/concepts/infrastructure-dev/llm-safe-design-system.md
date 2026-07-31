---
type: concept
status: active
created: 2026-07-28
updated: 2026-07-31
tags: [concept, design-system, llm-safe, design-tokens, ci-enforcement, lint-rules, stylex, constraint-by-construction, intermediate-representation, scorers]
sources: [polar-orbit-llm-safe-design-system, karrot-kraft-design-system-agent]
confidence: 0.79
---

# LLM-Safe Design System

> [!abstract] Summary
> A design system that makes off-system decisions **uncompilable** rather than discouraged. Tokens are typed and named for *intent* (`background-card`, not `bg-gray-100`), untyped styling surfaces are removed from the available syntax, theme resolution lives inside the token, and CI is treated as a contract rather than a suggestion. The generating model is left completely free — the constraint is on what can pass the gate.

> [!important] Why it Matters
> Documentation is the wrong enforcement layer for a generator that does not retain context across outputs. An LLM handed open-ended utilities will produce `p-4` here and `p-5` there, pick arbitrarily among available grays, and omit dark-mode variants — not from misunderstanding, but because the training data's paths of least resistance are still available. Closing those paths converts consistency from a team discipline into a language feature. The reported effect is on **review attention**: it moves from policing style drift to discussing behavior and layout.

## The formulation worth remembering

> "The LLM is free to write anything it wants. We just make sure the only things that pass CI are things we'd be happy to ship."

This is the cleanest statement in this wiki of a general principle: **constrain the acceptance criteria, not the generator.** It appears independently in [[wiki/sources/socar-self-healing-agents|SOCAR's]] schema-enforced outputs and [[wiki/sources/naver-d2-ai-hackathon-nstake|NStake's]] authorization boundaries.

## A second independent instance, at a different layer

[[wiki/sources/karrot-kraft-design-system-agent|Karrot's Kraft]] reached the same principle from screen generation rather than from styling, and implemented it **one layer up** — in a spec schema rather than in the type system. Kraft's `DesignSpec` has a `designTokens` field that accepts only SEED semantic token names (`bg.layerDefault`) and *cannot represent* a raw hex value. The author's claim is that this alone guarantees brand-correct color. Same move, different altitude: Polar makes the wrong value uncompilable, Karrot makes it unrepresentable in the plan.

Karrot then extends the principle in two directions Polar does not:

- **Machine-scored, not just gated.** Eleven [[wiki/concepts/ai-agents/generated-output-scoring|scorers]] — seven deterministic static checks, four LLM-based judgment checks — score each generated screen so the machine filters before a human reviews. CI answers pass/fail; scoring answers *how far off, and where*.
- **Cumulative, not just enforced.** Design decisions accumulate across sessions and repeated patterns are auto-promoted into per-domain principles, so the constraint set grows from use rather than only from authorship. See [[wiki/concepts/ai-agents/agent-memory|agent memory]].

The convergence is real and worth weighting — two teams, two countries, two problem framings, same conclusion. The shared limitation is equally real: **neither reports an outcome measurement.**

## 📝 Key Claims

- **Name tokens for the decision, not the value.** `background-card` is a design decision; `bg-gray-100` is a value. Spacing tokens are roles on a scale (`xs`…`xl`), not pixel counts. The vocabulary itself carries the system: an agent choosing from it cannot pick the wrong gray, because grays are not in it. *"A design system is not a pile of values. It's a set of decisions."*
- **Strings are the vulnerability.** Arbitrary `className` values are hard to lint and are exactly what training data favors. The fix is removal from the syntax, not a rule against them.
- **Typed props derived from token definitions** make arbitrary values unrepresentable rather than merely non-compliant.
- **Ban the untyped surface, restore what it provided.** Prohibiting raw `<div>` / `<section>` / `<nav>` would cost DOM semantics, so a polymorphic `as` prop returns them: `<Box as="nav">`.
- **Theme correctness by token, not by variant.** CSS `light-dark()` inside the token definition removes the entire class of bug where a component is right in light mode and broken in dark.
- **CI as contract:** "If a PR is green, it is safe to merge." Compliance is enforced at the gate, not by reviewers who tire.
- **Every escape hatch voids the guarantee.** A lint-disable is treated as a **design-system deficiency** — the token set is missing something — rather than as a legitimate exception.
- **The claimed benefit is relocated review attention**, not faster generation or fewer bugs.

## The four mechanisms

| Mechanism | What it forecloses |
|---|---|
| Typed props derived from token definitions | Arbitrary values become unrepresentable |
| Lint rule banning raw layout elements | Untyped styling surfaces (`<div className="…">`) |
| Theme resolution inside the token (`light-dark()`) | Forgotten dark-mode variants |
| Lint rules as CI contract | Style drift surviving to `main` via review fatigue |

## ⚖️ Conflicts & Caveats

> [!warning] No measurement
> The reported benefit is a qualitative observation by the team that built the system. No before/after comparison, no LLM-output evaluation, no error-rate data. Nothing in this wiki establishes that constrained-vocabulary generation *improves output quality* rather than merely **making failures visible earlier** — which would still be valuable, but is a different claim.

> [!warning] Closed vocabularies have a cost and an unknown ceiling
> The anchor source's team adds tokens **weekly** and is explicitly watching for the point where constraint turns counterproductive. That threshold is unknown. Too small a token set blocks legitimate work; too large a one reintroduces arbitrary choice through autocomplete noise.

> [!warning] Tension with documentation-as-context approaches
> The premise directly undercuts the sufficiency of [[wiki/concepts/infrastructure-dev/design-md|DESIGN.md]] and context-file strategies: a context file *tells* the model what to do, a type error *stops* it. This concept treats context files as necessary but not sufficient. That is a real disagreement with how [[wiki/concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]] frames the problem — legibility versus foreclosure — and it is not resolved by any source here.

> [!warning] Implementation is not framework-neutral
> The pattern (typed tokens + banned raw elements + theme-in-token + CI gate) is portable. The anchor implementation depends on StyleX and an incomplete migration from Tailwind, so it has never been tested as the only styling path in a codebase.

> [!warning] Forecloses legitimate exceptions too
> A system that makes arbitrary values impossible also blocks the one-off a designer genuinely wants. The source acknowledges this only as "sometimes too restrictive," and offers no process for a sanctioned exception.

## 🔗 Related Concepts

- [[wiki/concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]] — the parent frame. That concept asks whether AI *can understand and build with* the system; this one asks whether the system can make wrong output *fail*. Legibility is necessary; foreclosure is what holds.
- [[wiki/concepts/infrastructure-dev/deterministic-ai-workflows|Deterministic AI Workflows]] — the same move at workflow level: stable facts and repeatable checks leave the model and enter contracts.
- [[wiki/concepts/infrastructure-dev/color-token-architecture|Color Token Architecture]] — semantic token naming, of which intent-naming is the strict form.
- [[wiki/concepts/infrastructure-dev/hypertokens|Hypertokens]] — bundled decisions as an agent-facing primitive; the same instinct one tier up.
- [[wiki/concepts/infrastructure-dev/component-catalog|Component Catalog]] — the agent-facing palette; a typed token set is the same idea one layer down.
- [[wiki/concepts/infrastructure-dev/design-review-automation|Design Review Automation]] — what the CI gate replaces.
- [[wiki/concepts/infrastructure-dev/design-system-implementation|Design System Implementation]]
- [[wiki/concepts/ai-agents/permission-boundary-guardrails|Permission-Boundary Guardrails]] — the same structural-over-instructed logic applied to agent authorization.
- [[wiki/concepts/ai-agents/design-spec-intermediate-representation|Design Spec as Intermediate Representation]] — the same foreclosure enforced in a spec schema instead of a type system.
- [[wiki/concepts/ai-agents/generated-output-scoring|Generated-Output Scoring]] — what Kraft adds beyond a binary CI gate.
- [[wiki/comparisons/where-to-put-the-constraint|Where to Put the Constraint]] — the decision table across all four available layers.
- [[wiki/concepts/infrastructure-dev/agent-defense-in-depth|Agent Defense in Depth]]

## 📚 Sources

- [[wiki/sources/polar-orbit-llm-safe-design-system|Polar (2026): Building an LLM-Safe Design System (Orbit)]] — primary source: the four mechanisms, code examples, token conventions, and the CI-as-contract framing.
- [[wiki/sources/naver-d2-ai-hackathon-nstake|NAVER D2 (2026): What the Winning AI Hackathon Team Did *Not* Delegate to AI]] — independent convergence on structural-over-instructed constraint from a different domain.
- [[wiki/sources/socar-self-healing-agents|SOCAR (2026): AI Agents That Self-Repair Failures]] — schema-enforced output as the production-grade instance of the same principle.
- [[wiki/sources/karrot-kraft-design-system-agent|Karrot (2026): Kraft]] — second independent instance, enforced in a spec schema and extended with scoring and cross-session memory.

## ❓ Open Questions

- Does constrained-vocabulary generation measurably improve LLM output, or only surface failures earlier? Nobody has measured it.
- At what token count does a closed set stop being safer than an open one?
- What is the correct process for a legitimate exception — token addition, scoped disable, or an explicit escape component?
- How much of this transfers outside styling, to API surfaces, data schemas, or configuration?
- Does the review-attention benefit persist, or do reviewers find new low-value things to police?
