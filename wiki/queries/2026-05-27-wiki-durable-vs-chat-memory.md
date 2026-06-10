---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.72
---

# Which items should become durable wiki memory versus temporary chat context?

## Short Answer
Items that are source-grounded, reusable across multiple future sessions, or represent successful procedures belong in durable wiki memory. Single-session questions, one-off lookups, and conversational scaffolding remain temporary chat context. The key test is whether the knowledge would compound if reused.

## Evidence
- [[concepts/ai-agents/agent-memoryAgent Memory]] ??"Memory should be source-grounded and auditable. Long-term memory is most useful when paired with retrieval, structured notes, and change logs. Memory can store both knowledge and process patterns."
- [[concepts/infrastructure-dev/llm-wikiLLM Wiki]] ??"The raw source layer should remain immutable. The wiki layer is generated and maintained by the AI agent." Anything derived from a real source qualifies for the wiki layer.
- [[concepts/ai-agents/skill-systemSkill System]] ??"In an LLM Wiki, skills and source-grounded notes should stay separate: skills say how to work; wiki pages say what is known." This gives a second durable store for process knowledge.
- [[sources/brunch-ghidesigner-487|AI Designer LLM Wiki Article]] ??"The LLM Wiki pattern is meant to reduce the loss of useful knowledge between isolated AI chat sessions."

## Follow-up Sources Needed
- Criteria for when a query result or agent output is stable enough to promote to the wiki layer.

