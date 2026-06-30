---
type: concept
status: active
created: 2026-05-18
updated: 2026-06-29
tags: [mcp, ai-agent, integration, tooling]
sources:
  - sources/manyfast-homepage
  - sources/christinevallaure-agentic-ai-design-systems
confidence: 0.72
---

# MCP Integration

## Summary

MCP integration connects an AI-capable tool or data source to agentic development environments through the Model Context Protocol.

## Why It Matters

If product planning tools expose PRDs, specs, and flows through MCP, coding agents can consume planning context without copy-paste handoff.

## Key Claims

- MCP can make planning artifacts available to development tools.
- Integration quality depends on structured resources and clear permission boundaries.
- MCP-connected planning data should remain reviewable and source-grounded.
- **Design tools expose context via MCP too.** The Figma MCP (and a Storybook MCP) is how agents read component context — including component *descriptions* authored in Figma, which the MCP feeds to the agent — making MCP a load-bearing part of an agent-readable [[concepts/infrastructure-dev/ai-native-design-system|design system]] ([[sources/christinevallaure-agentic-ai-design-systems|Vallaure, 2026]]).

## Related Concepts

- [[concepts/ai-agents/planning-to-code-workflow|Planning-to-Code Workflow]]
- [[concepts/ai-agents/ai-agent-workflow|AI Agent Workflow]]
- [[concepts/product-management/ai-product-planning|AI Product Planning]]
- [[concepts/ux-research/ux-research-automation|UX Research Automation]]
- [[concepts/infrastructure-dev/figma-code-connect|Figma Code Connect]] — read over the Figma MCP.

## Sources

- [[sources/manyfast-homepage|Manyfast Product Website]]
- [[sources/user-interviews-ai-assistant|User Interviews AI Assistant]] — MCP early access for running recruitment/research within AI agents.
- [[sources/christinevallaure-agentic-ai-design-systems|Vallaure (2026): Agentic AI, Design Systems & Figma]] — Figma/Storybook MCP feeding component context to agents.

## Open Questions

- [Answered → [[queries/2026-05-27-mcp-server-planning-workspace|Query Page]]] What should an MCP server expose from a product planning workspace?

