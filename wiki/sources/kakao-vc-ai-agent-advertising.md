---
type: source
status: active
created: 2026-07-30
updated: 2026-07-30
tags: [ai-advertising, principal-agent, delegation, trust, agent-experience, regulation, monetization, kakao-ventures, korea]
source_path: raw/web/kakaovc-ai-agent-advertising-2026-07-30.md
source_url: https://www.kakao.vc/blog/ai-advertising
authors: [Kakao Ventures]
sources: []
ingest_level: deep
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.76
---

# Kakao Ventures (2026): AI Agents — Questioning the Qualifications of a True Representative

## Citation

Kakao Ventures, 「AI 에이전트, '진짜 대리인'의 자격을 묻다」 *(AI agents: questioning the qualifications of a true representative)*, **Kakao Ventures Blog**, 2026-07-29.

**Source type:** VC market analysis with a cited academic study. Forward-looking; part argument, part prediction.
**Raw capture:** [[raw/web/kakaovc-ai-agent-advertising-2026-07-30|kakaovc-ai-agent-advertising-2026-07-30]]

## Summary

The best-framed source in this vault on **what happens to advertising when an agent decides for you**. The reframe: search-era ads occupied *space* in a results page the user could compare against; agent-era ads infiltrate the *judgment-formation process itself*. That relocates competition from information access to **trustworthy delegation**, and makes the classic **principal–agent problem** the central design and regulatory question.

Its most valuable content is a cited Princeton study with numbers that should change how anyone reads "just label the sponsored results": conversational sponsored recommendations were selected at **61.2%** versus **22.4%** in search — and explicit "Sponsored" labels plus warnings only pulled that back to **55.5%**. When intent was hidden, users detected it **less than 10%** of the time.

## Key Claims

- **Advertising changes in kind, not degree.** From occupying space in a results page to shaping how a judgment gets formed. This is the claim the whole piece rests on and it is well argued.
- **Delegation is a spectrum, and commercial risk tracks it.** Four tiers, from filtered search to autonomous execution; influence opportunity and risk escalate together.
- **Disclosure is structurally insufficient here.** A 61.2% → 55.5% reduction under explicit labelling is the evidence. Labels work by inviting comparison; a single recommendation offers nothing to compare.
- **Restructure incentives rather than disclosing them.** The insurance analogy: spread commissions over time so the agent's payoff tracks the client's long-term outcome instead of the moment of sale.
- **Trust is a moat, not a compliance cost.** Competitive advantage will depend on demonstrable trustworthiness more than on raw model performance.
- **Regulation will arrive in three phases** — disclosure, then structure (recommendation mechanisms, performance-based payment contracts), then authority (limits on what an agent may execute without explicit approval).

## Useful Examples

**The Princeton figures** (as reported — see caveats):

| Condition | Sponsored-product selection |
|---|---:|
| Conversational AI, sponsored products with alternatives subtly downplayed | **61.2%** |
| Search engine, comparable setup | **22.4%** |
| Conversational AI **with explicit labels and warnings** | **55.5%** |
| User detection when intent was hidden | **< 10%** |

**The four-tier delegation spectrum:**

| Tier | What the user cedes | Named examples |
|---|---|---|
| 1. Filtered search | Almost nothing | Google Flights, Skyscanner |
| 2. Comparative recommendations | Shortlisting | Amazon Rufus |
| 3. Direct recommendations | The comparison itself | — |
| 4. Autonomous execution | The decision and the act | Amazon Buy for Me |

**Market positioning as a strategic signal:**

- **Anthropic** — rejected advertising outright; 2026 Super Bowl message quoted as *"Ads are coming to AI. But not to Claude."*
- **OpenAI** — advertising trials on free and budget ChatGPT tiers, expanding across countries.

Two frontier labs taking opposite positions on the same question, publicly, in the same year. That contrast is independently useful regardless of the rest of the argument.

## Constraints / Caveats

- **The Princeton study is cited, not characterized.** No sample size, task design, product category, incentive structure, or publication venue was captured. **These numbers are the most quotable thing in this source and the least verified.** Trace to the primary paper before any external use.
- **VC blog with an aligned conclusion.** "Trust is a moat" is congenial to a firm funding challengers to incumbent ad-funded platforms. The argument is good; the incentive is real and should be named.
- **The three-phase regulatory trajectory is prediction, not observation.** No jurisdiction, no draft legislation, no timeline is offered.
- **The insurance analogy is asserted, not tested.** Deferred-commission structures evolved over decades in a market with slow decision cycles, high contract values, and licensed intermediaries. AI recommendations are high-frequency, low-value, and unlicensed. The source acknowledges the transfer risk only in passing.
- **No technical feasibility discussion** for real-time explanation systems at the scale implied by "explainable recommendation architectures."
- **The Anthropic quotation** is a marketing message; treat as positioning, not policy commitment.
- Ingested from an AI-generated extraction of a Korean-language post, not a verbatim read.

## Design Implications

