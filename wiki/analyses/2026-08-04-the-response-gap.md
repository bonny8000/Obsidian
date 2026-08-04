---
type: analysis
status: active
created: 2026-08-04
updated: 2026-08-04
tags: [analysis, agent-experience, latency, voice-interface, system-state, turn-taking, modality, memo]
sources:
  - toyota-voice-interaction-humanoid-robots
  - paxton-yao-voice-ai-thinking-state
  - smashing-matching-ai-modality-user-intent
  - google-natively-adaptive-interfaces
  - google-search-io-2026-agents
confidence: 0.58
---

# The Response Gap: What Fills the Second That LLMs Added

**Memo date:** 2026-08-04 · Written under AGENTS.md Rule 11 on a five-source cluster.

## Research Question

LLM inference inserted a durable, user-visible pause into conversational interaction that did not previously exist. **What should occupy that pause, and does any of the available evidence say which choice is better?**

## Evidence Base

| Source | Contribution | Confidence |
|---|---|---|
| [[wiki/sources/toyota-voice-interaction-humanoid-robots\|Toyota FRC (2026)]] | Three latency techniques; the ~1s target; the admission it is not met | 0.62 |
| [[wiki/sources/paxton-yao-voice-ai-thinking-state\|Yao (2026)]] | The gap as a *new state*; two-vs-five state models; viewing-context rule | 0.48 |
| [[wiki/sources/smashing-matching-ai-modality-user-intent\|Yocco (2026)]] | Modality–intent matrix; the four constraint questions | 0.58 |
| [[wiki/sources/google-natively-adaptive-interfaces\|Google (2026)]] | Adaptation decided at runtime, inside the agent | — |
| [[wiki/sources/google-search-io-2026-agents\|Google Search I/O (2026)]] | Generative UI and background agents shipping at scale | 0.55 |

**Not one of these five measures anything about the response gap.** That is the memo's finding as much as its limitation.

## Synthesis

### 1. Two sources, published one day apart, solved the same problem in different media without knowing about each other

Toyota published 2026-07-31. Yao published 2026-08-01. Both are about the same second.

**Toyota fills it with speech.** A stated deadline (*"desirable for the response to begin within approximately one second"*), a priority ladder (main response > clarification > filler), parallel speculative execution across routing/retrieval/generation with discard, and "think while listening" — beginning generation before the user stops talking, then adopting the earliest candidate that survives a discrepancy check against the final transcript.

**Yao fills it with colour.** The gap is *"a new state that didn't exist before"*, so it needs representation: two states on desktop (Claude voice mode: orange speaking, blue listening), five in a car (NIO's NOMI: idle, countdown, listening, thinking, speaking), with the count set by whether the display is read foveally or peripherally.

Neither cites the other. Neither is aware the other exists. One comes from a Japanese automaker's robotics lab, one from a designer analysing a Chinese EV's assistant and a US AI product. **The convergence is on the problem, and the divergence is on the instrument.**

### 2. The two instruments are complementary, and nothing in the vault does both

They are not competing answers. They are answers to two different questions inside the same second:

- **Covering** (Toyota): make the wait shorter or make it not feel like a wait.
- **Labelling** (Yao): make the wait honest and readable.

A system could do both, and the memo's most useful observation is that **it is not obvious they compose.** A pre-emptively generated *"Um"* performs thought; an honest indicator reports thought. Run together, the filler risks reading as evasion rather than as naturalness — the user is being told "thinking" while also being given speech that implies the answer is nearly there. Nobody has tested this. It is a cheap experiment and it is the highest-value unrun study in this cluster.

### 3. The gap is a turn-taking problem wearing a latency costume

The most revealing detail in either source is NOMI's **countdown** state. It is not a processing state at all — it is a window in which the user may still speak. That is a *floor-holding* signal, and it is the state a system-centric model would never enumerate, because it describes the user's turn rather than the system's work.

Read through that lens, Toyota's fillers are the same move in a different medium: *"Um"* is not a progress indicator, it is a claim on the floor. Human conversation has used it that way forever. Both sources are reinventing turn-taking repair and neither names it, and [[wiki/concepts/agent-experience/initiative-and-interruption|the vault's initiative-and-interruption material]] does not connect to either.

**Implication:** the right frame for the response gap is not "loading state" but "who has the floor, and how do both parties know?" That reframing is this memo's main contribution and it is an inference, not a claim either source makes.

### 4. Modality choice constrains the stack, not just the interface

