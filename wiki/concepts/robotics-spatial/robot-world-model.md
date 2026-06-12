---
type: concept
status: active
created: 2026-05-18
updated: 2026-05-18
tags: [robotics, world-model, simulation]
sources:
  - sources/arxiv-2602-06949
confidence: 0.88
---

# Robot World Model

## Summary

A robot world model predicts or simulates how actions affect environments, objects, and future observations. It can support planning, policy evaluation, teleoperation, and simulation.

## Why It Matters

World models can reduce reliance on real-world trial and error, especially for contact-rich and dexterous tasks where physical experimentation is expensive.

## Key Claims

- Large human video data may help pretrain models of physical interaction.
- Latent proxy actions can provide action-like structure when explicit action labels are missing.
- Robot-data post-training is still needed to adapt the world model to target robot settings.

## Related Concepts

- [[concepts/robotics-spatial/egocentric-human-data|Egocentric Human Data]]
- [[concepts/infrastructure-dev/model-based-planning|Model-Based Planning]]
- [[concepts/robotics-spatial/human-to-robot-transfer|Human-to-Robot Transfer]]
- [[concepts/robotics-spatial/dexterous-manipulation|Dexterous Manipulation]]

## Sources

- [[sources/arxiv-2602-06949|DreamDojo]]

## Open Questions

- [Answered → [[queries/2026-05-27-robot-world-model-contact-dynamics|Query Page]]] How well do video-trained world models preserve physical contact dynamics?

