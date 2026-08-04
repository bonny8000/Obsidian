---
type: concept
status: active
created: 2026-07-31
updated: 2026-08-04
tags: [concept, agent-experience, modality, multimodal, conversational-ui, cognitive-load, context-of-use, accessibility, task-audit, latency]
sources: [smashing-matching-ai-modality-user-intent, toyota-voice-interaction-humanoid-robots, paxton-yao-voice-ai-thinking-state]
confidence: 0.6
---

# Modality–Intent Matching

> [!abstract] Summary
> Choosing an AI feature's input and output channels from the **user's physical, social, and cognitive situation** rather than from the model's natural output shape. The specific target is the chat default: text-in/text-out is treated as the container for every AI capability because LLMs are trained on dialogue, which is a fact about the model, not about the user.

> [!important] Why it Matters
> *"We've fallen into conversational tunnel vision, defaulting every AI capability into a chat-based interface simply because LLMs are trained on dialogue."* The chat default imposes two separable costs: a **blank input box** is a linguistic barrier and a discovery problem for anyone who cannot yet name what they want, and **prose output** is serial where much comprehension wants parallel. Neither cost is visible if chat is never treated as a choice.

## 📝 Key Claims

- **Four constraint questions decide most of it** — the Task Audit: are the **hands** available? Is looking at a **screen** safe and practical? Is **audible** interaction socially appropriate here? How much **cognitive load** is the primary task already taking?

- **Chat is right for ambiguous, exploratory intent** and wrong as a default. Where the user cannot yet name the need, natural language is correct precisely because it *"offers users freedom."* The argument is against the default, not the modality.

- **The intent → modality mapping:**

| User intent | Input | Output |
|---|---|---|
| Quick status check | Voice or single-tap | Audio or push notification |
| Specific detail query | Natural language chat | Short text summary |
| Complex analysis | GUI (filters, sliders) | Visual dashboard |
| Creative generation | Multi-modal (image + text) | Interactive canvas |
| Monitoring / alert | Passive background system | Push notification or audio alert |
| Guided task completion | Structured form or wizard | Inline confirmation + progress |

- **The handoff is a design object.** Users change context mid-task, and the transition is where the design fails. The one worked case switches from voice/audio in the field to a 15-inch mounted dashboard on return to the vehicle, because the larger surface enables parallel reading that a 10-inch tablet cannot.

- **Environmental constraints are the brief.** *"The physical and social realities of those spaces are not edge cases. They are the design brief."*

- **Accessibility multiplies pathways rather than substituting them** — a visual dashboard obliges a screen-reader-optimised audio alternative.

- **The audit can be cheap:** 2 hours field observation + 3–5 interviews + a 90-minute workshop, before the design sprint. Making it schedulable is most of what makes it happen.

## The Missing Fifth Question: Latency

> [!important] Added 2026-08-04 — modality choice constrains the architecture, not only the interface
> Two sources ingested 2026-08-04 supply a constraint the four Task Audit questions omit. Voice imposes a **~1 second budget to first output** ([[wiki/sources/toyota-voice-interaction-humanoid-robots|Toyota FRC, 2026]]), and *every* technique that improves answer quality — RAG, web search, multi-pass refinement — breaks it: *"there is a trade-off where utilizing these methods increases the delay until the final response."*
>
> So choosing voice is choosing a stack: shallower retrieval, or speculative execution, or an accepted quality ceiling. Toyota's honest baseline is that a dedicated team running three mitigation techniques still *"cannot get them to consistently respond within one second."*
>
> **The fifth Task Audit question: what latency does this modality tolerate, and can the answer be produced inside it?**
>
> The corollary from [[wiki/sources/paxton-yao-voice-ai-thinking-state|Yao (2026)]]: voice also needs *state* signalling that text does not, because *"silence means several different things."* See [[wiki/concepts/agent-experience/response-latency-masking|Response Latency Masking]], [[wiki/concepts/agent-experience/system-state-signaling|System State Signaling]], and [[wiki/analyses/2026-08-04-the-response-gap|the 2026-08-04 memo]] — which argues the gap is better framed as a turn-taking problem than as a loading state.

