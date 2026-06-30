---
type: concept
status: active
created: 2026-05-18
updated: 2026-06-26
tags: [llm-wiki, knowledge-management, obsidian]
sources:
  - sources/brunch-ghidesigner-487
  - sources/yozm-obsidian-llm-wiki-secondbrain
  - sources/brunch-ponyodesign-llm-wiki-clone
  - sources/yozm-tiro-ax-ontology
confidence: 0.85
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
- **This vault's blueprint:** [[sources/yozm-obsidian-llm-wiki-secondbrain|Gom's IT Blog (2026)]] documents the exact pattern this vault implements — Obsidian + GitHub + Claude Code, the immutable-raw → AI-maintained-wiki split, and the `/ingest` `/lint` `/query` skills — plus the discipline to *improve incrementally rather than over-design the structure up front.*
- **Convergent independent evidence (2026-06):** a designer's personal build ([[sources/brunch-ponyodesign-llm-wiki-clone|ponyodesign]] — *"Obsidian is the IDE, AI is the programmer, the wiki is the codebase,"* the same premise as this vault) and an organization-scale build ([[sources/yozm-tiro-ax-ontology|The Plato / Tiro]] — meeting-records → pre-[[concepts/infrastructure-dev/organizational-ontology|ontology]] → agents) show the same raw → AI-maintained-wiki pattern at both personal and org scope, both explicitly citing Karpathy's "LLM Wiki."

## Related Concepts

- [[concepts/product-management/compounding-knowledge|Compounding Knowledge]]
- [[concepts/ai-agents/ai-maintained-wiki|AI-Maintained Wiki]]
- [[concepts/infrastructure-dev/knowledge-linting|Knowledge Linting]]
- [[maps/llm-wiki-architecture|LLM Wiki Architecture]]

## Sources

- [[sources/brunch-ghidesigner-487|AI Designer LLM Wiki Article]]
- [[sources/yozm-obsidian-llm-wiki-secondbrain|Gom's IT Blog (2026): Building an Obsidian-Based LLM Wiki (this vault's blueprint)]]
- [[sources/brunch-ponyodesign-llm-wiki-clone|ponyodesign (2026): I Created a Clone of Myself That Knows Me Best (personal-scale build)]]
- [[sources/yozm-tiro-ax-ontology|Yozm × The Plato (2026): Ontology for AX from Meeting Records (org-scale build, feat. Tiro)]]

## Open Questions

- [Answered ??[[queries/2026-05-27-llm-wiki-source-types-first|Query Page]]] Which source types should Bonny ingest first?
- [Answered ??[[queries/2026-05-27-llm-wiki-git-version-control|Query Page]]] Should this vault be version controlled with Git?
- Which Obsidian plugins should be enabled after the basic workflow is stable? (insufficient evidence in wiki ??requires Obsidian plugin ecosystem knowledge not yet collected)


