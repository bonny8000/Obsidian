---
source_url: https://www.atlassian.com/blog/how-we-build/turning-handoffs-into-handshakes-integrating-design-systems-for-ai-prototyping-at-scale
captured: 2026-06-22
title: "Turning Handoffs into Handshakes: Integrating Design Systems for AI Prototyping at Scale"
authors: [Lewis-Ethan Healey, Kylor Hall]
published: 2025-11-26
publisher: Inside Atlassian (How We Build)
---

# Turning Handoffs into Handshakes: Integrating Design Systems for AI Prototyping at Scale

**Authors:** Lewis-Ethan Healey (Lead Design Technologist — AI, Atlassian Design System), Kylor Hall (Principal Prompt Engineer)
**Published:** 2025-11-26 — Inside Atlassian (How We Build) — est. 10 min read

## Summary

This is the operational "how we built it" companion to Atlassian's strategic Context Engine post and the DESIGN.md case study. It documents how the Atlassian Design System (ADS) team taught AI prototyping tools to generate UI that actually conforms to ADS — turning minimal prompts (and screenshots) into high-quality, on-brand prototypes at enterprise scale. The headline operational result: from a screenshot, AI prototyping reaches roughly 70% ADS accuracy in a single pass, improving over iterations. The piece frames AI as turning "handoffs into handshakes" — collapsing the linear design-to-engineering handoff into real-time collaboration, with AI taking first passes on ideation, UI comps, and PRDs so people focus on decisions rather than repetition.

The bulk of the article is a hard-won engineering retrospective on reducing design-system "hallucinations" (plausible-but-wrong outputs: bad imports, wrong token names, on-brand-looking but nonexistent icons, right component with wrong size/name). Key technical findings: public npm packages didn't work with AI prototyping tools (required a minor version bump of every component with a custom fix); the proprietary Compiled CSS-in-JS library isn't supported by most tools (temporary workaround: ship a per-component CSS file in prototypes); and instruction-only approaches produced unreliable imports. The team converged on roughly 2,000 lines of custom instructions focused on foundational elements (tokens, icons, buttons), and found that a single `guidelines.md` file beats multiple per-component files (e.g. `button.md`, `typography.md`) because most prototyping tools struggle to parse multiple files for context. The optimal structure places a table of contents plus a few high-priority instruction lines at the top of that single file — a vendor-recommended pattern that made generations faster and reduced hallucinations.

Two further levers proved decisive. Templates (a "Fast" template for speed, a "Full" template for complex interactions) bundle ADS instructions, feature flags, navigation, and a theme switcher; combining preconfigured code with focused instructions dropped errors to nearly zero and made screenshot-to-interactive-prototype possible in minutes, especially for navigation (the model leans on existing component APIs to recreate complex nav from an image). Structured JSON configuration beats open-ended prompting: moving top-nav/logo choices into a JSON config that the model edits — rather than rewriting code from a prompt like "Change the top-left logo to Confluence" — drove logo hallucinations to near zero. The stated lesson: the more constraints added, the more reliable the outputs.

The final third covers organizational scaling and content operations. To scale, every app/collection needs a template, organized using the same inheritance model Atlassian already used for Figma libraries (core → local hierarchy), which eased onboarding. Adoption was driven by a champions program (6–10% of users trained as experts), workshops, Loom walkthroughs, office hours, self-serve courses, and an AI Product Builders Week where 1,000+ Atlassians paused regular work (85% reported feeling more confident with AI afterward; outputs included 77 Loom explainers and a playbook of 115 new AI use cases). On the content side, Atlassian maintains "agentic content" — plain-language instructions, examples, and constraints fed to agents — starting from AI-drafted `llms.txt` manifests, broken into structured building blocks (guidance, examples, types, keywords, metadata) per package via an `offerings.json` schema. That content now powers a dozen+ tools including the `@atlaskit/ads-mcp` MCP server. They are beginning to share structured content publicly: 20k+ lines searchable through the MCP for development, 5k lines of "all" guidance for deep research (50+ packages), 2k lines of "fast" prototyping guidance (8 packages), and 2.5k lines of "full" prototyping guidance (17 packages). The candid closing note: prototypes look and feel like Atlassian, but generating production-quality code at scale remains challenging, and the notion of UI "control" is shifting.

