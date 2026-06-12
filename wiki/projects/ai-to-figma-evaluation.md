---
type: project
status: active
created: 2026-06-01
updated: 2026-06-01
tags: [project, figma, ai-generation, workflow-automation]
sources: [claude-history-sync]
---

# Project: AI-to-Figma Evaluation Pipeline (From UX to AX)

## Objectives
- [x] Instruct AI to replicate UI reference images directly into Figma.
- [x] Conduct automated visual regression reviews (comparing margins, layout, and colors between the reference and the generated Figma design).
- [x] Generate automated HTML slide reports using the `bonny8000/bonnyt` skill to display side-by-side comparisons.
- [x] **New:** Establish a "PRD to Code" workflow where PRDs are parsed into Flow -> Component Selection -> Interactive Code.

## Current Status
- **Phase:** Discovery / Prototyping
- **Last Update:** 2026-06-01 (Extracted from Claude history & Notion "Evaluation UX [I]" meeting)
- **Key Focus:** Moving beyond static mockups to generate interactive, browser-ready code, and implementing a "Dual-Track Review" mechanism (Top-down structure review -> Component detail review).

## Linked Concepts
- [[concepts/infrastructure-dev/figma-make|Figma Make]]
- [[concepts/infrastructure-dev/design-automation|Design Automation]]
- [[concepts/ai-agents/ai-visual-collaboration|AI Visual Collaboration]]
- [[concepts/infrastructure-dev/design-review-automation|Design Review Automation]]

## Key Decisions
- **Decision:** Utilize a custom web-based slide generator (`bonnyt` skill) to create one-pager HTML comparison reports rather than doing manual write-ups.
- [[decisions/dual-track-review-prd-to-code|Decision: Dual-Track Review & PRD-to-Code Workflow]]

## Tasks & Next Steps
- [ ] Refine the prompt logic to handle exact 1:1 margin and layout replication in Figma.
- [ ] Resolve scaling/cropping issues when original reference pictures are too small.
- [ ] Implement the "AI Decision Explainability" prompt so the agent explains *why* it chose specific components during the Human Review phase.
