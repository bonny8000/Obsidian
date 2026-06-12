---
type: concept
status: active
created: 2026-06-01
updated: 2026-06-01
tags: [ai, engineering, technical-debt]
sources: [founders-playbook-2026]
confidence: 0.90
---

# Agentic Technical Debt

## Summary
Agentic Technical Debt refers to the hidden costs, complexities, and maintenance burdens that arise from using AI agents to generate code or manage engineering workflows. 

## Sources of Debt
- **Unverified Code:** Large volumes of agent-generated code that lack thorough human review.
- **Context Fragmentation:** Code that works in isolation but fails to account for system-wide architectural patterns.
- **Agent-Specific Hacks:** Workarounds created by agents to bypass immediate errors that become permanent bottlenecks.
- **Prompt Rot:** Dependencies on specific model versions or prompt structures that break when models are updated.

## Why it matters
Because agents can generate code much faster than humans can review it, technical debt can accumulate at an exponential rate. Managing this debt requires automated linting, rigorous evals, and a shift in the engineer's role from "coder" to "architect and reviewer."

## Related Concepts
- [[concepts/infrastructure-dev/agentic-engineering|Agentic Engineering]]
- [[concepts/ux-research/usability-debt|Usability Debt]]
- [[concepts/product-management/shipping-velocity|Shipping Velocity]]
