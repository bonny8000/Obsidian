---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.68
---

# When the wiki ingest makes a bad link or summary, what introspection questions should Bonny ask first?

## Short Answer
Ask four questions in order: (1) Did the prompt provide enough source context for the model to create a valid link? (2) Did the model have clear instructions for when to create a new concept versus link to an existing one? (3) Was a verification step missing that would have caught the error? (4) Is this a recurring pattern or a one-off? The Cat Wu source frames introspection as diagnostic input, not guaranteed truth, so treat the model's explanation as a hypothesis.

## Evidence
- [[concepts/ai-agents/model-introspectionModel Introspection]] ??"Asking the model why it made a mistake can reveal likely friction in the harness. Introspection helps identify whether failures came from prompts, tools, delegation, or missing verification. Human judgment is still needed because model explanations can be incomplete or post-hoc."
- [[concepts/ai-agents/model-harnessModel Harness]] ??"Harness features can compensate for current model weaknesses." A bad link usually points to a prompt gap or missing verification, not a fundamental model failure.
- [[concepts/ai-agents/product-evalsProduct Evals]] ??"Features such as memory and agentic task completion benefit from explicit evals." Repeated bad links indicate a missing eval for link-creation behavior.
- [[sources/lennys-podcast-cat-wu-ai-pm-claude-code|Lenny's Podcast: Cat Wu on AI-Native PM]] ??"Introspection pairs well with trusted human feedback and quantitative evals."

## Follow-up Sources Needed
- Specific introspection prompt templates for Obsidian/Markdown link failures.

