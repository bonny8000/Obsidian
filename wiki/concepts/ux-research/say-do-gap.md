---
type: concept
status: active
created: 2026-06-22
updated: 2026-06-29
tags: [concept, say-do-gap, stated-vs-revealed, purchase-intent, willingness-to-pay, survey-validity]
sources: [svenja-pieritz-positioning-experiment, brox-digital-twins-market-research, voiceofuser-inhouse-digital-twins-blueprint]
confidence: 0.8
---

# Say-Do Gap

> [!abstract] Summary
> The gap between what people *say* (relevance, appeal, stated intent, desire) and what they *do* (buy, convert, pay). Stated preference is not revealed behavior — and the two often point in different directions.

> [!important] Why it Matters
> Research that measures appeal/relevance and reads it as demand is the classic trap: a concept can score high on "this is relevant to me" and still not move anyone to act. Measuring the wrong axis produces confident, wrong conclusions.

## 📝 Key Claims
- **Relevance ≠ purchase intent:** in Pieritz's framing test, all three framings felt relevant, but only the purchase-intent measure separated them (and the framing she was most confident in lost).
- **Desire ≠ willingness to pay:** users wanting high-value extras doesn't survive a real price (the Kiwi.com bundle example) — wanting and paying are different axes.
- Even surveyed *intent* is itself a stated measure — the deepest say-do gap (intent → actual conversion) needs behavioral data.
- Practical move: **measure intent/behavior, not just appeal**, and treat appeal-without-conversion as a signal to dig, not a green light.
- **Synthetic respondents inherit the say-do gap at its source.** [[concepts/ux-research/digital-twin-respondents|Digital-twin respondents]] built largely from *interviews* (self-report) model what people *say*, not what they'd *do* — Brox twins grounded in AI-driven interviews are vulnerable to exactly this ([[sources/brox-digital-twins-market-research|Brox, 2026]]). The in-house blueprint partly counters it by grounding on **behavioral telemetry** (what users *did*), but then a twin's *opinions* become model inferences over behavior — a fresh say-do tension rather than an escape from it ([[sources/voiceofuser-inhouse-digital-twins-blueprint|The Voice of User, 2026]]).

## 🔗 Related Concepts
- [[concepts/ux-research/validity-and-decision-relevance|Validity and Decision Relevance]]
- [[concepts/ux-research/self-reported-ux-metrics|Self-Reported UX Metrics]]
- [[concepts/agent-experience/satisfaction-vs-benefit|Satisfaction vs Benefit]]
- [[concepts/ux-research/synthetic-survey-data|Synthetic Survey Data]]
- [[concepts/ux-research/digital-twin-respondents|Digital-Twin Respondents]] — interview-grounded twins inherit the say-do gap.
- [[concepts/ux-research/maxdiff-prioritization|MaxDiff Prioritization]]

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> Behavioral measures aren't a panacea either — context, price framing, and moment all shift behavior. The point is not "ignore what people say" but "don't substitute stated appeal for revealed demand."

## 📚 Sources
- [[sources/svenja-pieritz-positioning-experiment|Pieritz (2026): People Loved How I Described My Services…]]
- [[sources/brox-digital-twins-market-research|Brox: 60,000 "digital twins" of real people (VentureBeat, 2026)]] — interview-grounded twins inherit stated-not-revealed bias.
- [[sources/voiceofuser-inhouse-digital-twins-blueprint|The Voice of User: In-House Digital-Twins Blueprint (2026)]] — behavioral grounding shifts, not removes, the say-do tension.

## ❓ Open Questions
- When does stated intent reliably predict behavior, and for which decisions?
- How to design cheap proxies for revealed behavior early in a study?
