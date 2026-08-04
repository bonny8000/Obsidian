---
type: concept
status: active
created: 2026-06-12
updated: 2026-08-04
tags: [agent-experience, transparency, explainability, ax, disclosure, principal-agent, citation, automation-bias]
sources:
  - sources/andru-saksena-adobe-haic-2025
  - sources/amershi-2019-human-ai-guidelines
  - sources/lee-see-2004-trust-in-automation
  - sources/christinevallaure-a2ui-generative-ui
  - sources/kakao-vc-ai-agent-advertising
  - pxd-writone-ai-writing-assistant
  - sources/paxton-yao-voice-ai-thinking-state
  - sources/toyota-voice-interaction-humanoid-robots
  - sources/cloudflare-responsible-ai-bot-principles
  - sources/google-search-io-2026-agents
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
- [[wiki/sources/pxd-writone-ai-writing-assistant|pxd (2026): Writone]] — **the favourable case for disclosure.** Every correction cites the guideline source and principle page, and the reason is given in human language rather than algorithmic terms. This is a materially stronger form than a label, because it is *checkable*: the user can go read the cited rule. It fits the mechanism [[wiki/analyses/2026-07-30-trust-measurement-and-monetization|the trust memo]] identifies — disclosure works by inviting a comparison the user can actually make. Note the limits: the source measures no acceptance rate, so it cannot show that citing the rule changes behaviour rather than merely reassuring, and there is no adversarial party here, which is what made the unfavourable cases unfavourable.

## State Legibility Is a Layer Beneath This One

> [!important] Added 2026-08-04 — a distinction this page has been missing
> Everything above concerns making *reasoning, data use, and provenance* legible. [[wiki/sources/paxton-yao-voice-ai-thinking-state|Yao (2026)]] identifies a cheaper, lower layer that has to work first: **what is the system doing right now?**
>
> In voice, *"silence means several different things"* — not heard, listening, processing, about to speak. And LLM inference created a state with no prior equivalent: *"gap is a new state that didn't exist before."* **A user who cannot tell whether the agent is listening has no use for a reasoning trace.** See [[wiki/concepts/agent-experience/system-state-signaling|System State Signaling]].
>
> This matters for the disclosure-scepticism warning above: the two failures are different. Disclosure fails because users do not *use* available information. State signalling fails because the information is not *there*. The second is a solvable design problem; the first may not be.

> [!warning] Latency masking is a small deception this vault should name
> [[wiki/sources/toyota-voice-interaction-humanoid-robots|Toyota (2026)]] generates fillers (*"Um"*, *"Well"*) **pre-emptively, when a delay is anticipated** — the system performing thought it is not yet doing. It is a fake progress bar made of speech, and Toyota treats it purely as craft.
>
> It is benign in a mascot robot. It is not obviously benign before a recommendation the user will act on, because a convincing stall manages the user's impression of the system's confidence. And it may actively conflict with honest state signalling: a filler implying the answer is nearly ready, running alongside an indicator reporting "thinking," gives the user two different stories. **Nobody has tested whether covering and labelling compose.**
>
> Guidance: no performed thinking ahead of a consequential decision. See [[wiki/concepts/agent-experience/response-latency-masking|Response Latency Masking]], [[wiki/comparisons/filling-the-response-gap|the decision table]], and [[wiki/analyses/2026-08-04-the-response-gap|the memo]].

> [!note] The one favourable structural case for disclosure: a machine audience
> [[wiki/sources/cloudflare-responsible-ai-bot-principles|Cloudflare's AI bot principles]] are disclosure obligations — declare identity, operator, and purpose — and they are the strongest available rebuttal to this page's disclosure scepticism, because **the audience is a machine-readable policy engine, not a person deciding under time pressure.** A filter can be made to act on a declaration; a human cannot be made to read one.
>
> The rebuttal holds only if the declaration is *verifiable*. Until **Web Bot Auth** (IETF draft) deploys, every one of those declarations is a self-reported string — which makes it [[wiki/concepts/agent-experience/checkbox-transparency|checkbox transparency]] with extra steps. See [[wiki/concepts/infrastructure-dev/ai-crawler-governance|AI Crawler Governance]].

> [!warning] A second audience with no interface
> Google's agentic booking now [[wiki/sources/google-search-io-2026-agents|places phone calls to businesses on a user's behalf]]. Every transparency framework on this page assumes the audience is the user. A callee has no interface, no disclosure, and no consent — and no concept in this vault covers that case. Whether the business is told it is speaking to an AI is not stated in the announcement.

## Open Questions

- What is the minimum process visibility users need during long-horizon agent tasks to stay comfortable without babysitting the agent?
- Does provenance display change decisions, or only confidence?
- Does an honest state indicator plus a latency-masking filler compose, or does the filler make the indicator read as evasion?
- **Where is the line at which latency masking becomes misleading rather than polite?**
- What does transparency owe a third party the agent contacts, who never agreed to anything?

## Additional Sources

- [[wiki/sources/paxton-yao-voice-ai-thinking-state|Yao (2026): Voice AI Gave Designers a New State to Show]] — state legibility as the layer beneath transparency.
- [[wiki/sources/toyota-voice-interaction-humanoid-robots|Toyota FRC (2026): Voice Interaction with Humanoid Robots]] — pre-emptive fillers as performed thinking.
- [[wiki/sources/cloudflare-responsible-ai-bot-principles|Cloudflare (2025/2026): Responsible AI Bot Principles]] — disclosure to a machine audience; the favourable structural case, contingent on verification.
- [[wiki/sources/google-search-io-2026-agents|Google (2026): Search at I/O 2026]] — agentic calling, and the third-party audience with no interface.
