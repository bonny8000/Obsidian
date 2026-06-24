---
type: concept
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [concept, agent-loop, loop-engineering, verification-loop, harness, reliability]
sources: [langchain-loop-engineering]
confidence: 0.8
---

# Loop Engineering

> [!abstract] Summary
> Designing an agent's control flow as a **stack of nested loops** — the core agent loop (model → tool → observation), a **verification loop** (grade → feedback → retry), event-driven triggers, and a hill-climbing/improvement loop — each instrumented and independently improvable.

> [!important] Why it Matters
> Much of an agent's reliability lives in the **loop**, not just the prompt or model: how iteration is structured, when it stops, what context each turn carries, and how feedback drives correction. Treating the loop as an engineered, observable object is what turns a demo into a dependable agent.

## 📝 Key Claims
- The agent is a **loop**, not a single call: model proposes → tool runs → observation feeds back → repeat until a stopping condition.
- A **verification loop** wraps the agent in a grader (deterministic check or [[concepts/ai-agents/agent-verifiers|LLM-as-judge verifier]]) that returns the output plus feedback for retry until it passes a rubric.
- Loops nest and compose; each should be **instrumented** (observable) so you can see and improve it.
- Stopping conditions, retry/backoff, and per-turn context discipline are first-class design decisions.

## 🔗 Related Concepts
- [[concepts/ai-agents/harness-engineering|Harness Engineering]]
- [[concepts/ai-agents/model-harness|Model Harness]]
- [[concepts/ai-agents/agent-verifiers|Agent Verifiers]]
- [[concepts/ai-agents/agentic-rag|Agentic RAG]]
- [[concepts/ai-agents/long-horizon-tasks|Long-Horizon Tasks]]
- [[concepts/ai-agents/self-improving-agent-workflows|Self-Improving Agent Workflows]]

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> More loops = more latency/cost, and loops can misfire: [[sources/bayer-prince-reliable-agentic-ai|Bayer PRINCE]] *removed* a net-negative LLM-review loop, and [[sources/fowler-sensors-coding-agents|Böckeler]] warns of feedback-overload spirals. Each loop must earn its place. Vendor lens (LangChain/LangGraph).

## 📚 Sources
- [[sources/langchain-loop-engineering|Runkle (2026): The Art of Loop Engineering]]

## ❓ Open Questions
- How to decide which loops are worth their latency/cost?
- How to detect a loop that's degrading rather than improving output?
