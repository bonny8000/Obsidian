---
type: source
status: active
created: 2026-06-10
updated: 2026-06-10
tags: [source, book, quant-ux, statistics, ux-research]
sources: []
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

## 🎯 Summary

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

## 💎 Key Claims

- Small samples (n < 20) are usable for statistical inference if the right methods are chosen — adjusted-Wald intervals, exact tests, and t-tests are robust at typical usability-study sizes. (conf 0.95)
- Confidence intervals are more informative than point estimates for UX metrics; report them by default. (conf 0.95)
- Sample size for formative (problem-finding) studies follows a probabilistic discovery model — the "5 users" heuristic is a special case, not a law. (conf 0.9)
- SUS is the most widely used standardized questionnaire; scores can be interpreted against normative grades/percentiles. (conf 0.9)
- Method choice should be driven by the decision at stake (benchmark vs. comparison vs. estimation), not by statistical tradition. (conf 0.9)

## 🧠 Concepts Extracted

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

## ⚠️ Reliability Notes

> [!warning] Caveats
> - Primary, authoritative source; both authors are leading figures in quant UX 