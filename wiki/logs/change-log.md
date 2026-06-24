---
type: log
status: active
created: 2026-05-18
updated: 2026-06-17
tags: [log, maintenance]
sources: []
confidence: 1.0
---

# Change Log

## 2026-06-17 - MeasuringU 5-pack ingest

Sources captured to `raw/web/`:

- `measuringu-tac10-screening-2026-06-17.md` — Lewis & Sauro, 2026-06-02.
- `measuringu-synthetic-users-review-2026-06-17.md` — Lewis & Sauro, 2026-04-14.
- `measuringu-credible-vs-confidence-intervals-2026-06-17.md` — Sauro & Lewis, 2026-04-08.
- `measuringu-bayes-priors-uxr-2026-06-17.md` — Sauro & Lewis, 2026-03-31.
- `measuringu-banner-tables-2026-06-17.md` — Lewis & Sauro, 2026-03-24.

- Created five source pages under `wiki/sources/` with full LLM-ready sections (key claims, useful examples, constraints, design implications, tensions, open questions, concepts linked, LLM use, reliability notes).
- New concepts:
  - [[concepts/ux-research/bayesian-credible-interval|Bayesian Credible Interval]] — Bayesian binary-outcome interval; near-identical numbers to adjusted-Wald under non-informative priors, different interpretation. Includes the four-method comparison table from the source.
  - [[concepts/ux-research/bayesian-priors-in-uxr|Bayesian Priors in UXR]] — captures the five-scenario sensitivity demonstration and the discipline of disclose / sensitivity-test / collect-more.
  - [[concepts/ux-research/tac-10-tech-savviness|TAC-10 Tech Savviness]] — instrument plus its Guttman-pattern data-cleaning role (87% plausible / <0.5% implausible).
  - [[concepts/ux-research/survey-data-quality-screening|Survey Data Quality Screening]] — the layered 8-method checklist with AI-fraud framing.
  - [[concepts/ux-research/banner-table|Banner Table]] — the market-research stub-and-banner format with use/avoid criteria and Skill-candidate framing.
- Updated existing concepts:
  - [[concepts/ux-research/synthetic-survey-data|Synthetic Survey Data]] — added the Lewis & Sauro 12-paper review (9 encouraging vs 14 discouraging findings; 21% replication on classic psych studies; shallow-extension trap in interviews); confidence 0.74 → 0.82.
  - [[concepts/ux-research/adjusted-wald-confidence-interval|Adjusted-Wald Confidence Interval]] — added the "likely range" / "plausible range" stakeholder phrasings from the credible-vs-CI source, plus a cross-link to the new Bayesian credible interval concept.
- Updated [[maps/ux-metrics-framework|UX Metrics Framework]] map with a Bayesian section, a Survey Quality and Reporting section, and citations to all five new MeasuringU sources. Confidence 0.84 → 0.86.
- Updated `wiki/index.md` and root `index.md` Recent Ingests.

## 2026-06-17 - Web ingest: Atlassian Context Engine (companion to DESIGN.md)

Source: `raw/web/atlassian-design-system-context-engine-2026-06-17.md` (Christley & Radford, Atlassian Blog, 2026-05-28)

- Captured Maria Christley (Head of Design, ADS) and Rachel Radford (Design Manager, ADS) framing piece into `raw/web/`. This is the strategic companion to the DESIGN.md case study ingested earlier today.
- Created [[sources/atlassian-design-system-context-engine|Atlassian: Building the Context Engine for the AI Era]] with full LLM-ready sections including the four-pillar AI-native definition, the expanded Context Engine infra stack, reported impact numbers (52% accuracy / 34% faster / 26% fewer calls / 16% fewer tokens — methodology not disclosed), the Core / Platform / App composition model and its evolution into a "constellation," and concrete artifact stories (date-time picker accessibility redesign, 1.5-pixel-stroke icon system, 5-token motion system, Panel component).
- Created [[concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]] concept with the four-pillar self-assessment maturity model and the Context Engine stack diagram.
- Updated [[concepts/infrastructure-dev/design-md|DESIGN.md]] concept to cross-link the new AI-Native Design System concept and the Christley & Radford companion source.
- Updated [[overview|Knowledge Base Overview]] with the Context Engine framing and AI-Native Design System maturity model.
- Updated `wiki/index.md` and root `index.md` with the new Recent Ingests entries and AI Design and Agents cluster links.

## 2026-06-17 (PM) - Web ingest: Atlassian DESIGN.md

Source: `raw/web/atlassian-design-md-2026-06-17.md` (Hall & Campbell, Atlassian Blog, 2026-06-15)

