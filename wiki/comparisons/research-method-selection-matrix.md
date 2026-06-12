---
type: comparison
status: active
created: 2026-06-12
updated: 2026-06-12
tags: [comparison, ux-research, method-selection]
sources:
  - sources/conjointly-research-methods-kb
  - sources/tullis-albert-measuring-ux-2013
  - sources/sauro-lewis-quantifying-ux-2016
  - sources/sage-10778004251401851-genai-reflexive-qualitative-research
confidence: 0.84
---

# Comparison: Research Method Selection Matrix

## Decision Question

Which UX research method should be used for a specific product decision?

## Criteria

- Decision type: discover, evaluate, measure, prioritize, or synthesize.
- Evidence type: behavior, attitude, preference, interpretation, or operational knowledge.
- Product maturity: undefined problem, concept, prototype, shipped product, or mature service.
- Risk level: low-stakes exploration vs decision-critical evidence.
- LLM suitability: whether AI can assist safely without creating unsupported evidence.

## Matrix

| Method | Best for | Weakness | Evidence needed | LLM risk |
| --- | --- | --- | --- | --- |
| [[methods/semi-structured-interviews|Semi-Structured Interviews]] | motivations, workflows, needs, language | weak prevalence and measurement | recordings, notes, quotes, recruitment criteria | summarization may flatten nuance |
| [[methods/usability-testing|Usability Testing]] | task friction, interface issues, learnability | not a market-demand test | tasks, observations, issue evidence, severity rubric | false positives and invented root causes |
| [[methods/surveys-and-standardized-metrics|Surveys and Standardized Metrics]] | tracking attitudes, benchmarks, perceived usability | self-report limits and sampling bias | questionnaire, sample frame, confidence intervals | overclaiming statistical meaning |
| [[methods/maxdiff-prioritization|MaxDiff Prioritization]] | relative priority among items | item wording can dominate results | stable item set, balanced design, sample plan | creating weak or overlapping item lists |
| [[methods/reflexive-thematic-analysis|Reflexive Thematic Analysis]] | meaning, nuance, contradictions | not mechanical or frequency-first | transcripts, coding, memoing, reflexive notes | replacing researcher interpretation |
| [[methods/ai-assisted-research-synthesis|AI-Assisted Research Synthesis]] | scaling summary and comparison across evidence | unreliable without raw evidence | source records, claim table, verification checklist | hallucination and unsupported themes |

## Recommendation Pattern

- If the question is "Can users complete this flow?", start with [[methods/usability-testing|Usability Testing]].
- If the question is "Why do users behave this way?", start with [[methods/semi-structured-interviews|Semi-Structured Interviews]].
- If the question is "How much or how many?", start with [[methods/surveys-and-standardized-metrics|Surveys and Standardized Metrics]].
- If the question is "Which of these matters most?", start with [[methods/maxdiff-prioritization|MaxDiff Prioritization]].
- If the question is "What does this qualitative material mean?", start with [[methods/reflexive-thematic-analysis|Reflexive Thematic Analysis]].
- If the question is "What do many sources collectively suggest?", use [[methods/ai-assisted-research-synthesis|AI-Assisted Research Synthesis]] with strict source verification.

## Source Evidence

- [[sources/conjointly-research-methods-kb|Conjointly Research Methods Knowledge Base]]
- [[sources/tullis-albert-measuring-ux-2013|Tullis and Albert - Measuring UX]]
- [[sources/sauro-lewis-quantifying-ux-2016|Sauro and Lewis - Quantifying UX]]
- [[sources/sage-10778004251401851-genai-reflexive-qualitative-research|GenAI and Reflexive Qualitative Research]]

