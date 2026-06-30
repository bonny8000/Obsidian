---
source_url: https://christinevallaure.substack.com/p/a2ui-under-the-hood-designing-for
captured: 2026-06-29
title: "A2UI under the hood. Designing for the new era of radically adaptive UI."
authors: [Christine Vallaure]
published: 2026-06-17
publisher: Christine Vallaure (Substack / moonlearning.io)
---

# A2UI under the hood. Designing for the new era of radically adaptive UI.

**Author:** Christine Vallaure — UI designer, educator, founder of moonlearning.io ("UX for designers"); teaches Figma, design systems, design tokens, and agentic AI for design. Subtitle: "An introduction for designers." Published 2026-06-17 on christinevallaure.substack.com.

**Capture status:** Full via web_fetch. The original URL is a Substack NOTE (`substack.com/@christinevallaure/note/p-202424104`) that 302-redirects to the full article at `christinevallaure.substack.com/p/a2ui-under-the-hood-designing-for`; the article body was fetched and converted to markdown successfully (not JS-blocked). Slug renamed from the suggested `christinevallaure-202424104` to `christinevallaure-a2ui-generative-ui` based on the resolved title.

## Summary

A designer-facing introduction to **A2UI** ("Agent-to-UI"), an open protocol initiated by Google and refined by CopilotKit and others, for building **generative UI** (a.k.a. **radically adaptive UI**). The core shift: instead of one static design serving an "average user," the interface is **built fresh in the moment** for the exact person and the exact thing they asked for. A2UI's key safety move is **constraint**: the AI agent can only assemble interfaces from components that already exist in a designer-authored **catalog** (a machine-readable subset of the design system), so generated screens stay on-brand and high-quality instead of becoming generic "div soup." The article walks through how A2UI works end to end (request → server bundles request + catalog + instructions → LLM returns a JSONL "recipe" → renderer builds the screen from catalog components only), distinguishes the **design system** (human artifact) from the **catalog** (machine contract) from the **code** (runtime), and argues the catalog elevates designer authority: "the quality of every screen a user ever sees is set by what a designer put in it." It also flags the main failure mode (**quiet downgrade** when the catalog lacks the right component) and the unresolved **designer-machine gap** — Figma cleanly expresses only ~1/3 of CSS, and catalogs today still live as hand-authored code "just past Figma's edge," so a human must stay "in the seam" supervising the translation.

## Key Points

