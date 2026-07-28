---
type: concept
status: active
created: 2026-07-28
updated: 2026-07-28
tags: [concept, agent-experience, app-functions, mcp, on-device-ai, android, agent-facing-api, accessibility]
sources: [veronikapj-whats-new-android-2026]
confidence: 0.66
---

# Agent-Invocable App Functions

> [!abstract] Summary
> Applications exposing their capabilities as **callable tools for an on-device agent** rather than only as screens for a person. In Android's implementation, a method annotated `@AppFunction` becomes an orchestratable tool over on-device MCP, and its **KDoc comment becomes the agent-readable description**. Where an app exposes nothing, **Computer Control** drives its UI instead, reading accessibility semantics.

> [!important] Why it Matters
> It relocates the unit of product design. If capabilities are invoked by an orchestrator rather than navigated by a person, the designed artifact is a **capability with a legible contract**, not a screen. Two consequences follow immediately: documentation becomes a functional surface — KDoc quality determines whether a capability is invoked correctly — and apps that expose nothing get automated anyway, through their accessibility tree, whether they intended it or not.

## 📝 Key Claims

- **Apps become tool providers.** The stated platform direction is a shift from UI-driven interaction to agent-invoked functionality.
- **Documentation is the interface.** `@AppFunction` + KDoc means the doc comment is what the agent reads to decide whether and how to call the capability. Prose quality becomes runtime behavior — the strongest version of [[wiki/concepts/infrastructure-dev/ai-readable-documentation|AI-readable documentation]] in this wiki, because a platform enforces it.
- **MCP moves on-device.** The same protocol shape this wiki has tracked in developer tooling appears inside the phone, with the OS as orchestrator.
- **There are two paths, and they differ in kind.** An explicit `@AppFunction` contract is narrow, intentional, and describable. Computer Control is broad UI automation over **accessibility semantics**, requiring no app cooperation at all.
- **Accessibility metadata gains a functional consumer.** Computer Control's dependence on the accessibility tree means under-labeled UI is now an agent-compatibility defect as well as an accessibility defect.
- **On-device capability is what makes it plausible** — Gemini Nano 4 is cited at up to 4× faster with 60% less battery (12GB RAM requirement, developer preview).

## The two invocation paths

| | Explicit contract | UI automation fallback |
|---|---|---|
| Mechanism | `@AppFunction` + KDoc → on-device MCP tool | Computer Control over accessibility semantics |
| App cooperation | Required | **None** |
| Surface exposed | Only what the developer declares | Whatever the UI can do |
| Legibility to the agent | Documented intent | Inferred from widget tree |
| Design implication | Design the capability contract | Audit accessibility semantics |

The gap between these columns is the interesting part: the fallback path exposes *more* than the intentional path, with *less* declared about it.

## Design implications

- **Design capabilities, not only screens.** Name the operation, its preconditions, its side effects, and its failure modes — the things an orchestrator needs and a screen implies.
- **Write documentation the agent will read.** If KDoc is the tool description, doc review is interface review.
- **Audit accessibility semantics as agent-compatibility work**, not only as inclusion work. It determines whether the fallback path works at all.
- **Declare the reversible surface deliberately.** An explicit function set is an opportunity to expose reads freely and gate writes — the [[wiki/concepts/ai-agents/permission-boundary-guardrails|permission-boundary]] discipline applied at the app's edge.

## ⚖️ Conflicts & Caveats

> [!warning] Preview-stage, secondary-sourced
> App Functions is Preview; Gemini Nano 4 is developer preview. The anchor is a **community conference recap of Google announcements** with no methodology behind any figure. Verify against Google's own release notes before acting, and expect API changes.

> [!warning] The consent model is undescribed
> Who authorizes an App Function call — the user per-call, per-app, per-agent? Where do they see it? The anchor source describes the mechanism and not the authorization, which is precisely the boundary [[wiki/sources/naver-d2-ai-hackathon-nstake|NStake]] argues must be settled *first*.

> [!warning] Computer Control resembles the pattern this cluster's evidence disfavors
> It is open-ended agent automation over UI without app cooperation, using the same accessibility-tree mechanism [[wiki/sources/socar-self-healing-agents|SOCAR]] used deliberately and narrowly. SOCAR's finding was that constrained sequential stages beat open-ended agency. A general-purpose UI-driving agent is the open-ended case, at OS scale.

> [!warning] It may expose capability the app never intended
> UI automation reaches whatever the interface can do. That is a security surface, and nothing in the anchor source addresses it.

> [!warning] Reliability against poor labeling is unknown
> Most apps are imperfectly labeled. The anchor source does not say how well semantics-driven automation performs on them — which is the majority case and therefore the real question.

## 🔗 Related Concepts

- [[wiki/concepts/agent-experience/natively-adaptive-interfaces|Natively Adaptive Interfaces]] — the sibling idea: the agent adapting the interface rather than invoking its functions.
- [[wiki/concepts/ux-research/web-accessibility-pour|Web Accessibility (POUR)]] — the semantics layer this depends on.
- [[wiki/concepts/ai-agents/mcp-integration|MCP Integration]] — the protocol, here at on-device scale.
- [[wiki/concepts/infrastructure-dev/ai-readable-documentation|AI-Readable Documentation]] — KDoc-as-tool-description is its enforced form.
- [[wiki/concepts/ai-agents/permission-boundary-guardrails|Permission-Boundary Guardrails]] — the unresolved authorization question.
- [[wiki/concepts/agent-experience/a2ui-protocol|A2UI Protocol]] — agents composing UI, the inverse direction of the same relationship.
- [[wiki/concepts/agent-experience/collaboration-patterns|Collaboration Patterns]]
- [[wiki/concepts/infrastructure-dev/edge-ai|Edge AI]] — the on-device capability that makes this viable.
- [[wiki/concepts/ai-agents/agent-skills|Agent Skills]] — procedural capability declaration in the developer-tooling equivalent.

## 📚 Sources

- [[wiki/sources/veronikapj-whats-new-android-2026|배필주 (2026): What's New in Android 2026]] — sole source: App Functions, KDoc-as-description, Computer Control, Gemini Nano 4. Secondary reporting; see caveats.

## ❓ Open Questions

- What is the authorization and consent model for an App Function call, and how is it surfaced to the user?
- Does Computer Control give agents effective access to functionality an app never intended to expose?
- How reliable is semantics-driven automation on poorly labeled apps?
- What does designing for agent-invoked capability look like when there is no screen — is there a design artifact for a capability contract?
- Does the explicit-contract path win over the automation path, or do both persist with the automation path doing most of the work?
