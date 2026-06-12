---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.72
---

# Which wiki maintenance workflow should be automated first: ingest, link checking, source verification, or periodic synthesis?

## Short Answer
Ingest should be automated first. The Cat Wu transcript explicitly states that good automation starts with repeated tasks the user already performs, and the LLM Wiki architecture defines ingest as the primary recurring operation. Without reliable ingest, there are no source or concept pages for lint or synthesis to operate on.

## Evidence
- [[concepts/ai-agents/agentic-work-automation|Agentic Work Automation]] ??"Good automation starts with repeated tasks the user already performs. A prototype that is never used daily creates little leverage."
- [[concepts/infrastructure-dev/llm-wiki|LLM Wiki]] ??"The main workflows are ingest, query, and lint." Ingest is listed first and is the foundation for the other two.
- [[maps/llm-wiki-architecture|LLM Wiki Architecture]] ??The defined flow starts with Bonny adding material to `raw/`, then the agent ingesting it; subsequent steps depend on ingest having succeeded.
- [[sources/lennys-podcast-cat-wu-ai-pm-claude-code|Lenny's Podcast: Cat Wu on AI-Native PM]] ??"The goal is to push workflows toward trustable, repeatable execution with clear verification."

## Follow-up Sources Needed
- A concrete ingest eval suite to measure when automated ingest is reliable enough to trust without per-run review.

