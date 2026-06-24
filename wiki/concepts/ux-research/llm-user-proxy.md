---
type: concept
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [concept, llm-user-proxy, qualitative-research, interview-analysis, well-posedness, rubric]
sources: [guanjie-li-llm-user-proxy]
confidence: 0.8
---

# LLM User Proxy

> [!abstract] Summary
> An LLM given a single real participant's input (e.g., an interview transcript) and asked to answer research questions about that participant — distinct from synthetic personas built from demographic priors.

> [!important] Why it Matters
> A prior question for any proxy is *which questions are worth asking it at all.* Empirically, some UXR questions travel well through the proxy and some do not — and the deciding factor is whether a human can transmit their intent, not how capable the model is.

## 📝 Key Claims
- "Well-posedness" measures how consistently the LLM can classify whether a question is answerable from a transcript (within-participant variance of repeated judgments); an unstable criterion has no stable target.
- Works well: observable behavior, factual experience, explicit stance — questions with a clear evidentiary standard.
- Works poorly: emotional/affective questions, fine-grained process/micro-behaviors, and normative positions — the product-relevant threshold resists being written into a rubric.
- The bottleneck is communication: the rubric is the only human↔LLM interface, and a tighter rubric finds what you specified while missing what you didn't.
- Therefore qualitative research can't be fully replaced by piping transcripts through an LLM — the most valuable insights reframe the question and can't be pre-specified.
- Three levers to improve: question selection, question refinement, and context provision (role, decisions, what you already know).

## 🔗 Related Concepts
- [[concepts/ux-research/ai-persona-replication|AI Persona Replication]]
- [[concepts/ux-research/grounded-synthetic-personas|Grounded Synthetic Personas]]
- [[concepts/ux-research/genai-in-qualitative-research|GenAI in Qualitative Research]]
- [[concepts/ux-research/human-interpretation|Human Interpretation]]
- [[concepts/ux-research/ai-analysis|AI Analysis]]
- [[concepts/ux-research/validity-and-decision-relevance|Validity and Decision Relevance]]

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> Optimism about "synthetic users replacing research" runs into this finding: capability is not the limiter; transmissible intent is. Results are from one question set, one dataset, one proxy architecture.

## 📚 Sources
- [[sources/guanjie-li-llm-user-proxy|Li (2026): What LLMs Can and Cannot Find in Interview Transcripts]]

## ❓ Open Questions
- How much can context provision raise the ceiling for ill-posed but articulable questions?
- Can proxies be designed to surface unexpected findings rather than only what the rubric specifies?
