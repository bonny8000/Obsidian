---
type: concept
status: active
created: 2026-06-17
updated: 2026-08-04
tags: [design-md, design-system, context-engineering, portability, ui-slop, agentic-engineering]
sources:
  - sources/atlassian-design-md
  - sources/nngroup-ux-context-design
confidence: 0.82
---

# DESIGN.md

> [!abstract] Summary
> An open-source Markdown format (originated by Google for the Stitch design tool) that captures a design system's brand and UI patterns as a single portable file. A two-part structure: machine-readable design tokens up top, human/agent-readable rationale for color, spacing, layout, elevation, and components below. Designed to be dropped into an AI agent's prompt to make generated UI feel on-brand instead of generic "slop."

> [!important] Why it Matters
> DESIGN.md is a fourth context primitive sitting beside [[concepts/infrastructure-dev/claudemd-context|AGENTS.md/CLAUDE.md]] (always-on project context), [[concepts/ai-agents/agent-skills|Agent Skills]] (on-demand procedural memory), and [[concepts/ai-agents/mcp-integration|MCP servers]] (external reach). It is the right primitive for *one-shot* and *portable* design-context jobs — and the wrong primitive for production codebases with an existing component library. Knowing which is which is now a routing decision design-systems teams have to make.

## 📝 Key Claims

- DESIGN.md captures **intent, not implementation.** It encodes design rationale and tokens, not the full technical spec of how the system works in production.
- The format has two parts: a machine-readable design-token block (front-matter style), then a human/agent-readable prose section covering color, spacing, layout, elevation, and components.
- **It fixes UI slop for one-shot generation.** With DESIGN.md attached, agents produce on-brand color/spacing/typography/elevation in one shot — exactly what Atlassian demonstrated at the Team '26 Figma Make + Teamwork Graph dashboard demo.
- **In a production codebase it underperforms MCP and Skills.** Atlassian's internal log-in-screen benchmark: DESIGN.md used ~92% more tokens than the ADS MCP, with ~2.7× the variance between runs.
- **Three structural limitations in production:**
  - **Loads everything every turn** — no on-demand fetching; context truncation kicks in earlier.
  - **Shortening kills sophistication** — Atlassian had to compress 2.5 MB of MCP-fetchable guidance into an 80 KB (~19,800 tokens) file, cutting usage guidance from 50+ components, trimming foundations, and dropping low-use tokens. Agents then read component implementations to recover missing context.
  - **It teaches re-implementation, not adoption** — because the spec describes how to *rebuild* the system, agents tend to re-create components (`<button>` from tokens) rather than import the existing one (`import Button from '@atlaskit/button'`). Direct tech-debt risk in established codebases.
- **DESIGN.md is "a guide on how to re-implement" the design system; MCP/Skills are "an instruction manual for using" it.** That distinction predicts which jobs each is right for.
- **Right primitive for these jobs:**
  - High-level artistic-direction documentation.
  - Quick prototyping in unfamiliar environments (no MCP available).
  - Interoperability with AI design tools that customize pre-built components.
  - Customer theming for adaptive UIs (admin uploads a DESIGN.md so AI-generated reports/dashboards feel like *their* brand).
- **Working token budget:** ~80 KB / ~19,800 tokens is on the larger side of community examples. If you can't fit your system in roughly that envelope, you probably need MCP/Skills on top.
- **The spec is still evolving.** No native theming support yet (Atlassian ships a non-standard dark-mode variant); Atlassian is feeding feedback upstream via GitHub.

## How to apply

- **Decide on the job.** If you're shipping production UI inside an existing codebase, prefer MCP + Skills + lint rules. If you're prototyping, doing customer theming, or shipping cross-tool, write a DESIGN.md.
- **Don't ship a DESIGN.md without checking whether it leaks internals.** If the spec describes proprietary token sets or component implementations you don't want exposed, that's a reason to keep the rich version behind an MCP and ship a slimmer DESIGN.md publicly.
- **Budget for the always-on cost.** Every turn pays the full DESIGN.md token cost. Treat that as active context budget per [[concepts/ai-agents/context-rot|Context Rot]] — keep the file lean and trust [[concepts/ai-agents/progressive-disclosure|Progressive Disclosure]] for everything that doesn't need to be always-on.
- **Watch for the canary signal.** If your agent is reading component implementations to find usage guidance, your DESIGN.md is missing something the agent needs — fix the file or move that knowledge into an MCP/Skill.
- **Consider a hybrid.** A small DESIGN.md as a brand snapshot up front, with deeper guidance fetched from MCP or `references/` inside a Skill on demand. Best-of-both-worlds for teams that already have MCP/Skills infrastructure.

