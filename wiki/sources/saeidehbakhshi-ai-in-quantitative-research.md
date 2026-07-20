---
type: source
status: active
created: 2026-07-20
updated: 2026-07-20
tags: [ux-research, quantitative-research, ai-analysis, synthetic-data, evidence, measurement, source]
source_path: raw/web/saeidehbakhshi-ai-in-quantitative-research-2026-07-13.md
source_url: https://saeidehbakhshi.substack.com/p/ai-in-quantitative-research
authors: [Saeideh Bakhshi]
sources: []
ingest_level: deep
coverage: full
llm_ready: true
raw_preserved: true
confidence: 0.85
---

# Bakhshi: AI in Quantitative Research

**Author:** Saeideh Bakhshi
**Published:** 2026-07-13 — personal Substack; the quantitative companion to [[wiki/sources/bakhshi-ai-in-qualitative-research-map|AI in Qualitative Research — A Map]]
**Raw capture:** [[raw/web/saeidehbakhshi-ai-in-quantitative-research-2026-07-13|verbatim full text]]

## Citation

Bakhshi, S. (2026, July 13). *AI in quantitative research.* Substack. https://saeidehbakhshi.substack.com/p/ai-in-quantitative-research

## Summary

A methodological map of where AI helps and where it endangers quantitative research. Core distinction: **an analysis is an artifact** (query, chart, model, forecast); **evidence is the connection between that artifact and the claim** — data provenance, measure construction, comparison design, assumptions, uncertainty. AI is becoming very good at producing artifacts; the practitioner's enduring value moves to the surrounding work that makes artifacts mean something. Bakhshi names this future role **evidence engineering**: specifying questions, constructing measures, validating model-derived variables, preserving the analytical path, and calibrating conclusions.

The piece organizes AI's roles by validation burden: (1) constrained transformations (checkable against ground truth — safe); (2) model-derived measurement (label errors propagate into estimates — needs reference data); (3) exploration and forecasting (directs attention, never confirms); (4) representing people and populations (highest burden). For synthetic data it proposes four roles — **rehearsal, forecasting, augmentation, substitution** — warning that current evidence does not support substitution for a target population.

## Key Claims

- Producing an analysis and determining what it should represent are connected but distinct work; benchmarks (Spider 2.0: 21.3% solve rate; StatQA; BLADE) show models produce executable analyses while missing most expert analytical decisions. (conf 0.9)
- Substituting predicted labels into downstream analysis biases estimates and invalidates confidence intervals even at high classifier accuracy; confidence-driven allocation of human annotation preserves valid intervals. (conf 0.85)
- Synthetic respondents reproduce toplines but not variance, relationships, or response-bias structure (3.6M-response Political Analysis study; TACL nine-model evaluation; Nature MI persona misportrayal). Prompt-only agents predicted next real shopping action at 11.86%. (conf 0.85)
- GPT-4 forecasts of 70 preregistered survey experiments correlated strongly with observed effects — synthetic *forecasting* to prioritize studies is defensible where substitution is not. (conf 0.8)
- Augmentation with statistical rectification against reserved human responses cut synthetic bias from 24–86% to <5% — real responses are the load-bearing element. (conf 0.8)
- AI scales researcher degrees of freedom: wide automated search returns one clean chart whose confidence interval ignores the search that produced it; exploration must stay distinct from confirmation. (conf 0.9)
- Provenance is becoming part of measurement: 34% of online participants report LLM help on open-ended answers; practitioners must distinguish behaviorally observed, human-reported, AI-assisted, model-derived, simulated, and mixed evidence. (conf 0.85)

## Useful Examples

- Retention-decline walkthrough: AI produces cohort, SQL, chart, and summary — while "new user," "retention," logging changes, and identity migrations all remain unsettled definitional choices.
- Support-ticket labels ("resolution failure") as model-derived measures whose errors enter downstream estimates.
- CHI study of 22 analysts: no single representation (prose, code, chart, table) sufficed to audit an AI-produced analysis.

## Constraints / Caveats

- Practitioner essay synthesizing academic work, not itself peer-reviewed; benchmark numbers date quickly.
- Claims lean on the author's curation of studies; check the linked papers when a specific number matters.

## Design Implications

- Build validation into recurring workflows (reference datasets, logging-change checks, experiment templates, visible analytical paths) instead of a specialist approving every output.
- Keep synthetic data visibly separate from observed data; require backtests before trusting synthetic outputs at decision level.
- Review has to travel with the artifact: definitions, exclusions, prompts, and alternative specifications should stay inspectable.

## Tensions

- Complements and sharpens the vault's synthetic-user thread: more permissive than [[wiki/concepts/ux-research/synthetic-user-bias|Synthetic User Bias]] alone (forecasting/augmentation get real support) but stricter than vendor claims (substitution unsupported).
- With [[wiki/sources/guanjie-li-llm-user-proxy|Li's user-proxy work]]: Li locates the bottleneck in communicating intent (qual); Bakhshi locates it in validation burden (quant). Both reject "capability" as the limiting factor.

## Open Questions

- How much reference data is enough per model-derived measure, and how should it be refreshed as models drift?
- What does an auditable "analytical path" artifact look like in practice for fast-moving product teams?

## Concepts Linked

- [[wiki/concepts/ux-research/evidence-engineering|Evidence Engineering]]
- [[wiki/concepts/ux-research/synthetic-data-roles|Synthetic Data Roles]]
- [[wiki/concepts/ux-research/researcher-degrees-of-freedom|Researcher Degrees of Freedom]]
- [[wiki/concepts/ux-research/ai-qualitative-research-map|AI Qualitative Research Map]]
- [[wiki/concepts/ux-research/synthetic-user-taxonomy|Synthetic User Taxonomy]]
- [[wiki/concepts/ux-research/digital-twin-respondents|Digital-Twin Respondents]]
- [[wiki/concepts/ux-research/hybrid-research-model|Hybrid Research Model]]
- [[wiki/concepts/ux-research/llm-user-proxy|LLM User Proxy]]

## LLM Use

- **Use for:** deciding which quantitative tasks are safe to delegate to AI, designing validation for model-derived measures, arguing for/against synthetic-respondent use by role (rehearse/forecast/augment/substitute).
- **Do not use for:** citing benchmark numbers as current without re-checking; treating the four-role taxonomy as settled consensus.
- **Best prompt pattern:** name the AI's role in the analysis first (transformation / measurement / exploration / representation), then apply the matching validation standard from this source.

## Reliability Notes

- Heavily referenced essay (17 linked studies incl. Nature, PNAS, NeurIPS, ACL) by a practitioner with a consistent methodological series; strongest as a framework, weaker as a source of durable numbers.
