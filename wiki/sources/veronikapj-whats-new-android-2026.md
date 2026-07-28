---
type: source
status: active
created: 2026-07-28
updated: 2026-07-28
tags: [android, compose, adaptive-ui, app-functions, mcp-integration, on-device-ai, accessibility, privacy, platform-reference]
source_path: raw/web/veronikapj-whats-new-android-2026-07-28.md
source_url: https://veronikapj.github.io/whats-new-android-2026/
authors: [배필주]
sources: []
ingest_level: deep
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.70
---

# 배필주 (2026): What's New in Android 2026 — Compose First to Multi-Device

## Citation

배필주 (Bae Pilju), 「What's New in Android 2026 · Compose First부터 멀티 디바이스까지」, personal site, 2026-07 baseline. Blog adaptation of a **GDG Korea Android / Google I/O Extended** session.

**Source type:** Secondary reporting — a community conference session summarizing Google platform announcements.
**Raw capture:** [[raw/web/veronikapj-whats-new-android-2026-07-28|veronikapj-whats-new-android-2026-07-28]]

## Summary

A six-theme survey of the Android 2026 release. Its relevance here is not the platform detail but the fact that **three of six themes are agent-and-adaptivity themes**: apps exposing callable functions to agents, capable on-device models, and adaptive layout becoming mandatory rather than optional.

The two entries worth carrying forward: **App Functions**, an on-device MCP where `@AppFunction`-annotated methods become agent-callable tools and **KDoc becomes the agent-readable description**; and **adaptive-by-default**, where the system simply ignores `screenOrientation`, `resizableActivity`, and aspect-ratio limits on large screens with **no opt-out for API 37+ targeting**.

## Key Claims

- **Apps become tool providers, not just UIs.** App Functions expose capabilities as orchestratable tools via on-device MCP; the stated direction is a shift from UI-driven interaction to agent-invoked functionality.
- **Documentation becomes the agent interface.** KDoc on an `@AppFunction` is what the agent reads to decide whether and how to call it — making doc comments a functional surface rather than a courtesy.
- **Accessibility semantics become the agent fallback path.** **Computer Control** drives apps that made no code changes, and it relies on accessibility semantics. The session lists an accessibility semantic audit as an "important, prepare now" item *because* it supports Computer Control.
- **Adaptivity is no longer opt-in.** On large screens (`sw > 600dp`) the system ignores orientation and resizability constraints, and the large-screen opt-out is removed for API 37+.
- **On-device capability jumped:** Gemini Nano 4, 12GB RAM requirement, up to 4× faster with 60% less battery (AICore Developer Preview).
- **Compose-first is now unambiguous:** the View toolkit is in maintenance mode; new code should be Compose, with interop preserving existing View code.
- **Silent failure is a new class of production bug:** Android 17's Memory Limiter kills processes exceeding per-app caps **with no stack trace**, detectable only via `ApplicationExitInfo` flagged `MemoryLimiter:AnonSwap`.
- **Privacy changes are picker-shaped:** standard system pickers (Contact Picker, Embedded Photo Picker) replace broad permissions, and targeting Android 17 blocks the permission where a picker solves the case.

## Useful Examples

**Reported performance figures** (as presented in the session, not independently verified):

| Change | Reported effect |
|---|---|
| Styles API vs. Modifier-only | ~77% fewer object allocations, ~59% less execution time |
| Full R8 mode (Monzo) | 35% ANR reduction, 30% cold-start improvement, 9% app-size reduction |
| Gemini Nano 4 | up to 4× faster, 60% less battery |
| Wear OS 7 | 10% battery improvement |

**Agent-facing surface, concretely:**

- `@AppFunction` annotation + KDoc description → on-device MCP tool.
- Computer Control → UI automation fallback over accessibility semantics, no app changes required.

**Adaptive layout API set (I/O 2026):** `Grid` and `FlexBox` auto-reflow · `MediaQuery` conditional UI · Navigation 3 Scene Decorators · window size classes (Compact / Medium / Expanded) · `CameraXViewfinder` for responsive camera preview across foldables · trackpad support raised to mouse level in Compose 1.11.

**Migration-critical items** named as timeline-bound: Contact Picker before Android 17 targeting · SMS OTP via SMS Retriever or SMS User Consent (3-hour read delay for non-targeted SMS) · BAL `PendingIntent` mode change (`ALLOW_ALWAYS` deprecated → `ALLOW_IF_VISIBLE`) · adaptive layouts for `sw > 600dp`.

## Constraints / Caveats

