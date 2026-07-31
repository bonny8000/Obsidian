---
source_url: https://www.smashingmagazine.com/2026/07/matching-ai-modality-user-intent-designing-right-interface/
captured: 2026-07-31
title: "Matching AI Modality To User Intent: Designing The Right Interface"
authors: [Victor Yocco]
published: 2026-07-02
publisher: Smashing Magazine
language: en
format: practitioner framework article
---

# Matching AI Modality To User Intent — Smashing Magazine

**Author:** Victor Yocco, PhD — UX Researcher at ServiceNow; author of *Design for the Mind* (Manning, 2016) and the forthcoming *Designing Agentic AI Experiences* (Routledge).
**Published:** 2026-07-02 · **Captured:** 2026-07-31

AI-written extraction. No full-text reproduction; short quoted phrases only.

---

## Thesis

The design community defaults every AI capability into a chat interface because LLMs are trained on dialogue. That default is the error.

> "We've fallen into conversational tunnel vision, defaulting every AI capability into a chat-based interface simply because LLMs are trained on dialogue."

> "Great UX is about matching modality to users' context, intent, and cognitive load, so the interface adapts to the user, not the other way around."

**Definition given:** *"Modality is the way a person uses their senses to interact with a system: seeing, hearing, touching, speaking, or typing."*

## The two conversational burdens

**Input burden** — a blank text box creates a linguistic barrier and choice paralysis. *"A blank chat box creates a major problem for users who need to discover what a tool can actually do."* *"Composing a prompt is a creative act… For many professionals, this creates a linguistic barrier."*

**Output burden** — dense text imposes a cognitive tax through sequential processing. *"Text is a serial medium: your brain has to read one word after the next to extract meaning."* Against which: *"Visual methods allow parallel processing. You can view a chart and spot a pattern in under a second."*

## Taxonomy — 7 input modalities

Button/Tap (binary actions; "eliminates recall overhead") · Voice (hands/eyes-busy) · Natural Language Chat (exploratory queries; "offers users freedom") · Form/Wizard (structured multi-field data) · GUI — filters, sliders, drag-and-drop (complex parameter setting) · Multi-modal, image + text (visual input with description) · Gesture (hands-free spatial; operating rooms).

## Taxonomy — 6 output modalities

Push Notification/Alert (time-sensitive ambient awareness) · Audio Summary (hands/eyes-busy) · Short Text Summary (focused queries) · Visual Dashboard (high-density comparative analysis) · Interactive Canvas (generative/iterative creative work) · Inline Confirmation (guided flows with feedback).

## Tool 1 — the Task Audit

Four areas of focus:

1. **Input constraints** — are the hands physically available?
2. **Output constraints** — is viewing a screen safe/practical?
3. **Social constraints** — is audible interaction appropriate here?
4. **Cognitive load** — how much mental effort is already spent on the primary task?

Research methods prescribed: contextual inquiry and observation, focused interviews, collaborative workshops. **Lightweight version:** 2 hours field observation + 3–5 interviews + a 90-minute workshop, run before the design sprint.

## Tool 2 — the Input/Output Alignment Matrix

| User intent | Input | Output |
| --- | --- | --- |
| Quick status check | Voice or single-tap | Audio or push notification |
| Specific detail query | Natural language chat | Short text summary |
| Complex analysis | GUI (filters, sliders) | Visual dashboard |
| Creative generation | Multi-modal (image + text) | Interactive canvas |
| Monitoring / alert | Passive background system | Push notification or audio alert |
| Guided task completion | Structured form or step-by-step wizard | Inline confirmation + progress indicator |

## Case study — field technicians at a national utility provider

**Problem:** technicians servicing high-voltage grids faced dangerous interface misalignment — heavy protective gloves defeated touchscreen precision, screen glare at height obscured text, and reading complex reports while monitoring live equipment created unsafe cognitive load.

**Research:** contextual inquiry observed technicians in bucket trucks wearing thick gloves, confirming hands-busy and eyes-busy constraints and sunlight glare; focused interviews across multiple sites confirmed the constraints were systemic rather than isolated.

**Solution:** voice input (hands-free on site); audio summary output (bypasses glare, preserves situational awareness); **adaptive handoff** — on return to the truck, automatic transition to a 15-inch vehicle-mounted visual dashboard for historical trends and grid maps, because a 10-inch field tablet lacks the real estate for complex schematics and the larger display enables parallel processing.

**Reported outcome:** *"reduced diagnostic time by twenty percent and increased daily tool adoption among field crews."*

## Decision rules given

Choose modality from the user's physical state and environment, not from the AI system's capabilities. High cognitive load → visual dashboards (parallel processing beats sequential reading). Time-sensitive → glanceable low-density output, not detailed summaries. Hands-busy → voice in, audio or push out. Eyes-busy → audio; remove screen-reading. Ambiguous/exploratory → natural language chat is genuinely appropriate, because the user needs freedom to express an unclear need. Structured data entry → form or wizard. Irreversible or high-stakes → inline confirmation, to reduce verification anxiety.

**Accessibility:** *"Modality choices should multiply pathways to information"* — a visual dashboard requires a screen-reader-optimized audio alternative.

Closing framings: *"The physical and social realities of those spaces are not edge cases. They are the design brief."* · *"Building a chatbot is fast and familiar… Building an interface that feels like a natural extension of how someone already works is harder, and it is the work that matters."*

**Downloadable asset:** "Modality Task Audit Field Template" (PDF), in three parts — Physical Reality Check, Cognitive Baseline, Handoff Map.

## Limitations and caveats (as observed in the text)

- **No academic citations.** Method names (contextual inquiry) appear, but no peer-reviewed research is cited for any claim, including the cognitive claims about serial vs. parallel processing.
- **The 20% figure is unsupported.** Single implementation, one client, no baseline definition, no sample size, no measurement method, no time window, no independent verification. "Increased adoption" is not quantified at all.
- **No limitations section.** The article asserts its frameworks as sound and never discusses boundary conditions.
- **Generalizability untested** — the only case is high-voltage field work, an extreme physical-constraint environment. Office, consumer, and hybrid contexts are not demonstrated.
- **No cost/benefit treatment.** Multi-modal implementation cost versus single-modality simplicity is never addressed, nor is prioritization when resources are limited.
- **Accessibility is asserted, then under-served** — the piece mandates multiplying pathways but does not address users whose disability conflicts with the environmental constraint (a Deaf technician in a hands-busy role; a blind technician where audio is the only channel).
- **Unaddressed:** how to detect ambiguous or mid-task-shifting intent; how adaptive handoff is triggered technically; whether chat is ever right in hands-busy contexts.
- The taxonomies are the author's own construction, presented without validation or inter-rater testing; the forthcoming book gives the author an interest in the framework's adoption.
