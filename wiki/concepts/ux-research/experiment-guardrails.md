---
type: concept
status: active
created: 2026-07-27
updated: 2026-07-27
tags: [ux-research, experimentation, guardrails, ai]
sources:
  - sources/ai-feature-monetization-spoonlabs
confidence: 0.72
---

# Experiment Guardrails

## Summary

Experiment guardrails are measures and constraints that prevent a local metric lift from being mistaken for user or business value.

## Why It Matters

AI product experiments can improve revenue or engagement while introducing cost, privacy, manipulation, or quality risks. Guardrails make those risks visible alongside the primary metric.

## Key Claims

- Pair proximate metrics with downstream outcomes and harm checks.
- Inspect outliers and durability before interpreting an average lift.
- Include AI cost, latency, error, and user-benefit limits in the experiment design.

## Related Concepts

- [[concepts/product-management/contextual-ai-value|Contextual AI Value]]
- [[concepts/product-management/ai-unit-economics|AI Unit Economics]]
- [[concepts/ux-research/methodological-integrity|Methodological Integrity]]

## Sources

- [[sources/ai-feature-monetization-spoonlabs|AI Feature Monetization at SpoonLabs]]

## Open Questions

- Which guardrails should stop an experiment automatically, and which should trigger review?