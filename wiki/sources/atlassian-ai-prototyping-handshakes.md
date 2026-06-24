---
type: source
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [design-system, ai-prototyping, mcp, agent-skills, context-engineering, hallucination-reduction, llms-txt, templates, atlassian]
source_path: raw/web/atlassian-ai-prototyping-handshakes-2026-06-22.md
source_url: https://www.atlassian.com/blog/how-we-build/turning-handoffs-into-handshakes-integrating-design-systems-for-ai-prototyping-at-scale
authors: [Lewis-Ethan Healey, Kylor Hall]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.8
---

# Atlassian: Turning Handoffs into Handshakes — Integrating Design Systems for AI Prototyping at Scale

**Authors:** Lewis-Ethan Healey (Lead Design Technologist — AI, Atlassian Design System) and Kylor Hall (Principal Prompt Engineer)
**Published:** 2025-11-26 — Inside Atlassian (How We Build)
**Raw capture:** [[raw/web/atlassian-ai-prototyping-handshakes-2026-06-22|atlassian-ai-prototyping-handshakes-2026-06-22]]
**URL:** [atlassian.com/blog/how-we-build/turning-handoffs-into-handshakes…](https://www.atlassian.com/blog/how-we-build/turning-handoffs-into-handshakes-integrating-design-systems-for-ai-prototyping-at-scale)
**Companion pieces:** [[sources/atlassian-design-system-context-engine|Christley & Radford (2026): Context Engine]] · [[sources/atlassian-design-md|Hall & Campbell (2026): DESIGN.md]] · see also [[comparisons/skills-vs-mcp-vs-agents-md|Skills vs MCP vs AGENTS.md vs DESIGN.md]]

## Citation

Healey, L.-E., & Hall, K. (2025, November 26). *Turning handoffs into handshakes: Integrating design systems for AI prototyping at scale.* Inside Atlassian (How We Build). Captured 2026-06-22 into `raw/web/atlassian-ai-prototyping-handshakes-2026-06-22.md`.

## Summary

This is the operational "how we built it" companion to Atlassian's two existing wiki sources — the strategic [[sources/atlassian-design-system-context-engine|Context Engine framing]] and the [[sources/atlassian-design-md|DESIGN.md case study]]. Where those explain *what* the Context Engine is and *which primitive wins in production*, this post documents *how* the Atlassian Design System (ADS) team actually taught AI prototyping tools to generate ADS-conformant UI at enterprise scale. The headline operational result: from a screenshot, AI prototyping reaches roughly **70% ADS accuracy in one pass**, improving over iterations. The framing is "handoffs into handshakes" — collapsing the linear design→engineering handoff into real-time collaboration, with AI taking first passes on ideation, UI comps, and PRDs.

The technical core is a hard-won retrospective on **reducing design-system hallucinations** (plausible-but-wrong outputs: bad imports, wrong token names, on-brand-looking but nonexistent icons, right component with wrong size/name). The team converged on ~**2,000 lines of custom instructions** focused on foundational elements (tokens, icons, buttons); found that a **single `guidelines.md` beats multiple per-component files** because most prototyping tools can't parse multiple files for context; and adopted a **table-of-contents-plus-high-priority-lines-at-the-top** structure that made generations faster and reduced hallucinations. Two further levers proved decisive: **templates** ("Fast" for speed, "Full" for complex interactions) bundling instructions, feature flags, navigation, and a theme switcher dropped errors to near zero; and **structured JSON configuration beats open-ended prompting** (editing a JSON config for logos/nav, rather than prompting code rewrites, drove logo hallucinations to near zero).

The final third is organizational and content-operational. Adoption scaled via a **champions program (6–10% of users)**, workshops, Loom walkthroughs, and an **AI Product Builders Week (~1,000 participants, 85% more confident afterward)**. Content is maintained as "**agentic content**" — structured building blocks (guidance, examples, types, keywords, metadata) per package, bootstrapped from AI-drafted **`llms.txt`** manifests and routed via an `offerings.json` schema — now powering a dozen+ tools including the `@atlaskit/ads-mcp` server, with **20k+ lines MCP-searchable** for development. Candid closer: prototypes look on-brand, but production-quality code at scale "remains challenging."

## Key Claims

- **~70% one-pass ADS accuracy from a screenshot**, improving over iterations. This is the central operational benchmark, and a more concrete figure than the [[sources/atlassian-design-system-context-engine|Context Engine post]]'s headline eval percentages.
- **~2,000 lines of custom instructions** are enough to ground foundational UI (tokens, icons, buttons); complex components live in the base template or are deferred.
- **A single `guidelines.md` beats multiple per-component files** (`button.md`, `typography.md`, …) — most prototyping tools struggle to parse multiple files for context. This is a direct, practical counterweight to the assumption that more granular = better.
- **Optimal single-file structure = table of contents + a few high-priority instruction lines at the top** (vendor-recommended); felt faster and reduced hallucinations.
- **Templates are the secret weapon.** Two templates — Fast (speed) and Full (complex interactions) — each bundle ADS instructions, feature flags, navigation, and a theme switcher. Hybrid templates + instructions dropped errors to **nearly zero**, especially for navigation; preconfigured code lets the model lean on real component APIs to recreate complex nav from an image.
- **Structured JSON config beats open-ended prompting to cut hallucinations.** Moving top-nav/logo choices into a JSON config (model edits config, not code) drove logo hallucinations to near zero. Stated lesson: "the more constraints we added, the more reliable the outputs became."
- **Three concrete tooling hurdles:** (1) public npm packages didn't work with AI prototyping tools → bumped a minor version of every component with a custom fix; (2) proprietary **Compiled** CSS-in-JS compiler unsupported → workaround ships per-component CSS in prototypes; (3) instruction-only imports were unreliable (and falsely self-reported as correct) → forced the template + instruction hybrid.
- **"Agentic content" is a maintained artifact**, not a one-off prompt: plain-language instructions, examples, and constraints, broken into structured building blocks (guidance, examples, types, keywords, metadata) per package via an `offerings.json` schema, bootstrapped from AI-drafted **`llms.txt`** manifests.
- **That content powers a dozen+ tools:** the MCP server `@atlaskit/ads-mcp`, AI prototyping tools, AI code editors, and multiple Rovo/Rovodev agents. Public tiers: **20k+ lines MCP-searchable** for dev, 5k "all" (50+ packages), 2k "fast" (8 packages), 2.5k "full" (17 packages).
- **Adoption is a cultural program, not a tool drop:** champions (6–10% of users) + workshops + Loom + office hours + self-serve courses; **AI Product Builders Week** with ~1,000 participants, **85% more confident** afterward, 77 Loom explainers, a playbook of 115 new AI use cases.
- **Templates organized via Atlassian's existing Figma library inheritance model** (core → local) — reusing a familiar mental model eased onboarding and kept generations aligned from the first prompt.
- **Candid limit:** prototypes look/feel like Atlassian, but generating production-quality code at scale "remains challenging," and the notion of "control" over UIs is shifting.

## Useful Examples

- **The single-file `guidelines.md` with a priority table of contents.** A concrete, copyable structure for any design-system context file fed to prototyping tools that can't parse multiple files.
- **Fast vs Full templates.** A two-tier template strategy (speed template vs complex-interaction template), each bundling instructions + feature flags + navigation + theme switcher — a reusable shape for "high-quality starting point every time."
- **The JSON-config-for-logos pattern.** "Change the top-left logo to Confluence" (prompt → hallucination) vs editing a top-nav JSON config the model touches instead of the implementation (hallucinations → near zero). The canonical example of "structured configuration beats open-ended prompting."
- **`llms.txt` → `offerings.json` content pipeline.** Bootstrapping agentic content from AI-drafted manifests, then restructuring into per-package building blocks routed to a dozen+ outputs.
- **The Compiled CSS-in-JS workaround** (ship a per-component CSS file in prototypes) — a concrete example of bridging proprietary tooling to AI tools that don't support a custom compiler.
- **The public content tiering** (20k+ MCP / 5k "all" / 2k "fast" / 2.5k "full") as a model for sizing design-system context to the consuming workflow.

## Constraints / Caveats

- **Single team, single design system, mostly qualitative.** Figures like ~70% one-pass accuracy and "near zero" hallucinations are Atlassian's own operational observations, not benchmarked results with a disclosed test set, model, or scoring rubric. Treat as directional.
- **No model named.** The post doesn't say which prototyping tools/models produced the ~70% figure, so it isn't apples-to-apples comparable.
- **Vendor lens.** Atlassian is describing its own ADS, MCP, and tooling; incentive aligns with the favorable narrative.
- **Tool-dependent findings.** "Single file beats multiple files" and "tools can't parse multiple files" are about *current* prototyping-tool limitations; the post itself hopes tools will soon fetch icons via TypeScript/MCP, which would change the calculus.
- **Participation-week stats are self-reported confidence** (85% "felt more confident"), not measured capability or output-quality gains. A related Atlassian post cites different framing numbers (1,400 invited, 108 presenters) for an AI Builders Week — treat headcounts as approximate.
- **Numbers will drift.** Line counts (2k, 5k, 20k+) and template counts reflect a fast-moving internal program described as "intentionally temporary and evolving."

## Design Implications

- **For Bonny's design-system / slide-system work:** the **single-file `guidelines.md` with a priority table of contents** is a directly adoptable structure for any context file fed to prototyping tools. Pair with the [[sources/atlassian-design-md|DESIGN.md]] 80 KB / ~19,800-token ceiling as a working budget.
- **Templates as the highest-leverage move.** When generation accuracy matters, invest in preconfigured templates (with nav, theme switcher, feature flags) before investing in more instruction text — the post is explicit that templates + instructions beat instructions alone.
- **Constrain, don't prompt, for deterministic edits.** Anything brand-critical or structurally sensitive (logos, navigation) should be a JSON config the agent edits, not free-text the agent rewrites. This is the practical, low-token sibling of the [[sources/atlassian-design-md|lint-rules-as-zero-token-feedback-loop]] idea.
- **Maintain "agentic content" as a first-class artifact.** Structured per-package building blocks + an `llms.txt` manifest is the shape of a design-context provider — not a token JSON dump. Mirrors the [[sources/atlassian-design-system-context-engine|Context Engine]] stack.
- **Adoption is a program, not a launch.** A champions cohort (~6–10%) plus learn-by-doing weeks is the replicable rollout pattern (see also [[comparisons/skills-vs-mcp-vs-agents-md]] for the primitive-routing side of the same effort).
- **Canary signal:** if the agent invents on-brand-looking icons that don't exist, your context is missing a machine-readable icon manifest (the post wants tools to fetch icons via package entry points / TypeScript / MCP).

## Tensions

- **Single file (this post) vs on-demand MCP fetching (the [[sources/atlassian-design-md|DESIGN.md]] post).** Here, a single `guidelines.md` wins for *prototyping tools that can't parse multiple files*; in production, on-demand MCP wins on tokens and accuracy. Both are true in different environments — the routing question from [[comparisons/skills-vs-mcp-vs-agents-md|the comparison]] decides which.
- **"More constraints = more reliable" vs the open-ended creativity prototyping is supposed to unlock.** Atlassian resolves this by constraining structure (templates, JSON config) while leaving content/layout open — guardrails, not handcuffs.
- **~70% one-pass accuracy (this post) vs the [[sources/atlassian-design-system-context-engine|Context Engine]] post's 52% accuracy *improvement*.** Different metrics (absolute one-pass conformance vs relative gain) — don't conflate them.
- **"Handshakes" collaboration narrative vs the candid admission that production-quality code at scale remains hard.** The optimism is about prototyping speed and on-brand fidelity; the honesty is about the production gap.

## Open Questions

- What is the ~70% figure measured against, and with which model/tool? Without that, it's directional only.
- Does the "single file beats multiple files" finding invert once prototyping tools gain robust multi-file / MCP context fetching (which the post anticipates)?
- How does the `offerings.json` / `llms.txt` building-block schema compare to the open DESIGN.md format and to AGENTS.md as a content-authoring discipline? Is there one authoring source feeding all three?
- What is the durable maintenance cost of "agentic content" once the system stabilizes (the team spent ~6 months "taming the complexity")?
- Could Bonny adopt a Fast/Full template split for slide/mock generation, with a JSON config for brand-critical elements?

## Concepts Linked

- [[concepts/infrastructure-dev/design-system-implementation|Design System Implementation]]
- [[concepts/infrastructure-dev/design-to-code-workflow|Design-to-Code Workflow]]
- [[concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]]
- [[concepts/infrastructure-dev/design-md|DESIGN.md]]
- [[concepts/infrastructure-dev/claudemd-context|CLAUDE.md / AGENTS.md Context]]
- [[concepts/infrastructure-dev/design-review-automation|Design Review Automation]]
- [[concepts/infrastructure-dev/color-token-architecture|Color Token Architecture]]
- [[concepts/infrastructure-dev/wireframe-generation|Wireframe Generation]]
- [[concepts/infrastructure-dev/design-automation|Design Automation]]
- [[concepts/infrastructure-dev/token-efficiency|Token Efficiency]]
- [[concepts/ai-agents/mcp-integration|MCP Integration]]
- [[concepts/ai-agents/agent-skills|Agent Skills]]
- [[concepts/ai-agents/vibe-design|Vibe Design]]
- [[concepts/ai-agents/vibe-coding|Vibe Coding]]
- [[comparisons/skills-vs-mcp-vs-agents-md|Skills vs MCP vs AGENTS.md vs DESIGN.md]]
- (new) concepts/infrastructure-dev/llms-txt — `llms.txt` instruction manifest as a machine-readable content entry point for agents/LLMs.
- [[concepts/infrastructure-dev/agentic-content|Agentic Content]] (new) — maintained, structured plain-language instructions/examples/constraints fed to agents, per-package building blocks routed to many outputs.
- [[concepts/infrastructure-dev/ai-prototyping|AI Prototyping]] (new) — preconfigured Fast/Full template strategy (instructions + nav + theme + feature flags) for reliable design-system-grounded generation.
- (new) concepts/infrastructure-dev/design-system-hallucination — plausible-but-wrong design-system outputs (bad imports, wrong tokens, nonexistent icons) and the constraint patterns that reduce them.

## LLM Use

- **Use for:** concrete, copyable patterns for grounding AI prototyping in a design system — single-file `guidelines.md` with a priority TOC, Fast/Full templates, JSON-config-over-prompting for brand-critical elements, and `llms.txt`/`offerings.json` content pipelines; justifying a champions-program rollout; citing ~70% one-pass screenshot accuracy as an operational (not benchmarked) data point.
- **Do not use for:** the ~70% figure as a generalizable benchmark (no model/test set named); claims of measured productivity gains (confidence stats are self-reported); production-code-quality guarantees (the post explicitly says this remains hard).
- **Best prompt pattern:** "Using Healey & Hall's Atlassian AI-prototyping playbook, design a design-system context setup for [tool]: specify the single-file guidelines structure (priority TOC), the template tiers, which brand-critical elements become JSON config vs prompt, and the agentic-content pipeline — then list the hallucination modes each choice mitigates."

## Reliability Notes

> [!warning] Caveats
> - **Operational, not benchmarked.** ~70% one-pass accuracy and "near zero" hallucinations are Atlassian's own observations; no model, test set, or rubric disclosed. Directional only.
> - **Vendor lens + fast-moving program.** Atlassian describing its own ADS/MCP/tooling; line counts and template details are "intentionally temporary and evolving."
> - **Tool-limitation-dependent findings.** "Single file beats multiple files" is contingent on current prototyping tools; the post anticipates this changing.
> - **Confidence:** 0.85 on the practical patterns (single-file guidelines, templates, JSON config, agentic content); 0.7 on the specific numbers (~70%, 2k/5k/20k lines, 85%); 0.9 on Atlassian's stated production stance.

## Backfill Status

- Newly written 2026-06-22 from a full web capture. All sections populated. No prior thin version to upgrade. Cross-linked to the two existing Atlassian companion sources and the Skills-vs-MCP comparison.
