---
type: concept
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [concept, agent-middleware, harness, hooks, composability, deep-agents]
sources: [langchain-agent-middleware, langchain-custom-agent-harness, langchain-box-ai-deep-agents]
confidence: 0.78
---

# Agent Middleware

> [!abstract] Summary
> A composable **interception layer** over an agent's loop — hooks that run **before/after model calls, before/after tool calls, and at startup/teardown** — that add cross-cutting capability (citations, caching, context summarization, guardrails) without rewriting the agent.

> [!important] Why it Matters
> Middleware is how you **customize a harness without forking it**: capability is added via deterministic logic, extra tools, custom state, and stream handlers at well-defined insertion points. In multi-agent (Deep Agents) setups it can also serve as the **inter-agent communication channel**.

## 📝 Key Claims
- Hook points: before/after the model call, before/after each tool call, plus startup and teardown.
- Adds capability through deterministic code, tools, custom state, and stream handlers — keeping the core loop intact.
- Cross-cutting uses: citation injection, caching, context summarization/compression, policy/guardrail enforcement, observability.
- In Deep Agents, middleware is part of how parent/child agents coordinate.

## 🔗 Related Concepts
- [[concepts/ai-agents/harness-engineering|Harness Engineering]]
- [[concepts/ai-agents/model-harness|Model Harness]]
- [[concepts/ai-agents/loop-engineering|Loop Engineering]]
- [[concepts/ai-agents/deep-agents|Deep Agents]]
- [[concepts/ai-agents/context-engineering|Context Engineering]]

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> Powerful but can become a hidden complexity layer (ordering/interaction of many hooks). Framework-specific (LangChain/Deep Agents) — the *pattern* transfers, the API doesn't. Vendor lens.

## 📚 Sources
- [[sources/langchain-agent-middleware|LangChain: Agent Middleware]] (canonical — the LangChain 1.0 origin post for this primitive)
- [[sources/langchain-custom-agent-harness|LangChain: How to Build a Custom Agent Harness]]
- [[sources/langchain-box-ai-deep-agents|Box × LangChain: Going AI-Native with Deep Agents]]

## ❓ Open Questions
- How to keep many middleware hooks debuggable and predictable in ordering?
