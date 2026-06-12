---
type: concept
status: active
created: 2026-05-18
updated: 2026-05-27
tags: [ai-agent, skills, automation]
sources:
  - sources/brunch-ghidesigner-486
  - sources/arxiv-2605-23904
confidence: 0.85
---

# Skill System

## Summary

A skill system stores reusable task patterns so an agent can repeat or improve a workflow without rediscovering the same steps every time.

## Why It Matters

Skills turn one-off agent work into compounding process knowledge. For design operations, a skill might encode how to summarize research, build a prototype, audit UI quality, or maintain the wiki.

## Key Claims

- Skills can capture successful procedures, not only facts.
- Skill quality depends on clear inputs, outputs, constraints, and verification steps.
- In an LLM Wiki, skills and source-grounded notes should stay separate: skills say how to work; wiki pages say what is known.

## Related Concepts

- [[concepts/ai-agents/autonomous-ai-agent|Autonomous AI Agent]]
- [[concepts/ai-agents/agent-memory|Agent Memory]]
- [[concepts/ai-agents/ai-agent-workflow|AI Agent Workflow]]
- [[concepts/ai-agents/skillopt|SkillOpt]]
- [[concepts/infrastructure-dev/text-space-optimization|Text-Space Optimization]]
- [[concepts/ai-agents/self-improving-agent-workflows|Self-Improving Agent Workflows]]

## Sources

- [[sources/brunch-ghidesigner-486|Hermes Agent AI for Designers]]
- [[sources/arxiv-2605-23904|arXiv 2605.23904: SkillOpt]] ??treats skill documents as external trainable weights; best results across 52 configurations

## Open Questions

- [Answered ??[[queries/2026-05-27-skill-system-repeated-workflows|Query Page]]] Which repeated Bonny workflows deserve dedicated skills?


