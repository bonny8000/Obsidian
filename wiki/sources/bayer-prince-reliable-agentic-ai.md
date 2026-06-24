---
type: source
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [agentic-rag, harness-engineering, context-engineering, text-to-sql, multi-agent, langgraph, human-in-the-loop, enterprise-ai, hybrid-retrieval]
source_path: raw/web/bayer-prince-reliable-agentic-ai-2026-06-22.md
source_url: https://martinfowler.com/articles/reliable-llm-bayer.html
authors: [Sarang Sanjay Kulkarni]
sources: []
ingest_level: deep
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.9
---

# Bayer PRINCE: Building Reliable Agentic AI Systems (Agentic RAG + Text-to-SQL)

**Authors:** Sarang Sanjay Kulkarni (Principal Consultant, Thoughtworks), with the Bayer team
**Published:** 2026-06-16 — martinfowler.com (Thoughtworks engineering)
**Raw capture:** [[raw/web/bayer-prince-reliable-agentic-ai-2026-06-22|bayer-prince-reliable-agentic-ai-2026-06-22]]
**URL:** [martinfowler.com/articles/reliable-llm-bayer.html](https://martinfowler.com/articles/reliable-llm-bayer.html)

## Citation

Kulkarni, S. S. (2026, June 16). *Building Reliable Agentic AI Systems: A case study in building production-ready agentic AI systems* [PRINCE at Bayer]. martinfowler.com. Captured 2026-06-22 into `raw/web/bayer-prince-reliable-agentic-ai-2026-06-22.md`. Companion peer-reviewed paper: *Frontiers in Artificial Intelligence* (10.3389/frai.2025.1636809).

## Summary

A production case study of **PRINCE** (Preclinical Information Center), an agentic AI platform built by Bayer with Thoughtworks so that pharmaceutical researchers can query decades of preclinical safety knowledge spread across structured metadata and unstructured PDF study reports. The system evolved through three phases — **Search** (unified metadata gateway), **Ask** (RAG over unstructured PDFs incl. scanned historical docs), and **Do** (a multi-agent assistant that orchestrates tasks and drafts regulatory documents). Live since early 2024; agentic integration added later that year.

The article's distinctive lens is **context engineering** (what each model sees, what it does not, and how context flows between steps) and **harness engineering** (the orchestration, state, retries, fallbacks, reflection loops, observability, and human review built *around* the models). Implemented on **LangGraph + FastAPI** with a React UI, PRINCE coordinates a **Researcher Agent**, **Reflection Agent**, and **Writer Agent** through: Clarify Intent → Think & Plan → Research (RAG + Text-to-SQL) → data-sufficiency check → Write. Its core discipline is **context discipline** — large context windows did not remove the need to route only the relevant slice to each agent. It implements **three reflection loops**: process (Think & Plan), data (Reflection Agent), and draft (Writer review).

This is the clearest concrete, regulated-domain worked example in the wiki of [[concepts/ai-agents/harness-engineering|Harness Engineering]] and [[concepts/ai-agents/model-harness|Model Harness]] applied to an [[concepts/ai-agents/agentic-ai|Agentic AI]] RAG system, complementing Böckeler's coding-agent sensor work (see [[sources/fowler-sensors-coding-agents|Fowler/Böckeler: Sensors for coding agents]], same publisher/genre).

## Key Claims

- **Reliability comes from engineering both the context the model sees AND the harness within which it acts** — not from better models or prompts alone. This is the article's thesis.
- **Search → Ask → Do** is the platform's evolution: metadata search → RAG question-answering → multi-agent task execution and regulatory drafting.
- **Context discipline beats one-big-prompt.** Each stage gets only its relevant context: planning context (Think & Plan), retrieval context (Researcher), evidence context (Reflection Agent), synthesis context (Writer). Concretely: Text-to-SQL injects only relevant schema; Reflection Agent gets question + evidence, not full history; Writer gets curated chunks + citation constraints, not raw retrieval.
- **Three complementary reflection loops:** process reflection (Think & Plan — right trajectory/tool/sequence), data reflection (Reflection Agent — sufficient & relevant evidence), draft reflection (Writer review — complete output, no missing sections/inconsistent tables).
- **Think & Plan ("thinking space," inspired by Anthropic's Think tool)** dramatically improved tool-selection accuracy once the tool count grew and domains (toxicology/pharmacology) overlapped, and enables multi-step orchestration where one tool's output drives the next.
- **Hybrid retrieval, tuned weights:** LLM keyword extraction + concurrent metadata-filter generation (e.g. `eq(study_id, T123456-2)`) + query expansion (n=5, smaller/faster model) + parallel weighted hybrid search (**0.7 semantic kNN / 0.3 keyword**) → ~20 chunks → cross-encoder rerank (**bge-reranker-large**) → **top 7** → grounded answer with automatic citations. Metadata pre-filtering shrinks the space from millions of vectors to tens–hundreds.
- **Text-to-SQL discipline:** dynamic relevant-schema injection, dynamic few-shot from a semantic-layer vector store, always-include study ID/title columns, SELECT-only validation, 50-row cap, up to **3** error-feedback self-correction retries. An LLM-review-of-SQL step was **removed** because it false-flagged valid queries.
- **Harness for resilience:** retries at LLM-call and node level; error context fed back so agents re-plan; state persistence (LangGraph checkpointer → Postgres for agent state, DynamoDB for app state) enables resume-from-failed-node and user retries that skip completed steps; multi-provider LLM fallbacks behind a unified OpenAI-compatible endpoint.
- **Trust via three mechanisms:** granular hover-level citations (link + page number + exact quote), visible intermediate steps/queries/tools, and human-in-the-loop. Regulatory drafts are always expert-reviewed; final submissions authored/approved by qualified personnel.
- **Evaluation at multiple stages (testing-pyramid analogy):** RAGAS metrics (Faithfulness, Answer Relevancy, Context Relevancy, Answer Accuracy, Semantic Similarity); dataset eval on major workflow/prompt/model changes; **daily live-traffic eval** batch job; CloudWatch (health) + Langfuse (traces + eval store).
- **NER-driven metadata repair with confidence-score quarantine:** a utility extracts entities from study PDFs; high-confidence fields auto-update Athena, low-confidence fields are quarantined for human review.
- **Direction of travel: domain-specific sub-agents.** A flat tool list on one Researcher becomes unmanageable; each domain should own its toolset + prompt instructions, with the top-level Researcher acting as a router/coordinator.

## Useful Examples

- **The three-reflection-loops taxonomy** (process / data / draft) — a reusable design checklist for any multi-step agentic workflow: is the trajectory right, is the evidence sufficient, is the output complete?
- **The worked hybrid-retrieval pipeline** on the query "Were any of the following clinical findings observed in study T123456-2: piloerection, ataxia, eyes partially closed, and loose faeces?" — shows keyword extraction, `eq(study_id, ...)` filter, n=5 expansion, 0.7/0.3 weighting, ~20→7 rerank. A concrete, copyable RAG recipe.
- **"Think & Plan" as a tool-selection fix** — a named, transferable pattern for when an agent's tool count grows and tool domains overlap.
- **Resume-from-failed-node + user-initiated retry** — concrete resilience UX: persisted state lets a retry skip already-completed steps, saving cost and latency.
- **Confidence-score quarantine for NER metadata** — a reusable pattern for automated data enrichment under a human-review safety net.
- **Removing the LLM-review-of-SQL step** — a useful counter-example: an extra reflection layer was net-negative because it false-flagged valid queries; not every reflection loop earns its place.
- **Context routing per agent** (schema-only for SQL, question+evidence for Reflection, curated chunks for Writer) — a concrete instantiation of context engineering.

## Constraints / Caveats

- **No quantitative outcome metrics disclosed.** The article reports qualitative improvements ("dramatic improvement in tool-selection accuracy," "promising results") but no benchmark numbers, baselines, or eval scores. The companion *Frontiers* paper is said to cover business impact — not captured here.
- **Vendor/practitioner genre.** A Thoughtworks consultant writing about a Thoughtworks+Bayer build. High engineering credibility, but it is a success-narrative case study, not independent evaluation.
- **Some architecture is aspirational.** Domain-specific sub-agents and the Writer's internal review loop are described as "proposed," "actively evolving," or "supports extending" — i.e. design intent / in-progress, not necessarily shipped. The NER metadata pipeline is "actively working on integrating."
- **Specific values are setup-specific.** The 0.7/0.3 weighting, n=5 expansion, top-7 rerank, 50-row cap, and 3-retry limit were tuned for this corpus; treat as reasonable defaults to test, not universal constants.
- **Regulated-domain framing.** Conclusions about needing explicit harness control are explicitly scoped to enterprise research where trust/traceability/reviewability matter; the author allows that harness layers may thin as models improve.

## Design Implications

- **For any enterprise agentic-RAG build:** adopt the three-reflection-loop separation (process / data / draft) rather than a single monolithic "reflect" step — it localizes failures (bad trajectory vs thin evidence vs incomplete draft) and makes each agent independently evaluable.
- **For [[concepts/ai-agents/harness-engineering|harness engineering]]:** treat orchestration (LangGraph-style), state persistence, multi-level retries, provider fallbacks, and observability as first-class, not afterthoughts. They are what makes an agent "less opaque and more reliable than an unconstrained autonomous agent."
- **For context engineering / [[concepts/ai-agents/context-rot|context discipline]]:** route the minimal relevant context to each agent; large windows are not a license to dump everything. This improves steerability, debuggability, and eval-ability.
- **For [[concepts/infrastructure-dev/domain-adaptation|domain adaptation]]:** as tool/domain count grows, move from one Researcher with a flat tool list toward domain sub-agents (each owning toolset + schema knowledge) with a routing coordinator.
- **For [[concepts/ux-research/human-in-the-loop|human-in-the-loop]] trust:** granular citations (page + exact quote) and visible intermediate steps are the trust primitives; pair automation with a confidence-score quarantine for anything that writes back to a system of record.
- **For [[concepts/infrastructure-dev/enterprise-ai-infrastructure|enterprise AI infrastructure]]:** a unified OpenAI-compatible gateway over multiple providers makes model-swapping and fallbacks tractable and centralizes rate-limiting/abuse controls.

## Tensions

- **Add reflection vs avoid over-engineering.** Three reflection loops were valuable, yet the LLM-review-of-SQL loop was removed for false-flagging valid queries. Reflection helps until it adds latency/noise without accuracy — each loop must earn its place. (Mirrors Böckeler's "feedback overload" worry in [[sources/fowler-sensors-coding-agents|the sensors article]].)
- **Large context windows vs context discipline.** The industry trend is bigger windows; PRINCE's lesson is that selectivity still matters for steerability and evaluation.
- **Monolithic agent (simple) vs domain sub-agents (coherent but more moving parts).** The "one researcher" UX is simple for users but hard to maintain as domains multiply; the proposed hierarchy trades internal complexity for per-domain coherence.
- **Accuracy-first vs cost.** The team deliberately optimized accuracy before cost, accepting higher early cost — a sequencing choice others under budget pressure may not be able to make.
- **Harness permanence vs model progress.** The author concedes some harness layers may move into native model capability over time, yet argues explicit control stays essential in regulated settings — an unresolved, context-dependent boundary.

## Open Questions

- What are the actual quantitative outcomes (accuracy, latency, adoption, researcher time saved)? The captured article gives none; the *Frontiers* paper would need ingesting.
- Which reflection loops generalize beyond this domain, and how do you decide when a loop is net-negative (as the SQL-review loop was)?
- How far has the domain-sub-agent architecture actually shipped vs remained a proposal?
- How are the retrieval hyperparameters (0.7/0.3, n=5, top-7) expected to shift across domains or corpora?
- How is the NER confidence threshold for auto-update vs quarantine set and calibrated against ground truth?
- As models gain native planning/reflection, which parts of this harness would Bayer remove first?

## Concepts Linked

- [[concepts/ai-agents/harness-engineering|Harness Engineering]] — the orchestration/recovery/observability scaffolding around the models; this is the article's primary lens.
- [[concepts/ai-agents/model-harness|Model Harness]] — the product/system scaffolding (tools, state, retries, fallbacks) PRINCE builds around the LLMs.
- [[concepts/ai-agents/agentic-ai|Agentic AI]] — PRINCE is a multi-agent (Researcher/Reflection/Writer) agentic RAG system.
- [[concepts/ai-agents/long-horizon-tasks|Long-Horizon Tasks]] — multi-step (the article cites a 50-step scenario) workflows requiring process reflection and trajectory checks.
- [[concepts/ai-agents/autonomous-ai-agent|Autonomous AI Agent]] — contrasted against: the bounded harness is "more reliable than an unconstrained autonomous agent."
- [[concepts/ai-agents/product-evals|Product Evals]] — RAGAS dataset + daily live-traffic evaluation, multi-stage (testing-pyramid) evaluation.
- [[concepts/ux-research/ai-evals|AI Evals]] — Faithfulness / Answer Relevancy / Context Relevancy / Answer Accuracy / Semantic Similarity metrics.
- [[concepts/ai-agents/context-rot|Context Rot]] — the "context discipline" argument against over-stuffing prompts even with large windows.
- [[concepts/infrastructure-dev/domain-adaptation|Domain Adaptation]] — domain-specific sub-agents owning their own tools, schemas, and prompt instructions.
- [[concepts/ux-research/human-in-the-loop|Human-in-the-Loop]] — citations, intermediate-step transparency, and confidence-score quarantine for trust.
- [[concepts/infrastructure-dev/enterprise-ai-infrastructure|Enterprise AI Infrastructure]] — unified OpenAI-compatible multi-provider gateway, state stores, observability.
- [[concepts/ai-agents/agentic-rag|Agentic RAG]] (new) — agentic Retrieval-Augmented Generation: an orchestrated multi-agent RAG loop (plan → retrieve → reflect → write) rather than single-shot retrieve-then-generate.
- [[concepts/ai-agents/context-engineering|Context Engineering]] (new) — deliberately shaping and routing the right context to the right agent/step (distinct from prompt engineering and from harness engineering).
- (new) concepts/ai-agents/reflection-loops — process/data/draft reflection as a design taxonomy for self-correcting agentic workflows.
- (new) concepts/ai-agents/text-to-sql — natural-language-to-SQL retrieval with schema injection, few-shot, validation, and self-correcting retries.
- (new) concepts/ai-agents/hybrid-retrieval — combining metadata filtering + semantic (kNN) + keyword search with weighted scoring and reranking.

## LLM Use

- **Use for:** designing reliable enterprise agentic-RAG systems; justifying harness components (orchestration, state persistence, multi-level retries, provider fallbacks, observability); the three-reflection-loop pattern; concrete hybrid-retrieval and Text-to-SQL recipes; framing context engineering vs harness engineering; trust mechanisms (granular citations, intermediate-step transparency, confidence-score quarantine) in regulated domains.
- **Do not use for:** quoting performance/accuracy numbers (none are given) or claiming proven ROI; treating the proposed domain-sub-agent architecture or Writer review loop as definitely shipped; treating the specific hyperparameters (0.7/0.3, n=5, top-7, 50-row, 3-retry) as universal.
- **Best prompt pattern:** "Using the PRINCE case study's context-engineering + harness-engineering lens, design (or critique) an agentic-RAG system with explicit process/data/draft reflection loops. For each loop, state what it checks, what context it needs, and how it self-corrects — then flag where a loop might be net-negative."

## Reliability Notes

> [!warning] Caveats
> - **Practitioner/vendor case study** (Thoughtworks consultant, Thoughtworks+Bayer build). High engineering credibility; not independent evaluation. Confidence **0.9** on the architecture and engineering patterns (these are described in concrete detail), lower (~0.6) on any implied outcomes since no metrics are disclosed.
> - **No quantitative results** in the captured article; the companion *Frontiers in Artificial Intelligence* paper (10.3389/frai.2025.1636809) would be needed for business-impact claims.
> - **Aspirational components** (domain sub-agents, Writer review loop, NER pipeline integration) are partly proposed/in-progress — do not cite as shipped without verification.
> - Retrieval hyperparameters are corpus-tuned; treat as starting points, not constants.

## Backfill Status

- Newly written 2026-06-22 from a full web capture (article read end-to-end via persisted fetch). All sections populated. No prior thin version to upgrade. `coverage: substantial` (deep read of the engineering article; the companion peer-reviewed paper and quantitative outcomes remain un-ingested).
