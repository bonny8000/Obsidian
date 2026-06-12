---
type: concept
status: active
created: 2026-05-18
updated: 2026-05-18
tags: [vla, robot-learning, foundation-model]
sources:
  - sources/arxiv-2512-22414
  - sources/arxiv-2602-16710
confidence: 0.88
---

# Vision-Language-Action Model

## Summary

A Vision-Language-Action (VLA) model connects visual perception, language conditioning, and action generation for robot behavior.

## Why It Matters

VLA models are a candidate architecture for generalist robot policies. The collected sources explore whether human video data and diverse pretraining can improve transfer and dexterous manipulation.

## Key Claims

- VLA transfer may improve with sufficient diversity across scenes, tasks, and embodiments.
- Human video can be part of VLA pretraining if the model can learn useful action-relevant representations.
- VLA scaling claims need careful evaluation because "emergence" depends on experiment design.

## Related Concepts

- [[concepts/robotics-spatial/human-to-robot-transfer|Human-to-Robot Transfer]]
- [[concepts/robotics-spatial/egocentric-human-data|Egocentric Human Data]]
- [[concepts/robotics-spatial/dexterous-manipulation|Dexterous Manipulation]]
- [[concepts/robotics-spatial/embodiment-gap|Embodiment Gap]]

## Sources

- [[sources/arxiv-2512-22414|Human-to-Robot Transfer in VLA Models]]
- [[sources/arxiv-2602-16710|EgoScale]]

## Open Questions

- [Answered → [[queries/2026-05-27-vla-pretraining-diversity-transfer|Query Page]]] What pretraining diversity is necessary before human-to-robot transfer appears?

