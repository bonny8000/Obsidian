---
type: concept
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [concept, agentic-content, llms-txt, context-layer, design-system, instructions]
sources: [atlassian-ai-prototyping-handshakes, atlassian-design-system-context-engine, figma-mcp-server-four-ways]
confidence: 0.8
---

# Agentic Content

> [!abstract] Summary
> The maintained, structured, plain-language instructions, examples, and constraints fed to agents and LLMs (e.g., `llms.txt` manifests, a single `guidelines.md`, per-package building blocks) so they know what to do and produce correct outputs.

> [!important] Why it Matters
> It is the maintainable content layer that powers MCP servers, AI prototyping tools, and AI code editors. Atlassian's lesson: "to identify the rules that help LLMs, you also uncover the rules that help explain these concepts to humans" — making content AI-legible makes it human-legible too.

## 📝 Key Claims
- A single well-structured file often beats many files because prototyping tools struggle to parse multiple files for context.
- Put a table of contents plus a few high-priority instruction lines at the top to speed generation and reduce hallucinations.
- Break prompts/docs into structured building blocks — guidance, examples, types, keywords, metadata — organized per package and routed to the right outputs.
- The discipline shifts from "what should we tell the model?" to "how do we keep these instructions accurate, maintained, and benchmarked?"

## 🔗 Related Concepts
- [[concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]]
- [[concepts/infrastructure-dev/design-md|DESIGN.md]]
- [[concepts/ai-agents/mcp-integration|MCP Integration]]
- [[concepts/infrastructure-dev/claudemd-context|CLAUDE.md Context]]
- [[concepts/ai-agents/agent-skills|Agent Skills]]
- [[concepts/infrastructure-dev/token-efficiency|Token Efficiency]]

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> Maintaining agentic content is ongoing work (Atlassian spent ~6 months "taming the complexity"); without evals/benchmarking it can drift from the real system it describes.

## 📚 Sources
- [[sources/atlassian-ai-prototyping-handshakes|Atlassian: Turning Handoffs into Handshakes]]
- [[sources/atlassian-design-system-context-engine|Atlassian: Building the Context Engine for the AI Era]]
- [[sources/figma-mcp-server-four-ways|Figma: 4 Ways We're Using Our MCP Server]]

## ❓ Open Questions
- How is agentic content kept consistent with code/design as both evolve?
- What does automated evaluation/benchmarking of instruction content look like?
