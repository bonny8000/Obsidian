---
type: concept
status: active
created: 2026-06-25
updated: 2026-06-25
tags: [planning-harness, harness-engineering, ai-pm, product-planning, skills, guardrails, claudemd]
sources:
  - sources/maily-product-makers-planning-harness
confidence: 0.78
---

# Planning Harness

## Summary

A **planning harness** is [[concepts/ai-agents/harness-engineering|harness engineering]] applied to product planning: a repo-shareable system (rules file + skills + reference spec) that turns ad-hoc AI chat into a controlled, repeatable pipeline for producing planning artifacts (specs, sequence diagrams, user flows).

## Why It Matters

PMs get good high-level strategy help from AI but revert to manual detailed planning, and edits blow up the AI's context. A harness moves the PM from **"AI sitter"** (babysitting hallucinations) to **"planning harness engineer"** (designing guardrails), making planning output consistent across sessions and teammates.

## Key Claims

- **Four principles:** **Context** (embed core service policy permanently), **Tool definition** (restrict to predefined skills), **Guardrails** (human approval for sensitive decisions), **Validation** (self-check output against original intent).
- **Harness ≠ file-sharing:** permanent pipeline (no per-session setup), real execution (AI edits local files like `spec.md`, `flow.mermaid`), and a team asset (GitHub-shareable, consistent results).
- **10-minute setup:** folder → rules file (`CLAUDE.md` / `.cursorrules` / `.clinerules`) → custom skills (`/sequence_diagram`, `/user-flow`, `/make-html`) → reference `spec.md` → optional GitHub push.
- Same primitive family as [[concepts/ai-agents/agent-skills|Agent Skills]] + [[concepts/infrastructure-dev/claudemd-context|CLAUDE.md Context]]: the PM authors procedural memory + context, not one-off prompts.

## Related Concepts

- [[concepts/ai-agents/harness-engineering|Harness Engineering]] — the general parent pattern.
- [[concepts/ai-agents/agent-skills|Agent Skills]] — the "tool definition" primitive.
- [[concepts/infrastructure-dev/claudemd-context|CLAUDE.md Context]] — the "context" primitive.
- [[concepts/ai-agents/prd-generation|PRD Generation]] / [[concepts/product-management/ai-prd|AI PRD]] — validation-against-intent ≈ spec/eval discipline at planning time.
- [[concepts/product-management/ai-pm-skills|AI PM Skills]]

## Conflicts & Caveats

> [!warning] Unproven efficacy
> Practitioner how-to, no metrics. "Validation = AI self-checks intent" is fallible (LLM judging itself) — keep human approval gates. Up-front setup pays off only with repeated, structured tasks.

## Sources

- [[sources/maily-product-makers-planning-harness|Product Makers Note: Build a Planning Harness (2026)]]

## Open Questions

- Break-even: how many planning cycles before a harness beats ad-hoc prompting?
- How does the harness stay in sync when underlying service policy changes (context drift)?
