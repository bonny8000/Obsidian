---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.70
---

# How should Bonny keep wiki categories stable while still ingesting new sources quickly?

## Short Answer
Use the schema layer (AGENTS.md / CLAUDE.md) to define category rules and require new source pages to map into existing concept clusters before creating new top-level categories. New clusters should only be created when two or more new sources converge on a gap that no existing category covers.

## Evidence
- [[maps/llm-wiki-architecture|LLM Wiki Architecture]] ??The schema layer ("Rules for structure, style, ingest, query, and linting") is the human-controlled governor of wiki structure. Keeping schema rules explicit prevents drift.
- [[concepts/product-management/ai-product-consistency|AI Product Consistency]] ??"Fast AI shipping can create overlapping features and unclear product boundaries." The same risk applies to wiki categories when ingesting rapidly.
- [[concepts/infrastructure-dev/knowledge-linting|Knowledge Linting]] ??Linting can detect orphan pages, broken links, and category drift. Regular lint passes are the operational signal that category stability is degrading.
- [[sources/lennys-podcast-cat-wu-ai-pm-claude-code|Lenny's Podcast: Cat Wu on AI-Native PM]] ??"Consistency should be balanced against the learning value of shipping experiments." Applied to the wiki: prefer linking new sources to existing concepts over creating new categories.

## Follow-up Sources Needed
- Specific lint rules for detecting premature category proliferation.

