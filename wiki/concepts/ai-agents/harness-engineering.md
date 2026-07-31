---
type: concept
status: active
created: 2026-05-21
updated: 2026-07-31
tags: [concept, ai-engineering, systems-design, harness, delegation, modes, guardrails]
sources: [sources/pxd-story-ai-insights, sources/maily-product-makers-planning-harness, karrot-kraft-design-system-agent, maily-product-makers-guardrails]
confidence: 0.78
---

# Harness Engineering

> [!abstract] Summary
> The discipline of designing the environment, constraints, and feedback loops (the "harness") in which AI agents operate.

> [!important] Why it Matters
> Shift in design focus from building UIs for humans to building environments where agents can perform reliably and safely.

## Key Claims
- Control is achieved through environment design rather than micromanaging the model.
- Includes observability, evaluation frameworks, and safety guardrails.
- **Applied to product planning** as a [[concepts/product-management/planning-harness|Planning Harness]] ([[sources/maily-product-makers-planning-harness|Product Makers Note, 2026]]): the four reusable elements are **context** (embed policy), **tool definition** (restrict to skills), **guardrails** (human approval), and **validation** (self-check vs. intent).
- **A worked production harness** ([[wiki/sources/karrot-kraft-design-system-agent|Karrot's Kraft]]): built after a multi-agent design was tried and abandoned for communication overhead and context loss. Its shape is the transferable part:
  - **Modes, not agents.** One harness holds two modes — *Plan* (decides and stops for approval) and *Orchestra* (end-to-end). The mode difference is enforced by **tool availability**: Plan mode simply does not have the code-writing tool.
  - **Delegate outward where a mature tool exists.** Code-writing goes to Claude Code via the Claude Agent SDK, spawned as a local binary with a whitelist of file and search tools plus one docs MCP — *"an adapter that embeds Claude Code as a tool."* Keep the contextual judgment inside; borrow the solved capability.
  - **Knowledge as loadable modules, not prompt bulk.** Seven markdown [[concepts/ai-agents/skill-system|skills]] load on demand rather than sitting in the system prompt.
  - **Ambiguity routes to a question.** Neither guess nor refuse — ask.
- **Guardrails inside the harness are themselves layered** ([[wiki/sources/maily-product-makers-guardrails|Product Makers Note #24]]): prompt, model tuning, and a separate inspection API, deployed in the inverse of their strength order because cost and time run the other way. See [[concepts/ai-agents/layered-content-guardrails|Layered Content Guardrails]].

## Related Concepts
- [[concepts/ai-agents/model-harness|Model Harness]]
- [[concepts/ai-agents/agentic-ai|Agentic AI]]
- [[concepts/product-management/planning-harness|Planning Harness]]
- [[concepts/ai-agents/loop-engineering|Loop Engineering]]
- [[concepts/ai-agents/layered-content-guardrails|Layered Content Guardrails]]
- [[concepts/ai-agents/multi-agent-architecture|Multi-Agent Architecture]] — what Karrot tried before the harness
- [[concepts/ai-agents/design-spec-intermediate-representation|Design Spec as Intermediate Representation]]
- [[concepts/ai-agents/generated-output-scoring|Generated-Output Scoring]]

## Sources
- [[sources/pxd-story-ai-insights|pxd story: AI & UX Insights]]
- [[sources/maily-product-makers-planning-harness|Product Makers Note (2026): Build a Planning Harness]]
- [[wiki/sources/maily-product-makers-guardrails|Product Makers Note (2026, #24): Guardrails]] — the guardrail element expanded into three technical layers.
- [[wiki/sources/karrot-kraft-design-system-agent|Karrot (2026): Kraft]] — a production harness with modes, external delegation, loadable skills, and scoring.

## ??Open Questions
- What are the standardized components of a robust AI harness?

