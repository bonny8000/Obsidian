---
type: concept
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [concept, eu-ai-act, compliance, governance, observability, audit, regulation]
sources: [langchain-eu-ai-act]
confidence: 0.78
---

# EU AI Act Compliance

> [!abstract] Summary
> Meeting the **EU AI Act's high-risk obligations** — risk management, data governance, event logging, transparency to deployers, human oversight, accuracy/robustness, post-market monitoring — for AI systems including agents, and the **observability → evals → human-in-the-loop → data-residency** backbone that *evidences* them.

> [!important] Why it Matters
> The Act is a stable, named regulatory regime that recurs across sources. Agentic autonomy raises the bar: you must be able to audit *which agent did what, when, and under whose authority*. Compliance is operationalized through tooling, not just policy.

## 📝 Key Claims
- Maps Act articles to capabilities: Art. 9 (risk management), 10 (data governance), 12 (event logging), 13 (transparency to deployers), 14 (human oversight), 15 (accuracy/robustness/cybersecurity), 72 (post-market monitoring).
- Tooling realization: **observability = the audit trail / event log**; **online evals = post-market monitoring**; **human-in-the-loop = Art. 14 oversight**; data residency for Art. 10.
- Complements [[concepts/ai-agents/agent-security-architecture|Day-4's Governance pillar]] (obligation-as-principle) with a concrete evidence layer (LangSmith / LangChain OSS in the source).

## 🔗 Related Concepts
- [[concepts/infrastructure-dev/cloud-ai-governance|Cloud AI Governance]]
- [[concepts/ai-agents/agent-security-architecture|Agent Security Architecture]]
- [[concepts/infrastructure-dev/enterprise-ai-infrastructure|Enterprise AI Infrastructure]]
- [[concepts/ux-research/human-in-the-loop|Human-in-the-Loop]]
- [[concepts/agent-experience/agent-transparency|Agent Transparency]]
- [[concepts/ai-agents/product-evals|Product Evals]]

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> Vendor lens: the source frames LangSmith/LangChain OSS as the compliance backbone — useful as a capability map, not legal advice. The Act's details and timelines evolve; verify specific article obligations against primary regulatory text.

## 📚 Sources
- [[sources/langchain-eu-ai-act|LangChain: LangSmith / LangChain OSS & the EU AI Act]]
- [[sources/vibe-coding-agent-security-evaluation-day-4|Day 4 — Security & Evaluation]] (Governance pillar)

## ❓ Open Questions
- Which obligations are hardest to evidence for *autonomous* agents specifically?
- How does the audit-trail requirement interact with data-minimization/residency?
