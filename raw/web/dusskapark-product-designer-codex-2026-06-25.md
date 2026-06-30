---
source_url: https://dusskapark.medium.com/how-far-can-a-product-designer-build-with-codex-82d4bc4bb57f
captured: 2026-06-25
title: "How Far Can a Product Designer Build with Codex?"
authors: [Joo Hyung Park (Jude)]
published: 2026-06-10
publisher: Medium
---

# How Far Can a Product Designer Build with Codex?

**Author:** Joo Hyung Park (Jude / dusskapark) — Medium, 2026-06-10.
**Capture status:** Fetched via web_fetch 2026-06-25; AI-written summary of the article (not verbatim). Stack names and the build narrative are the author's.

## Summary

A product designer asks how far the designer's responsibility can extend when AI coding tools (OpenAI **Codex**) collapse the cost of implementation. The reframed question: not "write more code," but **can a designer own the whole path** from problem → system model → implementation → testing → launch story? Jude answers by shipping a real **shuttle-booking platform for NaSum Church** (a Korean Presbyterian church in Singapore), end to end, across web + native iOS + Android + a dedicated driver app. Core thesis: **product judgment, not coding capacity, stays the bottleneck** — "Codex expanded reach but didn't decide what mattered."

## Key Points

- **The problem (real operational uncertainty):** riders didn't know where to wait, which route to take, whether the shuttle had passed, or if anyone boarded from their stop; operators didn't know stop usage, boarding counts, or demand patterns.
- **Build 1 — Web MVP:** Next.js, Neon Postgres, Prisma, Vercel, LINE LIFF. Features: route lookup, stop details, QR check-in, operator management. Discipline: **break work into small verification loops** with explicit inputs/outputs; a **Swagger API contract served as the product blueprint**.
- **Build 2 — Native apps:** iOS (SwiftUI, Google Maps SDK, push, deep links, "Liquid Glass"); Android (Kotlin, Jetpack Compose, Material 3 Expressive, FCM). Approach: **translate validated web flows**, not copy screen-by-screen.
- **Build 3 — Driver app:** key insight — QR check-ins can't signal an arrival at an *empty* stop (no riders = no event). Fix: a dedicated **Driver app makes the shuttle itself the authoritative signal source**; driver location updates the server, which updates rider maps. Result = a Rider–Driver platform.
- **Planning Mode:** before coding, used Codex to map flows, define API contracts, set scope, and establish verification criteria — more valuable than rushing to implementation.
- **Verification loop:** a feature is "done" only when data flows API → screen → DB with predictable failure modes.
- **Mobile/remote workflow ("hospital room"):** while caring for his father in Korea, Jude drove development on a Singapore Mac mini via ChatGPT mobile + **voice input**. Worked because Codex had repo context (voice → work plans) and because **visible feedback loops** let Codex read logs, summarize failures, and propose next steps.
- **Test-Drive Mode:** unable to test with real shuttles constantly, he had Codex build **simulator functionality** that surfaced sync and state-management bugs.
- **Tools:** Codex, Cursor, Claude Code (dev); Next.js/Neon/Prisma/Vercel/LINE LIFF (web/API); SwiftUI + Google Maps SDK (iOS); Jetpack Compose + Google Maps Compose + Firebase FCM (Android).
- **What worked:** small clear tasks with visible success criteria; API contract as cross-platform blueprint; web MVP validation before native; voice-controlled remote dev; real operational feedback exposing the empty-stop gap.
- **What didn't:** web-only messenger approach lacked platform-appropriate access; single-signal (rider check-in) model broke under realistic variation; mobile env couldn't initially replicate desktop inspection.
- **Lessons / quotes:** "The most useful habit was turning vague failure into a smaller sentence." Owning the SDLC doesn't require becoming a full-time engineer — it requires understanding system models, API contracts, data flows, platform constraints, real-device behavior, store requirements, and analytics deeply enough to **ask better questions**. The shift is owning the distance "between deciding and trying"; when that distance shrinks, ideas survive iteration instead of dying as prototypes.
- **Outcomes:** two shipped apps — *NaSum Shuttle Check-In* (rider) and *NaSum Shuttle Driver* — on iOS App Store + Google Play, plus a launch promo video.

## Follow-up

- Pull exact quotes/screenshots from the original for verbatim citation; capture any metrics (timeline, adoption) if added.
