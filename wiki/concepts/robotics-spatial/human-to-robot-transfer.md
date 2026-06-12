---
type: concept
status: active
created: 2026-05-18
updated: 2026-05-18
tags: [robot-learning, transfer, robotics]
sources:
  - sources/arxiv-2410-24221
  - sources/arxiv-2509-19626
  - sources/arxiv-2512-22414
  - sources/arxiv-2602-16710
  - sources/arxiv-2505-21864
  - sources/arxiv-2604-07607
confidence: 0.9
---

# Human-to-Robot Transfer

## Summary

Human-to-robot transfer is the process of using human behavior data to improve robot policies, representations, world models, or task performance.

## Why It Matters

It is the core promise behind the egocentric robot learning cluster: use abundant human behavior to reduce expensive robot demonstration collection.

## Key Claims

- Transfer quality depends on aligning human data with robot learning objectives.
- Sufficiently diverse pretraining may produce more embodiment-agnostic representations.
- Hardware, visual, latent-space, and dataset-level methods all address the transfer problem from different angles.

## Related Concepts

- [[concepts/robotics-spatial/egocentric-human-data|Egocentric Human Data]]
- [[concepts/robotics-spatial/embodiment-gap|Embodiment Gap]]
- [[concepts/infrastructure-dev/domain-adaptation|Domain Adaptation]]
- [[concepts/robotics-spatial/vision-language-action-model|Vision-Language-Action Model]]
- [[concepts/robotics-spatial/dexterous-manipulation|Dexterous Manipulation]]

## Sources

- [[sources/arxiv-2410-24221|EgoMimic]]
- [[sources/arxiv-2509-19626|EgoBridge]]
- [[sources/arxiv-2512-22414|Human-to-Robot Transfer in VLA Models]]
- [[sources/arxiv-2602-16710|EgoScale]]
- [[sources/arxiv-2505-21864|DexUMI]]
- [[sources/arxiv-2604-07607|EgoVerse]]

## Open Questions

- Which transfer mechanisms are robust across robot embodiments rather than task-specific? (insufficient evidence in wiki — requires cross-embodiment comparison studies beyond current source summaries)

