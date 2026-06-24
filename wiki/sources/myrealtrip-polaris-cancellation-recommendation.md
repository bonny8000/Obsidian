---
type: source
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [product-engineering, ux-case-study, recommendation, ai-as-critic, observational-data, platform-design, problem-definition, myrealtrip]
source_path: raw/web/myrealtrip-polaris-cancellation-recommendation-2026-06-22.md
source_url: https://blog.myrealtrip.com/cwisoreul-ggeuti-anira-sijagjeomeuro-cwiso-hwamyeoneseo-daeum-yeohaengeul-jeanhan-iyagi/
authors: [배재경 (Bae Jae-kyung)]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.78
---

# Myrealtrip "Polaris": Turning the Cancellation Screen into the Next Trip's Starting Point

**Author/Subject:** 배재경 (Bae Jae-kyung), Member/Order Dev Team — a Myrealtrip **PEPE** (Product Engineer Possibility Exchange) session write-up.
**Published:** 2026-06-19 — Myrealtrip Blog (Korean).
**Raw capture:** [[raw/web/myrealtrip-polaris-cancellation-recommendation-2026-06-22|myrealtrip-polaris-cancellation-recommendation-2026-06-22]]
**URL:** [blog.myrealtrip.com/…cwiso-hwamyeoneseo-daeum-yeohaengeul-jeanhan-iyagi](https://blog.myrealtrip.com/cwisoreul-ggeuti-anira-sijagjeomeuro-cwiso-hwamyeoneseo-daeum-yeohaengeul-jeanhan-iyagi/)

## Citation

Bae, J. (2026, June 19). *Turning cancellation into the start of the next trip: how one recommendation grew into a larger structure* [PEPE session]. Myrealtrip Blog. Captured 2026-06-22 into `raw/web/myrealtrip-polaris-cancellation-recommendation-2026-06-22.md`.

## Summary

A Product-Engineer case study at Myrealtrip (Korean travel platform). The problem was **the empty space after a cancellation** — after a refund notice, nothing answered "so what can I do *instead* of this trip?" Worst in Southeast-Asia tours (high weather-driven cancellations, low re-booking). The reframe: **treat cancellation as the *start* of the next trip, not the end** — at the moment cancellation completes, surface *currently bookable* alternatives, riding the cancellation flow rather than a separate re-engagement campaign. Named **"Polaris" (North Star)**. The single feature later grew into a reusable **audience / surface / trigger / content** platform.

## Key Claims

- **The hardest part was problem definition, not code** (~3 weeks). First time owning a problem end-to-end as a PE (define → design → build → own outcome), vs implementing a handed-down spec.
- **"Not showing badly" mattered as much as "showing well."** Deciding *when NOT to recommend* (and how to handle "no suitable product found") was harder than the show-rules — a clumsy recommendation at a sensitive moment harms the experience.
- **AI used as a critic/rebutter, not an answer machine:** he asked Claude Code & GPT to *argue against* his recommendation policy and surface missed conditions/edge cases. "AI's value wasn't in giving answers; it was in rebutting what I might have missed." → faster policy refinement, lighter decisions.
- **Result:** users shown a recommendation had a **~70% higher 7-day re-booking rate** vs not-shown, with meaningful GMV/profit; system-auto and ops-curated recommendations performed similarly.
- **Disciplined causal honesty:** "This is observational, not a randomized experiment, so I can't claim this is the pure effect of the recommendation" — treats the number as a *signal*, not proof (the two groups may differ in disposition).
- **Feature → platform:** new asks (ads, promotions, coupons elsewhere) all reduced to one question — **who, at what moment, what content, in what form** — so he re-architected into **four composable axes (audience / surface / trigger / content)** plus an **ops tool** decoupling builders from operators. "A good feature is used once; a good platform keeps solving new problems."

## Useful Examples

- **AI-as-rebutter prompt pattern** ("how should it behave here? what condition did I miss?") — a concrete, reusable way to use an LLM to harden a policy/spec rather than to author it.
- **The four-axis decoupling** (audience/surface/trigger/content) as a template for any contextual-messaging / in-product recommendation surface.
- **Ops-tool decoupling** (ops designs exposure policy, placement, content, schedule themselves) as a pattern for shortening idea→screen time.

## Constraints / Caveats

- **Company engineering-blog case study** (single team, single product), promotional in tone; not independent evaluation.
- **Headline ~70% lift is observational** — the author explicitly does *not* treat it as causal. Don't cite it as a clean effect size.
- Korean-language source; details summarized in the raw capture.

## Design Implications

- **Reframe "end states" (cancellation, error, empty) as next-action starting points** — design the bridge to the next behavior on the *same* surface, not via a later campaign.
- **AI-as-critic is a safe, high-value LLM use** for policy/spec/edge-case work — it complements the vault's other "AI as reviewer" evidence ([[sources/fowler-sensors-coding-agents|Böckeler sensors]], [[sources/bayer-prince-reliable-agentic-ai|Bayer PRINCE reflection loops]]).
- When the same question recurs across requests, **abstract to composable axes + an ops tool** instead of building one-off features.
- Carry the **observational-vs-causal humility** — pairs directly with [[sources/bakhshi-representative-sample|Bakhshi's claim-based sampling]].

## Tensions

- **Velocity vs sensitivity:** recommending at a sensitive moment (just-cancelled) can help or harm — restraint ("when not to show") is a first-class design decision.
- **Feature vs platform:** building the general structure costs more up front but absorbs future requests — the classic abstraction trade-off.

## Open Questions

- What would a true A/B (randomized) test show vs the ~70% observational lift?
- How far does the audience/surface/trigger/content platform generalize beyond cancellation (ads, coupons, onboarding)?

## Concepts Linked

- [[concepts/product-management/feature-vs-platform|Feature vs Platform]] (new)
- [[concepts/ai-agents/ai-as-thinking-partner|AI as Thinking Partner]]
- [[concepts/ai-agents/product-evals|Product Evals]]
- [[concepts/ux-research/validity-and-decision-relevance|Validity and Decision Relevance]]
- [[concepts/product-management/discovery-phase|Discovery Phase]]
- [[concepts/ux-research/problem-discovery-model|Problem Discovery Model]]
- [[concepts/product-management/role-convergence|Role Convergence]]

## LLM Use

- **Use for:** reframing end-states (cancel/error/empty) into next-action moments; the AI-as-rebutter pattern for hardening policies/specs/edge cases; the audience/surface/trigger/content platform pattern; modeling observational-vs-causal humility.
- **Do not use for:** citing the ~70% lift as a causal effect; treating a single company blog as generalizable evidence.
- **Best prompt pattern:** "Act as a rebutter of this recommendation/exposure policy: list the conditions where it should NOT fire, the edge cases I missed, and the moments where showing this could harm the experience."

## Reliability Notes

> [!warning] Caveats
> - **Vendor engineering-blog case study**, full text captured. Confidence 0.78 on the design lessons and patterns; the ~70% figure is observational by the author's own statement — not a clean effect.

## Backfill Status

- New 2026-06-22 from full web capture (Korean). All sections populated.
