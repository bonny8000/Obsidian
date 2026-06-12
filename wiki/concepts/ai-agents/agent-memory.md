---
type: concept
status: active
created: 2026-05-18
updated: 2026-06-12
tags: [ai-agent, memory, knowledge-management, evals]
sources:
  - sources/brunch-ghidesigner-486
  - sources/brunch-ghidesigner-487
  - sources/theaxlabs-contaminated-memory-performance
confidence: 0.72
---

# Agent Memory

## Summary

Agent memory is the persistent context that lets an AI system reuse prior interactions, decisions, project rules, source summaries, and successful procedures.

## Why It Matters

Without memory, useful AI work disappears at the end of a session. In an [[concepts/infrastructure-dev/llm-wiki|LLM Wiki]], memory becomes inspectable Markdown rather than an opaque model-side state.

## Key Claims

- Memory should be source-grounded and auditable.
- Long-term memory is most useful when paired with retrieval, structured notes, and change logs.
- Memory can store both knowledge and process patterns.
- Production memory needs lifecycle controls: write gates, promotion criteria, conflict handling, replay tests, and trace review.
- The main risk is [[concepts/ai-agents/memory-contamination|Memory Contamination]], where stale or unsupported memory becomes hidden context.

## Related Concepts

- [[concepts/infrastructure-dev/llm-wiki|LLM Wiki]]
- [[concepts/product-management/compounding-knowledge|Compounding Knowledge]]
- [[concepts/ai-agents/ai-agent-workflow|AI Agent Workflow]]
- [[concepts/ai-agents/skill-system|Skill System]]
- [[concepts/ai-agents/memory-contamination|Memory Contamination]]

## Sources

- [[sources/brunch-ghidesigner-486|Hermes Agent AI for Designers]]
- [[sources/brunch-ghidesigner-487|AI Designer LLM Wiki Article]]
- [[sources/theaxlabs-contaminated-memory-performance|AX LABS: Contaminated Memory Eats Away Performance]]

## Open Questions

- [Answered ??[[queries/2026-05-27-wiki-durable-vs-chat-memory|Query Page]]] Which items should become durable wiki memory versus temporary chat context?
- What memory metadata should this vault track to prevent contamination: provenance, promotion criteria, expiry, or conflict policy?

