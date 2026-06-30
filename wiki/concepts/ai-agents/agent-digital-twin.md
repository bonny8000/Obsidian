---
type: concept
status: active
created: 2026-06-26
updated: 2026-06-26
tags: [agent-digital-twin, per-person-agent, agent-identity, agentic-work-automation, macrohard]
sources:
  - sources/yozm-tiro-ax-ontology
confidence: 0.7
---

# Agent Digital Twin

## Summary

An **agent digital twin** is a per-person AI agent scoped to mirror one team member's thinking, voice, and judgment — pulling role-specific context from an organizational wiki and gated by a central rule repository before it acts. The Plato pairs one agent per person (e.g. "Mio" for the teammate "Leo"), and these agents' aggregate is meant to let the company keep operating with minimal daily human intervention (their "Macrohard" goal).

## Why It Matters

It reframes "AI headcount" from a pool of generic assistants to a roster of role-bound twins, each accountable for a person's domain (sales, security, triage). Because a twin converges toward a specific human's judgment over time (via feedback in Slack), its outputs are more trustable-in-context than a generic agent's — and the org can scale output (10 people → 300k-user service) without proportional hiring.

## Key Claims

- **One agent per person.** Each team member is paired with a twin scoped to their role and judgment, not a shared general assistant.
- **Voice/judgment convergence.** The twin improves by feedback loops, converging toward the human's actual decisions over time.
- **Context + gating.** Twins pull real-time context from the meeting-derived org wiki and must validate actions against a central rule repository before executing.
- **Named roster (Tiro):** Mio (internal ops / mirrors a teammate), Barin (B2B sales — monitors 200+ accounts, diagnoses churn, drafts responses), Gyeoul (security reports), a bug-triage agent (log diagnosis → fix proposal → summon engineer).
- **"Macrohard" ambition.** A company that largely self-operates via a fleet of twins — with humans retaining security approvals and taste/strategy.

## Related Concepts

- [[concepts/ai-agents/agent-identity|Agent Identity]] — what an individual agent "is"; a twin is identity bound to a person.
- [[concepts/ai-agents/agentic-work-automation|Agentic Work Automation]] — twins are the unit of automated work here.
- [[concepts/infrastructure-dev/organizational-ontology|Organizational Ontology]] — the shared context twins consume to act in-org.
- [[concepts/ai-agents/ai-maintained-wiki|AI-Maintained Wiki]] — the knowledge source twins read.
- [[concepts/ai-agents/harness-engineering|Harness Engineering]] — the rule-gating + context-injection scaffold around each twin.
- [[concepts/ai-agents/autonomous-ai-agent|Autonomous AI Agent]] — twins are bounded-autonomy agents with human gates.
- [[concepts/product-management/10-person-unicorn|10-Person Unicorn]] — the small-team-massive-leverage thesis twins enable.

## Conflicts & Caveats

> [!warning] Vendor case, anthropomorphic framing
> Single branded-content source; "digital twin of a person" is an evocative claim, not a measured fidelity. Convergence to a human's judgment is asserted, not quantified, and risks encoding one person's blind spots at scale. Humans still gate irreversible actions (security, infra).

## Sources

- [[sources/yozm-tiro-ax-ontology|Yozm × The Plato (2026): Ontology Essential for AX (feat. Tiro)]]

## Open Questions

- How is a twin's fidelity to its person measured, and what happens when the person and twin disagree?
- Does per-person scoping fragment shared knowledge, or does the org wiki keep twins coherent?
- What governance covers a twin acting on behalf of someone who is unavailable or has left?
