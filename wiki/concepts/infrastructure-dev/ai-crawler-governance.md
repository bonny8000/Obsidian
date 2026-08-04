---
type: concept
status: active
created: 2026-08-04
updated: 2026-08-04
tags: [concept, infrastructure-dev, ai-crawlers, web-bot-auth, robots-txt, ietf, agent-identity, publisher-economics, governance, geo]
sources: [cloudflare-responsible-ai-bot-principles, google-search-io-2026-agents]
confidence: 0.64
---

# AI Crawler Governance

> [!abstract] Summary
> The emerging set of norms and mechanisms by which a website operator can know **which AI crawler is fetching, on whose behalf, and for what purpose** — and express a preference the crawler is expected to honour. Proposed as five principles by [[wiki/sources/cloudflare-responsible-ai-bot-principles|Cloudflare (2025/2026)]]; partly standardised at the IETF; enforceable today only by infrastructure, not by agreement.

## Why It Matters

The economic argument: AI answers reduce referral traffic → publishers lose the revenue that funds content → content quality falls → AI labs lose the high-quality data they depend on. If that chain holds, governance is self-interested for every party rather than a favour to publishers.

The technical argument is sharper and less contestable. **Every existing preference mechanism is keyed to a self-reported string.** `robots.txt` (RFC 9309) operates per user agent, and a user agent is trivially forgeable. So the entire consent layer of the web is only as good as the crawler's honesty — which is why cryptographic identity is the load-bearing dependency of everything else in this concept.

## The Three-Purpose Taxonomy

The durable contribution, and the reason to have this concept at all. It converts "should we allow AI crawlers" — unanswerable — into three decisions with different economics:

| Purpose | What the publisher gives | What the publisher gets |
|---|---|---|
| **Search** | Index access | Referral traffic, attribution |
| **AI-input** (RAG, grounding, live answers) | Live content for generated answers | Possibly a citation; the visit is substituted |
| **Training** | Content as training data | Nothing directly |

Cloudflare's principle 3 requires a bot to declare **one** of these and not bundle: bundling forces *"an impossible choice onto website owners"* — permit both or lose search visibility. The rebuttal to the efficiency defence is the two-pizzas analogy: *"cost of the two pizzas … remains the same"* whether ordered together or separately, so bundling saves nothing that justifies removing the choice.

**OpenAI's bot split (GPTBot for training, OAI-SearchBot for search) is the working demonstration that separating purposes is technically trivial** — which is what makes bundling a choice rather than a constraint.

## The Five Principles (Cloudflare, condensed)

1. **Public disclosure** — identity (user agent, IPs, cryptographic ID), operator legal entity with contact, and purpose.
2. **Self-identification** — *"AI bots should truthfully self-identify"*; destination is cryptographic verification.
3. **Declared single purpose** — one of search / AI-input / training, unbundled.
4. **Respect preferences** — via `robots.txt`, HTTP headers, and the IETF AI preferences vocabulary, *"where proportionate and technically feasible."*
5. **Act with good intent** — no traffic flooding, no stealth crawling, no user-agent rotation or ASN switching to disguise activity.

## Mechanism Inventory

Knowing what exists versus what is drafted is the practical value here, and secondary coverage blurs it:

| Mechanism | What it does | Status |
|---|---|---|
| `robots.txt` (**RFC 9309**) | Per-user-agent crawl preferences | **Published standard**, unverifiable by design |
| HTTP Message Signatures (**RFC 9421**) | The signing primitive | **Published RFC** |
| **Web Bot Auth** | Cryptographic bot identity over RFC 9421 | IETF **draft** |
| HTTP Message Signatures Directory | Key discovery | IETF **draft** |
| **IETF AI Preference Vocabulary** | Purpose-aware preference terms | Working group **draft** (`ietf-wg-aipref`) |
| Pay-per-crawl, one-click blocking | Commercial enforcement | Cloudflare products, shipping |

**Until Web Bot Auth deploys, principles 1–3 are self-reported strings.** That is the single fact that determines whether this concept describes infrastructure or aspiration.

## ⚖️ Conflicts & Caveats

> [!warning] The proposer sells the enforcement
> Cloudflare's blocking and pay-per-crawl products are the commercial beneficiaries of these principles. The post does not disclose this. Structurally it is [[wiki/concepts/agent-experience/principal-agent-problem|the principal–agent problem]]: the same party proposes the rules, names the violators, and sells the remedy.

> [!warning] Company compliance claims are contested and possibly stale
> The source names Perplexity (stealth crawling), Anthropic (user agent only), and xAI (no self-identification), and praises OpenAI and Vercel. The post is from September 2025 with an **unmarked July 2026 edit**, and at least one accusation was publicly disputed when made. **Do not repeat any company-specific compliance claim without checking that company's current bot documentation.**

