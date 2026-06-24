---
type: source
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [ux-research, sampling, representative-sample, claim-based-sampling, selection-bias, validity, product-research]
source_path: raw/web/bakhshi-representative-sample-2026-06-22.md
source_url: https://saeidehbakhshi.substack.com/p/there-is-no-such-thing-as-a-representative
authors: [Saeideh Bakhshi]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.85
---

# Bakhshi (2026): There Is No Such Thing as a Representative Sample

**Author:** Saeideh Bakhshi — Research Toolbox (Substack)
**Published:** 2026-06-22
**Raw capture:** [[raw/web/bakhshi-representative-sample-2026-06-22|bakhshi-representative-sample-2026-06-22]]
**URL:** [saeidehbakhshi.substack.com/p/there-is-no-such-thing-as-a-representative](https://saeidehbakhshi.substack.com/p/there-is-no-such-thing-as-a-representative)
**Related in vault:** [[sources/saeidehbakhshi-the-fallacy-of-depth-at-scale|The Fallacy of Depth at Scale]] · [[sources/saeidehbakhshi-wicked-work-ai-unbundles-research|The Wicked Work…]] · [[sources/saeidehbakhshi-long-accommodation|The Long Accommodation]]

## Citation

Bakhshi, S. (2026, June 22). *There is no such thing as a representative sample.* Research Toolbox (Substack). Captured 2026-06-22 into `raw/web/bakhshi-representative-sample-2026-06-22.md`.

## Summary

"We need a representative sample" is usually a vibe, not a design. Demographic quota-matching is inherited from opinion polling — where demographics correlate with the outcome and population margins are known from the census. **Product research is different:** the outcomes we care about (task completion, onboarding, adoption, retention, willingness to pay, error recovery, trust after failure) are driven by *behavioral/contextual* variables (intent, tenure, plan tier, prior experience, workflow complexity, integration depth, role, stakes, job-to-be-done), not demographics. The thesis: **a sample is not representative in the abstract — it is only more or less adequate for a specific claim about a specific population.** Design the sample *backward from the claim.*

## Key Claims

- Two users identical on demographics can have completely different relationships to the product (new vs power user, casual vs blocked) — matching on demographics doesn't make them equally informative for a claim.
- Separate the layers and watch every gap: **target population** → **sample frame** → **realized sample** → **respondents**.
- **Four claim types, four sampling logics:**
  - **Prevalence** (how common): fails if entrants are systematically different on the estimated thing (e.g., surveying only onboarding *completers*); more N = a precise *wrong* number.
  - **Existence** (does it happen at all): one well-documented case can suffice; sample the *tail* conditions; the "middle" is the wrong place to look.
  - **Explanatory** (why): the sample MUST include people who had the outcome (churned, dropped off); survivors-only → coherent-but-wrong explanation.
  - **Comparison** (group difference): each group must represent its subgroup via *comparable* recruitment; mismatched recruitment confounds the difference.
- **Three failure modes:** (1) balanced on the wrong (easy-to-quota) variables; (2) selected by the outcome (nonresponse / self-selection / survivorship); (3) changing the claim after sampling (reading a detection/existence study as a frequency study — a category error).
- "More respondents reduce variance but do not remove bias." Adding N to a self-selected sample = a tighter number around the wrong answer.

## Useful Examples

- **Onboarding prevalence:** "80% of new users understand onboarding" can't come from completers only — they survived the very thing being estimated.
- **Payments failure (existence):** to find "users get stuck when a bank connection fails," sample small-bank / multi-account / older-device / recently-changed-employer users, *not* a demographically balanced average.
- **Trial non-conversion (explanatory):** interviewing only active payers explains why it works for stayers, not why others didn't convert.
- **New vs power users (comparison):** forum-recruited power users + intercept-recruited new users → the "difference" mixes tenure with recruitment.

## Constraints / Caveats

- Authoritative practitioner essay (former Meta/industry researcher), not a study; framed for product research specifically.
- Demographic quotas still matter for fairness, accessibility, regulatory, market-specific, or demographically-driven outcomes — the point is they're not the *default* definition of representation.

## Design Implications

- Replace "is the sample representative?" with **"representative *for what claim*?"** Make the claim type (prevalence / existence / explanatory / comparison) an explicit design input.
- Add a pre-study checklist: who is the claim about? who can recruiting reach? who's missing in a way that changes the answer? balanced on outcome-predicting variables or just quota-easy ones? is the sample available *because of* the outcome?
- Pairs directly with [[concepts/ux-research/llm-user-proxy|LLM user proxies]] and synthetic users: a proxy/synthetic sample is also only adequate *for a claim*, never representative in the abstract.

## Tensions

- Against the reflexive "match the customer base on demographics → call it representative" habit widespread in product orgs.
- Complements the [[sources/myrealtrip-polaris-cancellation-recommendation|Myrealtrip Polaris]] case's own honesty that a ~70% lift from *observational* data isn't a clean causal effect — same family of inference discipline.

## Open Questions

- How to operationalize "claim-first sampling" as a lightweight team ritual without heavy methodology overhead?
- For mixed claims in one study, how to sequence/segment recruitment so each claim is supportable?

## Concepts Linked

- [[concepts/ux-research/claim-based-sampling|Claim-Based Sampling]] (new)
- [[concepts/ux-research/participant-selection-criteria|Participant Selection Criteria]]
- [[concepts/ux-research/sample-size-for-usability-studies|Sample Size for Usability Studies]]
- [[concepts/ux-research/validity-and-decision-relevance|Validity and Decision Relevance]]
- [[concepts/ux-research/reliability-vs-validity|Reliability vs Validity]]
- [[concepts/ux-research/methodological-integrity|Methodological Integrity]]
- [[concepts/ux-research/research-strategy|Research Strategy]]

## LLM Use

- **Use for:** designing/critiquing a sampling plan from the claim backward; naming the claim type; spotting selection-by-outcome and "claim changed after sampling" errors; pushing back on demographic-quota-as-representation.
- **Do not use for:** as a stats reference (it's conceptual); cases where demographics genuinely drive the outcome (fairness/accessibility/regulated) — there quotas matter.
- **Best prompt pattern:** "State the claim type (prevalence/existence/explanatory/comparison) for this study, then design the sample backward: who must be included, who's missing in a way that changes the answer, and which variables actually predict the outcome."

## Reliability Notes

> [!warning] Caveats
> - **Practitioner essay**, full text captured. Confidence 0.85 on the framework (clear, well-argued, standard sampling theory applied to product research); it's a viewpoint, not new empirical evidence.

## Backfill Status

- New 2026-06-22 from full web capture. All sections populated. Cross-linked to existing Bakhshi sources.
