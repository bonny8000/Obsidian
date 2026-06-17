---
source_url: https://measuringu.com/how-to-use-banner-tables-to-present-survey-results/
captured: 2026-06-17
title: How to Use Banner Tables to Present Survey Results
authors: [Jim Lewis, Jeff Sauro]
published: 2026-03-24
publisher: MeasuringU
---

# How to Use Banner Tables to Present Survey Results

**Authors:** Jim Lewis, PhD and Jeff Sauro, PhD
**Published:** 2026-03-24 — MeasuringU

## Overview

Banner tables present survey results across multiple demographic segments in a single, scannable view. They compress numerous cross-tabulations into one wide table format, making them particularly valuable for large-scale surveys with segmentation analysis.

## What are banner tables?

A banner table displays survey metrics in rows (called the **stub**) with demographic or behavioral segments arranged in columns (the **banner**). The format allows stakeholders to quickly compare results without flipping between multiple slides or charts.

## Historical context

The origins of banner tables trace back to mid-20th-century survey practices. The terminology "stub-and-banner" or "stub-and-boxhead" appears in the 1949 U.S. Census Bureau publication, *Bureau of the Census Manual of Tabular Presentation*. The format emerged alongside large-scale surveys to compress extensive cross-tabulations into manageable visual summaries.

## Usage in different research contexts

**Market research.** Core deliverable — shows every key question broken out by segments like demographics, usage patterns, brand preferences, geographic regions. Standardized because:

- Sample sizes typically support numerous data splits.
- The format is standardized and repeatable.
- It meets stakeholder needs for results sliced multiple ways.

**UX research.** Less commonly requested, but valuable in large-scale surveys focused on segmentation analysis. Typically a supporting deliverable, not the primary output.

## Weighted vs unweighted results

Banner tables display both weighted and unweighted results simultaneously, allowing researchers to assess weighting impacts. Market research typically treats weighted as official, while maintaining unweighted bases for quality control and transparency.

## Example study

The article demonstrates banner tables using data from a 2024 SUPR-Q survey of social media platforms. Researchers surveyed **324 participants in August 2024** about their experiences with six platforms: Facebook, Instagram, LinkedIn, Snapchat, TikTok, X.

**Metrics examined:**

- Brand attitude (seven-point scale, reported as top-two box %).
- Reluctance to share political content (five-point scale, reported as bottom-two box %).

**Demographic variables:**

- Gender (female, male, nonbinary).
- Age (18-24, 25-29, 30-39, 40-49, 50-59, 60-69).
- Income ($0-$24k, $25k-$49k, $50k-$99k, $100k-$149k, $150k-$199k, $200k+).

### Key findings

**Brand attitude (Top-2 Box):**

- TikTok highest at 50.9% (unweighted).
- Facebook 24.5% (unweighted).
- LinkedIn 23.1% (unweighted).
- Female users substantially higher brand attitudes than male.
- Age 50–59 highest brand attitude.
- Income $25k–$49k rated highest at 30% (unweighted).

**Political discourse reluctance (Bottom-2 Box):**

- LinkedIn users most reluctant at 94.2% (unweighted).
- Nonbinary users least likely to engage in political discourse.
- Age 18–24 showed 80.9% reluctance (unweighted).
- Income $200k+ showed 87.5% reluctance (unweighted).

## Creating banner tables

**R packages used:**

- `openxlsx` — data import and formatted Excel output.
- `dplyr` — data frame manipulation.
- `tidyr` — tidy data format creation.

The article includes an R script (available as a PDF download) for the complete process for creating banner tables with both weighted and unweighted results.

## Key advantages

Banner tables:

- Compress many crosstabs into one viewable table.
- Work with common analysis tools including R and AI.
- Serve as ideal deliverables for large surveys with segmentation analysis.
- Facilitate easy comparison of weighted vs unweighted results.
- Enable stakeholders to quickly identify patterns across multiple segments.

## Best practices

1. **Freeze panes.** Lock the top row and left columns to support horizontal scrolling through demographic segments.
2. **Include sample sizes.** Display both unweighted n and weighted n.
3. **Use visual separation.** Empty columns with light color fill can separate different demographic variable sections.
4. **Provide context.** Include metric definitions to clarify whether larger percentages reflect positive (top-box) or negative (bottom-box) outcomes.

## When to use banner tables

Most appropriate for:

- Large-scale surveys with sample sizes supporting multiple data splits.
- Research requiring cross-tabulation by multiple demographic or behavioral segments.
- Stakeholders needing standardized, repeatable result formats.
- Side-by-side comparison of metrics across segments.

Less appropriate for:

- Small sample surveys where data splits produce unreliable estimates.
- Qualitative research or small-scale studies.
- Situations where visual charts better communicate findings.

## Summary

"Banner tables compress many crosstabs into one scannable view," providing efficient survey result summaries across multiple segments. While common in market research, they remain underutilized in UX research despite offering clear value for large-scale segmentation studies. Modern analysis tools, including AI and R packages, simplify creation of these professional deliverables.
