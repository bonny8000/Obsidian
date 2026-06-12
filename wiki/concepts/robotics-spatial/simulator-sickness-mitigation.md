---
type: concept
status: active
created: 2026-06-01
updated: 2026-06-01
tags: [robotics, vr, ar, usability]
sources: [gerhard-norton-vr-usability-2022]
confidence: 0.90
---

# Simulator Sickness Mitigation

## Summary
Simulator sickness (or motion sickness) occurs in VR/AR when there is a mismatch between what the eyes see and what the inner ear feels. Mitigation strategies are design patterns used to reduce or eliminate this discomfort.

## Mitigation Strategies
- **Fixed Reference Frames:** Keeping a static object (like a cockpit or dashboard) in the user's view.
- **Teleportation:** Moving the user instantly rather than using smooth locomotion.
- **Vignetting:** Narrowing the field of view (FOV) during movement.
- **Horizon Stabilization:** Keeping the virtual horizon level with the user's real-world orientation.

## Why it matters
If a spatial interface makes users physically ill, they will not use it. Mitigation is a core usability requirement for any spatial computing or remote robotics operation interface.

## Related Concepts
- [[concepts/robotics-spatial/spatial-ai|Spatial AI]]
- [[concepts/robotics-spatial/ar-glasses|AR Glasses]]
- [[concepts/robotics-spatial/immersion-vs-presence|Immersion vs Presence]]
