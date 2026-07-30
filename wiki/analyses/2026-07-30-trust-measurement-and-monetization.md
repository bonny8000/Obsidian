---
type: analysis
status: active
created: 2026-07-30
updated: 2026-07-30
tags: [analysis, trust, dependency, ai-advertising, measurement, agent-experience, principal-agent, transparency]
sources:
  - measuringu-measuring-the-ux-of-ai
  - kakao-vc-ai-agent-advertising
  - hbs-working-knowledge-ai-advice-willful-blindness
  - lee-see-2004-trust-in-automation
  - theaxlabs-contaminated-memory-performance
confidence: 0.71
---

# Measuring Trust While Trust Is Being Monetized — 2026-07-30

## Research Question

Two sources ingested on 2026-07-30 describe the same phenomenon with opposite valence. Sauro & Lewis want to **measure** AI trust and dependency as UX quality constructs. Kakao Ventures shows that dependency is **commercially valuable** and that disclosure barely touches it.

The question this memo answers: **if non-verification is both a UX defect and a revenue asset, what does that mean for how trust is designed, measured, and regulated?**

The short answer: this vault's entire trust-calibration model assumes miscalibration is an *accident*. Once there is a party profiting from over-trust, calibration becomes an adversarial problem, and almost none of the existing design guidance was built for that.

## Evidence Base

| Source | Claim | Evidence grade |
|---|---|---|
| [[wiki/sources/measuringu-measuring-the-ux-of-ai\|Sauro & Lewis (2026)]] | AI Trust and AI Dependency are measurable UX constructs; 66% don't verify, 56% erred from uncritical acceptance | **Instrument in development — no validation, no original data** (0.72) |
| [[wiki/sources/kakao-vc-ai-agent-advertising\|Kakao Ventures (2026)]] | Conversational sponsored recommendations convert at 61.2% vs 22.4% search; labels only reduce to 55.5%; hidden intent detected <10% | Cited study, **parameters unknown**; VC blog (0.76) |
| [[wiki/sources/hbs-working-knowledge-ai-advice-willful-blindness\|Chan (2026)]] | Users skip available explanations when incentives point away | Working paper (existing vault source) |
| [[wiki/sources/lee-see-2004-trust-in-automation\|Lee & See (2004)]] | Calibration / resolution / specificity; misuse–disuse taxonomy | **Foundational, validated — but pre-LLM** |
| [[wiki/sources/theaxlabs-contaminated-memory-performance\|AX LABS (2026)]] | Stale memory silently miscalibrates trust | Practitioner report |

**Note the shape.** The theory is validated and 22 years old. The measurement instrument is unvalidated. The most consequential numbers are second-hand with unknown methodology. This memo is therefore a **framing contribution**, not an evidential one, and should be read as such.

## Synthesis

### 1. The same construct is a defect and an asset

Sauro & Lewis's *AI Dependency* items — "I tend to accept answers from AI chatbots without verifying their accuracy" — measure exactly the behaviour that makes conversational advertising work. Their cited **66% non-verification** rate and Kakao's **61.2% sponsored-selection** rate are two views of one population.

For a researcher, high dependency is a finding to act on. For an ad-funded platform, it is the conversion mechanism. Nothing in either source acknowledges the other's frame, and the collision matters: **a UX metric that a business model rewards moving in the wrong direction will not be optimized in the user's favour.** Any AI-UX measurement programme should therefore expect Dependency to be the construct most resistant to improvement, and should treat *who commissioned the study* as relevant methodological information.

### 2. Trust calibration was built for noise, not for an opponent

This vault's [[wiki/concepts/agent-experience/trust-calibration|Trust Calibration]] page lists the design levers: show provenance, express uncertainty honestly, preview-then-commit, make failures legible, progressive autonomy. Every one of those assumes miscalibration arises from *system properties* — stale memory, uniform confidence, poor error surfacing.

Introduce a party with an economic interest in over-trust and the levers behave differently:

- **Provenance** can be technically accurate and commercially selected. Citing a real source says nothing about which real sources were suppressed.
- **Uncertainty display** is a design choice made by the interested party.
- **Progressive autonomy** — earning wider permissions through demonstrated reliability — becomes exploitable, because reliability on verifiable tasks buys trust that transfers to unverifiable ones.

Lee & See's *resolution* property (trust differentiating across contexts) is exactly what a well-designed influence channel defeats: it makes the sponsored recommendation indistinguishable in form from the unsponsored one. **The 2004 model still describes the target; it does not describe the adversary.**

### 3. Disclosure has now failed twice, independently

Two unrelated results, one design conclusion:

- **Kakao/Princeton:** explicit "Sponsored" labels *plus warnings* moved selection from 61.2% to **55.5%** — roughly six points against a channel converting at nearly three times search rates.
- **Chan (2026):** users *skip* explanations that are already available when incentives point the other way — [[wiki/concepts/agent-experience/willful-blindness|willful blindness]].

The first says disclosure is weak when supplied; the second says explanation goes unread when offered. Together they make [[wiki/concepts/agent-experience/checkbox-transparency|checkbox transparency]] an empirical finding rather than a critique.

The mechanism worth naming: **disclosure works by inviting comparison.** In a results page there is something to compare against. In a single generated recommendation there is not. That is why the failure is structural rather than a labelling-design problem — and why it worsens as products move up the [[wiki/concepts/agent-experience/delegation-spectrum|delegation spectrum]].

### 4. The intervention point moves upstream of the interface

