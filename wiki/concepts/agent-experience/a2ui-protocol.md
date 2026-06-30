---
type: concept
status: active
created: 2026-06-29
updated: 2026-06-29
tags: [a2ui, agent-protocol, generative-ui, agent-experience, ag-ui, mcp-ui, agent-to-ui, radically-adaptive-ui]
sources:
  - sources/christinevallaure-a2ui-generative-ui
confidence: 0.78
---

# A2UI Protocol

## Summary

A2UI ("Agent-to-UI") is an open protocol — initiated by Google and refined by CopilotKit and others — for building generative / radically adaptive UI under constraint. Instead of an agent emitting arbitrary markup, A2UI runs a four-step loop: (1) a plain-language request → (2) a server bundles request + a machine-readable component catalog + instructions for an LLM → (3) the model returns a structured JSONL "recipe" of components and arrangement → (4) a renderer builds the screen using catalog components only. The protocol is at spec version v0.9 and sits alongside a wider ecosystem of agent-UI protocols: AG-UI, A2A, MCP-UI, and Vercel's json-render, plus an A2UI Agent SDK and reference demos (e.g. Southleft).

## Why It Matters

A2UI is a concrete pattern for pulling open-ended generative UI back toward deterministic guarantees: the model can only name components that exist in the [[concepts/infrastructure-dev/component-catalog|catalog]], which keeps output on-brand and blocks "div soup." The recipe/renderer split is also an agent-experience surface — it bears on how users trust agent-generated screens and how gracefully the system degrades when the catalog lacks the right piece (the quiet-downgrade failure mode). For designers, it relocates the quality lever from per-screen craft to catalog design.

## Key Claims

- A2UI is an open, Google-initiated protocol (refined by CopilotKit and others) that constrains AI-generated UIs to pre-designed catalog components ([[sources/christinevallaure-a2ui-generative-ui|Vallaure, 2026]]).
- The four-step loop is request → server bundles request+catalog+instructions → model returns a JSONL recipe → renderer builds from catalog components only.
- Validation against the catalog is the protocol's security boundary, checked before and after generation.
- A2UI is one of several early agent-UI protocols (AG-UI, A2A, MCP-UI, Vercel json-render); how they relate or compete is unresolved, and the spec is at v0.9.
- The dominant failure mode is the quiet downgrade when the catalog is incomplete — the protocol does not guarantee good design, only valid assembly.

## Related Concepts

- [[concepts/infrastructure-dev/component-catalog|Component Catalog]] — the authorized palette A2UI renders from.
- [[concepts/ux-research/generative-ui|Generative UI]] — A2UI is a constrained, catalog-bounded form of it.
- [[concepts/infrastructure-dev/deterministic-ui|Deterministic UI]] — catalog validation reclaims determinism guarantees.
- [[concepts/agent-experience/agent-transparency|Agent Transparency]] — the recipe/renderer split shapes trust in generated screens.
- [[concepts/ai-agents/mcp-integration|MCP Integration]] — sibling agent-context plumbing (MCP-UI is named in the same ecosystem).
- [[concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]] · [[concepts/infrastructure-dev/design-to-code-workflow|Design-to-Code Workflow]]
- [[concepts/ux-research/designing-for-agency|Designing for Agency]]

## Conflicts & Caveats

> [!warning] Early spec, single-author explainer
> A2UI is at v0.9 and the surrounding protocols are early; specifics will move. The source is a single educational explainer, not the canonical spec — verify protocol details against authoritative docs. No studies or metrics show A2UI ships better real-world UX than static design or chat; the acknowledged failure modes are unquantified.

## Sources

- [[sources/christinevallaure-a2ui-generative-ui|Christine Vallaure (2026): A2UI Under the Hood — Designing for Radically Adaptive UI]]

## Open Questions

- What is the canonical A2UI spec at v0.9, and how do A2UI, AG-UI, A2A, MCP-UI, and json-render relate or compete?
- Does constrained-catalog generative UI measurably beat static design or chat on task success / satisfaction?
- How is catalog coverage governed so quiet downgrades are caught before users see them?
