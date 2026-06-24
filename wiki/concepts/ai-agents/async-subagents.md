---
type: concept
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [concept, async-subagents, background-agents, multi-agent, orchestration, long-horizon]
sources: [langchain-background-subagents]
confidence: 0.78
---

# Async / Background Subagents

> [!abstract] Summary
> Background, **stateful, individually-addressable** subagents that a supervisor launches **non-blockingly** (it gets a task ID immediately) and can later **poll, update, or cancel** — "fire-and-steer" rather than fire-and-wait.

> [!important] Why it Matters
> Blocking subagents stall the supervisor while they run. Background subagents enable parallel long-running work, mid-flight steering, and better responsiveness for long-horizon tasks — but require a management/queue layer and a way to address each running agent.

## 📝 Key Claims
- Non-blocking launch returns a **handle/task ID**; the supervisor keeps working and checks back.
- Subagents are **stateful** and individually addressable, so they can be updated or cancelled in flight ("fire-and-steer").
- Needs a management surface (e.g. a set of queue tools) to list/inspect/update/cancel running subagents.
- A framework-agnostic **agent protocol** (threads / runs / status / updates / memory) decouples orchestration from *where* a subagent is deployed (local vs remote).

## 🔗 Related Concepts
- [[concepts/ai-agents/multi-agent-architecture|Multi-Agent Architecture]]
- [[concepts/ai-agents/deep-agents|Deep Agents]]
- [[concepts/ai-agents/orchestrator-of-agents|Orchestrator of Agents]]
- [[concepts/ai-agents/long-horizon-tasks|Long-Horizon Tasks]]
- [[concepts/ai-agents/agent-middleware|Agent Middleware]]
- [[concepts/ai-agents/multi-agent-coordination|Multi-Agent Coordination]]

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> Background + addressable agents add real coordination/state complexity — and inherit the [[concepts/ai-agents/multi-agent-coordination|coordination-gap]] risk unless the supervisor stays in control. Vendor lens (LangChain/LangGraph).

## 📚 Sources
- [[sources/langchain-background-subagents|LangChain: Running Subagents in the Background]]

## ❓ Open Questions
- How does fire-and-steer interact with the coordination gap — does supervisor control fully mitigate it?
- What's the right UX for surfacing many in-flight background agents to a human?
