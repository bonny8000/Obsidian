---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.72
---

# Which source types should Bonny ingest first?

## Short Answer
Ingest primary written sources first?rticles, podcast transcripts, and academic papers where claims are explicit and extractable. These give the wiki concrete, attributable evidence. Secondary and social sources (videos, short-form posts) can follow once the core concept cluster is established, because they add signal but require more interpretive judgment.

## Evidence
- [[concepts/infrastructure-dev/llm-wikiLLM Wiki]] ??"The raw source layer should remain immutable." The current wiki already contains written web sources (brunch articles, podcast transcripts, arXiv papers) as its first sources, confirming this is the working pattern.
- [[sources/brunch-ghidesigner-487|AI Designer LLM Wiki Article]] ??The architecture explicitly defines a raw-source layer. Written sources translate most directly into source page claims and concept links.
- [[concepts/ai-agents/agent-memoryAgent Memory]] ??"Memory should be source-grounded and auditable." Written sources are easier to audit than video or oral content.
- [[maps/llm-wiki-architecture|LLM Wiki Architecture]] ??The existing source file collection (brunch, arxiv, naverlabs blogs, podcast transcripts) demonstrates the practical starting pattern.

## Follow-up Sources Needed
- Whether Obsidian or Claude Code can ingest PDF papers and YouTube transcripts reliably enough to expand the source type set.

