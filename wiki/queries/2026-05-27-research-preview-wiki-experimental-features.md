---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.70
---

# Which wiki features should be labeled experimental before Bonny relies on them?

## Short Answer
Label as experimental: (1) the query workflow (this session is its first structured test); (2) any automated link generation that has not been manually reviewed across a full ingest cycle; (3) confidence scores on concept pages (the scoring rules have not been formally validated); and (4) map pages that were generated from a single source and have not been cross-checked against additional evidence.

## Evidence
- [[concepts/product-management/research-preview|Research Preview]] ??"Research Preview can lower internal friction by reducing the perceived cost of shipping. It helps users understand that a feature is early and feedback-oriented. It can create risk if users depend on experimental behavior without enough stability guidance."
- [[concepts/product-management/ai-product-consistency|AI Product Consistency]] ??"Fast AI shipping can create overlapping features and unclear product boundaries." In the wiki, unvalidated features create the same problem if relied upon without the experimental label.
- [[concepts/infrastructure-dev/llm-wiki|LLM Wiki]] ??"The wiki layer is generated and maintained by the AI agent." Generated outputs that have not been reviewed should be marked as such.
- [[sources/lennys-podcast-cat-wu-ai-pm-claude-code|Lenny's Podcast: Cat Wu on AI-Native PM]] ??"Research Preview can help set expectations, but it does not replace coherent product architecture."

## Follow-up Sources Needed
- A status taxonomy (e.g., draft, experimental, active, needs-review) that Bonny can apply consistently to wiki pages.

