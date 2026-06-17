---
type: concept
status: active
created: 2026-05-18
updated: 2026-06-17
tags: [agents, feedback, automation, meta-skills]
sources:
  - sources/lennys-podcast-cat-wu-ai-pm-claude-code
  - sources/arxiv-2605-23904
  - sources/agent-skills-day-3
confidence: 0.84
---

# Self-Improving Agent Workflows

## Summary

Self-improving agent workflows capture feedback from task review and use it to improve future agent runs, reducing repeated mistakes over time.

## Why It Matters

The transcript frames the next stage of agentic work as moving from one successful task to many parallel tasks, with remote execution, verification, and feedback that the system remembers for future runs.

## Key Claims

- Parallel agent work needs clear task status, verification, and human attention routing.
- Feedback should be incorporated into future runs so the same mistake does not recur.
- Self-improvement depends on durable memory, skills, evals, or explicit process updates.
- This pattern is relevant for both code agents and non-code work agents.
- **SkillOpt** (arXiv 2605.23904) provides a concrete implementation: scored rollouts drive bounded text edits on skill documents, validated before acceptance, with epoch-wise optimization rounds. Best/tied across all 52 tested configurations on 6 benchmarks. (See [[concepts/ai-agents/skillopt|SkillOpt]].)
- Day-3 organizes the meta-skill landscape into four buckets: **(1) Authoring** (description → draft SKILL.md, e.g. Anthropic's `skill-creator`, Google ADK's "skill factory"); **(2) Assisted authoring from traces** (watch successful runs, harvest a skill, human confirms); **(3) Improvement** (existing skill + failing evals → proposed edits, e.g. SkillOpt, Anthropic's description-optimization loop, Karpathy's `autoresearch` pattern); **(4) Library evolution** (agent notices a recurring problem it just solved, proposes a new skill — Voyager-style, Schmid's `self-learning-skill`).
- **Habits that hold up:** anything an agent writes enters at the draft tier regardless of meta-skill confidence; keep a human in the loop for the first few edits; do not start with meta-skills before manual authoring works.

## Related Concepts

- [[concepts/ai-agents/agentic-work-automation|Agentic Work Automation]]
- [[concepts/ai-agents/model-harness|Model Harness]]
- [[concepts/ai-agents/product-evals|Product Evals]]
- [[concepts/ai-agents/agent-memory|Agent Memory]]
- [[concepts/ai-agents/agent-skills|Agent Skills]]
- [[concepts/ai-agents/skill-system|Skill System]]
- [[concepts/ai-agents/skillopt|SkillOpt]]
- [[concepts/infrastructure-dev/text-space-optimization|Text-Space Optimization]]
- [[concepts/ai-agents/procedural-memory|Procedural Memory]]

## Sources

- [[sources/lennys-podcast-cat-wu-ai-pm-claude-code|Lenny's Podcast: Cat Wu on AI-Native Product Management]]
- [[sources/arxiv-2605-23904|arXiv 2605.23904: SkillOpt]] — concrete implementation of validation-gated skill evolution.
- [[sources/agent-skills-day-3|Singhal et al. (2026): Agent Skills (Day 3)]] — Section 6 meta-skills taxonomy and the three habits that hold up.

## Open Questions

- [Answered → [[queries/2026-05-27-self-improving-ingest-rules|Query Page]]] What feedback from each wiki ingest should be saved as a rule for the next ingest?

