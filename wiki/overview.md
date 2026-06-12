---
type: overview
status: active
created: 2026-06-12
updated: 2026-06-12
tags: [overview, synthesis, ux-research, llm-wiki]
sources:
  - maps/llm-ready-source-index
  - maps/ai-ux-research-methods
  - maps/research-methods-knowledge-base
  - maps/ux-metrics-framework
confidence: 0.88
---

# Knowledge Base Overview

This vault is a research-first LLM knowledge base. `raw/` preserves evidence, `wiki/sources/` turns evidence into source records, and the durable working layer lives in concepts, methods, comparisons, analyses, maps, projects, decisions, and queries.

## Current Shape

- Source records: [[maps/llm-ready-source-index|68 tracked source pages]], with 50 currently marked `llm_ready: true`.
- UX research concept graph: [[concepts/ux-research/research-methods-foundations|research methods foundations]], [[concepts/ux-research/research-strategy|research strategy]], [[concepts/ux-research/research-operations|ResearchOps]], [[concepts/ux-research/ux-metrics|UX metrics]], and AI-assisted research concepts.
- UX research operating layer: [[methods/usability-testing|method pages]], [[comparisons/research-method-selection-matrix|comparison matrices]], and [[analyses/ux-research-wiki-gap-audit-2026-06-12|analysis memos]].

## Main Research Themes

- AI-assisted UX research: automation, hallucination control, human interpretation, and false-alarm triage.
- Quantitative UXR: metrics, sample sizing, standardized questionnaires, confidence intervals, and MaxDiff.
- Qualitative rigor: interviews, thematic analysis, reflexivity, validity, and methodological integrity.
- Research operations: research strategy, maturity, participant criteria, respect, ethics, and reusable research knowledge.
- Product-facing synthesis: translating research evidence into roadmaps, decisions, product taste, and AI-native workflows.

## How To Use With An LLM

- For grounded recommendations, start from `llm_ready: true` sources and cite the source pages that support the recommendation.
- For ideation, combine method pages with concept pages, then verify against source records before turning ideas into decisions.
- For UX research planning, begin with [[comparisons/research-method-selection-matrix|Research Method Selection Matrix]], then open the relevant method page and source records.
- For AI-assisted research, use [[comparisons/ai-assisted-research-risk-matrix|AI-Assisted Research Risk Matrix]] before trusting an LLM-generated insight.

## Known Gaps

- Some source records remain `coverage: partial` and should be deepened before being used as primary decision evidence.
- The method library is now seeded, but each method should be expanded with project examples, study templates, and decision criteria.
- Analysis memos should be added whenever sources are synthesized into a product or research recommendation.

