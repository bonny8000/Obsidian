---
type: concept
status: active
created: 2026-07-30
updated: 2026-07-30
tags: [concept, agent-experience, principal-agent, incentives, trust, monetization, governance, regulation]
sources: [kakao-vc-ai-agent-advertising, hbs-working-knowledge-ai-advice-willful-blindness]
confidence: 0.75
---

# Principal–Agent Problem (AI)

> [!abstract] Summary
> The classic economics problem, restated for AI: when an agent acts **on your behalf** but its payoff comes from **someone else**, its judgments drift toward the payer. In AI products the drift is unusually hard to detect, because the output looks like advice rather than like a placement — and the user has no comparison set to check it against.

> [!important] Why it Matters
> This is the failure mode that transparency does not fix, and this vault now has a number for that: sponsored recommendations delivered conversationally were selected at **61.2%** against **22.4%** in search, and adding explicit "Sponsored" labels *plus warnings* only reduced it to **55.5%**. When the commercial intent was hidden, users detected it **less than 10%** of the time. Interface honesty is downstream of incentive structure; where the payoff diverges, no amount of disclosure repairs it.

## 📝 Key Claims

- **The word "agent" carries an obligation the products often do not honour.** A true representative acts in the principal's interest; an ad-funded recommender has a second principal.
- **Advertising changes in kind, not degree.** Search-era ads occupied *space* in a page the user could compare against. Agent-era influence enters the **judgment-formation process itself**, where there is nothing to compare.
- **Disclosure is structurally weak here**, not merely poorly implemented — it works by inviting comparison, and a single recommendation offers none. See [[wiki/concepts/agent-experience/delegation-spectrum|Delegation Spectrum]] for why the tier determines this.
- **Restructure the incentive rather than announcing it.** The insurance analogy from the anchor source: spread commissions over time so the agent's payoff tracks the client's long-term outcome instead of the moment of sale.
- **Independent corroboration that transparency underperforms:** [[wiki/sources/hbs-working-knowledge-ai-advice-willful-blindness|Chan (2026)]] found users skip available explanations when incentives point the other way — [[wiki/concepts/agent-experience/willful-blindness|willful blindness]]. Two unrelated results, same conclusion: explanation mechanisms are weaker than designers assume.
- **Trust becomes a defensible asset.** If capability commoditizes, demonstrable non-divergence is a moat rather than a compliance cost.

## Detecting divergence in your own product

The useful audit is not "is the interface honest?" but "where does the money come from?":

1. **Whose payoff moves when the agent recommends X over Y?** If any answer is not the user's, that is a divergence surface.
2. **Could a user detect the divergence from the output alone?** At [[wiki/concepts/agent-experience/delegation-spectrum|tier 3+]] the answer is almost always no.
3. **Is the compensation contemporaneous with the recommendation, or linked to the outcome?** Contemporaneous payment maximizes divergence.
4. **Is there an auditable claim you could make** — and could an outsider verify it?

## Anticipated regulatory trajectory

The anchor source's three phases, useful as a planning frame rather than a forecast:

| Phase | What gets regulated |
|---|---|
| **Disclosure** | Labelling sponsored content |
| **Structure** | Recommendation mechanisms; performance-based payment contracts |
| **Authority** | What an agent may execute autonomously without explicit approval |

Note that phase 3 converges on the same control this vault reached for reliability reasons — see [[wiki/concepts/ai-agents/approval-gate|Approval Gate]]. Commercial capture and technical unreliability arrive at the same gate.

## Market positioning as a live signal

Two frontier labs took opposite public positions in the same year: **Anthropic** rejected advertising outright ("Ads are coming to AI. But not to Claude."), while **OpenAI** launched ad trials on free and budget tiers across multiple countries. Whatever else it is, this is a natural experiment worth tracking rather than a settled question.

## ⚖️ Conflicts & Caveats

> [!warning] The key numbers are second-hand
> The Princeton figures are **cited but not characterized** by the anchor source — no sample, task design, category, incentive structure, or venue. They are the most quotable content in this concept and the least verified. Locating the primary paper is the highest-value next ingest here.

> [!warning] Single primary source, with an investment interest
> The framework comes from a VC blog. "Trust is a moat" is congenial to a firm funding challengers to ad-funded incumbents. The reasoning is sound and the incentive is real.

> [!warning] The insurance analogy is untested
> Deferred-commission structures evolved over decades in a market with slow decision cycles, high contract values, and licensed intermediaries. AI recommendations are high-frequency, low-value, and unlicensed. Transfer is plausible and undemonstrated.

> [!warning] It cuts against this vault's own transparency material
> Much of [[wiki/concepts/agent-experience/agent-transparency|Agent Transparency]] and [[wiki/concepts/agent-experience/trust-calibration|Trust Calibration]] assumes that surfacing provenance and uncertainty produces appropriate reliance. That assumption holds against *noise*. It is much weaker against an **optimizing counterparty**, and no source in this vault yet designs for the adversarial case.

## 🔗 Related Concepts

- [[wiki/concepts/agent-experience/delegation-spectrum|Delegation Spectrum]] — how much judgment is ceded, and therefore how exploitable the position is.
- [[wiki/concepts/product-management/ai-advertising|AI Advertising]] — the concrete monetization mechanism.
- [[wiki/concepts/agent-experience/trust-calibration|Trust Calibration]] — calibration against an interested party, not just against noise.
- [[wiki/concepts/agent-experience/willful-blindness|Willful Blindness]] — the independent corroboration that explanations get skipped.
- [[wiki/concepts/agent-experience/checkbox-transparency|Checkbox Transparency]] — disclosure as ritual.
- [[wiki/concepts/agent-experience/ai-sycophancy|AI Sycophancy]] — divergence driven by engagement rather than payment.
- [[wiki/concepts/ai-agents/approval-gate|Approval Gate]] — the phase-3 control.
- [[wiki/concepts/ai-agents/agent-identity|Agent Identity]] — whose agent is it, formally.
- [[wiki/concepts/agent-experience/satisfaction-vs-benefit|Satisfaction vs. Benefit]] — the same wedge measured on the user side.

## 📚 Sources

- [[wiki/sources/kakao-vc-ai-agent-advertising|Kakao Ventures (2026): AI Agents — Questioning the Qualifications of a True Representative]] — the framing, the disclosure evidence, the incentive-restructuring proposal, the regulatory phases.
- [[wiki/sources/hbs-working-knowledge-ai-advice-willful-blindness|Chan (2026): When AI Gives Advice, Employees Rarely Ask Why]] — independent evidence that explanation mechanisms underperform when incentives diverge.

## ❓ Open Questions

- What are the cited study's actual parameters, and does the effect replicate?
- Is there any disclosure format that works when the user has nothing to compare against?
- Does outcome-linked compensation work at high frequency and low value?
- What would a *verifiable* "no commercial influence" claim require technically?
- Does the Anthropic/OpenAI divergence persist, and does either position show a measurable trust or retention effect?
- How should a design system or research practice test for divergence — is there a red-team method for this?
