---
type: source
status: active
created: 2026-08-04
updated: 2026-08-04
tags: [voice-interface, system-state, agent-transparency, latency, color-accessibility, automotive-ux, peripheral-vision, agent-experience]
source_path: raw/web/paxton-yao-voice-ai-thinking-state-2026-08-04.md
source_url: https://www.linkedin.com/pulse/voice-ai-gave-designers-new-state-show-thinking-paxton-yao-ugutc
authors: [Paxton Yao]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.48
---

# Yao (2026): Voice AI Gave Designers a New State to Show — Thinking

## Citation

Paxton Yao, "Voice AI Gave Designers a New State to Show: Thinking," **LinkedIn Pulse**, 2026-08-01.

**Source type:** Short practitioner design note. Comparative analysis of two shipped products. No research, no measurement.
**Raw capture:** [[raw/web/paxton-yao-voice-ai-thinking-state-2026-08-04|paxton-yao-voice-ai-thinking-state-2026-08-04]]
**Coverage note:** `coverage: substantial` — the argument, both state models, the colour reasoning, and the author's own stated limitation were captured. The piece is brief and the capture is close to complete; marked `substantial` rather than `full` because the LinkedIn rendering may omit images the argument refers to.

## Summary

A small source with one genuinely new observation. In voice interaction, *"silence means several different things"* — not heard, listening, processing, about to speak — so voice needs state feedback that text does not. LLM inference then added a state with no prior equivalent:

> "gap is a new state that didn't exist before"

Before LLMs, a voice assistant either understood you or did not; the wait was short enough not to need a name. Inference latency created a period that is neither listening nor answering, and it has to be shown.

Yao's contribution is not "show a spinner." It is that **the right number of states depends on where the interface is read.** He compares two shipped products:

