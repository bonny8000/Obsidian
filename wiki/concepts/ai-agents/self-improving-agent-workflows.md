---
type: concept
status: active
created: 2026-05-18
updated: 2026-05-27
tags: [agents, feedback, automation]
sources:
  - sources/lennys-podcast-cat-wu-ai-pm-claude-code
  - sources/arxiv-2605-23904
confidence: 0.80
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

## Related Concepts

- [[concepts/ai-agents/agentic-work-automation|Agentic Work Automation]]
- [[concepts/ai-agents/model-harness|Model Harness]]
- [[concepts/ai-agents/product-evals|Product Evals]]
- [[concepts/ai-agents/agent-memory|Agent Memory]]
- [[concepts/ai-agents/skill-system|Skill System]]
- [[concepts/ai-agents/skillopt|SkillOpt]]
- [[concepts/infrastructure-dev/text-space-optimization|Text-Space Optimization]]

## Sources

- [[sources/lennys-podcast-cat-wu-ai-pm-claude-code|Lenny's Podcast: Cat Wu on AI-Native Product Management]]
- [[sources/arxiv-2605-23904|arXiv 2605.23904: SkillOpt]] — concrete implementation of validation-gated skill evolution

## Open Questions

- [Answered → [[queries/2026-05-27-self-improving-ingest-rules|Query Page]]] What feedback from each wiki ingest should be saved as a rule for the next ingest?

