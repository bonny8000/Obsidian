---
type: concept
status: draft
created: 2026-07-30
updated: 2026-08-04
tags: [concept, ux-research, ux-metrics, standardized-questionnaires, psychometrics, ai-ux, trust, dependency, needs-validation]
sources: [measuringu-measuring-the-ux-of-ai, saeidehbakhshi-usability-metrics-static-product]
confidence: 0.65
---

# AI UX Measurement Constructs

> [!abstract] Summary
> Six candidate constructs for measuring the UX of generative AI chat, proposed by Sauro & Lewis as a **34-item diagnostic layer** beneath a UX-Lite baseline: **AI Productivity, AI Trust, AI Dependency, AI Anxiety, AI Personification, Early Adoption**. UX-Lite answers *how good is it*; these answer *what is driving that*.

> [!warning] Draft — an item pool, not a validated instrument
> No factor structure, no reliability coefficients, no convergent or discriminant validity, and **no response format or scale anchors stated**. The authors say validation is forthcoming. `status: draft` and `confidence: 0.65` reflect that. Do not report scores from these as if comparable to SUS or UX-Lite benchmarks.

## The six constructs

| Construct | Items | Example item | What it plausibly measures |
|---|---:|---|---|
| **AI Productivity** | 8 | "Using this AI chatbot greatly improves my productivity" | Perceived usefulness — the closest to a conventional UX outcome |
| **AI Trust** | 7 | "I trust this AI chatbot to provide reliable information" | Willingness to rely |
| **AI Dependency** | 3 | "I tend to accept answers from AI chatbots without verifying their accuracy" | **Non-verification behavior**, self-reported |
| **AI Anxiety** | 7 | "The increasing use of AI makes me uneasy" | Respondent disposition toward AI in general |
| **AI Personification** | 6 | "Interacting with this AI chatbot feels like communicating with a human" | Perceived humanness |
| **Early Adoption** | 3 | "I like to experiment with new technologies before most people do" | Respondent trait |

8 + 7 + 3 + 7 + 6 + 3 = **34 items**. Development convention cited: minimum three items per construct.

## 📝 Key Claims

- **Layer, don't replace.** Overall usefulness/usability first (UX-Lite), then AI-specific diagnostics. A good top-line score can otherwise conceal a trust or dependency problem beneath it.
- **Generic UX metrics under-describe AI products** — hence the diagnostic layer.
- **Dependency is already measurable and already a problem.** Context figures cited: **66%** rely on AI output without verifying; **56%** made mistakes from uncritical acceptance.
- **Pair attitudinal with behavioral.** Questionnaires are cheap; completion rates, errors and task time are rigorous. Both are recommended, and the 66% figure implies stated trust and actual verification diverge.
- **Validation is the named next step** — factor structure, item retention, and links to brand attitude, continuance intent, and recommendation intent.

## Two constructs may be measuring the respondent, not the product

**This is the most important reservation on the page and the anchor source does not address it.** *AI Anxiety* and *Early Adoption* are dispositions a person brings to the session; *AI Productivity* and *AI Personification* are judgments about a specific product. Mixing them into one instrument risks a factor structure that reflects **who answered** rather than **what they used**.

The likely correct use is as **moderators or segmentation variables**: an early adopter with low AI anxiety will rate almost any AI product higher, and knowing that is valuable — as a covariate, not as a UX score. Expect this to surface when the factor analysis publishes.

## Practical guidance if you field this now

1. **Treat it as an item bank, not a scale.** Pull items, do not compute a composite and call it validated.
2. **You must choose a response format** — none is given. That is itself a measurement decision (point count, anchors, neutral midpoint) and it will affect your results.
3. **Separate product constructs from respondent traits** in your analysis plan up front.
4. **Pilot and cut.** Expect items to fail; 34 items is a starting pool, not a final questionnaire.
5. **Add a behavioral measure of verification** if dependency matters to you. Self-reported non-verification is a weak proxy for observed non-verification — and per [[wiki/sources/nngroup-accelerating-research-with-ai|NN/g]], behavior is precisely where language-based instruments are weakest.
6. **Report it as provisional** in any deck. The authors do.

## ⚖️ Conflicts & Caveats

> [!warning] Authority–evidence asymmetry
> Sauro & Lewis wrote the standard references in quantitative UX, which makes it tempting to treat these six as settled. They are not, and the authors are clearer about that than a reader is likely to be.

> [!warning] Personification is measured without being evaluated
> Whether an interface *feels human* is measurable; whether that is *desirable* is a separate question this vault treats with caution — see [[wiki/concepts/agent-experience/parasocial-relationship|Parasocial Relationship]] and [[wiki/concepts/agent-experience/companion-attachment-dependency|Companion Attachment & Dependency]]. A higher Personification score is not self-evidently a better product.

