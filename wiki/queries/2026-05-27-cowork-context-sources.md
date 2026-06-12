---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.68
---

# Which personal context sources should Bonny connect or manually export before asking the wiki to synthesize knowledge?

## Short Answer
For a design and PM-focused knowledge worker, the highest-value context sources to connect or export first are: (1) Figma MCP for design artifacts, (2) manually exported meeting notes or Slack highlights, and (3) exported browser bookmarks or article saves. These cover the main channels where insight originates before reaching the wiki.

## Evidence
- [[concepts/ai-agents/cowork|Cowork]] ??"Cowork performs better when connected to relevant context sources such as Slack, Gmail, calendar, Drive, design templates, Salesforce, Gong, or Figma MCP." For Bonny's design workflow, Figma MCP and Slack exports are the most applicable.
- [[concepts/ai-agents/agent-memory|Agent Memory]] ??"Memory should be source-grounded and auditable." Connecting real context sources ensures synthesis is grounded, not hallucinated.
- [[sources/lennys-podcast-cat-wu-ai-pm-claude-code|Lenny's Podcast: Cat Wu on AI-Native PM]] ??"It can draft decks and briefs by synthesizing internal communications and source-of-truth documents." The more context is available, the better the synthesis.

## Follow-up Sources Needed
- Specific MCP server availability for Figma, Slack, and Gmail for Bonny's local Claude Code setup.
- Whether Obsidian vault itself can be exposed as a Cowork context source via MCP.

