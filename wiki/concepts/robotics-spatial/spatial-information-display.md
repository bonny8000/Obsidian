---
type: concept
status: active
created: 2026-06-01
updated: 2026-06-01
tags: [robotics, ar, visualization]
sources: [gerhard-norton-vr-usability-2022]
confidence: 0.90
---

# Spatial Information Display

## Summary
Spatial Information Display refers to the visualization of data within a 3D environment, often overlaid on the physical world (AR) or within a virtual space (VR). Unlike 2D dashboards, spatial displays must account for depth, occlusion, and the user's perspective.

## Key Primitives
- **World-Locked:** Elements that stay fixed at a specific physical location.
- **Body-Locked:** Elements that follow the user's movement (e.g., a heads-up display).
- **Occlusion Handling:** Ensuring virtual elements are correctly hidden by real-world objects.
- **Proximity-Based Revelation:** Displaying more detail as the user gets closer to an object.

## Why it matters
In robotics and spatial computing, users need to process information while maintaining awareness of their surroundings. Well-designed spatial displays reduce "cognitive tunneling" and help users make faster, safer decisions in complex 3D environments.

## Related Concepts
- [[concepts/robotics-spatial/spatial-ai|Spatial AI]]
- [[concepts/robotics-spatial/human-robot-interaction|Human-Robot Interaction]]
- [[concepts/infrastructure-dev/deterministic-ui|Deterministic UI]]
