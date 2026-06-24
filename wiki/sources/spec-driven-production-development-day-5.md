---
type: source
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [spec-driven-development, vibe-coding, production-grade, agentic-engineering, bdd, mcp, zero-trust, team-process, google-agentic-series]
source_path: raw/Spec-Driven-Production-Grade-Development-Day-5.pdf
authors: [Lee Boonstra]
sources: []
ingest_level: deep
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.85
---

# Day 5 — Spec-Driven Production-Grade Development in the Age of Vibe Coding (Boonstra, 2026)

**Author:** Lee Boonstra (reviewers incl. Elia Secchi, Antonio Gulli) — Google "Agentic Engineering" whitepaper series, **Day 5**
**Published:** May 2026 (38 pp)
**Subtitle:** "The Blueprint for Scalable Workflows and Team Evolution: From Vibe Prototypes to Production Reality"
**Raw file:** [[raw/Spec-Driven-Production-Grade-Development-Day-5.pdf|Spec-Driven-Production-Grade-Development-Day-5.pdf]]
**Series companions:** [[sources/the-new-sdlc-with-vibe-coding-day-1|Day 1 — New SDLC]] · [[sources/agent-tools-interoperability-day-2|Day 2 — Tools & Interoperability]] · [[sources/agent-skills-day-3|Day 3 — Agent Skills]] · [[sources/vibe-coding-agent-security-evaluation-day-4|Day 4 — Security & Evaluation]]

## Citation

Boonstra, L. (2026, May). *Spec-Driven Production-Grade Development in the Age of Vibe Coding* (Agentic Engineering series, Day 5). Google. PDF preserved at `raw/Spec-Driven-Production-Grade-Development-Day-5.pdf`.

## Summary

The series finale. Its slogan: **"Vibe Coding is not Vibe in Production."** AI coding agents (e.g. Antigravity, Gemini CLI) now use tools and execute tasks, churning out a thousand documented lines fast — "a legion of interns who never sleep." But this is the **"Illusion of Speed"**: AI also generates mistakes at unprecedented rate, and when an agent **hallucinates** it produces "a thousand lines of *vibe-consistent* but functionally broken logic." The bottleneck doesn't vanish — it **shifts downstream to the humans who must review and integrate** (reviewers "drowning in a sea of AI-generated PRs"). The paper's answer is **Spec-Driven Development (SDD)** plus team-process evolution and a **zero-trust safety net** to get from vibe prototypes to production-grade reliability.

Core mindset shift: from **Code-First** to **spec-first**, where the developer is a **technical architect**, not a typist — and **"code is now disposable"**: with a rock-solid spec you can regenerate the whole codebase (even flip Python→JavaScript in an afternoon), so there's no emotional attachment to it. The spec is the **"Architectural North Star"** and **single source of truth** for humans and AI, preventing **"context fragmentation"** (the AI playing "telephone" with stale file snapshots).

## Key Claims

- **Spec-Driven Development (SDD):** most time now goes into writing high-quality specs (requirements, DB schemas, API contracts), stored as Markdown/YAML in a `specs/` folder, checked into version control as the source of truth. Give the agent a **blueprint, not a vibe** — a "vibe" makes the brain *guess*, and "guessing is how Rogue Agent incidents occur."
- **Format matters (the "format tax"):** cites Ouyang et al. (2026), "SkCC," finding LLM agents are extremely sensitive to instruction format — up to a **40% performance drop** with generic Markdown. Best for Gemini: **hybrid Markdown + conditional YAML** (Markdown headers anchor attention; switch to YAML for structured config nested > 3 deep). Parsing accuracy for deeply-nested config: **YAML 51.9% vs JSON 43.1% vs XML 33.8%.** Tokenization is a hard physical constraint — every char/newline/indent costs budget + latency, so treat `/specs` as a lean, compiled instruction set.
- **Behaviour-Driven Development (BDD):** use **Gherkin** (`Scenario / Given / When / Then`) to force *State → Action → Outcome*, turning vague ideas into precise, guess-free specs.
- **Where instructions live (a hierarchy):** ephemeral **Chat** (orchestration) → versioned **`specs/`** folder (technical design, BDD, schemas) → **Agent Skills** (`.agent/skills/.../SKILL.md`, reusable trigger-based workflows) → **System Prompts** (global `~/.gemini/GEMINI.md`, shared cross-tool **`AGENTS.md`**, project `GEMINI.md`); files are concatenated hierarchically (global → local).
- **Different prompts for different jobs (execution modes):** Project Generation = *Architect* ("No YOLO mode" — propose structure/stack first); Feature Generation = *Builder* (match existing style, review the **Diff**); Bug Fixing = *Forensic Specialist* (**Evidence Prompting** with logs, not Symptom Prompting; reproduce with a failing test first; fix root cause only); Documentation = *Author* (docs as source of truth; Google-style docstrings/JSDoc); Data Engineering = *Librarian* (always show the SQL). Built-in browser (Antigravity) runs an **isolated sandbox Chrome** for autonomous E2E/visual testing.
- **MCP = "USB-C for AI tools":** build one MCP server (e.g. ~40 lines exposing a SQLite DB, SELECT-only guarded) and any MCP-compatible agent can use it without a custom integration.
- **Team culture & process evolution:** AI-aware **code reviews** and **sustainability** of the workflow as you scale from solo experiments to team production.
- **Zero-Trust Development (the safety net):** Guardrails, Sandboxing, Human-in-the-Loop, **AI-Generated Test Coverage** (use the freed-up capacity to write more tests than a human could), Evaluation, a **Policy Server**, and **Context Hygiene & Prompt Sanitization**.

