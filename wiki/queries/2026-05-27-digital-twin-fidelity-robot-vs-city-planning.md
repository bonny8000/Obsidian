---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.72
---

# What fidelity is necessary for robot operation versus city planning?

## Short Answer
Robot operation requires centimeter-level geometric fidelity, real-time updates, and material/surface properties (floor friction, obstacle height) because the robot makes immediate physical decisions. City planning requires broader spatial coverage with lower geometric precision, semantic labels (zone types, service routes), and temporal snapshots rather than live updates. The two uses need different fidelity profiles from the same underlying digital twin data.

## Evidence
- [[concepts/robotics-spatial/digital-twin|Digital Twin]] ??"Digital twins become more valuable when continuously updated with real-world data. For city-scale use, digital twins connect indoor spaces, logistics, roads, and services."
- [[concepts/robotics-spatial/visual-localization|Visual Localization]] ??"A robot's ability to act in a building starts with knowing where it is. Visual localization must remain robust under crowding, lighting change, and environmental change." This implies centimeter-level precision requirements for robot use.
- [[concepts/robotics-spatial/smart-city-ai|Smart City AI]] ??"Last-mile movement and indoor/outdoor continuity are important smart-city concerns." City planning needs route-level continuity, not centimeter precision.
- [[sources/naverlabs-blog-34515|NAVER LABS: AI and Space]] ??"Spatial AI requires digital representations of physical environments. NAVER LABS positions DUSt3R, novel view synthesis, visual localization as parts of a physical-world AI stack." These are robot-grade fidelity technologies.

## Follow-up Sources Needed
- Quantitative fidelity specifications from robot navigation papers (e.g., localization error bounds) versus city planning GIS standards.

