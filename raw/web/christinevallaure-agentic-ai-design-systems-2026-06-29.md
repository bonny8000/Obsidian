---
source_url: https://substack.com/@christinevallaure/note/p-192722971
captured: 2026-06-29
title: "Agentic AI, Design Systems & Figma: A Practical Guide"
authors: [Christine Vallaure]
published: 2026-03-31
publisher: Christine Vallaure (Substack) / moonlearning.io
---

# Agentic AI, Design Systems & Figma: A Practical Guide

**Author:** Christine Vallaure — UI designer, speaker, founder of moonlearning.io ("UX for designers") and theSolo; teaches Figma, UI design, and product strategy.

**Capture status:** Full via web_fetch. The supplied Substack *note* URL (`/@christinevallaure/note/p-192722971`) 302-redirects cross-host to the full article at `https://christinevallaure.substack.com/p/agentic-ai-design-systems-and-figma`; that article was fetched and is the basis for this capture. Slug renamed to `christinevallaure-agentic-ai-design-systems` per the resolved title. Body is an AI-authored faithful summary with verbatim quotes where load-bearing; no full copyrighted text reproduced.

## Summary

Vallaure argues that with agentic AI, a design system has stopped being passive documentation for developers and has become **executable instructions for a machine**. Agents now read a design system and assemble UI from it faithfully — going exactly where the designer points. She frames this as an *opportunity for more creative control* (not a replacement threat), but it is conditional: the control only materializes if the underlying Figma file and token architecture are built rigorously enough for a machine to parse. The bulk of the article is a practical, six-part checklist for setting up a Figma file so agents can read it correctly, bookended by a craft argument that designers must protect the upstream creative work (designing whole pages, not just maintaining libraries) because pure assembly optimized for efficiency produces generic, interchangeable "slop."

Thesis quote: *"The design system is no longer just documentation for developers. It is instructions for a machine."*
Closing quote: *"The machine is fast. It will go exactly where you point it. Point carefully."*

## Key Points

**Framing / thesis**
- Agentic AI reads design systems *as executable instructions, not documentation*. The agent performs assembly work faithfully and reads exactly what designers specify.
- Positioned as a creative opportunity: designers gain more control over outcomes — *but only if* they've thought through the design system thoroughly first.
- Subtitle: *"The Figma basics you were told to get right just became the foundation for something much bigger."*

**Process over library (craft argument)**
- Good components don't emerge from isolated library maintenance; they result from designing complete pages first, where designers see how components interact contextually. The library is a *distilled finding* from real creative work.
- Verbatim: *"The design system is a distilled finding. Designing the whole page is where the finding happened and hence not redundant."*
- The assembly risk: systems optimized purely for efficiency produce generic, interchangeable output. Thorough creative work upstream prevents this degradation.

**Six file-setup requirements**

1. **Variables architecture — three layers.**
   - Primitives: raw values (example given: `blue/500 = #3B8BD4`).
   - Semantic tokens: intent-based naming (example: `color/interactive/default`).
   - Component tokens: optional, for complex systems.
   - Principle: agents read the *semantic* layer to understand meaning, not appearance.

2. **Property matching.** Figma component properties must match code props exactly — same names (capitalization, spelling), same values; component names in PascalCase matching code exactly.
   - Verbatim: *"If your Figma button has a property called 'Style' with values 'Filled' and 'Outlined', but the code component has a prop called variant with values primary and secondary, nothing maps cleanly."*
   - Add descriptions to all components — the Figma **MCP (Model Context Protocol)** reads these and provides context to agents.

3. **Complete state design.** Every possible state must exist: hover, focus, active, disabled, error, empty, loading, skeleton.
   - Variants for visual changes; Booleans for on/off toggles; Instance swap for slotted elements; document gaps in the variant matrix.
   - Verbatim: *"If your Star component only has a default story, the agent thinks that is the only state it has."*

4. **Slots (new feature).** Figma introduced slots in **open beta on March 5, 2026**. Slots provide defined drop zones within components, preventing detachment and maintaining component integrity. Named slots specify exact content areas; enable composable components without detachment.

5. **Auto layout standards.** Every component uses auto layout; token-based spacing on all gaps and padding; intentional sizing (fill, hug, or fixed); semantic layer naming.
   - Verbatim: *"A frame with auto layout and token-based spacing is a description. A frame with manually placed elements and hardcoded values is a picture."*

6. **Code Connect.** Maps Figma components to their code counterparts. Without it, agents cannot tell whether a Figma component corresponds to an existing codebase component — forcing them to generate duplicates.

**Tools & concepts named**
- **MCP (Model Context Protocol):** standardized way for AI agents to read tool information. Figma has one; Storybook has one.
- **Figma Variables** — managing tokens across the three layers.
- **Code Connect** — explicit Figma-to-code component mapping.
- **Storybook** — component documentation/testing; provides behavioral context through "stories."
- **Tokens Studio & Style Dictionary** — tools for transforming tokens into CSS classes automatically.
- **Figma Slots** — new composability feature (open beta 2026-03-05).

**Open questions / gaps the author raises**
- *Visual truth location:* once agents compose components, where does review happen? Tests verify functionality, not aesthetic fit.
- *Visual intent encoding:* shadow weight, type rhythm, breathing room — brand elements that don't map cleanly to tokens yet.
- *Quality governance:* who ensures consistency as agents generate components faster than humans can review?
- *Market access:* most working implementations are enterprise-scale; simpler tooling for smaller teams is absent.
- *Tool winner:* which platform will unify design, code, and agentic AI in one environment?

**Practical recommendations**
- *Existing files:* pick your most-used component and restructure it completely (naming, all states, token-based spacing, semantic layers), then continue incrementally. Gradual improvement beats abandoned complete rebuilds.
- *Teams:* before building anything, developers and designers must align on property names, values, capitalization, and semantic token structure — described as roughly twenty minutes of conversation that saves weeks of rework (verbatim: *"Twenty uncomfortable minutes, weeks saved."*).
- *File structure:* name pages and layers semantically; "Page 1" and "Rectangle 3" give no navigational context for humans or agents.

**Conclusion**
- The risk isn't replacement — it's that efficient assembly replaces the conditions that make assembly meaningful. Design-system quality now has measurable metrics attached (speed, token cost, code conformity), but only when creative foundations remain protected.

## Follow-up

- Re-capture the article body verbatim if exact wording of any of the six sections is needed for citation (current capture preserves the load-bearing quotes but paraphrases surrounding prose).
- Confirm whether the article includes screenshots/diagrams of the three-layer token structure or the variant matrix (the markdown fetch would have dropped images).
- Vallaure notes she is "currently developing a course on agentic AI for designers" — worth tracking on moonlearning.io for a deeper companion resource.
- Verify the Figma slots open-beta date (2026-03-05) and any GA change against Figma's release notes when precision matters.
