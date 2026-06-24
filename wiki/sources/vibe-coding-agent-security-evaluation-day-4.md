---
type: source
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [vibe-coding, agent-security, agent-evaluation, harness-engineering, mcp-security, zero-trust, observability, agentic-engineering, google-agentic-series]
source_path: raw/Vibe-Coding-Agent-Security-and-Evaluation-Day-4.pdf
authors: [Sokratis Kartakis, Aron Eidelman, Wafae Bakkali, Meltem Subasioglu]
sources: []
ingest_level: deep
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.85
---

# Day 4 — Vibe Coding Agent Security and Evaluation (Kartakis et al., 2026)

**Authors:** Sokratis Kartakis, Aron Eidelman, Wafae Bakkali, Meltem Subasioglu (content contributors incl. Antonio Gulli; curator Anant Nawalgaria) — Google "Agentic Engineering" whitepaper series, **Day 4**
**Published:** May 2026 (41 pp)
**Raw file:** [[raw/Vibe-Coding-Agent-Security-and-Evaluation-Day-4.pdf|Vibe-Coding-Agent-Security-and-Evaluation-Day-4.pdf]]
**Series companions:** [[sources/the-new-sdlc-with-vibe-coding-day-1|Day 1 — New SDLC]] · [[sources/agent-tools-interoperability-day-2|Day 2 — Tools & Interoperability]] · [[sources/agent-skills-day-3|Day 3 — Agent Skills]] · [[sources/spec-driven-production-development-day-5|Day 5 — Spec-Driven Development]]

## Citation

Kartakis, S., Eidelman, A., Bakkali, W., & Subasioglu, M. (2026, May). *Vibe Coding Agent Security and Evaluation* (Agentic Engineering series, Day 4). Google. PDF preserved at `raw/Vibe-Coding-Agent-Security-and-Evaluation-Day-4.pdf`.

## Summary

The security-and-evaluation instalment of the Agentic Engineering series. Its premise: software is shifting "from writing code to expressing intent," along a spectrum from casual **vibe coding** (accept whatever the AI generates) to disciplined **agentic engineering** (AI as an implementation engine inside constraints). This high-velocity, non-deterministic style "shatters traditional paradigms of trust," so the paper redefines trust across **two axes**:

- **Security** — *did the agent stay inside the boundary?* (operate safely, no malicious intent)
- **Evaluation** — *is what happened inside the boundary actually worth shipping?* (quality, efficiency, alignment)

A key framing: **"a raw AI model is not an agent. It only becomes one when wrapped in a harness"** — so securing agents means securing the harness, not just code syntax. Static identity is a poor perimeter; trust must be **continuously earned** ("Effective Trust" across supply chain, identity, runtime behaviour, and contextual associations), shifting from **Identity-as-a-Perimeter (RBAC)** to **Context-as-a-Perimeter**. The security half is organised as a layered defence-in-depth on a **7-pillar baseline**; the evaluation half argues why vibe-coding agents need a different ("glass box") evaluation of their internal reasoning.

## Key Claims

- **The 7-Pillar Agent Security Architecture** (the mandatory baseline "safety envelope"):
  1. **Infrastructure & Networking** — ephemeral, kernel-level sandboxes (e.g. gVisor); strict network **egress governance**.
  2. **Data** — CMEK at rest, mTLS in transit, least-privilege scoping; vector-DB **tenant partitioning** to stop **Cross-Tenant Vector Poisoning**.
  3. **Model** — treat system instructions / prompt templates / rule files as the new "source code": sensitive, cryptographically attested artifacts; defend against semantic attacks.
  4. **Application & Runtime** — LLM firewalls for prompt/response filtering, deterministic lifecycle **hooks**, and a **Centralised Agent Gateway** governing Agent-to-Agent (A2A) orchestration to block lateral movement.
  5. **Identity & Access (IAM)** — unique cryptographic agent identities (e.g. **SPIFFE IDs**), **ABAC** + **Just-In-Time (JIT) token downscoping**; a permissions matrix of **Intent × User × Time**.
  6. **Observability & Security Ops** — an autonomous **SecOps triad** (Blue/Red/Green) on OpenTelemetry + Agent Behavioural Analytics.
  7. **Governance** — EU AI Act alignment, Algorithmic Impact Assessments, immutable audit trails binding every action to an agent and its human; replace "approve" buttons with **"Logic Reviews"** (syntax translated back to plain language) + Risk-Stratified Attestation.
