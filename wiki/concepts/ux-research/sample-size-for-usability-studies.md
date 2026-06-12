---
type: concept
status: active
created: 2026-06-10
updated: 2026-06-12
tags: [concept, statistics, quant-ux, sample-size]
sources:
  - sources/sauro-lewis-quantifying-ux-2016
  - sources/measuringu-statistics-30-participants
confidence: 0.95
---

# Sample Size for Usability Studies

## Summary

Sample size logic differs by study goal. **Summative** (measuring): driven by desired margin of error / detectable difference — work backward from the precision the decision needs (Sauro & Lewis ch. 6). **Formative** (finding problems): driven by the problem-discovery function 1 − (1 − p)ⁿ, where p is the probability an issue affects a given user (ch. 7).

## Why it matters

"How many users?" is the most common quant question in UX. The answer is a calculation, not folklore — and the calculation is small enough to do in a spreadsheet.

## Key claims

- The n >= 30 rule is a useful statistical approximation in some contexts, but it is not a universal UX sample-size requirement. Plan from data type, analysis goal, expected variability, desired confidence or power, and minimum effect size.

- Formative discovery follows 1 − (1 − p)ⁿ; Monte Carlo studies (Nielsen & Landauer 1993) found average p ≈ 0.31, which makes 5 users find ~85% of problems — the origin of the "magic number five". (conf 0.95)
- "Five users" and "eight is not enough" are both right: with low-p problems (p = 0.10–0.15) or problem sets defined more strictly, required n grows to dozens. The dispute dissolves once p is made explicit. (conf 0.9)
- Iterative testing changes the math: 3 + 4 + 7 participants across three fix cycles can hit 90% discovery of p = 0.15 problems. (conf 0.9)
- Summative comparisons need far larger n than formative studies — plan for the statistical test, not the lab schedule. (conf 0.9)

## Related concepts

- [[concepts/ux-research/problem-discovery-model|Problem Discovery Model]]
- [[concepts/ux-research/adjusted-wald-confidence-interval|Adjusted-Wald Confidence Interval]]
- [[concepts/ux-research/evaluator-effect|Evaluator Effect]]

## Sources

- [[sources/measuringu-statistics-30-participants|MeasuringU: Do Statistics Really Require 30 Participants?]]

- [[sources/sauro-lewis-quantifying-ux-2016|Sauro & Lewis (2016)]], ch. 6–7.

## Open questions

- Which Bonny research decisions need power planning versus only a precision estimate?

- What p is realistic for AI-moderated studies, where session quality differs from lab sessions?
