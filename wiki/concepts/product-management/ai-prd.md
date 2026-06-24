---
type: concept
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [concept, ai-prd, product-management, eval-plan, regression-testing, non-determinism, pricing]
sources: [yozm-ai-prd]
confidence: 0.8
---

# AI PRD

> [!abstract] Summary
> A product requirements doc for an AI feature must specify more than deterministic behavior: it must define the **range of acceptable answers** and **how acceptability is judged** — its new heart is an **Eval Plan** — because AI features are non-deterministic (same prompt → different answers).

> [!important] Why it Matters
> Classic PRDs assume same input → same output, so writing *what should happen* sufficed ("a pinch of salt" works for someone who already cooks). AI features differ every run, so a PRD must read like a Michelin recipe ("2.3g sea salt") — precise enough that the result is reproducible and objectively judgable. Whether the Eval Plan is written into the PRD decides the feature's fate months later.

## 📝 Key Claims
- **Eval Plan = the evaluation standard + tooling, written into the PRD.** Fundamentally a growing **test-case set** (input / expected / actual / score / pass-fail); start 20–30 cases, accrue to ~200 — the team's biggest asset.
- **Eval pyramid:** rule-based (fast/cheap/shallow) → **LLM-as-a-Judge** (fast/cheap, but its own bias/hallucination) → **human eval** (accurate, slow/expensive; required for regression baselines). The PM pre-assigns each case a layer to control cost.
- **Regression testing** ends the **"prompt swamp"** (fixing one case breaks another): rerun the whole Eval set on every prompt change and confirm no score dropped.
- **8 required AI-PRD items:** feature overview (AI must be *best* at the problem, not "AI for AI's sake"); input/output spec; system-prompt draft; quality standard; **failure definition**; Eval Plan; monitoring plan; risks & limitations.
- **Pricing belongs in the PRD** (token cost couples usage to margin): usage-based / outcome-based / hybrid — and the choice feeds success metrics (outcome pricing ⇒ define "resolved" in the Eval Plan).
- **PRD as promise:** an AI PRD promises *how it behaves, how we judge it works, how we detect breakage, how we cap cost.*

## 🔗 Related Concepts
- [[concepts/ai-agents/prd-generation|PRD Generation]]
- [[concepts/ai-agents/product-evals|Product Evals]]
- [[concepts/ux-research/ai-evals|AI Evals]]
- [[concepts/ai-agents/spec-driven-development|Spec-Driven Development]]
- [[concepts/ai-agents/vibe-coding-agent-evaluation|Vibe-Coding Agent Evaluation]]
- [[concepts/product-management/tokenomics|Tokenomics]]

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> LLM-as-a-Judge is the affordable middle of the pyramid yet can't be fully trusted (judge bias/hallucination) — it needs calibration against human eval. Source captured via a Chinese summary (not verbatim); exact figures are illustrative, and the monitoring-metrics detail is deferred to a follow-up article.

## 📚 Sources
- [[sources/yozm-ai-prd|Yozm IT (2026): What an AI PRD Must Do Differently]]

## ❓ Open Questions
- How to calibrate LLM-as-a-Judge so its scores are trustworthy?
- How to define "resolved" rigorously enough to bill on it (outcome-based pricing × Eval Plan)?
- What monitoring metrics/alerts complete the loop (deferred by the source)?
