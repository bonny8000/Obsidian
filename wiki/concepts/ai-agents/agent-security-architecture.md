---
type: concept
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [concept, agent-security, zero-trust, harness, effective-trust, context-as-perimeter, vibe-coding]
sources: [vibe-coding-agent-security-evaluation-day-4]
confidence: 0.8
---

# Agent Security Architecture

> [!abstract] Summary
> A layered, defence-in-depth model for securing autonomous agents, built on a **7-pillar baseline** and a shift from **Identity-as-a-Perimeter (RBAC)** to **Context-as-a-Perimeter**, where trust is continuously earned ("Effective Trust") rather than granted once at deployment.

> [!important] Why it Matters
> A raw model becomes an agent only when wrapped in a harness — so security must move from "securing code syntax" to "securing the harness." Static identity is a poor perimeter for non-deterministic agents that can execute generated code, hit internal APIs, and modify production. Assume the model can fail or be compromised, and enforce an external "safety envelope."

## 📝 Key Claims
- **7 pillars:** Infrastructure & Networking (ephemeral kernel sandboxes, egress governance), Data (CMEK/mTLS/least-privilege, vector-DB tenant partitioning), Model (system prompts/rule files as attested "source code"), Application & Runtime (LLM firewalls, lifecycle hooks, Centralised Agent Gateway for A2A), IAM (cryptographic agent identities e.g. SPIFFE, ABAC + JIT downscoping, Intent × User × Time), Observability & SecOps, Governance (EU AI Act, immutable audit, Logic Reviews).
- **Effective Trust** = a continuous metric across supply chain, identity, runtime behaviour, and contextual associations.
- **Zero Ambient Authority + JIT downscoping:** agents get fresh, hyper-restricted, self-expiring credentials, not the human's broad delegated access.
- **Distinct agentic identity** (not delegated user creds) defeats the **Confused Deputy** problem.
- Replace "approve/deny" buttons with **Logic Reviews** (syntax translated to plain language) + Risk-Stratified Attestation.

## 🔗 Related Concepts
- [[concepts/ai-agents/harness-engineering|Harness Engineering]]
- [[concepts/ai-agents/model-harness|Model Harness]]
- [[concepts/ai-agents/red-blue-green-agent-teaming|Red/Blue/Green Agent Teaming]]
- [[concepts/ai-agents/zero-trust-agent-development|Zero-Trust Agent Development]]
- [[concepts/ai-agents/slopsquatting|Slopsquatting]]
- [[concepts/ai-agents/mcp-integration|MCP Integration]]
- [[concepts/infrastructure-dev/cloud-ai-governance|Cloud AI Governance]]

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> This is a prescriptive Google reference architecture (Day 4), not an outcome study; full 7-pillar adoption may be realistic mainly in hyperscaler-grade environments. Security alone is insufficient — an agent can stay in-bounds yet still produce un-shippable work (see [[concepts/ai-agents/vibe-coding-agent-evaluation|Vibe-Coding Agent Evaluation]]).

## 📚 Sources
- [[sources/vibe-coding-agent-security-evaluation-day-4|Day 4 — Vibe Coding Agent Security and Evaluation]]

## ❓ Open Questions
- Which pillars give the most risk reduction per unit effort for a non-hyperscaler team?
- How are Intent Drift and Trust Decay measured in practice?
