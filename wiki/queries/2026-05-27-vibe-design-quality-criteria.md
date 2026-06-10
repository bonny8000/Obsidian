---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.68
---

# What criteria should Bonny use to judge AI-generated design quality?

## Short Answer
AI-generated design quality should be judged on: (1) consistency with the design system (tokens, spacing, typography match); (2) structural correctness (information hierarchy, affordances, interaction patterns); (3) user task alignment (does it serve the intended user task without confusion); (4) implementation feasibility (can a coding agent implement this without inventing new patterns); and (5) reviewability (is the artifact editable and explorable, not just a static image).

## Evidence
- [[concepts/ai-agents/vibe-design|Vibe Design]] ??"Quality still depends on design judgment, critique, and consistency with a design system. The useful unit of work becomes intent plus review, not just a static artboard."
- [[concepts/infrastructure-dev/design-automation|Design Automation]] ??"AI design workflows are more reliable when they can read existing design systems and codebases. Automation should preserve designer review and taste as control points."
- [[concepts/infrastructure-dev/design-to-code-workflow|Design-to-Code Workflow]] ??"AI design artifacts can become structured inputs for coding agents." This implies feasibility as a quality criterion.
- [[sources/brunch-ghidesigner-482|Vibe Design and Coding with Claude Design and Claude Code]] ??"Design-to-code work becomes more continuous when design intent, design-system rules, and implementation are represented in structured forms that agents can consume."

## Follow-up Sources Needed
- A rubric or scoring scale for each of the five criteria, calibrated to Bonny's specific design system.

