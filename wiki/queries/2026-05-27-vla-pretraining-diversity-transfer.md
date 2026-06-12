---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.82
---

# What pretraining diversity is necessary before human-to-robot transfer appears?

## Short Answer
Based on the arxiv sources, transfer appears when pretraining covers sufficient diversity across: (1) scenes and environments (not just a single lab setting); (2) task types (manipulation, navigation, interaction); and (3) embodiments (multiple robot types, not just one). The EgoScale source adds that large-scale human video diversity follows a log-linear relationship with model loss, implying more diversity monotonically helps until robot-data fine-tuning becomes the bottleneck.

## Evidence
- [[sources/arxiv-2512-22414|Human-to-Robot Transfer in VLA Models]] — "Diverse robot pretraining can help produce embodiment-agnostic representations. Human-to-robot skill transfer is framed as an emergent capability under sufficient data diversity."
- [[sources/arxiv-2602-16710|EgoScale]] — "Human video scale is reported to follow a log-linear relationship with validation loss in this setup. Human motion may provide an embodiment-agnostic motor prior for dexterous robot hands."
- [[concepts/robotics-spatial/vision-language-action-model|Vision-Language-Action Model]] — "VLA transfer may improve with sufficient diversity across scenes, tasks, and embodiments. VLA scaling claims need careful evaluation because 'emergence' depends on experiment design."
- [[concepts/robotics-spatial/embodiment-gap|Embodiment Gap]] — "Sufficiently diverse pretraining may produce more embodiment-agnostic representations." This is the key claim, but flagged as needing verification.

## Follow-up Sources Needed
- Specific dataset size thresholds and diversity metrics from the VLA transfer papers before the emergence phenomenon is observed.
