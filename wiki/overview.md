---
type: overview
status: active
created: 2026-06-12
updated: 2026-06-22
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

- Source records: [[maps/llm-ready-source-index|110 tracked source pages]], with 93 currently marked `llm_ready: true`.
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

## Agentic Engineering Series (Day 1–5)

Entry point: **[[maps/agentic-engineering|Agentic Engineering (MOC)]]** ties this whole cluster (concepts + Day 1–5 + the 15 LangChain sources + Bayer PRINCE) into one navigable hub. A five-paper arc now grounds the vault's agentic-engineering thinking:

- [[sources/the-new-sdlc-with-vibe-coding-day-1|Day 1 — The New SDLC With Vibe Coding]] (Osmani, Saboo, Kartakis): the move from ad-hoc prompting to agentic engineering — context engineering, the factory model, harness engineering, conductor vs orchestrator roles, the static-vs-dynamic context split.
- [[sources/agent-tools-interoperability-day-2|Day 2 — Agent Tools & Interoperability]] (Patlolla, Olejniczak, Ippolito): the five interoperability protocols — MCP (reach), A2A (delegation), A2UI (generative UI), AP2 (payments), UCP (commerce). Shifts orchestration from bespoke conductor to modular plug-and-play.
- [[sources/agent-skills-day-3|Day 3 — Agent Skills]] (Singhal, Hernandez Larios, Dus, Nigam, Kolan): Agent Skills as the procedural memory primitive — folder format, progressive disclosure, four failure modes, five-pattern evaluation toolkit, Read/Draft/Act graduation ladder, meta-skills, DAG orchestration, Capability Profiles, retail case study.
- [[sources/vibe-coding-agent-security-evaluation-day-4|Day 4 — Vibe Coding Agent Security & Evaluation]] (Kartakis, Eidelman, Bakkali, Subasioglu): two axes of trust — **Security** (did the agent stay inside the boundary?) and **Evaluation** (is what's inside worth shipping?). The **7-pillar agent security architecture**, Context-as-a-Perimeter / Effective Trust, slopsquatting, Confused Deputy / zero ambient authority, MCP spoofing, and **Red/Blue/Green agent teaming**.
- [[sources/spec-driven-production-development-day-5|Day 5 — Spec-Driven Production-Grade Development]] (Boonstra): "vibe coding ≠ vibe in production." **Spec-Driven Development** (spec as source of truth, code is disposable, BDD/Gherkin, the Markdown+YAML "format tax"), the instruction hierarchy (chat → specs → skills → GEMINI.md/AGENTS.md), and a **zero-trust safety net** for production.

Routing decision (Skill vs MCP vs AGENTS.md vs [[concepts/infrastructure-dev/design-md|DESIGN.md]]): see [[comparisons/skills-vs-mcp-vs-agents-md|Skills vs MCP vs AGENTS.md vs DESIGN.md]]. Mental model from Day-3: *System prompt = instinct. AGENTS.md = project README. Tools / MCP = hands. RAG = library. Skills = the runbook the experienced colleague hands you on day one.* The Atlassian DESIGN.md case study ([[sources/atlassian-design-md|Hall & Campbell, 2026]]) adds a production data point: DESIGN.md is the right primitive for one-shot / portable / customer-theming jobs, but in an established production codebase it burns ~92% more tokens than an MCP and steers agents to *re-implement* components rather than import them. Companion framing piece ([[sources/atlassian-design-system-context-engine|Christley & Radford, 2026]]) crystallizes the [[concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]] four-pillar maturity model and the **Context Engine** stack (foundations + tokens + components + context layer of structured content / MCP / skills / templates / DESIGN.md).

## AI × UX and Agentic Reliability (2026-06-22 batch)

A 14-source batch broadened the vault beyond the design-system/agentic-engineering core into AI-era UX research practice and human-AI experience. Four threads:

- **Agentic reliability as engineering:** [[sources/bayer-prince-reliable-agentic-ai|Bayer PRINCE]] (agentic RAG + the [[concepts/ai-agents/context-engineering|context-engineering]] vs harness split, three reflection loops) and [[sources/fowler-sensors-coding-agents|Böckeler's maintainability sensors]] ([[concepts/infrastructure-dev/maintainability-sensor|computational vs inferential sensors]], [[concepts/infrastructure-dev/mutation-testing|mutation testing]]). Both Thoughtworks/martinfowler.com — the system side and the code side of harness engineering.
- **Limits of AI collaboration and AI-mediated information:** [[sources/hai-cooperbench-agent-teamwork|CooperBench]] ([[concepts/ai-agents/multi-agent-coordination|the coordination gap]] — two agents do worse than one) and the [[sources/hai-headlines-ai-news-audit|six-chatbot news audit]] ([[concepts/ai-agents/ai-news-intermediary|retrieval, not reasoning, drives errors]]; aggregate accuracy hides regional and adversarial failure).
- **AI-era UX research practice:** [[sources/nngroup-design-process-compressed|process literacy/compression]], [[sources/guanjie-li-llm-user-proxy|LLM user proxies]] (the rubric is the bottleneck, not model capability), [[sources/trevor-calabro-ux-research-as-a-service|research-as-a-service]], and [[sources/ada-kim-satisfaction-vs-benefit-ai|satisfaction ≠ benefit]] / [[concepts/agent-experience/ai-sycophancy|sycophancy]].
- **Design-system AI prototyping:** [[sources/atlassian-ai-prototyping-handshakes|Atlassian]] and [[sources/figma-mcp-server-four-ways|Figma]] — [[concepts/infrastructure-dev/ai-prototyping|AI prototyping]] grounded in [[concepts/infrastructure-dev/agentic-content|agentic content]].

One source remains `coverage: partial` pending access (Ipsos' Ceros report); Newton's article and the ACM DIS 2026 paper ([[sources/acm-dis2026-algorithmic-self-portraits|Lee et al., TubeLens]], surfacing [[concepts/ux-research/algorithmic-self|Algorithmic Self]] and [[concepts/ux-research/uxr-role-split|UXR Role Split]]) were upgraded to full ingests on 2026-06-22 from user-supplied text/PDF.

A further same-day batch deepened the **UX-research-methods** layer: [[sources/bakhshi-representative-sample|claim-based sampling]] (a sample is adequate for a *claim*, not representative in the abstract), the [[sources/bakhshi-ai-in-qualitative-research-map|five-axis map for AI in qualitative research]], the [[concepts/ux-research/say-do-gap|say-do gap]] (Pieritz: relevance ≠ purchase intent), plus product cases — Myrealtrip's [[concepts/product-management/feature-vs-platform|feature→platform]] cancellation-recommendation (AI used as a *rebutter*, ~70% lift framed honestly as observational) and an [[concepts/product-management/ai-prd|AI-PRD]] framing (spec the acceptable-answer range + an Eval Plan).

An 8-post **LangChain agent-engineering** batch added the operational layer: [[concepts/ai-agents/multi-agent-architecture|multi-agent architecture]] (subagents / skills / handoffs / router — to be read *against* the [[concepts/ai-agents/multi-agent-coordination|coordination gap]]), [[concepts/ai-agents/loop-engineering|loop engineering]], [[concepts/ai-agents/agent-middleware|agent middleware]] / [[concepts/ai-agents/deep-agents|deep agents]], [[concepts/ai-agents/agent-verifiers|agent verifiers]] (LLM-as-judge), [[concepts/ai-agents/model-neutrality|model neutrality]], [[concepts/infrastructure-dev/agent-cost-control|agent cost control]], and enterprise builds (Box; Lyft's [[concepts/infrastructure-dev/self-serve-agent-platform|self-serve agent platform]]) — much of it on LangGraph/LangSmith, the same stack as [[sources/bayer-prince-reliable-agentic-ai|Bayer PRINCE]]. A second LangChain batch followed: [[concepts/ai-agents/agent-authorization|agent authorization]] (delegated vs own identity — extending Day-4's Confused Deputy), [[concepts/infrastructure-dev/eu-ai-act-compliance|EU AI Act compliance]] (observability → evals → HITL as the evidence layer), [[concepts/ai-agents/async-subagents|async/background subagents]], [[concepts/ai-agents/agent-interpreter|interpreter skills]], [[concepts/ai-agents/agent-trajectory-evaluation|trajectory evaluation]] of deep agents, and [[concepts/ai-agents/agentic-search|agentic search]] (Exa) — plus the canonical [[concepts/ai-agents/agent-middleware|Agent Middleware]] origin post.
