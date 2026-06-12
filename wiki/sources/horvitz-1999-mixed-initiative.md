---
type: source
status: active
created: 2026-06-12
tags: [source, paper, mixed-initiative, proactivity, agent-experience]
sources: []
updated: 2026-06-12
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.9
---

# Horvitz (1999): Principles of Mixed-Initiative User Interfaces

> [!info] Metadata
> - **Author:** Eric Horvitz
> - **Date:** CHI 1999, 159-166
> - **Type:** paper (peer-reviewed, ~1,000 citations, 16k+ downloads)
> - **Raw File:** [[raw/web/horvitz-1999-mixed-initiative]]

## Citation

Horvitz, E. (1999). Principles of Mixed-Initiative User Interfaces. Proceedings of CHI '99, 159-166. DOI 10.1145/302979.303030. Captured 2026-06-12 from ACM abstract and secondary literature; full text paywalled, coverage partial.

## Summary

The origin paper for proactive-agent interaction design. Resolves the direct-manipulation-versus-agents debate by coupling them: automation should add value within an interface the user still directly controls. Treats agent initiative as a decision-theoretic problem — act only when expected value exceeds the combined cost of being wrong and of interrupting — demonstrated via the Lookout scheduling system.

## Key Claims

- Provide automated service only when it clearly beats the user doing it directly.
- Reason about uncertainty in user goals before acting; weigh expected utility of action against costs of error and interruption.
- The user's attention is a costed resource; initiative timing must account for the user's current focus.
- When confidence is low, degrade gracefully: scope down, open a clarifying dialog, or stay silent rather than guess.
- Keep invocation and dismissal cheap; the user can always reclaim direct control.
- Maintain memory of recent interactions and learn from user behavior over time.

## Useful Examples

- Lookout's graded autonomy: from doing nothing, to suggesting, to acting with confirmation, to acting automatically — selected by inferred confidence. This is a ready-made template for proactivity-level logic.

## Constraints / Caveats

- 1999 inference machinery (Bayesian models over email text) is dated; the decision framework is what transfers, not the implementation.
- Partial ingest from abstract and secondary sources.

## Design Implications

- Replace binary autonomy settings with an expected-value gate: confidence × value vs. interruption + error cost.
- Design the full graded-autonomy ladder, not just the proactive end state.
- Budget attention explicitly; every unprompted touch must clear the interruption-cost bar.

## Tensions

- Tension with growth-driven notification design: Horvitz's frame treats most interruptions as negative-utility by default.

## Open Questions

- How should expected-value gating work when the agent's confidence estimates are themselves unreliable (LLM overconfidence)?

## Concepts Linked

- [[concepts/agent-experience/proactivity-design|Proactivity Design]]
- [[concepts/agent-experience/initiative-and-interruption|Initiative and Interruption]]
- [[concepts/agent-experience/collaboration-patterns|Collaboration Patterns]]

## LLM Use

- **Use for:** grounding proactivity and interruption design decisions, the graded-autonomy ladder, attention-cost framing.
- **Do not use for:** implementation details of the original system.
- **Best prompt pattern:** Ask the LLM to run a proposed proactive feature through the expected-value gate: value if right, cost if wrong, cost of interruption, reversibility.

## Reliability Notes

> [!warning] Caveats
> Pre-LLM but actively cited in 2025-26 proactive-agent literature; framework considered current. Coverage partial.

## Backfill Status

- Promote to coverage: full if PDF obtained.
