---
type: decision
status: active
created: 2026-06-01
updated: 2026-06-01
tags: [decision, ai-review, workflow, prd-to-code]
sources: [notion-sync]
---

# Decision: Dual-Track Review & PRD-to-Code Workflow

## Context & Background
As part of the "Evaluation UX [I]" meeting (and the broader From UX to AX vision), we needed to define how an AI Agent handles project workflows, specifically translating PRDs into interactive outputs while maintaining design quality.

## Options Considered
1. **Direct to Visuals:** AI generates static mockups straight from PRD. (High risk of missing UX states and logical flaws).
2. **Structured, Multi-Stage Generation & Review (Chosen):** AI must first generate intermediate specifications (Flow, UX rules) before rendering interactive code.

## Decision Made
We established three core operational rules for the AI Agent:
1. **Dual-Track Asset Generation:** The Agent must produce outputs readable by humans (visuals/code) AND standardized formats (SOP/specs) so the next Agent in the pipeline can pick up the work seamlessly.
2. **Top-Down Review Mechanism:** The Agent must review the "big picture" first (overall page structure, F-pattern navigation) before checking micro-details (component states, padding).
3. **AI Decision Explainability:** During the Human Review phase, the AI must explicitly state *why* it chose specific components, allowing designers to correct its logic.

## Evidence & Justification
- **Process Validation:** Testing showed that extracting the "Flow" from the PRD first, validating it, and *then* selecting components yields much higher accuracy.
- **Interoperability:** The final output is not a static image, but interactive React/Code that can run in a browser.
- Grounded in: [[concepts/ai-agents/ai-agent-workflow|AI Agent Workflow]]
- Grounded in: [[concepts/infrastructure-dev/design-to-code-workflow|Design-to-Code Workflow]]
- Supported by: [[concepts/infrastructure-dev/design-review-automation|Design Review Automation]]

## Consequences & Next Steps
This review tool and PRD-to-Code pipeline will be packaged so that non-designers (like PMs) can run a preliminary "Severity Check" on requirements before formal design review, filtering out major structural errors early.
