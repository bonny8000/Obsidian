---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.68
---

# Which code review checklist should be attached to Bonny's vibe-coding workflow?

## Short Answer
A minimal vibe-coding review checklist: (1) diff inspection?ead every changed line, not just the output; (2) test coverage check?nsure the new code has at least a smoke test; (3) design-system compliance?heck that any UI changes use the correct tokens and components; (4) no hardcoded values that should be tokens or config; (5) version control checkpoint?ommit before the next prompt so rollback is easy; and (6) behavior verification in browser or runtime, not only in the model's description of what it did.

## Evidence
- [[concepts/ai-agents/vibe-coding|Vibe Coding]] ??"The workflow requires tests, diffs, version control, and review because generated code can still be wrong. Vibe coding is strongest when paired with project context and clear coding standards."
- [[concepts/ai-agents/claude-code|Claude Code]] ??"The CLI is framed as the earliest and most powerful product surface for coding tasks." CLI diffs and version control are the operational tools for this checklist.
- [[concepts/infrastructure-dev/design-system-implementation|Design System Implementation]] ??"Design-system implementation must verify rendered output, not only code-level configuration." Item 3 comes from this.
- [[sources/brunch-ghidesigner-482|Vibe Design and Coding with Claude Design and Claude Code]] ??"Coding agents are positioned as project-aware collaborators that can inspect a local codebase and run validation steps."

## Follow-up Sources Needed
- A standard AI-assisted coding review checklist from a software engineering team that has used vibe-coding workflows in production.

