---
type: concept
status: active
created: 2026-06-10
updated: 2026-06-16
tags: [concept, statistics, quant-ux, sample-size]
sources:
  - sources/sauro-lewis-quantifying-ux-2016
  - sources/measuringu-statistics-30-participants
confidence: 0.95
---

# Sample Size for Usability Studies

## Summary

Sample size logic depends on the study goal. Formative problem discovery asks how many users are needed to uncover likely problems. Summative measurement asks how much precision, power, or detectable difference the decision needs. The common n >= 30 rule is a rough statistical teaching shortcut, not a universal UX research requirement.

## Why It Matters

"How many users?" is one of the most common UX research questions. A fixed threshold is easy to communicate, but it hides the real inputs: data type, analysis goal, expected variability, desired confidence or power, minimum effect size, and decision risk.

## Key Claims

- n >= 30 has real statistical roots, especially t-to-z convergence and broad Central Limit Theorem heuristics.
- The rule should not decide UX sample size by itself.
- Formative discovery follows a problem-discovery model: the required n depends on the probability that a problem affects a participant and on whether testing is iterative.
- Summative estimates and comparisons require precision or power planning.
- Rating scales can use t-based intervals or tests at small n when assumptions are reasonable.
- Binary completion rates need adjusted methods, not naive Wald intervals.
- Task-time estimates often need log transformation because time data is right-skewed.
- Small n usually means wider intervals and lower power, not automatic invalidity.

## Decision Routing

- Problem discovery: estimate issue prevalence and use the discovery function; do not borrow the n >= 30 rule.
- Rating-scale mean: use a t interval or t test with the correct degrees of freedom.
- Completion rate: use [[adjusted-wald-confidence-interval|Adjusted-Wald Confidence Interval]] for small-n uncertainty.
- Task time: log-transform for interval estimation, then transform back to the original scale.
- Two-design comparison: plan around expected effect size and whether the design is within-subjects or between-subjects.
- Stakeholder challenge: explain the method, uncertainty, and decision limit instead of defending a magic number.

## Report Language

- Good: "This sample supports a directional estimate with wide uncertainty; it is not powered for subtle differences."
- Good: "The interval width is the limiting factor, not the fact that n is below 30."
- Avoid: "Statistics require 30 participants."
- Avoid: "Small samples are always fine."

## Related Concepts

- [[concepts/ux-research/problem-discovery-model|Problem Discovery Model]]
- [[concepts/ux-research/adjusted-wald-confidence-interval|Adjusted-Wald Confidence Interval]]
- [[concepts/ux-research/ux-statistics-decision-map|UX Statistics Decision Map]]
- [[concepts/ux-research/quant-uxr-rigor|Quant UXR Rigor]]
- [[playbooks/small-n-ux-statistics-checklist|Small-N UX Statistics Checklist]]

## Sources

- [[sources/measuringu-statistics-30-participants|MeasuringU: Do Statistics Really Require 30 Participants?]]
- [[sources/sauro-lewis-quantifying-ux-2016|Sauro & Lewis (2016)]], ch. 6-7.

## Open Questions

- Which Bonny research decisions need formal power planning versus only a precision estimate?
- What problem prevalence is realistic for AI-assisted or AI-moderated usability sessions?
- Should the vault include a lightweight calculator for interval width and detectable effect size?
