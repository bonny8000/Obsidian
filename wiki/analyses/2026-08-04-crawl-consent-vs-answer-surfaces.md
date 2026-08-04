---
type: analysis
status: active
created: 2026-08-04
updated: 2026-08-04
tags: [analysis, ai-crawlers, publisher-economics, geo, web-bot-auth, agent-identity, governance, conflict, memo]
sources:
  - cloudflare-responsible-ai-bot-principles
  - google-search-io-2026-agents
  - google-good-seo-is-good-geo
  - hai-headlines-ai-news-audit
  - kakao-vc-ai-agent-advertising
confidence: 0.60
---

# Crawl Consent vs. Answer Surfaces: A Conflict the Vault Should Not Merge Away

**Memo date:** 2026-08-04 · Written under AGENTS.md Rule 11 and the Conflict Handling rules.

## Research Question

Two sources ingested in the same batch describe the same infrastructure from opposite ends of a bargain and never acknowledge each other. **What is actually in dispute, what is settled, and what would resolve it?**

## Evidence Base

| Source | Position | Confidence |
|---|---|---|
| [[wiki/sources/cloudflare-responsible-ai-bot-principles\|Cloudflare (2025/2026)]] | Crawlers must declare one purpose and honour operator preferences | 0.64 |
| [[wiki/sources/google-search-io-2026-agents\|Google Search I/O (2026)]] | 24/7 agents monitoring blogs/news/social; generated surfaces free to all | 0.55 |
| [[wiki/sources/google-good-seo-is-good-geo\|Kraham / Google (2026)]] | Publishers should optimise for being cited in AI answers | 0.90 |
| [[wiki/sources/hai-headlines-ai-news-audit\|Suzgun & Zou (2026)]] | Six chatbots audited on same-day news: retrieval and citation failures | 0.80 |
| [[wiki/sources/kakao-vc-ai-agent-advertising\|Kakao Ventures (2026)]] | Conversational recommendation defeats disclosure; hidden intent undetected >90% | — |

## The Conflict, Stated Precisely

**Cloudflare's principle 3:** a bot must have *one distinct purpose* and declare it — search, AI-input, or training — and must not combine purposes *"in a way that prevents web operators from deliberately and effectively deciding"* which uses they permit. The unnamed target is Google, for bundling search indexing with AI Overviews. The rebuttal to the efficiency defence is the two-pizzas analogy: bundling saves the operator nothing that justifies removing the publisher's choice.

**Google, two months earlier:** **Information Agents** that operate *"in the background, 24/7"* over *"blogs, news sites and social posts"*; **Generative UI free to all Search users**, assembling bespoke layouts in place of a page of links; **conversational follow-ups** designed to keep the user inside Search. Consent, compensation, attribution, and crawl declaration appear **nowhere** in the announcement.

Neither source engages the other. This memo records the disagreement rather than resolving it, per the vault's conflict-handling rule.

## Synthesis

### 1. What is genuinely settled

**The three-purpose taxonomy is good analysis regardless of who proposed it.** Search, AI-input, and training are three different bargains:

| Purpose | Publisher gives | Publisher gets |
|---|---|---|
| Search | Index access | Referral traffic, attribution |
| AI-input | Live content for generated answers | Possibly a citation; the visit is substituted |
| Training | Content as training data | Nothing directly |

**And separating them is technically trivial.** OpenAI already runs GPTBot (training) and OAI-SearchBot (search) as distinct declared bots. That fact is verifiable independently of Cloudflare and it is what converts bundling from a constraint into a choice. This is the strongest point in the entire cluster and it does not depend on trusting any party's advocacy.

### 2. What is not settled, and cannot be yet

**Every preference mechanism in existence is keyed to a self-reported string.** `robots.txt` (RFC 9309) operates per user agent, and a user agent is forgeable. So the whole consent layer of the web currently runs on crawler honesty.

Cryptographic verification — **Web Bot Auth**, an IETF draft over **RFC 9421** HTTP Message Signatures — is the proposed fix and **is not deployed.** Until it is, principles 1 through 3 are unverifiable declarations.

**This is the load-bearing fact of the whole cluster, and this vault has not checked its current status.** Whether AI crawler governance is becoming infrastructure or remains aspiration turns on one IETF draft's adoption. That check is the single highest-value action below.

### 3. The GEO contradiction inside Google's own output

Google publishes both sides:

- [[wiki/sources/google-good-seo-is-good-geo|Kraham (Think with Google, 2026)]] tells publishers how to be cited in AI answers — implying being cited is the reward and worth optimising for.
- [[wiki/sources/google-search-io-2026-agents|Reid (I/O 2026)]] ships Generative UI free to every Search user — a generated layout that substitutes for the visit, with no stated citation guarantee.

**"Optimise to be cited" and "the answer is now a generated component" are not obviously compatible.** GEO's existing tactics assume a text answer with attributable links. When the surface becomes an assembled layout with simulations and interactive tables, what counts as a citation is unsettled, and Google has not said. [[wiki/concepts/product-management/geo-generative-engine-optimization|The vault's GEO page]] needs this caveat.

### 4. The independent evidence undercuts the citation promise

