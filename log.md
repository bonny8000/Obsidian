---
type: log
status: active
created: 2026-06-12
updated: 2026-06-17
tags: [log, operations, llm-wiki]
sources: []
confidence: 1.0
---

# Operations Log

Append-only chronological log for structural vault changes. Detailed generated checks live in [[wiki/logs/lint-report|Lint Report]] and durable maintenance notes live in [[wiki/logs/change-log|Change Log]].

## 2026-06-17

- **MeasuringU 5-pack ingest.** Five Sauro/Lewis articles on UX research methodology captured to `raw/web/` and published as source pages, with five new concepts and three updated existing concepts:
  - [[wiki/sources/measuringu-tac10-screening|TAC-10 for Screening and Data Cleaning]] → new concepts [[wiki/concepts/ux-research/tac-10-tech-savviness|TAC-10 Tech Savviness]] and [[wiki/concepts/ux-research/survey-data-quality-screening|Survey Data Quality Screening]].
  - [[wiki/sources/measuringu-synthetic-users-review|A Review of Experiments with Synthetic Users]] (12-paper review) → updated [[wiki/concepts/ux-research/synthetic-survey-data|Synthetic Survey Data]] with empirical evidence (9 encouraging vs 14 discouraging findings; 21% replication on classic psych studies).
  - [[wiki/sources/measuringu-credible-vs-confidence-intervals|Credible vs Confidence Intervals]] → new concept [[wiki/concepts/ux-research/bayesian-credible-interval|Bayesian Credible Interval]]; updated [[wiki/concepts/ux-research/adjusted-wald-confidence-interval|Adjusted-Wald CI]] with the "likely range" / "plausible range" stakeholder phrasings.
  - [[wiki/sources/measuringu-bayes-priors-uxr|Bayes' Law — The Power and Perils of Priors]] → new concept [[wiki/concepts/ux-research/bayesian-priors-in-uxr|Bayesian Priors in UXR]] capturing the disclose/sensitivity-test/collect-more discipline.
  - [[wiki/sources/measuringu-banner-tables|How to Use Banner Tables]] → new concept [[wiki/concepts/ux-research/banner-table|Banner Table]] with use/avoid criteria and Skill-candidate framing.
- Updated [[wiki/maps/ux-metrics-framework|UX Metrics Framework]] map with Bayesian small-sample section, Survey Quality and Reporting section, and all 5 new source citations. Confidence 0.84 → 0.86.
- Updated `wiki/index.md` and root `index.md` Recent Ingests with the MeasuringU 5-pack.

- Ingested Christley & Radford (2026): "Atlassian Design System: Building the context engine for the AI era" — the strategic-framing companion to the DESIGN.md case study. Captured to `raw/web/atlassian-design-system-context-engine-2026-06-17.md` and created [[wiki/sources/atlassian-design-system-context-engine|source page]] (ingest_level: standard, coverage: substantial, llm_ready: true).
- Created new concept [[wiki/concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]] capturing the four-pillar maturity model (AI can understand it / build with it / contribute patterns to it / maintain it) and the **Context Engine** stack (foundations + tokens + components + context layer of structured content / MCP / skills / templates / DESIGN.md).
- Cross-linked [[wiki/concepts/infrastructure-dev/design-md|DESIGN.md]] to the new AI-Native Design System concept and added the Christley & Radford source.
- Updated `wiki/overview.md` to reference the AI-Native Design System maturity model and Context Engine framing.
- Updated `wiki/index.md` (Recent Ingests + AI Design and Agents cluster) and root `index.md` (Recent Ingests) with the new companion pair.

- Ingested Hall & Campbell (2026): "Atlassian's DESIGN.md is here — what we learned testing portable design context in practice" from the Atlassian Blog. Captured raw web copy to `raw/web/atlassian-design-md-2026-06-17.md`.
- Created [[wiki/sources/atlassian-design-md|Atlassian: DESIGN.md — Portable Design Context in Practice]] (ingest_level: standard, coverage: substantial, llm_ready: true) with the full production benchmark table (no context / ADS MCP / ADS skill / DESIGN.md on a log-in screen task), the three structural limitations, and the four jobs DESIGN.md is right for.
- New concept [[wiki/concepts/infrastructure-dev/design-md|DESIGN.md]] sits beside [[wiki/concepts/ai-agents/agent-skills|Agent Skills]], [[wiki/concepts/ai-agents/mcp-integration|MCP Integration]], and [[wiki/concepts/infrastructure-dev/claudemd-context|AGENTS.md / CLAUDE.md]] as a fourth context primitive (portable always-on design intent).
- Extended [[wiki/comparisons/skills-vs-mcp-vs-agents-md|Skills vs MCP vs AGENTS.md]] into a four-primitive comparison with a new DESIGN.md row, three new routing heuristics, and an Atlassian source-evidence pointer.
- Updated [[wiki/overview|Knowledge Base Overview]] to reflect the four-primitive routing decision.
- Updated `wiki/index.md` (Recent Ingests + AI Design and Agents cluster) and root `index.md` (Recent Ingests).

- Ingested Singhal et al. (2026): "Agent Skills" (Day 3). Copied PDF to `raw/Agent-Skills-Day-3.pdf` and read end-to-end via pdftotext.
- Created [[wiki/sources/agent-skills-day-3|Agent Skills (Day 3)]] source page (ingest_level: deep, coverage: full, llm_ready: true) covering Skill anatomy, progressive disclosure, four failure modes, five-pattern evaluation toolkit, Read/Draft/Act ladder, meta-skills four buckets, DAG orchestration, Capability Profiles, canonical skill taxonomy, marketplace trust defaults, Google Agents CLI worked example, and retail case study.
- New concept pages: [[wiki/concepts/ai-agents/agent-skills|Agent Skills]] (the format primitive), [[wiki/concepts/ai-agents/progressive-disclosure|Progressive Disclosure]] (3-level loading), [[wiki/concepts/ai-agents/context-rot|Context Rot]] (silent context-overflow failure mode), [[wiki/concepts/ai-agents/procedural-memory|Procedural Memory]] (memory typology completing episodic + semantic + procedural).
- New comparison: [[wiki/comparisons/skills-vs-mcp-vs-agents-md|Skills vs MCP vs AGENTS.md]] with routing heuristics and the Day-3 one-line mental model.
- Updated [[wiki/concepts/ai-agents/skill-system|Skill System]] with Day-3 evidence (procedural memory framing, evaluation toolkit, Read/Draft/Act ladder); raised confidence 0.85 → 0.9.
- Updated [[wiki/concepts/ai-agents/agent-memory|Agent Memory]] with procedural memory bullet; confidence 0.72 → 0.78.
- Updated [[wiki/concepts/ai-agents/self-improving-agent-workflows|Self-Improving Agent Workflows]] with Day-3 four-bucket meta-skill taxonomy and the three habits; confidence 0.80 → 0.84.
- Updated [[wiki/overview|Knowledge Base Overview]] with an "Agentic Engineering Series" section tying Day 1 + Day 2 + Day 3.
- Updated `wiki/index.md` (Recent Ingests + AI Design and Agents cluster) and root `index.md` (Recent Ingests).
- Fixed root `README.md` so it points to `D:\Obsidian\LLM-Wiki` instead of a stale `C:\Users\bonny_chen\LLM-Wiki` path.

## 2026-06-16

- Ingested Patlolla et al. (2026): "Agent Tools & Interoperability". Created [[wiki/sources/agent-tools-interoperability-day-2|Agent Tools & Interoperability]] summarizing MCP, A2A, A2UI, AP2, and UCP protocols.
- Ingested Osmani et al. (2026): "The New SDLC With Vibe Coding". Created [[wiki/sources/the-new-sdlc-with-vibe-coding-day-1|The New SDLC With Vibe Coding]] from provided OCR and archived PDF in raw.
- Added a detailed raw/source refresh for MeasuringU's n >= 30 statistics article and created [[wiki/playbooks/small-n-ux-statistics-checklist|Small-N UX Statistics Checklist]].
- Updated the Quant UXR graph around sample size, adjusted-Wald intervals, UX statistics routing, surveys/metrics, UX metrics framework, LLM-ready source index, and index entries.

## 2026-06-12

- Moved the vault to `D:\Obsidian\LLM-Wiki`.
- Cleaned Git metadata and normalized line endings before using Git as version backup/audit.
- Backfilled source pages with LLM-readiness metadata and standardized sections.
- Added UX research workspace structure modeled after the research-vault schema: methods, comparisons, analyses, overview, catalog, and operating schema.
- Ingested AX LABS memory contamination, Figma design taste, and MeasuringU n >= 30 statistics articles into raw source cards, source pages, concepts, maps, and index entries.

## 2026-06-12 - Agent Experience cluster and method library expansion

- Fixed 98 files with mojibake headings (`# ?`) and BOM characters from earlier encoding loss.
- Added `wiki/concepts/agent-experience/` with 8 concept notes: proactivity-design, trust-calibration, agent-transparency, initiative-and-interruption, error-recovery, collaboration-patterns, mental-model-onboarding, agent-evaluation-ux. All marked with honest confidence (0.55-0.65) pending empirical source ingestion.
- Added `wiki/maps/agent-experience-design.md` as the AX cluster entry point, linking new concepts to existing foundations (ax-ai-experience, haic-modalities-taxonomy, designing-for-agency, agent-memory).
- Added 8 method pages closing the gap-audit list: diary-studies, field-studies, concept-testing, card-sorting, tree-testing, benchmark-studies, longitudinal-research, plus wizard-of-oz-testing for agent interaction research.
- Updated root `index.md` with an Agent Experience Workspace section and the new method links.
- Next: ingest empirical AX sources (Lee & See trust calibration, Horvitz mixed-initiative, Amershi et al. human-AI guidelines) to promote cluster confidence above 0.7.

## 2026-06-12 - Foundational AX source ingest and cluster promotion

- Ingested three foundational empirical sources into raw/web/ and wiki/sources/: lee-see-2004-trust-in-automation, horvitz-1999-mixed-initiative, amershi-2019-human-ai-guidelines. Lee & See and Horvitz captured at coverage: partial (full text paywalled; ingested from abstracts plus secondary literature); Amershi at coverage: standard (paper abstract plus Microsoft Design announcement and HAX Toolkit). All marked llm_ready: true with explicit do-not-use-for boundaries.
- Promoted all 8 agent-experience concept notes: confidence raised from 0.55-0.65 to 0.70-0.80, stale "no ingested sources" caveats replaced with grounded caveats, one source-grounded key claim added per note, and body Sources sections added.
- Updated wiki/maps/agent-experience-design.md: confidence 0.65 -> 0.78, added an Evidence Base section, narrowed the gap list to recent agent-UX field studies.
- Updated root index.md Recent Ingests.
- Remaining promotion path: obtain full PDFs for Lee & See and Horvitz to move coverage from partial to full.   

## 2026-06-12 - Quant UXR book trio: full-PDF ingest and corruption recovery

- User supplied full PDFs for three foundational quant UXR books; all preserved in raw/files/: tullis-albert-measuring-ux-2e-2013.pdf, chapman-rodden-quant-uxr-2023.pdf (sauro-lewis PDF already present from the 2026-06-10 ingest; duplicate upload discarded).
- Rebuilt the two corruption-stub source pages from the actual books: tullis-albert-measuring-ux-2013 (metric taxonomy, ch-level map, ten-myths playbook) and chapman-rodden-quant-uxr-2023 (skill triad, HEART, Goals-Signals-Metrics, MaxDiff). Both promoted: status draft -> active, coverage partial -> substantial, llm_ready true, raw_preserved true, confidence 0.6 -> 0.92.
- Cross-linked the trio with explicit division of labor: Sauro & Lewis = statistics engine, Tullis & Albert = metric taxonomy, Chapman & Rodden = role and metric-derivation process.
- Remaining backfill: deeper extraction of survey-depth chapters on demand (noted per source page).
