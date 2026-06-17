---
type: concept
status: active
created: 2026-06-17
updated: 2026-06-17
tags: [ux-research, screening, tac-10, tech-savviness, data-cleaning, guttman-scaling, survey-quality]
sources:
  - sources/measuringu-tac10-screening
confidence: 0.88
---

# TAC-10 Tech Savviness

> [!abstract] Summary
> The Technical Activity Checklist (10 items) is a self-report instrument that measures tech savviness by counting how many of 10 technical activities a respondent reports being able to perform. Because the items are roughly ordered easy → hard and form a near-Guttman scale, the *response pattern* (not just the score) is also a useful **survey data-cleaning signal**: 87% of real respondents produce Guttman or near-Guttman patterns; fewer than 0.5% produce implausible inverse-Guttman patterns. Emerged from 8 years of research showing **activity checklists outperform quizzes and questionnaires** at measuring tech competence.

> [!important] Why it Matters
> Tech savviness is decision-relevant in many UX studies (developer tooling, AI products, enterprise software) and self-report scores from poorly-screened panels are notoriously noisy. TAC-10 gives a single measure that is both a *predictor variable* (low / medium / high tech savviness) and a *data-quality canary* (pattern plausibility flags inattentive or fraudulent respondents). It is most useful in verified human populations or as one signal in a screening stack — not as a standalone AI-fraud filter.

## 📝 Key Claims

- TAC-10 measures **confidence performing 10 technical activities**, scored by counting selected items.
- Two uses: **(1)** classifying respondents into low / medium / high tech savviness groups; **(2)** functioning as a **predictive variable** in statistical analysis.
- Emerged from 8 years of research analyzing thousands of participants — **technical activity checklists outperform quizzes and questionnaires** at measuring tech competence.
- Items form a near-Guttman scale (consistent easy → hard hierarchy). Of 1,024 theoretically possible 10-item binary patterns, only 199 appear in a 4,731-response dataset.
- **Pattern frequencies (4,731-response analysis):**
  - **Perfect Guttman patterns (11 patterns):** 56.4% of responses.
  - **Plausible near-Guttman patterns (21 high-frequency patterns):** 30.7%.
  - **Indeterminate patterns:** 12.4% (no single pattern > 0.4%).
  - **Implausible patterns** (e.g. starting `01…` — claims hard activity without easier prerequisite): 0.4%.
  - **Inverse Guttman patterns:** 0% — never observed.
- Pattern plausibility is therefore a **screening signal**: implausible patterns can be automatically flagged.
- **Limitation regarding AI fraud:** sophisticated LLMs can train on published TAC-10 research and mimic plausible patterns. TAC-10 is best deployed in verified-human contexts (customer lists, post-screened panels) or as one signal in a stack — not as a standalone AI-fraud filter.

## How to apply

- **As a predictor:** include TAC-10 in survey demographics when tech savviness might moderate the metric of interest. Report low / medium / high group breakdowns in [[concepts/ux-research/banner-table|banner tables]].
- **As a screening signal:** auto-flag responses matching the < 0.5% implausible patterns; combine with other [[concepts/ux-research/survey-data-quality-screening|screening signals]] (speeders, attention checks, straightlining, open-ended review).
- **In verified-human contexts (customer lists, recruited cohorts):** the pattern check is more trustworthy because there is no LLM impersonation pressure.
- **In paid-panel contexts:** layer TAC-10 with at least three other signals (timing, attention checks, open-ended review, duplicate / bot detection).

## 🔗 Related Concepts

- [[concepts/ux-research/survey-data-quality-screening|Survey Data Quality Screening]] — the broader checklist TAC-10 sits inside.
- [[concepts/ux-research/participant-selection-criteria|Participant Selection Criteria]]
- [[concepts/ux-research/reliability-vs-validity|Reliability vs Validity]]
- [[concepts/ux-research/methodological-integrity|Methodological Integrity]]
- [[concepts/ux-research/quant-uxr-rigor|Quant UXR Rigor]]
- [[concepts/ux-research/standardized-usability-questionnaires|Standardized Usability Questionnaires]]

## ⚖️ Conflicts & Caveats

> [!warning] Not AI-fraud-proof
> Sauro & Lewis are explicit: a sophisticated LLM trained on published TAC-10 research can produce plausible response patterns. Treat the pattern check as a complement to behavioral / timing / open-ended signals, not a replacement.

> [!warning] Single-dataset base rates
> The 87% / 0.4% pattern frequencies come from MeasuringU's TAC-16 dataset (n = 4,731). Don't treat them as universal benchmarks across populations and instruments.

## 📚 Sources

- [[sources/measuringu-tac10-screening|MeasuringU: Using the TAC-10 for Screening and Data Cleaning]] (Lewis & Sauro, 2026) — primary source.

## ❓ Open Questions

- What is the TAC-10 pattern base rate in Bonny's own customer-list populations vs paid panels?
- Can a Bonny-specific tech-activity checklist (Chinese-language tech context, e.g. activities common in Taiwan tech work) replace TAC-10 for relevant audiences?
- For agent-augmented surveys, does the response-pattern check still hold, or do agentic respondents reshape the pattern space?
