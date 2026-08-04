---
type: source
status: active
created: 2026-08-04
updated: 2026-08-04
tags: [affordance, cursor-pointer, design-system-defaults, shadcn, tailwind, w3c-spec, accessibility, convention, korean-source]
source_path: raw/web/boongranii-cursor-pointer-debate-2026-08-04.md
source_url: https://www.boongranii.dev/posts/cursor-pointer-debate
authors: [Boongranii]
sources: []
ingest_level: standard
coverage: full
llm_ready: true
raw_preserved: true
confidence: 0.60
---

# Boongranii (2026): Should Clickable Elements Use `cursor: pointer`?

## Citation

Boongranii, "클릭 가능한 요소에 cursor: pointer를 써야 할까?" (*Should Clickable Elements Use `cursor: pointer`?*), personal blog, 2026-06-04. Korean, stated reading time 5 minutes.

**Source type:** Practitioner opinion essay with implementation guidance. The historical account and the GitHub issue references are verifiable; the accessibility argument is the author's reasoning.
**Raw capture:** [[raw/web/boongranii-cursor-pointer-debate-2026-08-04|boongranii-cursor-pointer-debate-2026-08-04]]
**Coverage note:** `coverage: full` — the whole argument, both camps, the CSS recipe, all four cited GitHub issues, and the author's conceded limits.

## Summary

A small, well-structured example of a class of decision this vault has no other source for: **what to do when a formal specification and twenty years of learned user behaviour disagree.**

The trigger is concrete. shadcn/ui ships buttons with `cursor: default`, which felt wrong to the author. The reason it does: the **W3C CSS cursor specification** defines `pointer` as indicating *a link* — not a button, not a form control — and native macOS and Windows applications do not change the cursor over buttons. On the letter of the spec and on platform convention, `cursor: default` is correct. Tailwind CSS v4 changed its preflight default accordingly.

The two positions, both named:

| Camp | Advocate | Argument |
|---|---|---|
| **Prescriptivist** | **Adam Silver**, "Buttons shouldn't have a hand cursor" | *"버튼은 생김새 자체로 클릭 가능함을 전달해야 한다"* — a button must convey clickability by appearance alone. Needing a cursor means the visual design failed. |
| **Pragmatist** | **Chris Coyier** (CSS-Tricks) | Twenty-plus years have trained `pointer` = clickable. *"웹은 OS가 아니다"* — the web is not an OS. |

The author's contribution is not picking a side but identifying **the hidden premise in the prescriptivist argument**: it assumes strong visual affordance exists. In contemporary minimal UI it frequently does not.

> "시각적 어포던스가 약해요" — *the visual affordance is weak.*

The three cases given are the argument: a text-only button, a ghost button with a hairline border, and a whole card that is the click target. The card is the killer — nothing about a card announces that its entire surface is interactive, and no amount of visual craft short of adding a button changes that.

