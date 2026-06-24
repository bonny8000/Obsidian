---
type: log
status: active
created: 2026-06-12
updated: 2026-06-22
tags: [log, operations, llm-wiki]
sources: []
confidence: 1.0
---

# Operations Log

Append-only chronological log for structural vault changes. Detailed generated checks live in [[wiki/logs/lint-report|Lint Report]] and durable maintenance notes live in [[wiki/logs/change-log|Change Log]].

## 2026-06-22

- **14-source AI × UX / agentic-engineering batch ingest.** Captured 14 web sources to `raw/web/` and published source pages in `wiki/sources/`. 11 fetched fully (`coverage: substantial`, `llm_ready: true`); 3 are partial stubs (`llm_ready: false`) pending access.
  - Design-system AI prototyping: [[wiki/sources/atlassian-ai-prototyping-handshakes|Atlassian: Handoffs into Handshakes]] (companion to the existing Context Engine + DESIGN.md pages), [[wiki/sources/figma-mcp-server-four-ways|Figma: 4 Ways We're Using Our MCP Server]], [[wiki/sources/aidesign-guide-catalog|The AI Design Guide]] (light / resource directory).
  - Agentic reliability (Thoughtworks/martinfowler.com): [[wiki/sources/bayer-prince-reliable-agentic-ai|Bayer PRINCE]] (deep) and [[wiki/sources/fowler-sensors-coding-agents|Böckeler: Maintainability Sensors]] (deep).
  - Stanford HAI preprint write-ups: [[wiki/sources/hai-cooperbench-agent-teamwork|CooperBench: Agents Fail at Teamwork]] and [[wiki/sources/hai-headlines-ai-news-audit|Audit of Six News Chatbots]].
  - UXR & human-AI: [[wiki/sources/nngroup-design-process-compressed|NN/g: Process Compressed]], [[wiki/sources/guanjie-li-llm-user-proxy|Li: LLM User Proxies]] (deep), [[wiki/sources/trevor-calabro-ux-research-as-a-service|Calabro: Research as a Service]], [[wiki/sources/ada-kim-satisfaction-vs-benefit-ai|Kim: Satisfaction vs Benefit]].
  - Partial stubs (flagged for follow-up): [[wiki/sources/kevin-newton-uxr-three-jobs|Newton (LinkedIn, login-walled)]], [[wiki/sources/acm-dis2026-algorithmic-self-portraits|ACM DIS 2026 (title unverified)]], [[wiki/sources/ipsos-trust-ultimate-wireframe|Ipsos (Ceros report not rendered)]].
- Created 13 new concept pages and backlinked each to its anchor source: [[wiki/concepts/ai-agents/context-engineering|Context Engineering]], [[wiki/concepts/ai-agents/agentic-rag|Agentic RAG]], [[wiki/concepts/ai-agents/multi-agent-coordination|Multi-Agent Coordination]], [[wiki/concepts/ai-agents/ai-news-intermediary|AI as News Intermediary]], [[wiki/concepts/infrastructure-dev/maintainability-sensor|Maintainability Sensor]], [[wiki/concepts/infrastructure-dev/mutation-testing|Mutation Testing]], [[wiki/concepts/infrastructure-dev/agentic-content|Agentic Content]], [[wiki/concepts/infrastructure-dev/ai-prototyping|AI Prototyping]], [[wiki/concepts/ux-research/llm-user-proxy|LLM User Proxy]], [[wiki/concepts/ux-research/research-as-a-service|Research as a Service]], [[wiki/concepts/ux-research/process-literacy|Process Literacy]], [[wiki/concepts/agent-experience/ai-sycophancy|AI Sycophancy]], [[wiki/concepts/agent-experience/satisfaction-vs-benefit|Satisfaction vs Benefit]].
- Updated [[wiki/maps/llm-ready-source-index|LLM-Ready Source Index]] (74 → 88 sources, 58 → 69 `llm_ready`) and [[wiki/maps/ai-ux-research-methods|AI UX Research Methods]] map (added UXR sources + concepts).
- Updated [[wiki/overview|Knowledge Base Overview]] (new "AI × UX and Agentic Reliability" section + counts), `wiki/index.md`, and root `index.md` Recent Ingests.
- Deferred to future ingest (left as `(new)`/`(future)` notes, not created): reflection-loops, text-to-sql, hybrid-retrieval, computational-vs-inferential-sensors, self-correction-guidance, design-code-round-trip, socioaffective-alignment, ai-over-reliance, question-well-posedness, opt-in-approach. The 3 partial sources await an authenticated/rendered re-capture.
- **Same-day update:** Bonny supplied Newton's full article text and the ACM DIS 2026 PDF. Both upgraded from partial stubs to **full ingests** (`coverage: partial → substantial`, `llm_ready: false → true`; ACM `confidence 0.3 → 0.85`). ACM PDF preserved at `raw/files/lee-2026-tubelens-algorithmic-self-portraits-dis2026.pdf`. Confirmed the ACM title/authors: *Is This the Real Me? — Algorithmic Self-Portraits (TubeLens)*, Lee et al., UNIST. New concepts [[wiki/concepts/ux-research/uxr-role-split|UXR Role Split]] (Newton's three roles) and [[wiki/concepts/ux-research/algorithmic-self|Algorithmic Self]] (Lee et al.). Updated [[wiki/maps/llm-ready-source-index|source index]] (69 → 71 `llm_ready`; 20 → 18 partial) and the [[wiki/maps/ai-ux-research-methods|AI UX Research Methods]] map. Only Ipsos remains partial.
- **Day 4 & Day 5 ingest (Agentic Engineering series finale).** Bonny supplied two Google whitepaper PDFs — [[wiki/sources/vibe-coding-agent-security-evaluation-day-4|Day 4 — Vibe Coding Agent Security & Evaluation]] (Kartakis et al.) and [[wiki/sources/spec-driven-production-development-day-5|Day 5 — Spec-Driven Production-Grade Development]] (Boonstra) — both preserved in `raw/` and written as deep source pages (`coverage: substantial`, `llm_ready: true`), completing the Day 1–5 arc. Six new concepts: [[wiki/concepts/ai-agents/agent-security-architecture|Agent Security Architecture]], [[wiki/concepts/ai-agents/red-blue-green-agent-teaming|Red/Blue/Green Agent Teaming]], [[wiki/concepts/ai-agents/slopsquatting|Slopsquatting]], [[wiki/concepts/ai-agents/vibe-coding-agent-evaluation|Vibe-Coding Agent Evaluation]], [[wiki/concepts/ai-agents/spec-driven-development|Spec-Driven Development]], [[wiki/concepts/ai-agents/zero-trust-agent-development|Zero-Trust Agent Development]]. Extended [[wiki/overview|Overview]]'s Agentic Engineering Series section to Day 1–5; source index 88 → 90 (71 → 73 `llm_ready`).
- **UX-research & product batch (5 sources).** Ingested two Saeideh Bakhshi Substack pieces ([[wiki/sources/bakhshi-representative-sample|representative-sample / claim-based sampling]], [[wiki/sources/bakhshi-ai-in-qualitative-research-map|the five-axis AI-in-qualitative-research map]]), [[wiki/sources/svenja-pieritz-positioning-experiment|Pieritz's positioning experiment]] (relevance vs purchase intent), the [[wiki/sources/myrealtrip-polaris-cancellation-recommendation|Myrealtrip "Polaris"]] cancellation-recommendation case, and a partial [[wiki/sources/yozm-ai-prd|Yozm AI-PRD]] stub (JS-blocked). Five new concepts: [[wiki/concepts/ux-research/claim-based-sampling|Claim-Based Sampling]], [[wiki/concepts/ux-research/ai-qualitative-research-map|AI Qualitative Research Map]], [[wiki/concepts/ux-research/say-do-gap|Say-Do Gap]], [[wiki/concepts/product-management/feature-vs-platform|Feature vs Platform]], [[wiki/concepts/product-management/ai-prd|AI PRD]]. Source index 90 → 95 (73 → 77 `llm_ready`); updated overview, both indexes, and the AI-UX-Research-Methods map.
- **Yozm AI-PRD upgraded to full** (same day): Bonny supplied a Chinese summary of the JS-rendered article, so [[wiki/sources/yozm-ai-prd|the source page]] moved `partial → substantial` / `llm_ready → true` (the 8 PRD items, the Eval pyramid, regression-testing / "prompt swamp", and the three pricing models), and the [[wiki/concepts/product-management/ai-prd|AI PRD]] concept went `draft → active` (confidence 0.6 → 0.8). Source index `llm_ready` 77 → 78; partial 19 → 18.
- **LangChain agent-engineering batch (8 posts).** Ingested 8 LangChain blog posts via 3 parallel sub-agents: [[wiki/sources/langchain-multi-agent-architecture|multi-agent architecture]], [[wiki/sources/langchain-loop-engineering|loop engineering]], [[wiki/sources/langchain-custom-agent-harness|custom agent harness]], [[wiki/sources/langchain-verifiers-legal-agents|verifiers for legal agents]], [[wiki/sources/langchain-predictable-coding-agent-spend|predictable agent spend]], [[wiki/sources/langchain-model-neutrality|model neutrality]], [[wiki/sources/langchain-box-ai-deep-agents|Box deep agents]], [[wiki/sources/langchain-lyft-support-agent-platform|Lyft self-serve platform]]. Eight new concepts: multi-agent-architecture, loop-engineering, agent-middleware, agent-verifiers, model-neutrality, agent-cost-control, deep-agents, self-serve-agent-platform. **Images:** LangChain figures have no alt-text, so diagram content was captured from surrounding prose/captions/tables; one genuine gap flagged — Lyft's baseline-eval-metrics table exists only in a screenshot. Cross-linked to [[wiki/sources/bayer-prince-reliable-agentic-ai|Bayer PRINCE]] (same LangGraph/LangSmith stack) and [[wiki/sources/hai-cooperbench-agent-teamwork|CooperBench]] (the multi-agent coordination-gap tension). Source index 95 → 103 (78 → 86 `llm_ready`).
- **LangChain batch 2 (7 posts).** Ingested via 3 parallel sub-agents: [[wiki/sources/langchain-agent-middleware|agent middleware]] (the LangChain-1.0 origin post — added as canonical source to the [[wiki/concepts/ai-agents/agent-middleware|Agent Middleware]] concept), [[wiki/sources/langchain-background-subagents|background/async subagents]], [[wiki/sources/langchain-interpreter-skills|interpreter skills]], [[wiki/sources/langchain-agent-authorization|two types of agent authorization]], [[wiki/sources/langchain-eu-ai-act|LangSmith & the EU AI Act]], [[wiki/sources/langchain-evaluating-deep-agents|evaluating deep agents]], [[wiki/sources/langchain-exa|Exa agentic search]]. Six new concepts: agent-authorization, async-subagents, agent-interpreter, agent-trajectory-evaluation, agentic-search, eu-ai-act-compliance. Enriched the [[wiki/concepts/ai-agents/deep-agents|Deep Agents]] concept with the eval post. Authorization + EU-AI-Act cross-linked to [[wiki/sources/vibe-coding-agent-security-evaluation-day-4|Day 4]] (Confused Deputy, Governance pillar). Source index 103 → 110 (86 → 93 `llm_ready`).

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
