---
type: source
status: active
created: 2026-07-24
updated: 2026-07-24
tags: [spec-driven-development, context-engineering, change-brief, progressive-disclosure, documentation-debt, agentic-engineering, ai-agent]
source_path: raw/web/mainthread-spec-driven-development-exit-strategy-2026-07-24.md
source_url: https://www.the-main-thread.com/p/spec-driven-development-exit-strategy
authors: [Markus Eisele]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.8
---

# Eisele (2026): Spec-Driven Development Needs an Exit Strategy

## Citation

Markus Eisele, *"Spec-Driven Development Needs an Exit Strategy,"* **The Main Thread** (Substack), 2026-07-15.

**Source type:** Practitioner argument, with one cited empirical result.
**Raw capture:** [[raw/web/mainthread-spec-driven-development-exit-strategy-2026-07-24|mainthread-spec-driven-development-exit-strategy-2026-07-24]]

## Summary

A structural critique of spec-driven development as practiced with agents. Accumulated Markdown specs become **"a second codebase with weaker tooling"** — no compiler, no tests, no refactoring tools — that drifts from the running system while consuming the context budget agents need for the code itself. The prescription is an *exit strategy*: specs are temporary decision aids that expire at release, and durable facts migrate into native engineering artifacts.

## Key Claims

- **Specs are temporary.** "A change specification earns its cost when it helps a team decide and review that delta." Planning detail should expire after release.
- **Code is the primary fact.** "Code is actual behavior," becoming an observed contract through production use. Agents should read code rather than natural-language summaries of code.
- **Context is a budget, not a container.** Plans reaching 1,000+ lines competed with actual code review for attention — both human and model.
- **Durable facts belong in native artifacts**, each with real tooling behind it:

| Fact type | Native home |
|---|---|
| API shapes | OpenAPI / schemas |
| Data invariants | Types, database constraints |
| Security rules | Access policies, static analysis |
| Architecture boundaries | Module structure, dependency rules |
| Reliability requirements | Load tests, telemetry |

- **Judgment over uniform process.** "Consistency can spend attention on low-risk work while hiding the judgment needed for hard parts."

## Useful Examples

- **Modernization:** legacy behavior is a mix of durable business policy, published interfaces, obsolete workarounds, undocumented fixes and genuine defects. The agent's job is to **classify** — preserve / verify / redesign / remove — not to faithfully translate every layer.
- **Research-Plan-Implement, revised:** the original front-loaded human review and produced plans so long that engineers treated them as compiler output and stopped reviewing them. The fix was smaller contexts per phase — factual research, design, structure, implementation, review.

## Constraints / Caveats

- **Formal specification remains hard:** a 2026 evaluation found models achieved only **26.6% syntactic and 8.6% semantic correctness** translating requirements to TLA+. This is the one hard number in the piece, and it cuts against heavy formalization rather than against specs generally.
- Verification strength should scale with risk, not be applied uniformly.
- Small briefs still require real evidence and targeted clarification — "brief" is not "vague."
- Natural-language ambiguity in code generation is unsolved and not claimed to be solved here.

## Design Implications

- Replace the standing spec with a **[[wiki/concepts/ai-agents/change-brief|Change Brief]]**: outcome, non-goals, constraints, acceptance evidence — scoped to the delta.
- Practice **[[wiki/concepts/ai-agents/progressive-disclosure|progressive disclosure]]** for agent context: small maps, stable rules, pointers to depth.
- Review the implementation, not only the plan — a reviewed plan with an unreviewed diff is a false gate.
- At release, migrate facts into schemas, tests, policies, configuration, telemetry and decision records; keep rationale short and adjacent to what it explains.

## Tensions

- **Directly against [[wiki/concepts/ai-agents/spec-driven-development|Spec-Driven Development]] as currently held in this wiki.** That page records "code is disposable" and the spec as "Architectural North Star." This source inverts both: code is the durable fact, the spec is disposable. **Recorded, not merged** — see the Conflicts section on the SDD concept page.
- The two are reconcilable at different scopes: a *greenfield generate-from-spec* workflow versus *evolving an existing production system*. The disagreement is about which situation is typical.

## Open Questions

- Where exactly is the boundary between a brief that expires and rationale that should persist?
- Does "read the code, not the plan" hold when the codebase exceeds any usable context window?
- Is the TLA+ result evidence against formal specs, or against current models attempting them?

## Concepts Linked from This Source

- [[wiki/concepts/ai-agents/change-brief|Change Brief]]
- [[wiki/concepts/ai-agents/spec-driven-development|Spec-Driven Development]]
- [[wiki/concepts/ai-agents/progressive-disclosure|Progressive Disclosure]]
- [[wiki/concepts/ai-agents/context-engineering|Context Engineering]]

## LLM Use

Use when planning any agent workflow that is about to generate standing documentation. The key test to apply: *does this artifact help decide and review a specific delta, or is it becoming a parallel codebase?* Pair with the SDD concept page so both sides of the disagreement are in context.

## Reliability Notes

- **Practitioner argument, one cited empirical result.** Confidence 0.8 — internally coherent, addresses a real observed failure mode, but largely unmeasured.
- The TLA+ figures are cited without full attribution in the capture; verify the underlying 2026 evaluation before citing those numbers externally.
- **Ingested from an AI-generated extraction, not a verbatim read of the full article.**
