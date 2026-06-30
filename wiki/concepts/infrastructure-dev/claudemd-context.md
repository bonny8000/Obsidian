---
type: concept
status: active
created: 2026-06-01
updated: 2026-06-29
tags: [ai, claude, instructions, context]
sources:
  - lennys-podcast-cat-wu-ai-pm-claude-code
  - sources/christinevallaure-human-approach-agentic-ai
confidence: 0.95
---

# ClaudeMD Context

## Summary
ClaudeMD Context refers to the use of `.md` files (like `CLAUDE.md` and `GEMINI.md`) as standardized, machine-readable instructions and memory for AI agents (specifically Claude and Gemini) operating within a local workspace or repository.

## Key Primitives
- **Instruction Files:** `CLAUDE.md` for team/repo rules; `GEMINI.md` for agent-specific mandates.
- **Context Injection:** The process of automatically loading these files into the LLM's prompt window at the start of a session.
- **Durable Memory:** Using the file system as a persistent storage layer for agent preferences and project history.

## Why it matters
It solves the "amnesia" problem of stateless LLMs. By storing instructions in the repository, teams can ensure that AI agents behave consistently across different machines and users, adhering to local coding standards and architectural decisions.

## Key Claims
- **A single CLAUDE.md can carry an entire multi-agent system.** Vallaure's ~106-line `CLAUDE.md` defines five role/voice/rule personas (≈7 lines each) plus on-demand folders read only when needed — "not code... read and edited in any text editor" — the substrate for [[concepts/ai-agents/markdown-agent-orchestration|markdown agent orchestration]] ([[sources/christinevallaure-human-approach-agentic-ai|Vallaure, 2026]]).
- **Lean beats elaborate.** Stripping an over-specified setup (backstories, unnecessary file reads) measurably improved speed — context engineering as subtraction.

## Related Concepts
- [[concepts/ai-agents/ai-maintained-wiki|AI-Maintained Wiki]]
- [[concepts/ai-agents/claude-code|Claude Code]]
- [[concepts/infrastructure-dev/knowledge-linting|Knowledge Linting]]
- [[concepts/ai-agents/markdown-agent-orchestration|Markdown Agent Orchestration]] · [[concepts/ai-agents/persona-agent|Persona Agent]]

## Sources
- [[sources/christinevallaure-human-approach-agentic-ai|Christine Vallaure (2026): A Human Approach to Agentic AI]]
