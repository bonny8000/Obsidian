---
type: source
status: active
created: 2026-06-29
updated: 2026-06-29
tags: [design-tokens, hypertokens, design-systems, design-to-code, composite-tokens, dtcg, agent-readable, figma, token-efficiency]
source_path: raw/web/christinevallaure-hypertokens-2026-06-29.md
source_url: https://christinevallaure.substack.com/p/what-are-hypertokens-the-layer-between
authors: [Christine Vallaure]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.78
---

# Christine Vallaure (2026): Hypertokens — the bundled-decision layer between tokens and components, rebuilt for agents

**Christine Vallaure (moonlearning.io), Substack, 2026-06-28.**
**Raw capture:** [[raw/web/christinevallaure-hypertokens-2026-06-29|christinevallaure-hypertokens-2026-06-29]]
**URL:** [christinevallaure.substack.com/p/what-are-hypertokens…](https://christinevallaure.substack.com/p/what-are-hypertokens-the-layer-between)

> [!note] Full fetch; quotes pending verbatim re-check
> The article body was retrieved cleanly (the Substack NOTE 302-redirected to the article and the redirect was followed). Coverage is substantial. The concept is an **exploration, not a shipped feature**, and the standout quotes were returned by the fetch summarizer — re-verify them verbatim before quoting precisely.

## Citation

Vallaure, C. (2026, June 28). *What are hypertokens? The layer between tokens and components, rebuilt for agents.* Substack (moonlearning.io). Captured 2026-06-29 into `raw/web/christinevallaure-hypertokens-2026-06-29.md`.

## Summary

Vallaure explains **"hypertokens"** — a term **Jake Albaugh (Figma) coined during his Config 2026 talk** ("Jake Albaugh from Figma gave that gap a name: hypertokens") — a layer that sits **between design tokens and components** and holds *bundled* style decisions rather than single ones. The premise is that design decisions naturally travel in groups — typography is font-family + size + weight + line-height + letter-spacing *together*; a surface is background + border + radius + shadow *together* — yet today each bundle exists only as separate, hand-copied versions across CSS classes, Figma styles, and iOS/Android code, which drift out of sync. A hypertoken is "a named bundle of style properties, defined once, that every tool's copy is built from": a single upstream source of truth that **compiles automatically** into platform-specific outputs (CSS, Figma styles, Swift structs). She frames this explicitly as infrastructure for the **AI-agent era** — agents "build exactly what [they] find and guess the rest," so handing them named, grouped, semantic bundles (e.g. `Surface.brand`) instead of scattered raw properties yields less reconstruction, less code, and lower AI usage. Hypertokens **generalize** the W3C/DTCG composite-token idea from its fixed predefined types to "any recurring fragment your own system has." The concept is illustrated by Jake Albaugh's Figma exploration (a JSON pipeline compiling one source into many outputs, shown at Config 2026) and is explicitly **not yet shipped**.

## Key Claims

- **Definition & coinage.** The term was **coined by Jake Albaugh (Figma)** at his Config 2026 talk ("gave that gap a name: hypertokens"); this article is Vallaure's write-up. A hypertoken is "a named bundle of style properties, defined once, that every tool's copy is built from" — a single source of truth **upstream of design tools** that compiles into platform-specific outputs ("the CSS class, the Figma text style, and the Swift struct for iOS") automatically.
- **Position in the hierarchy.** **Raw values → Tokens (single decisions) → Hypertokens (bundled decisions) → Components (structure, behavior, accessibility).** Hypertokens handle **style bundles only**; behavioral logic, structure, and accessibility remain in the component layer.
- **Problem.** Style bundles are real (typography, surfaces, spacing, transforms, motion), but they currently live as **separate hand-copied versions per tool** (CSS, Figma, iOS, Android) that **drift out of sync over time**. Defining the bundle once and generating each copy removes the drift.
- **Why agents change the stakes.** *"An agent doesn't smooth anything over. It builds exactly what it finds and guesses the rest."* Scattered, ungrouped property lists force agents to **reconstruct** intent ("you asked for a cheese sandwich and got handed an encyclopedia on bread" — Jake Albaugh). **Semantic names like `Surface.brand` require less processing** than reverse-engineering raw values.
- **Generalizes composite tokens.** The W3C **DTCG composite token** types (typography, shadow, border, gradient, transition, strokeStyle) are *fixed and predefined*; hypertokens extend the idea to **"any recurring fragment your own system has"** — i.e. open-ended, user-defined composites.
- **Tooling proof-of-concept.** Albaugh's **JSON-based pipeline** compiled one source simultaneously into aliased variables (with code syntax), component libraries, icon libraries, **Code Connect** docs, base CSS, and **Svelte** presentation-layer components (date picker, table, charts). Reported outcome: *"less total code and lower AI usage for a better outcome."*
- **Status.** **Not shipped.** An exploration by Albaugh's team at Figma, referenced from his **Config 2026** talk; no "hypertoken button" in Figma as of June 2026.
- **Thesis line.** *"Precision up front is cheaper than cleanup later."*

## Useful Examples

- **Typography hypertoken:** font-family + font-size + font-weight + line-height + letter-spacing as one named unit.
- **`Surface.brand`:** the article's concrete worked example — *"Instead of fifteen lines of raw values, the AI gets two words, 'Surface.brand,' and knows exactly what you mean."*
- **`Surface.card`:** fill + border + radius + shadow applied as a single unit (named in the hierarchy as a bundled-decision example).
- **Other named bundles:** surfaces (background/border/radius/shadow), spacing groups, transforms, motion clusters.
- **Albaugh's one-source-to-many-outputs pipeline** (variables → component/icon libraries → Code Connect → base CSS → Svelte components) as the tooling demonstration.

## Constraints / Caveats

- **Forward-looking exploration, not a shipped capability** — there is no hypertoken primitive in Figma or any tool as of June 2026; treat it as a *proposed abstraction / vocabulary*, not validated practice.
- **Single-author advocacy piece** on a personal Substack; no empirical study, no adoption data. The "less code / lower AI usage" outcome is a **reported anecdote** from one demo, not a measured benchmark.
- **Quotes returned via the fetch summarizer** — re-verify verbatim before precise quotation.
- It does **not** prove that grouping tokens improves agent output quality at scale, nor that the abstraction survives real multi-platform systems; those are claims to test.
- Secondary write-up of **Jake Albaugh's** work (Config 2026); the primary source is his talk, not this article.

## Design Implications

- Treat **named, grouped, semantic style bundles** as a deliberate layer in the system, distinct from single-value tokens — useful framing whether or not a "hypertoken" primitive ever ships. Extends [[concepts/infrastructure-dev/color-token-architecture|Color Token Architecture]] (primitive/semantic/component) with a "bundled-decision" tier above semantic tokens.
- For **agent-built UI**, optimize the *input* the agent reads: prefer one upstream source compiling to many targets over hand-copied per-tool styles, so the agent doesn't "guess the rest." Strengthens [[concepts/infrastructure-dev/design-to-code-workflow|Design-to-Code Workflow]] and [[concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]].
- **Semantic naming as token efficiency:** `Surface.brand` over raw hex/px reduces agent reconstruction work — a concrete instance of [[concepts/infrastructure-dev/token-efficiency|Token Efficiency]] applied to design systems, and of [[concepts/infrastructure-dev/deterministic-ui|Deterministic UI]] (one source of truth → reproducible output).
- Connects to spec/declaration-first practices like [[concepts/infrastructure-dev/design-md|design.md]] and [[concepts/infrastructure-dev/scaffold-design-system|Scaffold Design System]]: the more design intent is declared once and grouped, the less drift and the less an agent must infer.
- Relevant to [[concepts/infrastructure-dev/design-system-implementation|Design System Implementation]] and the [[concepts/ai-agents/vibe-design|Vibe Design]] / [[concepts/infrastructure-dev/ai-prototyping|AI Prototyping]] workflows, and to [[concepts/figma-make|Figma Make]]–style code generation where grouped tokens feed the generator.

## Tensions

- **Abstraction vs. shipped reality:** a clean conceptual layer that no tool yet implements — adoption could stall on tooling, or the W3C DTCG composite spec could absorb it.
- **Open-ended user-defined composites vs. interoperability:** "any recurring fragment your own system has" maximizes expressiveness but works against the *fixed predefined types* that make composites portable across tools.
- **Human reconciliation vs. agent literalism:** humans smooth over minor inconsistency; agents don't. The same scattered system that humans tolerate becomes a liability the moment agents build from it — the case for hypertokens is strongest precisely where agents replace human judgment.
- **"Less code / lower AI usage" vs. unproven:** the efficiency claim is the most persuasive selling point and the least substantiated.

## Open Questions

- Does grouping tokens measurably improve agent output quality / reduce tokens at scale, or only in Albaugh's demo?
- Will the W3C **DTCG** spec extend composite tokens toward open-ended user-defined bundles, making "hypertoken" a vocabulary rather than a new mechanism?
- How do hypertokens interact with **theming/modes** (light/dark, brand variants) — does a bundle carry its own conditional logic, or stay flat?
- Where exactly is the boundary between a hypertoken (style bundle, no logic) and a component (structure + behavior + a11y) in practice?
- Does any tool (Figma, Tokens Studio, Style Dictionary) plan to implement this, and in what format (JSON pipeline as shown)?

## Concepts Linked

- [[concepts/infrastructure-dev/hypertokens|Hypertokens]] *(new — propose)*
- [[concepts/infrastructure-dev/color-token-architecture|Color Token Architecture]]
- [[concepts/infrastructure-dev/design-to-code-workflow|Design-to-Code Workflow]]
- [[concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]]
- [[concepts/infrastructure-dev/token-efficiency|Token Efficiency]]
- [[concepts/infrastructure-dev/deterministic-ui|Deterministic UI]]
- [[concepts/infrastructure-dev/design-md|design.md]]
- [[concepts/infrastructure-dev/scaffold-design-system|Scaffold Design System]]
- [[concepts/infrastructure-dev/design-system-implementation|Design System Implementation]]
- [[concepts/infrastructure-dev/figma-make|Figma Make]]
- [[concepts/infrastructure-dev/ai-prototyping|AI Prototyping]]
- [[concepts/ai-agents/vibe-design|Vibe Design]]
- [[concepts/ux-research/ai-native-ux-design|AI-Native UX Design]]
- [[concepts/ux-research/designing-for-agency|Designing for Agency]]
- Related sources: [[sources/pxd-color-token-design-2026|pxd: Color Token Design]], [[sources/atlassian-design-md|Atlassian design.md]], [[sources/atlassian-design-system-context-engine|Atlassian Design System Context Engine]]

## LLM Use

- **Use for:** explaining the *bundled-decision* layer above semantic tokens; the agent-readability argument for one-source-compiles-to-many; framing semantic naming (`Surface.brand`) as token efficiency; the relationship between hypertokens and W3C/DTCG composite tokens.
- **Do not use for:** claiming hypertokens are a real/shipped feature (they are an exploration as of June 2026); citing the "less code / lower AI usage" result as a measured benchmark; quoting strings as verbatim without re-checking the live article.
- **Best prompt pattern:** "Using Vallaure's hypertoken framing (Raw → Tokens → Hypertokens → Components), redesign these scattered per-tool style bundles into one named, agent-readable source of truth that compiles to CSS + Figma + Swift; flag where this generalizes a DTCG composite token vs. introduces a user-defined one."

## Reliability Notes

> [!warning] Caveats
> Single-author advocacy/explainer on a personal Substack describing a **forward-looking concept that no tool has shipped** (as of June 2026). The efficiency outcome is a one-demo anecdote, not data. Quotes were returned via the fetch summarizer and need verbatim re-check. Confidence **0.78**: the *framing and definitions* are reliably captured; the *claims of benefit* are unproven and the *concept's adoption* is speculative. The primary source is Jake Albaugh's Config 2026 talk, not this article.

## Backfill Status

- Captured 2026-06-29: full article body (definition, hierarchy, problem, agent argument, examples, DTCG relation, tooling demo, status, key quotes) via web_fetch following the NOTE→article redirect; raw capture written; source page authored.
- To reach `coverage: full`: re-verify all quotes verbatim against the live article; capture Jake Albaugh's **Config 2026** talk directly (primary source) and any published JSON/pipeline artifacts; confirm the current W3C **DTCG** composite-token type list; capture any diagrams/code snippets present in the original.