> [!warning] "Where proportionate and technically feasible" is the escape hatch
> Undefined, and attached to the principle that would otherwise do the most work.

> [!warning] No enforcement, no signatories, no adoption data
> No penalties are proposed and no adoption list exists. Cloudflare can measure compliance at 84M requests/second and **does not publish a compliance rate** — the number it is uniquely placed to supply.

> [!warning] The AI-input / training boundary may not be verifiable at all
> A cached grounding corpus and a training set differ in intent, not in mechanism. Nothing in the framework says how a publisher or verifier would tell them apart.

> [!warning] The economic premise rests on thin evidence
> Pew is cited without figures; the scale claim traces to a magazine headline ("The 60 Problem"). The causal chain is plausible and not established by this source.

## The Live Conflict With Product Reality

Two months before the Cloudflare page's last edit, [[wiki/sources/google-search-io-2026-agents|Google announced]] **Information Agents** that monitor *"blogs, news sites and social posts"* 24/7, and **Generative UI free to all Search users** — a generated surface substituting for the visited page. Consent, compensation, attribution, and crawl declaration appear nowhere in that announcement.

The two sources describe the same infrastructure from the two ends of the bargain and **neither engages the other.** This concept holds the conflict rather than resolving it; see [[wiki/analyses/2026-08-04-crawl-consent-vs-answer-surfaces|the 2026-08-04 memo]].

## Practical Guidance

- **Set crawler policy per purpose, not per company.** Search is a trade, AI-input is a substitution, training is a donation. Three different decisions.
- **Treat `robots.txt` as a request, not a control**, for anything that matters — until signature verification is deployed.
- **Track Web Bot Auth's status.** Every claim about verifiable bot identity is downstream of that draft landing and spreading.
- **If you build a fetching agent:** declare one purpose, publish identity and a contact, fetch `robots.txt` before crawling, and sign requests once signing is available. The principles are a reasonable crawler-side specification even without enforcement.
- **Note the self-application.** An agent that retrieves sources on a researcher's behalf is an **AI-input crawler** by this taxonomy — including this vault's own ingest activity, which inherits the consent obligations it describes.

## 🔗 Related Concepts

- [[wiki/concepts/ai-agents/agent-identity|Agent Identity]] — Web Bot Auth is agent identity as a wire protocol; the first concrete cryptographic answer in this vault to "which agent is this, really."
- [[wiki/concepts/ai-agents/agent-authorization|Agent Authorization]]
- [[wiki/concepts/product-management/geo-generative-engine-optimization|GEO]] — the same phenomenon from the opposite posture: GEO asks how to be cited, this asks whether the crawl is a fair trade.
- [[wiki/concepts/ai-agents/agentic-search|Agentic Search]]
- [[wiki/concepts/ai-agents/ai-news-intermediary|AI News Intermediary]] — the publisher-economics side.
- [[wiki/concepts/infrastructure-dev/cloud-ai-governance|Cloud AI Governance]]
- [[wiki/concepts/infrastructure-dev/eu-ai-act-compliance|EU AI Act Compliance]] — the regulatory counterpart to this voluntary framework.
- [[wiki/concepts/agent-experience/agent-transparency|Agent Transparency]] — disclosure to a machine-readable policy engine, not to a human under time pressure. That distinction is this framework's best defence against the vault's disclosure scepticism, and it depends entirely on verification existing.
- [[wiki/concepts/agent-experience/principal-agent-problem|Principal–Agent Problem]]

## 📚 Sources

- [[wiki/sources/cloudflare-responsible-ai-bot-principles|Cloudflare (2025/2026): Responsible AI Bot Principles]] — primary source. The five principles, the three-purpose taxonomy, the mechanism inventory, and the compliance narrative (read as advocacy).
- [[wiki/sources/google-search-io-2026-agents|Google (2026): Search at I/O 2026]] — the counterparty's product announcements, which the framework's principles would constrain.

## ❓ Open Questions

- **Has Web Bot Auth advanced, and who has deployed it beyond OpenAI and Vercel?** The single fact that decides whether this concept describes infrastructure or aspiration. Checkable; not yet checked here.
- What is the actual compliance rate, and why does the party who can measure it not publish it?
- Can the AI-input / training boundary be verified by anyone, or is it only ever a declaration?
- What changed in the unmarked 2026-07-15 edit to a post making specific accusations?
- If enforcement runs through one CDN's products, what is the governance difference between an industry norm and a single vendor's terms of service?
- What happens to publisher economics when the generated surface is the free default and the visit is the exception?
