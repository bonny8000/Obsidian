---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.68
---

# Should this vault be version controlled with Git?

## Short Answer
Yes. Git version control is the most practical way to make the wiki's change history inspectable and reversible. Because the AI agent writes and edits files during ingest, Git provides an audit trail of what changed in each ingest session—directly supporting the "auditable" memory principle the wiki is built around.

## Evidence
- [[concepts/infrastructure-dev/llm-wiki|LLM Wiki]] — "The wiki layer is generated and maintained by the AI agent." Agent-written files are exactly the case where version control is most important—changes are frequent, automated, and potentially wrong.
- [[concepts/ai-agents/agent-memory|Agent Memory]] — "Memory should be source-grounded and auditable." Git makes the wiki auditable at the commit level.
- [[concepts/infrastructure-dev/knowledge-linting|Knowledge Linting]] — If a lint pass detects regressions, Git enables rollback to the last good state.
- [[concepts/ai-agents/vibe-coding|Vibe Coding]] — "The workflow requires tests, diffs, version control, and review because generated code can still be wrong." The same principle applies to AI-generated Markdown.

## Follow-up Sources Needed
- Whether large raw files (PDFs, images) require Git LFS or should remain outside Git tracking.
- A `.gitignore` template appropriate for an Obsidian vault with AI-maintained wiki layers.
