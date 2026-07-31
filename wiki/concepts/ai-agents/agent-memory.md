---
type: concept
status: active
created: 2026-05-18
updated: 2026-07-31
tags: [ai-agent, memory, knowledge-management, evals, procedural-memory, cross-session, decision-log]
sources:
  - sources/brunch-ghidesigner-486
  - sources/brunch-ghidesigner-487
  - sources/theaxlabs-contaminated-memory-performance
  - sources/agent-skills-day-3
  - karrot-kraft-design-system-agent
confidence: 0.78
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
- Day-3 frames the memory typology as episodic ("what happened" — conversation history) + semantic ("facts" — RAG / pre-training) + [[concepts/ai-agents/procedural-memory|procedural memory]] ("how to do things step by step"). LLMs had reasonable analogs for the first two; [[concepts/ai-agents/agent-skills|Agent Skills]] are the first credible procedural memory primitive.
- Production memory needs lifecycle controls: write gates, promotion criteria, conflict handling, replay tests, and trace review.
- The main risk is [[concepts/ai-agents/memory-contamination|Memory Contamination]], where stale or unsupported memory becomes hidden context.

## Related Concepts

- [[concepts/infrastructure-dev/llm-wiki|LLM Wiki]]
- [[concepts/product-management/compounding-knowledge|Compounding Knowledge]]
- [[concepts/ai-agents/ai-agent-workflow|AI Agent Workflow]]
- [[concepts/ai-agents/skill-system|Skill System]]
- [[concepts/ai-agents/agent-skills|Agent Skills]]
- [[concepts/ai-agents/procedural-memory|Procedural Memory]]
- [[concepts/ai-agents/memory-contamination|Memory Contamination]]
- [[concepts/ai-agents/context-rot|Context Rot]]

## Sources

- [[sources/brunch-ghidesigner-486|Hermes Agent AI for Designers]]
- [[sources/brunch-ghidesigner-487|AI Designer LLM Wiki Article]]
- [[sources/theaxlabs-contaminated-memory-performance|AX LABS: Contaminated Memory Eats Away Performance]]
- [[sources/agent-skills-day-3|Singhal et al. (2026): Agent Skills (Day 3)]]
- [[wiki/sources/karrot-kraft-design-system-agent|Karrot (2026): Kraft]] — **cross-session memory with automatic promotion.** The problem stated plainly: a correction like "in this domain, always use `brandSolid` for CTAs" held for one session and vanished, and *"repeating the same correction every time is work for a person, not a tool."* The mechanism has three parts — decisions append to a per-session `decision-log.jsonl`; patterns repeating **above a threshold** are auto-promoted to per-domain principles in `principles.json`; new sessions read those principles back at the Memory Read step. Conversation context survives restarts in a LibSQL store. The promotion step is the reusable idea: memory that *summarises itself upward* rather than accumulating flat.
  **Caveat:** the threshold is unspecified, and nothing described prevents a wrong early decision from being promoted into a standing principle and propagating to every later user — which is [[concepts/ai-agents/memory-contamination|memory contamination]] with an automated distribution mechanism attached.

## Open Questions

- [Answered ??[[queries/2026-05-27-wiki-durable-vs-chat-memory|Query Page]]] Which items should become durable wiki memory versus temporary chat context?
- What memory metadata should this vault track to prevent contamination: provenance, promotion criteria, expiry, or conflict policy?

