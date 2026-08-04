---
type: concept
status: active
created: 2026-07-30
updated: 2026-08-04
tags: [concept, agent-experience, delegation, trust, autonomy, commercial-influence, approval-gate]
sources: [kakao-vc-ai-agent-advertising, google-search-io-2026-agents]
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
- **What does the spectrum owe a third party the agent contacts,** who is not on it at all?

## A Consumer Product Now Occupies the Far End

> [!important] Added 2026-08-04
> [[wiki/sources/google-search-io-2026-agents|Google's agentic booking]] (announced I/O 2026, US, summer 2026) extends to **placing phone calls to businesses on the user's behalf** — home repair, beauty, pet care.
>
> That sits at the top tier by every criterion this page uses: the user cannot observe the action while it happens, cannot verify it in flight, and the cost of an error lands outside the interface. The spectrum predicts verification collapses here, and this is the first mass-market consumer product in the vault to occupy that position.
>
> **The gap the spectrum does not model.** Every tier on this page describes a relationship between a user and an agent. An agent phoning a business creates a **third party who never delegated anything** — no interface, no disclosure, no consent, and no seat on the spectrum. Google's announcement does not say whether the callee is told they are speaking to an AI.
>
> Related: [[wiki/sources/kakao-vc-ai-agent-advertising|Kakao Ventures]] found hidden intent in conversational recommendation went undetected **over 90%** of the time. The pattern generalises — as agents mediate more, the parties bearing the consequences are increasingly the ones furthest from the interface. See [[wiki/analyses/2026-08-04-crawl-consent-vs-answer-surfaces|the 2026-08-04 memo]], which reaches the same conclusion from the publisher side.
>
> Caveat: this is a first-party product announcement with no evaluation data and a stated summer-2026 date. Announced ≠ shipped; not verified here.

## Additional Sources

- [[wiki/sources/google-search-io-2026-agents|Google (2026): Search at I/O 2026]] — agentic booking and outbound calling.
