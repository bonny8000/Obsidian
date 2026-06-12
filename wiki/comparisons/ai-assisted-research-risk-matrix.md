---
type: comparison
status: active
created: 2026-06-12
updated: 2026-06-12
tags: [comparison, ux-research, ai-assisted-research, risk]
sources:
  - sources/measuringu-ai-real-ui-problems-hallucinations
  - sources/measuringu-ai-usability-problem-analysis-video
  - sources/sage-10778004251401851-genai-reflexive-qualitative-research
  - sources/user-interviews-ai-assistant
confidence: 0.82
---

# Comparison: AI-Assisted Research Risk Matrix

## Decision Question

When is it safe to use an LLM in UX research, and what must be verified?

## Criteria

- Whether raw evidence exists.
- Whether the output is descriptive, interpretive, or decision-prescriptive.
- Whether the model can be checked against source material.
- Whether the task could create fake users, fake quotes, or fake severity.

## Matrix

| AI task | Useful for | Main risk | Required guardrail | Use level |
| --- | --- | --- | --- | --- |
| Summarizing transcripts or notes | speed and navigation | missed nuance | preserve raw notes and review summaries | medium |
| Clustering findings | pattern discovery | false grouping | keep evidence links per cluster | medium |
| Drafting discussion guides | first-pass structure | leading or generic questions | researcher review and pilot | medium |
| Coding qualitative data | candidate codes | replacing interpretation | researcher memo and sample audit | medium-high |
| Usability issue detection | triage and second opinion | hallucinated UI problems | compare against session/video evidence | high |
| Synthetic participants/personas | exploration | fake evidence | label as synthetic and never count as user data | high |
| Decision recommendations | synthesis | unsupported authority | require source-linked claims and caveats | high |

## Recommendation Pattern

- Use AI most confidently for navigation, summarization, and candidate generation.
- Use AI cautiously for interpretation and severity.
- Do not treat AI output as evidence unless it is grounded in preserved source material.
- For every generated insight, ask: which source record supports this, what raw evidence backs it, and what would change if it is wrong?

## Source Evidence

- [[sources/measuringu-ai-real-ui-problems-hallucinations|MeasuringU - AI Real UI Problems and Hallucinations]]
- [[sources/measuringu-ai-usability-problem-analysis-video|MeasuringU - AI Usability Problem Analysis Video]]
- [[sources/sage-10778004251401851-genai-reflexive-qualitative-research|GenAI and Reflexive Qualitative Research]]
- [[sources/user-interviews-ai-assistant|User Interviews - AI Assistant]]

