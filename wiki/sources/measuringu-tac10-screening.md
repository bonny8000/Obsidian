---
type: source
status: active
created: 2026-06-17
updated: 2026-06-17
tags: [source, ux-research, data-quality, screening, tac-10, tech-savviness, survey-cleaning, ai-fraud]
source_path: raw/web/measuringu-tac10-screening-2026-06-17.md
source_url: https://measuringu.com/using-the-tac10-for-screening-and-data-cleaning/
authors: [Jim Lewis, Jeff Sauro]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.88
---

# MeasuringU: Using the TAC-10 for Screening and Data Cleaning

**Authors:** Jim Lewis, PhD and Jeff Sauro, PhD
**Published:** 2026-06-02 — MeasuringU
**Raw capture:** [[raw/web/measuringu-tac10-screening-2026-06-17|measuringu-tac10-screening-2026-06-17]]
**URL:** [measuringu.com/using-the-tac10-for-screening-and-data-cleaning/](https://measuringu.com/using-the-tac10-for-screening-and-data-cleaning/)

## Citation

Lewis, J., & Sauro, J. (2026, June 2). *Using the TAC-10 for screening and data cleaning.* MeasuringU.

## Summary

The TAC-10 (Technical Activity Checklist with 10 items) is a tech-savviness measure that doubles as a survey data-cleaning instrument. Because tech activities form a near-Guttman hierarchy (easy → hard), the *response pattern* — not just the score — flags inattentive or fraudulent respondents. In an analysis of 4,731 TAC-16 responses, **87% of TAC-10 patterns matched Guttman or near-Guttman patterns** and only **< 0.5% were implausible** (no inverse-Guttman patterns at all). The TAC-10 is most useful as one screening method *alongside* speeders detection, attention checks, straightlining detection, and open-ended review — not as a standalone AI-fraud filter, because sophisticated LLMs can mimic plausible patterns.

## Key Claims

- About **10% of paid-panel respondents engage in cheating** (range 3–20%). Survey researchers need multiple screening methods.
- Standard screening / cleaning checklist: speeders, disqualifying questions, attention checks, open-ended review, internal consistency, straightlining, session recording review, duplicate / bot detection.
- The TAC-10 measures confidence performing 10 technical activities — scored by counting selected items — and emerged from **eight years of research** showing **technical activity checklists outperform quizzes and questionnaires** for measuring tech competence.
- Of **1,024 theoretically possible response patterns**, only **199 appeared** in the 4,731-response dataset.
- **Only 11 patterns are consistent with a perfect Guttman scale** (all 1s left, all 0s right). Perfect Guttman patterns account for **56.4%** of responses.
- **21 high-frequency plausible non-Guttman patterns** (one or two deviations, e.g. comfortable with everything except HTML → `1111111101`) account for another **30.7%** of cases.
- **No inverse Guttman patterns** in the database. Implausible patterns (selecting hard activities but not easier prerequisites) appeared in only **0.4%** of cases; another 0.1% selected single inconsistent activities.
- TAC-10 has two roles: (1) classifying participants into low / medium / high tech savviness and (2) acting as a predictive variable in statistical analysis.
- **Limitation regarding AI fraud:** "Sophisticated AI systems can convincingly mimic either low- or high-skill respondents by training on published TAC-10 research." TAC-10 is "valuable in contexts where respondents come from a known population, such as a customer list, or where other panel-level methods have already confirmed that participants are human."

## Useful Examples

- The Guttman pattern frequency table — pattern `1111111100` is the most common single pattern at 16.1%.
- The plausible-deviation example: `1111111101` (skilled developer who happens not to know HTML).
- The implausible pattern signature: any pattern starting `01…` (claims one activity but not its easier prerequisite).
- The 87% / < 0.5% framing as a quick benchmark for "how often do attention failures show up in a well-designed checklist screener."

## Constraints / Caveats

- Single dataset (4,731 TAC-16 responses re-analyzed for the 10-item subset). External replication outside MeasuringU's database not shown.
- The 87% plausible / 0.4% implausible split assumes Guttman-scaled items. For non-Guttman checklists, this pattern analysis does not apply.
- The TAC-10 is itself a published instrument — adversaries with LLM tools can train on it to produce plausible patterns. The authors are explicit that it is not a standalone fraud filter.
- No comparison shown against the other screening methods listed (speeders, straightlining). The TAC-10 is offered as a complement, not a replacement.

## Design Implications

- For Bonny's survey workflows: add a TAC-10 (or domain analog) when respondent tech savviness is decision-relevant *and* the population is verified human. Use it as one signal in a stack, not as the only check.
- For panel-based studies: pair TAC-10 with at least three other signals from the screening checklist (speeders, straightlining, open-ended review, attention checks).
- For ResearchOps automation: encode "pattern plausibility" as an automated cleaning rule. Inverse Guttman and `01…` starts are near-zero in real data; treat them as automatic discards.
- For AI-fraud-resistant survey design: prefer signals that require *behavior* the LLM can't easily simulate (timing variance, response trajectory) over signals that depend on *content*.
- Banner-table consumers (see [[sources/measuringu-banner-tables|banner tables source]]): when reporting tech-savviness banners, report unweighted screened-only data.

## Tensions

- **Screening rigor vs participant friction.** Stacking screening signals lowers fraud but also annoys legitimate participants. The authors don't quantify the tradeoff; they leave it as an engineering call.
- **TAC-10 as a tech-savviness measure vs as a screener.** Optimizing the items for *measurement* (capture savviness signal) and optimizing for *screening* (detect fraud) can pull in different directions if AI fraud grows.

## Open Questions

- What is the right base rate of TAC-10 plausibility in *Bonny's own* customer-list populations vs paid panels?
- Can a Bonny-specific activity checklist (Chinese-language tech context) replace TAC-10 for relevant audiences?
- For agent-augmented surveys, does the response-pattern check still hold, or do agents reshape the pattern space?

## Concepts Linked

- [[concepts/ux-research/tac-10-tech-savviness|TAC-10 Tech Savviness]] (new)
- [[concepts/ux-research/survey-data-quality-screening|Survey Data Quality Screening]] (new)
- [[concepts/ux-research/participant-selection-criteria|Participant Selection Criteria]]
- [[concepts/ux-research/quant-uxr-rigor|Quant UXR Rigor]]
- [[concepts/ux-research/reliability-vs-validity|Reliability vs Validity]]

## LLM Use

- **Use for:** designing screening / cleaning checklists for panel-based UX surveys, justifying TAC-10 as one signal in a screening stack, choosing automated cleaning rules (inverse Guttman / `01…` discards).
- **Do not use for:** standalone AI-fraud detection, generalizing pattern frequencies outside the TAC-16 dataset, or claiming TAC-10 is the only tech-savviness measure that works (it just outperforms quizzes / questionnaires per the cited 8-year research).
- **Best prompt pattern:** "Using Lewis & Sauro's TAC-10 screening framing, audit this survey's data-cleaning pipeline against the 8-method checklist and propose which signals are missing for the population at hand (verified human vs paid panel)."

## Reliability Notes

> [!warning] Caveats
> - **Single dataset.** Treat the 87% / 0.4% pattern figures as MeasuringU's database baseline, not a universal benchmark.
> - **Not AI-fraud-proof.** Authors are explicit. Pair with behavioral/timing signals when LLM fraud is a concern.
> - **Confidence:** 0.9 on the methodological framing; 0.85 on Guttman-pattern interpretation; 0.7 on generalization of pattern frequencies to other populations.

## Backfill Status

- New 2026-06-17. Full sections populated.
