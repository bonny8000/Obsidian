---
type: source
status: active
created: 2026-08-04
updated: 2026-08-04
tags: [ai-crawlers, web-bot-auth, robots-txt, ietf, agent-identity, publisher-economics, governance, cloudflare, geo]
source_path: raw/web/cloudflare-responsible-ai-bot-principles-2026-08-04.md
source_url: https://blog.cloudflare.com/building-a-better-internet-with-responsible-ai-bot-principles/
authors: [Sebastian Hufnagel]
sources: []
ingest_level: deep
coverage: full
llm_ready: true
raw_preserved: true
confidence: 0.64
---

# Cloudflare (2025/2026): Responsible AI Bot Principles

## Citation

Sebastian Hufnagel, "To build a better Internet in the age of AI, we need responsible AI bot principles. Here's our proposal," **Cloudflare Blog**, published 2025-09-24, page last modified 2026-07-15.

**Source type:** Vendor policy proposal. Cloudflare sells the enforcement layer these principles create demand for; read accordingly.
**Raw capture:** [[raw/web/cloudflare-responsible-ai-bot-principles-2026-08-04|cloudflare-responsible-ai-bot-principles-2026-08-04]]
**Coverage note:** `coverage: full` — all five principles with their exact wording, the named actors and their compliance status, the full technical mechanism list, and the enforcement gaps.
**Date note:** the post is from September 2025 but was modified 2026-07-15. What changed is not marked in the page. Treat compliance statements about specific companies as **possibly stale and definitely contested** — see caveats.

## Summary

Five proposed rules for how AI crawlers should behave, plus the economic argument for why AI labs should want them. The argument chain: AI answers cut referral traffic → publishers lose the revenue that funds content → content quality falls → AI labs lose the high-quality training data they depend on. Cloudflare's position is that this harms every party, so voluntary alignment is self-interested rather than altruistic.

The five principles, as worded:

1. **Public disclosure** — *"Companies should publicly disclose information about their AI bots."* Identity (user agent, IP ranges, cryptographic ID), operator (legal entity plus contact), and purpose.
2. **Self-identification** — *"AI bots should truthfully self-identify."* Today by user agent plus IP verification; destination is cryptographic verification.
3. **Declared single purpose** — *"AI bots should have one distinct purpose and declare it."* One of **search**, **AI-input** (RAG, grounding, real-time answers), or **training**.
4. **Respect preferences** — *"...where proportionate and technically feasible."* Via `robots.txt` (RFC 9309), HTTP headers, and the IETF AI preferences vocabulary.
5. **Act with good intent** — *"AI bots must not flood sites with excessive traffic or engage in deceptive behavior."*

**Principle 3 is the one with teeth,** and it is the only novel contribution. The others restate existing norms. Single-purpose declaration attacks bundling: a crawler that indexes for search *and* grounds AI answers forces *"an impossible choice onto website owners"* — permit both or lose search visibility. Cloudflare's rebuttal to the efficiency defence is the two-pizzas analogy: *"cost of the two pizzas … remains the same"* whether ordered together or separately, so bundling saves the operator nothing that justifies removing the publisher's choice.

The unnamed target of principle 3 is Google, which combines search indexing with AI Overviews. The post criticises the pattern and offers no mechanism against it.

## Key Claims

- **The declared-purpose taxonomy is the reusable artifact:** search (index and return links), AI-input (RAG, grounding, live generative answers), training (model training and fine-tuning). Three purposes, each with a different bargain for the publisher — search sends traffic back, AI-input substitutes for the visit, training pays nothing and returns nothing.

- **Cryptographic identity is the stated destination for bot trust.** *"Every AI bot should be cryptographically verified"* via **Web Bot Auth** (IETF draft) over **HTTP Message Signatures (RFC 9421)**. The reason given: *"bots are increasingly vulnerable to being spoofed by bad actors."*

- **User-agent identification is structurally inadequate.** It is a self-reported string with no verification, so every preference mechanism keyed to it — including all of `robots.txt` — is only as good as the crawler's honesty.

- **Compliance is uneven, and Cloudflare names names.** OpenAI is held up as the positive case (separate GPTBot for training, OAI-SearchBot for search; the ChatGPT agent signs requests with Web Bot Auth). Perplexity is accused of *"stealth undeclared crawlers to evade website no-crawl directives."* Anthropic is described as publishing a user agent only. Of xAI: *"grok, does not self-identify at all."* Vercel is credited with shipping Web Bot Auth support.

- **Preference expression is being standardised at the IETF,** through the AI preferences working group vocabulary, which is intended to give `robots.txt` purpose-aware granularity it does not have.

- **The zero-click mechanism is the named harm.** Pew is cited for reduced clicking when an AI summary is present; a Forbes piece, "The 60 Problem," is cited for the scale of decline.

