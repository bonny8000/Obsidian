---
type: concept
status: active
created: 2026-06-12
updated: 2026-07-30
tags: [agent-experience, trust, ax, human-ai-interaction, principal-agent, measurement]
sources:
  - sources/andru-saksena-adobe-haic-2025
  - sources/theaxlabs-contaminated-memory-performance
  - sources/lee-see-2004-trust-in-automation
  - sources/hbs-working-knowledge-ai-advice-willful-blindness
  - sources/kakao-vc-ai-agent-advertising
  - sources/measuringu-measuring-the-ux-of-ai
confidence: 0.82
---

# Trust Calibration

## Summary

Trust calibration is the goal of matching user trust to actual agent capability: enough trust to delegate where the agent is reliable, enough skepticism to verify where it is not.

## Why It Matters

Both failure modes are expensive. Over-trust leads to unreviewed errors shipping into real work; under-trust means users redo everything the agent did and the product delivers no leverage. The design target is appropriate reliance, not maximum trust.

## Key Claims

- Trust is dimension-specific, not global: a user can correctly trust an agent for retrieval but not for judgment calls.
- Calibration is driven more by experienced outcomes than by stated disclaimers; the first few failures shape long-term reliance.
- Uncertainty display (confidence signals, hedged language, "I could not verify X") is the main interface lever for preventing over-trust.
- Easy verification paths (citations, diffs, previews before commit) let users build trust incrementally instead of taking a delegation leap.
- Contaminated or stale memory silently miscalibrates trust because the user cannot see why the agent's behavior degraded — see [[concepts/ai-agents/memory-contamination|Memory Contamination]].
- Lee & See define three target properties: calibration (level matches capability), resolution (trust differentiates contexts), and specificity (trust attaches to the right function) — plus a misuse/disuse failure taxonomy — see [[sources/lee-see-2004-trust-in-automation|Lee & See 2004]].
- **Incentives and bias skew calibration:** Financial, outcome-based incentives and moral discomfort can cause users to ignore explanations (willful blindness), leading to uncalibrated over-reliance — see [[concepts/agent-experience/willful-blindness|Willful Blindness]].
- **Embrace Uncertainty:** Microsoft Design positions uncertainty as an expected feature of agent systems; exposing reasoning and certainty levels is foundational to establishing appropriate trust — see [[concepts/agent-experience/microsoft-agent-ux-principles|Microsoft Agent UX Principles]].
- **Calibration is now measurable, provisionally.** [[wiki/sources/measuringu-measuring-the-ux-of-ai|Sauro & Lewis (2026)]] propose *AI Trust* (7 items) and *AI Dependency* (3 items) as standardized constructs — the first candidate instrument for what this concept has described qualitatively. **Unvalidated**; see [[wiki/concepts/ux-research/ai-ux-measurement-constructs|AI UX Measurement Constructs]].
- **The population is already badly calibrated.** Cited in that source: **66%** rely on AI output without verifying accuracy, and **56%** made mistakes from uncritical acceptance. Over-trust is the dominant failure mode in practice, not under-trust.

## ⚖️ Calibration against an interested party

> [!warning] The levers below assume miscalibration is an accident
> Every lever in this concept treats miscalibration as arising from *system properties* — stale memory, uniform confidence, poor error surfacing. [[wiki/sources/kakao-vc-ai-agent-advertising|Kakao Ventures (2026)]] introduces a party with an **economic interest in over-trust**, and the levers behave differently:
>
> - **Provenance** can be technically accurate and commercially selected — citing a real source says nothing about which real sources were suppressed.
> - **Uncertainty display** is a design choice made by the interested party.
> - **Progressive autonomy** becomes exploitable: reliability on verifiable tasks buys trust that transfers to unverifiable ones.
>
> Lee & See's *resolution* property — trust differentiating across contexts — is precisely what a well-built influence channel defeats, by making sponsored and unsponsored recommendations identical in form.
>
> **Empirically:** conversational sponsored recommendations were selected at **61.2%** versus **22.4%** in search, and explicit labels *plus warnings* only reduced that to **55.5%**; hidden intent was detected **under 10%** of the time. (Second-hand figures — see the source page caveats.) Combined with [[concepts/agent-experience/willful-blindness|willful blindness]], disclosure has now underperformed in two independent results.
>
> Where incentives diverge, the intervention moves **upstream of the interface** to incentive structure. See [[wiki/concepts/agent-experience/principal-agent-problem|Principal–Agent Problem (AI)]] and [[wiki/analyses/2026-07-30-trust-measurement-and-monetization|the 2026-07-30 memo]].

