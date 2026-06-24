---
source_url: https://guanjie.li/Thinking-out-louder/2026/06/18/what-LLM-can-and-cannot-find.html
captured: 2026-06-22
title: "Lost in Translation: What LLM Can and Cannot Find for Product Teams in User Interview Transcripts"
authors: [Guanjie Li]
published: 2026-06-18
publisher: Thinking Out Louder (personal blog)
---

# Lost in Translation: What LLM Can and Cannot Find for Product Teams in User Interview Transcripts

**Authors:** Guanjie Li
**Published:** 2026-06-18 — Thinking Out Louder (personal blog); part of a series on LLM-powered user proxies

## Summary

An empirical, methodology-driven blog post asking which UX-research questions are actually suited to LLMs reading interview transcripts. "User proxy" here is defined specifically: not a synthetic persona built from demographic priors, but an LLM given a *single real participant's* interview transcript and asked to answer research questions about that participant. The author sampled 50 transcripts from Anthropic's publicly available LLM-conducted professional interview dataset (`Anthropic/AnthropicInterviewer`, covering how professionals think about AI at work — trust, workflow integration, emotional responses, social context) and designed 25 questions simulating what a product team might want to learn (friction in AI-assisted workflows, trust issues, roadmap priorities, reliability signals). Two questions were dropped (their topics appeared in fewer than three transcripts), leaving 23 for analysis.

Two evaluation instruments are crossed against each other:

1. **Well-posedness** — how consistently the LLM-grader can even classify a question as *answerable* from a given transcript. Operationalized via a transcript-grounded grader run 9 times on each of the 50 transcripts; the *within-participant variance* of those answerable/not judgments is the instability, normalized by the Bernoulli maximum 0.25 so the score reads as a fraction (1.0 = grader never uncertain; 0 = 50/50 every run). High well-posedness = stable criterion.
2. **Human prior-reading pass rate** — how often the proxy's response matched the author's own prior reading of the same transcript (a product-relevant judgment). Catches the case where the proxy answers *consistently* but answers the *wrong thing* — a failure invisible to any automated check.

**Findings (which question types travel through the rubric):**

- **Works (upper-right: stable + aligned):** questions about *observable behavior*, *factual experience*, and *explicit stance* — questions with a relatively clear evidentiary standard. A subset (Q13 privacy concerns, Q16 role shift to oversight, Q12 social stigma) have very low base rates (<1/4 of participants), and the proxy handles them well largely *by abstaining* when signal is absent.
- **Doesn't work, for distinct reasons:**
  - *Emotional/affective questions.* Q08 (positive emotions) is well-posed (blue) but pale — "user satisfaction" sounds simple, but what counts as a *product-relevant* expression of it is use-dependent (finding a value proposition needs affect strong enough to matter; long-term satisfaction may need only cognitive appraisal). Q10 (frustration) is lilac — whether negative mentions "count" as frustration has no stable answer until a threshold is defined. Q09 (performance concerns) was easy to surface literally but diverged from the author's reading, which wanted a *real gap between user expectation and LLM capability* at a decision-relevant grain.
  - *Fine-grained behavioral/process questions* (Q22 follow-up prompting, Q23 post-AI workflow handoff, Q24 communication-style preference). Signal for micro-behaviors is sparse and fragmented in interview text; Q24 also has a fuzzy construct ("communication style" spans prompts, file uploads, templates). These are often *most valuable to designers precisely because they're hard to ask directly* — and for the same reason hard for an LLM to extract reliably.
  - *Normative questions* (Q15 tasks humans should do regardless of AI capability, Q18 broader societal concerns). They ask what *ought* to be; whether a statement rises to a "considered position" needs tone/intent reading and product context the proxy lacks.
  - Q01 (AI tools used) is a special case: red but not pale — the proxy reads content well, but the *criterion itself* is unstable (does "an AI assistant" or "AI features in Adobe" count as specifying a tool?). Any definition of "specific enough" lags the fast-changing tool landscape.

**Core claim — the bottleneck is communication, not LLM capability.** A user proxy is a communication channel: the human specifies what they want, the proxy extracts it, an evaluator checks fidelity — every step needs a shared understanding of "what counts." Human colleagues build that understanding implicitly from accumulated product exposure; the rubric is the only interface between human and LLM, and some things don't fit through it because the understanding was never fully linguistic. This is *why qualitative research can't be fully replaced by running transcripts through an LLM, regardless of model capability*: the cost of communicating intent precisely is highest exactly where research value is highest — in the findings a team didn't know to look for until they saw them. **A tighter rubric makes the proxy more reliable at finding what you specified, and less likely to surface what you didn't.** The most valuable qualitative insights reframe the question and can't be pre-written into a rubric.

