---
type: source
status: active
created: 2026-07-30
updated: 2026-07-30
tags: [ux-research, ux-metrics, standardized-questionnaires, ai-ux, psychometrics, trust, dependency, measuringu]
source_path: raw/web/measuringu-measuring-the-ux-of-ai-2026-07-30.md
source_url: https://measuringu.com/measuring-the-ux-of-ai/
authors: [Jeff Sauro, Jim Lewis]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.72
---

# Sauro & Lewis (2026): Measuring the UX of AI

## Citation

Jeff Sauro & Jim Lewis, *Measuring the UX of AI*, **MeasuringU**, 2026-07-28.

**Source type:** Practitioner methodology article from the authors of the field's standard quantitative UX references. **An instrument in development, not a validated instrument.**
**Raw capture:** [[raw/web/measuringu-measuring-the-ux-of-ai-2026-07-30|measuringu-measuring-the-ux-of-ai-2026-07-30]]

## Summary

Sauro & Lewis extend standardized UX measurement to generative AI chat, proposing a **34-item questionnaire across six constructs** on top of an existing UX-Lite baseline. The layering is the design idea: UX-Lite answers *how good is it*, the new constructs answer *what is driving that*.

The honest headline is what the article does **not** yet have. There is no factor structure, no reliability coefficient, no convergent validity, and no original data of any kind. The authors say so directly and commit to publishing validation later. Its value to this vault is as **a well-constructed hypothesis about what to measure**, from unusually credible authors — not as a usable scale.

## Key Claims

- **Layer the measurement.** Start with UX-Lite for overall usefulness and usability; add AI-specific constructs for diagnosis. This is the article's central methodological recommendation.
- **Generic UX metrics are insufficient for AI products.** Six constructs are proposed as the missing diagnostic layer.
- **Trust is the pivotal construct.** The authors cite surveys showing "less than half of people regularly using AI were willing to trust it."
- **Dependency is measurable and already problematic.** Cited: **66%** rely on AI output without verifying accuracy; **56%** made mistakes from uncritical acceptance.
- **Attitudinal is cheap, behavioral is rigorous.** Standardized questionnaires are easier to collect; completion rates, errors and task time are more rigorous and harder to get. Both are recommended.
- **Validation is the next step, not an afterthought** — factor structure, item retention, and relationships to brand attitude / continuance / recommendation intent are named as forthcoming work.

## Useful Examples

The proposed instrument, which is the reusable artifact:

| Construct | Items | Example item |
|---|---:|---|
| **AI Productivity** | 8 | "Using this AI chatbot greatly improves my productivity" |
| **AI Trust** | 7 | "I trust this AI chatbot to provide reliable information" |
| **AI Dependency** | 3 | "I tend to accept answers from AI chatbots without verifying their accuracy" |
| **AI Anxiety** | 7 | "The increasing use of AI makes me uneasy" |
| **AI Personification** | 6 | "Interacting with this AI chatbot feels like communicating with a human" |
| **Early Adoption** | 3 | "I like to experiment with new technologies before most people do" |

Item count checks out: 8 + 7 + 3 + 7 + 6 + 3 = **34**. Development convention cited: minimum three items per construct.

**Context statistics, all borrowed from other sources:** Microsoft–LinkedIn 2024, 90% reported time savings · Anthropic 2026, 86% reported faster work · Melbourne–KPMG, 48,000 respondents across 47 countries · AP-NORC 2025, 44% believed AI would hurt society more than help.

## Constraints / Caveats

- **No psychometric validation.** No factor analysis, no Cronbach's alpha, no discriminant or convergent validity. Using these six as if they were established constructs would be exactly the error the authors warn against: "Items that look sensible on paper don't always hold up once real people respond."
- **The scale format is not stated** in what was captured — no response anchors, no point count. **This alone blocks direct reuse**; the items cannot be fielded without deciding the response format, which is itself a measurement decision.
- **Two constructs look like traits, not product attributes.** *AI Anxiety* and *Early Adoption* measure the **respondent**, not the product. They plausibly belong as moderators or covariates rather than as UX outcomes — mixing them into a product-UX instrument risks a factor structure that reflects who answered rather than what they used. The article does not address this.
- **AI Dependency is a 3-item floor**, the bare minimum, for what is arguably the most consequential construct here.
- **Scope is chat-based generative AI.** Explicitly may not generalize to recommendation algorithms, fraud detection, or embedded AI features.
- **Every statistic is second-hand.** The borrowed figures come with no methodology in this article; the 66% / 56% dependency numbers are the ones most likely to be quoted and least verified here.
- Ingested from an AI-generated extraction, not a verbatim read.

## Design Implications

