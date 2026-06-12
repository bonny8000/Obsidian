---
type: source
status: active
created: 2026-06-05
tags: [ai-uxr, maturity-matrix, research-ops, agentic-workflows]
sources: []
updated: 2026-06-12
ingest_level: deep
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 1.0
---

# How To AI UXR: The ResearchOps Review (2026)

- **Author:** Kate Towsey (for The ResearchOps Review)
- **Year:** 2026
- **Sponsor:** Strella
- **Location:** `raw/how-to-ai-uxr-2026.pdf`

## Summary

A maturity matrix and implementation guide for integrating AI into the UX Research (UXR) workflow. Based on 562 data points gathered in early 2026, the resource uses a "Crawl, Walk, Run" framework to categorize AI usage from individual task automation to fully autonomous agentic systems.

## The Maturity Framework

### 🐢 Crawl: Individual Task Augmentation
Off-the-shelf LLMs used for drafting, summarising, and clustering. Gains are individual and largely unseen at the organizational level. The standard research workflow remains intact.

### 🚶 Walk: Organisation-Level Systems
Focus shifts to team-level systems using RAG (Retrieval-Augmented Generation) and custom agents. Steps in the workflow (analysis/synthesis/packaging) start to merge. Introduction of "evals" as a discipline.

### 🏃 Run: Agentic Research Systems
Production-grade systems that anticipate needs and push insights. Research is delivered via Human-in-the-Loop (HITL) agentic systems. The workflow condenses into far fewer, often "black box" steps.

## Key Implementation Areas

The review maps AI implementations across 10 steps of the research journey:
1. Prioritisation & Roadmapping
2. Method Selection & Scoping
3. Existing Insights Retrieval & Reuse
4. Research Artefact Creation
5. Participant Recruitment
6. Data Collection
7. Data Preparation
8. Analysis
9. Synthesis
10. Insights Packaging & Communication

## Glossary of Key Terms

- **Agentic Workflow:** unit of work shifts from "task assistance" to "workflow ownership."
- **Evals (AI Evaluation):** systematic measurement of agent performance against predefined criteria.
- **Model Council:** multi-model architecture running queries through several LLMs for cross-verification.
- **Synthetic Personas:** AI-generated personas used to pressure-test ideas before human studies.
- **"Black Box" Insights:** opaque reasoning produced by AI requiring systematic evaluation.

## Concepts Linked

- [[concepts/ux-research/ai-uxr-maturity-matrix|AI UXR Maturity Matrix]]
- [[concepts/ux-research/agentic-research-workflows|Agentic Research Workflows]]
- [[concepts/ux-research/ai-evals|AI Evals in Research]]
- [[concepts/ux-research/grounded-synthetic-personas|Synthetic Personas]]
- [[concepts/ux-research/research-operations|Research Operations]]

## Key Claims

- Backfill note: no explicit claims were extracted before this upgrade. Promote claims from the raw source during a standard or deep ingest pass.

## Useful Examples

- Current example source: use examples, tables, cases, or named artifacts already present elsewhere in this note; otherwise return to `raw/how-to-ai-uxr-2026.pdf` before asking an LLM for concrete examples.

## Constraints / Caveats

- Coverage is `substantial` and ingest level is `deep`; do not treat this source as fully digested unless `coverage: full`.
- Claims should be checked against `raw/how-to-ai-uxr-2026.pdf` when used for recommendations, metrics, or external-facing work.

## Citation

- Source record: `How To AI UXR: The ResearchOps Review (2026)`.
- Raw evidence: `raw/how-to-ai-uxr-2026.pdf`.

## Reliability Notes

- Coverage is `substantial` and ingest level is `deep`; do not treat this source as fully digested unless `coverage: full`.
- Claims should be checked against `raw/how-to-ai-uxr-2026.pdf` when used for recommendations, metrics, or external-facing work.

> [!warning] Caveats
> Reliability was not assessed in the earlier note. Treat this source as a prompt for exploration until raw evidence is checked.

## Design Implications

- Use this source to shape research design, UX evidence, method selection, and evaluation prompts.
- Connect it with [[concepts/ux-research/ai-uxr-maturity-matrix]], [[concepts/ux-research/agentic-research-workflows]], [[concepts/ux-research/ai-evals]], [[concepts/ux-research/grounded-synthetic-personas]] before turning it into a project recommendation.

## Tensions

- Backfill note: source-specific tensions were not separately extracted in the earlier ingest. Compare this source with related concepts and maps before treating its framing as settled.

## Open Questions

- What evidence, examples, or counterexamples should be extracted from the raw source before marking this as `coverage: full`?
- Which linked concept would change most if this source were contradicted?

## LLM Use

- **Use for:** research design, UX evidence, method selection, and evaluation prompts.
- **Do not use for:** unsupported exact claims beyond the source note's `substantial` coverage.
- **Best prompt pattern:** Ask the LLM to combine this source with its linked concepts, then verify any specific claim against the raw source before final use.

## Backfill Status

- Retrofitted on 2026-06-12 by `scripts/backfill_llm_ready.py` from the existing source note.
- This standardizes the note for LLM use; it does not by itself mean the raw source has been fully re-read.
