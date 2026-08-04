---
type: concept
status: active
created: 2026-07-28
updated: 2026-08-04
tags: [concept, accessibility, wcag, pour, b2b-admin, agent-compatibility, front-end]
sources: [b2b-admin-web-accessibility, veronikapj-whats-new-android-2026, google-natively-adaptive-interfaces, boongranii-cursor-pointer-debate, paxton-yao-voice-ai-thinking-state]
confidence: 0.75
---

# Web Accessibility (POUR)

> [!abstract] Summary
> WCAG's four foundational principles — **Perceivable, Operable, Understandable, Robust** — and the practical claim attached to them here: accessibility metadata has acquired a **second consumer**. Semantics written for assistive technology now also determine whether agent-driven automation can operate an interface at all. Under-labeled UI is simultaneously an accessibility defect and an agent-compatibility defect.

> [!important] Why it Matters
> Two independent arguments for accessibility investment converged in 2026, neither of them compliance. First, **repetition economics**: in B2B admin tools the same operators repeat the same tasks daily, so each interaction improvement compounds instead of amortizing across one-time visitors. Second, **agent dependency**: Android's Computer Control drives apps that made no code changes by reading **accessibility semantics**, which makes an accessibility audit a prerequisite for agent compatibility.

## 📝 Key Claims

- **POUR benefits all users**, not only users with disabilities — the standard framing, and the basis for the repetition argument.
- **Accessibility payback scales with repetition, not traffic.** An internal tool with 20 daily operators can justify more per-user interaction investment than a page with 20,000 monthly visitors. Table-heavy interfaces used daily are the strongest case: screen readers cannot distinguish data types without header associations, and icon-only buttons without labels force repeated mouse navigation.
- **Accessibility semantics are the agent's fallback interface.** Where an app exposes no callable functions, agent automation reads the accessibility tree. The Android 2026 session lists an accessibility semantic audit as prepare-now work *because* it supports Computer Control.
- **Accessibility belongs in the agent context layer, not in downstream QA.** Rules written into `CLAUDE.md` / `AGENTS.md` produce accessible generated code by default; corrections after the fact do not scale.
- **Automated accessibility counts must be verified against source files.** Line-based search over multi-line markup produces large false positives — see the 168-vs-6 case below.
- **Partial assurance is the honest report.** "Pre-commit lint gives partial coverage" is correct; "we have zero missing alt attributes" usually is not.

## Highest-leverage first passes

Ordered by effect-to-effort, from the anchor implementation:

1. **`<html lang>`** set correctly — one line, changes screen-reader pronunciation for the whole application.
2. **Keyboard operability** — the whole flow reachable and completable without a mouse.
3. **Form labels** — programmatically associated, not merely adjacent.
4. **`aria-label` on icon-only buttons** — download, delete, refresh.
5. **`scope="col"` on table headers** — what makes a data table navigable rather than a grid of unlabeled values.
6. **Decorative vs. meaningful images** — `alt=""` for decorative; i18n-managed alt text for meaningful, reusing existing localization keys.

## The verification cautionary case

| Automated scan reported | Actual, after opening the files |
|---|---|
| 168 missing `alt` attributes | **6** |
| 166 missing `th` tags | **141** |

A 28× overcount on one metric, caused by line-based grep against multi-line attribute formatting. Note the asymmetry: the `th` finding was largely *real*. This is one unreliable instrument, not an argument against automated scanning — and the fix is parser- or AST-based analysis rather than line search, the same choice [[wiki/sources/socar-parking-brain-knowledge-graph|SOCAR]] made for code extraction.

## ⚖️ Conflicts & Caveats

> [!warning] The repetition-payback argument is unmeasured
> It is the most interesting claim here and the least supported one — no task-time study, no operator feedback data, one codebase. Treat as a **hypothesis worth testing**, not a finding. It is also a small, genuinely useful UX research study that nobody in this wiki's evidence base has run.

> [!warning] Structural correctness ≠ verified experience
> The anchor source reports no testing with actual assistive-technology users. Correct markup is necessary and not sufficient.

> [!warning] Unresolved: does agent adaptation increase or reduce the need for semantics?
> Android's Computer Control **consumes** accessibility metadata, so poor labeling breaks agent automation. Google's [[wiki/concepts/agent-experience/natively-adaptive-interfaces|Natively Adaptive Interfaces]] framing could be read as **generating** adaptation inside the agent instead. If agents adapt natively, is underlying semantic quality more or less important? No source resolves this, and the answer changes where to invest.

> [!warning] The remediation trap, in reverse
> "The agent adapts it" is available as an excuse not to make the underlying interface accessible — which would leave non-agent users worse off than before.

> [!warning] Partial scope
> The anchor implementation covers keyboard, labels, and table semantics. Contrast, focus management, live regions, and error handling are untouched, and this concept page inherits that gap.

## 🔗 Related Concepts

