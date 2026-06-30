---
type: query
status: active
created: 2026-05-27
updated: 2026-06-26
tags: [query]
sources: [sources/figma-you-never-stop-cultivating-taste, sources/nngroup-design-process-compressed, sources/atlassian-ai-prototyping-handshakes, sources/figma-mcp-server-four-ways, sources/dusskapark-product-designer-codex, sources/lennys-newsletter-new-inner-game]
confidence: 0.78
---

# Query: design tasks remain manual

## Short Answer

Across the wiki, the consistent pattern is that AI automates the *generative middle* of design — layout exploration, high-fidelity mockups, design-system-grounded prototypes, asset generation, and first-pass implementation — while a stable set of tasks stay human-owned. What remains manual clusters into four areas: (1) **problem framing and discovery** — deciding what to build and which user problem matters, which AI compresses but never removes; (2) **taste, critique, and final judgment** — the cultivated point of view, trade-off decisions, and the discernment to reject a first output; (3) **the review / last-mile pass** — both Atlassian (~70% one-pass design-system accuracy) and Figma ("first 80% done") report a *required human review* on every workflow to swap placeholders, fix unmapped tokens, and check production quality; and (4) **interpretation, specification, and accountability** — reading context and stakeholder dynamics, owning the verification loop, and being answerable for regulated/high-stakes decisions. The throughline is that AI raises *build reach* but does not supply *judgment about what matters* — "Codex expanded reach but didn't decide what mattered." Brand- or structurally-critical choices are also deliberately kept out of free-form generation (handled as constrained config, not prompts). The wiki is thinnest on a concrete, task-by-task review rubric, so the boundary is described in principle more than as an operational checklist.

## Evidence

- [[concepts/infrastructure-dev/design-automation|Design Automation]] — AI reduces repetitive design work (research synthesis, layout, HTML mockups, asset generation), but the strongest framing is *not replacement*: it moves the designer's work upward to framing problems, steering, and reviewing; designer review and taste should stay explicit control points.
- [[concepts/infrastructure-dev/ai-prototyping|AI Prototyping]] — automates "the first 80%," then a human reviews, swaps placeholders, and edits; production-quality code at scale "remains a work in progress," so discovery and final code quality stay human-owned.
- [[concepts/product-management/product-taste|Product Taste]] — deciding *what should be built* and what feels right is a rising bottleneck as code gets cheaper; taste (discernment, empathy, trade-off judgment, final call) is not replaced by AI, and accepting the first output as final is a "weak-taste failure mode."
- [[concepts/ai-agents/vibe-design|Vibe Design]] — the designer becomes director/reviewer of generated variations; the unit of work is *intent plus review*, and quality still depends on design judgment, critique, and system coherence — all human.
- [[concepts/ux-research/process-literacy|Process Literacy]] — problem framing stays human: speed of execution doesn't remove the need to frame the problem, and intuition can't replace process for juniors, in regulated/high-stakes domains, or where accountability and bias matter.
- [[concepts/ux-research/human-interpretation|Human Interpretation]] — situated sense-making (context, power, what went unspoken, scoping/reframing) is method-required human work; the safe pattern is AI-as-thinking-partner, not AI-as-analyst.
- [[concepts/infrastructure-dev/design-review-automation|Design Review Automation]] — even the review step is "augment, not replace": automated checks catch spacing/type/color mismatches, but designer judgment owns whether a difference is a defect or acceptable variance.
- [[concepts/infrastructure-dev/deterministic-ui|Deterministic UI]] — where layout is a pure function of data, manual per-page design *is* removed; but the human work shifts up to the ObjectView/token logic that defines the rules — design moves, it doesn't disappear.
- [[concepts/product-management/domain-expert-as-builder|Domain Expert as Builder]] — when implementation collapses in cost, the scarce skill is judgment, scoping, specification, and verification — not syntax; human-in-the-loop boundaries set up front keep the build responsible.
- [[concepts/product-management/role-convergence|Role Convergence]] — as PM/eng/design roles blur, the shared, retained skill is "judgment about what matters and whether the output is good enough."
- [[concepts/product-management/wisdom-stack|Wisdom Stack]] — when knowledge and effort are commoditized, the durable human edge is emotional clarity, conflict navigation, genuine creativity (which needs human iteration), and intrinsic motivation — none of which AI supplies.
- [[sources/figma-you-never-stop-cultivating-taste|Figma: You Never Stop Cultivating Taste]] — AI expands exploration and execution range, but "the vision and final judgment still come from the designer"; taste lives in trade-offs (form vs. function, what to add vs. remove) and is built through critique and intentional choices.
- [[sources/atlassian-ai-prototyping-handshakes|Atlassian: Turning Handoffs into Handshakes]] — ~70% one-pass design-system accuracy from a screenshot; brand-critical elements (logos, nav) are kept as constrained JSON config the agent edits, *not* free-text it rewrites — humans own the structurally sensitive choices, and "production-quality code at scale remains challenging."
- [[sources/figma-mcp-server-four-ways|Figma: 4 Ways We're Using Our MCP Server]] — every one of the four agent workflows shares a "first 80% done, human review pass still needed" cadence; agent output is "a strong first pass, not a finished one" (auto layout, fonts, unmapped colors still need human work).
- [[sources/dusskapark-product-designer-codex|Park: How Far Can a Product Designer Build with Codex?]] — even when one designer owns the full SDLC, "product judgment stays the bottleneck": defining the API contract, scope, and verification criteria, and owning the verification loop (input → screen → DB) are the human-owned acts.

## Reusable Notes

- The recurring boundary across independent sources is the **80/20 (or 70/30) split**: AI reliably produces the generative middle and a strong first pass, but the *opening* (problem framing, discovery, scoping) and the *closing* (review, taste call, verification, accountability) remain human — see [[concepts/infrastructure-dev/ai-prototyping|AI Prototyping]] + [[concepts/ux-research/process-literacy|Process Literacy]] + [[concepts/product-management/product-taste|Product Taste]].
- "Manual" is less about *pixels* and more about *judgment*: deterministic and generative tooling removes hand-execution but elevates rule design, trade-off decisions, and discernment — the work moves up a level rather than vanishing ([[concepts/infrastructure-dev/deterministic-ui|Deterministic UI]], [[concepts/product-management/role-convergence|Role Convergence]]).
- A practical control pattern emerges: keep **brand-critical and structurally-sensitive choices out of open-ended generation** (constrain via config), and gate intuition-led / solution-first work behind risk (juniors, regulated domains, accountability) — [[sources/atlassian-ai-prototyping-handshakes|Atlassian handshakes]] + [[concepts/ux-research/process-literacy|Process Literacy]].

## Follow-up Sources Needed

- A concrete, **task-by-task review rubric** that makes "taste" and the human review pass operational (the [[sources/figma-you-never-stop-cultivating-taste|Figma]] and [[concepts/product-management/product-taste|Product Taste]] pages flag this as an open question) — the wiki frames the boundary in principle but lacks a checklist.
- Independent, **metric-backed** evidence on where AI design output fails: current sources (Atlassian ~70%, Figma "first 80%") are vendor self-reports with no disclosed model/test set, so the manual-vs-automated line is directional, not measured.
- A page on **which build tasks should stay specialist-owned** (security, data modeling, store/compliance) — flagged as an open question in both [[concepts/product-management/domain-expert-as-builder|Domain Expert as Builder]] and the [[sources/dusskapark-product-designer-codex|Codex case study]], but not yet synthesized.
