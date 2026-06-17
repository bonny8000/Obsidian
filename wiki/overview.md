---
type: overview
status: active
created: 2026-06-12
updated: 2026-06-17
tags: [overview, synthesis, ux-research, llm-wiki, agentic-engineering]
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

- Source records: [[maps/llm-ready-source-index|71 tracked source pages]], with 53 currently marked `llm_ready: true`.
- UX research concept graph: [[concepts/ux-research/research-methods-foundations|research methods foundations]], [[concepts/ux-research/research-strategy|research strategy]], [[concepts/ux-research/research-operations|ResearchOps]], [[concepts/ux-research/ux-metrics|UX metrics]], and AI-assisted research concepts.
- UX research operating layer: [[methods/usability-testing|method pages]], [[comparisons/research-method-selection-matrix|comparison matrices]], and [[analyses/ux-research-wiki-gap-audit-2026-06-12|analysis memos]].

## Main Research Themes

- AI-assisted UX research: automation, hallucination control, human interpretation, and false-alarm triage.
- Quantitative UXR: metrics, sample sizing, standardized questionnaires, confidence intervals, and MaxDiff.
- Qualitative rigor: interviews, thematic analysis, reflexivity, validity, and methodological integrity.
- Research operations: research strategy, maturity, participant criteria, respect, ethics, and reusable research knowledge.
- Product-facing synthesis: translating research evidence into roadmaps, decisions, product taste, and AI-native workflows.
- Agent memory operations: memory lifecycle, contamination controls, trace review, and durable context governance.
- AI-era design taste: craft judgment, critique, care, and human review gates for generated artifacts.

## How To Use With An LLM

- For grounded recommendations, start from `llm_ready: true` sources and cite the source pages that support the recommendation.
- For ideation, combine method pages with concept pages, then verify against source records before turning ideas into decisions.
- For UX research planning, begin with [[comparisons/research-method-selection-matrix|Research Method Selection Matrix]], then open the relevant method page and source records.
- For AI-assisted research, use [[comparisons/ai-assisted-research-risk-matrix|AI-Assisted Research Risk Matrix]] before trusting an LLM-generated insight.

## Known Gaps

- Some source records remain `coverage: partial` and should be deepened before being used as primary decision evidence.
- The method library is now seeded, but each method should be expanded with project examples, study templates, and decision criteria.
- Analysis memos should be added whenever sources are synthesized into a product or research recommendation.

## Agent Experience (AX)

A dedicated cluster under `concepts/agent-experience/` now covers the design knowledge for agentic products, organized around the leverage-versus-control tension: initiative (proactivity, interruption, collaboration patterns) and trust (calibration, transparency, error recovery, mental-model onboarding), plus an evaluation bridge into the method library (wizard-of-oz, longitudinal, diary studies). Entry point: [[maps/agent-experience-design|Agent Experience (AX) Design]]. Current confidence is practitioner-level; the cluster's stated next step is ingesting empirical human-AI interaction sources.

## Agentic Engineering Series (Day 1 + Day 2 + Day 3)

A three-paper arc now grounds the vault's agentic-engineering thinking:

- [[sources/the-new-sdlc-with-vibe-coding-day-1|Day 1 — The New SDLC With Vibe Coding]] (Osmani, Saboo, Kartakis): the move from ad-hoc prompting to agentic engineering — context engineering, the factory model, harness engineering, conductor vs orchestrator roles, the static-vs-dynamic context split.
- [[sources/agent-tools-interoperability-day-2|Day 2 — Agent Tools & Interoperability]] (Patlolla, Olejniczak, Ippolito): the five interoperability protocols — MCP (reach), A2A (delegation), A2UI (generative UI), AP2 (payments), UCP (commerce). Shifts orchestration from bespoke conductor to modular plug-and-play.
- [[sources/agent-skills-day-3|Day 3 — Agent Skills]] (Singhal, Hernandez Larios, Dus, Nigam, Kolan): Agent Skills as the procedural memory primitive — folder format, progressive disclosure, four failure modes, five-pattern evaluation toolkit, Read/Draft/Act graduation ladder, meta-skills, DAG orchestration, Capability Profiles, retail case study.

Routing decision (Skill vs MCP vs AGENTS.md vs [[concepts/infrastructure-dev/design-md|DESIGN.md]]): see [[comparisons/skills-vs-mcp-vs-agents-md|Skills vs MCP vs AGENTS.md vs DESIGN.md]]. Mental model from Day-3: *System prompt = instinct. AGENTS.md = project README. Tools / MCP = hands. RAG = library. Skills = the runbook the experienced colleague hands you on day one.* The Atlassian DESIGN.md case study ([[sources/atlassian-design-md|Hall & Campbell, 2026]]) adds a production data point: DESIGN.md is the right primitive for one-shot / portable / customer-theming jobs, but in an established production codebase it burns ~92% more tokens than an MCP and steers agents to *re-implement* components rather than import them. Companion framing piece ([[sources/atlassian-design-system-context-engine|Christley & Radford, 2026]]) crystallizes the [[concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]] four-pillar maturity model and the **Context Engine** stack (foundations + tokens + components + context layer of structured content / MCP / skills / templates / DESIGN.md).
