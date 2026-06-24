---
type: concept
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [concept, agent-authorization, identity, security, confused-deputy, zero-trust]
sources: [langchain-agent-authorization]
confidence: 0.8
---

# Agent Authorization

> [!abstract] Summary
> The question of **who an agent authenticates as** when it takes an action: using the end-user's **delegated credentials** ("on-behalf-of") versus the agent having its **own fixed / service-account identity** — a choice with very different scoping and blast-radius properties.

> [!important] Why it Matters
> Agents take real actions (call APIs, move money, modify systems). Getting authorization wrong is exactly the **Confused Deputy** hole. The two models trade off cleanly: per-user scoping vs a shared blast radius.

## 📝 Key Claims
- **Type 1 — delegated / on-behalf-of:** the agent acts with the *user's* permissions (naturally per-user-scoped), but it inherits the user's **ambient** access — the classic Confused-Deputy risk if it's tricked.
- **Type 2 — own identity:** the agent has its own service-account credentials (clean separation), but **static, long-lived creds = a shared blast radius** — the "static identity is a poor perimeter" problem.
- LangChain's framing maps "Assistants" ≈ delegated identity and "Claws" ≈ own credentials.
- Reconciles with [[concepts/ai-agents/agent-security-architecture|Day-4 agent security]]: prefer a **distinct agentic identity** + **JIT downscoping** + human-in-the-loop for high-stakes actions, rather than broad delegated ambient access.

## 🔗 Related Concepts
- [[concepts/ai-agents/agent-security-architecture|Agent Security Architecture]]
- [[concepts/ai-agents/agent-identity|Agent Identity]]
- [[concepts/ai-agents/managed-ai-agents|Managed AI Agents]]
- [[concepts/ux-research/human-in-the-loop|Human-in-the-Loop]]
- [[concepts/agent-experience/agent-transparency|Agent Transparency]]

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> Neither model is "safe" by default: delegated risks Confused-Deputy; own-identity risks a fat static credential. The resolution (JIT, scoping, HITL) is operational, not a single right answer. Vendor lens (LangChain).

## 📚 Sources
- [[sources/langchain-agent-authorization|LangChain: Two Different Types of Agent Authorization]]
- [[sources/vibe-coding-agent-security-evaluation-day-4|Day 4 — Vibe Coding Agent Security & Evaluation]] (Confused Deputy / agentic identity)

## ❓ Open Questions
- When is delegated vs own-identity the right default for a given action class?
- How to scope an own-identity agent so its blast radius approximates per-user delegation?