- **Cloudflare's own vantage claim:** it handles *"on average 84 million requests per second,"* which is the basis both for its observations and for its ability to enforce (one-click blocking, pay-per-crawl).

## Useful Examples

**The three-purpose taxonomy** is the thing to take from this source. It converts "should we allow AI crawlers" — unanswerable — into three separate decisions with different economics:

| Purpose | What the publisher gives | What the publisher gets |
|---|---|---|
| **Search** | Index access | Referral traffic, attribution |
| **AI-input** | Live content for generated answers | Possibly a citation; the visit is substituted |
| **Training** | Content as training data | Nothing directly |

**OpenAI's bot split** (GPTBot / OAI-SearchBot) is the working demonstration that separating purposes is technically trivial — which is what makes bundling a choice rather than a constraint.

**The two-pizzas analogy** is a clean rebuttal to the efficiency defence for bundling, and it generalises to any argument that combining consent decisions saves cost.

**The mechanism stack:**

| Mechanism | Status |
|---|---|
| `robots.txt` (RFC 9309) | Published standard, unverifiable by design |
| HTTP Message Signatures (RFC 9421) | Published RFC |
| Web Bot Auth | IETF draft, in development |
| HTTP Message Signatures Directory | IETF draft |
| IETF AI Preference Vocabulary | Working group draft |
| Pay-per-crawl, one-click blocking | Cloudflare products, shipping |

## Constraints / Caveats

- **Cloudflare sells the enforcement.** Blocking and pay-per-crawl are commercial products that these principles create demand for. The post does not disclose this as an interest. It is the single most important thing to hold in mind when reading the compliance accusations.
- **The compliance statements are contested and possibly stale.** The post is from September 2025 with an unmarked July 2026 modification. Perplexity publicly disputed the stealth-crawling accusation when it was made. Do not repeat any company-specific compliance claim from this source as current fact without checking the company's own bot documentation.
- **Principle 4's escape hatch is the whole framework's weak point.** *"Where proportionate and technically feasible"* is undefined, and it is the clause any non-complying operator would invoke.
- **No enforcement mechanism and no signatories.** No penalties are proposed, no formal adoption list exists, and the principles are framed as *"starting points."* Compliance rests on consensus plus Cloudflare's commercial blocking — which is enforcement by one company's infrastructure, not by agreement.
- **The framework's integrity depends on a standard that does not exist yet.** Until Web Bot Auth is deployed, principles 1–3 are self-reported strings. The post is honest that the standard is in development, and does not dwell on what that means for the interim.
- **The AI-input / training boundary is not resolvable as stated.** A cached grounding corpus and a training set differ in intent, not in mechanism, and the post does not say how a publisher or a verifier would tell them apart.
- **The traffic-decline evidence is second-hand and thin.** Pew is cited without figures; "The 60 Problem" is a magazine headline, not a measurement. The 84-million-requests-per-second figure is Cloudflare's own and unaudited. **No adoption metric appears anywhere** — the post never says what share of crawlers comply with any principle, which is the number it is best placed to supply.
- **Good faith is assumed.** *"Most players … want to do the right thing"* is asserted. The post's own accusations against three named companies argue the other way.

## Design Implications

- **Decide crawler policy per purpose, not per company.** The three-purpose split is the useful unit, and it makes the trade explicit: search is a trade, AI-input is a substitution, training is a donation.
- **Do not build a policy that depends on user-agent honesty** for anything that matters. Treat `robots.txt` as a request, not a control, until signature verification is deployed.
- **Watch Web Bot Auth as the load-bearing dependency.** Every claim about verifiable bot identity in this space is downstream of that draft landing and being adopted.
- **For anyone building an agent that fetches the web:** declare one purpose, publish identity and contact, fetch `robots.txt` before crawling, and sign requests once signing is available. The principles are a reasonable specification for the crawler side even without an enforcement regime.
- **For research operations:** an agent that retrieves sources on a researcher's behalf is an AI-input crawler under this taxonomy, and inherits its consent obligations. This vault's own ingest activity sits in that category.

## Tensions

