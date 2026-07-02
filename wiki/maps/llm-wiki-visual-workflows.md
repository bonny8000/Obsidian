---
type: map
status: active
created: 2026-07-02
updated: 2026-07-02
tags: [map, llm-wiki, canvas, workflow, safety]
sources: []
confidence: 0.95
---

# LLM Wiki Visual Workflows

This hub translates the three user-provided reference diagrams into the actual architecture and capabilities of this vault.

## Open the Canvases

- [[../canvases/llm-wiki-three-layers.canvas|LLM Wiki: Three Layers]] — Raw evidence, compiled wiki, and schema/agent operating layer.
- [[../canvases/advanced-wiki-modules.canvas|Advanced Wiki Modules]] — implemented modules, optional local-model lane, and future retrieval modules.
- [[../canvases/safe-draft-review-apply.canvas|Safe Draft → Review → Apply]] — the human and validation gates that protect the vault.

## What Changed From the Reference Images

| Reference idea | Vault implementation |
| --- | --- |
| Raw → Wiki → Schema + Agents | Mapped to `raw/`, `wiki/`, and `AGENTS.md` / `CLAUDE.md` / scripts / dashboards. |
| PDF ingest | Original PDFs stay in `raw/files/`; extracted evidence becomes a raw card and source page. |
| Local LLM drafting | Ollama is installed but had no models on 2026-07-02; shown as optional, not production-ready. |
| Review folder | Implemented as a draft/diff and explicit review gate rather than a second uncontrolled knowledge tree. |
| Apply latest draft | Apply only after provenance and risk review, then run focused link checks and lint. |
| RAG / GraphRAG | Current retrieval uses links, maps, Bases, and graph view; semantic GraphRAG is a future module. |
| macOS launchers | Replaced with the current Windows + Codex workflow. |

## Operating Principle

> [!tip] Keep the core small
> The durable system is Raw → Source → Concept/Method/Map → Index/Log. Optional modules must feed that core without weakening provenance or bypassing review.

## Safety Boundary

- Raw evidence is immutable.
- Synthesis can change, but every substantive claim retains provenance.
- High-risk content requires a human review gate.
- No local model is trusted to write directly to `wiki/` without validation.
- A visually complete Canvas is navigation, not evidence.

## Related

- [[maps/llm-wiki-architecture|LLM Wiki Architecture]]
- [[playbooks/safe-ingest-promotion-workflow|Safe Ingest Promotion Workflow]]
- [[projects/llm-wiki-improvement-plan|LLM Wiki Improvement Plan]]