## Useful Examples

- **"Code is disposable"** — regenerate from the spec; flip a project's language in an afternoon; no fear of trashing and restarting.
- **The Markdown + YAML hybrid spec** with the SkCC parsing-accuracy numbers — a concrete, copyable instruction-authoring rule.
- **Gherkin BDD scenarios** as the anti-vibe spec format.
- **The instruction hierarchy** (Chat → `specs/` → `.agent` Skills → `GEMINI.md`/`AGENTS.md`) as a reusable map of "where do my AI instructions go."
- **Evidence Prompting** for debugging (paste the actual error logs / the request flow), not "the button doesn't work."
- **~40-line SQLite MCP server** as a minimal working integration.
- **Tip:** draft technical designs in Google Docs for human review *first*, then export to Markdown into `specs/` — catch logic flaws before the AI generates thousands of broken lines.

## Constraints / Caveats

- **Google vendor whitepaper**, Gemini/Antigravity-centric (GEMINI.md, Antigravity browser, Gemini CLI). Principles transfer across tools, but examples are Google-flavoured.
- Forward-looking best-practice guide, not an empirical study; the SkCC 40% / 51.9% figures come from a single cited 2026 paper — verify before quoting as established.
- **Capture depth:** SDD, format, BDD, instruction hierarchy, execution modes, and MCP captured in detail; team-culture, code-review, sustainability, and the zero-trust components captured at section level — deepen on demand for `coverage: full`.

## Design Implications

- **"Vibe coding ≠ vibe in production"** is the one-line takeaway: AI prototypes are a starting point, production needs specs + review + a safety net (echoes Atlassian's "looks on-brand, but production-quality code at scale is still hard" in [[sources/atlassian-ai-prototyping-handshakes|Day-4-adjacent Atlassian piece]]).
- The **instruction hierarchy** and **format rules** are directly usable when you author context for *any* AI tool — pairs with [[concepts/infrastructure-dev/agentic-content|Agentic Content]] and [[concepts/infrastructure-dev/design-md|DESIGN.md]].
- **AI-generated test coverage as the new safety budget** connects to [[sources/fowler-sensors-coding-agents|Böckeler's sensors]] (coverage ≠ effectiveness — pair with mutation testing).
- For Bonny: the **spec-as-source-of-truth + "review the design before the AI builds"** discipline maps cleanly onto research/spec-heavy product work, not just code.

## Tensions

- **Speed vs the human review bottleneck** — the "Illusion of Speed": writing fast just makes a bigger pile to review unless you add specs + process.
- **Disposable code vs institutional knowledge** — if code is regenerated at will, the *spec* must hold the knowledge; a weak spec means lost intent.
- **Velocity vs zero-trust friction** — the safety net (guardrails, policy server, HITL) is the Day-5 counterpart to Day-4's security harness.

## Open Questions

- What exactly is in the Policy Server / Context Hygiene section (capture pending)?
- How do AI-aware code reviews scale when most PRs are agent-generated?
- How portable is the GEMINI.md/Antigravity-specific guidance to non-Google stacks?

## Concepts Linked

- [[concepts/ai-agents/spec-driven-development|Spec-Driven Development]] (new)
- [[concepts/ai-agents/zero-trust-agent-development|Zero-Trust Agent Development]] (new)
- [[concepts/ai-agents/agent-skills|Agent Skills]]
- [[concepts/infrastructure-dev/claudemd-context|CLAUDE.md / AGENTS.md Context]]
- [[concepts/infrastructure-dev/agentic-content|Agentic Content]]
- [[concepts/ai-agents/mcp-integration|MCP Integration]]
- [[concepts/ai-agents/vibe-coding|Vibe Coding]]
- [[concepts/ai-agents/agentic-ai|Agentic AI]]
- [[concepts/ai-agents/harness-engineering|Harness Engineering]]
- [[concepts/infrastructure-dev/maintainability-sensor|Maintainability Sensor]]
- [[concepts/infrastructure-dev/token-efficiency|Token Efficiency]]
- [[concepts/ux-research/human-in-the-loop|Human-in-the-Loop]]
- [[concepts/ai-agents/context-rot|Context Rot]]

## LLM Use

- **Use for:** moving AI prototypes to production-grade work; authoring specs (SDD, BDD/Gherkin, Markdown+YAML format rules, the instruction hierarchy); choosing the right "execution mode" per task; minimal MCP server design; the zero-trust safety-net checklist.
- **Do not use for:** quoting the SkCC percentages as settled fact (single cited study); assuming the Gemini/Antigravity-specific files apply verbatim elsewhere; the detailed policy-server mechanics (not fully captured).
- **Best prompt pattern:** "Using Day-5 SDD, turn this vague feature idea into a production-grade spec: write the BDD (Gherkin) scenarios, the Markdown+YAML structure, where each instruction should live (chat / specs / skill / GEMINI.md), and the zero-trust safety net it needs before shipping."

## Reliability Notes

> [!warning] Caveats
> - **Vendor (Google) best-practice whitepaper**, Gemini/Antigravity-centric, May 2026. Confidence 0.85 on the SDD discipline and patterns; the cited SkCC metrics are from one paper.
> - First half (SDD/format/BDD/MCP/execution modes) captured deeply; team-process + zero-trust sections at section level (`coverage: substantial`).

## Backfill Status

- Newly written 2026-06-22 from the PDF (read SDD/format/BDD/MCP/execution-mode sections in detail + TOC for the rest). PDF preserved in `raw/`. Completes the Day 1–5 Agentic Engineering series. Deepen the zero-trust/policy-server section for `coverage: full`.
