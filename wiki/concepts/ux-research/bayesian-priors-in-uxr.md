---
type: concept
status: active
created: 2026-06-17
updated: 2026-06-17
tags: [statistics, bayesian, priors, sensitivity-analysis, methodological-integrity, quant-uxr]
sources:
  - sources/measuringu-bayes-priors-uxr
  - sources/measuringu-credible-vs-confidence-intervals
confidence: 0.88
---

# Bayesian Priors in UXR

> [!abstract] Summary
> A prior is the analyst's quantified belief about the parameter *before* the current data is observed. In UX research it can encode a historical baseline, a published benchmark, or a deliberately non-informative starting point. The choice of prior can flip a conclusion even when the data does not change. Honest practice = disclose the prior, run sensitivity analysis under multiple priors, collect more data when conclusions depend on the assumption.

> [!important] Why it Matters
> A Bayesian credible interval looks more intuitive than a frequentist confidence interval — but its credibility lives or dies on the prior. Sauro & Lewis (2026) showed that the same 18-of-20 task-completion observation can favor 90% **or** 78% depending on the prior, and **"changing the prior assumption had a larger effect on the conclusion than a modest increase in sample size would."** A team that quietly picks the prior that gives the answer it wants is doing motivated reasoning with statistical cover. Disclosure and sensitivity analysis are the only honest defense.

## 📝 Key Claims

- The **prior is a numerical weight assigned to competing hypotheses before observing the data.** It is not a confession of bias; it is documentation of background knowledge.
- **Five-scenario sensitivity result (Sauro & Lewis, 2026)** on 18-of-20 completion:
  - Neutral priors → 90% is **2.7×** more likely than alternatives.
  - Strong prior favoring historical 78% → **78% becomes more likely**.
  - Strong prior favoring 90% → 90% is **10.9×** more likely.
- Four of five priors favored 90%; only the strong-historical-78% prior reversed the result. Single-prior reporting hides this fragility.
- Common prior choices for binary UX outcomes:
  - **Beta(1,1) Uniform** — non-informative default.
  - **Beta(0.5, 0.5) Jeffreys** — non-informative with theoretical justification.
  - **Beta(2, 2) Agresti** — mildly informative; nudges toward 50%.
  - **Beta(α, β) informed by historical baseline** — α and β chosen so the prior mean matches the baseline and the spread reflects confidence in it.
- **Bayes factors** (2.7×, 10.9×) translate "how strong is the evidence" into a ratio stakeholders intuit faster than p-values.

## How to apply

- **Disclose the prior in every Bayesian UX report.** Without disclosure, the credible interval is opaque.
- **Run sensitivity analysis by default** — at least two priors (one non-informative, one informed by history). Report the range.
- **Use the prior–data tension as a signal.** When the answer flips between defensible priors, the conclusion is *not yet supported by data* — collect more.
- **Beware the "strong historical prior" trap.** When the historical rate is close to but different from the observed rate, a strong historical prior can dominate a small sample. Surface this explicitly.
- **Communicate with Bayes factors**, not just intervals. "10.9× more likely" lands faster than "the upper bound of the credible interval is X."

## 🔗 Related Concepts

- [[concepts/ux-research/bayesian-credible-interval|Bayesian Credible Interval]] — what the prior feeds into.
- [[concepts/ux-research/adjusted-wald-confidence-interval|Adjusted-Wald Confidence Interval]] — frequentist counterpart with no prior to disclose.
- [[concepts/ux-research/methodological-integrity|Methodological Integrity]] — disclosure of priors is part of integrity.
- [[concepts/ux-research/quant-uxr-rigor|Quant UXR Rigor]]
- [[concepts/ux-research/sample-size-for-usability-studies|Sample Size for Usability Studies]] — when the prior dominates, sample size is the lever.
- [[concepts/ai-agents/agent-skills|Agent Skills]] — prior-sensitivity analysis is a natural Skill candidate.

## ⚖️ Conflicts & Caveats

> [!warning] Power and peril
> Informative priors let prior knowledge inform analysis — and let a motivated researcher pick the answer they want. The defense is disclosure + sensitivity analysis, not "always use non-informative priors" (which throws away genuine knowledge).

> [!warning] Small-n amplification
> The "prior beats sample size" effect is most pronounced at small *n*. At larger *n* the data swamps any reasonable prior. For UX research, this means the prior matters most exactly where decisions are most consequential.

## 📚 Sources

- [[sources/measuringu-bayes-priors-uxr|MeasuringU: Bayes' Law in UX Research — The Power and Perils of Priors]] (Sauro & Lewis, 2026) — primary source for the five-scenario sensitivity demonstration.
- [[sources/measuringu-credible-vs-confidence-intervals|MeasuringU: Credible vs. Confidence Intervals]] (Sauro & Lewis, 2026) — companion piece showing near-equivalence under non-informative priors.

## ❓ Open Questions

- What is the right prior policy for Bonny's UX workflows — Uniform default with informative priors only when a documented historical baseline exists?
- Should internal dashboards force the analyst to declare a prior before showing a credible interval?
- Can an agent automate sensitivity analysis (try 3 priors, flag divergence, recommend act vs collect more)? This is a strong Skill candidate.
- For agent-augmented research, who is accountable for the prior — the analyst, the agent, or both?
