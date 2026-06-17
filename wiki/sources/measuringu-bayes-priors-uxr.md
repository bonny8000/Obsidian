---
type: source
status: active
created: 2026-06-17
updated: 2026-06-17
tags: [source, ux-research, statistics, bayesian, priors, sensitivity-analysis, quant-uxr]
source_path: raw/web/measuringu-bayes-priors-uxr-2026-06-17.md
source_url: https://measuringu.com/bayes-law-in-ux-research-the-power-and-perils-of-priors/
authors: [Jeff Sauro, Jim Lewis]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.88
---

# MeasuringU: Bayes' Law in UX Research — The Power and Perils of Priors

**Authors:** Jeff Sauro, PhD and Jim Lewis, PhD
**Published:** 2026-03-31 — MeasuringU
**Raw capture:** [[raw/web/measuringu-bayes-priors-uxr-2026-06-17|measuringu-bayes-priors-uxr-2026-06-17]]
**URL:** [measuringu.com/bayes-law-in-ux-research-the-power-and-perils-of-priors/](https://measuringu.com/bayes-law-in-ux-research-the-power-and-perils-of-priors/)

## Citation

Sauro, J., & Lewis, J. (2026, March 31). *Bayes' law in UX research: The power and perils of priors.* MeasuringU.

## Summary

The companion piece to the credible-vs-confidence interval article. Using the same 18-of-20 task-completion case study, the authors show how **the choice of prior changes the conclusion** even when the observed data does not. Across five priors, four of five favored 90% as the more likely completion rate — but a strong prior favoring a historical 78% baseline *reversed* that conclusion. Headline: *"Changing the prior assumption had a larger effect on the conclusion than a modest increase in sample size would."* The recommendation is to use Bayesian methods *thoughtfully and transparently* — be explicit about priors, run sensitivity analyses, and collect more data when conclusions depend heavily on assumptions.

## Key Claims

- Prior beliefs are numerical weights assigned to competing hypotheses *before* analyzing current data.
- Same data (18/20 successes, 90% completion rate), five prior scenarios, dramatically different conclusions:
  - **Neutral priors:** 90% completion rate is **2.7×** more likely.
  - **Strong prior favoring historical 78%:** 78% becomes more likely than 90%.
  - **Strong prior favoring 90%:** 90% is **10.9×** more likely.
- **"Changing the prior assumption had a larger effect on the conclusion than a modest increase in sample size would."** — quotable headline finding.
- Four out of five scenarios still favored 90% — but the one that reversed (strong 78%-favoring prior) demonstrates how a single defensible-seeming prior can flip a finding.
- Recommendations for researchers:
  1. Be explicit about prior selection methodology.
  2. Conduct prior sensitivity analysis (try multiple priors, report range).
  3. Exercise caution with uncertain priors.
  4. Collect additional data when conclusions heavily depend on assumptions.

## Useful Examples

- The five-scenario sensitivity analysis as a quotable case for stakeholder education.
- The 2.7× vs 10.9× Bayes-factor language as a tangible way to communicate strength of evidence.
- The "prior assumption beats modest sample-size increase" finding as a counter-narrative to "just add more participants."

## Constraints / Caveats

- Single case study (18/20 successes). The flip-on-strong-historical-prior effect is most pronounced when n is small and the historical baseline is close to but different from the observation.
- The article focuses on *binary* outcomes with Beta priors. Continuous metrics and other distributions are out of scope.
- "Strong" priors are not formally defined — readers need familiarity with Beta-distribution parameterization to judge what counts as strong.
- The article doesn't recommend a *default* prior policy for UX research teams; it leaves the choice (and its disclosure) to the researcher.

## Design Implications

- **Default to a transparent prior.** When using credible intervals in a report, name the prior (Beta(1,1) Uniform, Jeffreys, Agresti) so reviewers can judge.
- **Run sensitivity analysis by default.** Report at least two priors when a Bayesian result drives a decision — one non-informative, one informed by history.
- **Beware the "strong historical prior" trap.** When the historical rate is close to but different from the observed rate, a strong historical prior can flip the conclusion. Surface this explicitly.
- **Use Bayes factors (2.7×, 10.9×) for stakeholder language.** They translate "how strong is the evidence" into a tangible ratio that most stakeholders intuit faster than p-values.
- **When conclusions depend on the prior, collect more data.** The prior dominates small samples; data dominates large samples.

## Tensions

- **Power of priors vs ease of misuse.** Informative priors let prior knowledge inform analysis — but they also let a researcher pick the answer they want. Disclosure and sensitivity analysis are the only honest defense.
- **Default-prior practice vs principled-prior practice.** Always using Uniform priors is safe but throws away genuine historical knowledge. Always using strong informative priors is risky. The middle path — disclose, sensitivity-test, document — costs time.
- **Bayesian rigor vs stakeholder simplicity.** Stakeholders want one number. Bayesian rigor gives them a range of conclusions across priors. The translation work is non-trivial.

## Open Questions

- What is the right prior policy for Bonny's UX work — Uniform default, with informative priors only when documented historical baselines exist?
- Should internal dashboards force the analyst to declare a prior before showing a credible interval?
- For agent-augmented UX research, can an agent automate sensitivity analysis (try 3 priors, flag when conclusions diverge)? This is a natural Skill candidate.

## Concepts Linked

- [[concepts/ux-research/bayesian-priors-in-uxr|Bayesian Priors in UXR]] (new)
- [[concepts/ux-research/bayesian-credible-interval|Bayesian Credible Interval]] (new — companion concept)
- [[concepts/ux-research/adjusted-wald-confidence-interval|Adjusted-Wald Confidence Interval]]
- [[concepts/ux-research/quant-uxr-rigor|Quant UXR Rigor]]
- [[concepts/ux-research/methodological-integrity|Methodological Integrity]]
- [[concepts/ux-research/sample-size-for-usability-studies|Sample Size for Usability Studies]]

## LLM Use

- **Use for:** justifying explicit prior selection in Bayesian UX analysis, designing prior-sensitivity-analysis protocols, training stakeholders on Bayes-factor language (2.7×, 10.9×), recognizing when small-sample conclusions depend on priors.
- **Do not use for:** specific informative-prior recommendations without historical evidence; claims about Bayesian superiority over frequentist methods (the companion credible-vs-confidence article makes clear they often agree under non-informative priors).
- **Best prompt pattern:** "Run a prior sensitivity analysis on this UX completion-rate observation: compute credible intervals under Beta(1,1) Uniform, Beta(0.5, 0.5) Jeffreys, and a Beta prior matching the historical baseline. Report Bayes factors for each, flag if conclusions diverge, and recommend collect-more-data vs. act."

## Reliability Notes

> [!warning] Caveats
> - **Single illustrative case.** The "prior beats sample size" finding is dramatized by a small n.
> - **Beta-distribution priors only.** Other distributional choices (e.g., for time, satisfaction means) have different sensitivity behavior.
> - **Confidence:** 0.95 on the framing and recommendations; 0.9 on the specific Bayes factors (verifiable by reproducing the calculation); 0.85 on the "prior beats sample size" headline (true for small-n binary; less universal at larger n).

## Backfill Status

- New 2026-06-17. Full sections populated.
