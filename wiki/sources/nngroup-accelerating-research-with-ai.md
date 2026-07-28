---
type: source
status: active
created: 2026-07-28
updated: 2026-07-28
tags: [ux-research, ai, research-lifecycle, usability-testing, ai-analysis, ai-moderated-interviews, guardrails, nngroup]
source_path: raw/web/nngroup-accelerating-research-with-ai-2026-07-28.md
source_url: https://www.nngroup.com/articles/research-with-ai/
authors: [Kate Moran, Maria Rosala]
sources: []
ingest_level: deep
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.88
---

# NN/g (2024, reviewed 2026): Accelerating Research with AI

## Citation

Kate Moran & Maria Rosala, *Accelerating Research with AI*, **Nielsen Norman Group**, published 2024-09-27, last reviewed 2026-01-21.

**Source type:** Practitioner guidance from an established authority, organized as a lifecycle assessment. Opinion-and-experience based, not a study.
**Raw capture:** [[raw/web/nngroup-accelerating-research-with-ai-2026-07-28|nngroup-accelerating-research-with-ai-2026-07-28]]

## Summary

The most useful **stage-by-stage map** of where AI helps and fails across UX research, and the vault's best anchor for "which research tasks are safely delegable." The finding: AI is most helpful in **planning** and **analysis**, and least trustworthy in **conducting** research — because conducting is where behavior lives, and AI reads language.

The central limitation is stated plainly: AI-moderated usability tools analyze a *transcript*, not what the user did, and people often say one thing and do another. That single distinction does most of the load-bearing work in the article.

## Key Claims

- **Four stages, unequal suitability:** planning ✅, conducting ❌ (mostly), analyzing ✅ with heavy caveats, reporting ✅ for craft work.
- **AI cannot watch a usability test.** "Current AI tools are not (yet) capable of actually knowing what users are doing." The authors state they have yet to see a tool that can properly watch usability tests — despite AI being capable of video analysis in general.
- **Behavioral observation is the hard boundary.** Gestures, eye gaze, cursor hover, nonverbal cues are outside reach; AI backup notetakers miss behavioral observation entirely.
- **Semi-structured interviews resist automation** specifically because the guide is used *flexibly* — AI interviewers lack a face and cannot read expressions.
- **Language-based bias is the underlying mechanism.** AI performs better on attitudinal / self-reported data than behavioral data *because that data is language-based.* This explains the whole pattern of what works and what doesn't.
- **AI coding is an initial pass only.** Generated codes often miss large sections or cluster shallowly around keywords; a human must synthesize into insight.
- **Context blindness in analysis:** AI cannot ask how a statement contrasts with the participant's other statements, or whether the interviewer primed them.
- **Stochasticity is a design constraint, not a bug to prompt away:** "AI is stochastic — it can choose to pay attention to certain things but disregard others," which may mean attending to the wrong aspects of the data.
- **The intern framing:** the tools work best given ample instructions, context, constraints, and corrections.

## Useful Examples

**Where AI is endorsed:**

| Stage | Endorsed uses |
|---|---|
| Planning | Desk research (verify sources) · ideation for survey questions, interview prompts, usability tasks · documentation from templates — consent forms, screeners, facilitation scripts |
| Analyzing | Transcription and translation with timestamped linking · session summarization · PII sanitization · preliminary coding (Miro clustering, Dovetail suggested codes) · missing-data handling, descriptive stats, rough sentiment |
| Reporting | Copyediting and tone · persona / journey-map drafts **if grounded in real data** · repository querying by question rather than keyword |

**Where AI is refused:** moderating usability tests · notetaking behavioral observation during usability tests · running semi-structured interviews · replacing human interpretation in thematic analysis.

**Named guardrails worth lifting directly:**

- "Always ask AI systems to cite primary sources, and then go check those sources."
- Supply best-practice frameworks *before* asking for tasks or questions — AI may generate leading questions even when guided.
- Supply templates before asking for documentation drafts.
- Double-check transcriptions, especially with multiple speakers or poor audio.
- Provide research goals as context to improve output relevance.
- Spot-check quantitative analysis.
- Ground personas and journey maps in actual data; watch for invented details.
- AI interviewers are considerable for structured feedback at scale, but not for complex or specialized topics.

**A concrete misinterpretation example:** a sanitization pass redacted tool names in the mistaken belief it was protecting privacy — the failure mode where a safety behavior destroys the data.

## Constraints / Caveats

