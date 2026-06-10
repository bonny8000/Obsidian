---
type: concept
status: active
created: 2026-05-18
updated: 2026-05-18
tags: [domain-adaptation, robot-learning, transfer]
sources:
  - sources/arxiv-2509-19626
  - sources/arxiv-2604-07607
confidence: 0.88
---

# Domain Adaptation

## Summary

Domain adaptation adjusts representations, policies, or training objectives so learning transfers across data domains, such as human video and robot sensor/action data.

## Why It Matters

Egocentric human data and robot data differ in appearance, sensors, action spaces, and kinematics. Domain adaptation is one way to make them jointly useful for policy learning.

## Key Claims

- Aligning latent spaces can support transfer while preserving action-relevant information.
- Dataset alignment with robot objectives is as important as dataset scale.
- Optimal transport appears in EgoBridge as one alignment mechanism.

## Related Concepts

- [[concepts/robotics-spatial/human-to-robot-transfer|Human-to-Robot Transfer]]
- [[concepts/robotics-spatial/embodiment-gap|Embodiment Gap]]
- [[concepts/robotics-spatial/egocentric-human-data|Egocentric Human Data]]

## Sources

- [[sources/arxiv-2509-19626|EgoBridge]]
- [[sources/arxiv-2604-07607|EgoVerse]]

## Open Questions

- Which adaptation metrics best predict real robot success? (insufficient evidence in wiki — requires quantitative studies beyond current source summaries)

