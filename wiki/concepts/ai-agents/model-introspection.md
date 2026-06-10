---
type: concept
status: active
created: 2026-05-18
updated: 2026-05-18
tags: [llm, evals, debugging]
sources:
  - sources/lennys-podcast-cat-wu-ai-pm-claude-code
confidence: 0.68
---

# Model Introspection

## Summary

Model introspection is the practice of asking an AI model to explain why it behaved a certain way, then using that explanation as a hypothesis for improving prompts, tools, evals, or product flow.

## Why It Matters

The transcript describes introspection as useful for finding why a model skipped UI verification, delegated poorly, misunderstood the task, or followed confusing prompt context. It should be treated as diagnostic input, not guaranteed truth.

## Key Claims

- Asking the model why it made a mistake can reveal likely friction in the harness.
- Introspection helps identify whether failures came from prompts, tools, delegation, or missing verification.
- Human judgment is still needed because model explanations can be incomplete or post-hoc.
- Introspection pairs well with trusted human feedback and quantitative evals.

## Related Concepts

- [[concepts/ai-agents/product-evals|Product Evals]]
- [[concepts/ai-agents/model-harness|Model Harness]]
- [[concepts/product-management/ai-pm-skills|AI PM Skills]]
- [[concepts/ai-agents/self-improving-agent-workflows|Self-Improving Agent Workflows]]

## Sources

- [[sources/lennys-podcast-cat-wu-ai-pm-claude-code|Lenny's Podcast: Cat Wu on AI-Native Product Management]]

## Open Questions

- [Answered → [[queries/2026-05-27-model-introspection-bad-link|Query Page]]] When the wiki ingest makes a bad link or summary, what introspection questions should Bonny ask first?

