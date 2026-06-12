---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.70
---

# What should an MCP server expose from a product planning workspace?

## Short Answer
A planning workspace MCP server should expose: (1) the current PRD as a structured resource with goals, user problems, and acceptance criteria; (2) user flows as navigable step sequences; (3) wireframe references with component annotations; (4) open decisions and their current status; and (5) a changelog of planning changes with timestamps. These give a coding agent the context it needs without forcing it to read unstructured chat history.

## Evidence
- [[concepts/ai-agents/mcp-integration|MCP Integration]] ??"Integration quality depends on structured resources and clear permission boundaries. MCP-connected planning data should remain reviewable and source-grounded."
- [[concepts/ai-agents/planning-to-code-workflow|Planning-to-Code Workflow]] ??"Planning artifacts can become inputs to coding agents. The handoff works best when artifacts are structured, current, and source-grounded."
- [[concepts/ai-agents/prd-generation|PRD Generation]] ??"PRDs become more useful when linked to specs, flows, wireframes, and implementation tasks." An MCP server should surface these links.
- [[sources/manyfast-homepage|Manyfast Product Website]] ??"AI planning tools can structure product ideas into PRDs, functional specs, user flows, and wireframes." These are the exact resource types to expose.

## Follow-up Sources Needed
- MCP specification for resource types and whether structured JSON resources are more useful than Markdown text resources for coding agents.

