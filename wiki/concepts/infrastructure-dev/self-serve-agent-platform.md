---
type: concept
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [concept, self-serve-agent-platform, enterprise-agents, guardrails, prompt-as-spec, governance]
sources: [langchain-lyft-support-agent-platform]
confidence: 0.78
---

# Self-Serve Agent Platform

> [!abstract] Summary
> A platform that lets **non-engineers (domain experts) build, evaluate, and operate production AI agents** via prompts/configuration, while engineering owns the **guardrails** (safety gates, LLM-judge evals, prompt linting, observability). Lyft built one for customer support on LangGraph + LangSmith.

> [!important] Why it Matters
> It scales agent-building beyond the engineering team by **decoupling builders from operators** — the same lever as Myrealtrip's ops tool and Newton's "Research Systems Builder" role. Domain experts move fast; engineering keeps it safe.

## 📝 Key Claims
- Domain experts author agents through **prompts/config**, not code; engineering (MLE) owns reusable **guardrails**.
- Guardrails layer: safety gates, **[[concepts/ai-agents/agent-verifiers|LLM-as-judge evals]]** (binary pass/fail, shared + agent-specific metrics, multi-turn eval on sampled production traces), **prompt linting** (CI validation of a structured prompt template), routing, and observability.
- **Prompt-as-spec:** an agent's prompt is treated as a reviewed, linted product specification rather than informal instructions.
- Architecture uses a router + node patterns on LangGraph, with LangSmith for eval/observability.

## 🔗 Related Concepts
- [[concepts/infrastructure-dev/enterprise-ai-agent-platform|Enterprise AI Agent Platform]]
- [[concepts/ai-agents/managed-ai-agents|Managed AI Agents]]
- [[concepts/product-management/role-convergence|Role Convergence]]
- [[concepts/product-management/feature-vs-platform|Feature vs Platform]]
- [[concepts/ai-agents/agent-verifiers|Agent Verifiers]]
- [[concepts/ux-research/human-in-the-loop|Human-in-the-Loop]]

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> Self-serve authoring risks quality/consistency drift — the guardrail layer (evals, linting, safety gates) is what keeps it safe, and it's only as good as those checks. Vendor/customer-story lens (LangChain + Lyft), no independent metrics.

## 📚 Sources
- [[sources/langchain-lyft-support-agent-platform|Lyft × LangChain: A Self-Serve AI Agent Platform for Support]]

## ❓ Open Questions
- Where's the line between safe self-serve authoring and necessary engineering review?
- How do prompt-linting + LLM-judge evals scale as the number of self-served agents grows?
