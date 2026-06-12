---
type: source
status: active
created: 2026-05-27
tags: [source, book, ux-research, metrics]
sources: []
updated: 2026-06-12
ingest_level: deep
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.92
---

# Measuring the User Experience (2nd ed.)

> [!info] Metadata
> - **Author:** Tom Tullis & Bill Albert
> - **Date:** 2013 (2nd edition), Morgan Kaufmann / Elsevier
> - **Type:** book (PDF, 320 pages), ISBN 978-0-12-415781-1
> - **Raw File:** [[raw/files/tullis-albert-measuring-ux-2e-2013.pdf]]
> - **History:** original deep-ingest page lost in the 2026-05/06 corruption; rebuilt 2026-06-12 from the full PDF.

## Citation

Tullis, T. & Albert, B. (2013). *Measuring the User Experience: Collecting, Analyzing, and Presenting Usability Metrics*, 2nd ed. Morgan Kaufmann. PDF preserved in raw/files. Re-ingested 2026-06-12.

## Summary

The standard taxonomy of UX metrics: what kinds of measures exist, when each applies, and how to collect, analyze, and present them. Where Sauro & Lewis is the statistics engine, this book is the metric catalog and study-planning layer that sits on top of it.

Chapter structure:

1. Introduction — what UX metrics are, their value, and ten myths (e.g., that metrics need big samples, big budgets, or don't apply to new products)
2. Background — data types (nominal/ordinal/interval/ratio), descriptive statistics, confidence intervals
3. Planning — matching metrics to study goals, formative vs. summative framing, budgets and timelines
4. Performance Metrics — task success, time-on-task, errors, efficiency, ease of learning
5. Issue-Based Metrics — usability problem identification, severity, frequency, and the evaluator effect
6. Self-Reported Metrics — post-task and post-study ratings; SUS in detail, including using SUS to compare designs
7. Behavioral and Physiological Metrics — observation coding, eye tracking, emotion measures
8. Combined and Comparative Metrics — single usability scores, percentile-against-goal, comparisons to benchmarks and competitors
9. Special Topics — live-site analytics, card sorting data, accessibility, ROI
10. Case Studies — applied end-to-end examples
11. Ten Keys to Success — practitioner heuristics for making metrics stick in organizations

## Key Claims

- Every UX metric falls into a small taxonomy — performance, issue-based, self-reported, behavioral/physiological, combined — and study planning is the act of matching the decision to the metric class. (conf 0.95)
- Task success is the most fundamental performance metric and can be measured at small sample sizes if reported with confidence intervals. (conf 0.9)
- Self-reported and performance measures often diverge; collecting only one gives a misleading picture. (conf 0.9)
- Issue-based metrics are subject to the evaluator effect — different evaluators find different problems — so issue counting needs multiple evaluators or explicit caveats. (conf 0.85)
- Combined scores (e.g., a single usability metric) trade diagnostic detail for executive communicability; use them for tracking, not diagnosis. (conf 0.85)

## Useful Examples

- Ch. 1's ten myths double as a stakeholder-objection playbook when proposing measurement to skeptical teams.
- Ch. 8's combined/comparative approaches map directly onto benchmark-wave reporting.

## Constraints / Caveats

- 2013 edition: pre-dates modern product analytics stacks, HEART-era metric frameworks, and AI-assisted research; live-site material in ch. 9 is dated.
- Deep ingest covers TOC plus chapters 1-2, 4-6, 8 at working depth; chapters 7, 9-11 at survey depth.

## Design Implications

- Use the metric taxonomy as the default vocabulary in study plans: name the metric class before naming the tool.
- Pair every self-reported measure with at least one performance or behavioral measure.
- Report small-sample metrics with confidence intervals by default, per ch. 2.

## Tensions

- Issue-based metrics chapter is in tension with purely metric-driven benchmarking: problems found ≠ experience quality measured. The vault treats them as complementary layers.

## Open Questions

- Which parts of the taxonomy need extension for agentic products — e.g., where do intervention rate and verification effort sit?

## Concepts Linked

- [[concepts/ux-research/ux-metrics|UX Metrics]]
- [[concepts/ux-research/self-reported-ux-metrics|Self-Reported UX Metrics]]
- [[concepts/ux-research/ux-performance-benchmarking|UX Performance Benchmarking]]
- [[concepts/ux-research/evaluator-effect|Evaluator Effect]]
- [[concepts/ux-research/standardized-usability-questionnaires|Standardized Usability Questionnaires]]
- [[methods/usability-testing|Usability Testing]]
- [[methods/benchmark-studies|Benchmark Studies]]

## LLM Use

- **Use for:** metric selection, study planning vocabulary, taxonomy grounding, benchmark reporting structure.
- **Do not use for:** current analytics tooling guidance (dated) or statistical procedures beyond descriptive level (route to Sauro & Lewis).
- **Best prompt pattern:** Given a product decision, ask the LLM to propose one metric per relevant class from this taxonomy, then route statistical design to [[sources/sauro-lewis-quantifying-ux-2016|Sauro & Lewis]].

## Reliability Notes

> [!warning] Caveats
> Authoritative and widely cited; 2013 recency limits apply to tooling chapters only, not the taxonomy.

## Backfill Status

- Chapters 7, 9-11 available in raw PDF for deeper extraction on demand.
