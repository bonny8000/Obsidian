# Source Card: MeasuringU - Does AI Find Real UI Problems or Just Hallucinations?

URL: https://measuringu.com/does-ai-find-real-ui-problems-or-just-hallucinations/

Retrieved: 2026-06-10

Source type: UX research article

Publisher: MeasuringU

Authors: Jim Lewis, Jeff Sauro, Will Schiavone, Lucas Plabst

Published: 2026-05-26

Title: Does AI Find Real UI Problems or Just Hallucinations?

Extractor notes:

- Defuddle succeeded locally on 2026-06-10.
- Word count reported by extractor: 1743.
- This raw card records metadata, extracted numbers, and an AI-written summary rather than reproducing the full article text.

## Summary

The article follows MeasuringU's earlier reliability study on AI analysis of a usability-test video. Four professional UX researchers reviewed a six-minute video from an online dining reservation benchmark. Two LLMs, ChatGPT-5.4 Thinking and Gemini 3 Flash Thinking, reviewed the same video four times with the same prompt.

The new question was whether AI-only usability problems were genuine misses by human researchers, false alarms, or hallucinations. The study found one genuine AI-only usability issue, seven false alarms, and three hallucinations among the eleven AI-only issues.

## Extracted Data

| Measure | Reported value |
| --- | --- |
| Human researchers | 4 professional UX researchers |
| Video length | 6 minutes |
| AI systems | ChatGPT-5.4 Thinking; Gemini 3 Flash Thinking |
| Runs per AI system | 4 |
| Human-identified problems | 9 |
| AI-identified problems, combined | 14 |
| Problems found by humans and both AIs | 3 |
| ChatGPT matches against human list | 5 of 9 |
| Gemini matches against human list | 4 of 9 |
| AI-only problems | 11 |
| AI-only problems unique to ChatGPT | 6 |
| AI-only problems unique to Gemini | 4 |
| AI-only problem found by both AIs | 1 |
| AI-only genuine finds | 1 of 11, 9% |
| AI-only false alarms | 7 of 11, 64% |
| AI-only hallucinations | 3 of 11, 27% |

## Problem Classifications Captured

| Problem code | Short description | AI source | Classification |
| --- | --- | --- | --- |
| 4b | Vague claim that filters were not helpful | ChatGPT | False alarm |
| 5b | Participant used browser find to search for sushi in the expanded cuisine list | Gemini | Genuine find |
| 6b | Search results for sushi included restaurants not labeled sushi | ChatGPT | False alarm |
| 6c | Cuisine information was weak in search results | ChatGPT | False alarm |
| 7b-Gem | Claimed participant chose the highest price tier | Gemini | Hallucination |
| 7b-GPT | Sorting by highest rated surfaced non-sushi restaurants | ChatGPT | False alarm |
| 8b | UI pushed browsing without decision support | ChatGPT | False alarm |
| 9b | Seating options appeared only after selecting time | Gemini | False alarm |
| 9c | Claimed participant selected 5:10 instead of 5:00 | Gemini | Hallucination |
| 10a | Restaurant was labeled seafood rather than sushi | Both | False alarm |
| 10b | Claimed participant never reached the reservation step | ChatGPT | Hallucination |

## Extracted Claims

- AI can surface genuine usability problems that human reviewers miss, but AI-only issues require verification.
- In this study, most AI-only usability issues were either false alarms or hallucinations.
- False alarms can come from literal interpretation of task wording rather than pragmatic interpretation of participant success.
- Hallucinations were fewer than false alarms but still consequential because they cannot be detected without returning to the original video evidence.
- Multiple AI runs may help identify consistency patterns, but consistency still needs human review and validity checks.
- AI usability analysis is best treated as junior-researcher assistance, not as trusted expert judgment.

## Potential Wiki Concepts

- AI usability false-alarm triage
- AI usability analysis
- Reliability vs validity
- Evaluator effect
- Validity and decision relevance

## Verification Notes

- Primary source for this specific small study.
- The experiment used one video, one prompt setup, and two LLMs; conclusions should be treated as directional rather than general.
- The article builds directly on MeasuringU's earlier reliability article already captured in the wiki.

Copyright note: this card records metadata, data points, and a paraphrased summary, not a full copy of the article.
