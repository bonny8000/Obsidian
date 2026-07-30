---
type: concept
status: active
created: 2026-07-30
updated: 2026-07-30
tags: [concept, agent-experience, delegation, trust, autonomy, commercial-influence, approval-gate]
sources: [kakao-vc-ai-agent-advertising]
confidence: 0.74
---

# Delegation Spectrum

> [!abstract] Summary
> A four-tier scale of **how much judgment a user cedes to an agent** — from filtered search, through comparative recommendations, through direct recommendations, to autonomous execution. The tier determines which trust affordances are even *available*, and commercial-influence risk escalates in lockstep with the delegation.

> [!important] Why it Matters
> Trust interventions are not interchangeable across tiers, and most design advice silently assumes tier 1 or 2. **Disclosure works by inviting comparison** — so at tier 3, where the agent has already made the comparison and shows one answer, a "Sponsored" label has nothing to point at. The empirical version: conversational sponsored recommendations were selected at **61.2%** versus **22.4%** in search, and explicit labels plus warnings only moved that to **55.5%**.

## The four tiers

| Tier | What the user cedes | Available trust affordance | Named examples |
|---|---|---|---|
| **1. Filtered search** | Almost nothing — parameters only | Comparison is native; the result set is the evidence | Google Flights, Skyscanner |
| **2. Comparative recommendations** | Shortlisting | Comparison across the offered set; disclosure has something to attach to | Amazon Rufus |
| **3. Direct recommendations** | The comparison itself | **Weakest position.** Nothing on screen to compare; user rarely checks alternatives | — |
| **4. Autonomous execution** | The decision *and* the act | Only pre-approval and post-hoc audit | Amazon Buy for Me |

## 📝 Key Claims

- **Risk and commercial opportunity escalate together.** The same property that makes higher tiers valuable — the user does less work — is what makes influence profitable and undetectable.
- **Tier 3 is the dangerous middle.** Tier 4 at least announces that something consequential is happening and invites a gate. Tier 3 looks like advice and functions like a decision.
- **Detection collapses when intent is hidden** — users noticed **less than 10%** of the time in the cited study.
- **Design the recoverability of comparison, not just the recommendation.** At tiers 3–4 the useful question is whether a user can cheaply see what was *not* chosen, and why.
- **Tier placement should be a deliberate product decision**, not a drift. Products tend to migrate upward because higher tiers feel more capable; the trust cost is paid silently.

## How to use it

1. **Locate the product on the spectrum**, per surface rather than per product — search, recommendations, and checkout may sit on different tiers.
2. **Check whether the trust affordance you planned exists at that tier.** If the plan is "label it clearly" and you are at tier 3, the plan does not work.
3. **At tiers 3–4, move upstream** — audit the incentive structure, because interface honesty cannot repair a divergent payoff.
4. **Gate tier 4 on explicit approval**, which is where this concept meets [[wiki/concepts/ai-agents/approval-gate|Approval Gate]] from the commercial side rather than the reliability side.

## ⚖️ Conflicts & Caveats

> [!warning] The numbers are second-hand
> The 61.2% / 22.4% / 55.5% / <10% figures come from a Princeton study **cited but not characterized** by the anchor source — no sample size, task design, product category, or venue. Use the direction freely; verify before quoting decimals. Locating that paper is the highest-value next ingest for this concept.

> [!warning] Single source, and an interested one
> The framework comes from one VC blog post. It is well constructed and internally coherent, and the firm has an investment interest in "trust as a moat." Nothing here is corroborated by a second independent source yet.

> [!warning] The tiers are cleaner than reality
> Real products blend tiers within one interaction — a conversational answer that names one option, mentions two others in passing, and offers a buy button spans 2 through 4 in a single response. Tier assignment is a lens, not a taxonomy.

> [!warning] Says nothing about who chose the tier
> The spectrum measures what the user cedes and is silent on whether they knew they were ceding it. A user who believes they are at tier 2 while the system operates at tier 3 is the actual failure case, and no source here addresses that gap.

## 🔗 Related Concepts

- [[wiki/concepts/agent-experience/principal-agent-problem|Principal–Agent Problem (AI)]] — why higher tiers are exploitable.
- [[wiki/concepts/product-management/ai-advertising|AI Advertising]] — the monetization layer this spectrum maps.
- [[wiki/concepts/agent-experience/trust-calibration|Trust Calibration]] — the affordances whose availability the tier determines.
- [[wiki/concepts/agent-experience/checkbox-transparency|Checkbox Transparency]] — what a label becomes at tier 3.
- [[wiki/concepts/ai-agents/approval-gate|Approval Gate]] — the tier-4 control, reached here from commercial rather than reliability pressure.
- [[wiki/concepts/agent-experience/initiative-and-interruption|Initiative and Interruption]]
- [[wiki/concepts/agent-experience/proactivity-design|Proactivity Design]]
- [[wiki/concepts/ai-agents/autonomous-ai-agent|Autonomous AI Agent]]
- [[wiki/concepts/agent-experience/agent-transparency|Agent Transparency]]

## 📚 Sources

- [[wiki/sources/kakao-vc-ai-agent-advertising|Kakao Ventures (2026): AI Agents — Questioning the Qualifications of a True Representative]] — sole source: the four tiers, the escalation claim, and the cited disclosure figures.

## ❓ Open Questions

- What are the cited study's real parameters?
- Does the disclosure penalty shrink with repeated exposure (habituation) or grow (learned skepticism)?
- Is there *any* disclosure format that changes behavior at tier 3?
- How do users form beliefs about which tier they are on, and how often are they wrong?
- Should tier be surfaced to users as an explicit product setting?
