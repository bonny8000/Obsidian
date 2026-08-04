---
type: comparison
status: active
created: 2026-08-04
updated: 2026-08-04
tags: [comparison, agent-experience, latency, voice-interface, system-state, decision-table]
sources:
  - toyota-voice-interaction-humanoid-robots
  - paxton-yao-voice-ai-thinking-state
  - smashing-matching-ai-modality-user-intent
confidence: 0.55
---

# Filling the Response Gap

## Decision Question

**An LLM-backed conversational system will take longer to answer than the interaction tolerates. What goes in the gap?**

Applies to voice assistants, in-car assistants, embodied agents, and any chat surface where the wait is long enough for the user to wonder whether the system heard them.

## Criteria

| Criterion | Why it decides |
|---|---|
| **Perceived responsiveness** | Does the wait feel shorter? The thing most designs are trying to buy. |
| **Honesty** | Does the signal accurately report what the system is doing? |
| **Cost** | Compute, engineering complexity, screen real estate. |
| **Correctness risk** | Can this mechanism cause a *wrong* answer, not just a slow one? |
| **Works eyes-free** | Usable when the user cannot look at a display. |
| **Evidence** | Has anyone measured it? |

## Matrix

| Option | Perceived responsiveness | Honesty | Cost | Correctness risk | Eyes-free | Evidence |
|---|---|---|---|---|---|---|
| **Silence** | Worst — *"silence means several different things"* | Neutral (says nothing) | None | None | n/a | None needed; it is the failure case |
| **Spinner / generic indicator** | Weak; says "busy", not "listening vs. thinking" | Honest but uninformative | Trivial | None | ✗ | None in this cluster |
| **State signalling** (colour, 2–5 states) | Moderate — resolves *which* wait this is | **High** — reports actual state | Low, but consumes display and a colour channel | None | ✗ visual only | **None.** Yao: nobody knows if 5 states are perceived as 5 |
| **Filler speech** (*"Um"*, *"Well"*) | Claimed high | **Low** — performs thought the system is not doing | Low | None | ✓ | None |
| **Clarification question** (*"Are you asking about…?"*) | High, and it is *also useful* | High — a genuine question | Low | None | ✓ | None |
| **Speculative / parallel generation** | **Highest — actually shortens the wait** | Fully honest (invisible) | **High** — discarded compute, real complexity | **Yes** — a false accept answers a question the user did not finish asking | ✓ | None |

## Recommendation Pattern

**Default: combine the cheap honest options, and add the expensive one only where the budget demands it.**

1. **Never silence.** It is the only option in the table with no upside.
2. **Signal state as the baseline** wherever a display exists. Set the state count by viewing context — foveal 2, glanceable 3, peripheral up to 5 — and never encode state in colour alone (add shape, motion, audio, or haptic).
3. **Prefer a clarification over a filler.** Same latency cover, and it is genuinely useful. This is the best-value row in the table.
4. **Use fillers as the last tier of a priority ladder**, not as a scripted behaviour: main response > clarification > filler, emitting the best available under deadline. The variation then comes free from latency jitter.
5. **Add speculative generation when the modality's budget cannot otherwise be met** — voice at ~1 s. Specify the validity check deliberately; it is the only mechanism here that can make the system *wrong*.
6. **Do not mask latency ahead of a consequential decision.** A convincing stall manages the user's impression of the system's confidence. Fine for a museum robot; not fine before a recommendation the user will act on. Prefer an honest visible wait.

### By context

| Context | Recommended combination |
|---|---|
| **Desktop voice/chat** | 2-state signal + clarification. Fillers optional; speculative generation usually unnecessary. |
| **In-car assistant** | 3–5 state signal with a non-visual second channel + clarification + speculative generation. Ambiguity here costs a glance off the road. |
| **Embodied / social robot** | Full Toyota stack — priority ladder plus speculative generation. Conversational naturalness is the product. |
| **High-stakes advisory** | State signal only. **No fillers, no performed thinking.** Honesty outranks perceived responsiveness. |
| **Background / async agent** | None of the above applies — the gap is not perceived. Design the [[wiki/concepts/agent-experience/initiative-and-interruption\|interruption]] instead. |

## The Open Question That Changes the Table

**Do covering and labelling compose?** A filler performs thought while an honest indicator reports thought. Together, the filler may read as evasion rather than naturalness. No source has tested this, and the answer would change rows 4–6 of the recommendation.

Second open question: **does a filler improve perceived responsiveness, or only occupy an unimproved wait?** If the latter, three of the six options collapse.

## ⚠️ Evidence Warning

> [!warning] Every cell in the Evidence column is empty for a reason
> No source in this cluster measured anything. Toyota describes three techniques and reports no latency figures and no ablation. Yao compares two products and explicitly says nobody knows whether five states are perceived as five. This table is **architectural reasoning organised into a decision aid**, and the confidence of 0.55 is the ceiling that imposes.
>
> Toyota's own baseline is the honest reference: a dedicated research team with all three techniques deployed *"cannot get them to consistently respond within one second."*

## Source Evidence

- [[wiki/sources/toyota-voice-interaction-humanoid-robots|Toyota FRC (2026)]] — the priority ladder, parallel speculative execution, "think while listening", the ~1 s target and the admission it is unmet. Source for rows 4–6.
- [[wiki/sources/paxton-yao-voice-ai-thinking-state|Yao (2026)]] — the ambiguous-silence problem, the 2-vs-5 state models, the viewing-context rule. Source for rows 1 and 3.
- [[wiki/sources/smashing-matching-ai-modality-user-intent|Yocco (2026)]] — modality selection, which sets the latency budget the whole table operates under.

## Related

- [[wiki/analyses/2026-08-04-the-response-gap|Memo: The Response Gap]] — the synthesis this table serves, including the turn-taking reframe.
- [[wiki/concepts/agent-experience/response-latency-masking|Response Latency Masking]]
- [[wiki/concepts/agent-experience/system-state-signaling|System State Signaling]]
- [[wiki/concepts/agent-experience/agent-transparency|Agent Transparency]] — the cost of performed thinking.
- [[wiki/comparisons/delegate-vs-determinize|Delegate vs. Determinize]] — the adjacent architecture decision.
