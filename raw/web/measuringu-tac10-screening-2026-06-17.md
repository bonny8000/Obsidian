---
source_url: https://measuringu.com/using-the-tac10-for-screening-and-data-cleaning/
captured: 2026-06-17
title: Using the TAC-10 for Screening and Data Cleaning
authors: [Jim Lewis, Jeff Sauro]
published: 2026-06-02
publisher: MeasuringU
---

# Using the TAC-10 for Screening and Data Cleaning

**Authors:** Jim Lewis, PhD and Jeff Sauro, PhD
**Published:** 2026-06-02 — MeasuringU

## Introduction

"It's hard to collect data for UX research, and once you have it, you have to clean it." Research estimates approximately 10% of respondents on paid panels engage in cheating, ranging from 3–20%.

## Screening and cleaning strategies

Multiple approaches exist for identifying problematic respondents:

- Identification of speeders
- Disqualifying questions
- Attention checks
- Review of open-ended responses
- Internal consistency checks
- Straightlining detection
- Session recording review
- Duplicate and bot detection

AI complicates these detection methods, though panel operators have implemented safeguards against AI fraud.

## TAC-10 basics

The TAC-10 (Technical Activity Checklist with 10 items) emerged from eight years of research into measuring tech savviness. After analyzing thousands of participants, researchers determined that technical activity checklists outperformed quizzes and questionnaires for measuring tech competence.

The TAC-10 measures confidence performing ten technical activities, scored by counting selected items. It serves two purposes: classifying participants into low / medium / high tech savviness groups and functioning as a predictive variable in statistical analysis.

## Response pattern analysis

The researchers analyzed 4,731 TAC-16 responses to examine TAC-10 patterns for data cleaning purposes. Of 1,024 theoretically possible response patterns, only 199 appeared in the dataset.

### Guttman scaling patterns

Guttman scaling represents deterministic patterns where selected items progress consistently from easiest to most difficult activities. "Only 11, however, are consistent with a perfect Guttman scale (all 1s toward the left side of the pattern, all 0s to the right)."

**Perfect Guttman patterns accounted for 56.4% of cases.**

| Pattern | Frequency | Percent |
| --- | --- | --- |
| 1111111111 | 365 | 7.7% |
| 1111111110 | 633 | 13.4% |
| 1111111100 | 764 | 16.1% |
| 1111111000 | 474 | 10.0% |
| 1111110000 | 268 | 5.7% |
| 1111100000 | 104 | 2.2% |
| 1111000000 | 27 | 0.6% |
| 1110000000 | 20 | 0.4% |
| 1100000000 | 9 | 0.2% |
| 1000000000 | 5 | 0.1% |
| 0000000000 | 0 | 0.0% |
| **Total** | **2,669** | **56.4%** |

### Other plausible patterns

Twenty-one high-frequency plausible patterns accounted for 30.7% of cases. Example: someone comfortable with all activities except HTML produces 1111111101. "Although it's unlikely that someone who programs efficiently in C knows nothing about HTML, it's possible."

### Implausible patterns

The database contained **no inverse Guttman patterns**. Seventeen implausible patterns starting with "01" (comfort with one activity despite discomfort with easier prerequisites) appeared in only 21 cases (0.4%). Four additional cases (0.1%) selected single activities inconsistently with the item hierarchy.

### Indeterminate patterns

Remaining patterns lacking clear plausibility or implausibility markers were 12.4% of responses, none exceeding 0.4% individually.

## Key findings

1. **Plausible patterns dominated:** 87% of TAC-10 responses matched Guttman or near-Guttman patterns — suggesting respondent attentiveness despite randomized item presentation.
2. **Implausible patterns proved rare:** No inverse Guttman patterns occurred; problematic patterns < 0.5% of responses.
3. **Screening application value:** TAC-10 response patterns provide useful screening capability alongside open-ended response review, completion time analysis, multiple-choice distractors, attention checks, and straightlining detection.

## Limitations regarding AI fraud

Sophisticated AI systems can convincingly mimic either low- or high-skill respondents by training on published TAC-10 research. "However, the TAC-10 remains a valuable screening tool in contexts where respondents come from a known population, such as a customer list, or where other panel-level methods have already confirmed that participants are human."

The TAC-10 functions most effectively in verified human populations rather than as a standalone AI detection mechanism.
