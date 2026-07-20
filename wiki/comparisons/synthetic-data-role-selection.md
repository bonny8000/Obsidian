---
type: comparison
status: active
created: 2026-07-20
updated: 2026-07-20
tags: [comparison, ux-research, synthetic-users, decision-table]
sources:
  - sources/saeidehbakhshi-ai-in-quantitative-research
  - sources/measuringu-synthetic-users-review
  - sources/voiceofuser-inhouse-digital-twins-blueprint
  - sources/uxperiment-synthetic-users-vs-real
confidence: 0.85
---

# Comparison: Which Synthetic-Data Role Fits My Research Question?

## Decision Question

A team wants to use synthetic users / LLM-generated data. Which of the four roles — rehearsal, forecasting, augmentation, substitution — does their question actually permit, and what validation does each demand?

## Criteria

Output type needed · whether the output becomes *evidence* · human-data requirement · known failure mode · validation bar.

## Matrix

| | **Rehearsal** | **Forecasting** | **Augmentation** | **Substitution** |
|---|---|---|---|---|
| Typical question | "Will this survey/interview guide work?" | "Which of these options is likely stronger?" | "Can we extend a small real sample?" | "Can we skip recruiting?" |
| Output becomes evidence? | No — instrument improvement | No — prioritization signal | Partially — corrected estimates | Yes — and that's the problem |
| Human data needed | None required | Real study still follows | **Reserved human responses are load-bearing** (bias 24–86% → <5% only with rectification) | Would need outcome-level proof that doesn't yet exist |
| Known failure mode | Over-trusting fluent pilot answers | Treating forecast as confirmation | Skipping the calibration step | Under-dispersion; wrong subgroups, SDs, coefficients; consensus bias erases Black Swans |
| Validation bar | Low — sanity check | Medium — track forecast vs observed over time | High — hold-out calibration each run | Not currently attainable (vault verdict) |
| Verdict | ✅ Use freely | ✅ Use, then verify empirically | ⚠️ Use with reserved human data | ❌ Refuse pending backtested evidence |

## Recommendation Pattern

1. Name the role *before* generating anything; write it in the study plan.
2. Anything labeled substitution gets reframed (usually to forecasting or augmentation) or escalated for human recruitment.
3. Apply the prompt countermeasures regardless of role: cohort-relative positioning, permission to be uncertain, evidence-licensing (green/yellow/red).
4. Log forecast-vs-actual whenever a real study follows — that record is what could eventually justify stronger roles.

## Source Evidence

- [[wiki/analyses/2026-07-20-synthetic-users-evidence-synthesis|Analysis: What the Evidence Actually Supports on Synthetic Users]] (full synthesis)
- [[wiki/sources/saeidehbakhshi-ai-in-quantitative-research|Bakhshi: AI in Quantitative Research]] · [[wiki/sources/measuringu-synthetic-users-review|MeasuringU review]] · [[wiki/sources/voiceofuser-inhouse-digital-twins-blueprint|Voice of User blueprint]] · [[wiki/sources/uxperiment-synthetic-users-vs-real|UXperiment head-to-head]]
