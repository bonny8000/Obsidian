---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.84
---

# When is human demonstration data better than additional robot demonstration data?

## Short Answer
Human demonstration data is better than additional robot data when: (1) robot data collection is expensive or slow relative to collecting human video; (2) the task is common in human daily activity but rare for the specific robot embodiment; (3) the robot system needs diversity in objects, environments, or task sequences that robot data collection cannot efficiently cover; and (4) scaling is the priority and the embodiment gap can be handled by adaptation methods.

## Evidence
- [[sources/arxiv-2410-24221|EgoMimic]] ??"Additional human hand data may scale more favorably than additional robot data in the reported setting."
- [[concepts/robotics-spatial/robot-imitation-learningRobot Imitation Learning]] ??"Demonstration scale and diversity are central bottlenecks. Human data can complement robot data when aligned carefully."
- [[concepts/robotics-spatial/egocentric-human-dataEgocentric Human Data]] ??"Human egocentric data can cover diverse objects, environments, and everyday tasks."
- [[concepts/robotics-spatial/embodiment-gapEmbodiment Gap]] ??"Methods include hardware adaptation, visual inpainting, domain adaptation, latent-space alignment, and diverse pretraining." When these methods work, human data becomes viable; when they fail, robot data is still needed.
- [[concepts/robotics-spatial/human-to-robot-transferHuman-to-Robot Transfer]] ??"Transfer quality depends on aligning human data with robot learning objectives."

## Follow-up Sources Needed
- Quantitative comparisons of human vs. robot demonstration data efficiency across multiple tasks and robot platforms.

