---
source_url: https://christinevallaure.substack.com/p/what-are-hypertokens-the-layer-between
captured: 2026-06-29
title: "What are hypertokens? The layer between tokens and components, rebuilt for agents."
authors: [Christine Vallaure]
published: 2026-06-28
publisher: Christine Vallaure (Substack — moonlearning.io)
---

# What are hypertokens? The layer between tokens and components, rebuilt for agents.

**Author:** Christine Vallaure — UX designer & educator, founder of moonlearning.io ("UX for designers"); focuses on the design–development gap, Figma, design systems, design tokens, and AI in UX/design. Published on her Substack, 2026-06-28.

**Capture status:** Full article retrieved via web_fetch. The original suggested URL was the Substack NOTE `substack.com/@christinevallaure/note/p-203929617`, which 302-redirects to the article `christinevallaure.substack.com/p/what-are-hypertokens-the-layer-between`; the redirect was followed and the article body was returned cleanly (not a JS shell). Quotes below are as returned by the fetch summarizer and should be re-verified verbatim against the live article before being quoted precisely in published work.

## Summary

Vallaure writes up "hypertokens" — a term **Jake Albaugh (Figma) coined at his Config 2026 talk** ("Jake Albaugh from Figma gave that gap a name: hypertokens") — a layer that sits **between design tokens and components**, holding *bundled* style decisions rather than single ones. Her thesis: design decisions naturally travel in groups (typography needs font-family + size + weight + line-height + letter-spacing together; a surface needs background + border + radius + shadow together), but today those bundles exist only as separately hand-copied versions across CSS, Figma styles, and iOS/Android code, which drift out of sync. A hypertoken is "a named bundle of style properties, defined once, that every tool's copy is built from" — a single upstream source of truth that compiles automatically into platform-specific outputs (CSS, Figma styles, Swift structs, etc.). The article frames this explicitly as a fix for the **AI-agent era**: agents don't paper over inconsistency the way humans do — they "build exactly what [they] find and guess the rest" — so giving them named, grouped, semantic bundles ("Surface.brand") instead of scattered raw property lists means less reconstruction, less code, and lower AI usage. The concept generalizes the W3C/DTCG "composite token" idea beyond its fixed predefined types to "any recurring fragment your own system has." It is presented as an exploration (Jake Albaugh's team at Figma, referenced from his Config 2026 talk), **not a shipped feature** — there is no "hypertoken button" in Figma as of June 2026.

## Key Points

- **Definition (verbatim):** a hypertoken is "a named bundle of style properties, defined once, that every tool's copy is built from." It is a single source of truth sitting **upstream of design tools**, compiling into platform-specific outputs (CSS, Figma styles, Swift structs) automatically.

- **The hierarchy / where it sits:** **Raw values → Tokens (single decisions) → Hypertokens (bundled decisions) → Components (structure, behavior, accessibility).** Hypertokens sit *between* tokens and components: they handle **style bundles** but carry **no behavioral logic** (logic/structure/a11y live in the component layer).

- **Problem it solves — bundles that drift:** Design decisions travel in bundled groups (typography = font-family + font-size + font-weight + line-height + letter-spacing, together). Today those bundles exist as **separate hand-copied versions across tools** (CSS classes, Figma styles, iOS/Android implementations) that **drift out of sync over time**. A hypertoken makes the bundle exist *once*, then generates each tool's copy.

- **The AI-agent argument (the "rebuilt for agents" angle):**
  - Verbatim: *"An agent doesn't smooth anything over. It builds exactly what it finds and guesses the rest."* Where humans intuitively reconcile slightly-inconsistent copies, an agent faithfully reproduces whatever scattered/ungrouped data it is handed.
  - When agents read scattered copies, they get **ungrouped property lists that require reconstruction.** Borrowing Jake Albaugh's metaphor: *"you asked for a cheese sandwich and got handed an encyclopedia on bread."*
  - Agents reading **semantic names like "Surface.brand"** require **less processing** than reverse-engineering raw values — i.e., grouping + naming is a token-efficiency and reliability win for AI build pipelines.

- **Examples of style bundles given:**
  - **Typography:** font-family, font-size, font-weight, line-height, letter-spacing bundled as one unit.
  - **Surfaces:** background, border, radius, shadow combined.
  - Also named: **spacing groups, transforms, motion clusters.**
  - **Specific case:** "**Surface.card**" carrying fill + border + radius + shadow, applied as a single unit.

- **Relation to W3C/DTCG composite tokens:** Hypertokens **generalize the composite token concept** (DTCG composite types include typography, shadow, border, gradient, transition, strokeStyle). The distinction: **composites offer fixed, predefined types; hypertokens allow "any recurring fragment your own system has."** (i.e., hypertokens = user-defined, open-ended composites.)

- **Tooling demonstration (Jake Albaugh, Figma):** A **JSON-based pipeline** compiled *one source* simultaneously into: **aliased variables with code syntax, component libraries, icon libraries, Code Connect documentation, base CSS, and Svelte presentation-layer components** (date picker, table, charts). **Reported outcome (verbatim):** *"less total code and lower AI usage for a better outcome."*

- **Status:** **Not yet shipped.** An exploration by Albaugh's team at Figma, referenced from his **Config 2026** talk. **No "hypertoken button" exists in current Figma (as of June 2026).**

- **Closing key quote (verbatim):** *"Precision up front is cheaper than cleanup later."*

## Follow-up

- Re-verify all quoted strings verbatim against the live article (the definition, "cheese sandwich/encyclopedia on bread," "less total code and lower AI usage," "Precision up front is cheaper than cleanup later") before quoting precisely.
- Capture Jake Albaugh's **Config 2026** talk directly (the primary demo source) — title, link, and any published JSON/pipeline artifacts; this article is a secondary write-up of his work.
- Check the **W3C Design Tokens Community Group (DTCG)** spec for the current list/definition of composite token types to confirm Vallaure's framing.
- Note whether Vallaure includes diagrams/code snippets in the original (the fetch returned prose; verify the layer diagram and any JSON examples).
