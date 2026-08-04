---
type: concept
status: active
created: 2026-06-01
updated: 2026-08-04
tags: [ux-research, metrics, kpi, ai-ux]
sources: [nngroup-research-recommendations-roadmap, measuringu-measuring-the-ux-of-ai, saeidehbakhshi-usability-metrics-static-product]
confidence: 0.80
---

# UX Metrics

## Summary
UX metrics are quantitative measures used to track and evaluate the user experience of a product. They bridge the gap between qualitative user behavior and business-level key performance indicators (KPIs).

## Why it matters
Using the language of metrics is essential for gaining stakeholder buy-in. PMs are often measured on metrics like retention and conversion; research that links directly to these metrics is prioritized.

## Key Claims
- **Metric Alignment:** UX goals should be mapped to PM metrics (Retention, Activation, Conversion, Support Volume).
- **Usability Metrics:** Specific measures like task completion rate, satisfaction scores, and support-ticket volume can make usability investments legible to business stakeholders.
- **Risk Mitigation:** Metrics can also be used to frame "risk," such as potential drop-off due to poor navigation or legal risk from accessibility non-compliance.
- **AI products need a diagnostic layer beneath the top-line score.** [[wiki/sources/measuringu-measuring-the-ux-of-ai|Sauro & Lewis (2026)]] recommend UX-Lite for overall usefulness/usability, then AI-specific constructs to explain what drives it — because a healthy top-line score can conceal a trust or dependency problem underneath. See [[wiki/concepts/ux-research/ai-ux-measurement-constructs|AI UX Measurement Constructs]] (**unvalidated**).
- **Standard usability metrics assume a product that stays still.** On adaptive or personalised surfaces, effort, completion, error, and engagement all become conditional on the user, their history, the system state, and the stage of use — so *"the number may be precise while the underlying construct it is measuring is not the same thing"* ([[wiki/sources/saeidehbakhshi-usability-metrics-static-product|Bakhshi, 2026]]). Two consequences worth carrying: **less effort is ambiguous, not good** (*"the user had less room to compare, question, or change what happened"*), and **engagement can rise while the experience narrows.** See [[wiki/concepts/ux-research/measurement-under-adaptation|Measurement Under Adaptation]].
- **A metric a business model rewards moving the wrong way will not improve.** Self-reported non-verification ("AI Dependency") is a UX defect to a researcher and a **conversion mechanism** to an ad-funded platform. When selecting AI metrics, treat who commissioned the study as methodologically relevant — see [[wiki/analyses/2026-07-30-trust-measurement-and-monetization|the 2026-07-30 memo]].

## Related Concepts
- [[concepts/ux-research/heart-framework|HEART Framework]]
- [[concepts/ux-research/self-reported-ux-metrics|Self-Reported UX Metrics]]
- [[concepts/ux-research/ux-performance-benchmarking|UX Performance Benchmarking]]
- [[concepts/product-management/product-roadmap|Product Roadmap]]
- [[wiki/concepts/ux-research/ai-ux-measurement-constructs|AI UX Measurement Constructs]] — the AI-specific diagnostic layer.
- [[wiki/concepts/ux-research/measurement-under-adaptation|Measurement Under Adaptation]] — why these metrics' validity conditions move on personalised products.
- [[wiki/concepts/ux-research/steerability|Steerability]] — usability's missing partner for adaptive systems.
- [[wiki/concepts/agent-experience/trust-calibration|Trust Calibration]]

## Sources
- [[sources/nngroup-research-recommendations-roadmap|Research Recommendations and the Roadmap (NN/g)]]
- [[wiki/sources/measuringu-measuring-the-ux-of-ai|Sauro & Lewis (2026): Measuring the UX of AI]] — the layered approach and six candidate AI constructs. Instrument in development.
- [[wiki/sources/saeidehbakhshi-usability-metrics-static-product|Bakhshi (2026): Usability Metrics Assume the Product Stays Still]] — the conditionality argument, the effort-ambiguity claim, and the four-dimension alternative.

## Open Questions
- What are the most effective "proxy metrics" for long-term user trust?
- What is the minimum reportable condition set (whose goal, which product state, what outcome, what stage) that keeps a metric interpretable without making it unaffordable?
- How can we measure the impact of "micro-interactions" on high-level business KPIs?
- Does self-reported AI Dependency predict *observed* verification behavior? (The attitudinal/behavioral gap [[wiki/sources/nngroup-accelerating-research-with-ai|NN/g]] warns about.)