- **Locate your product on the delegation spectrum before designing trust affordances.** Tier 2 can rely on comparison; tiers 3 and 4 cannot, because there is nothing on screen to compare against. The interventions are not interchangeable.
- **Stop treating disclosure as the control.** If labelling moves behavior by ~6 points, a label is a compliance artifact, not a safeguard. This is [[wiki/concepts/agent-experience/checkbox-transparency|checkbox transparency]] with a number attached to it.
- **Audit the revenue model as a design surface.** Where the agent's payoff diverges from the user's outcome, no amount of interface honesty repairs it. Incentive structure is upstream of UX.
- **Make comparison recoverable at tiers 3–4.** If the agent picked one option, the design question is whether the user can cheaply see what was *not* picked and why.
- **Gate autonomous execution on explicit approval** — which is where the predicted "authority phase" of regulation and this vault's [[wiki/concepts/ai-agents/approval-gate|approval gate]] pattern converge from opposite directions, one commercial and one reliability-driven.
- **Treat verification affordances as a differentiator** rather than friction, if trust is genuinely a moat.

## Tensions

- **Sharpens [[wiki/concepts/agent-experience/trust-calibration|Trust Calibration]] with adversarial pressure it did not previously model.** That concept treats miscalibration as an accident to be designed against — stale memory, uniform confidence, poor provenance. This source adds a party with an *economic interest* in over-trust. Calibration against noise is a different problem from calibration against an optimizing counterparty.
- **Empirically undercuts transparency-as-solution**, which much of this vault's [[wiki/concepts/agent-experience/agent-transparency|agent-transparency]] material leans on. Alongside [[wiki/sources/hbs-working-knowledge-ai-advice-willful-blindness|Chan's willful-blindness finding]] (users skip explanations when incentives point the other way), there are now two independent results saying transparency mechanisms underperform expectations.
- **Complements [[wiki/sources/measuringu-measuring-the-ux-of-ai|Sauro & Lewis]] uncomfortably.** They propose measuring AI Trust and AI Dependency as UX quality constructs; this source shows dependency is a monetizable asset. Same phenomenon, opposite valence. See [[wiki/analyses/2026-07-30-trust-measurement-and-monetization|the memo]].
- **The delegation spectrum resembles this vault's constraint work from the user's side.** [[wiki/analyses/2026-07-28-constraining-ai-by-construction|Constraining AI by Construction]] asks how much *action* latitude an agent should get for reliability reasons; this asks how much *judgment* a user should cede given commercial capture. Same axis, different principal.
- **Against [[wiki/concepts/product-management/geo-generative-engine-optimization|GEO]] optimism.** If sponsored placement inside generated answers converts at 61.2%, generative-engine optimization is not a neutral discoverability discipline — it is the same influence channel viewed from the seller's side.

## Open Questions

- What are the Princeton study's actual parameters — sample, categories, incentives, venue? Without these, the 61.2% figure is directionally suggestive and not citable.
- Does the disclosure penalty (61.2% → 55.5%) shrink or grow with repeated exposure? A one-shot result says little about habituation.
- Is there any disclosure format that materially changes behavior at tier 3, where there is nothing to compare?
- Does deferred or outcome-linked compensation actually work for high-frequency, low-value recommendations?
- What would an auditable "no commercial influence" claim require technically — and could a user verify it?

## Concepts Linked from This Source

- [[wiki/concepts/agent-experience/delegation-spectrum|Delegation Spectrum]]
- [[wiki/concepts/agent-experience/principal-agent-problem|Principal–Agent Problem (AI)]]
- [[wiki/concepts/product-management/ai-advertising|AI Advertising]]
- [[wiki/concepts/agent-experience/trust-calibration|Trust Calibration]]
- [[wiki/concepts/agent-experience/agent-transparency|Agent Transparency]]
- [[wiki/concepts/agent-experience/checkbox-transparency|Checkbox Transparency]]
- [[wiki/concepts/agent-experience/willful-blindness|Willful Blindness]]
- [[wiki/concepts/ai-agents/approval-gate|Approval Gate]]
- [[wiki/concepts/product-management/geo-generative-engine-optimization|GEO / Generative Engine Optimization]]

## LLM Use

The **default source for AI advertising, delegation, and commercial trust capture.** Cite for: the space-versus-judgment reframe, the four-tier delegation spectrum, the disclosure-insufficiency finding, the incentive-restructuring proposal, and the Anthropic/OpenAI positioning contrast.

Attach the caveat every time the Princeton numbers are used: cited second-hand, parameters unknown. Use the *direction* freely; use the *decimals* only after verification. The regulatory three-phase model is a useful planning frame and not a forecast.

## Reliability Notes

- **Unusually well-structured for a VC blog post** — it names a mechanism, supplies a framework, cites evidence, and draws a falsifiable implication. That is why it earns `deep` rather than `light`.
- **Confidence 0.76:** the framing and the delegation spectrum are strong and internally coherent; the score is capped by second-hand statistics with no methodology, a predicted regulatory path, an untested cross-industry analogy, and the firm's investment incentive.
- **Highest-value verification step in this ingest:** locate the Princeton study and ingest it as a primary source. It would move several claims here from 0.76 toward 0.9 and would anchor [[wiki/concepts/agent-experience/principal-agent-problem|the principal–agent concept page]] properly.
- Fourth Kakao Ventures source in this vault, alongside [[wiki/sources/kakao-vc-upsell-design|upsell design]], [[wiki/sources/kakao-vc-ai-companion-relationship|AI companion relationships]], and [[wiki/sources/kakao-vc-ai-input-modality|input modality]] — a consistent publisher whose analytical quality has been reliable.