- **Published 2024-09-27, last reviewed 2026-01-21.** The tool-capability claims are the perishable part. "No AI tool can properly watch usability tests" is a statement about the 2024–early-2026 market, not a permanent limit, and the authors' own "(yet)" concedes this. Re-verify before citing as current.
- **No study behind it.** This is expert practitioner guidance, not empirical research — no sample, no measurement, no comparison of AI-coded versus human-coded output.
- **Named tools date fast.** Specific products cited as examples of AI moderation or AI interviewing may have changed materially since.
- **NN/g has commercial interest in research expertise** remaining scarce and valuable. The conclusions are well-argued and consistent with other sources in this wiki, but the institutional incentive is worth naming.
- Ingested from an AI-generated extraction, not a verbatim read.

## Design Implications

- **Split delegation by data type, not by task name.** The reliable predictor is whether the evidence is *language* (delegable with review) or *behavior* (not delegable). This generalizes better than any per-tool judgment.
- **Never let AI moderate a usability test**, and do not accept transcript analysis as a substitute for observation. If a vendor claims AI-moderated usability testing, ask what it observes.
- **Use AI to open the analysis, not to close it.** Preliminary codes, summaries, and sanitization are the safe band; theme synthesis and interpretation are not.
- **Front-load context and templates.** Every endorsed use in the article is conditioned on the researcher supplying framework, template, or goal first.
- **Require citations and check them.** Applies as much to internal desk research as to literature review.
- **Budget verification time into every acceleration claim.** Faster transcription plus mandatory multi-speaker double-checking is a smaller net gain than it appears.

## Tensions

- **Directly complements [[wiki/sources/when-research-gets-faster|Venkat's "when research gets faster"]]:** NN/g answers *what* can be accelerated; Venkat answers *why acceleration doesn't help by itself*. Read together they say the delegable band is real but narrow, and it sits in the middle of the process rather than at either end.
- **Corroborates [[wiki/concepts/ux-research/ai-moderated-interviews|AI-Moderated Interviews]]' bounded reading** and Bakhshi's "fallacy of depth at scale." Independent arrival at the same limit — language-bound methods cannot capture the unsaid — from a different author and publisher.
- **Against optimistic AI-UXR vendor claims** generally, and specifically against tools marketed as AI-moderated usability testing.
- **Tension with the "AI as senior hire" framing** running through this wiki's agent cluster: NN/g's operating metaphor is explicitly the *intern* — ample instructions, context, constraints, corrections. Two metaphors, opposite implications for how much latitude to grant, in different domains.
- **Recency conflict with itself.** A 2024 article reviewed in 2026 makes capability claims whose expiry date is unstated. Where it conflicts with a 2026 source on tool capability, prefer the 2026 source.

## Open Questions

- Has any tool since early 2026 demonstrably closed the behavioral-observation gap, and by what evaluation?
- Is there a published comparison of AI-generated versus human-generated qualitative codes with an agreement metric? This wiki lacks one.
- What is the actual error rate of AI transcription in multi-speaker research sessions, and does it vary by language?
- Does the "language-based data works, behavioral data doesn't" rule hold for multimodal models, or was it an artifact of text-only pipelines?

## Concepts Linked from This Source

- [[wiki/concepts/ux-research/ai-analysis|AI Analysis]]
- [[wiki/concepts/ux-research/ai-moderated-interviews|AI-Moderated Interviews]]
- [[wiki/concepts/ux-research/ai-usability-analysis|AI Usability Analysis]]
- [[wiki/concepts/ux-research/genai-in-qualitative-research|GenAI in Qualitative Research]]
- [[wiki/concepts/ux-research/validity-and-decision-relevance|Validity and Decision Relevance]]
- [[wiki/concepts/ux-research/human-interpretation|Human Interpretation]]
- [[wiki/concepts/ux-research/ai-uxr-maturity-matrix|AI UXR Maturity Matrix]]

## LLM Use

The **default authority** for "can AI do this research task?" Cite it for the four-stage split, the behavioral-observation boundary, the language-vs-behavior mechanism, and the named guardrails — which are specific enough to use as a checklist without paraphrase.

Treat its tool-capability claims as time-stamped: authoritative for the pattern, provisional for the market. Prefer a 2026 source on any specific tool's current ability.

## Reliability Notes

- **Highest-reliability source in the 2026-07-28 UXR cluster.** Established authority, two named expert authors, explicit last-reviewed date, consistent with independent sources in this wiki.
- **Confidence 0.88** rather than higher: it is expert opinion with no underlying study, its capability claims have a shelf life, and NN/g has an institutional stake in the conclusion.
- The "(yet)" hedging and explicit last-reviewed date are both good-faith signals about perishability.
- Ingested from an AI-generated extraction; quoted phrases need re-verification before external citation.
