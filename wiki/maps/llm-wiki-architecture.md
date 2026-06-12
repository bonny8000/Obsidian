---
type: map
status: active
created: 2026-05-18
updated: 2026-06-12
tags: [architecture, llm-wiki, obsidian, llm-ready]
sources:
  - sources/brunch-ghidesigner-487
confidence: 0.9
---

# LLM Wiki Architecture

The vault is now organized as an evidence-backed knowledge system rather than a loose note collection. It is not a traditional database, but it has enough structure for LLM-assisted ideation when source readiness is respected.

## Layers

| Layer | Folder / artifact | Owner | Purpose |
| --- | --- | --- | --- |
| Raw evidence | `raw/` | Human plus capture agent | Immutable source material, PDFs, transcripts, source cards, and web captures. |
| Source records | `wiki/sources/` | AI agent | Per-source records with citation, claims, examples, caveats, implications, tensions, open questions, and LLM-use guidance. |
| Synthesis graph | `wiki/concepts/`, `wiki/maps/`, `wiki/queries/` | AI agent plus Bonny | Durable concepts, topic maps, saved answers, open questions, and cross-source synthesis. |
| UX research workspace | `wiki/methods/`, `wiki/comparisons/`, `wiki/analyses/`, `wiki/overview.md` | AI agent plus Bonny | Method pages, decision matrices, research memos, and high-level synthesis for UX research work. |
| Operating layer | `CLAUDE.md`, `AGENTS.md`, `index.md`, `log.md`, `scripts/`, `dashboard.base` | Human plus AI | Ingest rules, catalog, operations log, linting, readiness audits, dashboards, and maintenance automation. |

## Source Readiness

Each source page should carry:

```yaml
ingest_level: light | standard | deep
coverage: partial | substantial | full
llm_ready: true | false
raw_preserved: true | false
```

- `light`: useful for exploration, not enough for grounded decisions.
- `standard`: suitable for LLM-assisted ideation if claims are checked against raw evidence before final use.
- `deep`: preferred for repeatedly cited sources, books, source families, methods, transcripts, and research references.

Use [[maps/llm-ready-source-index|LLM-Ready Source Index]] to choose which sources can support grounded ideation.

## Flow

1. Bonny adds or points to source material.
2. The agent preserves raw evidence in `raw/` when available.
3. The agent writes or updates source records with honest LLM-readiness metadata.
4. The agent links source claims into concepts, maps, methods, comparisons, analyses, projects, and saved queries.
5. UX research work starts from a research question, selects a method, checks comparison matrices, then grounds synthesis in source records.
6. LLM-assisted ideation starts from `llm_ready: true` sources and escalates to raw evidence when decisions or citations matter.
7. Maintenance scripts update readiness maps, lint reports, research agendas, and change logs.

## Practical Rule

The wiki can support strong ideation when the prompt asks the LLM to combine:

- a relevant map,
- a method or comparison page when the question is about UX research,
- 3-7 `llm_ready: true` source records,
- linked concepts,
- and raw evidence for any final claim.

It should not be treated as complete evidence when the source has `coverage: partial` or `llm_ready: false`.

## Related

- [[maps/llm-ready-source-index|LLM-Ready Source Index]]
- [[overview|Knowledge Base Overview]]
- [[comparisons/research-method-selection-matrix|Research Method Selection Matrix]]
- [[concepts/infrastructure-dev/llm-wiki|LLM Wiki]]
- [[concepts/ai-agents/ai-maintained-wiki|AI-Maintained Wiki]]
- [[concepts/infrastructure-dev/knowledge-linting|Knowledge Linting]]
