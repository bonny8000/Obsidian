---
type: concept
status: active
created: 2026-07-20
updated: 2026-07-20
tags: [ux-research, synthetic-users, quantitative-research, validation]
sources:
  - sources/saeidehbakhshi-ai-in-quantitative-research
confidence: 0.8
---
# Synthetic Data Roles

## Summary

A four-role taxonomy for synthetic (model-generated) research data, ordered by rising validation burden: **rehearsal** (test instruments, widen hypotheses), **forecasting** (predict which result is likely, to allocate effort), **augmentation** (combine generated data with real observations that calibrate and correct), and **substitution** (generated observations stand in for a target population). Roles that produce similar-looking rows are not evidentially equivalent.

## Key Claims

- Rehearsal and forecasting inform empirical work without becoming evidence; GPT-4 forecasts of 70 preregistered survey experiments correlated strongly with observed effects. *(Bakhshi 2026)*
- Augmentation works only when real responses do the calibrating: statistical rectification against reserved human data cut synthetic bias from 24–86% to under 5%. *(Bakhshi 2026)*
- Substitution is unsupported by current evidence: synthetic respondents reproduce toplines but compress variance, alter regression relationships, miss human response-bias patterns, and misportray identity groups. *(Bakhshi 2026)*
- Generating ten thousand rows does not create ten thousand independent observations — repeated generation reduces simulation noise, not coverage or calibration error. *(Bakhshi 2026)*

## Why It Matters (for UX)

Teams debating "synthetic users: yes or no?" are asking the wrong question — the defensible question is *which role*. This taxonomy gives the vault's synthetic-user cluster a decision rule: rehearse and forecast freely, augment with reserved human data, and demand outcome-level proof before any substitution.

## Related Concepts

- [[wiki/concepts/ux-research/synthetic-user-taxonomy|Synthetic User Taxonomy]]
- [[wiki/concepts/ux-research/digital-twin-respondents|Digital-Twin Respondents]]
- [[wiki/concepts/ux-research/synthetic-user-bias|Synthetic User Bias]]
- [[wiki/concepts/ux-research/hybrid-research-model|Hybrid Research Model]]
- [[wiki/concepts/ux-research/in-house-synthetic-user-pipeline|In-House Synthetic User Pipeline]]
- [[wiki/concepts/ux-research/evidence-engineering|Evidence Engineering]]

## Sources

- [[wiki/sources/saeidehbakhshi-ai-in-quantitative-research|Bakhshi: AI in Quantitative Research (2026)]]

## Open Questions

- What outcome-level backtests would count as sufficient evidence to promote a synthetic pipeline from augmentation to substitution in a bounded setting?