## Key Points

- From a screenshot, AI prototyping reaches **~70% ADS accuracy in one pass**, improving across iterations.
- AI takes first passes on ideation, UI comps, and PRDs; teams focus on decisions, not repetition — "turning handoffs into handshakes."
- **Configuration hurdle:** public npm packages didn't work with AI prototyping tools → required bumping a minor version of every component with a custom fix.
- **Styling hurdle:** proprietary Compiled CSS-in-JS compiler unsupported by most tools → temporary workaround ships a per-component CSS file inside prototypes.
- **Imports hurdle:** instruction-only approaches got packages/code samples wrong (and falsely claimed correctness) → forced a hybrid of pre-coded templates + instructions.
- Converged on **~2,000 lines of custom instructions**, focused on foundational UI (tokens, icons, buttons); complex components handled in base template or deferred.
- **A single `guidelines.md` beats multiple per-component files** — most prototyping tools struggle to parse multiple files for context.
- Optimal single-file structure: **a table of contents + a few high-priority instruction lines at the top** (vendor-recommended); felt faster and reduced hallucinations.
- Hallucinations = plausible-but-wrong outputs: incorrect component imports, wrong token names, on-brand-looking icons that don't exist, wrong size/name applied to the right thing.
- **Templates as the secret weapon:** "Fast" (speed) and "Full" (complex interactions), each bundling ADS instructions, feature flags, navigation, theme switcher. Hybrid templates + instructions dropped errors to **nearly zero**, esp. for navigation.
- Preconfigured code improves screenshot matching: model leans on existing component APIs (even without explicit training) to recreate complex navigation from an image.
- **JSON config beats open-ended prompting:** moving top-nav/logo choices into a JSON config (model edits config, not code) drove logo hallucinations to near zero. "Structured configuration beats open-ended prompting; the more constraints we added, the more reliable the outputs became."
- Templates organized via Atlassian's existing **Figma library inheritance model (core → local)** for faster onboarding.
- **Champions program: 6–10% of users** trained as experts; amplified across ~1,000 product designers and PMs.
- **AI Product Builders Week:** 1,000+ Atlassians participated; **85% felt more confident** afterward; 77 Loom explainers; playbook of 115 new AI use cases. (A related post cites 1,400 invited and 108 presenters.)
- **"Agentic content"** = plain-language instructions, examples, constraints fed to agents/LLMs. Bootstrapped from AI-drafted `llms.txt` manifests; ~6 months "taming the complexity."
- Content broken into structured building blocks (guidance, examples, types, keywords, metadata) per package/offering, powered by an `offerings.json` schema; routes the right instructions to the right places.
- That content powers a dozen+ tools: the MCP server (`@atlaskit/ads-mcp`), AI prototyping tools, AI code editors, multiple Rovo and Rovodev agents.
- Publicly shared structured content tiers: **20k+ lines MCP-searchable for dev**, **5k lines "all" (deep research, 50+ packages)**, **2k lines "fast" (8 packages)**, **2.5k lines "full" (17 packages)**.
- Candid limits: production-quality code at scale "remains challenging"; discovery still a work in progress; "control" over UIs is shifting.

> Short quoted excerpts:
> - "From a screenshot, AI prototyping reaches about 70% Atlassian Design System accuracy in one pass, improving over iterations."
> - "structured configuration beats open‑ended prompting; the more constraints we added, the more reliable the outputs became."
> - "Agentic content is the practical, plain‑language instructions, examples, and constraints we feed to agents and LLMs so they know what to do and how to respond."
> - "With our hybrid approach of templates plus instructions, those errors dropped to nearly zero."
