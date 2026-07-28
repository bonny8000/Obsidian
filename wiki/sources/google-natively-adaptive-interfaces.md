---
type: source
status: draft
created: 2026-07-28
updated: 2026-07-28
tags: [accessibility, adaptive-interfaces, multimodal-agents, gemini, gemma, google, documentation-hub, needs-deeper-capture]
source_path: raw/web/google-natively-adaptive-interfaces-2026-07-28.md
source_url: https://developers.google.com/natively-adaptive-interfaces
authors: []
sources: []
ingest_level: light
coverage: partial
llm_ready: false
raw_preserved: true
confidence: 0.45
---

# Google (n.d.): Natively Adaptive Interfaces (NAI)

## Citation

*Natively Adaptive Interfaces*, **Google for Developers** documentation. No publication date stated on the page; no named authors.

**Source type:** First-party vendor documentation — **hub / landing page**, not an article.
**Raw capture:** [[raw/web/google-natively-adaptive-interfaces-2026-07-28|google-natively-adaptive-interfaces-2026-07-28]]

> [!warning] Partial ingest — not LLM-ready
> `llm_ready: false` and `coverage: partial` are deliberate. The captured page is mostly navigation into sub-guides that were **not fetched**. What follows is the framing NAI states about itself, and nothing more. Do not build a design recommendation on this page.

## Summary

Google for Developers documentation introducing **Natively Adaptive Interfaces (NAI)**: a framework for building accessibility **into the core of multimodal AI agents** rather than adding it afterwards, using Gemini and Gemma models. The stated premise is that adaptive and interactive accessibility can be natively built in, so an interface adapts across differing user abilities and contexts by construction rather than by remediation.

The idea matters and the framing is consistent with two other sources in this ingest. The captured evidence, however, is a table of contents.

## Key Claims

Everything here is the source's self-description, not verified guidance:

- **Accessibility is foundational, not supplementary** — explicitly not a compliance afterthought.
- **Multimodal integration** — adaptivity built inside AI agents using Gemini and Gemma.
- **Native adaptation** — adaptive and interactive accessibility built into the agent itself rather than layered over a fixed interface.
- **Low entry barrier is claimed** — the MVP path is stated to require no prior accessibility experience.

## Useful Examples

None captured. The hub links to five sections, none of which were fetched:

1. Overview guide — the design approach.
2. MVP development — step-by-step, stated to need no prior accessibility experience.
3. Multimodal agent understanding — using Google's models for adaptive design.
4. Developer resources — code samples for key NAI configuration patterns.
5. Terminology reference — glossary including "multimodal AI agent."

## Constraints / Caveats

- **No date.** Recency cannot be established, which matters for anything Gemini/Gemma-versioned.
- **No named authors.**
- **No substantive guidance captured** — no principles enumerated, no form factors, no code, no requirements.
- **Vendor documentation.** NAI is Google's coinage, tied to Google models. Treat as a vendor framework, not an industry standard, and note that Gemini/Gemma dependence is architectural, not incidental.
- **"No prior accessibility experience required" is a marketing claim** that deserves scrutiny: accessibility failures are usually failures of judgment about users, and tooling does not obviously supply that.
- **The term is easy to confuse** with Android's "adaptive by default" layout work ([[wiki/sources/veronikapj-whats-new-android-2026|Android 2026]]), which is about window size classes and reflow — a different problem. NAI is about ability and context adaptation in agents. Keep them distinct.

## Design Implications

Provisional, pending a real capture:

- **The framing is worth adopting independently of the tooling:** accessibility as an agent capability rather than a UI property. If an agent mediates the interface, adaptation can happen per-interaction instead of per-breakpoint.
- **Multimodality is the mechanism** — an agent that can shift between voice, text, and visual channels can adapt to ability and context in ways a fixed layout cannot.
- **Watch for the remediation trap in reverse:** "the agent adapts" can become a reason not to make the underlying interface accessible, which would leave non-agent users worse off.

## Tensions

- **Converges with two independent sources in this ingest on accessibility gaining new load.** [[wiki/sources/b2b-admin-web-accessibility|rami_]] argues accessibility pays back through human repetition; [[wiki/sources/veronikapj-whats-new-android-2026|Android 2026]] shows accessibility semantics becoming the substrate for agent-driven Computer Control; NAI proposes accessibility as an agent-native capability. Three different reasons, same direction.
- **Potential tension with the semantics-as-substrate model.** If agents adapt interfaces natively, does that reduce or increase the need for accurate accessibility metadata underneath? Android's Computer Control depends on that metadata; NAI's framing could be read as generating adaptation instead of consuming semantics. Unresolved and worth resolving.
- **Vendor-framework caution:** as with "AI-native design system" (Atlassian's coinage), a useful frame arriving with a vendor's models attached. Adopt the concept; do not assume the stack.

## Open Questions

- What does NAI actually prescribe? Every substantive question is unanswered by this capture.
- Does it address accessibility for users of the *agent*, the *interface the agent operates*, or both?
- What is the relationship to WCAG — complement, superset, or orthogonal?
- Is any of it usable without Gemini or Gemma?
- When was it published, and is it current?

## Concepts Linked from This Source

- [[wiki/concepts/agent-experience/natively-adaptive-interfaces|Natively Adaptive Interfaces]]
- [[wiki/concepts/ux-research/web-accessibility-pour|Web Accessibility (POUR)]]
- [[wiki/concepts/agent-experience/agent-invocable-app-functions|Agent-Invocable App Functions]]
- [[wiki/concepts/ux-research/ai-native-ux-design|AI-Native UX Design]]

## LLM Use

**Do not use for grounded reasoning.** `llm_ready: false`. This page exists to record that the framework exists, what it claims about itself, and that it has not been properly ingested.

Acceptable use: noting that Google has published an accessibility-native agent-interface framework, and as a pointer for the next capture. Anything more requires fetching the sub-guides first.

## Reliability Notes

- **Confidence 0.45** — first-party vendor documentation (which is inherently reliable about its own contents) reduced to near-uselessness by a shallow capture. The low score reflects **capture quality, not source quality**; a proper ingest would likely land near 0.80.
- No date, no authors, no captured substance.

## Backfill Status

**Needs a second pass.** Next capture action, in order:

1. Fetch the **Overview** sub-page — the design approach and any enumerated principles.
2. Fetch the **MVP development** guide — the concrete procedure.
3. Fetch the **Terminology** reference — for the "multimodal AI agent" definition, useful to this wiki independently.
4. Establish a publication or last-updated date.

On completion, upgrade `ingest_level` to `standard` or `deep`, set `coverage` honestly, flip `llm_ready: true` if the sub-guides carry real guidance, revise confidence, and record the backfill in [[wiki/logs/change-log|the change log]].
