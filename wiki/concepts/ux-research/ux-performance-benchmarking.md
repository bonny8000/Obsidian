---
type: concept
status: active
created: 2026-06-01
updated: 2026-08-04
tags: [ux-research, benchmarking, metrics]
sources: [tullis-albert-measuring-ux-2013, saeidehbakhshi-usability-metrics-static-product]
confidence: 0.88
---

# UX Performance Benchmarking

## Summary
UX Performance Benchmarking is the systematic process of measuring the current user experience of a product to establish a baseline for future improvements or to compare against competitors.

## Key Primitives
- **Baseline Measurement:** Collecting metrics (success rate, time on task, satisfaction) on a stable version of the product.
- **Comparative Testing:** Testing the baseline against a new design or a competitor's product using the same tasks and metrics.
- **Trend Tracking:** Repeating the benchmark over time to see the impact of continuous deployments.

## Why it matters
Benchmarking turns "gut feelings" about design into measurable progress. It allows teams to say "Version B is 15% faster than Version A" with statistical confidence, which is essential for roadmap prioritization and ROI calculations.

## Related Concepts
- [[concepts/ux-research/ux-metrics|UX Metrics]]
- [[concepts/ux-research/reliability-vs-validity|Reliability vs Validity]]
- [[concepts/ux-research/behavioral-sequence-analysis|Behavioral Sequence Analysis]]
- [[wiki/concepts/ux-research/measurement-under-adaptation|Measurement Under Adaptation]] — the condition under which benchmarking stops being comparable.
- [[wiki/concepts/ux-research/steerability|Steerability]]

## ⚖️ Conflicts & Caveats

> [!warning] Benchmarking a personalised product is not comparable to itself — added 2026-08-04
> This practice's value proposition is comparability: over time, across releases, against competitors. [[wiki/sources/saeidehbakhshi-usability-metrics-static-product|Bakhshi (2026)]] argues that on an adaptive or personalised product that comparability is **unwarranted rather than merely degraded**, because the object of measurement is not stable:
>
> - *"Different users are using different versions of the product."*
> - *"The product changes as the same person uses it."*
> - *"The score is conditional on the user, their history, the state of the system, and the stage of use."*
>
> This is a validity problem, so more participants do not fix it. The number stays precise while its referent moves.
>
> **Minimum remedy, cheap and available now:** report the conditions with every benchmark figure — whose goal, which product state, what outcome, and what stage of use. A benchmark on a personalising surface without a declared product state is not comparable to its own previous run.
>
> Bakhshi's source is conceptual critique with no data, so this is an argument rather than a finding. It is a validity argument, which does not require data to be sound. See [[wiki/concepts/ux-research/measurement-under-adaptation|Measurement Under Adaptation]].

## 📚 Sources

- [[wiki/sources/saeidehbakhshi-usability-metrics-static-product|Bakhshi (2026): Usability Metrics Assume the Product Stays Still]] — the conditionality argument and the reporting standard.
