---
type: concept
status: active
created: 2026-06-12
updated: 2026-07-30
tags: [agent-experience, transparency, explainability, ax, disclosure, principal-agent]
sources:
  - sources/andru-saksena-adobe-haic-2025
  - sources/amershi-2019-human-ai-guidelines
  - sources/lee-see-2004-trust-in-automation
  - sources/christinevallaure-a2ui-generative-ui
  - sources/kakao-vc-ai-agent-advertising
confidence: 0.72
---

# Agent Transparency

## Summary

Agent transparency is the practice of making an agent's reasoning, data use, capabilities, and limits legible to the user at the right granularity — enough to support verification and trust, not so much that it becomes noise.

## Why It Matters

Probabilistic systems break the predictability assumptions of traditional UI. Users cannot form a working mental model of an agent unless the interface exposes what it considered, what it did, and what it cannot do.

## Key Claims

- Transparency operates at three layers: capability (what the agent can do), process (what it is doing now and why), and provenance (what evidence an output rests on).
- Full reasoning traces are rarely the right default; progressive disclosure (summary by default, detail on demand) preserves both legibility and flow.
- "Why am I seeing this" explanations matter most at proactive moments, where the agent acted without being asked.
- Transparency about data use (which personal context the agent read) is a trust and privacy requirement, not just a UX nicety.
- Honest capability boundaries ("I can't access X") outperform vague deflection in long-run trust.
- Lee & See's purpose/process/performance dimensions give the three-layer structure its empirical basis: users build trust from why the system exists, how it works, and its track record — see [[sources/lee-see-2004-trust-in-automation|Lee & See 2004]].
- **The recipe/renderer split is an agent-experience surface.** In [[concepts/agent-experience/a2ui-protocol|A2UI]], the agent emits a structured "recipe" that a renderer turns into a screen from approved catalog components — a provenance boundary that shapes whether users can trust generated UI, and where a [[concepts/infrastructure-dev/component-catalog|catalog]] gap can cause a silent "quiet downgrade" the user feels without explanation ([[sources/christinevallaure-a2ui-generative-ui|Vallaure, 2026]]).
- **Transparency, control, and consistency:** Microsoft Design states these three elements are foundational. Specifically, background agents running invisibly must provide a user-facing mechanism (logs/dashboards) to view and control their actions — see [[concepts/agent-experience/microsoft-agent-ux-principles|Microsoft Agent UX Principles]].

## Related Concepts

- [[concepts/agent-experience/trust-calibration|Trust Calibration]]
- [[concepts/agent-experience/proactivity-design|Proactivity Design]]
- [[concepts/agent-experience/mental-model-onboarding|Mental Model Onboarding]]
- [[concepts/ux-research/ax-ai-experience|AX (AI Experience)]]
- [[concepts/agent-experience/a2ui-protocol|A2UI Protocol]] — the agent-to-UI rendering surface.
- [[wiki/concepts/agent-experience/delegation-spectrum|Delegation Spectrum]] — why disclosure loses its mechanism at higher tiers.
- [[wiki/concepts/agent-experience/principal-agent-problem|Principal–Agent Problem (AI)]] — when the party providing the transparency has a stake in the outcome.
- [[concepts/agent-experience/checkbox-transparency|Checkbox Transparency]]

## Conflicts & Caveats

- Tension exists between transparency and cognitive load; more explanation is not always better. Amershi et al.'s G11 (explain why the system acted) and Lee & See's purpose/process/performance dimensions now ground the framework, though both predate long-horizon generative agents.

> [!warning] Disclosure has now underperformed in two independent results
> This concept's implicit premise is that legibility produces appropriate reliance. Two unrelated findings say the mechanism is weaker than assumed:
>
> - **Disclosure barely moves behavior.** Conversational sponsored recommendations were selected at **61.2%** versus **22.4%** in search; adding explicit "Sponsored" labels *plus warnings* reduced that only to **55.5%**, and hidden intent went undetected **over 90%** of the time ([[wiki/sources/kakao-vc-ai-agent-advertising|Kakao Ventures, 2026]] — second-hand figures, see source caveats).
> - **Available explanations go unread** when incentives point the other way — [[concepts/agent-experience/willful-blindness|willful blindness]] ([[sources/hbs-working-knowledge-ai-advice-willful-blindness|Chan, 2026]]).
>
> **The mechanism worth naming: disclosure works by inviting comparison.** A results page offers something to compare against; a single generated recommendation does not. So the failure is structural rather than a labelling-design problem, and it worsens as products move up the [[wiki/concepts/agent-experience/delegation-spectrum|delegation spectrum]]. Transparency remains necessary; it is not sufficient, and it should not be counted as a safeguard. See [[concepts/agent-experience/checkbox-transparency|Checkbox Transparency]] — now an empirical finding rather than a critique.

## Sources

- [[sources/amershi-2019-human-ai-guidelines|Amershi et al. (2019): Human-AI Guidelines]]
- [[sources/lee-see-2004-trust-in-automation|Lee & See (2004): Trust in Automation]]
- [[sources/andru-saksena-adobe-haic-2025|Adobe HAIC Framework]]
- [[sources/christinevallaure-a2ui-generative-ui|Vallaure (2026): A2UI Under the Hood]] — recipe/renderer split as a transparency/provenance surface.
- [[sources/microsoft-design-ux-for-agents|Microsoft Design (2025): UX Design for Agents]]
- [[wiki/sources/kakao-vc-ai-agent-advertising|Kakao Ventures (2026): AI Agents — Questioning the Qualifications of a True Representative]] — the disclosure-insufficiency evidence.

## Open Questions

- What is the minimum process visibility users need during long-horizon agent tasks to stay comfortable without babysitting the agent?
- Does provenance display change decisions, or only confidence?
