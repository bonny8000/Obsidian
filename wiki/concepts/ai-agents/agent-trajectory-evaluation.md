---
type: concept
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [concept, agent-evaluation, trajectory, deep-agents, evals, long-horizon]
sources: [langchain-evaluating-deep-agents]
confidence: 0.8
---

# Agent Trajectory Evaluation

> [!abstract] Summary
> Evaluating an agent by the **sequence of tool calls and arguments it produces** (its trajectory/path), not just its final output — including single-step decision checks and order-independent "was this tool called at some point" assertions.

> [!important] Why it Matters
> A long-horizon agent can reach a right answer via a bad path (wrong tool, bad args, wasteful loops) or a wrong answer via a reasonable path. Outcome-only evals miss process failures; trajectory evals catch them — essential for [[concepts/ai-agents/deep-agents|deep agents]].

## 📝 Key Claims
- A **3×3 eval matrix**: *ways to run* (single-step / full-turn / multi-turn) × *what to test* (trajectory / final-response / state).
- **Single-step** checks (e.g. `interrupt_before=["tools"]`) isolate one decision cheaply; LangChain found ~half of cases were single-step.
- **Bespoke per-datapoint assertions** (custom code per test) beat generic graders for trajectory.
- **Reset-per-test environments + API mocking** make trajectory tests deterministic and repeatable.
- Order-independent "tool-called-at-some-point" assertions avoid over-fitting to one valid path.

## 🔗 Related Concepts
- [[concepts/ai-agents/deep-agents|Deep Agents]]
- [[concepts/ai-agents/agent-verifiers|Agent Verifiers]]
- [[concepts/ai-agents/product-evals|Product Evals]]
- [[concepts/ux-research/ai-evals|AI Evals]]
- [[concepts/ai-agents/vibe-coding-agent-evaluation|Vibe-Coding Agent Evaluation]]
- [[concepts/ai-agents/loop-engineering|Loop Engineering]]

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> Trajectory evals are labor-intensive (bespoke assertions, mocked environments) and can over-fit to one "correct" path if written too strictly. Pair with outcome/state evals. Vendor lens (LangChain/LangSmith).

## 📚 Sources
- [[sources/langchain-evaluating-deep-agents|LangChain: Evaluating Deep Agents — Our Learnings]]

## ❓ Open Questions
- How to write trajectory assertions that tolerate multiple valid paths without becoming meaningless?
- Where's the line between single-step, full-turn, and multi-turn evaluation for a given agent?
