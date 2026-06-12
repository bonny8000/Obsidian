---
type: method
status: active
created: 2026-06-12
updated: 2026-06-12
tags: [method, ux-research, interviews, qualitative]
sources:
  - sources/user-interviews-ai-assistant
  - sources/medium-harizlim-ai-qualitative-research-2026
  - sources/sage-10778004251401851-genai-reflexive-qualitative-research
confidence: 0.82
method_family: generative
best_for: motivations, workflows, needs, decision context, language
avoid_when: exact prevalence, benchmark metrics, or behavioral claims are required
outputs: themes, opportunity areas, journey evidence, quotes, research questions
---

# Method: Semi-Structured Interviews

## Purpose

Semi-structured interviews explore how participants describe their goals, constraints, workflows, meanings, and decision criteria while preserving enough structure to compare across sessions.

## Use When

- The team needs to understand why behavior happens.
- The product problem is ambiguous or early-stage.
- The study needs participant language, mental models, or workflow context.

## Avoid When

- The team needs statistically representative prevalence.
- The research question can be answered more directly with behavioral data.
- Interview data will be over-generalized without triangulation.

## Inputs

- Interview guide with required probes and optional follow-ups.
- Participant criteria and exclusion criteria.
- Consent and privacy handling.
- Analysis plan before LLM assistance is used.

## Procedure

1. Write a guide around decisions, not curiosity alone.
2. Run sessions with consistent core questions and flexible probes.
3. Capture verbatim evidence and context.
4. Code patterns, contradictions, and outliers.
5. Convert themes into opportunities only after checking source evidence.

## Outputs

- Theme map with supporting evidence.
- User language and mental models.
- Opportunity hypotheses.
- Follow-up research questions.

## Quality Bar

- Distinguish participant claim, researcher interpretation, and product implication.
- Preserve contradictions rather than smoothing them away.
- Do not let an LLM create quotes or infer missing context.

## LLM Assistance

- **Safe uses:** summarizing transcripts, proposing code candidates, comparing themes.
- **Risky uses:** replacing human interpretation, generating synthetic evidence, flattening minority views.
- **Verification required:** every theme must trace back to raw notes or source records.

## Related Concepts

- [[concepts/ux-research/genai-in-qualitative-research|GenAI in Qualitative Research]]
- [[concepts/ux-research/reflexive-thematic-analysis|Reflexive Thematic Analysis]]
- [[concepts/ux-research/methodological-integrity|Methodological Integrity]]
- [[concepts/ux-research/validity-and-decision-relevance|Validity and Decision Relevance]]

## Source Evidence

- [[sources/user-interviews-ai-assistant|User Interviews - AI Assistant]]
- [[sources/medium-harizlim-ai-qualitative-research-2026|AI Qualitative Research]]
- [[sources/sage-10778004251401851-genai-reflexive-qualitative-research|GenAI and Reflexive Qualitative Research]]

