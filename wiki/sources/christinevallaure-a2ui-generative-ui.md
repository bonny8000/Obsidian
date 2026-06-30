---
type: source
status: active
created: 2026-06-29
updated: 2026-06-29
tags: [a2ui, generative-ui, radically-adaptive-ui, component-catalog, design-system, design-to-code, figma, design-tokens, agentic-design, agent-ui-protocol]
source_path: raw/web/christinevallaure-a2ui-generative-ui-2026-06-29.md
source_url: https://christinevallaure.substack.com/p/a2ui-under-the-hood-designing-for
authors: [Christine Vallaure]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.82
---

# Christine Vallaure (2026): A2UI Under the Hood — Designing for Radically Adaptive UI

**Christine Vallaure (moonlearning.io), 2026-06-17.**
**Raw capture:** [[raw/web/christinevallaure-a2ui-generative-ui-2026-06-29|christinevallaure-a2ui-generative-ui-2026-06-29]]
**URL:** [a2ui-under-the-hood](https://christinevallaure.substack.com/p/a2ui-under-the-hood-designing-for)

> [!note] Capture provenance
> The note URL (`substack.com/@christinevallaure/note/p-202424104`) 302-redirects to the full article, which was fetched cleanly (not JS-blocked). Body, quotes, and the JSONL example were captured via web_fetch; the recipe example was abbreviated and images were not captured, so coverage is **substantial**, not full.

## Citation

Vallaure, C. (2026, June 17). *A2UI under the hood. Designing for the new era of radically adaptive UI* [An introduction for designers]. christinevallaure.substack.com. Captured 2026-06-29 into `raw/web/christinevallaure-a2ui-generative-ui-2026-06-29.md`.

## Summary

A designer-facing primer on **A2UI** ("Agent-to-UI"), an open protocol initiated by **Google** and refined by **CopilotKit** and others, for building **generative UI** / **radically adaptive UI**. The premise: rather than ship one static design for an "average user," the interface is "built fresh in the moment, for the exact person or the exact thing they asked for." A2UI's safety mechanism is **constraint** — the agent may only assemble screens from components a designer has published into a machine-readable **catalog**, so output stays on-brand and high-quality instead of degrading into generic generated layouts. Vallaure traces the full loop (plain-language request → a server bundles request + catalog + instructions for an LLM → the model returns a structured **JSONL "recipe"** → a renderer builds the screen using catalog components only), then separates three layers — "the system you think in" (design system), "the contract you expose" (catalog), "the code that runs." Her central argument for designers: the catalog is the *only* source the agent can draw from, so "the quality of every screen a user ever sees is set by what a designer put in it" — turning previously-invisible craft (states, semantic tokens, naming, accessibility) into the load-bearing input. She is candid about limits: the dominant failure mode is the **quiet downgrade** when the catalog lacks the right component (e.g. a list instead of a map), validators catch technical but not design errors, **Figma cleanly expresses only ~1/3 of CSS**, and catalogs today still live as hand-authored code "just past Figma's edge" — so a human must stay "in the seam, on purpose."

## Key Claims

- **Generative / radically adaptive UI replaces one-size-fits-all design.** Thesis quote: "The interface is built fresh in the moment, for the exact person or the exact thing they asked for." The "average user" persona gives way to interfaces fitted to actual moments.
- **A2UI is an open protocol** (Google-initiated, refined by CopilotKit and others) that constrains AI-generated UIs to **pre-designed catalog components**, preventing "div soup" / generic output.
- **The 4-step A2UI loop:** (1) plain-language request → (2) server bundles request + catalog + instructions for the LLM → (3) model returns a structured **JSONL recipe** of components and arrangement → (4) renderer builds the screen from catalog components only.
- **"One idea, three layers: the system you think in, the contract you expose, the code that runs."** The **design system** is the full human artifact (Figma libraries, coded components, tokens, docs, philosophy); the **catalog** is the machine-readable *subset* exposed to the agent (the authorized menu of components + properties); the **code** is the runtime.
- **Catalogs can hold more than primitives.** Beyond Button/Text, a catalog can expose complex branded components (HotelSelector, FlightCard) and complete pre-built, designed experiences.
- **Validation is the security boundary:** "The model can only name components that exist in the catalog." The system validates against the catalog before and after generation, blocking invented widgets or made-up props.
- **Quiet downgrade is the main failure mode:** when the catalog lacks the right component, the agent defaults to the closest (often wrong) component, falls back to generic baseline components, or drops back to chat. The validator catches technical errors, **not design misjudgments** — "the only thing standing between the user and a near-miss interface is whether the catalog had the right piece in it."
- **The catalog elevates designer authority:** craft that felt like an invisible "tax" (naming, states, tokens, accessibility — "worthy, invisible, first to be cut") is now decisive — "the quality of every screen a user ever sees is set by what a designer put in it."
- **Figma expresses ~1/3 of CSS.** Well covered: layout, typography, color, spacing, components. **Not covered:** focus states, container queries, selectors, interactions, runtime-dependent properties. Catalogs therefore "still live as hand-authored code, just past Figma's edge."
- **The designer–machine gap is unresolved.** Design is "thought on a canvas, with your hands, fast and visual"; the machine needs "a precise, structured, machine-readable source." No tool bridges this cleanly, so "the person stays in the seam, on purpose."
- **Reframe for the audience:** "You do not need to learn to write a catalog in JSON. You need to become the person who makes a catalog worth writing."

## Useful Examples

- **Hotel-booking recipe (JSONL).** `createSurface` names a `surfaceId` ("hotel-booking") and a remote `catalogId` (`https://moonhotels.com/catalog/v1/catalog.json`); `updateComponents` nests a `Column` → `Text` (h1 "Find your room in New York"), `DateRangePicker` (value path `/booking/dates`), `Stepper` ("Guests", path `/booking/guests`), and a primary `Button` firing event `search_hotels`. Spec `"version": "v0.9"`.
- **Chatbot vs. A2UI contrast.** Traditional chatbot: sequential turns (dates → guests → check-in/out). A2UI: one interface at once — calendar with visible prices + guest stepper + search button.
- **Quiet-downgrade misfires:** showing a **list instead of a map**; using a **stepper when a calendar** was appropriate.
- **Ecosystem name-drops:** **AG-UI**, **A2A**, **json-render** (Vercel), **MCP-UI**, **A2UI Agent SDK**, and a **Southleft A2UI demo** (a2ui.southleft.com/demo).

## Constraints / Caveats

- **Single-author educational explainer**, not a spec or peer-reviewed work; framing and the "~1/3 of CSS" figure appear to be the author's own estimates.
- **Vendor/ecosystem optimism flag (mild):** the author runs a paid design-education business (moonlearning.io) and the piece doubles as positioning for "designers in the agentic era"; treat the empowerment framing ("designer authority is elevated") as advocacy, not measured outcome.
- **Recency / volatility:** A2UI is at `v0.9` and the surrounding protocols (AG-UI, A2A, MCP-UI) are early; specifics will move.
- **Does NOT prove** that constrained-catalog generative UI ships better real-world UX than static design or chat — no studies, metrics, or A/B evidence; the failure modes are acknowledged but not quantified.
- Recipe example was abbreviated in capture; images/diagrams not captured.

## Design Implications

- **Treat the design system as a machine contract, not just a human artifact.** The catalog is the agent's only palette, so [[concepts/infrastructure-dev/ai-native-design-system|AI-native design systems]] must publish a curated, validated, machine-readable subset — explicit states, [[concepts/infrastructure-dev/color-token-architecture|semantic tokens]], contractual names, props/slots — turning [[concepts/infrastructure-dev/design-system-implementation|design-system implementation]] into the quality ceiling for every generated screen.
- **Design the catalog's coverage, not just its components.** Because the dominant failure is the **quiet downgrade**, gap analysis ("which requests have no right component?") becomes a first-class design activity — adjacent to [[concepts/ux-research/designing-for-agency|designing for agency]] and graceful degradation, since the fallback (wrong component / chat) is what the user actually feels.
- **Keep a human "in the seam."** This is a [[concepts/infrastructure-dev/design-to-code-workflow|design-to-code workflow]] problem: Figma covers ~1/3 of CSS, so the catalog lives as hand-authored code past Figma's edge. Tooling like [[concepts/infrastructure-dev/figma-make|Figma Make]] and [[concepts/infrastructure-dev/ai-prototyping|AI prototyping]] partially close the gap, but supervision of the translation remains the designer's job.
- **Contrast with deterministic UI.** A2UI is a constrained form of [[concepts/ux-research/generative-ui|generative UI]] that pulls it back toward [[concepts/infrastructure-dev/deterministic-ui|deterministic UI]] guarantees via catalog validation — a useful middle path for [[concepts/ux-research/ai-native-ux-design|AI-native UX design]].
- **Position the catalog as an agent-experience surface.** The recipe/renderer split is an agent-to-UI protocol; it belongs in the [[concepts/agent-experience/agent-transparency|agent-experience]] conversation about how agents render and how users trust generated screens.

## Tensions

- **Creative canvas vs. machine-readable source** — the core unresolved tension; design wants fast/visual, the machine wants precise/structured, and no tool bridges it cleanly yet.
- **Designer empowerment vs. quiet downgrade** — the catalog gives designers unprecedented control *and* makes them the single point of failure; an incomplete catalog silently degrades UX.
- **Generative freedom vs. constraint** — A2UI's value comes from *restricting* the model to a catalog, the opposite of open-ended generation, trading flexibility for brand/quality safety.
- **Figma as the design home vs. Figma's ~1/3-of-CSS ceiling** — advocates staying in a design tool while admitting the catalog must be authored in code beyond it.

## Open Questions

- Does constrained-catalog generative UI measurably beat static design or chat on task success / satisfaction? (No evidence given.)
- How is catalog *coverage* governed and tested so quiet downgrades are caught before users see them?
- What is the canonical A2UI spec (at `v0.9`), and how do A2UI, AG-UI, A2A, MCP-UI, and Vercel json-render relate / compete?
- What tooling could finally let a designer "think on a canvas" and emit clean catalog code (the Config 2026 opportunity)?
- Who owns the catalog and its validation rules in practice — design, engineering, or a shared design-systems function?

## Concepts Linked

- [[concepts/ux-research/generative-ui|Generative UI]] (radically adaptive UI; primary)
- [[concepts/infrastructure-dev/deterministic-ui|Deterministic UI]] (the contrast A2UI partly reclaims)
- [[concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]]
- [[concepts/infrastructure-dev/design-to-code-workflow|Design-to-Code Workflow]]
- [[concepts/infrastructure-dev/design-system-implementation|Design System Implementation]]
- [[concepts/infrastructure-dev/color-token-architecture|Color Token Architecture]]
- [[concepts/infrastructure-dev/scaffold-design-system|Scaffold Design System]]
- [[concepts/infrastructure-dev/figma-make|Figma Make]]
- [[concepts/infrastructure-dev/ai-prototyping|AI Prototyping]]
- [[concepts/infrastructure-dev/design-md|design.md]]
- [[concepts/ai-agents/vibe-design|Vibe Design]]
- [[concepts/ux-research/ai-native-ux-design|AI-Native UX Design]]
- [[concepts/ux-research/designing-for-agency|Designing for Agency]]
- [[concepts/agent-experience/agent-transparency|Agent Transparency]]
- Proposed new: [[concepts/infrastructure-dev/component-catalog|Component Catalog]] (the machine-readable design-system subset an agent builds from)
- Proposed new: [[concepts/agent-experience/a2ui-protocol|A2UI Protocol]] (Agent-to-UI generative-rendering protocol)
- Related sources: [[sources/aidesign-guide-catalog|The AI Design Guide]] · [[sources/figma-mcp-server-four-ways|Figma MCP Server Four Ways]] · [[sources/drs2026-generative-events-design-ontology|DRS 2026: Generative Events & Design Ontology]] · [[sources/atlassian-design-system-context-engine|Atlassian Design System Context Engine]]

## LLM Use

- **Use for:** explaining A2UI / generative UI to designers; the 4-step request→recipe→render loop; the design-system vs. catalog vs. code distinction; arguing why a machine-readable component catalog raises (and gates) UX quality; enumerating failure modes (quiet downgrade) and the Figma-vs-CSS coverage gap.
- **Do not use for:** authoritative A2UI spec details (verify against canonical docs — this is a v0.9 explainer); empirical claims that generative UI outperforms static/chat (none provided); exact verbatim JSONL beyond what is captured (abbreviated here).
- **Best prompt pattern:** "Using Vallaure's A2UI model, draft a component-catalog plan for [product]: list candidate catalog components (primitives + branded + full experiences), the requests each covers, and the gaps that would trigger a quiet downgrade — then state what a designer must lock down (states, semantic tokens, names, props/slots) for each."

## Reliability Notes

> [!warning] Caveats
> Single-author educational explainer from a design educator with a commercial course business; empowerment framing is advocacy, not evidence. A2UI is at v0.9 and the ecosystem is volatile. The "Figma expresses ~1/3 of CSS" figure and the failure-mode taxonomy are the author's framing, not measured results. Confidence 0.82 on faithful capture of *what the article argues*; lower on any forward-looking or comparative claim.

## Backfill Status

- Captured 2026-06-29: full thesis, the 4-step loop, the abbreviated hotel-booking JSONL recipe, the three-layer (system/catalog/code) model, failure modes, designer tasks, the Figma/CSS gap, ecosystem name-drops, and the verbatim quotes above.
- To reach **coverage: full** — re-capture the complete unabridged JSONL examples and any diagrams/screenshots; pull the canonical A2UI / AG-UI / A2A / MCP-UI spec docs; verify the Southleft demo and A2UI Agent SDK; and stand up the two proposed concept pages ([[concepts/infrastructure-dev/component-catalog|Component Catalog]], [[concepts/agent-experience/a2ui-protocol|A2UI Protocol]]).
