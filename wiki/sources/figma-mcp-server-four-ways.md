---
type: source
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [figma, mcp, design-to-code, agent-skills, design-system, figma-make, figjam, round-trip-workflow]
source_path: raw/web/figma-mcp-server-four-ways-2026-06-22.md
source_url: https://www.figma.com/blog/4-ways-were-using-our-mcp-server-at-figma/
authors: [Mari Kong]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.8
---

# Figma: 4 Ways We're Using Our MCP Server at Figma

**Author:** Mari Kong (Product Marketing Manager, Figma — AI tools across design and code)
**Published:** 2026-06-16 — Figma Blog (Inside Figma / Product updates)
**Raw capture:** [[raw/web/figma-mcp-server-four-ways-2026-06-22|figma-mcp-server-four-ways-2026-06-22]]
**URL:** [figma.com/blog/4-ways-were-using-our-mcp-server-at-figma](https://www.figma.com/blog/4-ways-were-using-our-mcp-server-at-figma/)

## Citation

Kong, M. (2026, June 16). *4 ways we're using our MCP server at Figma.* Figma Blog. Captured 2026-06-22 into `raw/web/figma-mcp-server-four-ways-2026-06-22.md`.

## Summary

Two months after opening the Figma canvas to agents, Figma's MCP server now spans the whole platform — Figma Slides, FigJam, Figma Make, and the new Figma agent — so decks, boards, and prototypes can all be created or updated from a prompt. The post showcases four internal workflows and announces new MCP capabilities: **write support across Slides/FigJam/Make/Figma agent**, **uploaded custom-font support** (typefaces render correctly instead of web-safe approximations), and a new **`download_assets`** tool that returns real exportable files (SVG/PDF/JPG/PNG or original source) rather than screenshots.

The four workflows: **(1) Create/refresh decks in Figma Slides** — an evergreen AI-launch deck refreshed from a code-editor prompt pulling Slack/Drive/blog/release-notes, using the `use_figma` tool plus the `/figma-use-slides` skill, rendering custom fonts on-brand. **(2) Generate FigJam boards from live data** — a custom `/figjam-builder` skill builds a kickoff board from context across Slack, Asana, Notion, and Hex, starting from real data instead of an empty board. **(3) Move designs between code and canvas with Figma Make** — a design→code→canvas→code round trip without leaving Figma: bring a Make preview onto the canvas as design layers rebuilt from library components, edit component states (default/hover/drag), then push those states back to code as a GitHub PR. **(4) Split the work with the Figma agent** — take a code-only screen, push it into Figma reusing existing components/variables and generating new ones where missing, then let the canvas-native Figma agent finish layout/type/color-variable mapping before pushing back to code via MCP.

Across all four, the throughline is **design-system-grounded generation** (agents read your component library and tokens and reuse them, so output is on-brand and built from your design system) and a consistent **"first 80% done, human review pass still needed"** cadence. The Figma agent and Make's production-codebase integration are in closed beta; MCP write capabilities are in open beta.

## Key Claims

- **The Figma MCP server now spans Slides, FigJam, Figma Make, and the new Figma agent** — write capabilities reach all four surfaces, so decks/boards/prototypes are promptable.
- **New tooling:** uploaded **custom-font** support (no more web-safe approximations) and a new **`download_assets`** tool returning actual exportable files (SVG/PDF/JPG/PNG or original source) — "unlike a screenshot, it returns the actual exportable file… No manual export needed."
- **Skills guide agents** to better, more consistent outputs — `/figma-use-slides`, custom `/figjam-builder` — and are shareable via the Figma community skills directory and community-resources repo. This is a concrete, design-tool instance of [[concepts/ai-agents/agent-skills|Agent Skills]].
- **Workflow 1 (Slides):** evergreen deck refreshed from a code-editor prompt aggregating Slack/Drive/Shortcut-blog/Release-Notes; agent uses `use_figma` + `/figma-use-slides`; renders uploaded custom fonts; "first 80%" done, review pass for image swaps and copy.
- **Workflow 2 (FigJam):** `/figjam-builder` custom skill generates a kickoff board from live data across Slack, Asana, Notion (structure) and Hex (analytics) — not an empty board.
- **Workflow 3 (Make, design↔code round trip):** branch code → build interactive prototype in Make → bring preview onto canvas as design layers rebuilt from library components → edit component states → push states back to code as a GitHub PR. The agent reads/writes real components on both ends, akin to **Code Connect** mapping library to production code, so "design decisions that used to lose fidelity between handoff and review now travel all the way to the PR."
- **Workflow 4 (Figma agent, code→canvas):** push a code-only screen into Figma reusing existing components/variables and generating new component sets/variables where missing; agent reads the library in both Figma and codebase to decide reuse vs build. Result is "a strong first pass, not a finished one" (auto layout, fonts, unmapped colors still need work); canvas-native Figma agent finishes, then push back to code via MCP.
- **Recurring themes:** design-system-grounded generation; "first 80% done"; a required human review pass on every workflow.
- **Beta status:** Figma agent + Make production-codebase integration in **closed beta**; MCP **write** capabilities in **open beta**.

## Useful Examples

- **The Make design↔code round trip** (Iris Lin's audio editor): the cleanest concrete example of bidirectional design↔code travel — preview→canvas as design layers, edit default/hover/drag states, states→code as a PR. A reference workflow for [[concepts/infrastructure-dev/design-to-code-workflow|design-to-code]].
- **Code-only screen → canvas (Yarden Katz):** prompt to "reuse my existing components and variables where they exist, and generate proper component sets and variables where they don't" — a model prompt for reverse-engineering code into a design-system-attached canvas representation.
- **`/figjam-builder` custom skill:** packaging recurring workshop-prep instructions into a reusable skill so you "don't have to re-prompt them every time" — a clean illustration of why skills beat repeated prompting.
- **`download_assets` vs screenshots:** returning real exportable assets (SVG/PDF/JPG/PNG/source) instead of a flat screenshot — useful whenever an agent needs production-grade assets, not pixels.
- **Custom-font rendering in Slides:** the agent rendering uploaded brand fonts rather than web-safe fallbacks — a small but concrete on-brand-fidelity win.

## Constraints / Caveats

- **Vendor showcase.** Figma demonstrating its own MCP server and agent on internal ("Figmate") workflows — selected success stories, not independent evaluation or failure-rate data.
- **No metrics.** "First 80%" is a qualitative cadence, not a measured figure; no accuracy, token, or time numbers are reported.
- **Heavy beta gating.** The two most impressive capabilities (Figma agent, Make production-codebase integration) are in *closed* beta; only MCP write is in open beta. Availability ≠ general access.
- **Human review is load-bearing, not optional.** Every workflow explicitly ends with a person fixing layout, fonts, unmapped colors, or copy. The agent produces a strong first pass, not a shippable artifact.
- **Design-system dependency.** The "on-brand, built from your design system" benefit presupposes a well-structured component library and variables (Code Connect-style mapping). Teams without that won't see the same fidelity.
- **Tool-coupled.** Findings are specific to Figma's ecosystem (Slides/FigJam/Make/agent + Figma MCP); they don't directly transfer to other design tools.

## Design Implications

- **For Bonny's design-to-code and slide work:** the **round-trip pattern** (canvas↔code with components preserved on both ends) is the aspirational target — design edits that survive all the way to a PR. Worth tracking even while gated, as the shape design tooling is converging toward.
- **Skills over repeated prompts.** The `/figjam-builder` and `/figma-use-slides` examples reinforce the general lesson (also in the Atlassian sources) that recurring multi-step generation should be packaged as a [[concepts/ai-agents/agent-skills|skill]], not re-prompted.
- **Design-system grounding is the precondition for quality.** The on-brand results depend on the agent reading a real component library + variables. This is the consumer side of the [[sources/atlassian-design-system-context-engine|Context Engine]] argument — invest in the system so agents can reuse it.
- **Plan for the review pass.** "First 80% done" is the right mental model for staffing AI-assisted design work: budget human time for layout/type/color/copy cleanup rather than expecting finished output.
- **`download_assets` for asset pipelines.** When an agent needs production assets, prefer the real-file export path over screenshots.

## Tensions

- **"First 80%" speed vs the still-required human pass.** The value is acceleration and on-brand fidelity, not autonomy; the last 20% (layout, type, color mapping, copy) consistently needs a human.
- **Round-trip fidelity (this post) vs the [[sources/atlassian-design-md|DESIGN.md]] re-implementation risk.** Figma's agent reuses real library components on both ends (good); the DESIGN.md warning is that an under-grounded agent re-implements components instead. Same lesson from two directions: ground the agent in the *actual* component library, not a re-implementation spec.
- **MCP write power vs beta gating.** The most transformative capabilities are demonstrated but not generally available — promise outrunning access.
- **Design-tool-native agent (Figma agent) vs code-editor agent (MCP from your IDE).** The post tag-teams them (server brings code-only screens onto canvas; canvas-native agent finishes). The interesting design question is where each is the right host — see [[comparisons/skills-vs-mcp-vs-agents-md]] for the broader primitive-routing frame.

## Open Questions

- What are the actual accuracy/failure rates behind "first 80%"? No numbers are given.
- When do the closed-beta capabilities (Figma agent, Make production-codebase integration) reach general availability?
- How well does the round trip hold up on a *large* design system with deep component nesting, vs the demo-scale files shown?
- How does Figma's skill format relate to Claude/Anthropic [[concepts/ai-agents/agent-skills|Agent Skills]] and to Atlassian's `llms.txt`/`offerings.json` agentic content? Is there convergence on a shared authoring discipline?
- For Bonny: could a similar skill-driven, design-system-grounded round trip be set up for slide/mock generation, and where would the inevitable review pass land?

## Concepts Linked

- [[concepts/infrastructure-dev/figma-make|Figma Make]]
- [[concepts/infrastructure-dev/design-to-code-workflow|Design-to-Code Workflow]]
- [[concepts/infrastructure-dev/design-system-implementation|Design System Implementation]]
- [[concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]]
- [[concepts/infrastructure-dev/wireframe-generation|Wireframe Generation]]
- [[concepts/infrastructure-dev/design-automation|Design Automation]]
- [[concepts/ai-agents/mcp-integration|MCP Integration]]
- [[concepts/ai-agents/agent-skills|Agent Skills]]
- [[concepts/ai-agents/vibe-design|Vibe Design]]
- [[concepts/ai-agents/vibe-coding|Vibe Coding]]
- [[comparisons/skills-vs-mcp-vs-agents-md|Skills vs MCP vs AGENTS.md vs DESIGN.md]]
- [[concepts/infrastructure-dev/ai-prototyping|AI Prototyping]] (new)
- [[concepts/infrastructure-dev/agentic-content|Agentic Content]] (new)
- (future) concepts/infrastructure-dev/design-code-round-trip — bidirectional canvas↔code workflow that preserves real design-system components on both ends (Make/Figma-agent + MCP).

## LLM Use

- **Use for:** describing the current state of Figma's MCP-across-platform capabilities (Slides/FigJam/Make/agent write support, custom fonts, `download_assets`); concrete round-trip and code→canvas workflow patterns; the "skills over repeated prompts" lesson; the "first 80% + human review" cadence for staffing AI-assisted design.
- **Do not use for:** quantitative claims (no metrics given); assuming general availability (key features are closed beta); generalizing Figma-specific workflows to other design tools; treating "first 80%" as a measured number.
- **Best prompt pattern:** "Using Kong's four Figma MCP workflows, map a design-system-grounded workflow for [task] onto the right surface (Slides / FigJam / Make / Figma agent), name the skill that should carry the recurring instructions, and identify exactly where the human review pass lands."

## Reliability Notes

> [!warning] Caveats
> - **Vendor showcase, no metrics.** Selected internal success stories; "first 80%" is qualitative. Treat as capability demonstration, not evidence of accuracy.
> - **Closed-beta gating.** The headline agent/Make-codebase capabilities aren't generally available.
> - **Human-review-dependent.** Every workflow ends with a person finishing the work.
> - **Confidence:** 0.85 on the capability/workflow descriptions (what the MCP can now do); 0.6 on durability/availability (beta, fast-moving); 0.5 on any implied quality level (no metrics).

## Backfill Status

- Newly written 2026-06-22 from a full web capture. All sections populated. No prior thin version to upgrade.
