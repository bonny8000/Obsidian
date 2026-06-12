---
type: concept
status: active
created: 2026-05-18
updated: 2026-05-18
tags: [llm, agents, product-architecture]
sources:
  - sources/lennys-podcast-cat-wu-ai-pm-claude-code
confidence: 0.7
---

# Model Harness

## Summary

A model harness is the product and system scaffolding around a model: prompts, tools, workflows, UI constraints, memory, permissions, verification, and other structures that help the model perform a task.

## Why It Matters

The transcript emphasizes that harnesses should change as model capability changes. A product may need extra scaffolding for an older model, then remove or de-emphasize it when a newer model naturally performs the behavior.

## Key Claims

- Harness features can compensate for current model weaknesses.
- New model launches should trigger a review of system prompts and product crutches.
- Some scaffolding remains useful for user visibility even if the model no longer strictly needs it.
- Stronger models can unlock previously unreliable features such as richer code review.

## Related Concepts

- [[concepts/ai-agents/claude-code|Claude Code]]
- [[concepts/ai-agents/model-introspection|Model Introspection]]
- [[concepts/ai-agents/product-evals|Product Evals]]
- [[concepts/ai-agents/self-improving-agent-workflows|Self-Improving Agent Workflows]]

## Sources

- [[sources/lennys-podcast-cat-wu-ai-pm-claude-code|Lenny's Podcast: Cat Wu on AI-Native Product Management]]

## Open Questions

- [Answered → [[queries/2026-05-27-wiki-harness-vs-product-logic|Query Page]]] Which parts of Bonny's wiki ingest process are true product logic versus temporary model scaffolding?

