---
type: concept
status: draft
created: 2026-07-28
updated: 2026-07-28
tags: [concept, agent-experience, accessibility, adaptive-interfaces, multimodal-agents, gemini, gemma, needs-evidence]
sources: [google-natively-adaptive-interfaces, veronikapj-whats-new-android-2026]
confidence: 0.45
---

# Natively Adaptive Interfaces

> [!abstract] Summary
> Google's framing for building accessibility **into the core of a multimodal AI agent** rather than layering it over a fixed interface — so adaptation to a user's abilities and context happens per-interaction, as an agent capability, rather than per-breakpoint as a UI property. Named **NAI**, tied to Gemini and Gemma models.

> [!warning] Draft — framing only, no captured guidance
> The anchor source is a **documentation hub page**, captured without its sub-guides. Everything below is NAI's self-description plus this wiki's own reasoning. `confidence: 0.45` reflects **capture quality, not source quality**. Do not build a design recommendation on this page until [[wiki/sources/google-natively-adaptive-interfaces|the source]] is properly ingested.

## 📝 Key Claims

As stated by the source, unverified:

- **Accessibility is foundational, not supplementary** — explicitly not a compliance afterthought.
- **Multimodal integration is the mechanism** — an agent that shifts between voice, text, and visual channels can adapt to ability and context in ways a fixed layout cannot.
- **Native adaptation** — adaptive and interactive accessibility built into the agent itself.
- **Low entry barrier is claimed** — the MVP path is stated to require no prior accessibility experience.

## Why the framing is worth keeping anyway

Independent of Google's tooling, the reframing is substantive: **if an agent mediates the interface, adaptation can be per-interaction rather than per-breakpoint.** Responsive design adapts to the *device*; NAI proposes adapting to the *person and situation*. That is a different axis, and this wiki has no other source that names it.

It also arrives alongside two independent signals that accessibility metadata is gaining load:

| Source | Argument for accessibility investment |
|---|---|
| [[wiki/sources/b2b-admin-web-accessibility\|rami_ (2026)]] | Repetition economics — daily operators compound each improvement |
| [[wiki/sources/veronikapj-whats-new-android-2026\|Android 2026]] | Agent automation (Computer Control) *consumes* accessibility semantics |
| Google NAI | Accessibility as an agent-native capability |

Three different reasons, same direction, none of them compliance.

## ⚖️ Conflicts & Caveats

> [!warning] Unresolved: does agent adaptation raise or lower the need for underlying semantics?
> Android's Computer Control **reads** accessibility semantics, so poor labeling breaks agent automation. NAI's framing can be read as the agent **generating** adaptation instead. If agents adapt natively, is semantic quality underneath more important or less? The answer determines where to invest, and no source resolves it. This is the single most useful question to answer on the next pass.

> [!warning] The remediation trap in reverse
> "The agent adapts it" is available as a reason not to make the underlying interface accessible — which would leave every non-agent user worse off.

> [!warning] Vendor framework, model-coupled
> NAI is Google's coinage and the Gemini/Gemma dependence is architectural, not incidental. Compare the pattern of "AI-native design system" (Atlassian's coinage): adopt the concept, do not assume the stack.

> [!warning] "No prior accessibility experience required" deserves scrutiny
> Accessibility failures are usually failures of judgment about users. Tooling does not obviously supply that judgment, and this claim is the least examined part of the framing.

> [!warning] Easily confused with adaptive layout
> Android's "adaptive by default" is about window size classes and reflow — a device-geometry problem. NAI is about ability and context adaptation in agents. Different problems; keep the terms distinct.

## 🔗 Related Concepts

- [[wiki/concepts/ux-research/web-accessibility-pour|Web Accessibility (POUR)]] — the standards layer NAI claims to build in natively.
- [[wiki/concepts/agent-experience/agent-invocable-app-functions|Agent-Invocable App Functions]] — the sibling: agents *invoking* capability vs. agents *adapting* presentation.
- [[wiki/concepts/ux-research/ai-native-ux-design|AI-Native UX Design]]
- [[wiki/concepts/agent-experience/mental-model-onboarding|Mental Model Onboarding]]
- [[wiki/concepts/agent-experience/trust-calibration|Trust Calibration]]
- [[wiki/concepts/agent-experience/a2ui-protocol|A2UI Protocol]] — agent-composed UI from a machine-readable catalog; the generative-UI cousin.
- [[wiki/concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]] — where this wiki already holds that accessibility belongs in the context layer.

## 📚 Sources

- [[wiki/sources/google-natively-adaptive-interfaces|Google (n.d.): Natively Adaptive Interfaces]] — **partial capture, `llm_ready: false`.** Hub page only; sub-guides not fetched.
- [[wiki/sources/veronikapj-whats-new-android-2026|배필주 (2026): What's New in Android 2026]] — for the contrasting semantics-consuming model (Computer Control) and for the adaptive-layout distinction.

## ❓ Open Questions

- What does NAI actually prescribe? Every substantive question is open.
- Is it about accessibility for users **of the agent**, for the **interface the agent operates**, or both?
- Relationship to WCAG — complement, superset, or orthogonal?
- Is any of it usable without Gemini or Gemma?
- Does native adaptation reduce the need for accurate accessibility semantics, or depend on them?

## Backfill Status

Blocked on a deeper capture of the anchor source. See [[wiki/sources/google-natively-adaptive-interfaces|that page's Backfill Status]] for the ordered next steps: Overview guide → MVP guide → Terminology reference → establish a date. Promote this page from `draft` to `active` and revise confidence once real guidance is in hand.
