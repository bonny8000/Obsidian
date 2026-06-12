---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.70
---

# What is the Obsidian equivalent of a lightweight onboarding command for Bonny's LLM Wiki?

## Short Answer
The Obsidian equivalent is a pinned "Start Here" note in the wiki root (e.g., `wiki/index.md`) that surfaces the three core workflows (ingest, query, lint), links to the schema files, and lists the current top-level maps. This mirrors the `/power-up` pattern from the Cat Wu source? single entry point that teaches the most reliable paths without becoming documentation overload.

## Evidence
- [[concepts/product-management/ai-product-onboarding|AI Product Onboarding]] ??"A feature like `/power-up` is positioned as a way to surface core practices inside the product. Onboarding should guide users to reliable paths without turning into visible documentation overload."
- [[maps/llm-wiki-architecture|LLM Wiki Architecture]] ??The architecture already defines the three main operations (ingest, query, lint) and the schema layer. An index note can simply surface this.
- [[concepts/infrastructure-dev/llm-wiki|LLM Wiki]] ??"The schema layer tells the agent how to structure pages and workflows." The index can double as a human-readable schema summary.
- [[sources/lennys-podcast-cat-wu-ai-pm-claude-code|Lenny's Podcast: Cat Wu on AI-Native PM]] ??"Built-in education can reduce reliance on social media, scattered announcements, or trial and error."

## Follow-up Sources Needed
- A review of whether `wiki/index.md` already serves this function or needs to be expanded.

