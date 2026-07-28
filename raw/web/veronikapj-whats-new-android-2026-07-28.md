---
source_url: https://veronikapj.github.io/whats-new-android-2026/
captured: 2026-07-28
title: "What's New in Android 2026 · Compose First부터 멀티 디바이스까지"
authors: [배필주 (Bae Pilju)]
published: 2026-07
publisher: personal site (GDG Korea Android — Google I/O Extended session adaptation)
language: ko
---

# What's New in Android 2026 — From Compose First to Multi-Device

**Author:** 배필주 (Bae Pilju) · **Baseline:** 2026-07 · **Captured:** 2026-07-28
**Capture note:** AI-written summary of a Korean-language blog adaptation of a GDG Korea Android / Google I/O Extended session. Secondary reporting on Google announcements — figures are as presented in the session, not independently verified. Full text not reproduced.

## Summary

A six-theme survey of the Android 2026 platform release, notable for this vault because three of the six themes are about **agents and adaptivity**: apps exposing callable functions to agents, on-device model capability, and adaptive-by-default layout with no opt-out.

## 1. UI and development environment

- **Compose-first strategy.** The View toolkit enters maintenance mode — critical fixes only.
- **Styles API** (Compose 1.11, `@Experimental`): reusable style objects for visual properties with inheritance. Reported ~**77% fewer object allocations** and ~**59% less execution time** than Modifier-only approaches.
- **Android Skills:** an official Compose migration framework; the guidance is to customize it to preserve existing architecture (e.g. keep MVVM rather than being pushed into UDF).

## 2. Performance and build

- **R8 Configuration Analyzer:** three-score assessment (Shrinking / Optimization / Obfuscation) and identification of keep-rules that block optimization.
- **Memory Limiter (Android 17):** per-app memory caps; exceeding them kills the process **with no stack trace**. Detection via `ApplicationExitInfo` flagged `MemoryLimiter:AnonSwap`.
- **Full R8 mode:** 35% ANR reduction, 30% cold-start improvement, 9% app-size reduction (Monzo case study).

## 3. AI and intelligent agents

- **App Functions:** an **on-device MCP** exposing app capabilities as orchestratable tools. Functions are marked `@AppFunction`, and **KDoc becomes the agent-readable description**.
- **Computer Control:** fallback UI automation for apps that make no code changes — it relies on **accessibility semantics**.
- **Gemini Nano 4:** requires 12GB RAM; up to 4× faster, 60% less battery; available via AICore Developer Preview.
- The stated direction is a shift **from UI-driven interaction to agent-invoked functionality**.

## 4. Privacy and security (Android 17 critical path)

- **Contact Picker** — new standard UI replacing `READ_CONTACTS`; targeting Android 17 blocks using the permission where the picker solves the case.
- **SMS OTP hardening** — 3-hour read delay for non-targeted SMS; migrate to SMS Retriever (fully automatic) or SMS User Consent (single dialog).
- **Background Activity Launch hardening** — `setPendingIntentBackgroundActivityStartMode()` defaults to `MODE_BACKGROUND_ACTIVITY_START_ALLOW_IF_VISIBLE`; `ALLOW_ALWAYS` deprecated.
- **Embedded Photo Picker** — permission-free, SurfaceView-based in-app embedding with continuous selection and real-time UI sync (Android 14+, Play Services backport).
- **Local network** — SDK 37 targets require `ACCESS_LOCAL_NETWORK` runtime permission; blocked by default.
- **Certificate Transparency** — on by default; self-signed certificates need a Network Security Configuration opt-out.

## 5. Media and system integration

- **Media3 as the unified pipeline:** CameraX (capture) → Media3 AI Effects (post-processing) → ExoPlayer (playback).
- **PreloadManager** — smart prefetching for sequential video; the app specifies prefetch depth, the manager prioritizes by playback proximity.
- **CameraXViewfinder** — Compose component handling responsive preview scaling across foldables and tablets.
- **ExoPlayer Scrubbing Mode** — `setScrubbingModeEnabled(true)` for optimized rapid seeking.
- **Background audio hardening** — playback / focus / volume changes require a foreground activity or a `mediaPlayback` FGS with while-in-use permission (Android 17, API 37 targeting). `MediaSessionService` handles the lifecycle automatically.
- **CodecDB (Android 17)** — recommends optimal encoding per chipset.

## 6. Multi-device adaptive ecosystem

- **Adaptive by default.** The system **ignores** app-set `screenOrientation`, `resizableActivity`, and aspect-ratio limits on large screens (`sw > 600dp`). **No opt-out for API 37+ targeting.**
- **Window size classes** — Compact / Medium / Expanded branching.
- **New layout APIs (I/O 2026):** `Grid` and `FlexBox` auto-reflow; `MediaQuery` conditional UI; Navigation 3 Scene Decorators for shared UI.
- **Trackpad parity** — Compose 1.11 raises trackpad support to mouse level; focus indicators added.
- **Wear OS 7** (Android 17 base, H2 2026): 10% battery improvement, Wear Widgets (2×1 / 2×2), Live Updates, on-device Gemini (Nano v3).
- **Android XR** — Developer Preview 4; existing adaptive apps render unchanged in immersive environments.

## Feature / version index

| Feature | API level | Jetpack version | Status |
|---|---|---|---|
| Styles API | — | Compose 1.11 (BOM 2026.04.01) | `@Experimental` |
| R8 Analyzer | — | AGP | Production |
| Memory Limiter | 37 (Android 17) | — | Production |
| App Functions | — | — | Preview |
| Gemini Nano 4 | — | — | AICore Developer Preview |
| Contact Picker | 37 | — | Production |
| SMS Retriever | 26+ | Play Services | Production |
| Embedded Photo Picker | 34+ | Media3 | Production (Extensions 15+) |
| PreloadManager | — | Media3 | Production |
| MediaSessionService | 21+ | Media3 | Production |
| CameraXViewfinder | — | CameraX | Production |
| Adaptive layout APIs | — | Compose 1.11 | Production |

## Developer priorities as presented

**Critical (timeline-bound):** Contact Picker migration before Android 17 targeting; SMS OTP via Retriever or User Consent; BAL `PendingIntent` options; adaptive layouts for `sw > 600dp`.

**Important (prepare now):** R8 Analyzer baseline and keep-rule review; `ApplicationExitInfo` monitoring for Memory Limiter; **accessibility semantic audit** (which is what makes Computer Control fallback work); Wear OS 7 testing.

**Enhancement:** Styles API for theming; PreloadManager for video feeds; Embedded Photo Picker; Credential Manager conditional create.

## Deprecations and removals

- View toolkit: new features halted; RecyclerView 1.4.0 and Fragment 1.8.9 mark maintenance endpoints.
- `READ_CONTACTS`: blocked for Android 17 targeting where Contact Picker covers the case.
- `MODE_BACKGROUND_ACTIVITY_START_ALLOWED` deprecated in favor of `ALLOW_IF_VISIBLE`.
- `screenOrientation` XML attribute ignored on large screens; large-screen opt-out removed.

## Notable framing

"Adopt Compose at your own pace," but new code should be written in Compose; View remains functional via interop and receives no new features.
