---
type: concept
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [concept, agent-cost-control, finops, llm-gateway, token-spend, budgets]
sources: [langchain-predictable-coding-agent-spend]
confidence: 0.8
---

# Agent Cost Control

> [!abstract] Summary
> Operational **FinOps for agents** — making token/$ spend **visible and bounded in real time** (budgets by dimension/window, caps + alerts + an increase-request workflow) rather than discovering cost only at month-end. The control point is typically an **LLM gateway**.

> [!important] Why it Matters
> Every agent action burns real tokens, and non-deterministic usage can blow a flat price many times over. Predictable spend is a precondition for shipping agents at scale — and ties directly to how the product is priced.

## 📝 Key Claims
- **LLM gateway** = a centralized proxy/control point for model calls that meters spend, enforces budgets, and ties cost to traces/observability/evals.
- Make spend **real-time and bounded**: budgets by dimension and time window, runaway-prevention, caps with alerting and an increase-request flow.
- Reconcile **un-routable clients** (calls that bypass the gateway) so the picture is complete.
- Pricing is a *system*: cost control must align with the product's pricing model (see [[concepts/product-management/ai-prd|AI PRD]] pricing) and with [[concepts/ai-agents/model-neutrality|model routing]] (cheapest-capable model per task).

## 🔗 Related Concepts
- [[concepts/infrastructure-dev/token-efficiency|Token Efficiency]]
- [[concepts/product-management/tokenomics|Tokenomics]]
- [[concepts/product-management/ai-prd|AI PRD]]
- [[concepts/ai-agents/model-neutrality|Model Neutrality]]
- [[concepts/infrastructure-dev/enterprise-ai-infrastructure|Enterprise AI Infrastructure]]
- [[concepts/infrastructure-dev/agentic-technical-debt|Agentic Technical Debt]]

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> A gateway only controls what routes through it — un-routable clients are a real gap. Hard caps can also break legitimate long runs; the alert + increase-request workflow is the proposed balance. Vendor lens (LangChain/LangSmith).

## 📚 Sources
- [[sources/langchain-predictable-coding-agent-spend|LangChain: How We Made Coding-Agent Spend Predictable]]

## ❓ Open Questions
- How to capture spend from clients that bypass the gateway?
- How to set caps that prevent runaway cost without killing legitimate long-horizon runs?