The evidence offered is behavioural rather than experimental: after Tailwind v4 removed the default, shadcn/ui users kept filing the same issue (#7501, #7223, #6843, #7279). *"커서가 안 바뀌어서 누를 수 있는지 모르겠다는 글이 계속 올라온다"* — *posts keep appearing saying they can't tell it's clickable because the cursor doesn't change.* The recurrence is the signal.

> "결국 UX는 스펙이 아니라 사용자를 위한 거잖아요" — *in the end UX is for users, not for the spec.*

## Key Claims

- **The W3C spec supports the prescriptivist position and the author concedes it.** `pointer` means link. Native OS convention agrees. The pragmatist case has to be made *against* the spec, not by reinterpreting it.

- **The prescriptivist argument is conditional on a premise that often fails.** "The appearance should be enough" holds under ideal visual design. Ghost buttons, text buttons, and card-as-target are the counterexamples, and they are the dominant contemporary patterns rather than edge cases.

- **A twenty-year learned convention is a real user-side fact,** not a bad habit to be corrected. *"사람들이 20년 넘게 pointer = 클릭 가능으로 익혀왔잖아요"* — removing it *"사용자가 아니라 스펙을 위한 결정"* (a decision for the spec, not for the user).

- **Recurring bug reports are evidence of friction.** The author treats four independent issue filings on the same complaint as data about real confusion rather than as preference. This is a defensible inferential move and worth naming as such.

- **The cursor is nearly-free redundant feedback.** No performance cost, no side effects, and unlike a subtle hover colour change it does not depend on the user perceiving a small chromatic difference.

- **Disabled state deserves its own cursor.** The recommended recipe pairs `cursor: pointer` on interactive elements with `cursor: not-allowed` on `[disabled]` and `[aria-disabled='true']` — so the cursor carries *availability* as well as interactivity. This second half is the part most implementations skip.

## Useful Examples

**The recommended base layer** — the reusable artifact:

```css
@layer base {
  a, button, [role='button'], input[type='submit'],
  input[type='reset'], input[type='button'], label[for],
  select, summary, [onclick] {
    cursor: pointer;
  }

  [disabled], [aria-disabled='true'] {
    cursor: not-allowed;
  }
}
```

Note `label[for]` and `summary` — two genuinely clickable elements that most hand-rolled selector lists omit.

**The three weak-affordance cases** — text-only button, ghost button, clickable card. Useful as a diagnostic: if your interface contains any of these, the prescriptivist premise does not hold for it.

**The GitHub issue trail** (shadcn/ui #7501, #7223, #6843, #7279) is the best part of the source methodologically. It is a naturally-occurring, unprompted signal from developers reporting on behalf of their users, generated by a framework default change — as close to a natural experiment as this debate has.

## Constraints / Caveats

- **No usability study, no accessibility research, no measurement.** The accessibility claim — that a cursor change is more detectable than a hover colour change — is plausible reasoning and is not cited to anything. WCAG and the accessibility literature go unmentioned.
- **The GitHub issues are a biased sample.** Developers who file issues are not users, they are motivated intermediaries, and nobody counts how many users were actually confused. The signal is real; its magnitude is unknown.
- **The cursor helps only pointer users.** Touch has no cursor, keyboard navigation has no cursor, and screen readers do not have one either. The affordance problem the author correctly identifies — a card whose interactivity is unannounced — is *worse* for those users and `cursor: pointer` does nothing for them. The essay does not notice this, and it is the most significant gap: the fix addresses the one input modality that was already best served.
- **`[onclick]` in the selector list is a smell.** It matches inline handlers only, missing every element with a listener attached in JavaScript, which is nearly all of them in a React codebase. The recipe is not as complete as it appears.
- **Framing the disagreement as two camps flattens it.** Neither Silver nor Coyier is quoted at length or in context; both are used as position markers.
- **Single-author blog, no review.** The historical account is checkable and appears accurate; the conclusion is an opinion, correctly presented as one.

## Design Implications

- **Treat the cursor as redundant confirmation, never as the affordance.** If an element needs the cursor to be discoverable, it is undiscoverable to touch and keyboard users. Fix the visual affordance *and* set the cursor.
- **Use weak visual affordance as the trigger for the decision.** Strong, obviously-buttoned controls genuinely do not need it. Ghost buttons, text buttons, and clickable cards do — and the honest reading is that they need more than a cursor.
- **Set `not-allowed` on disabled controls.** Availability is state, and the cursor is a free channel for it.
- **Decide this once, in the base layer, and write down why.** A design system that leaves it to component authors gets an inconsistent answer, which is worse than either position.
- **When a spec and a learned convention conflict, name which one you are following and on what grounds.** The generalisable lesson: the specification is authoritative about meaning, not about what users have learned, and neither claim settles the other.

## Tensions

- **The central tension is between specification correctness and learned convention,** and this source is the vault's only worked instance of it. The generalisation matters more than the cursor: a formal standard describes intended semantics; twenty years of use creates an actual user expectation; a design system default must choose, and neither authority resolves the other.
- **Against [[wiki/concepts/ux-research/web-accessibility-pour|POUR]] in a way the source misses.** The essay makes an accessibility argument for a change that benefits pointer users only. Under POUR, the real defect in the clickable-card case is that interactivity is not perceivable or operable without a mouse — and `cursor: pointer` leaves that defect exactly where it was while making it *feel* addressed. That is the most useful correction to record on this page.
- **Against [[wiki/concepts/infrastructure-dev/design-system-implementation|design system implementation]] and [[wiki/concepts/infrastructure-dev/component-catalog|component catalog]].** Tailwind v4 changed one preflight default and the consequence propagated to every downstream consumer, generating four issue threads in one library. A design-system default is a decision made once and inherited by people who never see it — the strongest available argument for documenting defaults with their rationale.
- **Supports [[wiki/concepts/ux-research/mental-models|mental models]] with an unusually clean case.** Twenty years of consistent exposure produced a mental model (`pointer` = clickable) that is now a fact about users regardless of what the specification says. Mental models are formed by exposure, not by documentation.
- **Adjacent to [[wiki/concepts/ux-research/cta-friction|CTA friction]] from the opposite direction.** CTA friction is about not impeding action; this is about the target being *findable* at all. Both fail on the minimal-UI patterns the essay names.
- **Convergent with [[wiki/sources/smashing-matching-ai-modality-user-intent|Yocco]] on one point:** the receiver's actual situation outranks the producer's model of correctness. Yocco argues it about modality defaults; this argues it about specification defaults. Neither cites the other and the pairing is this vault's.

## Open Questions

- Has anyone measured discoverability of clickable cards with and without `cursor: pointer`? It is a trivially runnable study and the debate is twenty years old without one.
- What is the touch and keyboard equivalent of the affordance the cursor is patching, and does adding the cursor reduce the pressure to build it? This is the question the source most needs and does not ask.
- Did the Tailwind v4 default change measurably affect anything downstream beyond issue volume?
- Does the learned convention hold for users who came to computing on touch first? The twenty-year argument assumes a desktop-formed mental model.

## Concepts Linked from This Source

- [[wiki/concepts/ux-research/perceived-affordance|Perceived Affordance]] *(new)*
- [[wiki/concepts/ux-research/web-accessibility-pour|Web Accessibility (POUR)]]
- [[wiki/concepts/ux-research/mental-models|Mental Models]]
- [[wiki/concepts/ux-research/cta-friction|CTA Friction]]
- [[wiki/concepts/infrastructure-dev/design-system-implementation|Design System Implementation]]
- [[wiki/concepts/infrastructure-dev/component-catalog|Component Catalog]]
- [[wiki/concepts/infrastructure-dev/modern-web-guidance|Modern Web Guidance]]
- [[wiki/concepts/infrastructure-dev/scaffold-design-system|Scaffold Design System]]

## LLM Use Guidance

- **Use the spec-versus-convention framing** whenever a standard and an established user expectation conflict. That is the transferable content; the cursor is the example.
- **Use the base-layer CSS as a starting point,** with two corrections: `[onclick]` misses JS-attached listeners, and the list should be reviewed against the actual component set.
- **Always attach the accessibility correction** when citing this source: `cursor: pointer` helps pointer users only, and the affordance problem it patches is worse for touch and keyboard users. The source does not say this and it should not be repeated without it.
- **Do not cite the accessibility benefit as researched.** It is reasoning.
- **Do not treat the GitHub issue count as a measurement** of user confusion — it is developer-reported and unquantified.

## Reliability Notes

- **Confidence 0.60.** The historical account is accurate and checkable (W3C cursor spec, Tailwind v4 preflight change, the four shadcn/ui issues, both named advocates' positions). The reasoning is clear and the author concedes the opposing case explicitly, which is the main reason the score is not lower.
- Held down by: no research of any kind, an uncited accessibility claim, a selector list with a real defect, a biased evidence sample, and a blind spot on non-pointer input that undermines the essay's own accessibility framing.
- **Use it for the framing and the debate history. Do not use it as evidence about user behaviour.**
- **Highest-value verification step:** any published study on discoverability of low-affordance click targets by input modality. It would settle both the cursor question and the more important one the essay leaves open.
