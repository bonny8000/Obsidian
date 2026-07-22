---
type: concept
status: active
created: 2026-07-22
updated: 2026-07-22
tags: [concept, ux-research, methodology]
sources:
  - wiki/sources/ai-powered-ux-research
confidence: 0.95
---

# Micro Research

## Summary
Micro Research is the fastest operating mode in the [[wiki/concepts/ux-research/the-research-engine|Research Engine]], designed to deliver directional findings in 24 to 72 hours. It relies entirely on AI-moderated asynchronous data collection with real participants, lacking human follow-up sessions. 

## Why It Matters
Product teams make dozens of micro-decisions every sprint (copy tweaks, layout choices, comprehension checks). Traditional research cannot scale to cover these. Micro Research provides a structured, rigorous way to inject user evidence into these fast decisions rather than relying on internal opinion or raw analytics.

## Key Claims
- **Scope**: Used for low-risk, low-ambiguity, short-expiry questions. Typical use cases: comprehension checks, friction identification, preference selection, terminology validation.
- **Methodology**: 8 to 15 participants engaging with specific, concrete artifacts via text, audio, or video prompts moderated by AI. No researcher-led follow-ups.
- **Question Hygiene**: Requires strict scoping using a **[[wiki/concepts/ux-research/decision-contract|Decision Contract]]**. If the question is vague ("do users like this?"), it will fail.
- **First-Three-Participant Audit**: The researcher must manually review the first three raw transcripts to catch bad prompt design or AI hallucination/leading before collecting the rest of the sample.
- **Deliverable**: A **Directional Readout**. Short, concise, stating observations (not recommendations), explicit boundaries on what the data *cannot* support, and an expiry condition for the findings.
- **Quality Gates**: Every finding must have a traceable evidence chain to a participant quote, and synthesis must explicitly include disconfirming evidence.

## Related Concepts
- [[wiki/concepts/ux-research/the-research-engine|The Research Engine]]
- [[wiki/concepts/ux-research/decision-contract|Decision Contract]]
- [[wiki/concepts/ux-research/directional-readout|Directional Readout]]
- [[wiki/concepts/ux-research/sprint-research|Sprint Research]]

## Sources
- [[wiki/sources/ai-powered-ux-research|AI-Powered UX Research (Papas, 2026)]]
