---
type: source
status: draft
created: 2026-07-12
tags: [llm, uxr, user-proxies, evaluation]
---
# What LLMs Can and Cannot Find in UXR Transcripts

## Citation
Guanjie Li. (2026-06-18). What LLMs can and cannot find. https://guanjie.li/Thinking-out-louder/2026/06/18/what-LLM-can-and-cannot-find.html

## Summary
The post evaluates the effectiveness of using LLM-powered user proxies to answer UX Research (UXR) questions based on user interview transcripts. It empirically measures 23 UXR questions on two axes: "well-posedness" (consistency of the LLM's classification of answerability based on the transcript) and "human prior-reading pass rate" (how often the proxy's responses align with human expert readings). 

## Key Claims
- LLMs are effective at answering UXR questions about observable behavior, factual experience, and explicit stances.
- LLMs struggle with questions regarding emotional/affective states, fine-grained process behaviors, and normative positions.
- The bottleneck in using LLMs for qualitative research is not the model's capability, but the communication gap—the difficulty for humans to articulate their implicit thresholds and context into a rubric.
- To improve LLM processing of interview transcripts, researchers should select well-posed questions, refine wording carefully, and provide robust product context upfront.

## Useful Examples
- Q13 (privacy concerns), Q16 (role shift to oversight), and Q12 (social stigma) have low base rates but are handled well by the proxy because it abstains when the signal is absent.
- Q08 (positive emotions) and Q10 (frustration with AI) struggle because product-relevant definitions of "satisfaction" or "frustration" are highly context-dependent and difficult to transmit via a rubric.

## Constraints / Caveats
- Well-posedness does not measure total variance, but rather the within-participant variance of the grader's uncertainty.
- Refining a question’s rubric creates a tradeoff: a tighter rubric improves reliability for specific answers but reduces the likelihood of surfacing unexpected findings.

## Design Implications
- When building user proxies, focus engineering efforts on helping human researchers communicate their intent clearly, rather than just optimizing the LLM for data extraction.

## Tensions
- The tension between a rigid rubric that yields reliable answers and the exploratory nature of qualitative research, where the most valuable insights often come from answers to unasked questions.

## Open Questions
- How to better bridge the communication gap between human implicit product knowledge and the explicit rubrics required by LLMs?

## Concepts Linked
- [[guanjie-li-llm-user-proxy]]

## LLM Use
- The researcher used an LLM to build user proxies and grade answerability over multiple iterations per transcript.

## Reliability Notes
- The evaluation was conducted on 50 transcripts from the Anthropic LLM-conducted professional interview dataset, providing a reasonable empirical foundation for the claims. 

## Backfill Status
- Not started.