- **Exact title:** "A2UI under the hood. Designing for the new era of radically adaptive UI." Subtitle: "An introduction for designers." Author: Christine Vallaure. Published June 17, 2026.
- **Thesis quote:** *"The interface is built fresh in the moment, for the exact person or the exact thing they asked for."* Generative UI / radically adaptive UI replaces one-size-fits-all design and the "average user" persona with interfaces fitted to actual moments.
- **A2UI = protocol** developed by **Google** and refined by **CopilotKit** and others. It constrains AI-generated interfaces to **pre-designed components in a catalog**, ensuring quality/consistency rather than generic output.
- **How A2UI works (4 steps):**
  1. **User request** in plain language (running example: "I want a room in New York in March").
  2. **Agent processing** — a server-side program bundles the request with the catalog and instructions and passes it to an LLM.
  3. **Model generates a "recipe"** — the AI returns a structured **JSONL** description specifying which components to use and how to arrange them.
  4. **Rendering** — the renderer (the user's app) reads the recipe and builds the screen **using only catalog components**.
- **Verbatim recipe example** (JSONL, abbreviated in source):
  - `{ "version": "v0.9", "createSurface": { "surfaceId": "hotel-booking", "catalogId": "https://moonhotels.com/catalog/v1/catalog.json" } }`
  - then an `updateComponents` block whose `components` array nests `Column` → `Text` (variant `h1`, "Find your room in New York"), `DateRangePicker` (value path `/booking/dates`), `Stepper` (label "Guests", path `/booking/guests`), and a primary `Button` whose action fires event `search_hotels`.
- **Hotel-booking use case (contrast):** a traditional chatbot asks sequential questions (dates, then guests, then check-in/out) over multiple turns; the A2UI approach surfaces a **single interface** at once — calendar with visible prices, a guest stepper, and a search button.
- **Catalog vs. Design System vs. Code — "One idea, three layers: the system you think in, the contract you expose, the code that runs."**
  - **Design system** = the comprehensive human artifact: Figma libraries, coded components, tokens, documentation, design philosophy.
  - **Catalog** = the machine-readable **subset** exposed to the agent; the authorized "menu" of components and properties.
  - Catalogs are **not limited to primitives** (Button, Text); they can include complex branded components (HotelSelector, FlightCard) and complete pre-built, designed experiences.
- **Validation constraint (security):** *"The model can only name components that exist in the catalog."* The system validates against the catalog before and after generation, preventing invented widgets or made-up properties.
- **Failure mode — "Quiet Downgrade":** when the catalog lacks an appropriate component, the agent (a) defaults to the closest available component (often wrong), (b) falls back to generic A2UI baseline components, or (c) drops back to chat entirely. Example misfires: showing a **list instead of a map**; using a **stepper when a calendar** was appropriate. The validator catches technical errors but **not design misjudgments**: *"The only thing standing between the user and a near-miss interface is whether the catalog had the right piece in it."*
- **Designer authority elevated:** careful design work (naming, states, tokens, accessibility) used to feel like an "invisible tax"; now *"the catalog is the only thing the agent can build from, so the quality of every screen a user ever sees is set by what a designer put in it."*
- **Concrete designer tasks:**
  - **Task 1 — Build clean, structured files:** every state designed explicitly; semantic tokens carrying intentional meaning; names treated as contracts; mastery of components, variants, props, slots; added context traveling with components; all features understood inside-out.
  - **Task 2 — Know the gaps:** understand where Figma ends and human intervention begins; *"The catalog, like any other agentic design setup today, still lives as hand-authored code, just past Figma's edge."*
- **Figma vs CSS quantification:** **Figma cleanly expresses approximately one-third of CSS.**
  - **Well covered (visual/static):** layout, typography, color, spacing, components.
  - **Not covered (behavior/logic/runtime):** focus states, container queries, selectors, interactions, runtime-dependent properties.
  - Advocacy: *"You can generate stuff, but if you care about the creative process, you need a tool made for design, not a terminal."*
- **Designer-machine gap (core tension):** *"Design is thought on a canvas, with your hands, fast and visual, because that is the only way anything but generic comes out. The machine needs the opposite: a precise, structured, machine-readable source."* No tool bridges this cleanly today, so *"The person stays in the seam, on purpose"* — the human supervises the translation from creative vision to machine-readable spec.
- **Forward-looking:** *"The tool that finally lets a designer think on a canvas or similar creative environment and hand a machine clean-coded elements will decide how everything gets made."* Referenced as an opportunity at **Config 2026**.
- **Closing reframe (verbatim):** *"You do not need to learn to write a catalog in JSON. You need to become the person who makes a catalog worth writing."*
- **Related protocols / tools mentioned:** **A2UI** (primary; Google-initiated, open), **AG-UI**, **A2A**, **json-render** (Vercel), **MCP-UI**, **A2UI Agent SDK**, and an **A2UI demo tool by Southleft** at a2ui.southleft.com/demo.
- **Author self-description:** "Constitutionally incapable of writing a short article." Founder of moonlearning.io; author of a "Solo" book on independent product building; teaches UI design, Figma, and agentic AI for design systems.

## Follow-up

- Re-capture the **full verbatim JSONL examples** and any diagrams/screenshots (the fetch abbreviated the recipe and did not include images) to reach coverage: full.
- Confirm the exact **A2UI spec version** (`v0.9` appears in the example) and pull the canonical A2UI / AG-UI / A2A spec docs for a dedicated protocol concept page.
- Verify the **Southleft demo** (a2ui.southleft.com/demo) and the **A2UI Agent SDK** source/repo.
- Cross-check the "Figma expresses ~1/3 of CSS" claim against any source the author cites (appears to be her own estimate).
