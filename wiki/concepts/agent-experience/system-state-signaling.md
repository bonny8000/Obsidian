---
type: concept
status: active
created: 2026-08-04
updated: 2026-08-04
tags: [concept, agent-experience, system-state, voice-interface, turn-taking, peripheral-vision, color-accessibility, automotive-ux]
sources: [paxton-yao-voice-ai-thinking-state, toyota-voice-interaction-humanoid-robots]
confidence: 0.50
---

# System State Signaling

> [!abstract] Summary
> Making an agent's **current operating state** legible — listening, thinking, speaking, idle, or waiting for the user's turn — at a granularity the user can actually read in their viewing context.
>
> Distinct from, and beneath, [[wiki/concepts/agent-experience/agent-transparency|agent transparency]]: transparency explains *what the agent reasoned*; state signalling says *what it is doing right now*. A user who cannot tell whether the agent is listening has no use for a reasoning trace.

## Why It Matters

In voice, silence is overloaded. Per [[wiki/sources/paxton-yao-voice-ai-thinking-state|Yao (2026)]], *"silence means several different things"* — not heard, listening, processing, about to speak. Text interfaces do not have this problem: a blank screen is unambiguous.

LLM inference then added a state with no prior equivalent:

> "gap is a new state that didn't exist before"

Before LLMs, a voice assistant either understood you or did not, and the wait was too short to name. Inference latency created a period that is neither listening nor answering — and it has to be represented.

## The Design Rule

**State count follows viewing context, not system complexity.** This is the concept's most transferable content.

| System | States | Encoding | Why |
|---|---|---|---|
| **Claude voice mode** (desktop) | **2** — speaking, listening | Orange / blue | Foveal attention; minimal signalling suffices |
| **NOMI** (NIO in-car) | **5** — idle, countdown, listening, thinking, speaking | Colour + intensity gradient | Read in **peripheral vision while driving** |

Neither is wrong. A driver who cannot tell whether the assistant is listening will look at the screen to check, and ambiguous state *"pulls the driver's attention off the road"* — which makes granularity a safety argument rather than an aesthetic one.

**Three encoding channels, doing different jobs:**

- **Hue** — distinguishes state *type*
- **Saturation / brightness** — indicates *degree of engagement* within a state
- **Viewing context** — determines how many states are legible at all

Collapsing type and degree into one channel is what makes multi-state indicators unreadable.

## Key Claims

- **Enumerate states before designing the indicator.** The useful question is not "what does thinking look like" but "how many distinguishable states does this system have, and which does the user need?"

- **Name the states that belong to the user, not only the system.** NOMI's **countdown** is not system processing at all — it is a window in which the user may still speak. That is where the extra granularity comes from, and it is the category a system-centric state model omits. Turn-taking, not processing, is the real subject.

- **Choose the palette for the worst-case viewer at the encoding stage.** Orange and blue *"sit opposite each other on the color wheel"* and are *"distinguishable across nearly all forms of color vision deficiency"* — accessibility designed in rather than retrofitted with a label. (Red-green deficiency cited at roughly 8% of men; deuteranopia named.)

- **Cyan-purple is an emerging AI convention** — *"becoming a pattern … that didn't exist five years ago."* An observation about convention formation, not a recommendation.

- **Labelling the gap and covering it are different strategies.** [[wiki/concepts/agent-experience/response-latency-masking|Response latency masking]] shortens or covers the wait; this concept makes it honest and readable. No source in this vault does both.

## ⚖️ Conflicts & Caveats

> [!warning] Nobody knows whether five states are perceived as five
> Yao says so himself: *"I haven't seen data on whether drivers distinguish all five in practice or effectively collapse them into three."* If they collapse, two of NOMI's states cost design effort and screen presence for nothing. **This is the concept's central unknown and it is unresolved.**

> [!warning] Colour alone is a redundancy failure
> Choosing a colourblind-safe palette is good; making colour the *sole* state channel is exactly what [[wiki/concepts/ux-research/web-accessibility-pour|POUR]] exists to prevent. Yao demonstrates awareness of colour deficiency and not of the redundancy principle — and the safety framing makes the omission worse, not better. **Add a second channel: shape, motion, audio, or haptic.**

> [!warning] The visual-only framing skips the better in-car channels
> In a car, audio and haptics are available, eyes-free, and arguably superior for peripheral state. The source is entirely visual, which also leaves blind and low-vision users unaddressed inside an accessibility argument.

> [!warning] The safety claim is asserted, not demonstrated
> That ambiguous state causes a glance off the road is plausible and untested here — in a field (automotive HMI) that has a real measurement literature the source does not touch.

> [!warning] Evidence base is two products and no research
> Sample of two, chosen after the distinction was drawn, from a self-published post with no review.

## Practical Guidance

1. **List the distinguishable states first**, including the user's turn states, then decide how many to expose.
2. **Set the count from attention budget** — foveal, glanceable, and peripheral are three different problems.
3. **Separate hue (type) from intensity (degree)** when more than two states must read at a glance.
4. **Never let state rest on colour alone**, especially in a safety context.
5. **Make the "thinking" state honest.** If you are also masking latency with fillers, decide which signal is authoritative — otherwise the two contradict each other.
6. **Test discrimination, not preference.** The question is whether users can tell the states apart, and it is a straightforward study nobody has run.

## 🔗 Related Concepts

- [[wiki/concepts/agent-experience/response-latency-masking|Response Latency Masking]] — the complementary strategy; covering versus labelling.
- [[wiki/concepts/agent-experience/agent-transparency|Agent Transparency]] — the layer above; state legibility is its precondition.
- [[wiki/concepts/agent-experience/initiative-and-interruption|Initiative and Interruption]] — turn-taking, which is what the *countdown* state actually signals.
- [[wiki/concepts/agent-experience/modality-intent-matching|Modality–Intent Matching]]
- [[wiki/concepts/agent-experience/mental-model-onboarding|Mental Model Onboarding]] — state signals are how a user learns what the agent does.
- [[wiki/concepts/ux-research/web-accessibility-pour|Web Accessibility (POUR)]] — the principle this concept's source violates.
- [[wiki/concepts/robotics-spatial/spatial-information-display|Spatial Information Display]] — peripheral legibility, from the spatial side.
- [[wiki/concepts/robotics-spatial/input-modality|Input Modality]]
- [[wiki/concepts/ux-research/cognitive-load|Cognitive Load]] — what checking an ambiguous state costs.

## 📚 Sources

- [[wiki/sources/paxton-yao-voice-ai-thinking-state|Yao (2026): Voice AI Gave Designers a New State to Show]] — primary source. The ambiguous-silence observation, the two-vs-five comparison, the viewing-context rule, and the encoding channels.
- [[wiki/sources/toyota-voice-interaction-humanoid-robots|Toyota FRC (2026): Voice Interaction with Humanoid Robots]] — the same gap addressed with speech instead of colour; the counterpoint case.

## ❓ Open Questions

- Can users distinguish five states, or do they collapse to three? Yao's own question and a simple discrimination study.
- Does an accurate thinking indicator change waiting behaviour — fewer repeated utterances, fewer abandoned turns — or only perceived politeness?
- Is colour the right peripheral channel in a car at all, given audio and haptics are free and eyes-free?
- Do honest state signals and latency-masking fillers compose, or does the filler make the indicator read as evasion?
- Is the emerging cyan-purple AI convention doing work, or signalling AI-ness decoratively?
