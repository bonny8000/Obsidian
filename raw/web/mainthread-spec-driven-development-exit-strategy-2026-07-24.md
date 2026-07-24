---
source_url: https://www.the-main-thread.com/p/spec-driven-development-exit-strategy
captured: 2026-07-24
title: "Spec-Driven Development Needs an Exit Strategy"
authors: [Markus Eisele]
published: 2026-07-15
publisher: The Main Thread (Substack)
---

# Spec-Driven Development Needs an Exit Strategy — Markus Eisele

**Published:** 2026-07-15 · **Captured:** 2026-07-24
**Capture note:** AI-written summary from the public article. Full text not reproduced.

## Summary

A direct critique of how spec-driven development is practiced with AI agents. Eisele's argument: accumulating Markdown specifications produces **"a second codebase with weaker tooling"** that steadily diverges from the running system. Specifications should be **temporary artifacts** that guide a single decision and then expire; anything durable belongs in native engineering forms — code, schemas, tests, policies, telemetry.

## Key Points

- **Specs are temporary.** "A change specification earns its cost when it helps a team decide and review that delta." Most planning detail should expire at release.
- **Code is the primary fact.** "Code is actual behavior," and becomes an observed contract through extended production use. Agents should read the code, not natural-language summaries of it.
- **Context is a limited budget.** Every requirement and design note consumes working context; plans reaching 1,000+ lines competed with actual code review. **Progressive disclosure** — small maps, stable rules, pointers to deeper material — serves agents better than comprehensive documentation.
- **Durable facts go in native artifacts:**

| Fact type | Where it belongs |
|---|---|
| API shapes | OpenAPI / schemas |
| Data invariants | Types and database constraints |
| Security rules | Access policies, static analysis |
| Architecture boundaries | Module structure, dependency rules |
| Reliability requirements | Load tests, telemetry |

- **Judgment over process prescription.** "Consistency can spend attention on low-risk work while hiding the judgment needed for hard parts." Process weight should scale with risk.

### Named concepts

- **Change Brief** — the proposed replacement for "specification": states outcome, non-goals, constraints and acceptance evidence for the *delta* between current and desired state.
- **Progressive disclosure** — small maps and stable rules with pointers, rather than exhaustive docs.
- **Delta-focused approach** — describe what should change, not the whole system.

### Concrete examples

- **Modernization:** legacy systems mix durable business policy, published interfaces, obsolete workarounds, undocumented fixes and real defects. Agents must *classify* observed behavior — preserve / verify / redesign / remove — rather than faithfully translating every layer.
- **Research-Plan-Implement:** the original workflow front-loaded human review, producing long plans that engineers treated as compiler output rather than reviewing. The revision uses smaller contexts per phase: factual research, design, structure, implementation, review.

## Stated Caveats

- Formal specification remains hard: a 2026 evaluation found models reached only **26.6% syntactic and 8.6% semantic correctness** translating requirements to TLA+.
- Independence and verification strength should scale with risk.
- Small briefs still require real evidence and targeted clarification.
- Natural-language ambiguity in code generation is unsolved.

## Practical Recommendations

1. Start from code and operational evidence when describing current systems.
2. Define the intended delta, boundaries and known unknowns in a brief.
3. Add research, prototypes and design alignment only where risk demands.
4. Review the implementation, not only the plan.
5. At release, preserve facts in native artifacts — schemas, tests, policies, configuration, telemetry, decision records.
6. Keep durable rationale short, owned, and adjacent to the artifact it explains.
7. Scale process complexity to consequence.
