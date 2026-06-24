---
type: concept
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [concept, agent-verifiers, llm-as-judge, evaluation, verification, legal-agents]
sources: [langchain-verifiers-legal-agents]
confidence: 0.8
---

# Agent Verifiers

> [!abstract] Summary
> Automated checks that **score an agent's output pass/fail against rubric criteria** — most often via **LLM-as-a-Judge** — used both as evaluation and as gates / RL-reward signals. Designing the verifier (cost vs accuracy vs risk) is itself an engineering problem.

> [!important] Why it Matters
> Agents need a cheap, repeatable way to judge "is this output acceptable" at scale. Verifiers are the mechanism behind [[concepts/product-management/ai-prd|Eval Plans]], [[concepts/ai-agents/loop-engineering|verification loops]], and RL training — but a bad verifier (especially a **false pass** in a high-stakes domain like legal) is worse than none.

## 📝 Key Claims
- **LLM-as-a-Judge** is the dominant mechanism: an LLM grades another model's/agent's output against a rubric. Watch agreement metrics, **inter-model disagreement ceilings**, and **permissiveness / false-pass** failure modes.
- **Verifier design** is a real engineering choice: per-criterion vs batch scoring, judge-model choice, prompt tuning, sometimes bespoke fine-tuning — traded against cost, accuracy, and risk.
- **False-pass asymmetry:** in legal/high-stakes work, wrongly passing a bad output is far costlier than wrongly failing a good one — design for that asymmetry.
- Verifiers serve double duty: offline evals *and* online gating / reward signals.

## 🔗 Related Concepts
- [[concepts/ai-agents/product-evals|Product Evals]]
- [[concepts/ux-research/ai-evals|AI Evals]]
- [[concepts/product-management/ai-prd|AI PRD]]
- [[concepts/ai-agents/vibe-coding-agent-evaluation|Vibe-Coding Agent Evaluation]]
- [[concepts/ai-agents/loop-engineering|Loop Engineering]]
- [[concepts/ux-research/human-in-the-loop|Human-in-the-Loop]]

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> An LLM judge has its own bias/hallucination and can't be fully trusted — it needs calibration against human eval (the Eval-pyramid point in [[concepts/product-management/ai-prd|AI PRD]]). Vendor lens (LangChain/LangSmith).

## 📚 Sources
- [[sources/langchain-verifiers-legal-agents|LangChain: Designing Efficient Verifiers for Legal Agents]]

## ❓ Open Questions
- How to calibrate an LLM judge so its pass/fail is trustworthy in high-stakes domains?
- When is a bespoke fine-tuned verifier worth it vs a prompted judge?
