---
type: concept
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [concept, multi-agent, architecture, orchestration, subagents, handoffs, router]
sources: [langchain-multi-agent-architecture]
confidence: 0.8
---

# Multi-Agent Architecture (Four Patterns)

> [!abstract] Summary
> Four patterns for combining specialized agent capabilities into one coherent system — **Subagents**, **Skills**, **Handoffs**, **Router** — each making a different tradeoff in control, state, parallelism, latency, and cost. Start single-agent; graduate only at clear limits.

> [!important] Why it Matters
> As agent capabilities sprawl, two pressures push toward multi-agent: **context management** (specialized knowledge won't fit one prompt) and **distributed development** (different teams own different capabilities). But multi-agent adds latency/tokens, so the *pattern* must match the constraint.

## 📝 Key Claims
- **Subagents** — centralized orchestration: a supervisor calls **stateless** subagents as tools; strong context isolation; costs **+1 model call** per interaction (results flow back through the supervisor); great for parallel, multi-domain work.
- **Skills** — progressive disclosure: a single agent loads specialized prompts/knowledge on demand ("quasi-multi-agent"); lightweight, direct user interaction; risk = **token bloat** as skills accumulate in history.
- **Handoffs** — state-driven: the *active* agent switches via handoff tool calls, state surviving across turns; best for sequential/staged flows (e.g. support); most stateful.
- **Router** — stateless classify → parallel dispatch → synthesize; best for distinct verticals queried in parallel.
- **Decision axes:** distributed development, parallelization, multi-hop, direct user interaction. **Performance:** on multi-domain tasks Subagents used ~67% fewer tokens than Skills (context isolation); stateful patterns (Skills/Handoffs) save ~40% of calls on repeats. Anthropic's multi-agent research system (Opus-4 lead + Sonnet-4 subagents) beat single-agent Opus-4 by **90.2%**.
- Guidance: **"Add tools before adding agents."** Start single; graduate deliberately.

## 🔗 Related Concepts
- [[concepts/ai-agents/multi-agent-coordination|Multi-Agent Coordination]]
- [[concepts/ai-agents/orchestrator-of-agents|Orchestrator of Agents]]
- [[concepts/ai-agents/agent-skills|Agent Skills]]
- [[concepts/ai-agents/progressive-disclosure|Progressive Disclosure]]
- [[concepts/ai-agents/deep-agents|Deep Agents]]
- [[concepts/ai-agents/context-engineering|Context Engineering]]
- [[concepts/ai-agents/harness-engineering|Harness Engineering]]

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> Direct tension with [[concepts/ai-agents/multi-agent-coordination|the coordination gap]] (CooperBench: two coding agents collaborating do *worse* than one). Reconciliation: LangChain's gains come from **centralized, context-isolated orchestration** (Subagents/Router) where a supervisor controls routing — *not* from peer agents freely negotiating, which is exactly what CooperBench found agents bad at. So: structure the coordination; don't let agents free-negotiate. Vendor lens (promotes LangChain/Deep Agents).

## 📚 Sources
- [[sources/langchain-multi-agent-architecture|Runkle (2026): Choosing the Right Multi-Agent Architecture]]

## ❓ Open Questions
- At what measurable point should a single agent graduate to multi-agent?
- How do these patterns' coordination assumptions hold up against CooperBench-style conflict tasks?
