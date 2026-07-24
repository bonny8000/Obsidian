---
type: concept
status: active
created: 2026-07-24
updated: 2026-07-24
tags: [concept, spec-driven-development, change-brief, documentation-debt, context-engineering, agentic-engineering]
sources: [spec-driven-development-exit-strategy]
confidence: 0.78
---

# Change Brief

> [!abstract] Summary
> A **temporary, delta-scoped** replacement for the standing specification. A change brief states outcome, non-goals, constraints and acceptance evidence for one specific change — and then **expires at release**. Anything that must outlive the change migrates into a native engineering artifact instead.

> [!important] Why it Matters
> Accumulated Markdown specs become "a second codebase with weaker tooling" — no compiler, no tests, no refactoring — that drifts from the running system while consuming the context budget the agent needs for the code itself. The brief is designed to be *thrown away*, which is precisely what stops the drift.

## 📝 Key Claims

- **A spec earns its cost only by helping decide and review a delta.** Outside that job, it is overhead.
- **Code is the primary fact.** "Code is actual behavior," becoming an observed contract through production use. Agents should read code rather than prose summaries of code.
- **Durable facts belong in artifacts with tooling behind them:**

| Fact type | Native home |
|---|---|
| API shapes | OpenAPI / schemas |
| Data invariants | Types, database constraints |
| Security rules | Access policies, static analysis |
| Architecture boundaries | Module structure, dependency rules |
| Reliability requirements | Load tests, telemetry |

- **Context is a budget.** Plans reaching 1,000+ lines competed with actual code review for attention — human and model alike.
- **Scale process to consequence.** "Consistency can spend attention on low-risk work while hiding the judgment needed for hard parts."
- **Brief ≠ vague.** Small briefs still demand real evidence and targeted clarification.

## 🧭 The Exit Test

> At release, ask of every line in the brief: *does this belong in a schema, a test, a policy, or a decision record?* If yes, move it there. If no, delete it. What survives that question is rationale — keep it short, owned, and adjacent to what it explains.

## ⚖️ Conflicts & Caveats

> [!warning] Directly contradicts Spec-Driven Development as held in this wiki
> [[wiki/concepts/ai-agents/spec-driven-development|SDD]] records "code is disposable" with the spec as Architectural North Star. This concept inverts both. **Recorded, not merged.** The likely reconciliation is scope: SDD describes *greenfield generate-from-spec*; the change brief describes *evolving an existing production system*. The live disagreement is about which case is typical.

> [!note] Evidence
> Largely unmeasured. The one hard number cited — models reaching 26.6% syntactic and 8.6% semantic correctness on requirements→TLA+ translation — argues against heavy formalization specifically, not against specifications in general.

## 🔗 Related Concepts

- [[wiki/concepts/ai-agents/spec-driven-development|Spec-Driven Development]] — the position this challenges
- [[wiki/concepts/ai-agents/progressive-disclosure|Progressive Disclosure]] — the companion context tactic
- [[wiki/concepts/ai-agents/context-engineering|Context Engineering]]
- [[wiki/concepts/ai-agents/interview-first-elicitation|Interview-First Elicitation]]

## 📚 Sources

- [[wiki/sources/spec-driven-development-exit-strategy|Eisele (2026): Spec-Driven Development Needs an Exit Strategy]]

## ❓ Open Questions

- Where exactly is the line between a brief that expires and rationale that persists?
- Does "read the code, not the plan" hold when the codebase exceeds any usable context window?
- Who owns deleting expired briefs — and what happens when nobody does?