- **Vibe-coding-specific defences:**
  - **Ephemeral sandboxing** for the "vibe loop" (write → run → read errors → rewrite); reset state between runs.
  - **Hallucinated-package / "slopsquatting" defence** — LLMs invent package names; attackers pre-publish malware under those names; mitigate via vetted registries, cryptographic version pinning, SBOM + Binary Authorisation gates.
  - **Non-interactive egress** — fetch external data only via offline caches / pre-sanitised crawlers (an allowlist can't stop indirect prompt injection in third-party pages).
  - **Frontend-trust + open-backend failure modes** — AI dumps API keys / session flags into the client and skips default-deny (e.g. row-level) controls. Reconcile via **advisory linters in the IDE + hard enforcement (SAST/SCA) in CI/CD** ("shift left" without IDE hard-blocks).
  - **MCP Spoofing & Contextual Authorisation** — a forged MCP server can inject payloads; a runtime LLM firewall + Agent Gateway verify the call matches the developer's intent.
  - **Confused Deputy / Zero Ambient Authority** — an over-privileged agent tricked by injected instructions; give the agent a *distinct agentic identity* (not the human's delegated creds), JIT-downscoped, file-tree allowlists, deny-by-default.
  - **High-stakes actions** need elicitation / MFA / a **"Vibe Diff"** rather than simple approve-deny (the "It Works, Ship It" fallacy).
  - **Red/Blue/Green agent teaming** — Red (attacker, injects adversarial vibes), Blue (defender, behavioural analytics), Green (fixer, stateful quarantine + auto-refactoring); enforce small batch sizes.
  - **Observability of the "Vibe Trajectory"** — measure **Intent Drift** and **Trust Decay**; use checkpoints and **stateful circuit breakers**.
- **Evaluation half:** vibe-coding agents can pass every security check yet misread intent, ignore conventions, or silently degrade UX. Evaluation must open the "glass box" to measure the quality/efficiency/alignment of the agent's *reasoning*, with observability as a prerequisite (what to evaluate, how to evaluate, applied tips).

## Useful Examples

- **"Slopsquatting"** (Wiz's term) — the canonical agentic supply-chain attack: malware published under hallucinated package names.
- **The Confused Deputy via pasted repo content** — a malicious instruction hidden in an open-source repo a developer pastes into the IDE context window.
- **"Vibe Diff" + Logic Reviews** — translating opaque generated syntax back into plain language before a human approves a high-stakes action.
- **Red/Blue/Green triad** as a concrete operating model for autonomous SecOps.
- **Intent × User × Time** permissions matrix and JIT-downscoped, self-expiring tokens.

## Constraints / Caveats

- **Google vendor whitepaper / forward-looking framework.** High craft and concrete, but it's a prescriptive 2026 reference architecture, not an independent evaluation or field study — treat as a strong design framework, not evidence of outcomes.
- **Capture depth:** the **security half** (7 pillars + vibe-coding specifics) is captured in detail; the **evaluation half** (what/how to evaluate) is captured at section/framing level — deepen on demand for `coverage: full`.
- Tooling references (gVisor, SPIFFE, OpenTelemetry, Binary Authorisation) are illustrative; principles transfer, specific tools may not.

## Design Implications

- The **two-axis split (Security = stayed in bounds / Evaluation = worth shipping)** is a clean mental model for governing *any* non-deterministic AI feature — not just coding agents.
- For Bonny (non-engineering): the **"Logic Reviews instead of approve buttons"** and **"glass box" evaluation of reasoning** ideas apply directly to how teams review and trust AI output in research/product workflows.
- Reinforces the series' core: an AI model becomes a trustworthy agent only via the **harness** — pair with [[concepts/ai-agents/harness-engineering|Harness Engineering]] and [[sources/bayer-prince-reliable-agentic-ai|the Bayer PRINCE case study]].

## Tensions

- **Velocity vs control** — the whole paper is about reconciling vibe-coding speed with enterprise safety; e.g. **IDE friction vs CI/CD enforcement** (don't hard-block in the IDE; enforce in the pipeline).
- **"It compiles, ship it" vs Logic Reviews** — compiling code feels safe but can have bypassed backend controls.
- Mirrors the [[sources/fowler-sensors-coding-agents|sensors article]] (code-quality side) and [[sources/bayer-prince-reliable-agentic-ai|PRINCE]] (system side) as the *security* corner of the same harness-engineering triangle.

## Open Questions

- What does the evaluation half prescribe in detail (metrics, rubrics) for "is this worth shipping"? (Capture pending.)
- How much of the 7-pillar architecture is realistically adoptable outside a hyperscaler context?
- How are "Intent Drift" and "Trust Decay" actually measured in production?

## Concepts Linked

- [[concepts/ai-agents/agent-security-architecture|Agent Security Architecture]] (new — the 7-pillar / Context-as-a-Perimeter / Effective Trust model)
- [[concepts/ai-agents/red-blue-green-agent-teaming|Red/Blue/Green Agent Teaming]] (new)
- [[concepts/ai-agents/vibe-coding-agent-evaluation|Vibe-Coding Agent Evaluation]] (new)
- [[concepts/ai-agents/slopsquatting|Slopsquatting]] (new)
- [[concepts/ai-agents/harness-engineering|Harness Engineering]]
- [[concepts/ai-agents/model-harness|Model Harness]]
- [[concepts/ai-agents/mcp-integration|MCP Integration]]
- [[concepts/ai-agents/agentic-ai|Agentic AI]]
- [[concepts/ai-agents/vibe-coding|Vibe Coding]]
- [[concepts/infrastructure-dev/cloud-ai-governance|Cloud AI Governance]]
- [[concepts/infrastructure-dev/agentic-technical-debt|Agentic Technical Debt]]
- [[concepts/ai-agents/product-evals|Product Evals]]

## LLM Use

- **Use for:** designing a security/evaluation harness for agentic / vibe-coding systems; the 7-pillar checklist; agentic supply-chain (slopsquatting), MCP-spoofing, Confused-Deputy, and zero-ambient-authority threat models; the Security-vs-Evaluation framing; Red/Blue/Green SecOps.
- **Do not use for:** claiming measured security outcomes; treating the named tools as the only valid stack; the detailed evaluation metrics (not fully captured here).
- **Best prompt pattern:** "Using the Day-4 two-axis model, audit this agentic feature: (Security) which of the 7 pillars are covered vs missing; (Evaluation) what 'worth-shipping' criteria and observability we lack — and propose the minimal harness to close the top gaps."

## Reliability Notes

> [!warning] Caveats
> - **Vendor (Google) reference architecture**, May 2026. Confidence 0.85 on the framework and threat models (concrete and well-structured); it is prescriptive, not an outcome study.
> - Security half captured deeply; evaluation half at framing level (`coverage: substantial`).

## Backfill Status

- Newly written 2026-06-22 from the PDF (read security half end-to-end + evaluation TOC/intro). PDF preserved in `raw/`. Completes the Agentic Engineering series alongside Day 5. Deepen the evaluation section for `coverage: full`.
