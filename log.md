---
type: log
status: active
created: 2026-06-12
updated: 2026-06-12
tags: [log, operations, llm-wiki]
sources: []
confidence: 1.0
---

# Operations Log

Append-only chronological log for structural vault changes. Detailed generated checks live in [[wiki/logs/lint-report|Lint Report]] and durable maintenance notes live in [[wiki/logs/change-log|Change Log]].

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
