---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.82
---

# Which embodiment gaps can be solved by data scale versus explicit adaptation?

## Short Answer
Data scale (pretraining on large diverse datasets) can address gaps related to visual appearance diversity and task vocabulary. Explicit adaptation methods are needed for kinematic mismatches (different joint configurations), action-space differences (human hand DOF vs. robot hand DOF), and sensor gaps (egocentric camera placement differs from robot camera). The arxiv-2512-22414 source frames sufficiently diverse pretraining as producing embodiment-agnostic representations, but the other sources show this does not eliminate the need for adaptation at the kinematic level.

## Evidence
- [[sources/arxiv-2512-22414|Human-to-Robot Transfer in VLA Models]] ??"Human-to-robot skill transfer is framed as an emergent capability under sufficient data diversity." Scale addresses visual and task diversity gaps.
- [[sources/arxiv-2509-19626|EgoBridge]] ??"Human-to-robot transfer is limited by visual, sensor, and kinematic gaps. Aligning policy latent spaces can preserve action-relevant information while improving transfer." Explicit adaptation is needed for kinematic gaps.
- [[sources/arxiv-2505-21864|DexUMI]] ??"A wearable hand exoskeleton can adapt human motion toward feasible robot hand motion. Hardware and software adaptation are both used to bridge human-to-robot embodiment differences." Hardware adaptation for DOF gaps.
- [[concepts/robotics-spatial/embodiment-gap|Embodiment Gap]] ??"Embodiment gaps can be visual, kinematic, sensory, or action-space related. Some sources argue that scale can help produce embodiment-agnostic representations, but this needs full-paper verification."

## Follow-up Sources Needed
- Ablation studies isolating the contribution of data scale versus adaptation techniques across different gap types.

