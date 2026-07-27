---
type: source
status: active
created: 2026-07-27
updated: 2026-07-27
tags: [source, ai, design-systems, automation, contracts]
sources:
  - raw/web/2026-07-27-use-ai-to-need-less-ai.md
confidence: 0.78
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
---

# Use AI to Need Less AI

## Citation

TJ, “Use AI to Need Less AI,” Slot Machine, retrieved 2026-07-27. [Original article](https://southleft.substack.com/p/use-ai-to-need-less-ai)

## Source Type

Practitioner essay on design-system automation and deterministic contracts.

## Location

`raw/web/2026-07-27-use-ai-to-need-less-ai.md`

## Summary

The source proposes a division of labor: use AI for uncertain synthesis and setup, then move repeatable facts into tokens, component specifications, contracts, tests, and other machine-checkable artifacts. This reduces the need to ask a model to rediscover the same information.

## Key Claims

- Many design-system questions are lookups, not judgments.
- Explicit contracts make AI-assisted work more consistent and auditable.
- The best use of AI can be to create conditions where fewer future AI calls are needed.

## Useful Examples

- Store token values in a canonical source instead of asking a model to infer them.
- Validate component props and Figma/code agreement with deterministic checks.

## Constraints / Caveats

The essay does not provide a quantified cost or quality comparison across teams.

## Design Implications

Design systems should expose canonical, machine-readable facts and provide checks that fail clearly when design and implementation drift.

## Tensions

Contracts increase consistency but can become stale or burdensome if ownership and update workflows are unclear.

## Open Questions

- Which design-system facts should be canonicalized first?
- What is the right escalation path when a contract conflicts with a real user need?

## Concepts Linked

- [[concepts/infrastructure-dev/deterministic-ai-workflows|Deterministic AI Workflows]]
- [[concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]]

## LLM Use

Use this source when deciding whether a task needs model judgment or can be handled by retrieval, validation, or a contract.

## Reliability Notes

The source is a practitioner argument. It is strong for design rationale and examples, but not for generalized performance claims.

## Backfill Status

New source page created from the 2026-07-27 raw capture.