- Captured the Atlassian DESIGN.md blog post (Kylor Hall, Principal Prompt Engineer; Andrew Campbell, Senior Design Technologist) into `raw/web/`.
- Created [[sources/atlassian-design-md|Atlassian: DESIGN.md — Portable Design Context in Practice]] with full LLM-ready sections including the four-row benchmark table (no context / ADS MCP / ADS skill / DESIGN.md), the three structural limitations of DESIGN.md in production (loads everything every turn; shortening kills sophistication; teaches re-implementation, not adoption), and the four jobs DESIGN.md is right for (high-level artistic direction; quick prototyping; tool interoperability; customer theming).
- Added new concept [[concepts/infrastructure-dev/design-md|DESIGN.md]] as a fourth context primitive (portable, always-on, brand-intent) beside Agent Skills, MCP, and AGENTS.md.
- Extended [[comparisons/skills-vs-mcp-vs-agents-md|Skills vs MCP vs AGENTS.md]] into a four-primitive comparison with a DESIGN.md row in the matrix, an updated recommendation pattern, three new routing heuristics (one-shot vs production, re-implementation canary, missing-context canary), and an Atlassian source citation.
- Updated [[overview|Knowledge Base Overview]] with the four-primitive routing decision and the Atlassian production data point.
- Updated `wiki/index.md` and root `index.md` Recent Ingests, plus the AI Design and Agents cluster.

## 2026-06-17 - Deep ingest: Agent Skills (Day 3)

Source: `raw/Agent-Skills-Day-3.pdf` (Singhal, Hernandez Larios, Dus, Nigam, Kolan, May 2026; curated by Shubham Saboo)

- Copied user-supplied PDF from `D:\Bonny_Files\Downloads\Agent Skills_Day_3.pdf` to `raw/Agent-Skills-Day-3.pdf` and read end-to-end with `pdftotext -layout` (1,661 lines).
- Created [[sources/agent-skills-day-3|Agent Skills (Day 3)]] source page with deep ingest (ingest_level: deep, coverage: full, llm_ready: true, confidence: 0.92). Covers Skill anatomy + the two authoring paths, progressive disclosure with token math, four failure modes (Trigger / Execution / Token Budget / Regression), the five-pattern Evaluation Toolkit, EDD with a refund-skill JSON case, the Read/Draft/Act graduation ladder + pass^k, eval coverage gate, "98.4% operational infrastructure" Claude Code reverse-engineering claim, context overflow vs Lost in the Middle vs Context Rot, meta-skills four buckets, DAG orchestration + Capability Profiles + Canonical Skill Taxonomy, Context Debt and "Shift Intelligence Left", architectural tradeoffs table, skill source trust defaults, Google Agents CLI worked example, retail case study with read/draft/act ladder applied.
- Added new concepts:
  - [[concepts/ai-agents/agent-skills|Agent Skills]] — the format primitive (folder + SKILL.md + scripts/references/assets), the five rules, skill smells, minimal template.
  - [[concepts/ai-agents/progressive-disclosure|Progressive Disclosure]] — three-level loading model, token math, decoupling available vs active capability.
  - [[concepts/ai-agents/context-rot|Context Rot]] — silent context-overflow failure mode, Lost in the Middle + Chroma Research findings, three practical implications.
  - [[concepts/ai-agents/procedural-memory|Procedural Memory]] — completing the episodic/semantic/procedural typology for LLM agents.
- Added comparison [[comparisons/skills-vs-mcp-vs-agents-md|Skills vs MCP vs AGENTS.md]] — decision matrix, recommendation pattern, routing heuristics, and the Day-3 one-line mental model.
- Updated [[concepts/ai-agents/skill-system|Skill System]] with Day-3 evidence and links to the four new concepts; confidence 0.85 → 0.9.
- Updated [[concepts/ai-agents/agent-memory|Agent Memory]] with the procedural-memory bullet linking the new concept; confidence 0.72 → 0.78.
- Updated [[concepts/ai-agents/self-improving-agent-workflows|Self-Improving Agent Workflows]] with Day-3's four-bucket meta-skill taxonomy and the three habits that hold up; confidence 0.80 → 0.84.
- Updated [[overview|Knowledge Base Overview]] with a new "Agentic Engineering Series (Day 1 + Day 2 + Day 3)" section.
- Updated [[index|LLM Wiki Index]] and root `index.md` with the new Recent Ingests entries and AI Design and Agents cluster links.
- Out-of-scope housekeeping done in the same session: fixed the root `README.md` so it points to the actual D:\ vault path instead of stale C:\Users\bonny_chen\LLM-Wiki.

## 2026-06-16 - Detailed ingest: MeasuringU n >= 30 statistics

Source: `raw/web/measuringu-statistics-30-participants-2026-06-16-detailed.md`

- Added a detailed raw evidence card for [[sources/measuringu-statistics-30-participants|MeasuringU: Do Statistics Really Require 30 Participants?]] using Defuddle extraction and web verification.
- Promoted the source page from standard/substantial to detailed/detailed coverage.
- Rebuilt the connected small-n statistics notes: [[concepts/ux-research/sample-size-for-usability-studies|Sample Size for Usability Studies]], [[concepts/ux-research/adjusted-wald-confidence-interval|Adjusted-Wald Confidence Interval]], and [[concepts/ux-research/ux-statistics-decision-map|UX Statistics Decision Map]].
- Added [[playbooks/small-n-ux-statistics-checklist|Small-N UX Statistics Checklist]] for responding to stakeholder claims that statistics require 30 participants.
- Updated [[methods/surveys-and-standardized-metrics|Surveys and Standardized Metrics]], [[maps/ux-metrics-framework|UX Metrics Framework]], [[maps/llm-ready-source-index|LLM-Ready Source Index]], [[index|LLM Wiki Index]], and root `index.md`.

