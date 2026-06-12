---
type: concept
status: active
created: 2026-05-18
updated: 2026-05-18
tags: [robot-learning, egocentric-video, data]
sources:
  - sources/arxiv-2410-24221
  - sources/arxiv-2509-19626
  - sources/arxiv-2509-04443v1
  - sources/arxiv-2512-22414
  - sources/arxiv-2602-16710
  - sources/arxiv-2604-07607
  - sources/arxiv-2602-06949
confidence: 0.9
---

# Egocentric Human Data

## Summary

Egocentric human data is first-person human activity data, often video and sometimes hand/body/action annotations, used as a scalable source of demonstrations for robot learning.

## Why It Matters

Robot data is expensive to collect. The collected arXiv sources repeatedly explore whether human first-person data can scale robot manipulation, transfer, world models, and VLA training.

## Key Claims

- Human egocentric data can cover diverse objects, environments, and everyday tasks.
- Transfer to robots requires handling visual, kinematic, sensor, and embodiment gaps.
- Dataset standardization and alignment with robot objectives are recurring bottlenecks.

## Related Concepts

- [[concepts/robotics-spatial/human-to-robot-transfer|Human-to-Robot Transfer]]
- [[concepts/robotics-spatial/robot-imitation-learning|Robot Imitation Learning]]
- [[concepts/robotics-spatial/embodiment-gap|Embodiment Gap]]
- [[concepts/robotics-spatial/robot-learning-dataset|Robot Learning Dataset]]
- [[concepts/robotics-spatial/robot-world-model|Robot World Model]]

## Sources

- [[sources/arxiv-2410-24221|EgoMimic]]
- [[sources/arxiv-2509-19626|EgoBridge]]
- [[sources/arxiv-2509-04443v1|EMMA]]
- [[sources/arxiv-2512-22414|Human-to-Robot Transfer in VLA Models]]
- [[sources/arxiv-2602-16710|EgoScale]]
- [[sources/arxiv-2604-07607|EgoVerse]]
- [[sources/arxiv-2602-06949|DreamDojo]]

## Open Questions

- Which annotations are necessary for each downstream robot task? (insufficient evidence in wiki — requires detailed task-by-task analysis from full papers)
- How much human data is useful before robot-specific data becomes the limiting factor? (insufficient evidence in wiki — requires quantitative threshold data from full papers)

