---
type: concept
status: active
created: 2026-06-17
updated: 2026-06-17
tags: [agent-skills, skill-format, procedural-memory, progressive-disclosure, agentic-engineering]
sources:
  - sources/agent-skills-day-3
  - sources/the-new-sdlc-with-vibe-coding-day-1
confidence: 0.9
---

# Agent Skills

> [!abstract] Summary
> An Agent Skill is a folder anchored by a `SKILL.md` file (YAML frontmatter + markdown body) plus optional `scripts/`, `references/`, and `assets/` — a portable, vendor-neutral primitive that gives a general-purpose agent on-demand specialist competence without bloating its context window.

> [!important] Why it Matters
> Skills are the first credible **procedural memory** primitive for LLM agents and have become the durable unit of capability improvement once foundation models commoditize. The format is settled (open standard at `agentskills.io`, adopted by every major coding agent, AI chatbot, and agent framework); the engineering work is now around evaluation, composition, and governance.

## 📝 Key Claims

- A Skill is a *folder*, not just a file. `SKILL.md` is mandatory; `scripts/`, `references/`, and `assets/` are optional and load on demand.
- Skills load via [[concepts/ai-agents/progressive-disclosure|Progressive Disclosure]]: metadata always in context (~50 tokens/skill), body on trigger (~2,000 tokens), bundled resources only when referenced.
- Skills emerge from two paths: (Path A) subject-matter experts translating institutional knowledge they already have; (Path B) crystallizing successful agent trajectories into reusable workflows.
- A Skill teaches *know-how*; an MCP server provides *reach*. When a Skill needs data it calls a tool — typically one provided by an MCP server. They compose; they don't compete (see [[comparisons/skills-vs-mcp-vs-agents-md|Skills vs MCP vs AGENTS.md]]).
- **AGENTS.md is always loaded; Skills load on demand.** Vercel's production analysis found AGENTS.md hit 100% pass rate against a 53% baseline, while a poorly-designed Skill *subtracted* 5 percentage points of capability. Skills are for narrow action-specific workflows; global context belongs in AGENTS.md.
- The description field is the routing algorithm — the only thing the model sees during selection. Spend disproportionate authoring effort there.
- The right naming convention is snake_case directory, kebab-case skill name, gerund form (`managing-databases`, not `database-manager`). Avoid generic names (`utils`, `tools`) and vendor prefixes (`claude-*`).
- Skills are *conditional* (loaded on description match), *composable* (one Skill can call tools belonging to another), and *owned* (each lives in a versioned folder with a named author).
- By early 2026, public marketplaces had crossed 40,000 listings. Trust defaults differ by source: first-party (trust by default, pin), org-curated (trust within org, review on adoption), community (audit before adopting, pin aggressively).

## Minimal SKILL.md template

```yaml
---
name: skill-name
description: |
   [What it does in one verb-led sentence.] Use this skill when the user
   [trigger phrase 1], [trigger phrase 2], or [trigger phrase 3].
   Do NOT use for [anti-trigger 1] or [anti-trigger 2].
version: 1.0.0
license: MIT
allowed-tools: [Optional] Read Bash Write
metadata:
   author: your-handle
---

# Skill Name

## When to use
- [Concrete scenario]
- [Concrete scenario]

## When NOT to use
- [Out-of-scope scenario]

## Workflow
1. [Step]
2. [Step]
3. See `references/advanced.md` for [edge case].
```

## The five rules

1. **One skill, one job.** If you cannot describe what it does in one sentence, it is two skills.
2. **Descriptions are an interface.** A vague description means an unused skill.
3. **Skills are dependencies.** Version them, pin them, review them in PRs. A skill without a test is a hope, not a capability.
4. **The right team owns the right skill.** Domain experts own domain skills; don't bottleneck through the AI team.
5. **The agent runtime is interchangeable.** Portability is part of the value — don't tie skills to one runtime.

## Skill smells (revise if you see these)

- Over 5,000 words — probably two skills, or reference material that belongs in `references/`.
- Two domain teams could plausibly own it — split along team boundaries.
- You cannot write three test cases for it — description is too vague.
- It references no other resource — might be a long instruction that belongs in the system prompt.
- You keep adding "edge cases" sections — each edge case probably wants its own skill.
- Description starts with "a helpful skill for..." — rewrite. Name the trigger, inputs, and output.

## 🔗 Related Concepts

- [[concepts/ai-agents/progressive-disclosure|Progressive Disclosure]] — the 3-level loading mechanism that makes Skills viable.
- [[concepts/ai-agents/procedural-memory|Procedural Memory]] — the LLM memory typology Skills fill.
- [[concepts/ai-agents/context-rot|Context Rot]] — the failure mode Skills are designed to defeat.
- [[concepts/ai-agents/skill-system|Skill System]] — the broader pattern of reusable procedural memory; Agent Skills is its current standard implementation.
- [[concepts/ai-agents/skillopt|SkillOpt]] — text-space optimizer for evolving Skill documents.
- [[concepts/ai-agents/self-improving-agent-workflows|Self-Improving Agent Workflows]] — meta-skills that author, evaluate, and improve other skills.
- [[concepts/ai-agents/agent-memory|Agent Memory]]
- [[concepts/ai-agents/mcp-integration|MCP Integration]] — the Skill calls; the MCP server provides reach.
- [[concepts/infrastructure-dev/claudemd-context|CLAUDE.md / AGENTS.md Context]] — the always-loaded counterpart.
- [[concepts/ai-agents/harness-engineering|Harness Engineering]] — the scaffolding inside which Skills compose.
- [[concepts/infrastructure-dev/agentic-engineering|Agentic Engineering]]
- [[comparisons/skills-vs-mcp-vs-agents-md|Comparison: Skills vs MCP vs AGENTS.md]]

## ⚖️ Conflicts & Caveats

> [!warning] Contradictions
> Vercel's production result that AGENTS.md *outperforms* Skills in some agent evals tempers the broader bullishness on Skills. Resolution: Skills are for narrow action-specific workflows; global project context belongs in AGENTS.md. Mis-applying this split is the predicted failure mode.

> [!warning] Boundary
> Skills do not kill multi-agent architectures. Multi-agent remains correct for genuine parallelism, real capability boundaries (different access / security postures / external systems), hierarchical decomposition, adversarial setups, sub-agent intercommunication, or heterogeneous models.

## 📚 Sources

- [[sources/agent-skills-day-3|Singhal et al. (2026): Agent Skills (Day 3)]] — primary reference.
- [[sources/the-new-sdlc-with-vibe-coding-day-1|Osmani et al. (2026): The New SDLC With Vibe Coding (Day 1)]] — situates Skills inside the static-vs-dynamic-context split.
- [[sources/agent-tools-interoperability-day-2|Patlolla et al. (2026): Agent Tools & Interoperability (Day 2)]] — the MCP companion that Skills call.

## ❓ Open Questions

- Which of Bonny's recurring vault and AOCC AI Hub workflows have strong enough activation cues to make good Skills?
- What is the right central location for a personal Skills library so it works across Claude Code, Codex, Antigravity, and Cursor without per-tool duplication?
- How should the Read/Draft/Act ladder be tightened for skills that touch shared infrastructure (push, deploy, send-message) vs purely local skills?
