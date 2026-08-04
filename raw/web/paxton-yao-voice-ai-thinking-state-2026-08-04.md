---
source_url: https://www.linkedin.com/pulse/voice-ai-gave-designers-new-state-show-thinking-paxton-yao-ugutc
captured: 2026-08-04
title: "Voice AI Gave Designers a New State to Show: Thinking"
authors: [Paxton Yao]
published: 2026-08-01
publisher: LinkedIn (Pulse article)
language: en
format: practitioner design note
---

# Voice AI Gave Designers a New State to Show: Thinking — Paxton Yao

**Author:** Paxton Yao. **Published:** 2026-08-01 on LinkedIn Pulse · **Captured:** 2026-08-04

AI-written extraction. No full-text reproduction; short quoted phrases only.

---

## Thesis

Voice interfaces need visible system-state feedback that text interfaces do not, because in voice *"silence means several different things"* — the system may not have heard, may be listening, may be processing, or may be about to speak. LLM inference then added a state that had no prior equivalent:

> "gap is a new state that didn't exist before"

The design problem is therefore not "show a loading spinner" but **which states exist, and how many a user can actually read in the viewing context they are in.**

## The two state models compared

| System | States | Encoding |
| --- | --- | --- |
| **Claude voice mode** (desktop) | **2** — speaking, listening | Orange = speaking, Blue = listening |
| **NOMI** (NIO in-car assistant) | **5** — idle, countdown, listening, thinking, speaking | Colour plus an intensity gradient |

The argument is that neither is wrong: the state count should follow the viewing context. A desktop app has the user's foveal attention and can afford minimal signalling. An in-car assistant is read in **peripheral vision** while the user is driving, so state must be distinguishable without a direct look.

## Design variables named

- **Hue** — distinguishes the *type* of state.
- **Saturation / brightness** — indicates *degree of engagement* within a state.
- **Viewing context** — desktop foveal vs. peripheral, which sets how many states are legible at all.

## Colour reasoning

- Orange and blue are chosen because they *"sit opposite each other on the color wheel"* — maximum separation.
- Accessibility justification: the pair is *"distinguishable across nearly all forms of color vision deficiency"*. Red-green deficiency is cited as affecting *roughly 8% of men*; deuteranope vision is named specifically.
- A separate observation: cyan-purple is *"becoming a pattern … that didn't exist five years ago"* as an emerging convention for AI-ness.

## Safety argument for the in-car case

Ambiguous state *"pulls the driver's attention off the road"* — a driver who cannot tell whether the assistant is listening will look at the screen to check. In that context more granular state signalling is a safety feature, not decoration.

## Products and companies named

- Claude voice mode (Anthropic)
- NOMI — NIO's in-car assistant
- NIO, Jiyue — Chinese EV makers referenced as the context for in-car assistant design

## Evidence

- Colour-vision-deficiency prevalence (~8% of men) — stated without citation.
- General design principles about viewing conditions and safety — no formal studies cited.
- **No user research, no measurement, no A/B result.** The piece is an argued design analysis of two shipped products.

## The author's own stated limitation

> "Five states is more information than two, but I haven't seen data on whether drivers distinguish all five in practice or effectively collapse them into three."

The author explicitly suggests real user testing is needed to establish whether the middle states change behaviour at all — that is, whether the extra granularity is legible or merely present.
