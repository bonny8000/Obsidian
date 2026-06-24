---
source_url: https://www.figma.com/blog/4-ways-were-using-our-mcp-server-at-figma/
captured: 2026-06-22
title: "4 ways we're using our MCP server at Figma"
authors: [Mari Kong]
published: 2026-06-16
publisher: Figma Blog
---

# 4 Ways We're Using Our MCP Server at Figma

**Author:** Mari Kong (Product Marketing Manager, Figma — AI tools across design and code)
**Published:** 2026-06-16 — Figma Blog (Inside Figma / Product updates)

## Summary

Two months after opening the Figma canvas to agents, Figma's MCP server now reaches across the full platform — Figma Slides, FigJam, Figma Make, and the new Figma agent — meaning presentation decks, FigJam boards, and Make prototypes can all be created or updated from a prompt. The post catalogs four real internal workflows ("Figmates running them right now") and announces new MCP capabilities: write support spanning Slides/FigJam/Make/Figma agent, support for uploaded custom fonts (so a typeface on your machine renders correctly instead of a web-safe approximation), and a new `download_assets` tool that returns actual exportable files (SVG, PDF, JPG, PNG, or original source) from design files rather than screenshots. Across all four, the recurring theme is design-system-grounded generation: agents read your component library and variables and reuse them, producing output that is on-brand and built from your design system — and a consistent "first 80% done, human review pass still needed" cadence.

**Workflow 1 — Create and refresh decks in Figma Slides.** Designer advocate Mallory Dean maintains an evergreen deck of Figma's AI launches, refreshed every few weeks. She prompts from her code editor to update the deck with the new Figma agent, pulling content from Slack, Google Drive, the Shortcut blog, and Release Notes. The agent uses the `use_figma` tool plus the `/figma-use-slides` skill in Figma Slides to update the deck against her template, rendering type in her uploaded custom fonts. New slides still needed a review pass — image swaps and copy edits — but the first 80% of the content work was done. The same setup generalizes across PMs, designers, marketing, and sales building or updating decks.

**Workflow 2 — Generate FigJam boards from live data.** PM Prasant Lokinendi runs frequent feature-kickoff workshops and built `/figjam-builder`, a custom skill carrying his prep instructions so he doesn't re-prompt them each time. For the Make voice-to-text launch he prompted his agent to generate a FigJam board from context pulled across Slack, Asana, and Notion (project structure) plus Hex (analytics) — starting from up-to-date product vision, customer insights, and key decisions rather than an empty board. The post points readers to the Figma community skills directory and the community-resources repo for sharing custom skills.

**Workflow 3 — Move designs between code and canvas with Figma Make.** The MCP server now works in Figma Make, closing the loop from design edits to production PR without leaving Figma. Product designer Iris Lin branched code and built a real interactive audio editor in Figma Make (draggable/reorderable clips, a level-control popover, a scrubbing playhead). She brought the Make preview onto the canvas as design layers ("Can you bring back the preview here into Figma as design layers?"), rebuilt from the relevant components in her library, edited the audio-clip component with proper default/hover/drag states following her normal design patterns, then sent it back the other direction ("Pull those new states back into the code") — the agent wrote all three states into the component, ready to push to GitHub as a PR. The agent reads and writes real components on both ends, similar to how Code Connect maps a library to production code, so fidelity survives the round trip.

**Workflow 4 — Split the work with the Figma agent.** PM Yarden Katz (PM behind the MCP server) tackles a screen that exists only in code with no canvas representation, aiming to get it into Figma attached to the right design system. Working from a sample app (login flow + dashboard), she prompts from her code editor to push both into Figma, reusing existing components and variables where they exist and generating proper component sets/variables where they don't. The Figma plugin ships with skills giving the agent context on how to use Figma, so it reads her library in both Figma and the codebase and decides what to reuse vs build new. It produces a strong first pass, not finished — auto layout, fonts, and a few unmapped colors still need work. The canvas-native Figma agent then takes over with deep design-system context to fix layout, correct type, and map every color to the right variable; when done she pushes back to code through the MCP server. The `download_assets` tool can pull source images/icons directly without separate export. The post notes the Figma agent and Make's production-codebase integration are in closed beta; MCP write capabilities are in open beta.

## Key Points

- The Figma MCP server now works across **Figma Slides, FigJam, Figma Make, and the new Figma agent** — decks, boards, and prototypes can be created/updated from a prompt.
- **New capabilities announced:** write support across Slides/FigJam/Make/Figma agent; uploaded **custom font** support; new **`download_assets`** tool returning real exportable files (SVG/PDF/JPG/PNG or original source), not screenshots.
- **Skills guide agents** to better, more consistent outputs (`/figma-use-slides`, custom `/figjam-builder`); shareable via the Figma community skills directory and community-resources repo.
- **Workflow 1 (Slides):** evergreen AI-launch deck refreshed from a code-editor prompt pulling Slack/Drive/Shortcut blog/Release Notes; agent uses `use_figma` + `/figma-use-slides` skill; renders custom fonts on-brand; "first 80%" done, review pass for images/copy.
- **Workflow 2 (FigJam):** `/figjam-builder` custom skill generates a kickoff board from live data across Slack, Asana, Notion (structure) and Hex (analytics) — not an empty board.
- **Workflow 3 (Make):** design→code→canvas→code round-trip without leaving Figma; built interactive audio editor; brought Make preview onto canvas as design layers rebuilt from library components; edited component states (default/hover/drag); pushed states back to code as a GitHub PR. Agent reads/writes real components both ends (akin to Code Connect).
- **Workflow 4 (Figma agent):** code-only screen → canvas attached to the right design system; agent reads library in both Figma and codebase, reuses existing components/variables, builds new where missing; strong first pass (auto layout, fonts, unmapped colors still needed); canvas-native Figma agent finishes (layout, type, color→variable mapping), then push back to code via MCP.
- **Recurring themes:** design-system-grounded generation (output is on-brand, built from your library and tokens); "first 80% done"; a human review pass still required on every workflow.
- **Beta status:** Figma agent and Make's production-codebase integration in **closed beta**; MCP **write** capabilities in **open beta**.

> Short quoted excerpts:
> - "The Figma MCP server reaches further across the platform than it ever has."
> - "The new slides still needed a review pass... but the first 80% of the content work was already done by the time she jumped in."
> - On `download_assets`: "Unlike a screenshot, it returns the actual exportable file—SVG, PDF, JPG, or the original source image. No manual export needed."
> - "Design decisions that used to lose fidelity between handoff and review now travel all the way to the PR."
