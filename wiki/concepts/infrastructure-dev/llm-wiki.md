---
type: concept
status: active
created: 2026-05-18
updated: 2026-05-18
tags: [llm-wiki, knowledge-management, obsidian]
sources:
  - sources/brunch-ghidesigner-487
confidence: 0.8
---

# LLM Wiki

## Summary

An LLM Wiki is a persistent Markdown knowledge base maintained by an AI agent. Instead of retrieving raw fragments only at question time, the agent compiles sources into linked notes at ingest time.

## Why It Matters

The pattern turns repeated AI conversations into durable knowledge. It also makes the knowledge base inspectable in tools like Obsidian, where links and graph view can reveal clusters, gaps, and important concepts.

## Key Claims

- The raw source layer should remain immutable.
- The wiki layer is generated and maintained by the AI agent.
- The schema layer tells the agent how to structure pages and workflows.
- The main workflows are ingest, query, and lint.

## Related Concepts

- [[concepts/product-management/compounding-knowledge|Compounding Knowledge]]
- [[concepts/ai-agents/ai-maintained-wiki|AI-Maintained Wiki]]
- [[concepts/infrastructure-dev/knowledge-linting|Knowledge Linting]]
- [[maps/llm-wiki-architecture|LLM Wiki Architecture]]

## Sources

- [[sources/brunch-ghidesigner-487|AI Designer LLM Wiki Article]]

## Open Questions

- [Answered ??[[queries/2026-05-27-llm-wiki-source-types-first|Query Page]]] Which source types should Bonny ingest first?
- [Answered ??[[queries/2026-05-27-llm-wiki-git-version-control|Query Page]]] Should this vault be version controlled with Git?
- Which Obsidian plugins should be enabled after the basic workflow is stable? (insufficient evidence in wiki ??requires Obsidian plugin ecosystem knowledge not yet collected)


