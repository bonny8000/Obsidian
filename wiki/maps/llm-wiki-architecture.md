---
type: map
status: active
created: 2026-05-18
updated: 2026-05-18
tags: [architecture, llm-wiki, obsidian]
sources:
  - sources/brunch-ghidesigner-487
confidence: 0.8
---

# LLM Wiki Architecture

The working pattern has three layers:

| Layer | Folder | Owner | Purpose |
| --- | --- | --- | --- |
| Raw sources | `raw/` | Human | Immutable evidence and source material |
| Wiki | `wiki/` | AI agent | Compiled Markdown knowledge base |
| Schema | `AGENTS.md` / `CLAUDE.md` | Human plus AI | Rules for structure, style, ingest, query, and linting |

## Flow

1. Bonny adds material to `raw/`.
2. The AI agent ingests it.
3. The AI agent updates source pages, concept pages, maps, and logs.
4. Bonny reads and explores the result in Obsidian.
5. Query results and new insights can become additional wiki pages.

## Related

- [[concepts/infrastructure-dev/llm-wiki|LLM Wiki]]
- [[concepts/ai-agents/ai-maintained-wiki|AI-Maintained Wiki]]
- [[concepts/infrastructure-dev/knowledge-linting|Knowledge Linting]]


