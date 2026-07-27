---
type: concept
status: active
created: 2026-07-27
updated: 2026-07-27
tags: [ai, automation, contracts, design-systems, reliability]
sources:
  - sources/use-ai-to-need-less-ai
confidence: 0.8
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

## Related Concepts

- [[concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]]
- [[concepts/infrastructure-dev/design-system-implementation|Design System Implementation]]
- [[concepts/infrastructure-dev/ai-readable-documentation|AI-Readable Documentation]]

## Sources

- [[sources/use-ai-to-need-less-ai|Use AI to Need Less AI]]

## Open Questions

- Which contracts deserve automated enforcement first?
