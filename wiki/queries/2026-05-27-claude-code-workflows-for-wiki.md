---
type: query
status: active
created: 2026-05-27
updated: 2026-06-26
tags: [query]
sources: [sources/yozm-obsidian-llm-wiki-secondbrain, sources/lennys-podcast-cat-wu-ai-pm-claude-code, sources/agent-skills-day-3, sources/brunch-ponyodesign-llm-wiki-clone, sources/yozm-tiro-ax-ontology, sources/maily-product-makers-planning-harness, sources/heyratel-ios-ai-agent-environment]
confidence: 0.78
---

# Query: claude code workflows for wiki

## Short Answer

The workflows that best support this vault are the ones the wiki's own architecture is built on: a small set of Claude Code skills running over an immutable-raw → AI-maintained-wiki split, governed by an always-loaded instruction file. The blueprint this vault implements ([[sources/yozm-obsidian-llm-wiki-secondbrain|Gom's IT Blog]]) names three core skills — **/ingest** (turn raw material into linked pages), **/lint** (daily checks for broken links, orphan pages, sensitive data), and **/query** (contextual Q&A over the whole wiki) — backed by Obsidian + GitHub + the Claude Code CLI. Treat that loop as [[concepts/ai-agents/harness-engineering|harness engineering]]: control comes from designing the environment (a tight [[concepts/infrastructure-dev/claudemd-context|CLAUDE.md/AGENTS.md]], well-scoped [[concepts/ai-agents/agent-skills|Agent Skills]], readiness metadata) rather than from re-prompting each session. Two governance disciplines matter most: keep irreversible/judgment steps human-gated ([[concepts/ai-agents/criteria-driven-ai-adoption|criteria-driven adoption]] — "automate mechanical waste, not judgment"), and let the workflow improve itself by capturing feedback into rules and skills ([[concepts/ai-agents/self-improving-agent-workflows|self-improving workflows]]). Because models change, periodically revisit which scaffolding is still needed ([[concepts/ai-agents/model-harness|model harness]]). The wiki is well-evidenced on the *shape* of these workflows; it is thinner on operational specifics (exact skill definitions, Obsidian plugin choices, measured outcomes), so those remain open.

## Evidence

