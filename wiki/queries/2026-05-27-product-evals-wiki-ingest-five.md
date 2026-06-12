---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.71
---

# What are the first five eval tasks for Bonny's LLM Wiki ingest workflow?

## Short Answer
The five most useful starting evals are: (1) concept page created with at least one valid source link; (2) source page created with accurate citation and summary matching the raw content; (3) no hallucinated concept links?very `[[concepts/X]]` link must correspond to an existing file; (4) confidence score not set above 0.8 when the raw source was a secondary/perspective article; and (5) "Related Concepts" links are bidirectional?f A links to B, B should link back to A.

## Evidence
- [[concepts/ai-agents/product-evals|Product Evals]] ??"PMs do not always need hundreds of evals; a small set of strong evals can be useful. Evals are most valuable when a feature needs clearer behavioral definition. Features such as memory and agentic task completion benefit from explicit evals."
- [[concepts/infrastructure-dev/llm-wiki|LLM Wiki]] ??The three-layer architecture defines what a correct ingest output looks like: immutable raw, accurate wiki, schema compliance. Each of the five evals maps to one of these requirements.
- [[sources/lennys-podcast-cat-wu-ai-pm-claude-code|Lenny's Podcast: Cat Wu on AI-Native PM]] ??"A small set of strong evals can be useful. Evals translate fuzzy product quality into examples, tasks, expected outcomes, and failure modes."
- [[concepts/ai-agents/model-harness|Model Harness]] ??"Harnesses should change as model capability changes." These evals also serve as the test suite for knowing when to relax scaffolding.

## Follow-up Sources Needed
- A script or Claude Code command that runs these five checks automatically after each ingest session.