[[wiki/concepts/agent-experience/modality-intent-matching|Yocco's matrix]] maps user intent to input/output modality on ergonomic grounds — hands, eyes, social context, spare attention. Both new sources supply a constraint it does not model.

Voice imposes a **~1 second budget**, and every technique that improves answer quality — RAG, web search, multi-pass refinement — breaks it. *"There is a trade-off where utilizing these methods increases the delay until the final response."* So choosing voice is choosing an architecture: shallower retrieval, or speculative execution, or an accepted quality ceiling.

That is a real addition to the matrix. Yocco's four constraint questions (are the hands available, is a screen safe, is audio appropriate, how much attention is left) should have a fifth: **what latency does this modality tolerate, and can the answer be produced inside it?**

### 5. The honest baseline: Toyota cannot hit its own target

> "Even with these measures, we still cannot get them to consistently respond within one second."

A dedicated research team, three named techniques, two years of public deployment, and the target is not consistently met. Anyone planning a real-time conversational product should take that as the reference point rather than as a Toyota-specific shortfall.

### 6. The scale mismatch nobody in this cluster addresses

Toyota's work is two robots in a museum. Yao's is two products. Meanwhile [[wiki/sources/google-search-io-2026-agents|Google announced]] Generative UI free to all Search users and Information Agents monitoring the web 24/7 — response-gap design at population scale, with **no state model, no latency discussion, and no interruption contract described at all.**

The cluster's careful thinking about a one-second pause is happening in robotics labs and design blogs. The deployment is happening at a billion users with none of it.

## Implications

1. **Frame the gap as floor-holding, not loading.** Enumerate states that belong to the user (may I still speak?) alongside states that belong to the system (am I thinking?). This is the reframing to carry forward.
2. **Add latency to the modality decision.** Voice's ~1s budget determines what retrieval architecture is available. Make that explicit at modality-selection time, not at implementation time.
3. **Decide whether you are covering or labelling, and pick one as authoritative.** Doing both without deciding which the user should believe is the untested risk.
4. **Rank stalls; let jitter make the variation.** Toyota's cleanest idea: a priority ladder over a variable-latency generator produces natural variation as a by-product. No scripted rotation needed.
5. **Do not mask latency ahead of a consequential decision.** A convincing stall manages the user's impression of the system's confidence. Benign in a mascot robot; not benign before a recommendation the user will act on.
6. **Budget for discarded compute** and say so in the design. Speculative parallel execution is cheap relative to a conversation that feels broken, and it is a real line item.

## Risks and Counterpoints

- **This memo is built on five unmeasured sources.** Every recommendation above is architectural reasoning, not evidence. Confidence 0.58 reflects that ceiling honestly.
- **The turn-taking reframe is the vault's inference.** Neither Toyota nor Yao says it. It may be a better frame; it is not their claim, and it should not be attributed to them.
- **Latency masking is a small deception, and this memo partly endorses it.** [[wiki/concepts/agent-experience/agent-transparency|Agent transparency]] would predict a cost to a system that performs thought it is not doing. Toyota treats it as craft; this memo flags it at point 5 rather than resolving it. That is the weakest joint in the argument.
- **Generalisability from two products and two robots is very limited.** Yao's sample was chosen after the distinction was drawn; Toyota's case is a museum mascot with no task stakes.
- **The 8%-of-men colour-vision figure and the ~1s conversational threshold are both uncited.** Both are broadly accepted; neither source is a warrant.
- **The vault's own priors could be doing too much work here.** The response-gap cluster is small and new; treating it as a coherent field may be premature.

## Next Research Actions

1. **Find or run a latency-versus-perceived-responsiveness study for voice agents.** Does a filler improve perceived responsiveness or only occupy the wait? This single result determines whether half the techniques in this cluster are worth their complexity. **Highest priority in this area.**
2. **Ingest the automotive HMI literature on glance behaviour and assistant state ambiguity.** Yao's safety argument rests on it and does not cite it; the literature very likely exists and would either ground or deflate the claim.
3. **Ingest the conversational turn-taking literature** (gap/overlap timing, repair). Both sources reinvent it. Grounding the ~1s figure properly would improve two concept pages and this memo.
4. **Test whether covering and labelling compose.** Filler + honest indicator versus each alone. Cheap, unrun, and the answer changes a design default.
5. **Watch for any published state model from a large-scale deployment.** Google shipped generative and agentic surfaces to a billion users with no state model described; if one is published, it is the first population-scale evidence in this cluster.

## Sources

- [[wiki/sources/toyota-voice-interaction-humanoid-robots|Toyota FRC (2026): Voice Interaction with Humanoid Robots]]
- [[wiki/sources/paxton-yao-voice-ai-thinking-state|Yao (2026): Voice AI Gave Designers a New State to Show — Thinking]]
- [[wiki/sources/smashing-matching-ai-modality-user-intent|Yocco (2026): Matching AI Modality to User Intent]]
- [[wiki/sources/google-natively-adaptive-interfaces|Google (2026): Natively Adaptive Interfaces]]
- [[wiki/sources/google-search-io-2026-agents|Google (2026): Search at I/O 2026]]

## Concepts

- [[wiki/concepts/agent-experience/response-latency-masking|Response Latency Masking]]
- [[wiki/concepts/agent-experience/system-state-signaling|System State Signaling]]
- [[wiki/concepts/agent-experience/modality-intent-matching|Modality–Intent Matching]]
- [[wiki/concepts/agent-experience/initiative-and-interruption|Initiative and Interruption]]
- [[wiki/concepts/agent-experience/agent-transparency|Agent Transparency]]
- [[wiki/concepts/robotics-spatial/human-robot-interaction|Human–Robot Interaction]]

## Decision Table

[[wiki/comparisons/filling-the-response-gap|Filling the Response Gap]] — the six options with their costs and the conditions under which each is the right choice.
