---
type: concept
status: active
created: 2026-05-18
updated: 2026-05-18
tags: [robotics, planning, world-model]
sources:
  - sources/arxiv-2602-06949
confidence: 0.82
---

# Model-Based Planning

## Summary

Model-based planning uses a model of the environment or dynamics to evaluate possible actions before executing them.

## Why It Matters

If a robot world model can simulate likely outcomes, a robot can choose actions with less real-world trial and error.

## Key Claims

- World models can support planning by forecasting the effect of actions.
- Real-time speed and consistency matter for live use.
- Contact-rich robotics makes accurate planning difficult.

## Related Concepts

- [[concepts/robotics-spatial/robot-world-model|Robot World Model]]
- [[concepts/robotics-spatial/egocentric-human-data|Egocentric Human Data]]
- [[concepts/robotics-spatial/dexterous-manipulation|Dexterous Manipulation]]

## Sources

- [[sources/arxiv-2602-06949|DreamDojo]]

## Open Questions

- Which planning benchmarks are appropriate for egocentric-video-trained robot world models? (insufficient evidence in wiki — requires benchmark survey beyond current source summaries)

