---
type: concept
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [concept, mutation-testing, test-effectiveness, regression, coding-agents]
sources: [fowler-sensors-coding-agents]
confidence: 0.85
---

# Mutation Testing

> [!abstract] Summary
> Introducing small, deliberate code mutations and checking whether the test suite catches them — a way to find missing assertions that code-coverage metrics hide.

> [!important] Why it Matters
> As AI generates most tests with little review, coverage stops being a sufficient signal: a line can be executed (covered) without its behavior being verified. Mutation testing monitors exactly that gap, which matters when the test suite is the codebase's regression safety net.

## 📝 Key Claims
- "Survivors" (mutations the tests fail to catch) reveal weak or missing assertions even at 100% statement coverage.
- High coverage from broad end-to-end/acceptance tests can give a false sense of security; mutation testing exposes thin assertions.
- It is resource-intensive, so it is often run incrementally or on changed files rather than continuously.
- Pairs with tooling (e.g., Stryker) plus scripts that let an agent query results without clogging its context.

## 🔗 Related Concepts
- [[concepts/infrastructure-dev/maintainability-sensor|Maintainability Sensor]]
- [[concepts/ai-agents/product-evals|Product Evals]]
- [[concepts/ux-research/ai-evals|AI Evals]]

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> Mutation testing only checks *test effectiveness* (do tests catch breakage), not *test correctness* (do tests assert the right behavior) — a separate, harder problem.

## 📚 Sources
- [[sources/fowler-sensors-coding-agents|Böckeler (2026): Maintainability Sensors for Coding Agents]]

## ❓ Open Questions
- What cadence balances mutation-testing cost against drift detection?
- Can AI reliably triage mutation survivors into "matters" vs "noise"?