- **Secondary source, twice removed.** A community-session blog adaptation of Google announcements. Every figure should be traced to Google's own release notes before being used in a decision.
- **No methodology for any performance number.** The 77% / 59% Styles API figures, the Monzo R8 numbers, and the Nano 4 claims all arrive without test conditions, baselines, or workloads.
- **Preview-stage features are described alongside production ones.** App Functions is Preview; Gemini Nano 4 is Developer Preview; Styles API is `@Experimental`. Timelines and APIs will change.
- **Version and date specificity is a liability.** API levels, BOM versions, and H2-2026 ship dates make this source perishable — it is a snapshot with a short half-life.
- **Korean-language conference recap**, ingested from an AI-generated extraction. Terminology may not match Google's official English naming exactly.
- **Not a design source.** It says agent-invocable functions and mandatory adaptivity are arriving; it says nothing about how to *design* for either.

## Design Implications

- **Treat app capabilities as an API for agents.** If agent invocation is the direction, the unit of product design shifts from screens to callable capabilities with legible contracts.
- **Write documentation the agent will actually read.** KDoc-as-agent-description means doc quality directly determines whether a capability is invoked correctly — the same claim [[wiki/concepts/infrastructure-dev/ai-readable-documentation|AI-Readable Documentation]] makes, now enforced by a platform.
- **Accessibility metadata acquires a second consumer.** Semantics that were for assistive technology now also determine whether agent-driven automation can operate the app. Under-labeled UI is now both an accessibility defect and an agent-compatibility defect.
- **Stop treating orientation and size as app decisions.** Adaptive-by-default with no opt-out makes window size classes and reflow layout table stakes.
- **Add silent-kill monitoring.** A crash class with no stack trace requires deliberate `ApplicationExitInfo` instrumentation or it will be invisible.
- **Prefer system pickers over broad permissions** as the default pattern — permission-light UX is being enforced, not merely encouraged.

## Tensions

- **Reinforces [[wiki/sources/b2b-admin-web-accessibility|the accessibility source]] from the opposite direction.** One argues accessibility pays back through daily human repetition; this one shows accessibility semantics becoming the substrate for agent automation. Two independent 2026 sources, two different reasons, same conclusion: accessibility metadata is now load-bearing.
- **Extends [[wiki/concepts/ai-agents/mcp-integration|MCP Integration]] to the on-device consumer surface.** Most MCP material in this wiki concerns developer tooling and server-side integration; App Functions puts the same protocol shape inside a phone, with the OS as orchestrator.
- **Against the 2026-07-28 cluster's constraint theme, mildly.** Computer Control is explicitly agent automation over UI *without* app cooperation — capability granted broadly rather than a narrow contract. It resembles the open-ended agency that [[wiki/sources/socar-self-healing-agents|SOCAR]] found unreliable, with the same accessibility-tree mechanism SOCAR used deliberately.
- **Unresolved: who authorizes an App Function call?** This source describes the mechanism and not the consent model, which is precisely the boundary [[wiki/sources/naver-d2-ai-hackathon-nstake|NStake]] argues must come first.

## Open Questions

- What is the authorization and consent model for App Functions — per-call, per-app, per-agent — and where does the user see it?
- Does Computer Control give agents effective access to functionality the app never intended to expose, and is that a security surface?
- How reliable is accessibility-semantics-driven automation on apps with poor labeling — the majority case?
- Which of these previews actually ships, and on what timeline? Revisit this page against Google's own release notes.
- What does designing for agent-invoked capability look like in practice, when there is no screen to design?

## Concepts Linked from This Source

- [[wiki/concepts/agent-experience/agent-invocable-app-functions|Agent-Invocable App Functions]]
- [[wiki/concepts/agent-experience/natively-adaptive-interfaces|Natively Adaptive Interfaces]]
- [[wiki/concepts/ai-agents/mcp-integration|MCP Integration]]
- [[wiki/concepts/infrastructure-dev/ai-readable-documentation|AI-Readable Documentation]]
- [[wiki/concepts/ux-research/web-accessibility-pour|Web Accessibility (POUR)]]
- [[wiki/concepts/infrastructure-dev/edge-ai|Edge AI]]
- [[wiki/concepts/infrastructure-dev/android-dynamic-feature-module|Android Dynamic Feature Module]]

## LLM Use

Use as a **platform-direction signal and a migration checklist**, not as an authority. The valuable content is App Functions (apps as agent tool providers), Computer Control (accessibility semantics as the agent's interface), and adaptive-by-default (adaptivity is mandatory). Cite the *direction*; verify every version, API level, and percentage against Google's release notes before acting.

Treat as **partial-strength for grounded recommendation**: fine for orientation and planning, not for a decision that turns on a specific figure or ship date.

## Reliability Notes

- **Secondary reporting of first-party announcements**, which is the source's main limitation — accurate transmission cannot be assumed and is not verifiable from the capture.
- **Confidence 0.70:** the platform facts are almost certainly directionally correct and specifically stated, but every number is unsourced, several features are preview-stage, and the page is a community recap.
- **Highly perishable.** Re-verify or supersede when Android 17 ships and Google publishes final release notes; update this page rather than creating a second one.
- Ingested from an AI-generated extraction of a Korean-language post.