[[wiki/sources/hai-headlines-ai-news-audit|Suzgun & Zou's audit]] of six commercial chatbots on same-day news is the only *independent measured* source in this cluster, and it found retrieval and citation-attribution failures. That matters here because the entire publisher-side bargain in the AI-input case rests on citation working. **Measured evidence says it does not work reliably** — which weakens Google's implicit promise and strengthens Cloudflare's case, without either party's advocacy being involved.

### 5. Both parties' framings are self-serving in the same structural way

Cloudflare proposes the rules, names the violators, and **sells the enforcement** (one-click blocking, pay-per-crawl) — an undisclosed interest, and structurally [[wiki/concepts/agent-experience/principal-agent-problem|the principal–agent problem]]. Google's announcement omits the publisher side of a bargain it is a party to.

Symmetry is not equivalence, though. Cloudflare's technical claims are checkable (real RFCs, real drafts, OpenAI's verifiable bot split); its *compliance narrative* is advocacy — company accusations from a vendor with a stake, at least one publicly disputed, behind an **unmarked July 2026 edit** to a September 2025 post. Google's product descriptions are reliable and its usage figures (1B monthly AI Mode users, queries doubling quarterly) are unauditable first-party claims with no stated definitions.

**Separating each party's checkable content from its advocacy is the operative skill, and it is a different cut for each.**

### 6. The gap nobody in this cluster covers: the third party

Google's agentic booking now extends to **placing phone calls to businesses on a user's behalf**. Every governance framework here concerns crawlers and publishers. None covers a party the agent *contacts* who has no interface, no disclosure, and no consent — and no concept in this vault covers it either.

Add to that [[wiki/sources/kakao-vc-ai-agent-advertising|Kakao Ventures']] finding that hidden intent in conversational recommendation goes undetected **over 90%** of the time. The pattern generalises: as agents mediate more, the parties bearing the consequences are increasingly the ones with no seat at the interface.

## Implications

1. **Adopt the three-purpose split as the working frame** for crawler policy, agent-fetching ethics, and publisher-side decisions. It survives both parties' interests.
2. **Treat `robots.txt` as a request, not a control,** for anything consequential — and say so when advising anyone.
3. **Add the substitution caveat to GEO work.** Optimising for citation assumes the answer surface cites. Independent measurement says citation is unreliable, and generative layouts make "cited" undefined.
4. **Do not repeat either party's numbers.** Cloudflare's economic premise rests on Pew-without-figures and a magazine headline; Google's usage figures have no definitions. Both are unusable as evidence.
5. **Recognise the vault's own position in the taxonomy.** An agent fetching sources for a researcher is an **AI-input crawler**. This vault's ingest activity — including today's — sits in the category whose consent norms are being argued over. Worth stating explicitly rather than leaving implicit.
6. **Watch for third-party consent as an emerging concept gap.** Agent-to-business contact has no coverage in this vault and is now shipping.

## Risks and Counterpoints

- **The economic premise is not established here.** "AI answers reduce traffic → content quality falls" is plausible and rests on second-hand evidence in this cluster. It may be true; these sources do not show it.
- **The Cloudflare compliance claims may be stale or wrong.** An unmarked edit to a post making specific accusations is a provenance defect, and this memo relies on the framework rather than the accusations.
- **Google may have publisher-side commitments not in this announcement.** A product post is not a policy statement, and absence of discussion is not evidence of absence of policy.
- **Confidence 0.60** reflects a cluster with one independently measured source (the HAI audit) and four with commercial interests in their own conclusions.
- **Selection risk:** this memo's frame — a two-sided bargain — is itself a choice. A user-welfare frame or a competition-law frame would organise the same sources differently and is not obviously worse.

## Next Research Actions

1. **Check the current status and adoption list of the Web Bot Auth IETF draft.** One fact, decisive for the whole cluster, not yet checked here. **Highest priority.**
2. **Check the IETF `aipref` vocabulary's progress** — whether purpose-aware preferences became a standard or stalled.
3. **Find independent measurement of AI-answer referral impact.** The economic premise needs a real source; both current citations are inadequate.
4. **Verify which I/O 2026 capabilities actually shipped** — particularly whether agentic calling discloses itself to the business being called.
5. **Open a concept page on third-party consent in agent-mediated contact** if a second source appears. One source is not enough; the gap is real and worth watching.
6. **Re-audit [[wiki/concepts/product-management/geo-generative-engine-optimization|GEO]] against generative answer surfaces.** Its tactics assume a surface that may no longer be the default.

## Sources

- [[wiki/sources/cloudflare-responsible-ai-bot-principles|Cloudflare (2025/2026): Responsible AI Bot Principles]]
- [[wiki/sources/google-search-io-2026-agents|Google (2026): Search at I/O 2026 — AI Agents and More]]
- [[wiki/sources/google-good-seo-is-good-geo|Kraham / Google (2026): Good SEO is Good GEO]]
- [[wiki/sources/hai-headlines-ai-news-audit|Suzgun & Zou (2026): Real-Time Audit of Six Commercial Chatbots]]
- [[wiki/sources/kakao-vc-ai-agent-advertising|Kakao Ventures (2026): AI Agents and Advertising]]

## Concepts

- [[wiki/concepts/infrastructure-dev/ai-crawler-governance|AI Crawler Governance]]
- [[wiki/concepts/ai-agents/agent-identity|Agent Identity]]
- [[wiki/concepts/product-management/geo-generative-engine-optimization|GEO]]
- [[wiki/concepts/ai-agents/ai-news-intermediary|AI News Intermediary]]
- [[wiki/concepts/agent-experience/delegation-spectrum|Delegation Spectrum]]
- [[wiki/concepts/agent-experience/principal-agent-problem|Principal–Agent Problem]]
