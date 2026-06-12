---
type: source
status: active
created: 2026-05-27
tags: [source, book, quant-ux, ux-research, career]
sources: []
updated: 2026-06-12
ingest_level: deep
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.92
---

# Quantitative User Experience Research

> [!info] Metadata
> - **Author:** Chris Chapman & Kerry Rodden (ex-Google Quant UXR; Rodden is the originator of the HEART framework)
> - **Date:** 2023, Apress
> - **Type:** book (PDF, 384 pages), ISBN 978-1-4842-9268-6
> - **Raw File:** [[raw/files/chapman-rodden-quant-uxr-2023.pdf]]
> - **History:** original deep-ingest page lost in the 2026-05/06 corruption; rebuilt 2026-06-12 from the full PDF.

## Citation

Chapman, C. & Rodden, K. (2023). *Quantitative User Experience Research: Informing Product Decisions by Understanding Users at Scale*. Apress. PDF preserved in raw/files. Re-ingested 2026-06-12.

## Summary

The definition of Quant UXR as a discipline and career, written by the people who built the role at Google. Distinct from the other two quant books in the vault: Sauro & Lewis teaches the statistics, Tullis & Albert catalogs the metrics, and this book explains the role — what a quant UX researcher does, the skill triad it requires, and how the function operates inside product organizations. Authoritative home of the HEART framework and the Goals-Signals-Metrics process.

Part structure:

- Part I: Getting Started (ch. 1-3) — what Quant UXR is, how it relates to general UX research, overview of the role
- Part II: Core Skills (ch. 4-6) — the skill triad: UX research foundations, statistics, programming (R/SQL-centric)
- Part III: Tools and Techniques (ch. 7-10) — Metrics of UX including the HEART framework (7.1) and Goals-Signals-Metrics process (7.2); customer satisfaction surveys; log sequence visualization; MaxDiff for prioritizing features and needs
- Part IV: Organizations and Careers (ch. 11-15) — UX org models, interviews and job postings, research processes and stakeholder reporting, career development, future of the discipline

## Key Claims

- Quant UXR sits at the intersection of three skills — research methods, statistics, and programming — and the role's value is the combination, not depth in any single one. (conf 0.95)
- HEART (Happiness, Engagement, Adoption, Retention, Task success) gives product teams a metric vocabulary spanning attitudinal and behavioral signals. (conf 0.95)
- Goals-Signals-Metrics is the derivation discipline: start from product goals, identify observable signals, only then define metrics — preventing metric-first cargo culting. (conf 0.95)
- Log/behavioral data analysis is a first-class research method, not just analytics support; sequence visualization reveals behavior patterns surveys cannot. (conf 0.85)
- MaxDiff outperforms rating scales for prioritization because it forces trade-offs instead of allowing everything to be rated important. (conf 0.9)

## Useful Examples

- Ch. 7's HEART × Goals-Signals-Metrics worksheet structure is directly reusable for defining platform-level metrics.
- Ch. 12-13's interview cases and stakeholder-reporting patterns double as career-development material for moving toward quant-leaning roles.

## Constraints / Caveats

- Programming material is R-centric; translation needed for Python-first environments.
- Written from a large-org (Google-scale) perspective; smaller teams need to collapse the role boundaries it describes.
- Deep ingest covers TOC plus chapters 1-3, 7, 10 at working depth; remaining chapters at survey depth.

## Design Implications

- Derive metrics through Goals-Signals-Metrics before opening any dashboard tool; the process is the deliverable.
- Use HEART as the category checklist when proposing platform metrics, then route statistical rigor to Sauro & Lewis.
- Treat behavioral log analysis as a research method with research questions, not as passive monitoring.

## Tensions

- HEART's engagement category can conflict with calibrated-trust goals in agent products: maximizing engagement is not the same as appropriate reliance — see [[concepts/agent-experience/trust-calibration|Trust Calibration]].

## Open Questions

- How should HEART be extended or reweighted for proactive-agent products where less interaction can mean more value?

## Concepts Linked

- [[concepts/ux-research/heart-framework|HEART Framework]]
- [[concepts/ux-research/quant-uxr-role-identity|Quant UXR Role Identity]]
- [[concepts/ux-research/quant-uxr-learning-path|Quant UXR Learning Path]]
- [[concepts/ux-research/quant-uxr-rigor|Quant UXR Rigor]]
- [[concepts/ux-research/behavioral-sequence-analysis|Behavioral Sequence Analysis]]
- [[concepts/ux-research/ux-metrics|UX Metrics]]
- [[methods/maxdiff-prioritization|MaxDiff Prioritization]]
- [[methods/surveys-and-standardized-metrics|Surveys and Standardized Metrics]]

## LLM Use

- **Use for:** HEART and Goals-Signals-Metrics grounding, quant UXR role/career questions, metric-derivation process, MaxDiff rationale.
- **Do not use for:** verbatim R code (not extracted) or statistical test selection (route to Sauro & Lewis).
- **Best prompt pattern:** Give the LLM a product goal and ask it to run Goals-Signals-Metrics from this source, propose HEART-category metrics, then hand sample-size and test design to [[sources/sauro-lewis-quantifying-ux-2016|Sauro & Lewis]].

## Reliability Notes

> [!warning] Caveats
> 2023, current, and authoritative for the discipline; org-design advice assumes large-company structures.

## Backfill Status

- Chapters 4-6, 8-9, 11-15 available in raw PDF for deeper extraction on demand.
