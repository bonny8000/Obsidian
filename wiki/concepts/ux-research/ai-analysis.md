---
type: concept
status: active
created: 2026-06-03
updated: 2026-07-28
tags: [ux-research, ai, analysis]
sources:
  - sources/user-interviews-ai-assistant
  - sources/nngroup-accelerating-research-with-ai
confidence: 0.9
---

# AI Analysis

## Summary

AI Analysis in the context of UX Research involves using AI models to process raw qualitative data (transcripts, recordings, notes) into structured insights, themes, and citations.

## Why It Matters

Qualitative analysis is traditionally labor-intensive. AI can accelerate the time-to-insight by providing instant summaries, searchable grounded transcripts, and cross-session comparisons.

## Key Claims

- **Grounded Exploration:** AI chat tools can answer questions about research data with direct citations to the source transcript or video.
- **Session Breakdowns:** Automated extraction of key observations and metadata from individual sessions.
- **Comparative Analysis:** Tools like data grids allow for side-by-side comparison of participant responses across sessions.

## Bounds on the delegable band

[[wiki/sources/nngroup-accelerating-research-with-ai|NN/g (Moran & Rosala)]] endorse AI in the analysis stage while marking its limits precisely:

- **Endorsed:** transcription and translation with timestamped linking, session summarization, PII sanitization, preliminary coding, descriptive statistics and missing-data handling.
- **Initial pass only.** AI-generated codes "often miss large sections or produce shallow groupings around keywords." A human must synthesize codes into insight.
- **Context blindness is the hard limit.** AI cannot ask how a statement contrasts with the participant's other statements, or whether the interviewer accidentally primed them — the contextual reasoning that thematic analysis depends on.
- **Stochasticity is a design constraint, not a prompting problem:** "AI is stochastic — it can choose to pay attention to certain things but disregard others," which may mean attending to the wrong parts of the data.
- **The underlying mechanism:** AI performs better on attitudinal / self-reported data than on behavioral data **because that data is language-based.** This single fact predicts what works across the whole research lifecycle better than any per-tool judgment.
- **Verification is not optional:** double-check transcriptions especially with multiple speakers, supply research goals as context, and spot-check quantitative output.

Note the net-gain caution: faster transcription plus mandatory multi-speaker verification is a smaller improvement than it first appears.

## Related Concepts

- [[concepts/ux-research/ux-research-automation|UX Research Automation]]
- [[concepts/ux-research/reflexive-thematic-analysis|Reflexive Thematic Analysis]]
- [[concepts/ux-research/human-interpretation|Human Interpretation]]
- [[concepts/ux-research/genai-in-qualitative-research|GenAI in Qualitative Research]]
- [[wiki/concepts/ux-research/ai-usability-analysis|AI Usability Analysis]] — where the behavioral-data limit bites hardest.
- [[wiki/concepts/ux-research/validity-and-decision-relevance|Validity and Decision Relevance]]

## Sources

- [[sources/user-interviews-ai-assistant|User Interviews AI Assistant]] — provides AI chat, session breakdowns, and grounded insights.
- [[wiki/sources/nngroup-accelerating-research-with-ai|NN/g (2024, reviewed 2026): Accelerating Research with AI]] — the stage-by-stage bounds, the language-vs-behavior mechanism, and the verification guardrails.

## Open Questions

- How do we maintain "grounding" and prevent AI hallucinations during qualitative synthesis?
- What is the best balance between AI speed and human-led thematic deep-dives?
- Is there a published comparison of AI-generated versus human qualitative codes with an agreement metric? This wiki has none, and it is the load-bearing question under "initial pass only."
- Does the language-vs-behavior limit hold for multimodal models, or was it an artifact of text-only pipelines?
