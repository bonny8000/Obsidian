---
type: source
status: active
created: 2026-06-17
updated: 2026-06-17
tags: [source, ux-research, statistics, bayesian, credible-interval, confidence-interval, adjusted-wald, quant-uxr]
source_path: raw/web/measuringu-credible-vs-confidence-intervals-2026-06-17.md
source_url: https://measuringu.com/credible-vs-confidence-intervals/
authors: [Jeff Sauro, Jim Lewis]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.9
---

# MeasuringU: Credible vs. Confidence Intervals — Different Meanings but Similar Decisions

**Authors:** Jeff Sauro, PhD and Jim Lewis, PhD
**Published:** 2026-04-08 — MeasuringU
**Raw capture:** [[raw/web/measuringu-credible-vs-confidence-intervals-2026-06-17|measuringu-credible-vs-confidence-intervals-2026-06-17]]
**URL:** [measuringu.com/credible-vs-confidence-intervals/](https://measuringu.com/credible-vs-confidence-intervals/)

## Citation

Sauro, J., & Lewis, J. (2026, April 8). *Credible vs. confidence intervals: Different meanings but similar decisions.* MeasuringU.

## Summary

A practical comparison of frequentist confidence intervals (adjusted-Wald) and Bayesian credible intervals on a UX-relevant binary case — 18 of 20 task completions (90% completion rate). The four methods give intervals **within ~5% of each other in width and position** (29.7% / 27.4% / 26.3% / 28.6%), and the confidence interval "encompassed two of the Bayesian intervals" — so the practical decision is the same. The difference is **interpretation**, not numbers. Confidence intervals are widely taught but hard to explain correctly; credible intervals match how stakeholders naturally think ("95% probability the true value is in this range") but are computationally heavier. Authors' decision rule: *"If you'd make the same decision for both endpoints, then you have enough information to make the decision. Otherwise, you need more data."*

## Key Claims

- The technically correct frequentist interpretation — "If we ran many tests with 20 users and computed confidence intervals each time, on average, 95 out of 100 intervals will contain the unknown population completion rate" — is a poor stakeholder explanation.
- **Common but technically incorrect interpretations:**
  - "There's a 95% probability the true completion rate is between X and Y."
  - "There's a 95% chance the true rate falls within these bounds."
  - "95% of future tests will show rates in this range."
- **Practical fallback phrasings** (not technically Bayesian but defensible): "the *likely range*" or "values inside are *plausible*; values outside are implausible."
- Bayesian credible intervals **do** support "95% probability the true value is in this range" — by construction.
- For the 18/20 case, four 95% intervals:

  | Method | Prior/Setup | 95% Interval | Width |
  | --- | --- | --- | --- |
  | Adjusted-Wald | Add ~2 successes & ~2 failures | 68.7% – 98.4% | 29.7% |
  | Bayesian credible | Beta(1,1) Uniform prior | 69.6% – 97.0% | 27.4% |
  | Bayesian credible | Beta(0.5, 0.5) Jeffreys prior | 71.6% – 97.9% | 26.3% |
  | Bayesian credible | Beta(2, 2) Agresti prior | 66.4% – 95.0% | 28.6% |

- *"The numbers don't know where they come from"* — the same data yields nearly the same range; the difference is what you can *say* about it.
- **Decision rule:** make the call at both endpoints. If both endpoints lead to the same decision, you have enough data. If not, collect more.
- The frequentist confidence interval in this case "encompassed two of the Bayesian intervals," giving it both 95% frequentist confidence and at least 95% Bayesian credibility.

## Useful Examples

- The four-row interval table — directly quotable when stakeholders ask "what's the difference?"
- The 18-of-20 / 90% example — small-n UX standard scenario.
- The "decide at both endpoints" rule — a stakeholder-ready test for "do we have enough data?"
- The three common-but-wrong interpretations of frequentist CIs — useful in training materials.

## Constraints / Caveats

- Single example. The "near-equivalence" of intervals depends on a moderate proportion (0.9) and small n (20). At extreme proportions or very small n, frequentist and Bayesian intervals diverge more.
- The Bayesian intervals shown are all *symmetric / non-informative* priors. With informative priors (especially strong ones), the divergence grows — see [[sources/measuringu-bayes-priors-uxr|Bayes' Law in UX Research: The Power and Perils of Priors]].
- The article assumes the audience has at least passing familiarity with adjusted-Wald. For audiences new to small-sample UX statistics, pair with [[sources/measuringu-statistics-30-participants|MeasuringU: Do Statistics Really Require 30 Participants?]].
- "Modern software handles" the Bayesian computation, but in practice many UX teams still don't have a Bayesian calculator wired into their dashboards.

## Design Implications

- **For stakeholder reporting:** when "95% probability the true value is in this range" matters for the audience, switch to Bayesian credible intervals. Otherwise, default to adjusted-Wald and use the **"likely range"** or **"plausible range"** phrasing instead of probability claims.
- **For decision-making:** use the *both-endpoints* rule. Walk both the lower and upper bounds against the decision criterion; act only if both lead to the same call.
- **For tooling:** an internal calculator should output both adjusted-Wald and at least one credible interval (Beta(1,1) Uniform is the safe default). MeasuringU offers a calculator.
- **For training:** make the three-common-mistakes list a teaching artifact for new UX researchers and AI-augmented research workflows.

## Tensions

- **Stakeholder clarity vs technical fidelity.** Bayesian intervals are easier to explain; frequentist intervals are more widely taught. Avoid pretending the frequentist interval is Bayesian by calling it a "probability range" — use the "likely range" phrasing instead.
- **Practical equivalence under flat priors vs divergence under informative priors.** The "near-equivalence" headline is true *only* with non-informative priors. When historical data justifies a strong prior, the methods can disagree — see the [[sources/measuringu-bayes-priors-uxr|Bayes priors article]].

## Open Questions

- What should an internal UX dashboard surface by default — adjusted-Wald, Bayesian credible, or both side by side?
- For very small n (≤ 5), do the methods still converge, or is one preferred?
- For comparisons of two proportions (A/B testing), is there a Bayesian analog of the N − 1 two-proportion test, and does it tell the same story?

## Concepts Linked

- [[concepts/ux-research/bayesian-credible-interval|Bayesian Credible Interval]] (new)
- [[concepts/ux-research/adjusted-wald-confidence-interval|Adjusted-Wald Confidence Interval]] (updated with credible-interval comparison)
- [[concepts/ux-research/bayesian-priors-in-uxr|Bayesian Priors in UXR]] (new)
- [[concepts/ux-research/sample-size-for-usability-studies|Sample Size for Usability Studies]]
- [[concepts/ux-research/ux-statistics-decision-map|UX Statistics Decision Map]]
- [[concepts/ux-research/quant-uxr-rigor|Quant UXR Rigor]]

## LLM Use

- **Use for:** picking between adjusted-Wald and Bayesian credible intervals for a stakeholder audience, explaining what a confidence interval *actually* means, designing internal calculators, training new UXR-AI agents to report uncertainty correctly.
- **Do not use for:** comparison of two proportions (different methods apply), continuous metrics (use t-based intervals), or informative-prior Bayesian analysis (see [[sources/measuringu-bayes-priors-uxr|Bayes priors]]).
- **Best prompt pattern:** "Given a binary UX outcome of X of Y successes at 95% confidence, return both an adjusted-Wald interval and a Beta(1,1) Bayesian credible interval. State the stakeholder-ready interpretation in *plausible-range* phrasing, then apply the both-endpoints decision rule to recommend act / collect more."

## Reliability Notes

> [!warning] Caveats
> - **Single illustrative example.** Don't over-generalize the near-equivalence to extreme proportions or very small n.
> - **Non-informative priors only.** For informative priors, divergence grows — see the companion Bayes' priors article.
> - **Confidence:** 0.95 on the misinterpretations of frequentist CIs (well-established); 0.9 on the decision rule; 0.85 on the near-equivalence claim (true for the example, holds for moderate proportions and modest n).

## Backfill Status

- New 2026-06-17. Full sections populated.