## 2026-06-12 - Ingest: memory contamination, design taste, and n >= 30 statistics

Sources: `raw/web/theaxlabs-contaminated-memory-performance-2026-06-12.md`, `raw/web/figma-you-never-stop-cultivating-taste-2026-06-12.md`, `raw/web/measuringu-statistics-30-participants-2026-06-12.md`

- Created source pages for [[sources/theaxlabs-contaminated-memory-performance|AX LABS: Contaminated Memory Eats Away Performance]], [[sources/figma-you-never-stop-cultivating-taste|Figma: You Never Stop Cultivating Taste]], and [[sources/measuringu-statistics-30-participants|MeasuringU: Do Statistics Really Require 30 Participants?]].
- Created [[concepts/ai-agents/memory-contamination|Memory Contamination]] and updated [[concepts/ai-agents/agent-memory|Agent Memory]] with memory lifecycle and contamination controls.
- Updated [[concepts/product-management/product-taste|Product Taste]] with Figma's taste-as-care and AI-era craft framing.
- Updated Quant UXR concepts and [[methods/surveys-and-standardized-metrics|Surveys and Standardized Metrics]] with the MeasuringU n >= 30 guidance.
- Updated [[maps/ai-design-agent-workflows|AI Design Agent Workflows]], [[maps/ai-native-product-management|AI-Native Product Management]], [[maps/ux-metrics-framework|UX Metrics Framework]], [[maps/ai-ux-research-methods|AI UX Research Methods]], root `index.md`, [[index|LLM Wiki Index]], and root `log.md`.

## 2026-06-12 - UX research workspace schema

- Expanded `CLAUDE.md` into a full operating schema inspired by the reference research-vault structure.
- Added root `index.md`, root `log.md`, and [[overview|Knowledge Base Overview]] as first-class vault entrypoints.
- Added `wiki/methods/`, `wiki/comparisons/`, and `wiki/analyses/` with reusable templates.
- Seeded UX research method pages for usability testing, semi-structured interviews, surveys and standardized metrics, MaxDiff prioritization, reflexive thematic analysis, and AI-assisted research synthesis.
- Added [[comparisons/research-method-selection-matrix|Research Method Selection Matrix]], [[comparisons/ai-assisted-research-risk-matrix|AI-Assisted Research Risk Matrix]], and [[analyses/ux-research-wiki-gap-audit-2026-06-12|UX Research Wiki Gap Audit]].
- Updated `AGENTS.md`, `dashboard.base`, and [[index|LLM Wiki Index]] so future ingests update source, concept, method, comparison, and analysis layers together.

## 2026-06-12 - LLM-ready source backfill

- Added LLM-readiness fields to source records: `ingest_level`, `coverage`, `llm_ready`, and `raw_preserved`.
- Updated `wiki/_templates/source.md` and `AGENTS.md` so future ingests distinguish light, standard, and deep coverage.
- Added `scripts/backfill_llm_ready.py` to retrofit existing source pages and regenerate [[maps/llm-ready-source-index|LLM-Ready Source Index]].
- Backfilled all 68 existing `wiki/sources/` pages with LLM-ready sections: key claims, useful examples, constraints/caveats, design implications, tensions, open questions, LLM use, reliability notes, and backfill status.
- Updated [[maps/llm-wiki-architecture|LLM Wiki Architecture]], `dashboard.base`, and [[index|LLM Wiki Index]] to surface LLM-ready sources and sources needing deeper ingest.

## 2026-06-10 - Phase 1+2: lint tooling, Sauro & Lewis deep ingest, research agenda, dashboards

