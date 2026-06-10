---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.70
---

# Which parts of Bonny's wiki ingest process are true product logic versus temporary model scaffolding?

## Short Answer
True product logic includes the three-layer architecture (raw/wiki/schema), the concept-source-map page structure, the ingest/query/lint workflow sequence, and the requirement that all claims be source-grounded. Temporary scaffolding includes specific prompt wording, confidence thresholds, and workarounds for current model limitations that should be revisited when a better model is available.

## Evidence
- [[concepts/ai-agents/model-harness|Model Harness]] ??"Harness features can compensate for current model weaknesses. New model launches should trigger a review of system prompts and product crutches. Some scaffolding remains useful for user visibility even if the model no longer strictly needs it."
- [[maps/llm-wiki-architecture|LLM Wiki Architecture]] ??The three-layer table (raw/wiki/schema) and the five-step flow are product logic because they define what the wiki is, regardless of which model runs it.
- [[concepts/infrastructure-dev/llm-wiki|LLM Wiki]] ??"The raw source layer should remain immutable." This is a product-logic rule, not a model-capability workaround.
- [[sources/lennys-podcast-cat-wu-ai-pm-claude-code|Lenny's Podcast: Cat Wu on AI-Native PM]] ??"Stronger models can unlock previously unreliable features such as richer code review." In the wiki context, specific link-extraction and confidence rules may soften as models improve.

## Follow-up Sources Needed
- A changelog tracking which ingest rules have been relaxed as model capability has improved.

