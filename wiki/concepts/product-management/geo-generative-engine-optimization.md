---
type: concept
status: active
created: 2026-05-19
updated: 2026-08-04
tags: [ai, marketing, search, agents, seo, eeat]
sources: [wiki/sources/pxd-story-ai-insights.md, sources/google-good-seo-is-good-geo, cloudflare-responsible-ai-bot-principles, google-search-io-2026-agents, hai-headlines-ai-news-audit]
confidence: 0.90
---

# GEO (Generative Engine Optimization)

## Summary
Generative Engine Optimization (GEO) is the process of optimizing digital content and brand presence so that it is correctly understood, indexed, and recommended by AI-powered generative engines and autonomous agents.

## Why it Matters
As users increasingly bypass traditional search engines (like Google) in favor of asking AI agents for recommendations, companies must ensure their data is structured in a way that AI models can "find" and endorse them. It is the AI-era successor to SEO.

## Key Claims
- Companies must optimize their digital presence for AI "knowledge" rather than just keyword ranking [wiki/sources/pxd-story-ai-insights.md].
- GEO is critical for maintaining brand visibility in an agent-driven search landscape [wiki/sources/pxd-story-ai-insights.md].
- **Google's counter-position: "good SEO is good GEO."** On Google surfaces, AI Mode / AI Overviews are built **directly on top of core ranking systems** and retrieve from the **same index**, so foundational SEO *is* GEO — chase fundamentals + E-E-A-T + business outcomes, not LLM-specific hacks (skip `LLMs.txt`, keyword-stuffing, artificial snippets) [[sources/google-good-seo-is-good-geo|Kraham/Google, 2026]].
- Caveat to that: Google's claim is authoritative for Google surfaces but **unproven for non-Google engines** (ChatGPT, Perplexity, Copilot), where retrieval/ranking differ.

## Related Concepts
- [[concepts/ai-agents/agentic-ai|Agentic AI]]
- [[concepts/ai-agents/agentic-search|Agentic Search]]
- [[concepts/infrastructure-dev/ai-as-infrastructure|AI as Infrastructure]]

## Conflicts & Caveats

> [!warning] "New discipline" vs. "just do SEO"
> The SEO industry (and [[sources/pxd-story-ai-insights|pxd]]) frames GEO as a new discipline; Google ([[sources/google-good-seo-is-good-geo|Kraham, 2026]]) says it's the same foundational work on top of core ranking. Likely both true on different surfaces — Google reuses core ranking; standalone LLMs may still reward distinct structuring.

## Sources
- [[wiki/sources/pxd-story-ai-insights.md|pxd story: AI & UX Insights]]
- [[sources/google-good-seo-is-good-geo|Kraham / Google (2026): Good SEO is good GEO]]
- [[wiki/sources/cloudflare-responsible-ai-bot-principles|Cloudflare (2025/2026): Responsible AI Bot Principles]] — the same phenomenon from the opposite posture.
- [[wiki/sources/google-search-io-2026-agents|Google (2026): Search at I/O 2026]] — generative UI free to all users; the surface GEO optimises for is changing.

## Two Caveats Added 2026-08-04

> [!warning] "Optimise to be cited" assumes a surface that cites
> Google publishes both sides of this and they do not obviously reconcile. [[wiki/sources/google-good-seo-is-good-geo|Kraham (Think with Google)]] tells publishers how to earn citation in AI answers. Two months earlier, [[wiki/sources/google-search-io-2026-agents|Reid (I/O 2026)]] announced **Generative UI free to every Search user** — bespoke assembled layouts with interactive visuals and simulations, replacing the page of links, with no stated citation guarantee.
>
> GEO's existing tactics assume a text answer with attributable links. **When the answer becomes a generated component, what counts as a citation is undefined** — and Google has not said.
>
> Independent evidence makes this worse rather than better: [[wiki/sources/hai-headlines-ai-news-audit|Suzgun & Zou's audit]] of six commercial chatbots on same-day news found retrieval and citation-attribution failures. That is the only *measured* source in this cluster, and the publisher-side bargain rests entirely on citation working.

> [!warning] GEO is one posture toward AI crawling; there is another
> This concept frames AI answer surfaces as an optimisation target. [[wiki/concepts/infrastructure-dev/ai-crawler-governance|AI Crawler Governance]] frames the traffic they replace as the problem being governed, and supplies a taxonomy GEO lacks: **search** (index access for referral traffic — a trade), **AI-input** (live content for generated answers — the visit is substituted), **training** (content as data — nothing returned). GEO reasons almost entirely about the first two as though they were one thing.
>
> Same phenomenon, opposite question: GEO asks how to be cited; crawler governance asks whether the crawl is a fair trade at all. See [[wiki/analyses/2026-08-04-crawl-consent-vs-answer-surfaces|the 2026-08-04 memo]].

## Related (added 2026-08-04)
- [[wiki/concepts/infrastructure-dev/ai-crawler-governance|AI Crawler Governance]]
- [[wiki/concepts/ux-research/generative-ui|Generative UI]]
- [[wiki/concepts/ai-agents/ai-news-intermediary|AI News Intermediary]]

