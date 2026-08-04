---
type: concept
status: active
created: 2026-08-04
updated: 2026-08-04
tags: [concept, ux-research, affordance, discoverability, convention, design-system-defaults, accessibility, mental-models]
sources: [boongranii-cursor-pointer-debate, smashing-matching-ai-modality-user-intent]
confidence: 0.62
---

# Perceived Affordance

> [!abstract] Summary
> An affordance is what a control actually permits. A **perceived** affordance is what the user can tell it permits, before acting. The two come apart routinely, and the gap is where discoverability failures live.
>
> The vault's worked instance is the `cursor: pointer` debate ([[wiki/sources/boongranii-cursor-pointer-debate|Boongranii, 2026]]), which is really a case study in a more general problem: **what to do when a formal specification and a learned user convention disagree.**

## Why It Matters

The classical position — Adam Silver's, in the cursor debate — is that a control should announce itself: *"a button must convey clickability by appearance alone."* If it needs a cursor change to be discoverable, the visual design failed.

That argument is sound **and conditional on a premise that contemporary UI frequently violates.** The three standard cases where visual affordance is genuinely thin:

- a **text-only button** with no border or fill
- a **ghost button** with a hairline border
- a **whole card** as the click target

The card is the decisive one. Nothing about a card announces that its entire surface is interactive, and no amount of visual craft short of adding a visible button changes that. *"시각적 어포던스가 약해요"* — the visual affordance is weak.

## Specification vs. Learned Convention

The general form of the problem, and the reason this concept is worth having beyond CSS:

| Authority | What it establishes | What it cannot establish |
|---|---|---|
| **Specification** (W3C, platform HIG) | Intended semantics — `cursor: pointer` means *link* | What users have learned to expect |
| **Learned convention** (20+ years of use) | An actual fact about users' [[wiki/concepts/ux-research/mental-models\|mental models]] | That the semantics are correct |

Neither authority resolves the other. A design system default must pick one, and the honest move is to **name which you are following and on what grounds** rather than to argue the other side away.

Boongranii's position: *"결국 UX는 스펙이 아니라 사용자를 위한 거잖아요"* — *in the end UX is for users, not for the spec.* Removing a twenty-year convention because it conflicts with a specification is *"사용자가 아니라 스펙을 위한 결정"* — a decision for the spec, not for the user.

## Key Claims

- **Perceived affordance is formed by exposure, not documentation.** Twenty years of consistent behaviour made `pointer` = clickable a fact about users regardless of what the spec says. This is the clearest example in the vault of a mental model created by accumulated exposure.

- **Recurring bug reports are evidence of a discoverability gap.** After Tailwind CSS v4 removed the pointer default, shadcn/ui users filed the same complaint repeatedly (#7501, #7223, #6843, #7279): *"posts keep appearing saying they can't tell it's clickable because the cursor doesn't change."* Unprompted recurrence following a single default change is close to a natural experiment.

- **A design-system default is a decision made once and inherited by people who never see it.** One preflight change propagated to every downstream consumer and generated four issue threads in one library. The strongest available argument for documenting defaults *with rationale*. See [[wiki/concepts/infrastructure-dev/design-system-implementation|Design System Implementation]].

- **Availability is part of the affordance.** The recommended recipe pairs `cursor: pointer` on interactive elements with `cursor: not-allowed` on `[disabled]` and `[aria-disabled='true']` — the half most implementations skip.

- **The receiver's situation outranks the producer's model of correctness.** [[wiki/sources/smashing-matching-ai-modality-user-intent|Yocco]] makes the same argument about modality defaults; this makes it about specification defaults. Two independent instances of one principle.

## ⚖️ Conflicts & Caveats

> [!warning] The cursor fix serves only the input modality that was already best served
> This is the most important correction on the page and neither source states it. A cursor exists only for pointer users. Touch has none; keyboard navigation has none; screen readers have none. The clickable-card problem — interactivity that is not announced — is **worse** for those users, and `cursor: pointer` leaves it exactly where it was while making it feel addressed.
>
> Under [[wiki/concepts/ux-research/web-accessibility-pour|POUR]], the real defect is that the target is not perceivable or operable without a mouse. Fix the affordance *and* set the cursor; do not let the cursor substitute for the fix.

> [!warning] The accessibility argument in the source is reasoning, not research
> Boongranii's claim that a cursor change is more detectable than a subtle hover colour change is plausible and cited to nothing. WCAG and the accessibility literature go unmentioned.

> [!warning] The GitHub-issue evidence is developer-reported and unquantified
> Developers who file issues are motivated intermediaries, not users. The signal is real; its magnitude is unknown.

> [!warning] Nobody has measured it
> After twenty years of this debate, there appears to be no published study on discoverability of low-affordance click targets by input modality. That is the gap, and it is trivially runnable.

## Practical Guidance

1. **Treat the cursor as redundant confirmation, never as the affordance.** If an element needs it to be discoverable, it is undiscoverable to touch and keyboard users.
2. **Use weak visual affordance as the trigger.** Obviously-buttoned controls do not need it; ghost buttons, text buttons, and clickable cards do — and they need more than a cursor.
3. **Set `not-allowed` on disabled controls.** State is free to encode here.
4. **Decide once, in the base layer, and record why.** An inconsistent answer across components is worse than either position.
5. **When spec and convention conflict, write down which you chose.** The decision is legitimate either way; leaving it undocumented is what causes the churn.

## 🔗 Related Concepts

- [[wiki/concepts/ux-research/mental-models|Mental Models]] — where learned conventions live.
- [[wiki/concepts/ux-research/web-accessibility-pour|Web Accessibility (POUR)]] — the principle that catches what the cursor argument misses.
- [[wiki/concepts/ux-research/cta-friction|CTA Friction]] — the adjacent problem: not impeding an action the user has already found.
- [[wiki/concepts/infrastructure-dev/design-system-implementation|Design System Implementation]] — where defaults are decided and inherited.
- [[wiki/concepts/infrastructure-dev/component-catalog|Component Catalog]]
- [[wiki/concepts/infrastructure-dev/modern-web-guidance|Modern Web Guidance]]
- [[wiki/concepts/agent-experience/modality-intent-matching|Modality–Intent Matching]] — the same receiver-over-producer principle, applied to modality.
- [[wiki/concepts/ux-research/five-planes-of-ux|Five Planes of UX]] — affordance sits on the surface plane and fails because of skeleton-plane decisions.
- [[wiki/concepts/agent-experience/system-state-signaling|System State Signaling]] — the agent-era version: making state, not just interactivity, perceivable.

## 📚 Sources

- [[wiki/sources/boongranii-cursor-pointer-debate|Boongranii (2026): Should Clickable Elements Use cursor: pointer?]] — primary source. The debate history, both named camps, the weak-affordance cases, the base-layer recipe, and the GitHub-issue evidence.
- [[wiki/sources/smashing-matching-ai-modality-user-intent|Yocco (2026): Matching AI Modality to User Intent]] — the parallel instance of receiver-over-producer, from modality.

## ❓ Open Questions

- What is the discoverability rate for a clickable card with and without `cursor: pointer`, by input modality? Twenty years of debate and no study.
- What is the touch and keyboard equivalent of the affordance the cursor patches — and does adding the cursor reduce pressure to build it?
- Does the twenty-year convention hold for users who came to computing on touch first? The argument assumes a desktop-formed mental model.
- Are there other live cases where a specification and a learned convention conflict, and does the same "name your choice" resolution hold?