## 🔗 Related Concepts

- [[concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]] — the broader Context Engine stack DESIGN.md sits inside.
- [[concepts/ai-agents/agent-skills|Agent Skills]] — the on-demand alternative for procedural design knowledge.
- [[concepts/ai-agents/mcp-integration|MCP Integration]] — the on-demand reach for component data and design tokens.
- [[concepts/infrastructure-dev/claudemd-context|CLAUDE.md / AGENTS.md Context]] — the always-on project-wide counterpart.
- [[concepts/ai-agents/progressive-disclosure|Progressive Disclosure]] — the principle DESIGN.md *doesn't* use.
- [[concepts/ai-agents/context-rot|Context Rot]] — the failure mode DESIGN.md becomes vulnerable to as it grows.
- [[concepts/infrastructure-dev/design-system-implementation|Design System Implementation]]
- [[concepts/infrastructure-dev/design-to-code-workflow|Design-to-Code Workflow]]
- [[concepts/infrastructure-dev/design-review-automation|Design Review Automation]]
- [[concepts/infrastructure-dev/color-token-architecture|Color Token Architecture]]
- [[concepts/ai-agents/vibe-design|Vibe Design]]
- [[concepts/ai-agents/vibe-coding|Vibe Coding]]
- [[comparisons/skills-vs-mcp-vs-agents-md|Comparison: Skills vs MCP vs AGENTS.md vs DESIGN.md]]

## ⚖️ Conflicts & Caveats

> [!warning] Single-team evidence
> Atlassian's production numbers come from one team, one task (log-in screen), and one set of internal tools. The ~92% / 2.7× figures are directional, not load-bearing for token budgeting.

> [!warning] Cache behavior unaddressed
> A static DESIGN.md should benefit from prompt caching. Atlassian's comparison doesn't say whether caching was on. If your stack uses prefix caching aggressively, the cost picture may shift.

> [!warning] Vendor lens
> Atlassian compared DESIGN.md against the MCP and skills they themselves built. The finding aligns with their incentives — which doesn't make it wrong, but warrants independent evaluation before universalizing.

## 📚 Sources

- [[sources/atlassian-design-md|Hall & Campbell (2026): Atlassian's DESIGN.md is here — what we learned testing portable design context in practice]] — primary source for the format and production limitations.
- [[sources/atlassian-design-system-context-engine|Christley & Radford (2026): Building the context engine for the AI era]] — companion piece situating DESIGN.md as one slice of a broader Context Engine stack.
- [[sources/agent-skills-day-3|Singhal et al. (2026): Agent Skills (Day 3)]] — situates the always-on-vs-on-demand split this concept lives inside.

## ❓ Open Questions

- Does prompt caching change the cost picture enough to make DESIGN.md competitive in production?
- Is there a real crossover point (small system, no MCP infra) where DESIGN.md beats Skills on TCO?
- What does a *customer-uploaded* DESIGN.md unlock for white-label AI features (admin uploads a brand kit; AI-generated reports respect it)?
- For Bonny's own bilingual slide system: should `bonny-slide-design` ship its own DESIGN.md analog, and what's the right token budget?
- **What is the `UX.md` equivalent worth shipping** — and would the five NN/g components survive the same TCO scrutiny applied to DESIGN.md above?

## DESIGN.md Cited as the Precedent for a Wider Practice

> [!important] Added 2026-08-04
> [[wiki/sources/nngroup-ux-context-design|NN/g (Alicea, 2026)]] uses DESIGN.md as **the existence proof** for a practice it names [[wiki/concepts/ux-research/ux-context-design|UX-Context Design]]: curating organisational knowledge into the context that steers generated output. The argument is that if machine-readable design values plus human-readable rationale works for the visual system, the same shape should carry research and behaviour.
>
> The proposed extension, a hypothetical **`UX.md`**, would hold research synthesis as *actionable constraints*, interaction standards, a glossary of the users' vocabulary, user models, and **world models** — the circumstances of use, which is the component with no traditional home.
>
> **Two things to keep straight.** First, the pattern NN/g takes from DESIGN.md is the **split**: machine-readable values for the generator, human-readable rationale for the reviewer who has to judge whether the generator got it right. That split is the transferable part.
>
> Second, **`UX.md` does not exist.** It is a proposal in an article — no format, no spec, no tool, no adoption. DESIGN.md has all four. Do not let secondary coverage present them as peers.

## Additional Sources

- [[wiki/sources/nngroup-ux-context-design|Alicea (2026): UX-Context Design]] — cites DESIGN.md as precedent; proposes `UX.md`.
