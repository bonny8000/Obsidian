---
type: source
status: active
created: 2026-06-03
tags: [ai-recruitment, ai-analysis, uxr-tools, user-interviews]
sources: [raw/2026-06-03-user-interviews-ai-assistant.md]
updated: 2026-06-12
ingest_level: deep
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 1.0
---

# User Interviews AI Assistant

## Citation

User Interviews. (2026). *AI Assistant: Recruit faster and drive impact with AI-assisted targeting, screening, and analysis.* [Online]. Available at: https://www.userinterviews.com/ai-assistant

## Summary

User Interviews has launched an AI Assistant suite designed to streamline the entire research lifecycle, from participant recruitment to data analysis. The suite includes prompt-based targeting, smart screener generation, a project creation agent, and various AI-driven analysis tools like session breakdowns and grounded insight exploration.

## Key Claims

- **AI-Assisted Targeting:** Users can describe ideal participants in natural language to generate recruitment criteria.
- **Smart Screener Generation:** AI generates screener questions and qualification criteria.
- **Project Creation Agent:** A guided conversational agent helps move from a research idea to a launch-ready project draft.
- **AI Analysis Tools:** Includes AI chat for grounded insight exploration (with citations to transcripts), session breakdowns, and highlight clips.
- **MCP Integration:** Early access available for running User Interviews inside AI tools like Claude, ChatGPT, and Cursor via the Model Context Protocol (MCP).

## Concepts Linked

- [[concepts/ai-recruitment|AI Recruitment]]
- [[concepts/ai-analysis|AI Analysis]]
- [[concepts/mcp-integration|MCP Integration]]
- [[concepts/ux-research/ux-research-automation|UXR Automation]]

## Useful Examples

- Current example source: use examples, tables, cases, or named artifacts already present elsewhere in this note; otherwise return to `raw/2026-06-03-user-interviews-ai-assistant.md` before asking an LLM for concrete examples.

## Constraints / Caveats

- Coverage is `substantial` and ingest level is `deep`; do not treat this source as fully digested unless `coverage: full`.
- Claims should be checked against `raw/2026-06-03-user-interviews-ai-assistant.md` when used for recommendations, metrics, or external-facing work.

## Reliability Notes

- Coverage is `substantial` and ingest level is `deep`; do not treat this source as fully digested unless `coverage: full`.
- Claims should be checked against `raw/2026-06-03-user-interviews-ai-assistant.md` when used for recommendations, metrics, or external-facing work.

Primary source from the product vendor. High confidence in feature availability and intended use cases.

## Design Implications

- Use this source to shape research design, UX evidence, method selection, and evaluation prompts.
- Connect it with [[concepts/ai-recruitment]], [[concepts/ai-analysis]], [[concepts/mcp-integration]], [[concepts/ux-research/ux-research-automation]] before turning it into a project recommendation.

## Tensions

- Backfill note: source-specific tensions were not separately extracted in the earlier ingest. Compare this source with related concepts and maps before treating its framing as settled.

## Open Questions

- What evidence, examples, or counterexamples should be extracted from the raw source before marking this as `coverage: full`?
- Which linked concept would change most if this source were contradicted?

## LLM Use

- **Use for:** research design, UX evidence, method selection, and evaluation prompts.
- **Do not use for:** unsupported exact claims beyond the source note's `substantial` coverage.
- **Best prompt pattern:** Ask the LLM to combine this source with its linked concepts, then verify any specific claim against the raw source before final use.

## Backfill Status

- Retrofitted on 2026-06-12 by `scripts/backfill_llm_ready.py` from the existing source note.
- This standardizes the note for LLM use; it does not by itself mean the raw source has been fully re-read.
