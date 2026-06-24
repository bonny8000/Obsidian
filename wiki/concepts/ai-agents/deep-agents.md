---
type: concept
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [concept, deep-agents, long-running-agents, subagents, planning, langchain]
sources: [langchain-box-ai-deep-agents, langchain-multi-agent-architecture, langchain-evaluating-deep-agents]
confidence: 0.78
---

# Deep Agents

> [!abstract] Summary
> LangChain's open-source framework for **long-running agents on complex tasks** — bundling planning, **subagents**, **skills**, a file-system/"memory", and **middleware** — and usable **recursively** (a parent and its children are all Deep Agents, children invoked as tools, each with isolated context).

> [!important] Why it Matters
> It packages the Subagents + Skills patterns into an out-of-the-box way to tackle multi-step, long-horizon work, so teams don't hand-build orchestration. Box used it to go "AI-native" over its content platform.

## 📝 Key Claims
- **Recursive composition:** parent + child agents are all Deep Agents; children are exposed as tools; each child gets an **isolated context** (context isolation = the token-efficiency win from the Subagents pattern).
- Built-ins: a **planner**, subagents, skills (progressive disclosure), a virtual file system / memory, and a **middleware** bus for cross-cutting behavior + inter-agent communication.
- Aimed at **long-running / complex** tasks rather than single-shot Q&A.
- A concrete implementation of [[concepts/ai-agents/multi-agent-architecture|the Subagents + Skills patterns]].

## 🔗 Related Concepts
- [[concepts/ai-agents/multi-agent-architecture|Multi-Agent Architecture]]
- [[concepts/ai-agents/agent-skills|Agent Skills]]
- [[concepts/ai-agents/orchestrator-of-agents|Orchestrator of Agents]]
- [[concepts/ai-agents/long-horizon-tasks|Long-Horizon Tasks]]
- [[concepts/ai-agents/agent-middleware|Agent Middleware]]
- [[concepts/ai-agents/agentic-rag|Agentic RAG]]
- [[concepts/ai-agents/agent-trajectory-evaluation|Agent Trajectory Evaluation]]

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> A LangChain framework — adopting it is also adopting LangChain's stack/abstractions. Recursive subagents inherit the [[concepts/ai-agents/multi-agent-coordination|coordination-gap]] risk unless orchestration stays centralized/context-isolated. Vendor lens.

## 📚 Sources
- [[sources/langchain-box-ai-deep-agents|Box × LangChain: Going AI-Native with Deep Agents]]
- [[sources/langchain-multi-agent-architecture|Runkle (2026): Choosing the Right Multi-Agent Architecture]]
- [[sources/langchain-evaluating-deep-agents|LangChain: Evaluating Deep Agents — Our Learnings]]

## ❓ Open Questions
- How deep does recursion stay reliable before coordination/cost dominates?
