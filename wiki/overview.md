---
type: overview
status: active
created: 2026-06-12
updated: 2026-07-02
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

- Source records: [[maps/llm-ready-source-index|151 tracked source pages]], with 129 currently marked `llm_ready: true`.
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
- Inclusive conversational research: audio-first access, community co-design, AI disclosure, and the separation of completion from data validity.
- Product monetization design: value, reassurance, and convenience upsells bounded by clear choice and trust metrics.

## How To Use With An LLM

- For grounded recommendations, start from `llm_ready: true` sources and cite the source pages that support the recommendation.
- For ideation, combine method pages with concept pages, then verify against source records before turning ideas into decisions.
- For UX research planning, begin with [[comparisons/research-method-selection-matrix|Research Method Selection Matrix]], then open the relevant method page and source records.
- For AI-assisted research, use [[comparisons/ai-assisted-research-risk-matrix|AI-Assisted Research Risk Matrix]] before trusting an LLM-generated insight.

## Known Gaps

- Some source records remain `coverage: partial` and should be deepened before being used as primary decision evidence.
- The method library is now seeded, but each method should be expanded with project examples, study templates, and decision criteria.
- Analysis memos should be added whenever sources are synthesized into a product or research recommendation.

## Cross-Domain Ingest and Visual Workflow Upgrade (2026-07-02)

Four sources expanded four different parts of the graph:

- [[sources/sangwook-typescript-6-migration-troubleshooting|TypeScript 6 migration troubleshooting]] → [[concepts/infrastructure-dev/typescript-configuration-hygiene|TypeScript Configuration Hygiene]]: make module resolution, output layout, ambient types, and tool-generated options explicit.
- [[sources/clova-merit-post-training|CLOVA MERIT]] → [[concepts/ai-agents/conflict-aware-instruction-tuning|Conflict-Aware Instruction Tuning]]: split heterogeneous datasets by gradient conflict, train independently, and merge once.
- [[sources/arxiv-2606.30660-value-sensitive-conversational-ai|Value-sensitive conversational surveys]] → [[concepts/ux-research/value-sensitive-conversational-surveys|Value-Sensitive Conversational Surveys]]: voice and culturally aligned cues can improve completion, but validity, transparency, consent, and causal attribution remain unresolved.
- [[sources/kakao-vc-upsell-design|Kakao Ventures on upsell design]] → [[concepts/product-management/upsell-design|Upsell Design]]: value, reassurance, and convenience offers require a viable base option, clear opt-out, and long-term trust metrics.

The user-provided architecture images also produced a new visual operating layer: [[maps/llm-wiki-visual-workflows|LLM Wiki Visual Workflows]] and [[playbooks/safe-ingest-promotion-workflow|Safe Ingest Promotion Workflow]].

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

## AI-Era Practice & Product (2026-06-25 batch)

A 9-source batch broadened the vault from "how agents work" toward **who builds with AI, how organizations adopt it, and how AI changes search and research practice**:

