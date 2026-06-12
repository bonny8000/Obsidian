---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.72
---

# Which artifact format should be the canonical handoff: Markdown, JSON, Figma, code comments, or MCP resources?

## Short Answer
MCP resources are the most robust canonical handoff format for planning-to-code workflows because they let a coding agent consume planning artifacts directly without copy-paste. Markdown is the best human-readable format for review and version control. In practice, the two complement each other: Markdown is the source of truth, and an MCP server exposes it to agents. Figma and code comments are secondary artifacts downstream, not canonical handoffs.

## Evidence
- [[concepts/ai-agents/mcp-integration|MCP Integration]] ??"If product planning tools expose PRDs, specs, and flows through MCP, coding agents can consume planning context without copy-paste handoff."
- [[concepts/ai-agents/planning-to-code-workflow|Planning-to-Code Workflow]] ??"The handoff works best when artifacts are structured, current, and source-grounded."
- [[concepts/infrastructure-dev/llm-wiki|LLM Wiki]] ??The wiki itself uses Markdown as its source of truth and the agent reads it directly. The same pattern applies to planning artifacts.
- [[sources/manyfast-homepage|Manyfast Product Website]] ??"Planning documents can become machine-readable inputs for coding agents." MCP is the structured channel for machine readability.

## Follow-up Sources Needed
- MCP resource schema standards for planning artifacts (PRD, user flow, wireframe reference).