- Created `scripts/lint.py` (broken links, pipe-stripped links, empty pages, frontmatter, orphans, lost-content stubs) → [[logs/lint-report|Lint Report]]. Fixed 19 more broken links it caught (digit-prefixed titles, mojibake'd emoji links, 2 wrong targets); 17 remain (4 missing concept pages + template placeholders), listed in the report.
- Deep-ingested Sauro & Lewis ch. 1, 3, 6–8: created [[concepts/ux-research/adjusted-wald-confidence-interval|Adjusted-Wald CI]], [[concepts/ux-research/sample-size-for-usability-studies|Sample Size for Usability Studies]], [[concepts/ux-research/problem-discovery-model|Problem Discovery Model]], [[concepts/ux-research/standardized-usability-questionnaires|Standardized Usability Questionnaires]], [[concepts/ux-research/ux-statistics-decision-map|UX Statistics Decision Map]]. Updated source page and [[maps/ux-metrics-framework|UX Metrics Framework]]. Remaining backlog: ch. 4–5, 9–10.
- Created [[maps/research-agenda|Research Agenda]] (85 open questions harvested from all concept pages) + `scripts/harvest_questions.py` to regenerate it.
- Extended `dashboard.base` with views: Drafts, Low Confidence, Lost Content, Stale (60 days).
- Updated [[index|LLM Wiki Index]] map list.

## 2026-06-10 - Phase 0 Repair: git, broken links, corrupted pages

- Initialized git version control with baseline commit of pre-repair state. Added `.gitignore`.
- Fixed 590 pipe-stripped wikilinks (alias pipe removed, path fused with title) across 125 files via script with dry-run verification.
- Rebuilt all 25 corrupted/empty pages: 5 fully from `raw/`, 3 from backlink context, 6 as citation stubs needing re-ingest, 11 as tombstones. Details in [[logs/2026-06-10-corruption-recovery|Corruption Recovery Log]].
- Created [[projects/llm-wiki-improvement-plan|LLM Wiki Improvement Plan]] (Phases 0–3).

## 2026-06-10 - Ingest: Sauro & Lewis, Quantifying the User Experience (2nd ed.)

Source: `raw/files/sauro-lewis-quantifying-the-user-experience-2e.pdf` (copied from Downloads, renamed from corrupted original filename)

- Copied book PDF (354 pp.) into `raw/files/`.
- Created [[sources/sauro-lewis-quantifying-ux-2016|Quantifying the User Experience (2016)]] source page with chapter map, key claims, and deep-ingest backlog (candidate concepts: adjusted-Wald CI, sample size for usability studies, standardized questionnaires, problem-discovery model).
- Deep ingest of individual chapters deferred — tracked in the source page under "Candidate new concept pages".
- Noted during ingest: [[maps/ux-metrics-framework]] and [[sources/tullis-albert-measuring-ux-2013]] contain only `---` (corrupted/empty) — flagged for repair.

## 2026-06-10 - Ingest: MeasuringU, Quant UXR Resources, QuantUX, and Meta Research

Sources: `raw/web/measuringu-ai-real-ui-problems-hallucinations-2026-05-26.md`, `raw/web/carl-pearson-quant-uxr-self-study-resources-2025-02-17.md`, `raw/web/quantuxblog-source-collection-2026-06-10.md`, `raw/web/meta-research-medium-publication-2016-2023.md`

- Created source pages for the new MeasuringU hallucination follow-up, Carl Pearson quant UXR self-study guide, Quantitative UX Research Blog, and Meta Research Medium publication.
- Created concept pages for [[concepts/ux-research/ai-usability-false-alarm-triage|AI Usability False-Alarm Triage]], [[concepts/ux-research/quant-uxr-learning-path|Quant UXR Learning Path]], [[concepts/ux-research/quant-uxr-rigor|Quant UXR Rigor]], and [[concepts/ux-research/synthetic-survey-data|Synthetic Survey Data]].
- Updated [[concepts/ux-research/ai-usability-analysis|AI Usability Analysis]] and [[concepts/ux-research/quant-uxr-role-identity|Quant UXR Role Identity]].
- Updated [[maps/ai-ux-research-methods|AI UX Research Methods]], [[index|LLM Wiki Index]], and this change log.

## 2026-06-08 - Ingest: Saeideh Bakhshi, The Long Accommodation

Source: `raw/web/saeidehbakhshi-long-accommodation-2026-06-07.md`

- Created `wiki/sources/saeidehbakhshi-long-accommodation.md`.
- Created `wiki/concepts/ux-research/validity-and-decision-relevance.md`.
- Updated `methodological-integrity`, `reliability-vs-validity`, `research-strategy`, `research-operations`, `wicked-research-scoping`, `research-methods-foundations`, and `ai-evals`.
- Updated `wiki/maps/ai-ux-research-methods.md`, `wiki/index.md`, and this change log.

## 2026-06-08 - Ingest: Saeideh Bakhshi, Wicked Work and AI-Unbundled Research

Source: `raw/web/saeidehbakhshi-wicked-work-ai-research-2026-05-10.md`

- Created `wiki/sources/saeidehbakhshi-wicked-work-ai-unbundles-research.md`.
- Created `wiki/concepts/ux-research/wicked-research-scoping.md`.
- Updated `methodological-integrity`, `human-interpretation`, `senior-ux-researcher`, and `research-strategy`.
- Updated `wiki/maps/ai-ux-research-methods.md`, `wiki/index.md`, and this change log.

## 2026-06-08 - Ingest: pxd Color Tokens and LinkedIn Participant Selection

Sources: `raw/web/pxd-color-token-design-2026-05-18.md`, `raw/web/linkedin-user-selection-criteria-2026-05-14.md`

- Created `wiki/sources/pxd-color-token-design-2026.md` and `wiki/concepts/infrastructure-dev/color-token-architecture.md`.
- Created `wiki/sources/linkedin-user-selection-criteria.md` and `wiki/concepts/ux-research/participant-selection-criteria.md`.
- Updated `design-system-implementation`, `scaffold-design-system`, `deterministic-ui`, `ai-recruitment`, and `research-operations` with backlinks.
- Updated `wiki/maps/ai-ux-research-methods.md` and `wiki/index.md`.

## 2026-06-08 - Ingest: Conjointly Research Methods Knowledge Base

Source: `raw/web/conjointly-research-methods-kb/`

- Captured 127 table-of-contents links from the Conjointly-hosted Research Methods Knowledge Base into raw Markdown files.
- Created `wiki/sources/conjointly-research-methods-kb.md` as the collection source page.
- Created `wiki/maps/research-methods-knowledge-base.md` as the navigable method map.
- Created `wiki/concepts/ux-research/research-methods-foundations.md` as the umbrella methodology concept.
- Updated `wiki/maps/ai-ux-research-methods.md` and `wiki/index.md` to link the new source and map.

## 2026-06-05 — Ingest: How To AI UXR (The ResearchOps Review, 2026)

Source: `raw/how-to-ai-uxr-2026.pdf`

- **Created** `wiki/sources/how-to-ai-uxr-2026.md` — source page for the maturity matrix.
- **Created** `wiki/concepts/ux-research/ai-uxr-maturity-matrix.md` — Crawl, Walk, Run framework.
- **Created** `wiki/concepts/ux-research/agentic-research-workflows.md` — shift to workflow ownership.
- **Created** `wiki/concepts/ux-research/ai-evals.md` — system evaluation and quality control.
- **Updated** `wiki/concepts/ux-research/grounded-synthetic-personas.md` — integrated "Vibe Checks" context.
- **Updated** `wiki/maps/ai-ux-research-methods.md` — added the new concepts to the map.

## 2026-06-05 — Ingest: Research That Scales (Kate Towsey, 2024)

Source: `raw/research-that-scales-towsey-2024.pdf`

- **Created** `wiki/sources/research-that-scales-towsey-2024.md` — source page for the Research Operations handbook.
- **Created** `wiki/concepts/ux-research/research-operations.md` — defined ResearchOps as the "power to act."
- **Created** `wiki/concepts/ux-research/research-strategy.md` — blueprint for value delivery.
- **Created** `wiki/concepts/ux-research/eight-elements-of-research-ops.md` — core framework of interconnected components.
- **Created** `wiki/concepts/ux-research/operational-maturity-phases.md` — progression from Build to KTLO.
- **Created** `wiki/concepts/ux-research/pwdr.md` — People Who Do Research cohort.
- **Created** `wiki/concepts/ux-research/rkm-model.md` — Research Knowledge Management model.
- **Created** `wiki/concepts/ux-research/respect-in-research-trifecta.md` — Ethics, Data Governance, and Data Privacy synchronization.
- **Updated** `wiki/concepts/ux-research/research-ethics.md` — integrated "Respect in Research" and legal vs. ethical distinctions.
- **Updated** `wiki/maps/ai-ux-research-methods.md` — added ResearchOps cluster and concepts.
- **Updated** `wiki/index.md` — added "Research Operations and Strategy" topic cluster.

## 2026-06-03 — Ingest: User Interviews AI Assistant

Source: `raw/2026-06-03-user-interviews-ai-assistant.md`

- **Created** `wiki/sources/user-interviews-ai-assistant.md`
- **Created** `wiki/concepts/ux-research/ai-recruitment.md` — new concept: prompt-based targeting and automated screening.
- **Created** `wiki/concepts/ux-research/ai-analysis.md` — new concept: grounded insight exploration and session breakdowns.
- **Updated** `wiki/concepts/ux-research/ux-research-automation.md` — added User Interviews as a key example of recruitment/analysis automation.
- **Updated** `wiki/concepts/ai-agents/mcp-integration.md` — noted the strategic move of exposing research context via MCP.
- **Created** `wiki/logs/2026-06-03-ingest-report.md` — detailed report of the ingestion actions and findings.

## 2026-06-01 — Evolution: Notion Synchronization Pipeline Completed

- **Phase 1 (Anchor Sync):** Synced all active and completed projects from the Notion "Projects" database into `wiki/projects/`. Injected tasks from the "Todo List" database into the corresponding project pages (e.g., `openclaw-rog-pitch.md`).
- **Phase 2 (Insight Extraction):** Extracted meeting notes from the "Meetings" database. Created a new Decision Record (`wiki/decisions/evaluation-ux-ai.md`) detailing the "Workflow Timeline" and "UX Specs vs Figma" agreements.
- **Phase 3 (Playbook Construction):** Queried the "Skills" database for active tools. Generated new playbooks: `wiki/playbooks/weekly-report.md` and `wiki/playbooks/mentor-analysis.md`.
- **Global Context:** The Wiki is now fully populated with the user's first-party data, bridging the gap between theoretical UX/PM knowledge and actual daily operations.

## 2026-06-01 — Evolution: Project Operating System Activation

- **Updated** `AGENTS.md` ??redefined the vault contract to include `wiki/projects/` and `wiki/decisions/`. Added a new **Project Workflow** for proactive work integration.
- **Created** `wiki/_templates/project-template.md` and `wiki/_templates/decision-record.md` ??standardizing how work is documented and linked to theory.
- **Updated** `wiki/index.md` ??added a new "?? Active Work" dashboard section to surface ongoing projects and decisions.
- **Created** `wiki/projects/` and `wiki/decisions/` directories.

## 2026-06-01 ??Ingest: NN/g, Research Recommendations and the Roadmap

Source: `raw/research-recommendations-roadmap.md` (Nielsen Norman Group article)

- **Created** `wiki/sources/nngroup-research-recommendations-roadmap.md`
- **Created** `wiki/concepts/research-influence.md` ??new concept: ability of UX research to shape product strategy and priorities.
- **Created** `wiki/concepts/usability-debt.md` ??new concept: accumulation of UX issues/friction, framed as risk.
- **Created** `wiki/concepts/product-roadmap.md` ??new concept: the source of truth for product direction and prioritization.
- **Created** `wiki/concepts/ux-metrics.md` ??new concept: quantitative measures used to evaluate UX and align with business KPIs.
- **Created** `wiki/concepts/discovery-phase.md` ??new concept: early product development stage for problem framing and user understanding.
- **Updated** `wiki/maps/ai-ux-research-methods.md` ??added the new concept and source.
- **Updated** `wiki/maps/ai-native-product-management.md` ??added the new concepts and source.
- **Updated** `wiki/index.md` ??integrated new concepts into PM and UXR clusters.

## 2026-06-01 ??Ingest: Brunch, Gemini Spark

Source: `raw/web/brunch-ghidesigner-497.md` (Blog post by Prof. Yoo Hoon-sik)

- **Created** `wiki/sources/brunch-ghidesigner-497.md`
- **Created** `wiki/concepts/gemini-spark.md` ??new concept: Google's "always-on" agentic AI unveiled at I/O 2026.
- **Updated** `wiki/concepts/agentic-ai.md` ??added Gemini Spark as a production example of agentic AI.

## 2026-06-01 ??Ingest: Saeideh Bakhshi, The Fallacy of Depth at Scale

Source: `raw/2026-06-01-the-fallacy-of-depth-at-scale.md` (Substack article)

- **Created** `wiki/sources/saeidehbakhshi-the-fallacy-of-depth-at-scale.md`
- **Created** `wiki/concepts/ai-moderated-interviews.md` ??new concept: AI-moderated interviews as a new affordance with specific limits (misses the unsaid, inherits fluency skew, doesn't measure prevalence).
- **Updated** `wiki/maps/ai-ux-research-methods.md` ??added the new concept and source to the map.

## 2026-05-28 ??Ingest: Hariz Lim, AI in Qualitative Research

Source: `raw/web/medium-harizlim-ai-qualitative-research-2026-05-10.md` (Medium, captured as summary ??paywall)

- **Created** `wiki/sources/medium-harizlim-ai-qualitative-research-2026.md`
- **Created** `wiki/concepts/ai-as-thinking-partner.md` ??new concept: AI as structured sparring partner rather than analyst; practitioner counterpoint to the SAGE rejection position
- **Updated** `wiki/concepts/genai-in-qualitative-research.md` ??added Lim's claims and a Conflicts section documenting the SAGE vs. Lim tension
- **Updated** `wiki/concepts/reflexive-thematic-analysis.md` ??added Lim's "AI intensifies reflexivity" claim and Conflicts section
- **Updated** `wiki/concepts/human-interpretation.md` ??added "humans own irreplaceable context" framing and new source
- **Updated** `wiki/concepts/methodological-integrity.md` ??added "false credibility" and talent pipeline claims
- **Updated** `wiki/maps/ai-ux-research-methods.md` ??added source, new concept link, and working interpretation note on the SAGE/Lim fork

?? Capture note: Full article text not available (Medium paywall). Source confidence capped at 0.75.

## 2026-05-27 ??Orphan Wiring Pass

- Added new "?? UX Metrics & Foundational Methods" cluster to [[index|LLM Wiki Index]] with all 11 previously orphaned concepts.
- Added "Foundational UX Frameworks & Methods" section to [[maps/ai-ux-research-methods|AI UX Research Methods]] map, grouping orphans into three sub-clusters: Frameworks & Process Models, UX Metrics & Measurement, Quant UXR Methods & Role.
- ?? Flagged: 28 stub files found across wiki (16 concept/source/map pages + 5 log files + 7 raw stubs). These were created as empty shells by previous ingest agents on 2026-05-27. Content needs to be populated ??see [[logs/lint-report|Lint Report]] for full list.

## 2026-05-27 ??Wiki Improvement Pass

- Created `wiki/queries/` folder (was defined in AGENTS.md but never existed).
- Ran full Open Questions synthesis: found 96 open questions across 93 concept pages.
  - 72 answered with existing wiki evidence ??72 new query pages at `wiki/queries/2026-05-27-*.md`.
  - 24 left open (require external sources or personal portfolio data).
  - All concept pages updated with `[Answered ??[[queries/...]]]` backlinks.
- Ran fresh lint (previous lint was 2026-05-21, stale by 6 days and 5 ingest sessions).
  - Confirmed 7 previously broken links are now resolved.
  - Found 18 new broken links (missing concept pages) ??see [[logs/lint-report|Lint Report]].
  - Found 11 orphan concept pages in the UX Research cluster ??not yet linked from index or maps.
  - Frontmatter compliance: 100%.
- Updated [[logs/lint-report|Lint Report]] with full current state.

## 2026-06-01

- Added [[queries/2026-06-01-impressive-large-project-strategy|Impressive Large Project Strategy]] as a saved query describing project directions that can become a strong AI/UX/product portfolio system.
- Updated the project direction to avoid overfitting to Bonny's personal wiki, UX-only workflows, Figma-only workflows, or a single product category.
- Created [[projects/product-workflow-studio|Product Workflow Studio]] as the full 1-4 step product plan, including visual direction, feature modules, MVP scope, build phases, technical plan, and next tasks.

## 2026-05-25

- Ingested three new sources: [[sources/founders-playbook-2026|Founder's Playbook (2026)]], [[sources/bucketplace-2026-05-08-financial-data-lake|Unlocking Finance to the Data Lake (Bucketplace)]], and [[sources/bucketplace-2026-05-06-ai-for-designers|How Designers Use AI (Bucketplace)]].
- Created six new concept pages:
    - [[concepts/product-management/10-person-unicorn|10-Person Unicorn]]
    - [[concepts/ai-agents/orchestrator-of-agents|Orchestrator of Agents]]
    - [[concepts/infrastructure-dev/nexus-data-lake|Nexus Data Lake]]
    - [[concepts/product-management/fpa-central|FP&A Central]]
    - [[concepts/ai-agents/interactive-specs|Interactive Specs]]
    - [[concepts/ai-agents/athena-mcp|Athena MCP]]
- Updated [[index|LLM Wiki Index]] to integrate new concepts into "AI Design and Agents" and "AI-Native Product Management" clusters.
- Added raw content to `raw/web/` for source provenance.

## 2026-05-18

- Created initial LLM Wiki vault structure.
- Added `AGENTS.md` and `CLAUDE.md` operating instructions.
- Added source card for the Brunch LLM Wiki article.
- Created initial index, architecture map, source page, and concept pages.
- Added raw source cards for Brunch, NAVER LABS, Teams placeholder, and arXiv links provided by Bonny.
- Added `raw/web/source-collection-2026-05-18.md` as the collection inventory.
- Ingested the 2026-05-18 source collection into `wiki/sources/`, `wiki/concepts/`, and `wiki/maps/`.
- Created [[logs/2026-05-18-ingest-report|2026-05-18 Ingest Report]].
- Added and ingested the Bucketplace Pretendard JP article into multilingual typography/localization source, concept, and map pages.
- Added raw source cards for Manyfast, Mashdigi/AWS OpenAI Bedrock, MeasuringU AI usability analysis, SAGE GenAI/reflexive qualitative research, Brunch Gemini Enterprise, and Digital iNSIGHT Claude Design links. These are collected in `raw/web/` and not yet ingested into `wiki/`.
- Ingested the Manyfast, Mashdigi/AWS OpenAI Bedrock, MeasuringU, SAGE, Brunch Gemini Enterprise, and Digital iNSIGHT Claude Design source cards into `wiki/sources/`, `wiki/concepts/`, and `wiki/maps/`.
- Added [[maps/ai-ux-research-methods|AI UX Research Methods]] and expanded [[maps/ai-design-agent-workflows|AI Design Agent Workflows]].
- Added raw source card for Lenny's Podcast transcript link with Caitlin Kalinowski on the AI hardware boom. This is collected in `raw/web/` and not yet ingested into `wiki/`.
- Added user-provided partial transcript excerpt for the Lenny/Caitlin AI hardware episode under `raw/files/` and linked it from the raw source card.
- Ingested the Lenny/Caitlin AI hardware episode into `wiki/sources/`, hardware/robotics concept pages, and the new [[maps/ai-hardware-and-physical-ai|AI Hardware and Physical AI]] map.
- Added raw transcript capture for Cat Wu on AI-native product management, Claude Code, Cowork, evals, and agentic workflows.
- Ingested the Cat Wu transcript capture into [[sources/lennys-podcast-cat-wu-ai-pm-claude-code|Lenny's Podcast: Cat Wu on AI-Native Product Management]], 15 concept pages, and [[maps/ai-native-product-management|AI-Native Product Management]].

## 2026-05-19

- Ingested three new sources (GeekNews, Rapport Labs, pxd story) into `wiki/sources/`, `wiki/concepts/`, and created a new [[logs/2026-05-19-ingest-report|2026-05-19 Ingest Report]].
- Added new concepts: [[concepts/ux-research/contextual-translation|Contextual Translation]], [[concepts/ai-agents/ai-inspection-bot|AI Inspection Bot]], [[concepts/ai-agents/harness-engineering|Harness Engineering]], and [[concepts/product-management/geo-generative-engine-optimization|GEO (Generative Engine Optimization)]].
- Updated existing concepts: [[concepts/ai-agents/vibe-coding|Vibe Coding]], [[concepts/ux-research/human-in-the-loop|Human-in-the-loop]], and [[concepts/ai-agents/agentic-ai|Agentic AI]].

## 2026-05-20

- Added new concept: [[concepts/infrastructure-dev/modern-web-guidance|Modern Web Guidance]].
- Documented tool features, integration with AI agents, and relevance to AI product consistency.
- Updated [[index|LLM Wiki Index]] to include the new concept under AI Design and Agents.
- Ingested five new sources: MeasuringU (Senior UXR), Brunch (Agentic AI Competencies), Google I/O 2026, Gemini 3.5 Launch, and ZDNet (Dell AI-Native).
- Created new source pages for all five sources in `wiki/sources/`.
- Created/Updated concepts: [[concepts/ai-agents/agentic-ai|Agentic AI]], [[concepts/ai-agents/gemini-3-5|Gemini 3.5]], [[concepts/product-management/tokenomics|Tokenomics]], and [[concepts/ux-research/senior-ux-researcher|Senior UX Researcher]].
- Updated [[index|LLM Wiki Index]] to reflect new content across multiple topic clusters.

## 2026-05-21

- Ingested new source from Hansol Lim: [[sources/hsol-ai-portfolio-6|AI Portfolio Making (6): A Data Model for a Person]].
- Created seven new concept pages related to personal data modeling and Palantir Foundry ontology.
- Added new "Personal AI and Data Modeling" topic cluster to [[index|LLM Wiki Index]].
- Created [[logs/2026-05-21-ingest-report|2026-05-21 Ingest Report]].
- **Skill-Driven Overhaul:**
    - Installed and activated `obsidian-markdown`, `obsidian-cli`, `obsidian-bases`, and `defuddle` skills.
    - Created `dashboard.base` for structured vault visualization.
    - Redesigned [[index|LLM Wiki Index]] using Obsidian callouts and base embeds.
    - Enhanced [[concepts/infrastructure-dev/palantir-foundry-ontology|Palantir Foundry Ontology]] with Mermaid diagrams and callouts.


- **2026-05-27:** Deep ingest of Tullis &

## 2026-06-22 — AI × UX / agentic-engineering batch (14 sources)

- Ingested 14 web sources into `raw/web/` + `wiki/sources/` (11 `substantial`/`llm_ready`, 3 partial stubs). Themes: design-system AI prototyping (Atlassian, Figma), agentic reliability (Bayer PRINCE, Böckeler sensors), Stanford HAI preprints (CooperBench, six-chatbot news audit), and AI-era UXR / human-AI (NN/g process compression, Li's LLM user proxies, Calabro's research-as-a-service, Kim's satisfaction-vs-benefit).
- Added 13 concept pages (context-engineering, agentic-rag, multi-agent-coordination, ai-news-intermediary, maintainability-sensor, mutation-testing, agentic-content, ai-prototyping, llm-user-proxy, research-as-a-service, process-literacy, ai-sycophancy, satisfaction-vs-benefit), each backlinked to its source.
- Updated llm-ready-source-index (74 → 88 sources / 58 → 69 `llm_ready`), the ai-ux-research-methods map, overview, `wiki/index.md`, root `index.md`, and `log.md`.
- Partial sources (Newton/LinkedIn, ACM DIS 2026, Ipsos Ceros report) flagged for authenticated/rendered re-capture.
- **Same-day follow-up:** Newton + ACM upgraded to full ingests from user-supplied text/PDF (ACM PDF preserved in `raw/files/lee-2026-tubelens-algorithmic-self-portraits-dis2026.pdf`); added concepts `uxr-role-split` and `algorithmic-self`; source-index 69 → 71 `llm_ready`; only Ipsos remains partial.
- **Day 4 & 5 added (Agentic Engineering finale):** ingested two Google whitepapers (Day 4 security & evaluation; Day 5 spec-driven production) as deep source pages with PDFs preserved in `raw/`; added 6 concepts (agent-security-architecture, red-blue-green-agent-teaming, slopsquatting, vibe-coding-agent-evaluation, spec-driven-development, zero-trust-agent-development); overview series section now Day 1–5; source index 88 → 90 (71 → 73 `llm_ready`).
- **UX-research & product batch (5 sources):** 2× Bakhshi (claim-based sampling; five-axis AI-qual map), Pieritz positioning experiment, Myrealtrip "Polaris" case, partial Yozm AI-PRD; 5 new concepts (claim-based-sampling, ai-qualitative-research-map, say-do-gap, feature-vs-platform, ai-prd); source index 90 → 95 (73 → 77 `llm_ready`).
- **Yozm AI-PRD upgraded** to full from a user-supplied Chinese summary (8 items, Eval pyramid, regression/prompt-swamp, pricing models); ai-prd concept `draft → active`; source index `llm_ready` 77 → 78, partial 19 → 18.
- **LangChain agent-engineering batch (8 posts):** multi-agent architecture, loop engineering, custom harness, verifiers (legal), predictable spend, model neutrality, Box deep-agents, Lyft self-serve platform; 8 new concepts (multi-agent-architecture, loop-engineering, agent-middleware, agent-verifiers, model-neutrality, agent-cost-control, deep-agents, self-serve-agent-platform); diagrams captured from text (LangChain figures have no alt-text), Lyft baseline-metrics table is an image-only gap; source index 95 → 103 (78 → 86 `llm_ready`).
- **LangChain batch 2 (7 posts):** agent middleware (1.0 origin), background/async subagents, interpreter skills, agent authorization, EU AI Act, evaluating deep agents, Exa agentic search; 6 new concepts (agent-authorization, async-subagents, agent-interpreter, agent-trajectory-evaluation, agentic-search, eu-ai-act-compliance); enriched agent-middleware + deep-agents concepts with canonical sources; source index 103 → 110 (86 → 93 `llm_ready`).
