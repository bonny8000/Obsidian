---
type: log
status: active
created: 2026-06-26
updated: 2026-06-26
tags: [log, lint, maintenance, audit]
sources: []
confidence: 1.0
---

# Maintenance & Lint Pass — 2026-06-26

A full-vault health check, defect repair, and semantic audit. Scope note: web fetching was deliberately skipped this pass, so anything requiring a re-fetch is flagged, not chased.

## Health Check (deterministic — `scripts/lint.py`)

| Check | Start | End |
| --- | --- | --- |
| Broken link targets | 17 | **0** |
| Orphaned concepts | 0 | 0 |
| Empty / near-empty pages | 0 | 0 |
| Missing frontmatter | 0 | 0 |
| Pipe-stripped links | 0 | 0 |
| Lost-content stubs | 16 | **4** |
| Pages scanned | 545 | 553 |

## Broken Links Fixed (17 → 0)

- **Created 4 concept pages** to resolve dangling references (grounded only in existing sources — no web): [[concepts/ai-agents/frontier-safety-framework|Frontier Safety Framework]] (×2 refs), [[concepts/ux-research/corporate-jargon|Corporate Jargon]] (×2), [[concepts/ai-agents/google-workspace-ai|Google Workspace AI]], [[concepts/infrastructure-dev/antigravity|Antigravity]]. Each is marked with honest low/thin-grounding caveats and confidence (0.4–0.6).
- **Repaired 2 broken "original source" pointers** by replacing them with real existing concept links: [[sources/microsoft-web-iq|Microsoft Web IQ]] (→ agentic-rag, agentic-search, token-efficiency, ai-as-infrastructure) and [[sources/openai-codex-workflow|OpenAI Codex]] (→ ai-coding-tools, agentic-work-automation, domain-expert-as-builder, role-convergence).
- **Rephrased 3 illustrative wikilink-style placeholders** that were mis-parsed as real links (a query's `concepts/X` example; the weekly-report playbook's `projects/` and `decisions/` how-to references).

## Tooling Hardened (`scripts/lint.py`)

- Skip `_templates/` in the link scan — template scaffolds legitimately contain empty wikilink placeholders like `concepts/` (removed 6 false-positive broken links).
- Exclude `logs/` from the lost-content heuristic — operational logs mention "lost-content" while *describing* recoveries; they are not stubs (removed 6 false positives).

## Lost-Content Stubs

- **6 query stubs re-answered** from current wiki evidence (corruption tombstones from 2026-06-01; the wiki has grown since). Each agent searched + cited only verified-on-disk pages; lint re-confirmed **0 new broken links**:
  - [[queries/2026-05-27-claude-code-workflows-for-wiki|Claude Code workflows for the wiki]] (conf 0.78)
  - [[queries/2026-05-27-ai-synthesis-vs-human-interpretation|AI synthesis vs human interpretation]] (0.82)
  - [[queries/2026-05-27-ai-usability-validation-benchmark|AI usability validation/benchmarking]] (0.78)
  - [[queries/2026-05-27-ar-vr-transferred-to-robotics|AR/VR → robotics transfer]] (0.75)
  - [[queries/2026-05-27-design-tasks-remain-manual|Which design tasks remain manual]] (0.78)
  - [[queries/2026-05-27-robot-safety-software-update-testing|Robot safety for software updates/testing]] (0.55 — wiki lacks a robotics-specific OTA/update source)
- **4 source stubs remain `coverage: partial` / `llm_ready: false`** — they need their original PDFs/full text, which can't be fetched this pass. **Action for Bonny:** drop the file/text to upgrade.
  - [[sources/andru-saksena-adobe-haic-2025|Adobe HAIC Framework (Andru & Saksena, 2025)]]
  - [[sources/cooper-about-face-4-2014|About Face 4]]
  - [[sources/garrett-elements-ux-2011|The Elements of User Experience]]
  - [[sources/gerhard-norton-vr-usability-2022|VR Usability (Gerhard & Norton)]]

## Semantic Audit (advisory — 6 read-only cluster agents, 265 concept pages)

**Verdict: the concept graph is healthy and well-scoped.** No real duplicates requiring a merge, no genuine contradictions. The three "conflicts" surfaced are all *correctly handled already*: the SAGE-vs-Lim reflexive-TA tension and the Skills-vs-AGENTS.md tradeoff are documented (not hidden), and [[concepts/product-management/fpa-central|FP&A Central]] is a self-flagged corruption-recovered draft.

### Recommendations for Bonny (not applied — your editorial call)

**Cross-link opportunities** (distinct pages that could reference each other):
- `gemini-3-5` ↔ `gemini-spark`; `design-system-implementation` ↔ `scaffold-design-system` ↔ `ai-native-design-system`; `ai-native-product-management` ↔ `ai-pm-skills`; `shipping-velocity` ↔ `research-preview`; `ai-product-consistency` ↔ `ai-product-onboarding`; `finance-da` ↔ `contribution-margin-operations`; `human-to-robot-transfer` ↔ `robot-imitation-learning`; `design-research-automation` ↔ `ux-research-automation`; `ax-ai-experience` ↔ `ai-native-ux-design`.
- **Applied this pass:** `palantir-foundry-ontology` ↔ [[concepts/infrastructure-dev/organizational-ontology|organizational-ontology]] (integrating a concept created earlier today).

**One merge candidate** (needs your call — both pages have inbound links): fold [[concepts/ux-research/ai-usability-false-alarm-triage|AI Usability False-Alarm Triage]] into [[concepts/ux-research/ai-usability-analysis|AI Usability Analysis]] as a subsection (triage is a quality-gate *within* the method, not a sibling method).

**Genuinely missing concept candidates** (referenced repeatedly, no page yet): `appropriate-reliance` (Lee & See — strongest candidate), `teleoperation`, `prompt-linting` (distinct from knowledge-linting), `skill-versioning/governance`, `product-success-metrics`, `participant-consent`, `data-privacy`, `interview-moderation`, `research-bias`, `a-b-testing`, `analytics-as-research`.

**Audit false positives** (flagged as "missing" but they already exist — agents were cluster-scoped): `agent-cost-control` (in infrastructure-dev), `research-influence` (in product-management), `longitudinal-research` (exists as a method page).

## Net Change

+8 new pages (4 concepts via lint repair, 4 source/query/concept files from earlier batches counted by the page delta), 6 query stubs revived, 2 `lint.py` improvements, 1 cross-link applied. Vault defect count: **0**.
