---
type: concept
status: active
created: 2026-06-26
updated: 2026-06-26
tags: [text-to-sql, llm-safety, deterministic-validation, ast-validation, pgvector, multi-tenant-security, harness-engineering]
sources:
  - sources/imweb-safe-llm-generated-sql
confidence: 0.78
---

# Text-to-SQL

## Summary

**Text-to-SQL** is the capability of translating a natural-language question into executable SQL via an LLM — and, just as importantly, the **deterministic safety harness** needed to make that generated SQL trustworthy. The hard problem is not generating SQL but trusting it: an LLM can rewrite the *entire query structure*, so the defense is to treat the generator as untrusted and validate the **generated artifact**, not the input.

## Why It Matters

Text-to-SQL lets non-technical users (e.g. e-commerce sellers) self-serve data answers, removing the data-team bottleneck of hand-writing every query. But LLM-generated SQL is a structurally different threat from classic SQL injection: it invents columns, picks wrong tables, does NULL-poisoned arithmetic, or omits tenant isolation. Input sanitization is useless here — safety has to live at the data boundary. This makes Text-to-SQL a clean, copyable case study in [[concepts/ai-agents/zero-trust-agent-development|zero-trust]] tool design for any agent that touches sensitive data.

## Key Claims

- **Validate the generated artifact, not the input.** The classic injection defense (sanitize values) does not apply when the model controls the whole query; you must parse and check the SQL itself.
- **Judgment/Execution separation.** Split a "brain" (intent, response synthesis) from a "toolbox" (generate, validate, execute) so security localizes at the data layer and every entry point (UI, API, future agent) inherits the same gates.
- **Deterministic AST gates.** Imweb's pattern: parse to an AST and run sequential checks — **Existence** (table/column allowlist vs catalog), **Policy** (forced tenant filter, no full scans, COALESCE for NULL arithmetic, no destructive keywords), **Shape** (SELECT-only, valid syntax, reject hallucinated identifiers). Gates return *actionable corrections*, not just rejections.
- **Domain rules as retrieved data.** Business definitions (e.g. revenue = net, not gross) live in a `pgvector` knowledge base (pinned + cosine-retrieved), so a wrong rule is fixed by editing a row and re-embedding — no redeploy.
- **Bounded self-repair.** Feed gate violations back to the model as instructions, capped (e.g. 2 attempts) then escalate to the human — to avoid runaway regeneration.
- **Silent semantic errors are uncatchable pre-execution.** Valid grammar + valid columns + wrong meaning runs cleanly, so gates are necessary but not sufficient; you still need golden-set regression + post-deploy monitoring.

## Related Concepts

- [[concepts/ai-agents/zero-trust-agent-development|Zero-Trust Agent Development]] — "distrust the model output" is the parent stance.
- [[concepts/ai-agents/agent-security-architecture|Agent Security Architecture]] — gate at the resource, not the entry point.
- [[concepts/ai-agents/agent-verifiers|Agent Verifiers]] — the AST gates are deterministic verifiers with repair.
- [[concepts/ai-agents/harness-engineering|Harness Engineering]] — the validation/repair scaffold around the generator.
- [[concepts/ai-agents/loop-engineering|Loop Engineering]] — the bounded self-repair loop.
- [[concepts/ai-agents/agentic-rag|Agentic RAG]] / [[concepts/ai-agents/context-engineering|Context Engineering]] — domain rules retrieved from a vector store.
- [[concepts/ux-research/ai-evals|AI Evals]] — golden-set, stage-wise judging with code-side aggregation.

## Conflicts & Caveats

> [!warning] Necessary but not sufficient
> Deterministic gates catch structural faults but are blind to valid-but-wrong semantics; the safety story is incomplete by design. Stronger gates also breed their own false positives — precision, not aggressiveness, is the goal. Evidence so far is a single-vendor closed beta (no benchmark, no model disclosed).

## Sources

- [[sources/imweb-safe-llm-generated-sql|Choi / Imweb (2026): How to Safely Use SQL Written by AI]]

## Open Questions

- How are silent logic errors detected post-deploy — automated monitors, sampling, or user-reported?
- How does a catalog-allowlist gate stay correct as the warehouse schema evolves?
- How do you stop secondary-LLM judges from sharing the generator's blind spots?
