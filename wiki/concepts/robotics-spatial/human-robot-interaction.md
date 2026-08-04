---
type: concept
status: active
created: 2026-05-18
updated: 2026-08-04
tags: [hri, robotics, ux]
sources:
  - sources/naverlabs-blog-34515
  - sources/naverlabs-blog-10034251
  - sources/lennys-podcast-ai-hardware-boom-caitlin-kalinowski
  - sources/toyota-voice-interaction-humanoid-robots
confidence: 0.82
---

# Human-Robot Interaction

## Summary

Human-Robot Interaction (HRI) studies how people and robots perceive, affect, coordinate with, and accept each other in shared environments.

## Why It Matters

Physical AI succeeds only when robot behavior fits human expectations, safety constraints, spatial norms, and social comfort. The elevator boarding source shows that "can move" and "should move" are different questions.

## Key Claims

- Robot behavior must consider social context, not only geometric feasibility.
- Shared building infrastructure creates recurring HRI situations such as elevators, corridors, and delivery zones.
- Human acceptance can be modeled and tested through survey and immersive simulation methods.
- Robots should feel non-threatening and responsive when operating near people.

## Related Concepts

- [[concepts/robotics-spatial/robot-boarding-area|Robot Boarding Area]]
- [[concepts/robotics-spatial/socially-aware-navigation|Socially Aware Navigation]]
- [[concepts/robotics-spatial/physical-ai|Physical AI]]
- [[concepts/robotics-spatial/spatial-ai|Spatial AI]]
- [[concepts/robotics-spatial/robot-safety|Robot Safety]]

## Sources

- [[sources/naverlabs-blog-10034251|NAVER LABS: Robot Elevator Boarding Acceptance]]
- [[sources/naverlabs-blog-34515|NAVER LABS: AI and Space]]
- [[sources/lennys-podcast-ai-hardware-boom-caitlin-kalinowski|Lenny's Podcast: Beginning of the AI Hardware Boom]]

## Open Questions

- [Answered → [[queries/2026-05-27-human-robot-efficiency-vs-comfort|Query Page]]] What interaction rules should robots follow when their efficiency conflicts with human comfort?
- **What is the scope of a person's consent to their own LLM replica**, and who reviews what it says? Toyota builds robots modelled on named living people and does not address this.
- **After two years of public deployment taking open questions from strangers, what has it got wrong?** The most valuable unpublished part of the Toyota work.

## What an LLM-Era HRI Stack Actually Looks Like

> [!important] Added 2026-08-04 — the vault's most concrete implementation account
> [[wiki/sources/toyota-voice-interaction-humanoid-robots|Toyota's Frontier Research Center (2026)]] describes two 90 cm mascot robots modelled on named living people — **Tommy** (a *Toyota Times* announcer) and **AI Morizo** (Chairman Akio Toyoda) — in more mechanical detail than corporate publications usually allow. Three named challenges, and each maps to an HRI problem this concept has treated abstractly.
>
> **1. Person-likeness carried in three channels** — physical appearance, a speech-synthesis model trained on the real person's recorded voice, and *reasoning process*. Toyota explicitly rejected training on past remarks: *"we limited the input knowledge to basic profiles, placing emphasis on extracting the underlying philosophies and thought processes."* The stated reason is coverage — memorised utterances cannot answer a novel question in character.
>
> **2. The latency budget is the binding constraint.** ~1 second to first output is the stated target, and every quality technique breaks it. Three mitigations: parallel speculative execution with discard; a priority ladder (main response > clarification > filler); and "think while listening," generating before the user finishes and adopting the earliest candidate that survives a discrepancy check. **Toyota reports it still cannot consistently hit one second** — the honest baseline for embodied conversation.
>
> **3. Non-verbal behaviour is a two-stage vision pipeline** — an ML model picks *"the person the robot should pay attention to now,"* then a **high-speed VLM** reads that person's appearance and actions; fast LLMs then select movement and expression at high frequency. This is what "embodied agents communicate multi-modally" means in an implementation.
>
> **The candid weak link:** expression is **selected from a few fixed patterns, not generated.** Toyota says the vocabulary is *"still insufficient"* and that attention targeting remains unsolved. That is where embodied expressiveness actually stands.
>
> **Evidence warning:** no quantitative results of any kind. No latency figures, no ablation, no user data. The only evaluative statement is Akio Toyoda's *"the answers sound exactly like me"* — one subject rating his own replica. Cite this source for architecture, never for outcomes.

## Additional Sources

- [[wiki/sources/toyota-voice-interaction-humanoid-robots|Toyota FRC (2026): Voice Interaction with Humanoid Robots]] — the full stack, the three challenges, and the unmet latency target.

## Additional Related Concepts

- [[wiki/concepts/agent-experience/response-latency-masking|Response Latency Masking]] — the latency techniques, generalised beyond robotics.
- [[wiki/concepts/agent-experience/system-state-signaling|System State Signaling]]
- [[wiki/concepts/ux-research/ai-persona-replication|AI Persona Replication]] — Toyota's philosophy-not-transcripts method, and why it is riskier in a research context.
