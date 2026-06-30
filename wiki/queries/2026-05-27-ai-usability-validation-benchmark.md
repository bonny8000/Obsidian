---
type: query
status: active
created: 2026-05-27
updated: 2026-06-26
tags: [query]
sources: [sources/measuringu-ai-real-ui-problems-hallucinations, sources/measuringu-ai-usability-problem-analysis-video, sources/measuringu-synthetic-users-review, sources/toss-tech-research-platform-ai]
confidence: 0.78
---

# Query: ai usability validation benchmark

## Short Answer

Validate AI-generated usability findings on two separate axes — reliability (consistency) and validity (truth) — and never let one stand in for the other. First measure reliability: run the AI multiple times on the same session and across models, then quantify overlap with [[concepts/ux-research/any-2-agreement|Any-2 Agreement]], interpreting low overlap against the known human [[concepts/ux-research/evaluator-effect|Evaluator Effect]] rather than treating it as automatic failure. Then test validity by triaging every AI-only issue into genuine finds, false alarms, or hallucinations against the original video/transcript — MeasuringU's 2026 follow-up found only 1 of 11 AI-only issues genuine, 7 false alarms, and 3 hallucinations, so triage is a mandatory quality gate, not cleanup. Benchmark AI output against a human baseline drawn from the same material: in the MeasuringU video study, four human researchers found 9 problems while two AI families across runs surfaced 14 (11 AI-only). For summative tracking, use a locked [[methods/benchmark-studies|Benchmark Study]] protocol with standardized metrics and confidence intervals so AI assistance never substitutes for measured human results. Throughout, AI's safe role is candidate generation, triage, and a second opinion — not final expert judgment or evidence in its own right. The wiki documents this validation logic well but lacks a settled numeric agreement threshold and a published calibration of any production tool (e.g. [[concepts/ux-research/huribot|Huribot]]) against formal UT results.

## Evidence

- [[concepts/ux-research/ai-usability-analysis|AI Usability Analysis]] — AI-generated problems must be evaluated for reliability before use; consistency does not prove correctness, and AI is best treated as assistance/triage until validated against human expert analysis and participant evidence.
- [[concepts/ux-research/reliability-vs-validity|Reliability vs Validity]] — reliability (consistency across runs/models) is a prerequisite for trust but not the same as accuracy; report consistency metrics first, then check validity against participant behavior and human judgment.
- [[concepts/ux-research/any-2-agreement|Any-2 Agreement]] — a practical reliability metric: does a problem found in one run/system appear in at least one other? Quantifies repeatability of problem lists but cannot by itself establish validity or importance.
- [[concepts/ux-research/evaluator-effect|Evaluator Effect]] — different evaluators naturally find different problems from the same session, so AI's low overlap with humans should be read against known human variability, not as proof AI is useless.
- [[concepts/ux-research/ai-usability-false-alarm-triage|AI Usability False-Alarm Triage]] — classify every AI-only issue as genuine find, false alarm, or hallucination before it enters a report; false alarms misinterpret something real, hallucinations report what never happened, and only checking the source video catches the latter.
- [[sources/measuringu-ai-real-ui-problems-hallucinations|MeasuringU: Does AI Find Real UI Problems or Just Hallucinations?]] — the validity benchmark: 4 humans found 9 problems, two AI families (ChatGPT-5.4 Thinking, Gemini 3 Flash Thinking) over 4 runs each surfaced 14, of which 11 were AI-only and only 1 genuine; ~9 in 10 AI-only issues needed correction or dismissal.
- [[sources/measuringu-ai-usability-problem-analysis-video|MeasuringU: AI Reliability for Finding UI Problems]] — the reliability benchmark: Gemini had higher within-model reliability than ChatGPT while cross-model reliability was low; do not treat AI problem lists as stable findings without validation.
- [[concepts/ux-research/validity-and-decision-relevance|Validity and Decision Relevance]] — pair validity (does the evidence support the claim?) with decision relevance (does the claim answer the real decision?); AI lowers artifact cost but volume never proves soundness, so evaluate generated outputs against both, not against fluency.
- [[concepts/ux-research/ai-evals|AI Evals in Research]] — operational acceptance tests for AI research output: source verification against originals, confidence scoring, model councils (cross-checking multiple LLMs), and counter-bias querying to surface contradictory evidence.
- [[methods/benchmark-studies|Benchmark Studies]] — for summative human-baseline comparison: lock tasks, metrics, and analysis plan; report deltas with confidence intervals and never read movement inside the interval; LLMs are safe for drafting/anomaly-flagging but statistics must be reproduced from raw data, not LLM arithmetic.
- [[comparisons/ai-assisted-research-risk-matrix|AI-Assisted Research Risk Matrix]] — rates usability issue detection as high-risk with the required guardrail "compare against session/video evidence"; AI output is not evidence unless grounded in preserved source material.
- [[sources/measuringu-synthetic-users-review|MeasuringU: A Review of Experiments with Synthetic Users]] — the validation pattern generalizes: synthetic users match humans on surface means but fail on variance, subgroup means, and depth (only 21% of psychology studies replicated), so AI-as-human-substitute must clear an explicit validation gate before any decision.
- [[concepts/ux-research/huribot|Huribot]] — Toss's production AI usability assistant is deliberately positioned as a "check" tool that supplements rather than replaces formal UT, with formal usability testing reserved for deeper validation — a real-world instance of keeping the human benchmark in the loop.
- [[concepts/ux-research/sample-size-for-usability-studies|Sample Size for Usability Studies]] — any human-vs-AI comparison must respect sample-size logic: small-n usually means wider intervals and lower power, not invalidity; report interval width rather than defending a magic-number participant count.

## Reusable Notes

- Validation is two gates in sequence: a reliability gate (Any-2 overlap across runs and models, read against the Evaluator Effect) then a validity gate (genuine / false-alarm / hallucination triage against the original session evidence). Passing the first does not satisfy the second — consistency is not validity.
- Benchmark AI against a same-material human baseline, and treat the AI-only set as hypotheses, not findings. The empirical anchor from the wiki is roughly 1-in-11 AI-only issues genuine, which makes triage a required quality gate rather than optional cleanup.
- Keep AI in the [[comparisons/ai-assisted-research-risk-matrix|high-risk]] lane for issue detection: useful as candidate generation and a second opinion, but never counted as evidence unless every claim links to preserved source material.

## Follow-up Sources Needed

- A defensible Any-2 / overlap threshold: the wiki names the metric but no source sets the acceptable agreement level for trusting AI-assisted triage (open question carried in the Any-2 Agreement page).
- A published calibration of a production tool against formal UT — Huribot's open questions explicitly ask how Toss measures its reliability against real UT outcomes; no source answers this yet.
- A minimum evidence checklist / lightweight rubric for accepting an AI-generated usability issue (open question in the False-Alarm Triage and Validity-and-Decision-Relevance pages), plus replication of the MeasuringU result beyond its single video and two model families.
