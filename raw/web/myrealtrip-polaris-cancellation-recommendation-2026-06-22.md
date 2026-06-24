---
source_url: https://blog.myrealtrip.com/cwisoreul-ggeuti-anira-sijagjeomeuro-cwiso-hwamyeoneseo-daeum-yeohaengeul-jeanhan-iyagi/
captured: 2026-06-22
title: "취소를 끝이 아닌 다음 여행 시작으로 (Turning cancellation into the start of the next trip)"
authors: [배재경 (Bae Jae-kyung), Myrealtrip]
published: 2026-06-19
publisher: Myrealtrip Blog (PEPE session)
---

# Myrealtrip "Polaris": Turning the Cancellation Screen into the Next Trip's Starting Point

**Author/Subject:** 배재경 (Bae Jae-kyung), Member/Order Dev Team — a Myrealtrip PEPE (Product Engineer Possibility Exchange) session write-up.
**Published:** 2026-06-19 — Myrealtrip Blog (Korean).

## Summary

A Product-Engineer case study at Myrealtrip (Korean travel platform). The problem: **the empty space after a cancellation** — when a booking is cancelled the user sees a refund notice and leaves, with nothing answering "so what can I do instead of this trip?" Worst in Southeast Asia tours (high weather-driven cancellations, low re-booking). The reframe: **treat cancellation not as the end but as the starting point of the next trip** — at the moment cancellation completes, show *currently bookable* alternative products, riding the cancellation action rather than a separate re-engagement campaign. Project named **"Polaris" (North Star)** — guiding a disoriented traveller to a next direction.

## Key Points

- **Hardest part was problem definition, not code** (~3 weeks total). First-time end-to-end PE experience: he had to decide *who to show what, when* — and especially *when NOT to show* a recommendation (a clumsy recommendation at a sensitive moment harms the experience). "Not showing badly" mattered as much as "showing well"; edge cases (no suitable product found) were heavier than implementation.
- **AI used as a critic/rebutter, not an answer machine:** he asked Claude Code & GPT to *argue against* his recommendation policy ("how should it behave here?", "what conditions did I miss?") to find holes — "AI's value wasn't in giving answers; it was in rebutting what I might have missed." Faster policy refinement, lighter decisions.
- **Result:** users shown a recommendation had a **~70% higher 7-day re-booking rate** vs not-shown, with meaningful GMV/profit. System-auto vs ops-curated recommendations performed similarly.
- **Careful, non-overclaiming framing (important):** "This is observational, not a randomized experiment, so I can't claim this is the pure effect of the recommendation" — the two groups may differ in disposition. Treats it as a *signal*, not proof. (Mirrors causal-inference caution.)
- **From feature to platform:** new asks (ads, promotions, coupons elsewhere) all reduced to one question — **who, at what moment, what content, in what form** — so he re-architected into **four composable axes: audience / surface / trigger / content**, plus an ops tool letting the ops org design exposure policy, pick placement, register content, manage schedule (decoupling builders from operators → faster iteration). "A good feature is used once; a good platform keeps solving new problems." Cancellation-recommendation became one case running on a shared structure.
