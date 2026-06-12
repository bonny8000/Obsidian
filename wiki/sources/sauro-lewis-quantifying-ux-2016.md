---
type: source
status: active
created: 2026-06-10
tags: [source, book, quant-ux, statistics, ux-research]
sources: []
updated: 2026-06-12
ingest_level: deep
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.95
---

# Quantifying the User Experience: Practical Statistics for User Research (2nd ed.)

> [!info] Metadata
> - **Author:** Jeff Sauro & James R. Lewis
> - **Date:** 2016 (2nd edition), Morgan Kaufmann / Elsevier
> - **Type:** book (PDF, 354 pages)
> - **ISBN:** 978-0-12-802308-2
> - **Raw File:** [[raw/files/sauro-lewis-quantifying-the-user-experience-2e.pdf]]
> - **Note:** Downloaded filename incorrectly credited "Professor of Religious Studies James R Lewis" — that is a different person. This author is Jim Lewis, senior human factors engineer at IBM, co-editor of the Journal of Usability Studies.

## Summary

The reference text for applying statistics to small-sample UX research. Unlike general statistics textbooks, every method is framed around a practical UX decision: estimating a completion rate, comparing two designs, choosing a sample size, or picking a standardized questionnaire. Chapter 1 provides decision maps that route a research question to the right statistical test — useful as a standalone playbook.

Chapter structure:

1. Introduction and how to use this book (decision maps for choosing tests)
2. Quantifying user research (data types, populations vs. samples, central tendency)
3. How precise are our estimates? Confidence intervals (incl. adjusted-Wald for small-sample completion rates)
4. Did we meet or exceed our goal? (one-sample tests against benchmarks)
5. Is there a statistical difference between designs? (two-sample comparisons, within vs. between subjects)
6. What sample sizes do we need? Part 1: summative studies
7. What sample sizes do we need? Part 2: formative studies (problem-discovery model, p = 0.31, "magic number 5" debate)
8. Standardized usability questionnaires (SUS, PSSUQ, CSUQ, SUPR-Q, UMUX, NPS)
9. Six enduring controversies in measurement and statistics
10. Correlation, regression, and ANOVA

## Key Claims

- Small samples (n < 20) are usable for statistical inference if the right methods are chosen — adjusted-Wald intervals, exact tests, and t-tests are robust at typical usability-study sizes. (conf 0.95)
- Confidence intervals are more informative than point estimates for UX metrics; report them by default. (conf 0.95)
- Sample size for formative (problem-finding) studies follows a probabilistic discovery model — the "5 users" heuristic is a special case, not a law. (conf 0.9)
- SUS is the most widely used standardized questionnaire; scores can be interpreted against normative grades/percentiles. (conf 0.9)
- Method choice should be driven by the decision at stake (benchmark vs. comparison vs. estimation), not by statistical tradition. (conf 0.9)

## Concepts Linked

Existing pages this source strengthens (add backlinks on deep ingest):

- [[concepts/ux-research/ux-metrics|UX Metrics]]
- [[concepts/ux-research/self-reported-ux-metrics|Self-Reported UX Metrics]]
- [[concepts/ux-research/ux-performance-benchmarking|UX Performance Benchmarking]]
- [[concepts/ux-research/quant-uxr-rigor|Quant UXR Rigor]]
- [[concepts/ux-research/quant-uxr-learning-path|Quant UXR Learning Path]]

Concept pages created from deep ingest (2026-06-10, ch. 1, 3, 6–8):

- [[concepts/ux-research/adjusted-wald-confidence-interval|Adjusted-Wald Confidence Interval]]
- [[concepts/ux-research/sample-size-for-usability-studies|Sample Size for Usability Studies]]
- [[concepts/ux-research/problem-discovery-model|Problem Discovery Model]]
- [[concepts/ux-research/standardized-usability-questionnaires|Standardized Usability Questionnaires]]
- [[concepts/ux-research/ux-statistics-decision-map|UX Statistics Decision Map]]

Remaining backlog: ch. 4–5 (benchmark and comparison tests), ch. 9 (six controversies), ch. 10 (correlation/regression/ANOVA).

## Useful Examples

- Current example source: use examples, tables, cases, or named artifacts already present elsewhere in this note; otherwise return to `raw/files/sauro-lewis-quantifying-the-user-experience-2e.pdf` before asking an LLM for concrete examples.

## Constraints / Caveats

- Coverage is `substantial` and ingest level is `deep`; do not treat this source as fully digested unless `coverage: full`.
- Claims should be checked against `raw/files/sauro-lewis-quantifying-the-user-experience-2e.pdf` when used for recommendations, metrics, or external-facing work.

## Citation

- Source record: `Quantifying the User Experience: Practical Statistics for User Research (2nd ed.)`.
- Raw evidence: `raw/files/sauro-lewis-quantifying-the-user-experience-2e.pdf`.

## Reliability Notes

- Coverage is `substantial` and ingest level is `deep`; do not treat this source as fully digested unless `coverage: full`.
- Claims should be checked against `raw/files/sauro-lewis-quantifying-the-user-experience-2e.pdf` when used for recommendations, metrics, or external-facing work.

> [!warning] Caveats
> - Primary, authoritative source; both authors are leading figures in quant UX (MeasuringU; IBM/JUS).
> - 2016 edition — predates AI-moderated research; pair with [[sources/measuringu-ai-usability-problem-analysis-video|MeasuringU AI analysis]] material for current practice. A 3rd edition exists; check for updated guidance before citing exact procedures.
> - Copyrighted book: keep only summaries and short excerpts in the wiki, full text stays in `raw/`.

## Design Implications

- Use this source to shape research design, UX evidence, method selection, and evaluation prompts.
- Connect it with [[concepts/ux-research/ux-metrics]], [[concepts/ux-research/self-reported-ux-metrics]], [[concepts/ux-research/ux-performance-benchmarking]], [[concepts/ux-research/quant-uxr-rigor]] before turning it into a project recommendation.

## Tensions

- Backfill note: source-specific tensions were not separately extracted in the earlier ingest. Compare this source with related concepts and maps before treating its framing as settled.

## Open Questions

- What evidence, examples, or counterexamples should be extracted from the raw source before marking this as `coverage: full`?
- Which linked concept would change most if this source were contradicted?

## LLM Use

- **Use for:** research design, UX evidence, method selection, and evaluation prompts.
- **Do not use for:** unsupported exact claims beyond the source note's `substantial` coverage.
- **Best prompt pattern:** Ask the LLM to combine this source with its linked concepts, then verify any specific claim against the raw source before final use.

## Backfill Status

- Retrofitted on 2026-06-12 by `scripts/backfill_llm_ready.py` from the existing source note.
- This standardizes the note for LLM use; it does not by itself mean the raw source has been fully re-read.