| System | States | Encoding |
|---|---|---|
| **Claude voice mode** (desktop) | **2** — speaking, listening | Orange = speaking, Blue = listening |
| **NOMI** (NIO's in-car assistant) | **5** — idle, countdown, listening, thinking, speaking | Colour plus intensity gradient |

Neither is wrong. A desktop app has the user's direct attention and can afford minimal signalling. An in-car assistant is read in **peripheral vision while driving**, where ambiguous state *"pulls the driver's attention off the road"* — a driver who cannot tell whether the assistant is listening will look over to check. More granular state becomes a safety feature.

The author then undercuts his own case, which is the most creditable thing in the piece:

> "Five states is more information than two, but I haven't seen data on whether drivers distinguish all five in practice or effectively collapse them into three."

## Key Claims

- **Silence is ambiguous in voice in a way that a blank screen is not in text.** The user cannot distinguish "did not hear you," "listening," "thinking," and "about to speak." This is the source's foundational observation and it is correct on inspection.

- **The thinking state is new.** LLM inference created a durable, user-visible processing period that pre-LLM voice assistants did not have to represent.

- **State count should follow viewing context, not system complexity.** The desktop/peripheral distinction is the actual design rule the piece contributes, and it is more useful than either state model.

- **Three encoding channels, doing different jobs:** **hue** distinguishes state *type*; **saturation/brightness** indicates *degree of engagement* within a state; **viewing context** determines how many states are legible at all.

- **Orange and blue are chosen for maximum separation** — they *"sit opposite each other on the color wheel"* — and for robustness: the pair is *"distinguishable across nearly all forms of color vision deficiency."* Red-green deficiency is cited at *roughly 8% of men*, with deuteranopia named.

- **Cyan-purple is becoming an AI convention** — *"becoming a pattern … that didn't exist five years ago."* Offered as an observation about emerging convention, not as a recommendation.

- **In a driving context, state granularity is a safety argument** rather than an aesthetic one, because the cost of ambiguity is a glance away from the road.

## Useful Examples

**The two-versus-five comparison** is the reusable artifact, and its value is the pairing rather than either model. Same underlying problem, same era, two shipped answers differing by 2.5×, each defensible from its viewing context.

**The five NOMI states** — idle, countdown, listening, thinking, speaking. Note that **countdown** is not a system-processing state at all: it is a window in which the user may still speak. That is a category the desktop model has no need for, and it is where the extra granularity comes from.

**The colour-vision reasoning** is a good worked example of accessibility applied at the *encoding* stage rather than as a retrofit: the palette is chosen so that the state distinction survives deuteranopia, instead of adding a text label afterwards.

**Saturation as intensity within a state** — the part most designers would miss. Hue answers *which state*; saturation answers *how much*, which is what lets five states stay readable at a glance.

## Constraints / Caveats

- **No research of any kind.** No user testing, no measurement, no A/B result, no observational study. Two products, examined by a designer.
- **The ~8% colour-vision figure is uncited** (it is a broadly accepted figure, and this source is not a warrant for it).
- **The safety argument is asserted, not demonstrated.** That ambiguous state causes a glance off the road is plausible and untested here — and automotive HMI is a field with a real measurement literature that goes uncited.
- **The author's own limitation is the central one:** nobody knows whether five states are perceived as five. If drivers collapse them to three, two of NOMI's states cost design effort and screen presence for nothing.
- **No account of non-visual state signalling.** In a car, audio and haptics are available and are arguably better peripheral channels than colour; the piece is entirely visual. This also leaves blind and low-vision users unaddressed while making an accessibility argument about colour.
- **Colour alone as the state channel** is a redundancy failure by the vault's own [[wiki/concepts/ux-research/web-accessibility-pour|POUR]] material, even with a colourblind-safe palette — the argument shows awareness of colour deficiency and not of the principle that state should not rest on one channel.
- **Sample of two, both chosen after the fact** to illustrate a distinction the author had already drawn.
- **LinkedIn Pulse:** self-published, no editorial review, and the platform's own affordances mean the piece is partly professional positioning.

## Design Implications

- **Enumerate your states before designing the indicator.** The useful question is not "what does thinking look like" but "how many distinguishable states does this system actually have, and which does the user need?"
- **Set state count from viewing distance and attention budget.** Foveal, glanceable, and peripheral are three different design problems, and this is the source's genuine contribution.
- **Separate the encoding channels deliberately:** hue for state type, intensity for degree. Collapsing both into one channel is what makes multi-state indicators unreadable.
- **Choose the palette for the worst-case viewer at the point of encoding,** not by adding a label later.
- **Do not let state rest on colour alone.** Add a second channel — shape, motion, audio, haptic — especially in a safety context. The source does not say this and should.
- **Name the states that belong to the user, not the system.** NOMI's *countdown* is a user-turn state; those are the ones a system-centric state model omits.

## Tensions

- **Converges with [[wiki/sources/toyota-voice-interaction-humanoid-robots|Toyota FRC (2026)]] on the same problem with the opposite instrument.** Both address the second that LLM inference inserted into voice. Toyota fills it with speech — fillers, clarifications, speculative generation. Yao fills it with colour — a visible state. Published a day apart, from automotive-adjacent and robotics contexts, neither aware of the other. Toyota's approach *shortens or covers* the gap; Yao's *labels* it. They are complementary and no source in this vault does both. See [[wiki/analyses/2026-08-04-the-response-gap|the memo]] and [[wiki/comparisons/filling-the-response-gap|the decision table]].
- **Narrower than [[wiki/concepts/agent-experience/agent-transparency|agent transparency]] and importantly so.** Transparency is about making reasoning and provenance legible. This is about making *system state* legible — a lower, cheaper layer that has to work before any transparency claim is meaningful. A user who cannot tell whether the agent is listening has no use for a reasoning trace. The vault's transparency material does not currently distinguish the two.
- **Extends [[wiki/concepts/agent-experience/modality-intent-matching|modality–intent matching]] with the same correction Toyota supplies.** Yocco maps intent to modality on ergonomic grounds; both new sources show voice carries a latency constraint that reshapes the interface, which the matrix does not model.
- **Against its own accessibility argument, per [[wiki/concepts/ux-research/web-accessibility-pour|POUR]].** Choosing a colourblind-safe palette is good; making colour the sole state channel is the failure the accessibility principle exists to prevent. The piece does the first and not the second, and the safety framing makes the omission worse rather than better.
- **Relevant to [[wiki/concepts/agent-experience/initiative-and-interruption|initiative and interruption]] in a way the source does not develop.** The *countdown* state is a turn-taking signal: it tells the user the floor is still theirs. Turn-taking is the actual subject underneath the state model, and neither this source nor the vault's initiative material connects them.

## Open Questions

- Can users distinguish five states, or do they collapse to three? The author's question, and it is a straightforward discrimination study.
- Does an accurate "thinking" indicator change waiting behaviour — fewer repeated utterances, fewer abandoned turns — or only perceived politeness?
- Is colour the right peripheral channel in a car at all, given audio and haptics are free and eyes-free?
- Is the emerging cyan-purple AI convention doing useful work, or is it decorative signalling of AI-ness?
- What is the interaction between labelling the gap (Yao) and covering it (Toyota)? Plausibly they conflict: a filler that performs thought while an indicator honestly reports thought is two answers to one question.

## Concepts Linked from This Source

- [[wiki/concepts/agent-experience/system-state-signaling|System State Signaling]] *(new)*
- [[wiki/concepts/agent-experience/response-latency-masking|Response Latency Masking]] *(new)*
- [[wiki/concepts/agent-experience/agent-transparency|Agent Transparency]]
- [[wiki/concepts/agent-experience/initiative-and-interruption|Initiative and Interruption]]
- [[wiki/concepts/agent-experience/modality-intent-matching|Modality–Intent Matching]]
- [[wiki/concepts/ux-research/web-accessibility-pour|Web Accessibility (POUR)]]
- [[wiki/concepts/robotics-spatial/input-modality|Input Modality]]
- [[wiki/concepts/robotics-spatial/spatial-information-display|Spatial Information Display]]

## LLM Use Guidance

- **Use the state-enumeration move** — list the distinguishable states, then decide how many to expose — for any waiting or processing interface, voice or not.
- **Use the viewing-context rule** (foveal / glanceable / peripheral sets the state count) as a design constraint. It is the source's real contribution and it transfers cleanly.
- **Use the hue/intensity channel split** when more than two states must be readable at a glance.
- **Do not cite the safety claim as established.** It is reasoning, and automotive HMI has a real literature this piece does not touch.
- **Do not treat five states as validated.** The author says outright that nobody knows whether they are perceived.
- **Do not reproduce colour-only state signalling** from this source without adding a second channel.
- Pair with [[wiki/sources/toyota-voice-interaction-humanoid-robots|Toyota]] whenever designing for the response gap — labelling it and covering it are different moves and the two sources only cover one each.

## Reliability Notes

- **Confidence 0.48.** Low, and the number reflects evidence rather than usefulness: no research, an uncited statistic, an asserted safety claim in a domain with a measurement literature, a post-hoc sample of two, and self-publication with no review.
- What keeps it above the floor: the founding observation about ambiguous silence is checkable and correct; the viewing-context rule is a real and transferable design constraint; and the author explicitly flags the one thing that would falsify his own recommendation, which is rarer than it should be.
- **Use it for the framing and the design rule. Do not use it for any claim about what users perceive.**
- **Highest-value verification step:** an automotive-HMI study on glance behaviour and assistant state ambiguity. That literature very likely exists and would either ground or deflate the safety argument this source rests on.
