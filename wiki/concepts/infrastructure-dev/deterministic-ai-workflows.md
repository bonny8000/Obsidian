---
type: concept
status: active
created: 2026-07-27
updated: 2026-07-28
tags: [ai, automation, contracts, design-systems, reliability]
sources:
  - sources/use-ai-to-need-less-ai
  - sources/naver-d2-ai-hackathon-nstake
  - sources/polar-orbit-llm-safe-design-system
confidence: 0.84
---

# Deterministic AI Workflows

## Summary

Deterministic AI workflows use models for uncertain synthesis, then move stable facts and repeatable checks into canonical files, contracts, retrieval, tests, or tooling.

## Why It Matters

Repeatedly asking a model to rediscover stable facts is slower, more expensive, and less consistent than giving machinery a canonical source of truth.

## Key Claims

- Lookup work should usually be handled by retrieval or validation.
- Contracts reduce improvisation after an AI-generated artifact is accepted.
- The workflow should make exceptions explicit rather than silently overriding rules.
- **The reproducibility test decides placement.** *Must identical input produce identical output?* If yes, the work leaves the model. [[wiki/sources/naver-d2-ai-hackathon-nstake|NStake]] removed the LLM from monthly-report generation after identical transaction data produced varying wording, format drift, and a dependency on model uptime — classification and totals became explicit rules shared by every surface.
- **Constrain the acceptance criteria, not the generator.** [[wiki/sources/polar-orbit-llm-safe-design-system|Polar Orbit]]: *"The LLM is free to write anything it wants. We just make sure the only things that pass CI are things we'd be happy to ship."*
- **Reserve models for the band where being wrong is cheap and visible** — drafts the user will re-review, multiple acceptable phrasings, and narrowing where a human should look. NStake's delegation table makes each of these an explicit assignment rule.
- **Determinism has a standing price.** Rule authoring, baseline schemas, and token curation are all recurring costs, and no source states the volume at which they break even.

## Related Concepts

- [[wiki/concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]]
- [[wiki/concepts/infrastructure-dev/llm-safe-design-system|LLM-Safe Design System]] — the front-end instance: off-system values made uncompilable.
- [[wiki/concepts/ai-agents/rule-statistical-external-validation|Rule / Statistical / eXternal Validation]] — how to split findings the system can decide from findings it cannot.
- [[wiki/concepts/ai-agents/permission-boundary-guardrails|Permission-Boundary Guardrails]] — the same logic applied to access rather than computation.
- [[wiki/concepts/infrastructure-dev/design-system-implementation|Design System Implementation]]
- [[wiki/concepts/infrastructure-dev/ai-readable-documentation|AI-Readable Documentation]]

## Sources

- [[sources/use-ai-to-need-less-ai|Use AI to Need Less AI]]
- [[wiki/sources/naver-d2-ai-hackathon-nstake|NAVER D2 (2026): What the Winning AI Hackathon Team Did *Not* Delegate to AI]] — the delegation table and the report-generation reversal.
- [[wiki/sources/polar-orbit-llm-safe-design-system|Polar (2026): Building an LLM-Safe Design System (Orbit)]] — types and CI as the acceptance gate.

## Open Questions

- Which contracts deserve automated enforcement first?
- At what volume does rule maintenance cost more than the failures it prevents? Unanswered by every source here.
- Does the reproducibility test have a useful analogue in judgment-heavy domains with no deterministic right answer?

## See Also

- [[wiki/comparisons/delegate-vs-determinize|Comparison: Delegate to a Model vs. Determinize in Code]]
- [[wiki/analyses/2026-07-28-constraining-ai-by-construction|Analysis: Constraining AI by Construction]]
