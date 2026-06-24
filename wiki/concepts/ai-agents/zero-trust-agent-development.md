---
type: concept
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [concept, zero-trust, vibe-coding, guardrails, human-in-the-loop, policy-server, production-grade]
sources: [spec-driven-production-development-day-5]
confidence: 0.78
---

# Zero-Trust Agent Development

> [!abstract] Summary
> A "safety net" for production-grade agentic development that **assumes AI output cannot be trusted by default**, layering guardrails, sandboxing, human-in-the-loop, AI-generated test coverage, evaluation, a policy server, and context hygiene / prompt sanitization.

> [!important] Why it Matters
> When AI writes most of the code and can hallucinate "vibe-consistent but functionally broken" logic, trust has to be **enforced by external controls**, not assumed. It's the production counterpart to the Day-4 security harness — applied from the start, not bolted on halfway.

## 📝 Key Claims
- Core components: **guardrails, sandboxing, human-in-the-loop, AI-generated test coverage, evaluation, a policy server, and context hygiene / prompt sanitization**.
- **AI-generated test coverage** turns freed-up implementation capacity into more tests than a human could write — a programmatic way to raise confidence (pair with mutation testing, since coverage ≠ effectiveness).
- Use these techniques **from the start** of a project, not midway.
- Complements [[concepts/ai-agents/spec-driven-development|SDD]]: the spec defines intent, the zero-trust net verifies the output is safe to ship.

## 🔗 Related Concepts
- [[concepts/ai-agents/agent-security-architecture|Agent Security Architecture]]
- [[concepts/ai-agents/harness-engineering|Harness Engineering]]
- [[concepts/ux-research/human-in-the-loop|Human-in-the-Loop]]
- [[concepts/infrastructure-dev/maintainability-sensor|Maintainability Sensor]]
- [[concepts/ai-agents/spec-driven-development|Spec-Driven Development]]

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> Each control adds friction/latency; the art is layering enough to be safe without killing the velocity that motivated vibe coding (the same velocity-vs-control tension as the Day-4 security harness). Day-5 captures the components at section level; mechanics (e.g. the policy server) need deeper ingest.

## 📚 Sources
- [[sources/spec-driven-production-development-day-5|Day 5 — Spec-Driven Production-Grade Development]]

## ❓ Open Questions
- What exactly does the policy server enforce, and how is context hygiene implemented?
- How much of the safety net can be automated vs requires human judgement?
