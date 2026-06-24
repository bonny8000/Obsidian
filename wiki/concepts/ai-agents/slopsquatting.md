---
type: concept
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [concept, supply-chain-security, hallucination, package-security, vibe-coding, agent-security]
sources: [vibe-coding-agent-security-evaluation-day-4]
confidence: 0.8
---

# Slopsquatting

> [!abstract] Summary
> A supply-chain attack unique to AI code generation: LLMs frequently **hallucinate package names that don't exist**, and attackers **pre-publish malware under those exact fabricated names** so that autonomous agents inadvertently download them.

> [!important] Why it Matters
> Autonomous agents can alter dependency graphs **without human confirmation**, so a single hallucinated import can pull malware straight into the build environment. It's a new, high-severity failure mode created precisely by agentic, intent-driven coding.

## 📝 Key Claims
- Term attributed to **Wiz's** research on vibe coding; attackers monitor AI outputs/forums for commonly hallucinated names and squat them.
- Mitigations: source dependencies only from **vetted / internal enterprise registries**, enforce **cryptographic version pinning**, and gate CI/CD with **SBOM verification + digital signatures (Binary Authorisation)** before anything reaches production.
- A concrete instance of the broader rule that **vibe-coded output cannot be implicitly trusted** just because it compiles/runs.

## 🔗 Related Concepts
- [[concepts/ai-agents/agent-security-architecture|Agent Security Architecture]]
- [[concepts/infrastructure-dev/agentic-technical-debt|Agentic Technical Debt]]
- [[concepts/ai-agents/harness-engineering|Harness Engineering]]

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> Depends on current model tendencies to hallucinate package names; better models or built-in registry checks may shrink the surface, but the "don't trust unverified dependencies" principle stays.

## 📚 Sources
- [[sources/vibe-coding-agent-security-evaluation-day-4|Day 4 — Vibe Coding Agent Security and Evaluation]]

## ❓ Open Questions
- How often do current coding agents propose non-existent packages, and which ecosystems are worst hit?
- Can registry-side defences (reserving hallucinated names) outpace attackers?
