---
type: concept
status: active
created: 2026-07-24
updated: 2026-07-24
tags: [concept, ai-agent, agent-experience, trust, capability, cognitive-science, ai]
sources: [ai-as-senior-hire-not-intern]
confidence: 0.72
---

# Jagged Frontier

> [!abstract] Summary
> Model capability is **uneven in ways that are not predictable from the outside**. Tasks that look similarly difficult to a human fall on opposite sides of the boundary. The frontier is jagged rather than a smooth line, so performance on one task licenses no inference about performance on its apparent neighbor.

> [!important] Why it Matters
> This is the mechanism behind a specific, repeating trust failure: impressive results invite people to **anthropomorphize**, forming a general model of competence — and then an error inside the same apparent task class reads as **"betrayal"** rather than as an expected sample from an uneven distribution. The emotional whiplash is caused by the user's smooth mental model meeting a jagged reality.

## 📝 Key Claims

- **Capability is uneven and the unevenness is not legible** from the outside of the system.
- **Users build smooth models from jagged evidence.** A few good results generalize into trust that the next similar task will also succeed.
- **The betrayal reaction is a design problem, not a user error.** Interfaces that present uniform confidence across a non-uniform capability surface manufacture it.
- **Capability also moves discontinuously over time** — an abrupt step-change in coding performance around December 2025 was qualitative, not incremental.
- **Novelty trapping** compounds it: visually impressive output does not imply better decisions, so surface polish becomes a misleading proxy for reliability.

## 🧭 Design Implications

- Make **uncertainty legible per task**, not as a global confidence setting.
- Never let demonstrated success in one task class retire a safeguard in another — this is the direct argument for keeping [[wiki/concepts/ai-agents/approval-gate|approval gates]] positioned by reversibility rather than by observed reliability.
- Expect trust to be **non-monotonic**; design recovery paths for the moment after a surprising failure.
- Treat "it worked last time" as the weakest possible evidence in a plan.

## ⚖️ Conflicts & Caveats

> [!note] Term provenance
> The phrase predates this source (originating in 2023 work on AI and knowledge-worker performance). This page records it as used in [[wiki/sources/ai-as-senior-hire-not-intern|Ozenc & Holbrook]], where it is invoked as a practitioner observation rather than defined empirically. **Confidence 0.72** reflects a widely-corroborated phenomenon captured here from a single non-empirical source — worth a dedicated evidence pass against the original literature.

## 🔗 Related Concepts

- [[wiki/concepts/ai-agents/ai-as-senior-hire|AI as a Senior Hire]] — the framing this most complicates
- [[wiki/concepts/ai-agents/approval-gate|Approval Gate]]
- [[wiki/concepts/infrastructure-dev/agent-defense-in-depth|Agent Defense in Depth]]
- [[wiki/concepts/ux-research/human-in-the-loop|Human in the Loop]]

## 📚 Sources

- [[wiki/sources/ai-as-senior-hire-not-intern|Ozenc & Holbrook (2026): AI as a Senior Hire, Not an Intern]]

## ❓ Open Questions

- Can the frontier be mapped well enough per-domain to warn users before they cross it?
- Does the betrayal reaction diminish with expertise, or only change shape?
- What interface makes jaggedness legible without making the system feel untrustworthy overall?