## 🔗 Related Concepts

- [[wiki/concepts/agent-experience/natively-adaptive-interfaces|Natively Adaptive Interfaces]] — **a competing bet.** Google's NAI puts adaptation inside the agent, inferred per interaction; this puts it in design-time fieldwork. Runtime inference vs. prior research; neither source acknowledges the other.
- [[wiki/concepts/ux-research/cognitive-load|Cognitive Load]]
- [[wiki/concepts/agent-experience/delegation-spectrum|Delegation Spectrum]] — the missing dimension here; see caveats.
- [[wiki/concepts/agent-experience/proactivity-design|Proactivity Design]]
- [[wiki/concepts/agent-experience/initiative-and-interruption|Initiative and Interruption]]
- [[wiki/concepts/ux-research/minimally-technical-reporting|Minimally Technical Reporting]] — the same instinct in research communication: shape the artifact to the receiver's capacity, not the producer's convenience.
- [[wiki/concepts/agent-experience/response-latency-masking|Response Latency Masking]] — the latency constraint this matrix omits.
- [[wiki/concepts/agent-experience/system-state-signaling|System State Signaling]] — what voice needs and text does not.
- [[wiki/concepts/ux-research/perceived-affordance|Perceived Affordance]] — the same receiver-over-producer principle, applied to specification defaults.
- [[wiki/methods/field-studies|Field Studies]]

## ⚖️ Conflicts & Caveats

- **Modality is treated as ergonomics, never as trust.** [[wiki/concepts/agent-experience/delegation-spectrum|Delegation spectrum]] would predict that channel choice changes how much a user *can* verify — an audio summary removes exactly the comparison a dashboard affords, and [[wiki/analyses/2026-07-30-trust-measurement-and-monetization|the trust memo]] identifies removed comparison as the mechanism by which disclosure stops working. **Applying this matrix to a recommendation surface, rather than a status surface, without accounting for that is a real risk.**
- **The evidence base is thin.** One case, in an extreme physical-constraint environment where the answer is nearly overdetermined. The headline "20% reduction in diagnostic time" has no methodology, sample, baseline, or verification and **should not be repeated as evidence**.
- **The cognitive claims are uncited.** Serial vs. parallel processing is stated as established fact. It is broadly consistent with mainstream cognitive psychology, but this source is not the warrant for it.
- **The taxonomies are self-constructed and unvalidated** — plausible, but nothing establishes that six intents are the right cut.
- **Accessibility is mandated then under-served**: the case where a user's disability conflicts with the environmental constraint (a Deaf technician in a hands-busy role) is not addressed.

## 📚 Sources

- [[wiki/sources/smashing-matching-ai-modality-user-intent|Yocco (2026): Matching AI Modality to User Intent]] — the matrix and the four constraint questions.
- [[wiki/sources/toyota-voice-interaction-humanoid-robots|Toyota FRC (2026): Voice Interaction with Humanoid Robots]] — the latency budget voice imposes, and the quality/speed trade.
- [[wiki/sources/paxton-yao-voice-ai-thinking-state|Yao (2026): Voice AI Gave Designers a New State to Show]] — the state-signalling requirement voice adds.

## ❓ Open Questions

- How is intent detected at runtime? The matrix is indexed by intent, and the source's own list of unaddressed problems begins with ambiguous intent.
- Does modality change verification behaviour — do users check an audio summary less than a dashboard? This is the question that would connect the framework to the trust cluster, and nobody has asked it.
- Does the mapping hold outside physically constrained work?
- What triggers an adaptive handoff, and how does the system avoid switching at the wrong moment?
- Should the matrix carry a latency column? Voice and audio rows are the ones where the architecture is constrained, and the matrix currently reads as though modality were free.
