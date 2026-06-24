---
type: concept
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [concept, agentic-search, web-research, retrieval, multi-agent, rag]
sources: [langchain-exa]
confidence: 0.78
---

# Agentic Search

> [!abstract] Summary
> Autonomous, agent-driven web search that **plans a query, runs multiple parallel retrieval tasks, and returns structured findings** — the evolution from "search API → answers → deep-research agent," as opposed to single-shot search or static RAG.

> [!important] Why it Matters
> Complex research questions need decomposition, multi-source parallel retrieval, and synthesis. Agentic search is the *retrieval* counterpart to [[concepts/ai-agents/agentic-rag|agentic RAG]] — and a building block for deep-research agents.

## 📝 Key Claims
- A **Planner / Tasks / Observer** multi-agent structure decomposes a question, runs retrieval tasks in parallel, and synthesizes.
- **Selective inter-task context:** peer tasks see only each other's final cleaned outputs (not raw context) — context isolation for efficiency.
- **Snippet-first, then full-content** retrieval to control cost/latency.
- **Structured JSON output** for programmatic (API) consumption.
- **Token-usage observability** drives pricing (cost-as-a-system).

## 🔗 Related Concepts
- [[concepts/ai-agents/agentic-rag|Agentic RAG]]
- [[concepts/ai-agents/multi-agent-architecture|Multi-Agent Architecture]]
- [[concepts/ai-agents/mcp-integration|MCP Integration]]
- [[concepts/ai-agents/ai-news-intermediary|AI as News Intermediary]]
- [[concepts/ai-agents/long-horizon-tasks|Long-Horizon Tasks]]

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> Agentic search inherits AI-news-intermediary risks (retrieval fidelity, source divergence, which sources get surfaced) and multi-agent coordination cost. Vendor/partner lens (Exa × LangChain); operational metrics only, no quality numbers.

## 📚 Sources
- [[sources/langchain-exa|Exa × LangChain: Agentic Web Search]]

## ❓ Open Questions
- How is retrieval *fidelity/quality* measured for agentic search (vs just latency/throughput)?
- How does selective inter-task context affect synthesis quality vs cost?
