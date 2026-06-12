---
type: method
status: active
created: 2026-06-12
updated: 2026-06-12
tags: [method, ux-research, ai-assisted-research, synthesis]
sources:
  - sources/how-to-ai-uxr-2026
  - sources/measuringu-ai-real-ui-problems-hallucinations
  - sources/research-that-scales-towsey-2024
  - sources/user-interviews-ai-assistant
confidence: 0.82
method_family: synthesis
best_for: summarizing evidence, clustering findings, drafting research memos, scaling review
avoid_when: raw evidence is missing or the team cannot verify AI outputs
outputs: synthesis memo, finding clusters, evidence table, risk notes
---

# Method: AI-Assisted Research Synthesis

## Purpose

AI-assisted synthesis uses LLMs to accelerate summarization, clustering, comparison, and drafting while preserving human accountability for evidence quality, interpretation, and decisions.

## Use When

- Raw notes, transcripts, or source records are preserved.
- The team needs faster synthesis across many evidence items.
- A human researcher can verify outputs against source material.

## Avoid When

- The model would be asked to infer missing evidence.
- The output will be used externally without verification.
- The team cannot separate source facts from model-generated interpretation.

## Inputs

- Source records with `raw_preserved: true`.
- Research question and synthesis frame.
- Evidence table or note set.
- Verification checklist.

## Procedure

1. Select only relevant source records.
2. Ask the LLM to extract claims with source links.
3. Cluster claims and preserve dissenting evidence.
4. Review clusters against raw or source notes.
5. Draft analysis with reliability notes and open questions.

## Outputs

- Finding clusters.
- Evidence-linked analysis memo.
- Risks, caveats, and contradictions.
- Next research actions.

## Quality Bar

- Every finding must trace to a source record.
- Treat generated themes as candidates until verified.
- Track unsupported claims explicitly.

## LLM Assistance

- **Safe uses:** summarization, clustering, contradiction search, memo drafting.
- **Risky uses:** replacing participant data, inventing examples, making unsupported decisions.
- **Verification required:** claims, quotes, source attribution, severity, and recommendation strength.

## Related Concepts

- [[concepts/ux-research/ux-research-automation|UX Research Automation]]
- [[concepts/ux-research/ai-analysis|AI Analysis]]
- [[concepts/ux-research/human-interpretation|Human Interpretation]]
- [[concepts/ux-research/validity-and-decision-relevance|Validity and Decision Relevance]]

## Source Evidence

- [[sources/how-to-ai-uxr-2026|How to AI UXR]]
- [[sources/measuringu-ai-real-ui-problems-hallucinations|MeasuringU - AI Real UI Problems and Hallucinations]]
- [[sources/research-that-scales-towsey-2024|Research That Scales]]
- [[sources/user-interviews-ai-assistant|User Interviews - AI Assistant]]