**Three practical levers** to improve LLM transcript processing: (1) **question selection** (favor observable/factual/explicit questions; emotional/process/normative cost more and may not be worth it); (2) **question refinement** (sharpen wording/rubric boundary — but if the boundary depends on product context, no rewording fully closes the gap, and over-specifying suppresses unexpected findings); (3) **context provision** (give the LLM your role, decisions, and what you already know — highest effort, highest ceiling, but requires externalizing tribal knowledge you may not know you have). For builders: extracting info is the easy half; the hard half is helping product-team members communicate intent clearly enough that the rubric can carry it — design question sets iteratively, stress-test rubric boundaries against real responses, build in context-specification.

## Key Points

- **User proxy = single real participant's transcript + LLM**, not a demographic synthetic persona. The post asks a prior question for any proxy: which questions are worth asking it at all?
- **Dataset:** 50 transcripts sampled from Anthropic's public `AnthropicInterviewer` LLM-conducted professional-interview dataset; 25 questions designed, 2 dropped (base rate < 3 transcripts), 23 analyzed.
- **Well-posedness** = 1 − (mean within-participant variance / 0.25), grader run 9× on each of 50 transcripts. Measures whether a question has a *stable enough target* for any proxy to be held to. Measured *through the grader*, not the proxy, because answerability is a property of transcript + rubric, not the proxy alone.
- **Human prior-reading pass rate** = how often the proxy matched the author's product-relevant reading; catches "answered consistently but answered the wrong thing."
- **Works:** observable behavior, factual experience, explicit stance (clear evidentiary standard). Low-base-rate questions handled well via abstention.
- **Doesn't work:** emotional/affective (threshold of "what counts" is use-dependent), fine-grained process/micro-behaviors (sparse, fragmented signal; fuzzy constructs), normative positions (need tone/intent + product context).
- **Q01 lesson:** instability can live in the *criterion* ("specific enough"), not the proxy's reading; rubrics lag a fast-moving tool landscape.
- **Central thesis:** the bottleneck is *communication*, not model capability. The rubric is the only human↔LLM interface and some understanding was never fully linguistic.
- **Irreducibility of qual research:** the highest-value insights reframe the question and can't be written into a rubric in advance; tighter rubric ⇒ more reliable on the specified, less likely to surface the unspecified.
- **Three levers:** question selection, question refinement, context provision (ascending effort and ceiling).
- **For builders:** the hard half is the human side — eliciting and externalizing implicit/tribal product knowledge into the rubric.

## Methodology / Instrument Detail

- **Well-posedness formula:** for each question–transcript pair, grader runs r times producing a binary answerable/not judgment; p_b = fraction of runs calling it answerable for participant b; within-participant variance = p_b(1 − p_b) (0 when consistent, max 0.25 at p=0.5). Well-posedness = 1 − (1/0.25)(1/N) Σ p_b(1−p_b). N = 50, r = 9.
- **Caveat 1:** uses *within-participant* variance, not total variance — deliberately excludes between-participant base-rate heterogeneity (e.g., Q13 privacy, Q16 oversight have near-zero well-posedness variance but low base rates; the grader is consistent that most transcripts don't address them).
- **Caveat 2:** raw (uncorrected) variance used for normalization to keep the [0,1] bound; differs from unbiased estimator by <12%, doesn't change ranking.
- **Caveat 3:** Figure 1 is for direction, not precision — bootstrap 90% CIs over 50 transcripts overlap for mid-range questions. Q01 sits clearly left (0.64); a handful sit clearly right (1.0); the middle is hard to rank confidently.
- **Why not measure answerability from the proxy directly?** Answerability isn't a property of the proxy alone — it only has meaning once you define what counts as an answer, and that choice lives in the rubric (Q01 is the clearest case). No grader-free shortcut: re-running the proxy and comparing responses would itself require applying the rubric.
- **Why not a human judge?** A human faces the same instability on genuinely ambiguous boundary cases; the difference is the grader's drift is *measurable* (re-run with no memory) and human drift is not. The grader makes instability visible and quantifiable, not a substitute for human judgment.

## Short Quoted Excerpts

- "The bottleneck isn't the model's ability to read or reason, but the cost of communicating what you are looking for precisely enough that the model can find it."
- "A tighter rubric makes the proxy more reliable at finding what you specified; it also makes it less likely to surface what you didn't. The most valuable qualitative insights tend to be the ones that reframe the question, and those can't be written into a rubric in advance."
- "The rubric is the only interface between a human and an LLM, and some things don't fit through it, because the understanding itself was never fully linguistic to begin with."
- "Getting the proxy to extract information from a transcript is the easier half of the problem. The harder half is on the human side."
- "It is not a capability problem. It is a question design problem, and more specifically, a communication problem: the LLM may have found what the question asked for; the question just didn't ask for what you needed."

## Context Notes

- Part of a series: prior posts established the two graders (transcript-grounded + human prior-reading) and the "user proxies in the LLM era" framing.
- Author: Guanjie Li (independent researcher; LinkedIn profile linked; GitHub Pages / Jekyll blog).
- The figure (well-posedness × human prior-reading pass rate) is an interactive scatter; per-point detail and CIs revealed on hover.
