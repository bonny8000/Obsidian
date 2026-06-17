---
type: source
status: active
created: 2026-06-17
updated: 2026-06-17
tags: [design-md, design-system, mcp, agent-skills, context-engineering, ui-slop, atlassian, vibe-coding]
source_path: raw/web/atlassian-design-md-2026-06-17.md
source_url: https://www.atlassian.com/blog/ai-at-work/atlassians-design-md-is-here-what-we-learned-testing-portable-design-context-in-practice
authors: [Kylor Hall, Andrew Campbell]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.85
---

# Atlassian: DESIGN.md — Portable Design Context in Practice

**Authors:** Kylor Hall (Principal Prompt Engineer) and Andrew Campbell (Senior Design Technologist)
**Published:** 2026-06-15 — Atlassian Blog (AI at Work)
**Raw capture:** [[raw/web/atlassian-design-md-2026-06-17|atlassian-design-md-2026-06-17]]
**URL:** [atlassian.com/blog/ai-at-work/atlassians-design-md-is-here…](https://www.atlassian.com/blog/ai-at-work/atlassians-design-md-is-here-what-we-learned-testing-portable-design-context-in-practice)
**Live files:** atlassian.design/DESIGN.md

## Citation

Hall, K., & Campbell, A. (2026, June 15). *Atlassian's DESIGN.md is here: what we learned testing portable design context in practice.* Atlassian Blog (AI at Work). Captured 2026-06-17 into `raw/web/atlassian-design-md-2026-06-17.md`.

## Summary

Atlassian tested **DESIGN.md** — an open-source Markdown format originated by Google for the Stitch design tool — as a portable snapshot of a design system that can be dropped into an AI agent's prompt to combat "UI slop." Their finding: DESIGN.md works *well* for one-shot prototypes, theming, and tool interoperability where MCP/skills aren't available, but **performs worse than MCP or Agent Skills inside a production codebase** because it loads everything every turn, has to shrink past usefulness to fit, and teaches agents to *re-implement* components rather than import existing ones. Their head-to-head test on a log-in screen showed DESIGN.md used ~92% more tokens than the ADS MCP, with ~2.7× the variance between runs.

The piece is significant because it gives a concrete production data point on the **Skills vs MCP vs AGENTS.md** routing question, and it adds a fourth primitive (DESIGN.md) to the static-vs-dynamic context taxonomy from the [[sources/the-new-sdlc-with-vibe-coding-day-1|Day-1 SDLC paper]].

## Key Claims

- **The slop problem has a context cause.** Without brand/component/pattern context, AI defaults to "the average of everything it's trained on. Generic in, generic out."
- **DESIGN.md is portable design context, not a full design system spec.** Two parts: machine-readable design tokens up top; human/agent-readable rationale for color, spacing, layout, elevation, and components below. Captures *intent*, not implementation.
- **DESIGN.md fixes slop for one-shot prototyping.** At the Team '26 keynote, a Figma Make dashboard demo used DESIGN.md to align generated output with Atlassian's design language in one shot without needing internal MCP. Color, spacing, shape, typography, and elevation all came out correct.
- **In production it underperforms MCP and Skills** (one production task, log-in screen):

  | Approach | Design system context | Avg tokens | Avg time | Avg turns |
  | --- | --- | --- | --- | --- |
  | No context | ~5% | 4.20M | 6m 19s | 43 |
  | ADS MCP | ~80% | 3.75M | 5m 1s | 35.1 |
  | ADS skill | ~80% | 4.43M | 5m 23s | 36 |
  | DESIGN.md | ~30% | 7.21M | 6m 46s | 45.3 |

  DESIGN.md used ~92% more tokens than ADS MCP and had ~2.7× variance between runs.
- **Three structural limitations in production:**
  1. **Loads all at once, not on demand.** Higher cost and slower from the start; context truncation occurs in fewer turns, reducing accuracy.
  2. **Shortening kills sophistication.** ADS-on-demand: ~2.5 MB. DESIGN.md (loaded every turn): trimmed to **80 KB ≈ 19,800 tokens (~10,700 without frontmatter)**. Had to cut usage guidance from 50+ components, trim foundation guidance heavily, and drop low-use tokens. Agents then read component implementations to recover the missing guidance.
  3. **It teaches re-implementation, not adoption.** Because the spec describes *how to rebuild* the system, agents tend to re-create components rather than import existing ones (e.g. write a styled `<button>` instead of `import Button from '@atlaskit/button'`). This is direct tech-debt risk in an established codebase.
- **DESIGN.md is excellent at four jobs that have nothing to do with production code:**
  - High-level artistic direction documentation.
  - Quick prototyping in unfamiliar environments (no MCP available).
  - Interoperability with AI design tools that assemble UI from pre-built components.
  - Customer theming for adaptive UIs (an admin uploads their own DESIGN.md so dynamic dashboards/reports feel like *their* brand, not Atlassian's).
- **Lint rules act as a zero-token-cost positive feedback loop** alongside MCP/skills — they enforce coding standards for humans and agents alike with no token spend at all.
- **MCP and skills are an "instruction manual for using" the design system; DESIGN.md is "a guide on how to re-implement" it.** That framing predicts which jobs each is right for.
- Atlassian is shipping its DESIGN.md files publicly at `atlassian.design/DESIGN.md`, including a non-standard dark-mode variant since the spec doesn't yet support theming. They've fed feedback upstream via GitHub.

## Useful Examples

- **Figma Make + Teamwork Graph dashboards demo (Team '26, Anaheim).** Same prompt with and without DESIGN.md — produced clearly more on-brand UI when the file was attached.
- **The button code comparison.** What DESIGN.md teaches the agent (re-implement button styling from tokens) vs what the codebase actually wants (`import Button from '@atlaskit/button'; <Button appearance="primary" spacing="compact" />`).
- **The on-demand tool call analogy.** `ads_plan` MCP call fetches guidance for a specific component, vs DESIGN.md's all-at-once loading. Important for heavy parts of a system like hundreds of icons or hundreds of semantic tokens.
- **Atlassian's distillation math:** 2.5 MB of fetchable guidance behind the MCP vs 80 KB ≈ 19,800 tokens for the single-file DESIGN.md (50+ components had usage guidance cut to make this fit).

## Constraints / Caveats

- **Single team, single product line, single test task.** The log-in screen comparison is one task in one playground — Atlassian explicitly says "this blog is not a research paper." Different models, prompts, design systems, and environments will yield different numbers. Treat the ~92% / 2.7× figures as directionally robust, not load-bearing for budgeting.
- **Confounded comparisons.** The "context available" estimates (5% / 80% / 80% / 30%) are Atlassian's own qualitative judgments. The MCP and skill variants both have ~80% available, but their token usage differs — suggests at least one other variable in play.
- **No model named.** The post doesn't say which agent/model ran the tests, which makes apples-to-apples comparison hard.
- **Vendor lens.** Atlassian built the ADS MCP and skills they're benchmarking against. They have an incentive to find MCP/skills better, and the result aligns with that incentive — which doesn't make the result wrong, but warrants pairing with internal evaluation before treating as universal.
- **No information on cache behavior.** A static DESIGN.md file should benefit massively from prompt caching, which would change the cost picture. The post doesn't address whether caching was enabled in the comparison.
- **DESIGN.md is a Google-originated open-source format** (for the Stitch design tool); other tool/framework support varies. Spec is still evolving (Atlassian's dark-mode variant is non-standard).

## Design Implications

- **For Bonny's design-system work / AOCC AI Hub tooling:** the framing "MCP/Skills = manual for *using* the existing system, DESIGN.md = guide for *re-implementing* it" is a useful split. Apply it as a routing question: am I generating *new* UI from scratch, or extending an existing codebase? The answer picks the primitive.
- **For one-shot prototyping (Figma Make, V0, Vercel-style):** DESIGN.md is the right primitive. The portability premium is real and there's no MCP to call.
- **For production codebases with a real component library:** prefer MCP + Skills + lint rules. Avoid DESIGN.md as the *sole* design source, because it actively encourages component re-implementation.
- **For customer-facing dynamic UI** (white-label dashboards, customer-uploaded brand kits): DESIGN.md is the right primitive precisely because it's portable, customer-supplied, and detached from any one codebase.
- **For evaluation:** the 80 KB / ~19,800-token ceiling is a useful working budget for design-system context that must load every turn. Anything heavier needs on-demand loading.
- **For internal docs hygiene:** the Atlassian observation that agents "read component implementations to recover missing guidance" is a useful canary signal — if your agent does this, your context primitive is missing something the agent thinks it needs.

## Tensions

- **DESIGN.md (always-on) vs Agent Skills (on-demand).** The blog reads as a direct empirical counterpart to the Day-3 progressive-disclosure argument: when context loads all at once, accuracy degrades in fewer turns. This is exactly the [[concepts/ai-agents/context-rot|Context Rot]] curve playing out on a real production workflow.
- **DESIGN.md (re-implementation) vs MCP/Skills (importation).** The same Markdown content could be either, depending on whether it tells the agent how to *build* a component or how to *use* one. The Atlassian framing argues this is the deciding factor in production.
- **Atlassian's MCP wins on tokens vs the Day-3 Vercel finding "AGENTS.md outperforms Skills".** Two different result spaces. Reconcile: the right primitive depends on whether your context is *project-wide global* (AGENTS.md), *narrow workflow-specific* (Skill / MCP), *external system reach* (MCP), or *portable brand snapshot* (DESIGN.md). Mis-applying the split is the predicted failure mode.
- **Portability vs sophistication.** DESIGN.md is explicit: you trade fidelity for portability. The 2.5 MB → 80 KB compression is the empirical version of that trade.

## Open Questions

- What is the token economics picture *with prompt caching enabled*? Does DESIGN.md become competitive again when its prefix is cached?
- How should Atlassian-style results generalize to a small design system (say, 10 components, no MCP server budget)? Is there a crossover where DESIGN.md beats Skills?
- Where should DESIGN.md sit in Bonny's own UI work (Bonny Slide System V2, internal mock decks)? Is the 80 KB ceiling a useful budget for a "slide system .md"?
- How does the picture change when the agent has filesystem access to the actual component library code? Does the agent still re-implement, or does it find and use the existing component?
- Is there a hybrid: small DESIGN.md catalog up front pointing into MCP-fetched component detail on demand? The blog hints at this with "MCP and skills are an instruction manual to using the existing design system, rather than a guide on how to re-implement it."
- What does *customer-uploaded DESIGN.md* unlock for white-label UI generation? Is this the right primitive for an enterprise feature where customers want their brand respected in AI-generated reports?

## Concepts Linked

- [[concepts/infrastructure-dev/design-md|DESIGN.md]] (new — the format itself)
- [[concepts/ai-agents/agent-skills|Agent Skills]]
- [[concepts/ai-agents/mcp-integration|MCP Integration]]
- [[concepts/ai-agents/progressive-disclosure|Progressive Disclosure]]
- [[concepts/ai-agents/context-rot|Context Rot]]
- [[concepts/infrastructure-dev/claudemd-context|CLAUDE.md / AGENTS.md Context]]
- [[concepts/infrastructure-dev/design-system-implementation|Design System Implementation]]
- [[concepts/infrastructure-dev/design-to-code-workflow|Design-to-Code Workflow]]
- [[concepts/infrastructure-dev/design-review-automation|Design Review Automation]]
- [[concepts/infrastructure-dev/color-token-architecture|Color Token Architecture]]
- [[concepts/ai-agents/vibe-design|Vibe Design]]
- [[concepts/ai-agents/vibe-coding|Vibe Coding]]
- [[comparisons/skills-vs-mcp-vs-agents-md|Skills vs MCP vs AGENTS.md]] (updated with DESIGN.md row)

## LLM Use

- **Use for:** justifying the routing decision between DESIGN.md and MCP/Skills for design-system context, budgeting tokens for an always-on design-context file (80 KB ≈ 19,800 tokens as a real ceiling), framing the re-implementation-vs-importation tradeoff, designing customer-theming features that want a portable brand snapshot, choosing the right primitive for one-shot vs production UI generation.
- **Do not use for:** quoted percentage comparisons as if they generalize across teams (single-task, single-team data); claims about peer-reviewed evidence (this is a vendor blog post); detailed DESIGN.md spec authority (defer to the open standard at atlassian.design/DESIGN.md and the Google Stitch reference).
- **Best prompt pattern:** "Using Hall & Campbell's Atlassian DESIGN.md findings, classify the following design-context need as one-shot prototyping, production codebase, customer theming, or cross-tool interoperability — then recommend a primitive (DESIGN.md, MCP, Skill, AGENTS.md, or a composition) and the token-budget shape that fits."

## Reliability Notes

> [!warning] Caveats
> - **Single-team, single-task evidence.** Treat the headline ~92% / 2.7× numbers as directional, not as a budget input.
> - **No model named, no caching addressed.** Two missing variables that would change the cost picture.
> - **Vendor lens.** Atlassian compares DESIGN.md against the MCP and skills they themselves built. Not wrong, but pair with independent evaluation.
> - **Confidence:** 0.85 on the framing (re-implementation vs importation, on-demand vs all-at-once); 0.7 on the specific token/turn numbers; 0.9 on Atlassian's own production stance ("we use MCP + Skills + lint rules internally").

## Backfill Status

- Newly written 2026-06-17 from a full web capture. All sections populated. No prior thin version to upgrade.
