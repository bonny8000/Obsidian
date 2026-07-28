---
source_url: https://www.nngroup.com/articles/research-with-ai/
captured: 2026-07-28
title: "Accelerating Research with AI"
authors: [Kate Moran, Maria Rosala]
published: 2024-09-27
last_reviewed: 2026-01-21
publisher: Nielsen Norman Group
language: en
---

# Accelerating Research with AI — NN/g

**Authors:** Kate Moran, Maria Rosala
**Published:** 2024-09-27 · **Last reviewed:** 2026-01-21 · **Captured:** 2026-07-28
**Capture note:** AI-written summary with short quoted phrases for attribution. Full text not reproduced.

## Summary

NN/g's stage-by-stage assessment of where AI helps and where it fails across the UX research lifecycle. Headline finding: **AI is currently most helpful in planning and analysis**, least trustworthy in *conducting* research. Human oversight is treated as non-negotiable throughout; the article's operating metaphor is that AI tools work "like interns."

## Framework — four stages

1. **Planning studies**
2. **Conducting research**
3. **Analyzing data**
4. **Reporting research**

Each stage carries capability marks (useful / limited / avoid) plus specific watch-outs.

## Where AI works well

### Planning

- **Desk research** — identifying starting sources, verification required.
- **Ideation** — survey questions, interview prompts, usability tasks; "a decent start" that needs expert review.
- **Documentation** — consent forms, screeners, facilitation scripts, when given templates.

Caution: AI may generate leading questions or violate best practices even when guided.

### Analysis

- **Transcription and translation**, multi-language, with timestamped linking.
- **Summarization** — key-point extraction from session recordings.
- **Data sanitization** — removing personally identifying information.
- **Preliminary coding** — initial tags and groupings from transcripts (Miro clustering, Dovetail suggested codes cited as examples).
- **Quantitative support** — missing data, descriptive statistics, rough sentiment analysis.

Limitation: AI-generated codes often miss large sections or produce shallow groupings around keywords.

### Reporting

- Copyediting and tone adjustment.
- Persona and journey-map drafts, **if grounded in real data**.
- Repository querying — stakeholders ask questions rather than searching by keyword.

## Where AI fails

### Conducting research — the critical gap

- **Usability testing.** "Current AI tools are not (yet) capable of actually knowing what users are doing." Tools claiming AI moderation analyze a *transcript*, not what the user did — which matters because people often say one thing and do another. The article's direct instruction: avoid using AI tools to moderate usability tests.
- **Behavioral observation.** AI cannot interpret gestures, eye gaze, cursor hover, or nonverbal cues. The authors note they "have yet to see an AI tool that can properly watch usability tests."
- **Notetaking during usability tests.** AI backup notetakers miss behavioral observations entirely.
- **Semi-structured interviews.** AI interviewers lack a face and the ability to read facial expressions, and are not capable of running semi-structured interviews where the guide is used flexibly.

### Analysis limits

- **Context blindness** — cannot ask how a statement contrasts with what else the participant said, or whether the interviewer accidentally primed them.
- **Misinterpretation** — e.g. redacting tool names in the mistaken belief it is protecting privacy.
- **Hallucination** — transcription errors with multiple speakers or poor audio; summaries that omit details.

## Recommendations and guardrails

**Planning** — "Always ask AI systems to cite primary sources, and then go check those sources." Specialized tools help but no generative system is free of misinformation, bias, or hallucination. Supply best-practice frameworks and templates before asking for drafts.

**Conducting** — AI notetakers acceptable as backup only; AI interviewers considerable for structured feedback at scale but not for complex or specialized topics; do not let AI moderate usability tests.

**Analyzing** — double-check transcriptions, especially multi-speaker; provide research goals as context; treat AI coding as an initial pass only, with humans synthesizing insight; spot-check quantitative analysis; ensure notes are complete enough to parse.

**Reporting** — ground personas and journey maps in actual data and watch for invented details; use chatbots for audience-specific tailoring.

## Caveats

- **Stochastic behavior** — "AI is stochastic — it can choose to pay attention to certain things but disregard others," which may mean focusing on the wrong aspects of the data.
- **No autonomous analysis** — a human still has to make sense of data and translate it into insight.
- **Language-based bias** — AI performs better on attitudinal / self-reported data than on behavioral data, because that data is language-based.
- **Contextual reasoning absent** — current tools cannot replicate the context-informed consideration humans apply in thematic analysis.
- **Instruction-dependent** — the tools work best given ample instructions, context, constraints, and corrections.
