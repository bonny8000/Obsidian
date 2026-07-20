---
type: source
status: active
created: 2026-06-22
updated: 2026-07-20
tags: [ux-research, llm-user-proxy, interview-transcripts, well-posedness, rubric-design, qualitative-research, ai-analysis, question-design, validity, synthetic-users]
source_path: raw/web/guanjie-li-llm-user-proxy-2026-06-22.md
source_url: https://guanjie.li/Thinking-out-louder/2026/06/18/what-LLM-can-and-cannot-find.html
authors: [Guanjie Li]
sources: []
ingest_level: deep
coverage: full
llm_ready: true
raw_preserved: true
confidence: 0.8
---

# Lost in Translation: What LLMs Can and Cannot Find in Interview Transcripts (Guanjie Li)

**Authors:** Guanjie Li
**Published:** 2026-06-18 — Thinking Out Louder (personal blog); part of a series on LLM-powered user proxies
**Raw capture (upgraded to verbatim full text incl. both appendices, 2026-07-20):** [[raw/web/guanjie-li-llm-user-proxy-2026-06-22|guanjie-li-llm-user-proxy-2026-06-22]]
**URL:** [guanjie.li/.../what-LLM-can-and-cannot-find](https://guanjie.li/Thinking-out-louder/2026/06/18/what-LLM-can-and-cannot-find.html)

## Citation

Li, G. (2026, June 18). *Lost in translation: What LLM can and cannot find for product teams in user interview transcripts.* Thinking Out Louder. Retrieved 2026-06-22 from https://guanjie.li/Thinking-out-louder/2026/06/18/what-LLM-can-and-cannot-find.html

## Summary

An empirical methodology post on which UX-research questions suit LLMs reading interview transcripts. A "user proxy" is defined narrowly: an LLM given a *single real participant's* transcript (not a demographic synthetic persona) and asked research questions about that participant. Using 50 transcripts from Anthropic's public `AnthropicInterviewer` dataset and 23 product-team questions, the author crosses two instruments: **well-posedness** (how consistently an LLM-grader classifies a question as answerable — within-participant variance over 9 runs, normalized by 0.25) and **human prior-reading pass rate** (how often the proxy matched the author's own product-relevant reading). Observable-behavior, factual-experience, and explicit-stance questions travel well; emotional/affective, fine-grained process/micro-behavior, and normative questions do not — because the product-relevant *threshold* for a useful answer is hard to transmit through a rubric. The core claim: **the bottleneck is communication, not LLM capability.** Qual research can't be fully replaced because the highest-value insights reframe the question and can't be pre-written into a rubric; a tighter rubric finds what you specified but misses what you didn't. Three levers improve results: question selection, question refinement, context provision.

## Key Claims

- **A user proxy is a communication channel**, not just an extractor: human specifies → proxy extracts → evaluator checks fidelity; every step needs a shared "what counts," and the rubric is the only human↔LLM interface.
- **Well-posedness** (criterion stability) and **human prior-reading pass rate** (answering the *right* thing) catch *different* failures; neither alone suffices. A question can be well-posed yet pale (stable criterion, content diverges from product-relevant reading — e.g., Q08 positive emotions).
- **Works:** observable behavior, factual experience, explicit stance (clear evidentiary standard). Low-base-rate topics are handled well via abstention.
- **Doesn't work, for distinct reasons:** emotional/affective (threshold is use-dependent), fine-grained process/micro-behaviors (sparse, fragmented signal; fuzzy constructs like "communication style"), normative positions (need tone/intent + product context).
- **Instability can live in the criterion, not the proxy** (Q01 "AI tools used": the proxy reads correctly, but "specific enough" is undefinable and lags the fast-moving tool landscape).
- **Qualitative research is not fully LLM-replaceable** regardless of model capability: the cost of communicating intent is highest exactly where research value is highest. **Tighter rubric ⇒ more reliable on the specified, less likely to surface the unspecified.**
- **Three levers (ascending effort/ceiling):** question selection, question refinement, context provision; context provision can rescue ill-posed questions but requires externalizing implicit/tribal knowledge.

## Useful Examples

- **Q08 (positive emotions)** — well-posed but pale: "user satisfaction" sounds simple, but whether affect is *product-relevant* depends on use (value-prop discovery needs strong affect; long-term satisfaction may need only cognitive appraisal). A concrete demonstration that affect questions need a specified threshold.
- **Q10 (frustration)** — lilac: negative mentions don't "count" as frustration until a threshold is defined.
- **Q01 (AI tools used)** — red-but-not-pale: "does 'AI features in Adobe' count as specifying a tool?" shows criterion instability independent of proxy reading.
- **Q22/Q23/Q24 (follow-up prompting, post-AI handoff, communication style)** — the micro-behaviors most valuable to designers are the hardest both to ask directly and for an LLM to extract.
- **Well-posedness formula** (raw capture, Methodology) — a reusable instrument: 1 − (1/0.25)(1/N) Σ p_b(1−p_b), grader run 9× over 50 transcripts.

## Constraints / Caveats

- Coverage is `substantial`; the post's interactive figure and per-question CIs were not fully transcribed (Figure 1 is "for direction, not precision" — mid-range questions' bootstrap CIs overlap). Verify specific per-question scores against `raw/web/guanjie-li-llm-user-proxy-2026-06-22.md` and the original interactive figure.
- Single dataset (Anthropic professional-interview transcripts about AI-at-work), one question set, one proxy architecture; the *pattern* is argued to generalize, but the specific scores are context-bound (author says so explicitly).
- Independent-researcher blog with stated methodology; not peer-reviewed. Confidence 0.8.
- Well-posedness uses *within-participant* variance by design (excludes base-rate heterogeneity); raw (uncorrected) variance used for the [0,1] bound (<12% difference, ranking unchanged).

## Design Implications

- **Triage research questions before handing them to an LLM:** route observable/factual/explicit questions to proxies; keep emotional, micro-process, and normative questions for human analysis or invest heavily in context provision.
- **Treat the rubric as a product surface**: design question sets iteratively, stress-test rubric boundaries against real proxy responses, and build explicit context-specification into proxy tooling.
- **Guard against the over-specification trap:** for exploratory/discovery work where unexpected findings are the point, do *not* over-tighten the rubric — it suppresses what you didn't know to ask.
- **Set expectations honestly:** "uneven LLM results" are usually a question-design/communication problem, not a model failure — sharpen the question or supply context before blaming the model.
- Pairs directly with the depth-at-scale and synthetic-user critiques already in the vault: this is the *mechanism* (rubric-as-bottleneck) behind why scale doesn't replace interpretation.

## Tensions

- **Reliability vs. discovery.** A tighter rubric raises proxy reliability on specified targets but lowers the chance of surfacing reframing insights — directly in tension for exploratory research.
- **Automatable vs. valuable.** The questions easiest to automate (observable/factual) are often the least strategically valuable; the most valuable (affective, micro-behavioral, normative) are the hardest to transmit.
- **Grader instability vs. human-judge instability.** Both drift on boundary cases; the grader's drift is measurable and a human's isn't — so the grader is the instrument that makes fuzziness *visible*, not a replacement for human judgment.

## Open Questions

- How far does the works/doesn't-work pattern hold across other domains, question sets, and proxy architectures?
- Can "context provision" be systematized into reusable context templates that externalize tribal product knowledge without huge per-study effort?
- Is there a principled way to detect, in advance, when a question's useful threshold is "non-linguistic" and therefore rubric-resistant?
- How should teams decide the ROI line between investing in context provision vs. doing the analysis manually?

## Concepts Linked

- [[concepts/ux-research/ai-analysis|AI Analysis]]
- [[concepts/ux-research/human-interpretation|Human Interpretation]]
- [[concepts/ux-research/genai-in-qualitative-research|GenAI in Qualitative Research]]
- [[concepts/ux-research/grounded-synthetic-personas|Grounded Synthetic Personas]]
- [[concepts/ux-research/ai-persona-replication|AI Persona Replication]]
- [[concepts/ux-research/validity-and-decision-relevance|Validity and Decision Relevance]]
- [[concepts/ux-research/ai-moderated-interviews|AI-Moderated Interviews]]
- [[concepts/ux-research/llm-user-proxy|LLM User Proxy]] (new) — an LLM given a single real participant's transcript and asked research questions about that participant (distinct from demographic synthetic personas).
- (new) concepts/ux-research/question-well-posedness — how consistently a question's answerability can be classified from a transcript; criterion stability as a precondition for reliable LLM extraction.
- (new) concepts/ux-research/rubric-as-communication-bottleneck — the rubric is the only human↔LLM interface; the limit on LLM qual analysis is transmitting intent, not model capability.

## LLM Use

- **Use for:** deciding which interview-transcript questions to send to an LLM vs. keep human; designing and stress-testing extraction rubrics; explaining *why* LLM transcript analysis is uneven; arguing the irreducibility of qual research from a methodology (not vibes) basis.
- **Do not use for:** quoting precise per-question well-posedness scores without checking the interactive figure; generalizing the numeric results beyond the single dataset; claiming LLMs *cannot* find affective/normative signal (the claim is about cost/threshold transmission, not impossibility).
- **Best prompt pattern:** "For this research question and transcript set, classify the question as observable/factual/explicit vs. affective/micro-process/normative; if it's the latter, propose either a sharpened rubric boundary or the specific product context to provide — and flag whether tightening would suppress discovery."

## Reliability Notes

> [!warning] Caveats
> - **Independent blog, stated methodology, not peer-reviewed.** Confidence 0.8: high for the conceptual argument (rubric-as-bottleneck, the works/doesn't-work taxonomy), lower for the exact numeric scores (single dataset, overlapping CIs, author's own "direction not precision" caveat).
> - The well-posedness instrument is the author's construction; treat the formula as a reasonable but bespoke metric, not a field standard.
> - Verify any specific Q-number score, base rate, or formula detail against the raw capture before external use.

## Backfill Status

- New 2026-06-22. Deep ingest: all sections plus methodology detail captured from full-text fetch.