- **Builders & adoption.** [[concepts/product-management/domain-expert-as-builder|Domain Expert as Builder]] (a product designer ships full-stack with [[sources/dusskapark-product-designer-codex|Codex]]; 20 non-developer experts build & own agents in [[sources/theaxlabs-hanwha-life-claude-code-pbl|Hanwha Life's 6-week PBL]]) and [[concepts/infrastructure-dev/ai-adoption-culture|AI Adoption Culture]] — two routes to org-wide capability: Toss's bottom-up [[sources/toss-tossplace-ai-surf-day|AI Surf Day]] vs. a structured cohort. Recurring lesson, from both a designer and a vendor case: *the bottleneck is judgment and a continuous "define → data → structure → unblock" flow, not coding.*
- **PM tooling.** The [[concepts/product-management/planning-harness|Planning Harness]] ([[sources/maily-product-makers-planning-harness|Product Makers Note]]) is [[concepts/ai-agents/harness-engineering|harness engineering]] applied to planning — context + skills + guardrails + validation — the "AI sitter → harness engineer" shift, and a sibling of [[concepts/ai-agents/agent-skills|Agent Skills]] / [[concepts/infrastructure-dev/claudemd-context|CLAUDE.md]].
- **AI search.** Google's [[sources/google-good-seo-is-good-geo|"good SEO is good GEO"]] sharpens [[concepts/product-management/geo-generative-engine-optimization|GEO]] with a first-party counter-position (AI features ride core ranking; invest in E-E-A-T + fundamentals, not LLM hacks) — held in tension with the "GEO is a new discipline" view for non-Google engines.
- **Synthetic users & wearables.** A grounding-based [[concepts/ux-research/synthetic-user-taxonomy|Synthetic User Taxonomy]] (proto → demographic → persona → research-grounded → digital-twin) extends [[concepts/ux-research/synthetic-survey-data|synthetic survey data]]; [[concepts/robotics-spatial/input-modality|Input Modality]] (Kakao Ventures) maps the wearable sensor-input race (channel × collection × the trust barrier) beneath the [[concepts/ux-research/haic-modalities-taxonomy|HAIC modalities]] layer.
- **Meta.** [[sources/yozm-obsidian-llm-wiki-secondbrain|Gom's IT Blog]] is the **blueprint this vault implements** (raw → AI-maintained wiki, `/ingest` `/lint` `/query`, Obsidian + GitHub + Claude Code), now linked from [[concepts/infrastructure-dev/llm-wiki|LLM Wiki]]. One partial stub ([[sources/carrotcap-naver|Naver carrotcap]]) is blocked pending user-supplied text.

## Raw Drop — Safe LLM Tooling, Robotics & AI-Era Work (2026-06-26 batch)

A 5-source drop spanning the safety, hardware-efficiency, human, and autonomy edges of the AI stack:

- **Safe LLM tooling.** [[sources/imweb-safe-llm-generated-sql|Imweb's safe Text-to-SQL]] is a clean, copyable harness: treat the generator as untrusted and validate the *generated artifact* via deterministic AST gates (Existence / Policy / Shape), externalize domain rules into a [[concepts/ai-agents/agentic-rag|pgvector]] store, and bound the self-repair loop — the SQL-specific instance of [[concepts/ai-agents/zero-trust-agent-development|zero-trust]] [[concepts/ai-agents/agent-security-architecture|agent security]] and [[concepts/ai-agents/harness-engineering|harness engineering]]. New concept: [[concepts/ai-agents/text-to-sql|Text-to-SQL]].
- **On-robot efficiency.** Naver Labs Europe's [[sources/naverlabs-europe-divine-encoder|DIVINE]] consolidates many specialist perception encoders into one shared encoder via [[concepts/robotics-spatial/multi-teacher-distillation|multi-teacher distillation]] (DUSt3R + multi-HMR teachers), reportedly cutting encoder memory ~90% / system memory 62% — efficiency-as-architecture for [[concepts/robotics-spatial/physical-ai|physical AI]] under [[concepts/infrastructure-dev/on-premise-ai|onboard-compute]] limits (vendor metrics, unverified).
- **Agentic engineering in the field.** [[sources/heyratel-ios-ai-agent-environment|HeyRatel's iOS team]] builds an agent environment from explicit criteria ("the standard chooses the tools") — distributed CLAUDE.md, single-responsibility skills, custom curl skills over MCP for tokens, symlinked AGENTS.md, and an advisor-mode escalation gate. New concepts [[concepts/ai-agents/criteria-driven-ai-adoption|Criteria-Driven AI Adoption]] and [[concepts/ai-agents/model-escalation-gate|Model Escalation Gate]] — a working application of [[concepts/ai-agents/harness-engineering|harness engineering]] beside the [[concepts/product-management/planning-harness|planning harness]].
- **The human and autonomy edges.** Hudson's [[sources/lennys-newsletter-new-inner-game|New Inner Game]] argues that once knowledge and effort are commoditized, emotional clarity (the [[concepts/product-management/wisdom-stack|Wisdom Stack]]) is the durable advantage — the human-side companion to [[concepts/product-management/role-convergence|role convergence]] and [[concepts/product-management/domain-expert-as-builder|domain-expert-as-builder]]. Datarize's [[sources/datarize-intelligence-to-autonomy|From Intelligence to Autonomy]] (vendor marketing) reframes AI value as closing the [[concepts/product-management/insight-to-execution-gap|insight-to-execution gap]] — value = friction removed, not model sophistication.

## Raw Drop #2 — Org Ontology, Algorithmic Hiring Bias & a Self-Mirroring Wiki (2026-06-26 batch)

A 3-source follow-on drop, two of which reflect this vault straight back at it:

- **The LLM-Wiki pattern, independently rebuilt — twice.** A designer's personal build ([[sources/brunch-ponyodesign-llm-wiki-clone|ponyodesign]]: 3 years of notes → Obsidian → an AI "clone" that flags circular thinking; *"Obsidian is the IDE, AI the programmer, the wiki the codebase"*) and an org-scale build ([[sources/yozm-tiro-ax-ontology|The Plato / Tiro]]: meeting records → pre-ontology → agents) converge on the exact raw → AI-maintained-wiki pattern this vault implements, both citing Karpathy's "LLM Wiki." The Plato extends it into an [[concepts/infrastructure-dev/organizational-ontology|organizational ontology]] (data + logic + action) feeding per-person [[concepts/ai-agents/agent-digital-twin|agent digital twins]] — both now enriching [[concepts/infrastructure-dev/llm-wiki|LLM Wiki]] and [[concepts/ai-agents/ai-maintained-wiki|AI-Maintained Wiki]] as convergent evidence.
- **The cost of the same pattern at societal scale.** [[sources/hai-algorithmic-hiring-bias|Stanford HAI]] shows that when one AI hiring model is reused across most employers, individual bias becomes [[concepts/ux-research/algorithmic-monoculture|algorithmic monoculture]] → *systemic rejection* (rejected everywhere at once), invisible to pooled metrics and exposed only by a position-level four-fifths audit — a reminder that the [[concepts/ux-research/ai-evals|evaluation]] discipline must disaggregate, and an ethics counterweight to the build-it-everywhere enthusiasm of the other two.

## Digital Twins & AI-UX (2026-06-29 batch)

A 6-source batch that deepened the **synthetic-users / digital-twins** cluster and opened an **AI-companion** thread (run as a verified multi-agent workflow: fetch → adversarial fact-check → concept synthesis):

- **Digital-twin respondents — productized vs. home-built.** [[concepts/ux-research/digital-twin-respondents|Digital-Twin Respondents]] is the Type-5 (individual-replica) end of the [[concepts/ux-research/synthetic-user-taxonomy|synthetic-user taxonomy]], now evidenced from both ends: Brox sells ~60,000 standing twins as instant survey panels ([[sources/brox-digital-twins-market-research|VentureBeat]] — *vendor-PR; body unreadable, numbers unvalidated, `llm_ready: false`*), while an [[concepts/ux-research/in-house-synthetic-user-pipeline|in-house blueprint]] ([[sources/voiceofuser-inhouse-digital-twins-blueprint|The Voice of User]]) shows a team can build the same Type 4–5 panel itself ("a digital twin *is* a system prompt"). The decisive evidence: the blueprint's baseline ladder (random 0.63 / empty 0.73 / demographics 0.75 / **full twins 0.75**) shows rich grounding may **not beat demographics on individual accuracy** — concrete proof that *grounding richness ≠ accuracy*, and validation (MAE vs real humans, under-dispersion 154/164) is the real deliverable. This sharpens [[concepts/ux-research/synthetic-survey-data|synthetic survey data]], [[concepts/ux-research/grounded-synthetic-personas|grounded personas]], [[concepts/ux-research/say-do-gap|the say-do gap]], and [[concepts/ux-research/algorithmic-monoculture|algorithmic monoculture]].
- **AI companions as a business-model spectrum.** Kakao Ventures ([[sources/kakao-vc-ai-companion-relationship|relationship depth → BM]], companion to the 06-25 [[sources/kakao-vc-ai-input-modality|input-modality]] piece) seeds an agent-experience sub-cluster (consolidated 6→4): [[concepts/agent-experience/ai-companion|AI Companion]], [[concepts/agent-experience/relationship-architecture|Relationship Architecture]] (relationship depth as a design surface → revenue scale — now also home to the revenue-surface / IP & fandom monetization thesis), [[concepts/agent-experience/parasocial-relationship|Parasocial Relationship]], and the safety counterweight [[concepts/agent-experience/companion-attachment-dependency|Companion Attachment & Dependency]] (it's a VC thesis with thin hard data).
- **AI-UX practice & theory.** [[sources/uxfolio-ai-ux-design|UXfolio]] reframes the designer from execution to curation ([[concepts/ux-research/ai-native-ux-design|AI-native UX design]]; vendor/promotional — framework, not evidence), and the DRS2026 theory paper [[sources/drs2026-generative-events-design-ontology|Yu & Zhao]] proposes [[concepts/ux-research/generative-events|generative events]] as the ontological unit fusing participatory + co-design (abstract-only capture). An off-theme tool listing, [[sources/opencut-open-source-video-editor|OpenCut]], was captured light.

## Design Systems for Agents & Agentic Orchestration (Christine Vallaure, 2026-06-29 batch)

Four Christine Vallaure (moonlearning.io) articles deepened the **design-system-as-machine-instructions** thread and added a no-code orchestration angle:

- **The design system becomes the agent's contract.** [[sources/christinevallaure-agentic-ai-design-systems|"Agentic AI, Design Systems & Figma"]] reframes a design system as *"instructions for a machine,"* with a concrete six-part Figma pre-flight (three-layer variables, exact prop/name parity, full state matrix, Slots, token-based auto-layout, [[concepts/infrastructure-dev/figma-code-connect|Code Connect]]) — feeding [[concepts/infrastructure-dev/ai-native-design-system|AI-native design system]], [[concepts/infrastructure-dev/design-to-code-workflow|design-to-code]], and [[concepts/infrastructure-dev/agentic-technical-debt|the import-vs-reimplement debt lever]]. Two new token-layer primitives sit underneath: [[concepts/infrastructure-dev/hypertokens|Hypertokens]] (named style bundles compiling to many targets — *coined by Jake Albaugh at Config 2026*, not Vallaure) and the [[concepts/infrastructure-dev/component-catalog|component catalog]].
- **Generative UI, bounded.** [[sources/christinevallaure-a2ui-generative-ui|"A2UI Under the Hood"]] introduces the [[concepts/agent-experience/a2ui-protocol|A2UI protocol]] (Google-initiated): interfaces assembled fresh per request, but **only** from a designer-authored [[concepts/infrastructure-dev/component-catalog|component catalog]] — the catalog is the security boundary and the quality ceiling, sharpening [[concepts/ux-research/generative-ui|generative UI]] and [[concepts/infrastructure-dev/deterministic-ui|deterministic UI]].
- **The no-code orchestration floor.** [[sources/christinevallaure-human-approach-agentic-ai|"A Human Approach to Agentic AI"]] (n=1) shows a non-coder running a five-[[concepts/ai-agents/persona-agent|persona-agent]] book operation from a single CLAUDE.md via Cowork — [[concepts/ai-agents/markdown-agent-orchestration|markdown agent orchestration]] as the extreme case of [[concepts/product-management/domain-expert-as-builder|domain-expert-as-builder]] ("the only skill is having a human conversation"), with "be honest, not helpful" as a [[concepts/agent-experience/ai-sycophancy|counter-sycophancy]] move and a milder [[concepts/agent-experience/parasocial-relationship|parasocial over-trust]] caveat.
