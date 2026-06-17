---
type: concept
status: active
created: 2026-06-17
updated: 2026-06-17
tags: [statistics, bayesian, credible-interval, quant-uxr, small-sample, completion-rate]
sources:
  - sources/measuringu-credible-vs-confidence-intervals
  - sources/measuringu-bayes-priors-uxr
confidence: 0.9
---

# Bayesian Credible Interval

> [!abstract] Summary
> A range of values that contains the true parameter with a stated probability *given* the data and a chosen prior. Unlike a frequentist confidence interval, a 95% Bayesian credible interval supports the natural-language interpretation "there is a 95% probability the true value lies in this range." For binary UX outcomes (task completion, conversion) the credible interval is computed from a Beta posterior given a Beta prior; common choices are Beta(1,1) Uniform, Beta(0.5, 0.5) Jeffreys, and Beta(2, 2) Agresti.

> [!important] Why it Matters
> Stakeholders consistently misinterpret frequentist confidence intervals as probability statements about the true value — and the correct frequentist phrasing is hard to land in a status meeting. Credible intervals deliver the interpretation people already make. Under non-informative priors they yield nearly identical numbers to adjusted-Wald, so the choice is often about *what you can say*, not *what you compute*.

## 📝 Key Claims

- For 18 of 20 task completions (90% completion rate), the four 95% intervals are within ~5% in width and position — under non-informative priors, frequentist and Bayesian methods produce **similar ranges, different interpretations**.
- The Beta posterior given a Beta(α, β) prior and *x* successes in *n* trials is Beta(α + x, β + n − x). The credible interval is the 2.5th–97.5th percentile of that posterior.
- **Common priors for binary UX data:**
  - **Beta(1,1) Uniform** — non-informative; default safe choice when no historical baseline exists.
  - **Beta(0.5, 0.5) Jeffreys** — non-informative; theoretically motivated by invariance under reparameterization.
  - **Beta(2, 2) Agresti** — mildly informative; pulls slightly toward 50%.
- The credible-interval interpretation depends on the prior. **With informative priors**, the same data can produce conclusions that reverse the Uniform-prior result — see [[concepts/ux-research/bayesian-priors-in-uxr|Bayesian Priors in UXR]].
- **Decision rule (Sauro & Lewis):** *"If you'd make the same decision for both endpoints, then you have enough information to make the decision. Otherwise, you need more data."* Apply at both the lower and upper bound of the credible interval.
- Under non-informative priors, the frequentist confidence interval often *encompasses* multiple credible intervals — meaning it has 95% frequentist confidence *and* at least 95% Bayesian credibility.

## Use When

- The stakeholder audience requires "probability the true value is in this range" framing.
- A binary UX outcome (completion, conversion, pass/fail) is being reported.
- Historical data exists that justifies an informative prior — and the team is willing to disclose it.
- Internal calculators or dashboards can deliver both adjusted-Wald and credible intervals side by side.

## Avoid When

- The audience is statistically literate and accepts adjusted-Wald with "likely range" phrasing.
- The metric is continuous (use t-based intervals) or involves comparison of two proportions.
- The team cannot disclose its prior — without disclosure, the credible interval is opaque.
- Software / pipeline support is not in place. The math is not hard, but the tooling friction can outweigh the interpretive gain.

## 🔗 Related Concepts

- [[concepts/ux-research/adjusted-wald-confidence-interval|Adjusted-Wald Confidence Interval]] — the frequentist counterpart; near-equivalent numbers under non-informative priors.
- [[concepts/ux-research/bayesian-priors-in-uxr|Bayesian Priors in UXR]] — how prior choice changes the credible interval.
- [[concepts/ux-research/sample-size-for-usability-studies|Sample Size for Usability Studies]]
- [[concepts/ux-research/ux-statistics-decision-map|UX Statistics Decision Map]]
- [[concepts/ux-research/quant-uxr-rigor|Quant UXR Rigor]]
- [[concepts/ux-research/standardized-usability-questionnaires|Standardized Usability Questionnaires]]
- [[concepts/ai-agents/agent-skills|Agent Skills]] — credible-interval calculator is a strong Skill candidate.

## ⚖️ Conflicts & Caveats

> [!warning] Prior-dependent conclusions
> The credible interval is only as defensible as the prior. With a strong informative prior, the same data can produce a different conclusion. Always disclose the prior; consider sensitivity analysis under multiple priors.

> [!warning] Computational practicalities
> Modern software handles the computation, but many UX teams still don't have a Bayesian calculator wired into their reporting pipeline. The gap is tooling, not theory.

## 📚 Sources

- [[sources/measuringu-credible-vs-confidence-intervals|MeasuringU: Credible vs. Confidence Intervals — Different Meanings but Similar Decisions]] (Sauro & Lewis, 2026)
- [[sources/measuringu-bayes-priors-uxr|MeasuringU: Bayes' Law in UX Research — The Power and Perils of Priors]] (Sauro & Lewis, 2026)
- [[sources/measuringu-statistics-30-participants|MeasuringU: Do Statistics Really Require 30 Participants?]] — background on small-sample UX statistics.

## ❓ Open Questions

- What should an internal UX dashboard surface by default — adjusted-Wald, Bayesian credible, or both side by side?
- For very small *n* (≤ 5), do credible intervals from different priors converge or diverge?
- Is there a clean Bayesian analog of the N − 1 two-proportion test for A/B comparisons, and does it tell the same story?
