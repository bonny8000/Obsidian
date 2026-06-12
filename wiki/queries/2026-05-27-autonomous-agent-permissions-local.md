---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.65
---

# What permissions should autonomous agents have in Bonny's local workflow?

## Short Answer
Agents should have read access to the full vault and write access only to the wiki layer (wiki/concepts, wiki/sources, wiki/maps, wiki/queries, wiki/logs). They should not have write access to raw/ (immutable sources), system files, or external services unless explicitly approved per session. This matches the LLM Wiki architecture's principle of keeping the raw layer immutable and agent-maintained layers separate.

## Evidence
- [[concepts/ai-agents/autonomous-ai-agent|Autonomous AI Agent]] ??"Autonomy requires guardrails, approvals, and clear operating instructions." Scoped write access is the minimal-footprint implementation of this.
- [[maps/llm-wiki-architecture|LLM Wiki Architecture]] ??"The raw source layer should remain immutable." This directly defines the boundary for agent write permissions.
- [[concepts/ai-agents/agent-identity|Agent Identity]] ??"Long-running design or research agents need scoped access rather than broad ambient access."
- [[sources/brunch-ghidesigner-486|Hermes Agent AI for Designers]] ??"Agent workflows become more valuable when repeated successful patterns can be stored and reused." Scoped access makes the agent's operations auditable and reversible.

## Follow-up Sources Needed
- Claude Code permission model documentation for defining allowed vs. disallowed file paths in AGENTS.md or CLAUDE.md.

