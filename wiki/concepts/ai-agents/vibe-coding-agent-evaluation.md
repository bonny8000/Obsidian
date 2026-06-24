---
type: concept
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [concept, agent-evaluation, vibe-coding, alignment, observability, glass-box]
sources: [vibe-coding-agent-security-evaluation-day-4]
confidence: 0.78
---

# Vibe-Coding Agent Evaluation

> [!abstract] Summary
> Evaluating intent-driven coding agents on whether their output is **"actually worth shipping"** — a distinct axis from security ("did the agent stay inside the boundary?"). It opens the **"glass box"** to measure the quality, efficiency, and alignment of the agent's *reasoning*, not just pass/fail tests.

> [!important] Why it Matters
> A vibe-coded agent can **pass every security check and still fundamentally misread intent**, ignore project conventions, or silently degrade UX. Deterministic tests don't capture whether the agent did the *right* thing or reasoned well — so evaluation needs its own discipline, with observability as a prerequisite.

## 📝 Key Claims
- **Two axes of trust:** Security = stayed in bounds; **Evaluation = worth shipping**. Both are required; neither implies the other.
- Evaluate the **internal reasoning** (the "glass box"): quality, efficiency, and alignment with the developer's intent and conventions — not only final outputs.
- **Observability is the prerequisite** — you can't evaluate what you can't trace (the "vibe trajectory").
- Frames *what* to evaluate, *how* to evaluate, and applied tips for intent-driven agentic systems.

## 🔗 Related Concepts
- [[concepts/ai-agents/agent-security-architecture|Agent Security Architecture]]
- [[concepts/ai-agents/product-evals|Product Evals]]
- [[concepts/ux-research/ai-evals|AI Evals]]
- [[concepts/agent-experience/agent-evaluation-ux|Agent Evaluation UX]]
- [[concepts/agent-experience/satisfaction-vs-benefit|Satisfaction vs Benefit]]

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> "Worth shipping ≠ passes tests" parallels [[concepts/agent-experience/satisfaction-vs-benefit|satisfaction ≠ benefit]] and "compiles ≠ safe": surface signals (green tests, clean compile, user thumbs-up) can all mask a bad outcome. The Day-4 evaluation half is captured at framing level; concrete metrics need deeper ingest.

## 📚 Sources
- [[sources/vibe-coding-agent-security-evaluation-day-4|Day 4 — Vibe Coding Agent Security and Evaluation]]

## ❓ Open Questions
- What concrete metrics/rubrics capture "intent alignment" and "reasoning quality"?
- How do you evaluate reasoning without exploding cost/latency?