If disclosure is weak and calibration levers are capturable, the remaining leverage is **incentive structure**, which is not a UX surface at all. Kakao's proposal — spread compensation over time so the agent's payoff tracks the user's outcome, as insurance did — is the only intervention in this cluster that survives an adversarial reading, because it changes what the optimizing party *wants*.

This is uncomfortable for design and research practice: the most effective available intervention is a business-model decision, and the honest form of a trust audit is *"where does the money come from?"* rather than *"is the interface clear?"* Practically, that makes [[wiki/concepts/agent-experience/principal-agent-problem|principal–agent divergence]] a research question — auditable, testable — rather than an ethics preamble.

### 5. Measurement is still worth doing — for a different reason than stated

Sauro & Lewis frame their instrument as diagnosing product quality. This cluster suggests a second use they do not claim: **measured dependency is evidence in a governance argument.** A validated, benchmarked AI-Dependency score would let a researcher say *this product produces more non-verification than its category norm* — which is the kind of claim that survives contact with a regulator or an executive in a way that a heuristic critique does not.

That raises the stakes on the validation gap. An unvalidated 3-item construct cannot carry that weight. The forthcoming psychometric work is the load-bearing next step, and its absence is why this memo's confidence is 0.71 rather than higher.

## Implications

1. **Add "where does the money come from?" to trust review.** Before auditing provenance or uncertainty display, locate the divergence. Interface honesty is downstream of incentive alignment.
2. **Locate the product on the [[wiki/concepts/agent-experience/delegation-spectrum|delegation spectrum]] before choosing trust affordances.** At tier 3+ there is nothing to compare, so comparison-based interventions — including labels — do not apply.
3. **Stop treating disclosure as a control.** Two independent results now say it underperforms. Keep it for compliance; do not count it as a safeguard.
4. **Measure verification behaviour, not only self-reported dependency.** Per [[wiki/sources/nngroup-accelerating-research-with-ai|NN/g]], language-based instruments are weakest exactly where behaviour matters. Pair the items with an observed measure.
5. **Treat Personification with suspicion, not as an upside.** Measurable does not mean desirable — see [[wiki/concepts/agent-experience/parasocial-relationship|Parasocial Relationship]].
6. **Do not retire a gate on demonstrated reliability** where commercial incentives exist. Progressive autonomy assumes a non-adversarial counterparty.
7. **Push for the validation work.** A benchmarked dependency metric is more useful as governance evidence than as a product scorecard.

## Risks & Counterpoints

- **The decisive numbers are unverified.** The 61.2% / 55.5% / <10% figures are cited second-hand with no sample, task design, category, or venue. If they do not replicate, sections 3 and 4 weaken substantially. **This is the memo's single largest exposure.**
- **Two of five sources have aligned incentives.** Kakao Ventures profits from "trust is a moat"; MeasuringU profits from measurement being necessary. Neither is disqualifying; neither is disinterested.
- **The adversarial framing may be overdrawn.** Most AI products today are subscription- or usage-funded, where the divergence does not exist. This memo describes a risk concentrated in ad-funded consumer AI, and generalizing it to all agent design would be a mistake.
- **One-shot findings say nothing about habituation.** Users may become more skeptical of conversational recommendations with exposure, or less. The disclosure penalty could grow or shrink; no evidence either way.
- **The insurance analogy is untested** in high-frequency, low-value, unlicensed contexts.
- **No source in this cluster proposes a workable tier-3 intervention.** The memo identifies the gap and does not close it.
- **Lee & See predates LLMs by two decades.** Its properties are used here as a framework, and their transfer to generative agents remains formally unvalidated — a caveat this vault already carries on that source.

## Next Research Actions

- [ ] **Locate and ingest the Princeton study as a primary source.** Highest-value action in this cluster by a wide margin — it would anchor [[wiki/concepts/agent-experience/principal-agent-problem|principal–agent]], [[wiki/concepts/agent-experience/delegation-spectrum|delegation spectrum]], and [[wiki/concepts/product-management/ai-advertising|AI advertising]] all at once.
- [ ] **Ingest Sauro & Lewis's validation article when it publishes** — factor structure, retained items, response format, reliability. Upgrade the existing pages rather than duplicating.
- [ ] **Find or design a behavioural measure of verification** to pair with the self-reported Dependency construct. This is a genuinely open, tractable UX research question.
- [ ] **Source evidence on habituation** — does skepticism toward conversational recommendations increase with exposure?
- [ ] **Look for any tested tier-3 intervention** — a disclosure or comparison affordance that measurably changes behaviour when only one option is shown.
- [ ] **Track the Anthropic/OpenAI advertising divergence** as a natural experiment; revisit in six months.
- [ ] Consider a comparison page on **trust interventions by delegation tier** once a second independent source lands.

## Related

- [[wiki/concepts/agent-experience/principal-agent-problem|Principal–Agent Problem (AI)]]
- [[wiki/concepts/agent-experience/delegation-spectrum|Delegation Spectrum]]
- [[wiki/concepts/product-management/ai-advertising|AI Advertising]]
- [[wiki/concepts/ux-research/ai-ux-measurement-constructs|AI UX Measurement Constructs]]
- [[wiki/concepts/agent-experience/trust-calibration|Trust Calibration]]
- [[wiki/concepts/agent-experience/willful-blindness|Willful Blindness]]
- [[wiki/concepts/agent-experience/checkbox-transparency|Checkbox Transparency]]
- [[wiki/concepts/agent-experience/satisfaction-vs-benefit|Satisfaction vs. Benefit]]
- [[wiki/analyses/2026-07-28-constraining-ai-by-construction|Constraining AI by Construction]] — the same delegation axis viewed from reliability rather than commercial capture.
