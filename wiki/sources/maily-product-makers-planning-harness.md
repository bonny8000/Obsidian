---
type: source
status: active
created: 2026-06-25
updated: 2026-06-25
tags: [planning-harness, harness-engineering, product-management, ai-pm, skills, claudemd, guardrails]
source_path: raw/web/maily-product-makers-planning-harness-2026-06-25.md
source_url: https://maily.so/makersnote/posts/1gz2e564z3q
authors: [Product Makers Note]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.8
---

# Product Makers Note (2026, #19): Build a Planning Harness

**Author/Newsletter:** Product Makers Note (makersnote) — Maily, 2026-06-24. (Reached via a `share.google` short link.)
**Raw capture:** [[raw/web/maily-product-makers-planning-harness-2026-06-25|maily-product-makers-planning-harness-2026-06-25]]
**URL:** [maily.so/makersnote/posts/1gz2e564z3q](https://maily.so/makersnote/posts/1gz2e564z3q)

## Citation

Product Makers Note. (2026, June 24). *[19호] …Planning Harness* [newsletter]. Maily. Captured 2026-06-25 into `raw/web/maily-product-makers-planning-harness-2026-06-25.md`.

## Summary

PMs use AI well for **high-level strategy** but fall back to **manual detailed planning** — and edits blow up the AI's context, producing unreliable specs. The fix is a **"planning harness"**: a system that turns loose chat into a *tightly controlled automation factory* for product planning. Role shift: stop being an **"AI sitter"** babysitting hallucinations; become a **"planning harness engineer"** who designs the guardrails. This is [[concepts/ai-agents/harness-engineering|harness engineering]] applied to the PM's planning workflow.

## Key Claims

- **A harness has four principles:** **Context** (embed core service policies permanently, not re-pasted), **Tool definition** (restrict the AI to predefined **skills** only), **Guardrails** (human approval for sensitive decisions), **Validation** (AI self-checks output against original intent).
- **A harness ≠ sharing files:** it gives a *permanent pipeline* (no per-session setup), *real execution* (AI directly edits local files like `spec.md`, `flow.mermaid`), and a *team asset* (GitHub-shareable, consistent across teammates).
- **10-minute setup:** folder (`local-harness`) → rules file (`CLAUDE.md` / `.cursorrules` / `.clinerules`) → custom skills (`/sequence_diagram`, `/user-flow`, `/make-html`) → reference `spec.md` → optionally push to GitHub.
- **Future vision:** separate **design (Figma)** from **logic planning (harness-generated artifacts)** to eliminate duplicate effort.

## Useful Examples

- **Memo-app comment feature:** the harness auto-produced a client–server–DB **sequence diagram**, a **user-flow** chart, and an **HTML visualization** — work that otherwise needed manual cross-tool prompting.
- The concrete `CLAUDE.md` + `/skills` + `spec.md` folder as a copyable starter.
- Key quote: "Stop wasting time chatting aimlessly with AI. Design your own sturdy guardrails instead."

## Constraints / Caveats

- Practitioner newsletter, single author; a how-to, not a study — no efficacy metrics.
- The four principles closely mirror agent-engineering's general harness framing; novelty is the **PM-planning application**, not the underlying idea.
- "Validation = AI self-checks intent" is itself fallible (an LLM judging its own output) — still needs human gates.

## Design Implications

- Gives PMs a concrete entry to [[concepts/product-management/planning-harness|Planning Harness]] / [[concepts/product-management/ai-pm-skills|AI PM Skills]]: a repo-shareable `CLAUDE.md` + skills + reference spec that yields consistent planning artifacts.
- Same primitive family as [[concepts/ai-agents/agent-skills|Agent Skills]] and [[concepts/infrastructure-dev/claudemd-context|CLAUDE.md Context]] — the PM is authoring procedural memory + context, not prompting ad hoc.
- Strong tie to [[concepts/ai-agents/prd-generation|PRD Generation]] and [[sources/yozm-ai-prd|the AI-PRD / Eval Plan source]]: the harness's "validation against intent" is the spec/eval discipline applied at planning time.

## Tensions

- **Up-front harness investment vs. just-prompting** — the 10-minute setup pays off only with repeated, structured tasks.
- **Self-validation vs. real review** — automated intent-checking can give false confidence without human guardrails (the article keeps a human-approval step, which is the right call).

## Open Questions

- Where's the break-even: how many planning cycles before a harness beats ad-hoc prompting?
- How does a planning harness stay in sync when the underlying service policy changes (context drift)?

## Concepts Linked

- [[concepts/product-management/planning-harness|Planning Harness]]
- [[concepts/ai-agents/harness-engineering|Harness Engineering]]
- [[concepts/ai-agents/agent-skills|Agent Skills]]
- [[concepts/infrastructure-dev/claudemd-context|CLAUDE.md Context]]
- [[concepts/ai-agents/prd-generation|PRD Generation]]
- [[concepts/product-management/ai-pm-skills|AI PM Skills]]

## LLM Use

- **Use for:** setting up a PM planning harness (CLAUDE.md rules + skills + reference spec); arguing the "AI sitter → planning harness engineer" role shift; generating planning artifacts (sequence diagrams, user flows) reproducibly.
- **Do not use for:** efficacy/time-savings claims (none measured); as a substitute for human guardrails on sensitive decisions.
- **Best prompt pattern:** "Scaffold a planning harness: write a CLAUDE.md with service-policy context + guardrails, define `/sequence_diagram` `/user-flow` `/make-html` skills, and a `spec.md`; then run `/sequence_diagram` for feature X."

## Reliability Notes

> [!warning] Caveats
> Practitioner how-to, no metrics. Confidence 0.8 on the pattern (consistent with this vault's harness/skills cluster), unproven on time savings.

## Backfill Status

- New ingest 2026-06-25 from full web_fetch. To reach `full`, capture the Korean original's exact section titles and example screenshots.
