---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.76
---

# How well do video-trained world models preserve physical contact dynamics?

## Short Answer
The DreamDojo source indicates that video-trained world models can capture general interaction patterns but require robot-data post-training to accurately represent contact dynamics for specific robot settings. Contact-rich tasks (grasping, pushing, tool use) are the hardest to preserve because video does not encode force, compliance, or tactile feedback. The world model provides useful qualitative prediction but is not yet reliable for high-precision planning of contact-rich tasks.

## Evidence
- [[concepts/robotics-spatial/robot-world-model|Robot World Model]] ??"World models can reduce reliance on real-world trial and error. Contact-rich robotics makes accurate planning difficult. Robot-data post-training is still needed to adapt the world model to target robot settings."
- [[sources/arxiv-2602-06949|DreamDojo]] ??"Large human video corpora can help pretrain robot world models for varied interactions. World models can support planning and evaluation for contact-rich robotics tasks after robot-data post-training."
- [[concepts/infrastructure-dev/model-based-planning|Model-Based Planning]] ??"Contact-rich robotics makes accurate planning difficult. Real-time speed and consistency matter for live use."
- [[concepts/robotics-spatial/dexterous-manipulation|Dexterous Manipulation]] ??"Large-scale egocentric human video is being explored as a motor prior for dexterous robot policies." A motor prior is not the same as contact dynamics fidelity.

## Follow-up Sources Needed
- Quantitative benchmarks measuring contact prediction accuracy of video-trained world models versus physics-based simulators.