## Design Levers

- Show provenance: where did this answer/action come from
- Express uncertainty honestly instead of uniform confidence
- Preview-then-commit for consequential actions
- Make agent failures legible and recoverable rather than hidden
- Progressive autonomy: earn wider permissions through demonstrated reliability

## Related Concepts

- [[concepts/agent-experience/agent-transparency|Agent Transparency]]
- [[concepts/agent-experience/error-recovery|Error Recovery]]
- [[concepts/agent-experience/proactivity-design|Proactivity Design]]
- [[concepts/ux-research/human-in-the-loop|Human in the Loop]]
- [[concepts/ai-agents/agent-memory|Agent Memory]]
- [[wiki/concepts/agent-experience/principal-agent-problem|Principal–Agent Problem (AI)]] — the adversarial case these levers were not built for.
- [[wiki/concepts/agent-experience/delegation-spectrum|Delegation Spectrum]] — which affordances are even available at a given delegation tier.
- [[wiki/concepts/ux-research/ai-ux-measurement-constructs|AI UX Measurement Constructs]] — the candidate instrument for measuring trust and dependency.

## Conflicts & Caveats

- Now grounded in Lee & See (2004), the foundational appropriate-reliance model; note it predates LLMs, so transfer of specific dynamics to generative agents should still be validated per feature.
- **The 2004 model describes the target, not the adversary.** It was built for automation that could be unreliable, not for automation that could be *incentivized*. See the callout above.
- **Comparison-based interventions do not scale down the delegation spectrum.** At [[wiki/concepts/agent-experience/delegation-spectrum|tier 3+]] the user has nothing on screen to compare against, so labels and disclosures lose their mechanism. No source in this vault yet proposes a tested tier-3 intervention.

## Sources

- [[sources/lee-see-2004-trust-in-automation|Lee & See (2004): Trust in Automation]]
- [[sources/hbs-working-knowledge-ai-advice-willful-blindness|Chan (2026): When AI Gives Advice, Employees Rarely Ask Why]]
- [[sources/andru-saksena-adobe-haic-2025|Adobe HAIC Framework]]
- [[sources/theaxlabs-contaminated-memory-performance|AX LABS: Contaminated Memory]]
- [[sources/microsoft-design-ux-for-agents|Microsoft Design (2025): UX Design for Agents]]
- [[wiki/sources/kakao-vc-ai-agent-advertising|Kakao Ventures (2026): AI Agents — Questioning the Qualifications of a True Representative]] — commercial capture of calibration; the disclosure-insufficiency figures.
- [[wiki/sources/measuringu-measuring-the-ux-of-ai|Sauro & Lewis (2026): Measuring the UX of AI]] — candidate trust and dependency constructs. Unvalidated.

## Open Questions

- Which uncertainty display format actually changes verification behavior rather than being ignored?
- How fast does trust recover after a visible agent failure, and what repair moves accelerate it?
- Does self-reported AI Dependency predict *observed* verification behavior?
- Is there any calibration lever that survives an optimizing counterparty, short of changing its incentives?

## See Also

- [[wiki/analyses/2026-07-30-trust-measurement-and-monetization|Analysis: Measuring Trust While Trust Is Being Monetized]]
