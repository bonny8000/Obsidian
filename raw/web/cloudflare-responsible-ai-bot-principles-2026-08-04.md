---
source_url: https://blog.cloudflare.com/building-a-better-internet-with-responsible-ai-bot-principles/
captured: 2026-08-04
title: "To build a better Internet in the age of AI, we need responsible AI bot principles. Here's our proposal."
authors: [Sebastian Hufnagel]
published: 2025-09-24
updated: 2026-07-15
publisher: Cloudflare Blog
language: en
format: vendor policy proposal
---

# Responsible AI Bot Principles — Cloudflare

**Author:** Sebastian Hufnagel, Cloudflare.
**Published:** 2025-09-24 · **Page last modified:** 2026-07-15 · **Captured:** 2026-08-04

AI-written extraction. No full-text reproduction; short quoted phrases only.

---

## Thesis

The web needs consensus "rules of the road" for AI crawler behaviour. The stated causal chain: AI answers reduce referral traffic → publishers lose the revenue that funds content → content quality declines → AI companies lose the high-quality training data they depend on. Cloudflare's position is that this harms every party including the AI labs, so voluntary alignment is in their interest.

Cloudflare's standing in the argument: it states it handles **on average 84 million requests per second**, which is the basis for its claim to see crawler behaviour at scale and for its ability to enforce (bot blocking, pay-per-crawl).

## The five principles (as worded)

1. **Public disclosure** — *"Companies should publicly disclose information about their AI bots."*
   Required disclosures: **identity** (user agent, IP ranges, cryptographic ID), **operator** (legal entity plus a contact point), **purpose** (one of search / AI-input / training).

2. **Self-identification** — *"AI bots should truthfully self-identify."*
   Today via user agent plus IP verification; the stated destination is cryptographic verification via **Web Bot Auth**.

3. **Declared single purpose** — *"AI bots should have one distinct purpose and declare it."*
   The three approved purposes:
   - **Search** — indexing to return results and links.
   - **AI-input** — RAG, grounding, real-time generative answers.
   - **Training** — model training and fine-tuning.
   Bots should not combine purposes *"in a way that prevents web operators from deliberately and effectively deciding"* which uses they permit.

4. **Respect preferences** — *"AI bots should respect and comply with preferences expressed by website operators where proportionate and technically feasible."*
   Mechanisms named: `robots.txt` (RFC 9309), emerging HTTP headers, the IETF AI preferences vocabulary. Crawlers should make a *"good faith attempt"* to fetch `robots.txt` before crawling.

5. **Act with good intent** — *"AI bots must not flood sites with excessive traffic or engage in deceptive behavior."*
   Explicitly prohibited: stealth crawling, rotating user agents to disguise identity, switching ASNs to hide activity, ignoring `robots.txt`. Also required: monitoring one's own network for compromise and patching vulnerabilities.

## The single-purpose argument

The load-bearing rhetorical move. Cloudflare argues that bundling search crawling with AI-answer crawling forces *"an impossible choice onto website owners"* — allow both or be delisted from search. The rebuttal to the efficiency defence is the two-pizzas analogy: *"cost of the two pizzas … remains the same"* whether ordered together or separately, so combining purposes saves the operator nothing that justifies removing the publisher's choice.

## Named actors and their compliance status

| Actor | Status as described |
| --- | --- |
| **OpenAI** | Held up as the positive example. Separate declared bots — GPTBot (training), OAI-SearchBot (search). *"GPTBot is an example of this principle in action."* The ChatGPT agent signs requests using Web Bot Auth / RFC 9421. |
| **Vercel** | Announced bot verification supporting Web Bot Auth roughly a month before the post. |
| **Perplexity** | Criticised for *"stealth undeclared crawlers to evade website no-crawl directives."* |
| **Anthropic** | Publishes a user agent only; the post treats the absence of verifiable information as a trust gap. |
| **xAI** | *"xAI's bot, grok, does not self-identify at all."* |
| **Google** | Not accused of stealth, but named as the case that combines search indexing with AI Overviews — the precise pattern principle 3 targets. |

No formal signatory list exists. The principles are framed as *"starting points"* for discussion.

## Technical mechanisms named

| Mechanism | What it does | Status |
| --- | --- | --- |
| **Web Bot Auth** | Cryptographic bot identity via HTTP message signatures | IETF draft, in development |
| **HTTP Message Signatures (RFC 9421)** | The signing primitive underneath | Published RFC |
| **HTTP Message Signatures Directory** | Key discovery for the above | IETF draft |
| **`robots.txt` (RFC 9309)** | Per-user-agent crawl preferences | Published standard |
| **IETF AI Preference Vocabulary** | Finer-grained, purpose-aware preference terms | IETF working group draft (`ietf-wg-aipref`) |
| **HTTP preference headers** | Server-level machine-readable signals | Under discussion |
| **Pay-per-crawl** | Charging AI crawlers for access | Cloudflare product, available |
| **One-click AI crawler blocking** | Blocking by default | Cloudflare product, available |
| **Verified bots policy** | Cloudflare's own enforcement framework | Published |

## Evidence cited

- **84 million requests/second** — Cloudflare's own traffic, the basis of its vantage claim.
- **Pew Research** — cited for the finding that Google users click links less often when an AI summary is present.
- **Forbes, "The 60 Problem"** — cited for the scale of referral-traffic decline.
- Traffic decline is otherwise characterised qualitatively (*"dramatic decrease in those eyeballs"*), and *"zero-click searches"* is the named mechanism.
- **No adoption metrics.** The post gives no figure for what share of crawlers comply with any principle.

## Gaps and limits

| Gap | Detail |
| --- | --- |
| Discretionary wording | Principle 4 applies *"where proportionate and technically feasible"* — neither term is defined, and it is the escape hatch for the whole framework. |
| No enforcement mechanism | No penalties proposed. Compliance rests on industry consensus plus Cloudflare's own commercial blocking. |
| Standards unfinished | Web Bot Auth and the AI preference vocabulary are both drafts. The cryptographic destination is not yet reachable. |
| Purpose boundary is fuzzy | The line between AI-input and training is contestable and the post does not resolve it. |
| Combined-purpose loophole | Google's search+AI-Overviews bundling is criticised but no blocking mechanism for it is offered. |
| Spoofing until crypto lands | `robots.txt` operates per user agent, which is trivially forgeable; the framework's integrity depends on a standard that does not yet exist. |
| Self-interest | Cloudflare sells the enforcement layer (blocking, pay-per-crawl) that these principles create demand for. The post does not treat this as a conflict. |
| Assumed good faith | *"Most players … want to do the right thing"* is stated rather than evidenced. |

## Author's own framing

The principles are presented as a rough draft requiring broader stakeholder input, with the IETF named as the neutral forum for holistic consideration.
