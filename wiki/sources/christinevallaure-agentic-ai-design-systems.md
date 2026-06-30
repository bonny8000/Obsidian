---
type: source
status: active
created: 2026-06-29
updated: 2026-06-29
tags: [design-system, design-to-code, agentic-ai, figma, design-tokens, mcp, code-connect, figma-slots, storybook, design-to-code-workflow, ui-slop]
source_path: raw/web/christinevallaure-agentic-ai-design-systems-2026-06-29.md
source_url: https://substack.com/@christinevallaure/note/p-192722971
authors: [Christine Vallaure]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.82
---

# Christine Vallaure (2026): Agentic AI, Design Systems & Figma — A Practical Guide

**Christine Vallaure (moonlearning.io), published 2026-03-31 on Substack.**
**Raw capture:** [[raw/web/christinevallaure-agentic-ai-design-systems-2026-06-29|christinevallaure-agentic-ai-design-systems-2026-06-29]]
**URL:** [christinevallaure.substack.com/p/agentic-ai-design-systems-and-figma](https://christinevallaure.substack.com/p/agentic-ai-design-systems-and-figma) (via note [p-192722971](https://substack.com/@christinevallaure/note/p-192722971))

## Citation

Vallaure, C. (2026, March 31). *Agentic AI, Design Systems & Figma: A Practical Guide.* Christine Vallaure (Substack). Captured 2026-06-29 into `raw/web/christinevallaure-agentic-ai-design-systems-2026-06-29.md`.

## Summary

A practitioner essay arguing that agentic AI has changed what a design system *is*: no longer passive documentation for developers, but **executable instructions for a machine** that reads the system and assembles UI from it. Vallaure's central move is to reframe the AI shift as an *opportunity for more creative control* rather than a replacement threat — with a hard condition attached: the control only materializes if the Figma file and token architecture are built rigorously enough for a machine to parse unambiguously. The article is structured as a six-part Figma setup checklist (variables, property matching, complete states, slots, auto layout, Code Connect), wrapped in a craft argument: designers must protect the upstream work of *designing whole pages* (where the real "finding" happens) because pure assembly optimized for efficiency degrades into generic, interchangeable output. It connects the design-systems-as-context theme to concrete Figma mechanics and the tooling (MCP, Code Connect, Tokens Studio, Style Dictionary, Storybook) that makes a file machine-legible.

## Key Claims

- **A design system is now instructions, not documentation.** *"The design system is no longer just documentation for developers. It is instructions for a machine."* Agents read exactly what you specify and assemble faithfully — *"It will go exactly where you point it."*
- **The shift is an opportunity, conditional on rigor.** Designers gain more control over outcomes only if the system is thought through first; a sloppy file yields sloppy agent output.
- **Process over library — the page is where the finding happens.** *"The design system is a distilled finding. Designing the whole page is where the finding happened and hence not redundant."* Components earn their place from contextual page design, not isolated library upkeep.
- **The assembly risk = slop.** Systems optimized purely for efficiency produce generic, interchangeable UI; thorough creative work upstream is the antidote.
- **Six concrete file-setup requirements** (the actionable core):
  1. **Three-layer variables** — primitives (`blue/500 = #3B8BD4`), semantic tokens (`color/interactive/default`), optional component tokens. Agents read the *semantic* layer for meaning, not appearance.
  2. **Property matching** — Figma properties must equal code props exactly (names, capitalization, values); PascalCase component names matching code. *"If your Figma button has a property called 'Style' with values 'Filled' and 'Outlined', but the code component has a prop called variant with values primary and secondary, nothing maps cleanly."* Add component descriptions — Figma MCP feeds them to agents.
  3. **Complete state design** — hover, focus, active, disabled, error, empty, loading, skeleton; Variants for visual change, Booleans for toggles, Instance swap for slots; document the variant matrix's gaps. *"If your Star component only has a default story, the agent thinks that is the only state it has."*
  4. **Slots** — Figma's new feature (open beta 2026-03-05): defined drop zones that allow composability without detachment.
  5. **Auto layout standards** — auto layout everywhere, token-based spacing, intentional sizing (fill/hug/fixed), semantic layer names. *"A frame with auto layout and token-based spacing is a description. A frame with manually placed elements and hardcoded values is a picture."*
  6. **Code Connect** — explicit Figma↔code mapping; without it agents can't tell if a component already exists in the codebase and will duplicate it.
- **Tooling that makes a file machine-legible:** MCP (Model Context Protocol — Figma has one, Storybook has one), Figma Variables, Code Connect, Storybook (behavioral context via stories), Tokens Studio + Style Dictionary (transform tokens → CSS automatically).
- **Design-system quality is now measurable** — speed, token cost, code conformity — but those metrics only stay meaningful when the creative foundation is protected.

## Useful Examples

- **The `blue/500 = #3B8BD4` → `color/interactive/default` ladder** as a concrete illustration of primitive vs semantic token layers (and why the agent should bind to the semantic name).
- **The "Style" vs "variant" mismatch** as the canonical property-matching failure: a divergence in both the property name ("Style" vs "variant") and its values ("Filled"/"Outlined" vs primary/secondary) breaks the Figma→code mapping.
- **The Star-component-with-only-a-default-story** as the failure mode of incomplete state design — the agent assumes the documented state is the only state.
- **"Frame as description vs frame as picture"** — auto-layout + tokens encodes intent the machine can act on; manually placed elements with hardcoded values are an opaque bitmap to an agent.
- **The ~20-minute designer↔dev alignment conversation** (the article's phrasing: *"Twenty uncomfortable minutes, weeks saved."*): designers + devs agree on property names, values, capitalization, and semantic token structure *before* building.
- **Incremental migration of legacy files:** restructure your single most-used component fully (naming, states, token spacing, semantic layers), then continue — gradual beats an abandoned full rebuild.

## Constraints / Caveats

- **Practitioner opinion piece, not research.** No experiments, benchmarks, or measured token/cost numbers; claims are craft heuristics from an educator's vantage, not validated findings.
- **Figma-centric and tool-specific.** The whole checklist assumes Figma + its MCP + Code Connect + Variables; teams on other design tools must translate. Tool features cited (slots open beta 2026-03-05) are time-sensitive and may have changed since publication.
- **Vendor-feature adjacency.** Reads partly as enablement content for current Figma capabilities; the author also markets courses on this exact topic (moonlearning.io; a forthcoming "agentic AI for designers" course), so there is a soft commercial incentive to frame the workflow as essential.
- **Does not prove agents produce good UI** from a well-structured file — it argues the file is a *necessary* condition, and the author herself flags open questions about where visual review happens and how visual intent (shadow weight, type rhythm, breathing room) gets encoded.
- **Enterprise-skew acknowledged by the author:** most working implementations are enterprise-scale; small-team tooling is "absent."
- **Recency:** captured 2026-06-29 of a 2026-03-31 article — fast-moving space; verify Figma slots/MCP/Code Connect specifics against current release notes before relying on them.

## Design Implications

- **Treat the Figma file as a machine interface, not a deliverable.** The six requirements are a concrete pre-flight checklist for any [[concepts/infrastructure-dev/design-to-code-workflow|design-to-code workflow]] that hands off to an agent — apply them before expecting clean [[concepts/infrastructure-dev/ai-native-design-system|AI-native design system]] output.
- **Invest in [[concepts/infrastructure-dev/color-token-architecture|token architecture]] at the semantic layer.** Binding components to intent-named tokens (not raw values) is what lets an agent reason about *meaning*; this is the same instinct behind [[concepts/infrastructure-dev/design-md|DESIGN.md]] and the broader move to make design context machine-readable.
- **Name-parity between Figma and code is a hard dependency, not polish.** Property matching + Code Connect determine whether an agent *reuses* or *re-implements* components — directly governing [[concepts/infrastructure-dev/agentic-technical-debt|agentic technical debt]]. This echoes Atlassian's "import vs re-implement" finding (see [[sources/atlassian-design-md|Atlassian DESIGN.md]]).
- **Encode the full state matrix or the agent under-builds.** Skeleton/loading/empty/error states must exist in the file; otherwise generated UI silently omits them.
- **Protect the page-design step in research/product process.** Vallaure's "designing the whole page is where the finding happened" is a guardrail against [[concepts/infrastructure-dev/scaffold-design-system|scaffolded]] / [[concepts/ai-agents/vibe-design|vibe-designed]] output collapsing into sameness — keep a human "finding" phase upstream of agent assembly.
- **For Bonny's design-system / AI Hub tooling:** the ~20-minute designer↔dev alignment conversation is a cheap, high-leverage ritual to institutionalize before any agent-assisted handoff.

## Tensions

- **Creative control vs efficiency.** The article promises *more* designer control via agents, yet its own logic shows the easiest path (efficient assembly) actively erodes craft — the control is only realized through extra upstream discipline most teams skip.
- **Documentation vs instruction.** Reframing the system as "instructions for a machine" optimizes for machine legibility, which can conflict with the human/rationale value design systems also carry (the same static-context tension Atlassian's [[sources/atlassian-design-md|DESIGN.md]] write-up surfaces).
- **Enterprise rigor vs small-team reality.** The full six-part setup is heavy; the author admits viable implementations skew enterprise, leaving solo/small teams without proportionate tooling — yet they're the ones most tempted by fast agent assembly.
- **Tokens vs visual intent.** Tokens capture color/spacing cleanly but not "shadow weight, type rhythm, breathing room" — so a perfectly tokenized file can still produce on-spec-but-off-brand UI.

## Open Questions

- Where does *visual* review happen once agents compose components — tests verify function, not aesthetic fit. Who owns that gate?
- How do you encode visual intent (shadow weight, type rhythm, breathing room) that doesn't map to tokens yet?
- Quality governance: who keeps consistency when agents generate faster than humans can review?
- Will simpler agent-ready design-system tooling emerge for small teams, or stay enterprise-bound?
- Which platform unifies design + code + agentic AI in one environment (the "tool winner" question)?
- Does a fully machine-legible file measurably improve agent UI output, and by how much? (Unmeasured here.)

## Concepts Linked

- [[concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]]
- [[concepts/infrastructure-dev/design-to-code-workflow|Design-to-Code Workflow]]
- [[concepts/infrastructure-dev/color-token-architecture|Color / Token Architecture]]
- [[concepts/infrastructure-dev/design-system-implementation|Design System Implementation]]
- [[concepts/infrastructure-dev/design-md|DESIGN.md]]
- [[concepts/infrastructure-dev/scaffold-design-system|Scaffold Design System]]
- [[concepts/infrastructure-dev/figma-make|Figma Make]]
- [[concepts/infrastructure-dev/ai-prototyping|AI Prototyping]]
- [[concepts/infrastructure-dev/agentic-technical-debt|Agentic Technical Debt]]
- [[concepts/ai-agents/mcp-integration|MCP Integration]]
- [[concepts/ai-agents/vibe-design|Vibe Design]]
- [[concepts/ux-research/ai-native-ux-design|AI-Native UX Design]]
- [[concepts/ux-research/designing-for-agency|Designing for Agency]]
- Related sources: [[sources/atlassian-design-md|Atlassian: DESIGN.md]], [[sources/atlassian-design-system-context-engine|Atlassian Design System Context Engine]]
- New concept: [[concepts/infrastructure-dev/figma-code-connect|Figma Code Connect]]. (*Figma Slots* and the *"design system as instructions"* reframing were folded in rather than given their own pages — see [[concepts/infrastructure-dev/design-system-implementation|Design System Implementation]] and [[concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]].)

## LLM Use

- **Use for:** a concrete, opinionated checklist for making a Figma file agent-readable (three-layer tokens, property/name parity, full state matrix, slots, auto layout, Code Connect); framing language for "design system as instructions for a machine"; the craft argument for protecting whole-page design upstream of agent assembly.
- **Do not use for:** quantitative claims, benchmarks, or tool-comparison data (none present); authoritative/current Figma feature status (verify slots/MCP/Code Connect against release notes); evidence that machine-legible files actually improve agent output (asserted, not measured).
- **Best prompt pattern:** "Using Vallaure's six Figma setup requirements (three-layer variables, property matching, complete states, slots, auto layout, Code Connect), audit this component / file for agent-readiness and list the specific gaps." Or: "Draft the ~20-minute designer↔dev alignment agenda (property names, values, capitalization, semantic token structure) implied by this source."

## Reliability Notes

> [!warning] Caveats
> Practitioner opinion essay (Substack, 2026-03-31), not research — no data, benchmarks, or measured outcomes. Figma-specific and time-sensitive (slots cited as open beta 2026-03-05); verify current feature status. The author markets courses on this exact topic, so treat the "this is now essential" framing as having a soft commercial incentive. Captured via cross-host 302 redirect from a Substack note; body is an AI-authored faithful summary with load-bearing quotes preserved, not the full text. Confidence 0.82 — high on faithful representation of the article's content, lower on external validity of its claims.

## Backfill Status

- **Captured 2026-06-29:** full article fetched via redirect; thesis, all six setup requirements, every named tool, all author-raised open questions, practical recommendations, and load-bearing verbatim quotes preserved.
- **To reach coverage: full:** confirm exact wording of each of the six sections if needed for direct citation; capture any diagrams/screenshots (token-layer figure, variant matrix) dropped by the markdown fetch; verify Figma slots/MCP/Code Connect status against current release notes; track Vallaure's forthcoming "agentic AI for designers" course as a companion resource.
