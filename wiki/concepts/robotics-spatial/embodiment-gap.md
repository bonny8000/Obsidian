---
type: concept
status: active
created: 2026-05-18
updated: 2026-05-18
tags: [robot-learning, embodiment, transfer]
sources:
  - sources/arxiv-2410-24221
  - sources/arxiv-2509-19626
  - sources/arxiv-2512-22414
  - sources/arxiv-2505-21864
confidence: 0.88
---

# Embodiment Gap

## Summary

The embodiment gap is the mismatch between a human body or sensing setup and a robot body, sensor suite, action space, or kinematic constraints.

## Why It Matters

Human data is abundant, but robots do not have human hands, arms, sensors, or movement constraints. Bridging this gap is necessary for useful [[concepts/robotics-spatial/human-to-robot-transfer|Human-to-Robot Transfer]].

## Key Claims

- Embodiment gaps can be visual, kinematic, sensory, or action-space related.
- Methods include hardware adaptation, visual inpainting, domain adaptation, latent-space alignment, and diverse pretraining.
- Some sources argue that scale can help produce embodiment-agnostic representations, but this needs full-paper verification.

## Related Concepts

- [[concepts/robotics-spatial/human-to-robot-transfer|Human-to-Robot Transfer]]
- [[concepts/infrastructure-dev/domain-adaptation|Domain Adaptation]]
- [[concepts/robotics-spatial/dexterous-manipulation|Dexterous Manipulation]]
- [[concepts/robotics-spatial/vision-language-action-model|Vision-Language-Action Model]]

## Sources

- [[sources/arxiv-2410-24221|EgoMimic]]
- [[sources/arxiv-2509-19626|EgoBridge]]
- [[sources/arxiv-2512-22414|Human-to-Robot Transfer in VLA Models]]
- [[sources/arxiv-2505-21864|DexUMI]]

## Open Questions

- [Answered → [[queries/2026-05-27-embodiment-gap-scale-vs-adaptation|Query Page]]] Which embodiment gaps can be solved by data scale versus explicit adaptation?

