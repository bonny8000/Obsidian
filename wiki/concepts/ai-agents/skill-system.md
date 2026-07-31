---
type: concept
status: active
created: 2026-05-18
updated: 2026-07-31
tags: [ai-agent, skills, automation, procedural-memory, design-system, lazy-loading]
sources:
  - sources/brunch-ghidesigner-486
  - sources/arxiv-2605-23904
  - sources/agent-skills-day-3
  - karrot-kraft-design-system-agent
confidence: 0.9
---

# Skill System

## Summary

A skill system stores reusable task patterns so an agent can repeat or improve a workflow without rediscovering the same steps every time. The current standard implementation is the [[concepts/ai-agents/agent-skills|Agent Skills]] format (a folder anchored by `SKILL.md`), now an open standard at `agentskills.io` adopted across every major coding agent and AI chatbot.

## Why It Matters

Skills turn one-off agent work into compounding process knowledge — Day-3 frames them as the first credible [[concepts/ai-agents/procedural-memory|procedural memory]] primitive for LLM agents. For design operations or wiki maintenance, a skill might encode how to summarize research, build a prototype, audit UI quality, or maintain the wiki. As foundation models commoditize, *the skill is the unit of capability improvement*.

## Key Claims

- Skills can capture successful procedures, not only facts.
- Skill quality depends on clear inputs, outputs, constraints, and verification steps.
- In an LLM Wiki, skills and source-grounded notes should stay separate: skills say how to work; wiki pages say what is known.
- Skills load via [[concepts/ai-agents/progressive-disclosure|Progressive Disclosure]] — metadata always loaded (~50 tokens/skill), body on trigger, resources on demand. Anthropic published an example where converting a workflow to skills cut active context from ~150K tokens to ~2K (98%+ reduction).
- **A skill without a test is a hope, not a capability.** SkillsBench 2025 found 19% of real-world skills *actively degrade* capability. The four failure modes (Trigger, Execution, Token Budget, Regression) determine the evaluation surface.
- Skills must graduate through tiers of authority: **Read-Only → Draft-Only → Action-Allowed**. Action-allowed requires sustained pass^k, not just a single happy-path pass.
- Skills compose with — they do not replace — MCP servers and AGENTS.md. See [[comparisons/skills-vs-mcp-vs-agents-md|Comparison: Skills vs MCP vs AGENTS.md]].
- A reverse-engineering of Claude Code v2.1.88 found 98.4% of the codebase is operational infrastructure, not agent loop — the durable engineering asset is the Skill library that runs inside that infrastructure.

## Related Concepts

- [[concepts/ai-agents/agent-skills|Agent Skills]] — the standard format implementation of this pattern.
- [[concepts/ai-agents/progressive-disclosure|Progressive Disclosure]] — the loading mechanism.
- [[concepts/ai-agents/procedural-memory|Procedural Memory]] — the memory typology this fills.
- [[concepts/ai-agents/context-rot|Context Rot]] — the failure mode skills defeat.
- [[concepts/ai-agents/autonomous-ai-agent|Autonomous AI Agent]]
- [[concepts/ai-agents/agent-memory|Agent Memory]]
- [[concepts/ai-agents/ai-agent-workflow|AI Agent Workflow]]
- [[concepts/ai-agents/skillopt|SkillOpt]]
- [[concepts/infrastructure-dev/text-space-optimization|Text-Space Optimization]]
- [[concepts/ai-agents/self-improving-agent-workflows|Self-Improving Agent Workflows]]
- [[comparisons/skills-vs-mcp-vs-agents-md|Comparison: Skills vs MCP vs AGENTS.md]]

## Sources

- [[sources/agent-skills-day-3|Singhal et al. (2026): Agent Skills (Day 3)]] — current standard reference for format, evaluation, composition, and governance.
- [[sources/brunch-ghidesigner-486|Hermes Agent AI for Designers]]
- [[sources/arxiv-2605-23904|arXiv 2605.23904: SkillOpt]] — treats skill documents as external trainable weights; best results across 52 configurations.
- [[wiki/sources/karrot-kraft-design-system-agent|Karrot (2026): Kraft]] — **design-system knowledge as seven markdown skills** (`spacing-constraint`, `radius-constraint`, `typography-constraint`, `screen-patterns`, `small-writing-guide`, `design-principles`, `eval-self-check`), loaded only when relevant: a form screen pulls layout and spacing rules, while the copy guide loads only once copy is being decided. Two claimed benefits worth carrying — putting every rule in the system prompt both **wastes tokens and adds noise** (context-irrelevant rules actively degrade output, not merely cost money), and a design-system rule change edits **one skill file** rather than the system prompt. A concrete instance of skills as the maintenance boundary for institutional knowledge.

## Open Questions

- [Answered → [[queries/2026-05-27-skill-system-repeated-workflows|Query Page]]] Which repeated Bonny workflows deserve dedicated skills?
- Which of those workflows have strong enough activation cues to pass the 90% trigger-accuracy bar from Day-3?
- For the LLM Wiki specifically: should ingest, lint, query-answering, and gap-audit each be their own Skill, or compose under one `maintaining-wiki` umbrella?