- **Measure the AI-specific layer separately from overall UX**, so a good UX-Lite score cannot hide a trust or dependency problem underneath it.
- **Treat dependency as a first-class metric, not a footnote.** If 66% do not verify, verification behavior is a design target — and it is measurable.
- **Separate product constructs from respondent traits** when fielding this. Anxiety and early-adoption tendency are better used to segment respondents than to score a product.
- **Do not field these six as a scale yet.** Use the item pool as a starting bank, write your own response format, and expect to cut items after piloting.
- **Personification deserves care.** Measuring whether an interface feels human is not the same as it being *desirable* that it does — see [[wiki/concepts/agent-experience/parasocial-relationship|Parasocial Relationship]] and [[wiki/concepts/agent-experience/companion-attachment-dependency|Companion Attachment & Dependency]] for the risk side.
- **Pair attitudinal with behavioral.** The article's own framing implies self-reported trust and observed verification behavior can diverge — and the 66% figure suggests they do.

## Tensions

- **The measurement problem it names is being actively monetized.** Read alongside [[wiki/sources/kakao-vc-ai-agent-advertising|Kakao Ventures (2026)]]: Sauro & Lewis want to *measure* AI trust and dependency; the Princeton figures in that source show sponsored recommendations succeed at **61.2%** through conversational AI versus 22.4% in search, and that explicit labels only pull it back to **55.5%**. Dependency is not just a UX quality issue — it is a commercial asset. Synthesized in [[wiki/analyses/2026-07-30-trust-measurement-and-monetization|the 2026-07-30 memo]].
- **Against [[wiki/sources/nngroup-accelerating-research-with-ai|NN/g's]] language-vs-behavior boundary.** NN/g's core finding is that self-reported data is where AI-assisted research works and behavior is where it fails. A 34-item attitudinal instrument sits squarely on the easy side of that line. It is the right *start* and cannot settle whether people actually verify.
- **Consistent with this vault's [[wiki/concepts/agent-experience/trust-calibration|Trust Calibration]] material, and adds the missing instrument.** Lee & See (2004) supply the theory — calibration, resolution, specificity; misuse/disuse — and this supplies candidate items. The pairing is useful; note the theory is validated and the items are not.
- **Authority vs. evidence asymmetry.** Sauro & Lewis are as credible as practitioner sources get in quantitative UX, which makes it tempting to treat the six constructs as settled. They are not, and the authors are clearer about that than a reader might be.

## Open Questions

- What is the actual factor structure — do six constructs survive, or collapse into three or four?
- What response format and anchors are intended?
- Do *AI Anxiety* and *Early Adoption* load as product constructs or as respondent traits?
- Does self-reported AI Dependency predict observed verification behavior? This is the question that would make the construct valuable rather than merely interesting.
- How do the constructs relate to continuance and recommendation intent — the outcome linkage the authors defer?

## Concepts Linked from This Source

- [[wiki/concepts/ux-research/ai-ux-measurement-constructs|AI UX Measurement Constructs]]
- [[wiki/concepts/ux-research/ux-metrics|UX Metrics]]
- [[wiki/concepts/ux-research/self-reported-ux-metrics|Self-Reported UX Metrics]]
- [[wiki/concepts/agent-experience/trust-calibration|Trust Calibration]]
- [[wiki/concepts/agent-experience/companion-attachment-dependency|Companion Attachment & Dependency]]
- [[wiki/concepts/ux-research/reliability-vs-validity|Reliability vs. Validity]]
- [[wiki/concepts/agent-experience/satisfaction-vs-benefit|Satisfaction vs. Benefit]]

## LLM Use

Cite for **what to measure in AI UX** and for the layered UX-Lite-plus-diagnostics approach. The item pool is genuinely useful as a starting bank when designing an AI product survey.

Do **not** cite it as a validated instrument, do not report scores from it as if they were comparable to SUS or UX-Lite benchmarks, and do not repeat the 66%/56% dependency figures without tracing them to their primary sources. Treat as **hypothesis-grade**: excellent for designing a study, insufficient for concluding one.

## Reliability Notes

- **Highly credible authors, deliberately preliminary artifact.** Sauro & Lewis wrote the standard references in quantitative UX ([[wiki/sources/sauro-lewis-quantifying-ux-2016|Quantifying the User Experience]] is already in this vault), and they flag the validation gap themselves.
- **Confidence 0.72** — high for the *reasoning* and the construct selection, capped by the total absence of data, the unstated scale format, and the trait-vs-attribute confound this page identifies.
- **Revisit when the validation article publishes** and upgrade this page rather than creating a second one. That follow-up is the single most valuable thing to ingest next in this area.
- Ingested from an AI-generated extraction; item wording should be re-verified against the original before fielding.