- [[sources/yozm-obsidian-llm-wiki-secondbrain|Gom's IT Blog: Obsidian LLM Wiki second brain]] — the blueprint this vault implements: the **/ingest /lint /query** triad on **Obsidian + GitHub private repo + Claude Code CLI**, with a Chrome/share-sheet capture inbox and regex sensitive-data masking; core advice is "don't chase a perfect structure — improve incrementally."
- [[concepts/infrastructure-dev/llm-wiki|LLM Wiki]] — the three layers (immutable raw, AI-maintained wiki, schema) and the three main workflows (ingest, query, lint) that compile sources into linked notes at ingest time instead of retrieving fragments at question time.
- [[concepts/ai-agents/ai-maintained-wiki|AI-Maintained Wiki]] — the practical contract: humans provide sources, goals, and review; the agent maintains `wiki/`; raw stays in `raw/`; the instruction file governs behavior.
- [[maps/llm-wiki-architecture|LLM Wiki Architecture]] — the 7-step flow (human points to source → agent preserves raw → writes honest source records → links into concepts/maps/methods → grounds synthesis in `llm_ready: true` sources → escalates to raw for any final claim → maintenance scripts refresh readiness maps and change logs).
- [[concepts/ai-agents/claude-code|Claude Code]] — the CLI is framed as the earliest and most powerful surface for this work; product evolution ties to model capability, harness design, verification, and parallel agent tasks.
- [[concepts/ai-agents/agent-skills|Agent Skills]] — the portable `SKILL.md` primitive (one skill, one job; the description is the routing interface; version and review skills like dependencies) is the right unit for recurring vault workflows; load on demand via progressive disclosure.
- [[comparisons/skills-vs-mcp-vs-agents-md|Skills vs MCP vs AGENTS.md vs DESIGN.md]] — routing guidance: project-wide always-on rules belong in AGENTS.md/CLAUDE.md; repeatable workflows belong in Skills; a poorly-scoped Skill can *subtract* capability, so the discipline lives in descriptions and evals.
- [[concepts/infrastructure-dev/claudemd-context|CLAUDE.md / AGENTS.md Context]] — instruction files solve the "amnesia" problem: they inject durable conventions and operating rules into every session so the agent behaves consistently (exactly this vault's `CLAUDE.md`/`AGENTS.md` contract).
- [[concepts/ai-agents/harness-engineering|Harness Engineering]] — frame the whole maintenance loop as designing the environment, constraints, and feedback loops; control via environment design, observability, and guardrails rather than micromanaging the model.
- [[concepts/ai-agents/model-harness|Model Harness]] — new model launches should trigger a review of prompts and "product crutches"; stronger models can unlock richer behavior (e.g. better review), so prune scaffolding the model no longer needs.
- [[concepts/infrastructure-dev/knowledge-linting|Knowledge Linting]] — the maintenance pass behind `/lint`: broken links, orphan pages, duplicated concepts, unsourced claims, stale/superseded claims, and recurring terms missing a concept page.
- [[concepts/ai-agents/self-improving-agent-workflows|Self-Improving Agent Workflows]] — capture feedback from review so the same mistake does not recur; anything the agent authors enters at the **draft** tier, with a human in the loop for early edits — don't start with meta-skills before manual authoring works.
- [[concepts/ai-agents/criteria-driven-ai-adoption|Criteria-Driven AI Adoption]] — "the standard chooses the tools": automate proven, repeated waste, keep irreversible decisions (commits, merges, approvals) human-gated, and treat context as a budget (keep it small and clean).
- [[concepts/product-management/planning-harness|Planning Harness]] — a concrete repo-shareable harness recipe (rules file + custom skills + reference spec) showing the 10-minute setup and the four principles: context, tool definition, guardrails, validation.
- [[concepts/product-management/compounding-knowledge|Compounding Knowledge]] — the payoff: each new source improves the existing wiki instead of being a one-off upload, so the understanding spent on a source is preserved and reused.
- [[sources/lennys-podcast-cat-wu-ai-pm-claude-code|Lenny's Podcast: Cat Wu on AI-Native Product Management]] — Claude Code as daily work infrastructure; eval-driven development, revisiting harnesses as models improve, and moving from one task to many parallel tasks with verification and feedback.
- [[sources/brunch-ponyodesign-llm-wiki-clone|ponyodesign: LLM Wiki clone]] — independent practitioner echo: human captures, AI structures/links/summarizes; minimizing capture friction matters more than a clever model ("Obsidian is the IDE, AI is the programmer, the wiki is the codebase").

## Reusable Notes

- The minimal, evidence-backed workflow set for this vault is **three skills over a raw→wiki split, governed by an instruction file**: `/ingest`, `/lint`, `/query` ([[concepts/ai-agents/ai-maintained-wiki|AI-Maintained Wiki]] + [[concepts/infrastructure-dev/llm-wiki|LLM Wiki]]). Everything else (parallel subagents, meta-skills) is an optimization layered on top once the basic loop is reliable.
- Encode durable rules in [[concepts/infrastructure-dev/claudemd-context|CLAUDE.md/AGENTS.md]] (always loaded) and recurring procedures as [[concepts/ai-agents/agent-skills|Agent Skills]] (loaded on demand); a vague skill description is the main failure mode ([[comparisons/skills-vs-mcp-vs-agents-md|routing comparison]]).
- Keep humans on the irreducible loop — review, sensitive-data approval, and "what's worth automating" — per [[concepts/ai-agents/criteria-driven-ai-adoption|criteria-driven adoption]]; let agent-authored content enter at the draft tier per [[concepts/ai-agents/self-improving-agent-workflows|self-improving workflows]]. This directly mirrors how this very tombstone is being regenerated under human-defined rules.

## Follow-up Sources Needed

- Verbatim **skill definitions** for `/ingest`, `/lint`, `/query` (and the exact Obsidian plugin list) — the blueprint source is at `coverage: substantial`, so the precise contract is not yet captured ([[sources/yozm-obsidian-llm-wiki-secondbrain|Gom's IT Blog backfill note]]).
- **Measured outcomes / break-even data** for harness-style workflows — current sources (planning harness, criteria-driven adoption, the ponyodesign clone) are qualitative practitioner accounts with no metrics, so claims about payoff stay unproven.
- An **Obsidian-plugin-after-stable-workflow** source — flagged as missing in [[concepts/infrastructure-dev/llm-wiki|LLM Wiki]]'s open questions (which plugins to enable once the basic loop works), requiring plugin-ecosystem knowledge not yet collected.
