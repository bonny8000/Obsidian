---
type: source
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [resource-directory, design-system, agentic-ai, prompts, design-tokens, mcp, figma-mcp, curated-library]
source_path: raw/web/aidesign-guide-catalog-2026-06-22.md
source_url: https://www.aidesign.guide/
authors: [Romina Kavcic]
sources: []
ingest_level: light
coverage: partial
llm_ready: false
raw_preserved: true
confidence: 0.75
---

# The AI Design Guide (aidesign.guide) — Curated Resource Directory

**Author / Curator:** Romina Kavcic (also runs The Design System Guide, thedesignsystem.guide)
**Published:** Living catalog — landing page captured 2026-06-22 — The AI Design Guide (aidesign.guide)
**Raw capture:** [[raw/web/aidesign-guide-catalog-2026-06-22|aidesign-guide-catalog-2026-06-22]]
**URL:** [aidesign.guide](https://www.aidesign.guide/)

## Citation

Kavcic, R. (2026). *The AI Design Guide* [Curated resource library]. aidesign.guide. Landing/catalog page captured 2026-06-22 into `raw/web/aidesign-guide-catalog-2026-06-22.md`. (Living resource, updated weekly.)

## Summary

The AI Design Guide is a curated, weekly-updated resource library for designers building with agentic AI and design-system automation. It is a **directory/index, not an article** — the home page points into guides, prompts, tools, a knowledge base, a dictionary, templates, comparisons, a 158-system design-systems directory, and several free interactive tools. Tagline: "Agentic AI for designers." The library is partly gated (login / pricing / "First Agentic Design Community") and pairs with a weekly Substack newsletter (DSG — Design, Systems, Growth). Content is practical and tool-specific: Figma MCP setup, Claude Code for design systems, token pipelines, component audits, and production prompts tested across Claude/ChatGPT/Gemini.

Its value to this wiki is as a **discovery surface / pointer**, not as citable evidence. The most concretely useful artifacts are free interactive tools — Style Explorer (20 styles → copy CLAUDE.md rules), Tools.md Generator (tools.md context for Claude/Codex/Cursor), Trust Levels Playground (five levels of agent autonomy), Token Audit (50 token files compared), and Name Design Tokens — plus the design-systems directory. Because it updates weekly and is partly paywalled, specific counts and titles drift; re-verify before relying on any number.

## Key Claims

> This is a curated catalog, so "claims" here are descriptions of what the resource offers, not evidence-bearing assertions.

- A **living, weekly-updated curated library** for agentic-AI + design-system work; "built from real projects, not theory."
- Sections: **Guides, Prompts, Tools, Knowledge Base, Dictionary, Templates, Compare, Design Systems directory, Learning paths.**
- Advertised size at capture: ~**87 guides, 33 prompts, 34 dictionary terms, 26 templates, 9 learning paths**; **158-system** design-systems directory (Netflix, Meta, Porsche, Volvo, etc.).
- **Free interactive tools:** Style Explorer, Tools.md Generator, Trust Levels Playground, Token Audit, Name Design Tokens (namedesigntokens.guide).
- Tool reviews (Claude, Cursor) and comparisons (Style Dictionary vs Tokens Studio; Claude Code vs Cursor), "no affiliate links, no hedging."
- Recent guides signal currency: "Build Your Own MCP Server for Your Design System," "Claude Fable 5 for Designers," "Rolling Out AI Across a Design Team," "The Taste Stack."
- Partly **gated**; weekly Substack newsletter; logos claim **502+ designers** from named companies (Atlassian, Meta, Salesforce, Replit, etc.).

## Useful Examples

- **Style Explorer** — pick one of 20 visual directions, copy generated CLAUDE.md rules. Directly relevant to design-system context-engineering / [[concepts/infrastructure-dev/claudemd-context|CLAUDE.md context]].
- **Tools.md Generator** — produces a `tools.md` context file for Claude, Codex, Cursor, and coding agents (a sibling of the agentic-content / `llms.txt` idea seen in the Atlassian sources).
- **Trust Levels Playground** — one finding rendered at five levels of agent autonomy, to "feel the difference" — a teaching artifact for calibrating agent autonomy.
- **Token Audit** — 50 token files compared — a reference for [[concepts/infrastructure-dev/color-token-architecture|token architecture]] decisions.
- **Design Systems directory (158 systems)** — searchable comparison of what real companies ship (tokens, components, docs).

## Constraints / Caveats

- **Index, not evidence.** This is a curated pointer/discovery surface. Do not cite it as authority for any specific empirical claim — follow through to the underlying guide/tool and evaluate that.
- **Single-author, commercial.** Curated and monetized by one person (Romina Kavcic); much content is gated behind login/pricing. Quality is "honest reviews" by her own framing, but it is opinion/thought-leadership, not independent research.
- **Volatile counts.** Section counts conflict even within the captured page (e.g., 87/33/34/26 vs 15/21) and update weekly. Treat every number as a snapshot.
- **Landing page only.** This capture is of the home/catalog page; individual guides/tools were not fetched and are not summarized here.
- **Not LLM-ready as evidence.** Marked `llm_ready: false` deliberately — usable as a resource pointer, not as a source to quote for claims.

## Design Implications

- **As a discovery entry point** for designer-facing agentic-AI tooling: useful when scoping what tools/prompts/templates exist for a design-system automation task, especially the free generators.
- **Tools.md Generator and Style Explorer** map directly onto the wiki's design-system context-engineering work (CLAUDE.md/agentic-content authoring) — worth a hands-on look as templates, not as authorities.
- **Trust Levels Playground** is a useful teaching artifact when explaining agent-autonomy calibration to a design audience.
- **Re-check before relying** on any catalog figure; bookmark for periodic re-scan given weekly updates.

## Tensions

- **Breadth/currency vs depth/authority.** Frequent updates and wide coverage make it a good radar; the same churn and single-author commercial nature make it weak as a citable source.
- **Free tools vs gated library.** The most independently useful artifacts (Style Explorer, Tools.md Generator, Trust Levels Playground, Token Audit) are free; the deeper guides are paywalled.

## Open Questions

- Which specific guides/tools are worth a full standalone ingest later (e.g., "Build Your Own MCP Server for Your Design System," "The Taste Stack")? Those could become their own substantial sources.
- How does the Tools.md Generator's output compare to Atlassian's `llms.txt`/`offerings.json` agentic content and to DESIGN.md as authoring formats?
- Is the design-systems directory (158 systems) accurate/maintained enough to cite for comparative claims, or only for discovery?

## Concepts Linked

- [[concepts/infrastructure-dev/claudemd-context|CLAUDE.md / AGENTS.md Context]]
- [[concepts/infrastructure-dev/color-token-architecture|Color Token Architecture]]
- [[concepts/infrastructure-dev/design-system-implementation|Design System Implementation]]
- [[concepts/infrastructure-dev/design-automation|Design Automation]]
- [[concepts/infrastructure-dev/figma-make|Figma Make]]
- [[concepts/ai-agents/mcp-integration|MCP Integration]]
- [[concepts/ai-agents/agent-skills|Agent Skills]]
- [[concepts/ai-agents/claude-code|Claude Code]]
- [[concepts/ai-agents/vibe-design|Vibe Design]]
- [[concepts/infrastructure-dev/agentic-content|Agentic Content]] (new) — `tools.md`/`llms.txt`-style machine-readable context files for coding agents (the Tools.md Generator produces exactly this).

## LLM Use

- **Use for:** discovering designer-facing agentic-AI tools, prompts, templates, and the free interactive generators (Style Explorer, Tools.md Generator, Trust Levels Playground, Token Audit); as a periodically-refreshed radar for the agentic-design space.
- **Do not use for:** citing any specific claim as evidence (it is a curated index — `llm_ready: false`); quoting catalog counts as stable facts (they drift weekly); treating reviews/comparisons as independent/peer-reviewed.
- **Best prompt pattern:** "Treat aidesign.guide as a directory only: from its catalog, list candidate tools/guides relevant to [design-system task], then for each, name what would need independent verification before citing it."

## Reliability Notes

> [!warning] Caveats
> - **Resource directory, not citable evidence.** `llm_ready: false`, `coverage: partial`, `ingest_level: light` — this is a pointer/index. Always follow through to the underlying artifact.
> - **Single-author, partly gated, weekly-churning.** Counts and titles are snapshots; deeper content is paywalled; framing is commercial thought-leadership.
> - **Landing page only.** Individual guides/tools not fetched or summarized.
> - **Confidence:** 0.75 that it is a high-quality, current discovery surface for agentic-design tooling; not a confidence in any specific claim it makes.

## Backfill Status

- Newly written 2026-06-22 from a landing-page web capture. All sections populated. Treated as a light-ingest resource pointer (not citable evidence). No prior version to upgrade.
