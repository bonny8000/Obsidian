---
type: source
status: active
created: 2026-06-17
updated: 2026-06-17
tags: [source, ux-research, surveys, banner-table, cross-tabulation, segmentation, market-research, reporting]
source_path: raw/web/measuringu-banner-tables-2026-06-17.md
source_url: https://measuringu.com/how-to-use-banner-tables-to-present-survey-results/
authors: [Jim Lewis, Jeff Sauro]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.88
---

# MeasuringU: How to Use Banner Tables to Present Survey Results

**Authors:** Jim Lewis, PhD and Jeff Sauro, PhD
**Published:** 2026-03-24 — MeasuringU
**Raw capture:** [[raw/web/measuringu-banner-tables-2026-06-17|measuringu-banner-tables-2026-06-17]]
**URL:** [measuringu.com/how-to-use-banner-tables-to-present-survey-results/](https://measuringu.com/how-to-use-banner-tables-to-present-survey-results/)

## Citation

Lewis, J., & Sauro, J. (2026, March 24). *How to use banner tables to present survey results.* MeasuringU.

## Summary

Banner tables (a.k.a. stub-and-banner, stub-and-boxhead) are the standard market-research format for compressing many cross-tabulations into a single scannable wide table — metrics in rows (the **stub**), demographic / behavioral segments in columns (the **banner**). They are a market-research staple but underused in UX research. They earn their keep when sample sizes support multiple data splits and stakeholders need standardized, repeatable side-by-side comparison. The article shows the format on a 2024 SUPR-Q social-media study (n = 324) and provides best practices (freeze panes, include weighted and unweighted n, visual separation between banner groups, define top/bottom box explicitly). R packages: `openxlsx`, `dplyr`, `tidyr`.

## Key Claims

- A banner table has metrics in rows (the **stub**) and segments in columns (the **banner**) — terminology traces to the 1949 U.S. Census Bureau *Manual of Tabular Presentation*.
- Banner tables compress many crosstabs into one viewable wide table — they are the standard market-research deliverable for segmented results.
- They are **underused in UX research** but become valuable when:
  - Sample sizes support numerous data splits.
  - Stakeholders need standardized, repeatable formats.
  - Segmentation by demographics or behavior is decision-relevant.
- **Weighted and unweighted results should appear side by side.** Market research treats weighted as official; unweighted is kept for quality control and transparency.
- The 2024 SUPR-Q social-media study (n = 324, August 2024) covered Facebook, Instagram, LinkedIn, Snapchat, TikTok, X, with:
  - Brand attitude (7-pt scale, reported as top-2 box %).
  - Reluctance to share political content (5-pt scale, reported as bottom-2 box %).
  - Banner: gender, age (6 bins), income (6 bins).
- **Headline findings from the example study:**
  - Brand attitude: TikTok 50.9% top-2 box (highest); Facebook 24.5%; LinkedIn 23.1%. Female > male. Age 50–59 highest. Income $25k–$49k highest at 30%.
  - Political reluctance: LinkedIn 94.2% bottom-2 box (highest reluctance). Nonbinary least likely to engage. Age 18–24: 80.9% reluctance. Income $200k+: 87.5% reluctance.

## Best Practices (with rationale)

1. **Freeze panes.** Lock top row and left columns so horizontal scrolling across banner segments stays oriented.
2. **Include sample sizes.** Both unweighted *n* and weighted *n* — without them, the cells lie.
3. **Visual separation between banner groups.** Empty columns with light fill — readers parse the structure faster.
4. **Define metric direction.** Make explicit whether a larger % is positive (top-box) or negative (bottom-box).

## When to use / avoid

| Use when | Avoid when |
| --- | --- |
| Large-scale surveys with sample sizes supporting multiple data splits | Small-sample surveys where splits produce unreliable estimates |
| Multiple demographic or behavioral segments are decision-relevant | Qualitative research or small-scale studies |
| Stakeholders need standardized, repeatable result formats | Visual charts communicate the finding better |
| Side-by-side metric comparison across segments adds value | A single-metric deliverable is enough |

## Useful Examples

- The SUPR-Q social-media banner-table study as a concrete UX use case for the format.
- The brand-attitude vs political-reluctance metric pair as a clean top-box / bottom-box demonstration.
- The R-package stack (`openxlsx`, `dplyr`, `tidyr`) for generating banner tables with both weighted and unweighted columns.

## Constraints / Caveats

- Banner tables require *enough* sample to make subgroup splits meaningful. With n = 324 split across 6 platforms × 3–6 demographic bins, some cells already have very small n. The article doesn't enforce a per-cell minimum.
- The article doesn't address how AI tools should *consume* banner tables in agentic research workflows — only how to *produce* them.
- "Market research treats weighted as official" is a convention, not a rule. UX teams must decide which they trust.
- The R script is referenced via PDF download — not embedded in-article.

## Design Implications

- **For UX teams running large segmentation surveys:** banner tables should be a standard supporting deliverable, not optional. Encode the format in the report template.
- **For analysis pipelines:** a banner-table generator is a strong candidate for an Agent Skill (see [[concepts/ai-agents/agent-skills|Agent Skills]]) — deterministic R/Python work, repeated across studies, with clear input (raw survey data) and output (formatted Excel).
- **For dashboards:** any survey dashboard that exposes only one cut of the data is leaving money on the table — provide a banner view by default.
- **For stakeholder review:** banner tables encourage segment-level questions ("why is LinkedIn so high on political reluctance?") that single-number summaries hide. This is feature, not bug.
- **For Bonny's bilingual survey work:** banner tables surface language / locale segmentation differences explicitly — useful when localizing UX metrics across markets.

## Tensions

- **Comprehensiveness vs noise.** A banner with 20 segments shows everything *and* hides the signal in clutter. The format rewards careful segment selection.
- **Standardization vs custom visualizations.** Market research loves standardization; UX research often prefers tailored visuals. Banner tables are the conservative deliverable; charts are the persuasive one. Use both.
- **Weighted vs unweighted reporting.** When the headline number is weighted and the cell-level number is unweighted, readers can misread. Best practice: label every cell.

## Open Questions

- For Bonny's vault: should every large-survey ingest also produce a banner-table export by default?
- What is the right per-cell minimum *n* before a banner cell should be reported (vs masked)?
- Is there a clean agentic / AI workflow that consumes a banner table and surfaces the 3 most decision-relevant segments? (Candidate Skill.)
- How should AI moderators interpret banner-table results when generating follow-up qualitative interview guides?

## Concepts Linked

- [[concepts/ux-research/banner-table|Banner Table]] (new)
- [[concepts/ux-research/standardized-usability-questionnaires|Standardized Usability Questionnaires]]
- [[concepts/ux-research/self-reported-ux-metrics|Self-Reported UX Metrics]]
- [[concepts/ux-research/quant-uxr-rigor|Quant UXR Rigor]]
- [[concepts/ux-research/participant-selection-criteria|Participant Selection Criteria]]
- [[concepts/ai-agents/agent-skills|Agent Skills]] — banner-table generator as Skill candidate.

## LLM Use

- **Use for:** designing banner-table deliverables for large segmentation surveys, writing analysis Skills that produce them, training stakeholders on stub-banner terminology, designing dashboards that expose weighted + unweighted segment views.
- **Do not use for:** small-sample qualitative work, single-metric reporting where a chart is clearer, claims about weighted-vs-unweighted authority (it's a team convention).
- **Best prompt pattern:** "Given this survey dataset (n, columns, weighting), produce a banner table with the named metrics as the stub and these demographic / behavioral cuts as the banner. Include weighted and unweighted *n*, freeze panes guidance, top/bottom-box definitions in the header. Flag any cell with weighted n < 30."

## Reliability Notes

> [!warning] Caveats
> - **Single example study.** The SUPR-Q social-media findings are illustrative, not benchmarks.
> - **No per-cell n threshold** is enforced in the article — readers must decide.
> - **Confidence:** 0.95 on the format definition and best practices (well-established market-research practice); 0.85 on UX-specific recommendations; 0.7 on the example study's headline findings (single study, August 2024).

## Backfill Status

- New 2026-06-17. Full sections populated.