- [[wiki/concepts/agent-experience/natively-adaptive-interfaces|Natively Adaptive Interfaces]] — accessibility as an agent-native capability; the source of the unresolved tension above.
- [[wiki/concepts/agent-experience/agent-invocable-app-functions|Agent-Invocable App Functions]] — the explicit-contract alternative to semantics-scraping automation.
- [[wiki/concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]] — argues accessibility constraints belong in the context layer, generating accessible UI by default.
- [[wiki/concepts/infrastructure-dev/claudemd-context|CLAUDE.md / AGENTS.md Context]] — where accessibility rules live to prevent regression.
- [[wiki/concepts/ai-agents/workflow-completeness|Workflow Completeness]] — verify by inspection, not by the tool's report.
- [[wiki/concepts/infrastructure-dev/localization-ux|Localization UX]] — i18n-managed alt text and `lang` correctness.
- [[wiki/concepts/infrastructure-dev/knowledge-linting|Knowledge Linting]]
- [[wiki/concepts/ux-research/ai-native-ux-design|AI-Native UX Design]]

## 📚 Sources

- [[wiki/sources/b2b-admin-web-accessibility|rami_ (2026): Applying Web Accessibility to a B2B Admin Service]] — POUR framing, repetition-payback argument, the first-pass checklist, and the grep verification case.
- [[wiki/sources/veronikapj-whats-new-android-2026|배필주 (2026): What's New in Android 2026]] — accessibility semantics as the substrate for Computer Control agent automation.
- [[wiki/sources/google-natively-adaptive-interfaces|Google (n.d.): Natively Adaptive Interfaces]] — accessibility as an agent-native capability. **Partial capture, `llm_ready: false`** — framing only.

## ❓ Open Questions

- Does accessibility work in high-repetition internal tools produce measurable task-time improvement?
- What is the reliable false-positive rate for line-based versus AST-based accessibility scanning?
- Do accessibility rules in an agent context file actually prevent regression in generated code, and how would that be measured?
- Which constraints are best expressed as lint rules (structural) versus context-file guidance (judgment)?
- How reliable is accessibility-semantics-driven agent automation against poorly labeled apps — the majority case?
- **What is the touch and keyboard equivalent of the affordance `cursor: pointer` patches** — and does adding the cursor reduce the pressure to build it?
- What is the discoverability rate of a clickable card by input modality? Twenty years of debate on this and apparently no published study.

## Two Cases Where an Accessibility Argument Fixes the Wrong Channel

> [!warning] Added 2026-08-04 — both new sources make an accessibility case for a single-channel signal
> POUR exists partly to prevent exactly this, and two sources ingested 2026-08-04 walk into it from different directions. Recorded here because in both, the reasoning is well-intentioned and the effect is to make a defect *feel* addressed.
>
> **1. `cursor: pointer` serves the modality that was already best served.** [[wiki/sources/boongranii-cursor-pointer-debate|Boongranii (2026)]] argues for setting the cursor on clickable elements partly on accessibility grounds: not all users perceive a subtle hover colour change, and a cursor change is near-universally detectable.
>
> That is true **for pointer users, who are the only users a cursor exists for.** Touch has no cursor; keyboard navigation has none; screen readers have none. And the case the essay makes best — a whole card as the click target, with nothing announcing that its surface is interactive — is **worse** for those users. Under POUR the real defect is that the target is not *perceivable* or *operable* without a mouse, and the cursor leaves that defect exactly where it was.
>
> **Guidance: fix the affordance and set the cursor.** Never let the cursor substitute for the fix. See [[wiki/concepts/ux-research/perceived-affordance|Perceived Affordance]].
>
> **2. Colour-only state signalling, chosen for colourblind safety.** [[wiki/sources/paxton-yao-voice-ai-thinking-state|Yao (2026)]] picks orange/blue for a voice assistant's state indicator because the pair is *"distinguishable across nearly all forms of color vision deficiency"* — good reasoning at the encoding stage, and then colour is the *sole* channel carrying state.
>
> A colourblind-safe palette does not satisfy the redundancy principle. The argument is made in a **driving** context, where the alternatives (audio, haptics) are free and eyes-free, and where blind and low-vision users go unaddressed inside an accessibility argument. **Guidance: state must never rest on one channel** — add shape, motion, audio, or haptic. See [[wiki/concepts/agent-experience/system-state-signaling|System State Signaling]].
>
> **The generalisable pattern:** an accessibility improvement to one channel is not an accessibility fix if the underlying signal is still single-channel. Ask which modality the fix reaches, then ask which modalities the original defect affects.

## Additional Sources

- [[wiki/sources/boongranii-cursor-pointer-debate|Boongranii (2026): Should Clickable Elements Use cursor: pointer?]] — the weak-affordance cases and the pointer-only accessibility argument.
- [[wiki/sources/paxton-yao-voice-ai-thinking-state|Yao (2026): Voice AI Gave Designers a New State to Show]] — colour-vision-safe palette selection as sole state channel.
