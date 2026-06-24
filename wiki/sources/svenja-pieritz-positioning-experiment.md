---
type: source
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [quant-uxr, positioning, between-subjects, purchase-intent, say-do-gap, willingness-to-pay, framing, consulting]
source_path: raw/web/svenja-pieritz-positioning-experiment-2026-06-22.md
source_url: https://www.svenjapieritz.com/articles/positioning-experiment
authors: [Svenja Pieritz]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.8
---

# Pieritz (2026): People Loved How I Described My Services — They Just Didn't Want to Hire Me For It

**Author:** Svenja Pieritz (Senior Quantitative UX Researcher; cognitive-science background)
**Published:** 2026-06-08 — svenjapieritz.com (2nd in a series on a self-run positioning study)
**Raw capture:** [[raw/web/svenja-pieritz-positioning-experiment-2026-06-22|svenja-pieritz-positioning-experiment-2026-06-22]]
**URL:** [svenjapieritz.com/articles/positioning-experiment](https://www.svenjapieritz.com/articles/positioning-experiment)

## Citation

Pieritz, S. (2026, June 8). *People loved how I described my services. They just didn't want to hire me for it.* svenjapieritz.com. Captured 2026-06-22 into `raw/web/svenja-pieritz-positioning-experiment-2026-06-22.md`.

## Summary

A between-subjects framing experiment on **90 senior decision-makers (n=30/cell)** testing three descriptions of the author's consulting service and measuring **relevance** vs **purchase intent**. The three framings: **person** (name/background first), **method** (the offer first), **problem** (the buyer's pain first). She was most confident in the **problem** framing. Result: all three scored similarly on *relevance*, but on *purchase intent* the **person framing won, method second, problem framing last** — the one she believed in most lost on the only metric that matters. The takeaway: **relevance ≠ buying intent**, and people want to know *who* is behind a complex service.

## Key Claims

- **Relevance and purchase intent are different measures.** A framing can feel relevant ("yes, this is my problem") and still not move anyone to hire — the gap *is* the finding.
- **Person framing wins purchase intent.** A real person with a real name/background cuts through in a way no carefully crafted problem framing can; omit the person and you "sound like everything else on the internet" (one respondent literally said the problem framing "sounds AI generated").
- **Desire ≠ willingness to pay** — generalized from a prior Kiwi.com extras study: travellers wanted high-value extras, but bundling them with a real price made the bundle feel expensive and conversion dropped.
- **The qualitative open-ends carried the insight**, not the means: person-framing reactions were personal/vivid; problem-framing reactions were polite-but-distant. One gave relevance 4/5 and intent 1/5.
- **Acted proportionally to the evidence:** didn't redesign the site off one underpowered study; instead changed behavior (started writing personal, process-revealing articles — "let people find out who's behind the service").

## Useful Examples

- The **person / method / problem** framing trichotomy as a reusable positioning-test design.
- The relevance(4/5) + intent(1/5) respondent as a one-line embodiment of the say-do gap.
- **Exemplary methodological honesty** (see caveats) — a model for reporting an underpowered study without overclaiming.

## Constraints / Caveats

- **Single self-study, underpowered:** n=30/cell; ANOVA on purchase intent significant (p=.034) but non-parametric Kruskal-Wallis not (p=.054); medium effect (Cohen's f=0.284). Her own note: "directional finding is clear but the inferential claim is not bulletproof."
- One product (her own consulting), senior-decision-maker sample (companies 50+) — transfer to other offers/audiences unproven.
- Self-interested context (positioning her own business), though the honesty is unusually high.

## Design Implications

- **Measure purchase intent, not just relevance/appeal**, when testing positioning or value props — appeal that doesn't convert is the classic trap (ties to [[concepts/agent-experience/satisfaction-vs-benefit|satisfaction ≠ benefit]] and the "looks good ≠ truly good" theme).
- For complex/expert services, **foreground the person** (named expertise, visible thinking) rather than only the abstracted problem.
- Read this as a worked example of [[concepts/ux-research/claim-based-sampling|claim-based sampling]] + honest small-N reporting: a detection-grade study reported as directional, not definitive.

## Tensions

- Against "sales 101" intuition (lead with the buyer's problem, hide your credentials) — the data inverted it here.
- Stated preference vs revealed behavior: surveyed *intent* is itself a stated measure — the deeper say-do gap (intent → actual contracting) remains untested.

## Open Questions

- Does person-framing's advantage hold for non-expert/commodity services, or only high-trust expert work?
- What would a properly powered (or behavioral/conversion) replication show? (MaxDiff results promised next in her series.)

## Concepts Linked

- [[concepts/ux-research/say-do-gap|Say-Do Gap]] (new)
- [[concepts/ux-research/validity-and-decision-relevance|Validity and Decision Relevance]]
- [[concepts/ux-research/self-reported-ux-metrics|Self-Reported UX Metrics]]
- [[concepts/agent-experience/satisfaction-vs-benefit|Satisfaction vs Benefit]]
- [[concepts/ux-research/synthetic-survey-data|Synthetic Survey Data]]
- [[concepts/ux-research/maxdiff-prioritization|MaxDiff Prioritization]]
- [[concepts/product-management/research-influence|Research Influence]]

## LLM Use

- **Use for:** designing positioning / value-prop tests that separate relevance from purchase intent; arguing the say-do and desire-vs-WTP gaps; a model of honest small-N reporting.
- **Do not use for:** treating the result as a powered/generalizable finding (it isn't); claiming person-framing wins universally.
- **Best prompt pattern:** "Design a between-subjects framing test that measures relevance AND purchase intent separately; pre-state the claim type and the N needed; flag where stated intent may diverge from actual behavior."

## Reliability Notes

> [!warning] Caveats
> - **Single underpowered self-study**, full text + methodology note captured. Confidence 0.8 on the *directional* insight and the framing-test design; low on any inferential/universal claim (author concurs).

## Backfill Status

- New 2026-06-22 from full web capture (incl. methodology note). All sections populated.