- **Direct conflict with [[wiki/sources/google-search-io-2026-agents|Google Search I/O 2026]], ingested in the same batch.** Cloudflare's principle 3 says a bot must declare one purpose and not bundle in a way that removes the publisher's choice. Two months earlier Google announced **Information Agents** that monitor *"blogs, news sites and social posts"* 24/7, and Generative UI that substitutes a generated surface for a visited page — with no discussion of consent, compensation, or crawl declaration. The two sources describe the same infrastructure from the two ends of the bargain and neither acknowledges the other's position. This is the sharpest live conflict in the vault's current source set.
- **Supplies the missing mechanism for [[wiki/concepts/product-management/geo-generative-engine-optimization|GEO]].** The vault's GEO material treats AI answer surfaces as an optimisation target. This source says the traffic those surfaces replace is the *problem* being governed. Same phenomenon, opposite posture: GEO asks how to be cited, this asks whether being crawled at all is a fair trade.
- **Extends [[wiki/concepts/ai-agents/agent-identity|agent identity]] from an intra-system concern to an internet-scale one.** Web Bot Auth is agent identity as a wire protocol — the first concrete cryptographic answer in this vault to "which agent is this, really."
- **Against [[wiki/concepts/agent-experience/checkbox-transparency|checkbox transparency]] and the vault's disclosure scepticism.** Principles 1–3 are disclosure obligations, and [[wiki/concepts/agent-experience/agent-transparency|agent transparency]] now records two independent findings that disclosure barely moves behaviour. The rebuttal here is real and worth stating: the audience is a *machine-readable policy engine*, not a human deciding under time pressure. Disclosure to a filter can be enforced; disclosure to a person relies on them reading it. Whether that distinction holds depends entirely on Web Bot Auth landing — without verification, this too is a checkbox.
- **The vendor-interest structure mirrors [[wiki/concepts/agent-experience/principal-agent-problem|the principal–agent problem]]:** the party proposing the rules, naming the violators, and selling the enforcement is the same party.

## Open Questions

- Has Web Bot Auth advanced since this post, and has anyone beyond OpenAI and Vercel deployed it? This is the single fact that decides whether the framework is real; it is checkable and this vault has not checked it.
- What is the actual compliance rate? Cloudflare can measure it at 84M req/s and does not publish it.
- Can the AI-input / training boundary be verified by anyone, or is it only ever a declaration?
- What did the 2026-07-15 modification change? An undated edit to a post making specific accusations is a provenance problem.
- Do the referral-traffic figures hold up under independent measurement, or is "The 60 Problem" doing more work in this argument than it can bear?
- If enforcement runs through one CDN's products, what is the governance difference between an industry norm and a single vendor's terms?

## Concepts Linked from This Source

- [[wiki/concepts/infrastructure-dev/ai-crawler-governance|AI Crawler Governance]] *(new)*
- [[wiki/concepts/ai-agents/agent-identity|Agent Identity]]
- [[wiki/concepts/ai-agents/agent-authorization|Agent Authorization]]
- [[wiki/concepts/ai-agents/agentic-search|Agentic Search]]
- [[wiki/concepts/product-management/geo-generative-engine-optimization|GEO (Generative Engine Optimization)]]
- [[wiki/concepts/infrastructure-dev/cloud-ai-governance|Cloud AI Governance]]
- [[wiki/concepts/agent-experience/agent-transparency|Agent Transparency]]
- [[wiki/concepts/agent-experience/principal-agent-problem|Principal–Agent Problem]]
- [[wiki/concepts/ai-agents/ai-news-intermediary|AI News Intermediary]]

## LLM Use Guidance

- **Use the three-purpose taxonomy** (search / AI-input / training) whenever reasoning about crawler consent, publisher economics, or agent fetching policy. It is the durable contribution.
- **Use the mechanism table** to know what exists (RFC 9309, RFC 9421) versus what is drafted (Web Bot Auth, AI preference vocabulary). The distinction matters and gets blurred in secondary coverage.
- **Do not repeat the company compliance claims as current fact.** They are from a vendor with a commercial stake, at least one is publicly disputed, and the page has been silently edited since publication.
- **Do not cite the traffic-decline figures.** Pew is cited without numbers and the Forbes reference is a headline.
- **Do not present the principles as adopted.** There are no signatories and no enforcement.
- When this vault's own agents fetch sources, they are AI-input crawlers by this taxonomy — a useful frame for its own ingest ethics.

## Reliability Notes

- **Confidence 0.64.** The technical content is solid and checkable: the RFCs are real, the IETF drafts are real and named with links, the three-purpose taxonomy is coherent and useful, and OpenAI's bot split is verifiable independently. Cloudflare genuinely does have the vantage point it claims.
- Held down by: an undisclosed commercial interest in the enforcement layer; company-specific accusations that are contested and possibly stale behind an unmarked edit; second-hand and headline-grade evidence for the economic premise; no adoption or compliance data from the one party who can measure it; and an undefined feasibility escape clause in the principle that would do the most work.
- **The taxonomy and the mechanism inventory are the trustworthy parts. The compliance narrative is advocacy.** Separating those two is the whole skill of using this source.
- **Highest-value verification step:** current status of the Web Bot Auth IETF draft and its adoption list. If it has shipped and spread, this framework is becoming infrastructure; if it has stalled, the principles remain unverifiable self-reporting and the confidence here should fall.
