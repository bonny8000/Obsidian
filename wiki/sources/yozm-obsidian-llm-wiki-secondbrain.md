---
type: source
status: active
created: 2026-06-25
updated: 2026-06-25
tags: [llm-wiki, second-brain, obsidian, claude-code, knowledge-management, ingest, lint, query]
source_path: raw/web/yozm-obsidian-llm-wiki-secondbrain-2026-06-25.md
source_url: https://yozm.wishket.com/magazine/detail/3792/
authors: [곰씨네 IT 블로그 (Gom's IT Blog)]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.85
---

# Gom's IT Blog (2026): Building an Obsidian-Based LLM Wiki (Second Brain)

**Author:** 곰씨네 IT 블로그 (Gom's IT Blog) — Yozm IT (Wishket), 2026-06-10.
**Raw capture:** [[raw/web/yozm-obsidian-llm-wiki-secondbrain-2026-06-25|yozm-obsidian-llm-wiki-secondbrain-2026-06-25]]
**URL:** [yozm.wishket.com/magazine/detail/3792](https://yozm.wishket.com/magazine/detail/3792/)

> [!important] Meta-source for this vault
> This is the **blueprint article that this LLM-Wiki implements.** The `raw/` → `wiki/` split, the `/ingest` `/lint` `/query` skills, and the **Obsidian + GitHub + Claude Code** stack all trace back to this design. It documents the *why* behind the operating contract in `AGENTS.md` / `CLAUDE.md`.

## Citation

Gom's IT Blog. (2026, June 10). *나만의 세컨 브레인: 옵시디언 기반 LLM 위키 구축기* [My Second Brain: Building an Obsidian-Based LLM Wiki]. Yozm IT (Wishket). Captured 2026-06-25 into `raw/web/yozm-obsidian-llm-wiki-secondbrain-2026-06-25.md`.

## Summary

The author is tired of re-explaining personal context to every AI tool (Claude, ChatGPT, Gemini) because information is scattered across Google Keep, Notion, Workspace, and GitHub — so no AI sees the whole picture. The fix (after Karpathy's "second brain"): one centralized, **AI-maintained LLM Wiki**. Outcome: AI answers shift from generic → **situation-optimized**, reasoning over the user's philosophy, priorities, and constraints at once.

## Key Claims

- **Stack:** **Obsidian** (notes, Minimal theme) + **GitHub private repo** (backup + multi-device sync) + **Claude Code CLI** (maintenance/automation). Plugins: Git sync, Terminal, template/visualization tools.
- **Unified capture** — Chrome web-clipper (desktop) + share sheet (mobile) funnel everything into one inbox (the role this vault's `raw/` plays).
- **Three automation skills:** **/ingest** (material → wiki pages), **/lint** (daily checks for sensitive data, broken links, orphan pages), **/query** (contextual Q&A over the whole wiki).
- **7-category personal-context structure:** Identity, Thoughts, Goals, History, People, Assets, Works.
- **Security layers:** regex sensitive-data masking, 2FA, fine-grained GitHub tokens.
- **Result:** generic → situation-optimized answers; the assistant reasons over philosophy + priorities + constraints simultaneously.
- **Honest limits:** OCR errors on handwriting; growing wiki = more sensitive-info exposure; GitHub compromise = total breach; collaboration needs a *separate* team wiki (breaks single-source-of-truth); Obsidian learning curve.
- **Core advice:** **don't chase a perfect structure from day one — improve incrementally** (avoids abandonment).

## Useful Examples

- The `/ingest` `/lint` `/query` triad as the minimal skill set for an AI-maintained knowledge base (exactly this vault's workflow contract).
- The **raw inbox → compiled wiki** separation as the durability mechanism.
- The 7-category personal schema as a contrast to this vault's research/UX-oriented `wiki/` taxonomy.

## Constraints / Caveats

- Single-author build log, personal-life context — this vault diverges deliberately (research/UX/agentic-engineering focus, source/concept/method/comparison/analysis taxonomy rather than Identity/Thoughts/…).
- No quantified outcomes; "situation-optimized" is qualitative.
- Security model is necessary but not sufficient — the breach surface grows with the corpus (an inherent tension, not solved here).

## Design Implications

- Validates and explains this vault's own architecture: keep [[concepts/infrastructure-dev/llm-wiki|LLM Wiki]] (immutable raw + AI-maintained wiki + schema) and the [[concepts/ai-agents/ai-maintained-wiki|AI-maintained]] `/ingest` `/lint` `/query` loop.
- "Improve incrementally" → treat the wiki taxonomy as evolvable; don't over-design `wiki/` upfront.
- The sensitive-data masking + lint discipline is a direct argument for keeping [[concepts/infrastructure-dev/knowledge-linting|Knowledge Linting]] in the lint workflow.

## Tensions

- **Single-source-of-truth vs. collaboration** — a personal second brain resists being a shared team wiki (the author flags this explicitly).
- **Centralization value vs. breach blast-radius** — the more context you centralize, the worse a compromise.

## Open Questions

- Which of the author's 7 personal categories (if any) are worth importing for Bonny's own-context layer alongside this vault's research focus?
- What's the right boundary between this research/UX vault and a separate personal/team context store?

## Concepts Linked

- [[concepts/infrastructure-dev/llm-wiki|LLM Wiki]]
- [[concepts/ai-agents/ai-maintained-wiki|AI-Maintained Wiki]]
- [[concepts/infrastructure-dev/knowledge-linting|Knowledge Linting]]
- [[concepts/ai-agents/1-person-vault|1-Person Vault]]
- [[concepts/ai-agents/agent-skills|Agent Skills]]
- [[concepts/product-management/compounding-knowledge|Compounding Knowledge]]

## LLM Use

- **Use for:** explaining/justifying this vault's architecture; designing a personal "second brain" (raw inbox + AI-maintained wiki + ingest/lint/query skills + GitHub sync + masking).
- **Do not use for:** quantified productivity claims; collaboration/team-wiki design (the author flags it as out of scope).
- **Best prompt pattern:** "Compare this vault's `AGENTS.md` contract to Gom's blueprint (raw→wiki, /ingest /lint /query, 7 categories) and propose incremental improvements without over-restructuring."

## Reliability Notes

> [!warning] Caveats
> Personal build log, qualitative. Confidence 0.85 as the design rationale for this vault's pattern; not evidence of generalizable outcomes.

## Backfill Status

- New ingest 2026-06-25 from full web_fetch. To reach `full`, capture the verbatim plugin list and exact skill definitions for a closer reconciliation with this vault's contract.
