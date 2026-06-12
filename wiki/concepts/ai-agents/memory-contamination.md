---
type: concept
status: active
created: 2026-06-12
updated: 2026-06-12
tags: [ai-agent, memory, evals, contamination, agent-operations]
sources:
  - sources/theaxlabs-contaminated-memory-performance
confidence: 0.84
---

# Memory Contamination

## Summary

Memory contamination is the failure mode where incorrect, stale, unsupported, or self-generated information enters an agent's durable memory and later gets reused as if it were trusted context.

It is not only a retrieval problem. A memory system can retrieve something successfully and still harm performance if the remembered item was badly written, promoted too early, injected into the wrong context, or left unresolved after a conflict.

## Why It Matters

Agent memory creates compounding value only when it remains source-grounded and governable. Without write gates, promotion criteria, conflict handling, and trace-based review, memory becomes hidden technical debt: old exceptions become rules, summaries become false authority, and agent inference becomes durable "fact."

## Key Claims

- Memory quality should include contamination resistance, not just retrieval recall.
- Memory lifecycle stages include search, context injection, use in action, and update or deletion.
- Memory writes need provenance labels such as user statement, system record, source-backed fact, or agent inference.
- Promotion criteria should separate one-off facts from durable operating rules.
- Conflict handling should record whether a new memory replaces, coexists with, or invalidates older memory.
- Replay testing can expose drift by comparing empty memory vs. real memory, injecting known bad memory, changing time order, and planting canary memories.
- Trace-level evaluation is necessary because final-answer grading can hide memory-path failures.

## Related Concepts

- [[concepts/ai-agents/agent-memory|Agent Memory]]
- [[concepts/ai-agents/product-evals|Product Evals]]
- [[concepts/ai-agents/model-harness|Model Harness]]
- [[concepts/ai-agents/self-improving-agent-workflows|Self-Improving Agent Workflows]]
- [[concepts/infrastructure-dev/llm-wiki|LLM Wiki]]

## Sources

- [[sources/theaxlabs-contaminated-memory-performance|AX LABS: Contaminated Memory Eats Away Performance]]

## Open Questions

- Should this vault add memory-item metadata for provenance, promotion criteria, expiry, and conflict policy?
- How should Codex memories distinguish source-grounded knowledge from inferred operating preferences?
- Can source readiness fields (`llm_ready`, `raw_preserved`, `coverage`) be adapted for agent memory governance?