> [!warning] Dependency has a double valence
> Measuring dependency as a UX quality issue assumes everyone wants it lowered. [[wiki/concepts/product-management/ai-advertising|AI advertising]] makes non-verification **commercially valuable** — the same construct is a defect to a researcher and an asset to an ad-funded platform. See [[wiki/analyses/2026-07-30-trust-measurement-and-monetization|the 2026-07-30 memo]].

> [!warning] All context statistics are second-hand
> The 66% / 56% figures, and the Microsoft–LinkedIn, Anthropic, KPMG and AP-NORC numbers, arrive without methodology. Trace before quoting.

> [!warning] Scope
> Chat-based generative AI only. Explicitly may not transfer to recommendation systems, embedded AI features, or agentic execution.

> [!warning] On adaptive products, the validity conditions move under the instrument — added 2026-08-04
> This page's reservations are all about the instrument's *construction* — factor structure, response format, product-versus-trait confounds. [[wiki/sources/saeidehbakhshi-usability-metrics-static-product|Bakhshi (2026)]] adds a reservation about its *referent*: on a personalised or adaptive product, *"the score is conditional on the user, their history, the state of the system, and the stage of use"* — so *"the number may be precise while the underlying construct it is measuring is not the same thing."*
>
> The two critiques are compatible and unflattering in combination. Even a fully validated version of these six constructs would still be measuring a moving object unless the conditions are pinned and reported.
>
> **Two direct consequences for this instrument:**
>
> - **AI Trust and AI Dependency are trajectory variables, not levels.** Both plausibly change as a user's relationship with a system matures, which means a single administration is a snapshot of an unknown point on a curve. Bakhshi's argument is that on adaptive products the direction is the finding.
> - **The scope caveat above becomes sharper.** "May not transfer to recommendation systems" understates it: recommendation systems are precisely the case where the product differs per user and per session, so a benchmark across respondents is comparing different products.
>
> **Practical addition to the guidance list above:** report the product state and the respondent's stage of use alongside any score from this item bank. See [[wiki/concepts/ux-research/measurement-under-adaptation|Measurement Under Adaptation]] and [[wiki/concepts/ux-research/steerability|Steerability]] — the latter is a construct these six do not cover and adaptive products need.

## 🔗 Related Concepts

- [[wiki/concepts/ux-research/ux-metrics|UX Metrics]] — the parent frame.
- [[wiki/concepts/ux-research/self-reported-ux-metrics|Self-Reported UX Metrics]] — the measurement family this belongs to.
- [[wiki/concepts/ux-research/reliability-vs-validity|Reliability vs. Validity]] — the standard this instrument has not yet met.
- [[wiki/concepts/agent-experience/trust-calibration|Trust Calibration]] — the theory these items would operationalize.
- [[wiki/concepts/agent-experience/companion-attachment-dependency|Companion Attachment & Dependency]] — the risk side of Personification and Dependency.
- [[wiki/concepts/agent-experience/satisfaction-vs-benefit|Satisfaction vs. Benefit]] — why a high self-reported score may not mean the user was helped.
- [[wiki/concepts/ux-research/validity-and-decision-relevance|Validity and Decision Relevance]]
- [[wiki/concepts/ux-research/ux-performance-benchmarking|UX Performance Benchmarking]]
- [[wiki/concepts/ux-research/heart-framework|HEART Framework]]

## 📚 Sources

- [[wiki/sources/measuringu-measuring-the-ux-of-ai|Sauro & Lewis (2026): Measuring the UX of AI]] — sole source: the six constructs, the item examples, the layered approach.
- [[wiki/sources/sauro-lewis-quantifying-ux-2016|Sauro & Lewis (2016): Quantifying the User Experience]] — the authors' foundational reference, for the psychometric standards this instrument has yet to meet.

## ❓ Open Questions

- Do six constructs survive factor analysis, or collapse into three or four?
- What response format and anchors are intended?
- Do AI Anxiety and Early Adoption load as product constructs or respondent traits?
- **Does self-reported AI Dependency predict observed verification behavior?** The question that decides whether the construct is useful or merely interesting.
- How do the constructs relate to continuance and recommendation intent?

## Backfill Status

**Blocked on the authors' validation article.** When it publishes, upgrade this page and [[wiki/sources/measuringu-measuring-the-ux-of-ai|the source page]] rather than creating duplicates: record the surviving factor structure, retained items, response format, and reliability coefficients, then promote `draft → active` and revise confidence. That follow-up is the single most valuable thing to ingest next in this area.
