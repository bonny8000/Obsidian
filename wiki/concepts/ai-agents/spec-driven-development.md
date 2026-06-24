---
type: concept
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [concept, spec-driven-development, bdd, vibe-coding, production-grade, instruction-format]
sources: [spec-driven-production-development-day-5]
confidence: 0.8
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
- [[concepts/infrastructure-dev/agentic-content|Agentic Content]]
- [[concepts/infrastructure-dev/claudemd-context|CLAUDE.md / AGENTS.md Context]]
- [[concepts/infrastructure-dev/design-md|DESIGN.md]]
- [[concepts/ai-agents/agent-skills|Agent Skills]]
- [[concepts/ai-agents/prd-generation|PRD Generation]]
- [[concepts/ai-agents/planning-to-code-workflow|Planning-to-Code Workflow]]
- [[concepts/ai-agents/zero-trust-agent-development|Zero-Trust Agent Development]]

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> "Code is disposable" only holds if the spec truly captures intent — a weak spec means lost knowledge. The format metrics come from a single cited 2026 paper (SkCC), and the guidance is Gemini/Antigravity-centric.

## 📚 Sources
- [[sources/spec-driven-production-development-day-5|Day 5 — Spec-Driven Production-Grade Development]]

## ❓ Open Questions
- How do teams keep specs and regenerated code in sync at scale?
- Does "disposable code" hold for large legacy systems, or only greenfield?
