---
type: concept
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [concept, ai-prototyping, design-to-code, templates, design-system, hallucination-control]
sources: [atlassian-ai-prototyping-handshakes, figma-mcp-server-four-ways]
confidence: 0.8
---

# AI Prototyping

> [!abstract] Summary
> Generating high-fidelity, design-system-grounded prototypes from prompts or screenshots in minutes, using preconfigured templates plus structured config to keep outputs consistent and curb hallucination.

> [!important] Why it Matters
> It turns design–engineering "handoffs into handshakes": wireframes, specs, and code now happen in minutes, and a design system can stay in sync at enterprise scale. It also democratizes prototyping to less-experienced practitioners — while still needing human review for the last mile.

## 📝 Key Claims
- From a screenshot, AI prototyping can reach ~70% design-system accuracy in one pass, improving over iterations.
- Templates (e.g., Fast for speed, Full for complex interaction) plus a JSON config for safe choices beat open-ended prompting — structured constraints drove hallucinations toward zero.
- Preconfigured code improves screenshot matching because the model leans on real component APIs.
- The design system is the single source of truth; "the first 80%" is automated, then a human reviews, swaps placeholders, and edits.
- Production-quality code at scale remains hard; prototypes look/feel right but discovery and code quality are still works in progress.

## 🔗 Related Concepts
- [[concepts/infrastructure-dev/design-to-code-workflow|Design-to-Code Workflow]]
- [[concepts/infrastructure-dev/wireframe-generation|Wireframe Generation]]
- [[concepts/infrastructure-dev/figma-make|Figma Make]]
- [[concepts/infrastructure-dev/scaffold-design-system|Scaffold Design System]]
- [[concepts/infrastructure-dev/agentic-content|Agentic Content]]
- [[concepts/ai-agents/vibe-coding|Vibe Coding]]

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> Speed can outrun quality: "production-quality code at scale remains challenging." Pair with [[concepts/ux-research/process-literacy|Process Literacy]] — fast prototyping does not remove the need to frame the problem.

## 📚 Sources
- [[sources/atlassian-ai-prototyping-handshakes|Atlassian: Turning Handoffs into Handshakes]]
- [[sources/figma-mcp-server-four-ways|Figma: 4 Ways We're Using Our MCP Server]]

## ❓ Open Questions
- How far can one-pass design-system accuracy rise before human review is mostly about taste?
- How do teams keep prototypes from silently shipping as production code?
