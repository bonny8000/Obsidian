---
type: concept
status: active
created: 2026-05-18
updated: 2026-05-18
tags: [robotics, mobile-manipulation, robot-learning]
sources:
  - sources/arxiv-2509-04443v1
confidence: 0.82
---

# Mobile Manipulation

## Summary

Mobile manipulation combines navigation and manipulation: a robot must move through space and interact with objects as part of the same task.

## Why It Matters

It is harder to scale than static manipulation because teleoperation is expensive and spatial configurations vary. EMMA explores egocentric human data as a way to reduce this bottleneck.

## Key Claims

- Mobile robot teleoperation is expensive.
- Human mobile manipulation data may support policy learning when co-trained with robot data.
- Generalization to new scenes is a central evaluation point.

## Related Concepts

- [[concepts/robotics-spatial/robot-imitation-learning|Robot Imitation Learning]]
- [[concepts/robotics-spatial/egocentric-human-data|Egocentric Human Data]]
- [[concepts/robotics-spatial/human-to-robot-transfer|Human-to-Robot Transfer]]

## Sources

- [[sources/arxiv-2509-04443v1|EMMA]]

## Open Questions

- How much mobile context must be represented for transfer from human movement to robot movement? (insufficient evidence in wiki — requires quantitative mobile context analysis from full papers)

