---
type: concept
status: active
created: 2026-06-22
updated: 2026-07-24
tags: [concept, spec-driven-development, bdd, vibe-coding, production-grade, instruction-format, change-brief]
sources: [spec-driven-production-development-day-5, spec-driven-development-exit-strategy]
confidence: 0.7
---

# Spec-Driven Development (SDD)

> [!abstract] Summary
> A workflow where developers write a high-quality **specification** (the single source of truth) and AI agents generate code from it. The developer becomes a **technical architect**, the spec is the **"Architectural North Star,"** and **"code is disposable"** — with a solid spec the codebase can be regenerated at will.

> [!important] Why it Matters
> **"Vibe coding is not vibe in production."** Giving an agent a "vibe" instead of a "blueprint" makes it *guess* — and guessing is how "Rogue Agent" incidents happen. A version-controlled spec prevents **context fragmentation** (the AI playing "telephone" with stale file snapshots) and shifts the scarce human effort from typing to designing.

## 📝 Key Claims
- Specs live in a version-controlled **`specs/` folder** (Markdown/YAML), as the source of truth for humans and AI.
- **Format is a performance lever:** LLM agents are extremely format-sensitive (up to ~40% drop with generic Markdown — SkCC, Ouyang et al. 2026). Best for Gemini: **hybrid Markdown + conditional YAML** (YAML for config nested > 3; YAML 51.9% vs JSON 43.1% vs XML 33.8% parsing accuracy). Tokenization is a hard cost/latency constraint.
- **Behaviour-Driven Development (BDD)** via **Gherkin** (`Given / When / Then`) forces *State → Action → Outcome*, eliminating ambiguity.
- **Instruction hierarchy:** ephemeral Chat → `specs/` → Agent Skills (`.agent/.../SKILL.md`) → System Prompts (`GEMINI.md` global/project, shared cross-tool `AGENTS.md`).
- **Different execution modes per job:** Architect (generate), Builder (feature), Forensic (bug-fix via Evidence Prompting), Author (docs), Librarian (data).

## 🔗 Related Concepts
- [[wiki/concepts/infrastructure-dev/agentic-content|Agentic Content]]
- [[wiki/concepts/infrastructure-dev/claudemd-context|CLAUDE.md / AGENTS.md Context]]
- [[wiki/concepts/infrastructure-dev/design-md|DESIGN.md]]
- [[wiki/concepts/ai-agents/agent-skills|Agent Skills]]
- [[wiki/concepts/ai-agents/prd-generation|PRD Generation]]
- [[wiki/concepts/ai-agents/planning-to-code-workflow|Planning-to-Code Workflow]]
- [[wiki/concepts/ai-agents/zero-trust-agent-development|Zero-Trust Agent Development]]
- [[wiki/concepts/ai-agents/change-brief|Change Brief]] — the counter-proposal
- [[wiki/concepts/ai-agents/interview-first-elicitation|Interview-First Elicitation]] — how the spec gets written in the first place

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> "Code is disposable" only holds if the spec truly captures intent — a weak spec means lost knowledge. The format metrics come from a single cited 2026 paper (SkCC), and the guidance is Gemini/Antigravity-centric.

> [!danger] Directly contradicted (2026-07-24)
> [[wiki/sources/spec-driven-development-exit-strategy|Eisele (2026)]] inverts **both** core claims on this page:
>
> | This page holds | Eisele holds |
> |---|---|
> | The spec is the source of truth ("Architectural North Star") | The **code** is the primary fact — "code is actual behavior" |
> | "Code is disposable" | The **spec** is disposable; it should expire at release |
> | Specs live durably in a version-controlled `specs/` folder | Accumulated specs become "a second codebase with weaker tooling" |
>
> **Not merged — both positions stand recorded.** The most likely reconciliation is *scope*: this page describes greenfield generate-from-spec work, while Eisele describes evolving an existing production system. The live disagreement is over which case is typical. Eisele's proposed replacement is the [[wiki/concepts/ai-agents/change-brief|Change Brief]] — delta-scoped, expiring, with durable facts migrated into schemas, tests and policies.
>
> Confidence on this page lowered 0.8 → 0.7 pending resolution.

## 📚 Sources
- [[wiki/sources/spec-driven-production-development-day-5|Day 5 — Spec-Driven Production-Grade Development]]
- [[wiki/sources/spec-driven-development-exit-strategy|Eisele (2026): Spec-Driven Development Needs an Exit Strategy]] *(contra)*
- [[wiki/sources/claude-code-interview-first|AX LABS (2026): Let Claude Code Interview You]] *(elicitation front-end)*

## ❓ Open Questions
- How do teams keep specs and regenerated code in sync at scale?
- Does "disposable code" hold for large legacy systems, or only greenfield?
- Which is the typical case — greenfield generation or production evolution? This determines which of the two contradictory positions above should govern.
