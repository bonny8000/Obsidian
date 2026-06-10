---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.68
---

# What fidelity threshold is required before design-to-code output is useful?

## Short Answer
Design-to-code output becomes useful when: (1) component identity is resolved (the design specifies which design-system component to use, not just a visual shape); (2) spacing and typography tokens are explicit (not eyeballed pixel values); and (3) the design is connected to a real design system that the coding agent can reference. Below this threshold, the agent must guess implementation decisions, producing output that requires heavy manual correction.

## Evidence
- [[concepts/infrastructure-dev/design-to-code-workflowDesign-to-Code Workflow]] ??"A useful workflow includes design-system context, codebase context, browser verification, and human review."
- [[concepts/infrastructure-dev/design-system-implementationDesign System Implementation]] ??"AI design-to-code workflows should respect design-system implementation constraints."
- [[concepts/ai-agents/vibe-designVibe Design]] ??"The useful unit of work becomes intent plus review, not just a static artboard." Intent must include enough specificity to drive code generation.
- [[sources/ditoday-claude-design-uiux-workflow|Digital iNSIGHT: Claude Design and UI/UX Workflow]] ??"Design outputs may become implementation-ready bundles that connect to coding agents." 'Implementation-ready' implies the fidelity requirements above.

## Follow-up Sources Needed
- Case studies measuring implementation quality as a function of design specification fidelity level.

