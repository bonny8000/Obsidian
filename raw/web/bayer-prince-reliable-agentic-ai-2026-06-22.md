---
source_url: https://martinfowler.com/articles/reliable-llm-bayer.html
captured: 2026-06-22
title: Building Reliable Agentic AI Systems
authors: [Sarang Sanjay Kulkarni]
published: 2026-06-16
publisher: martinfowler.com
---

# Building Reliable Agentic AI Systems

**Authors:** Sarang Sanjay Kulkarni (Principal Consultant, Thoughtworks), with the Bayer team (Adam Zalewski, Annika Kreuchwig, Carlos Henrique Vieira-Vieira, Jobst Löffler, Jonas Münch)
**Published:** 2026-06-16 — martinfowler.com

> Immutable capture. AI-written summary, key points, and short quoted excerpts only — no full article text. See the source URL for the complete article.

## Summary

This is a Thoughtworks engineering case study of PRINCE (Preclinical Information Center), a cloud-hosted agentic AI platform built by Bayer AG with Thoughtworks to let pharmaceutical researchers query decades of preclinical safety-study knowledge buried in structured metadata and unstructured PDF reports. The platform is presented as an evolution across three phases — **Search** (a unified, metadata-driven gateway over thousands of nonclinical study reports), **Ask** (RAG-based natural-language question answering over unstructured PDFs, including scanned historical documents), and **Do** (a multi-agent active research assistant that orchestrates workflows and drafts regulatory documents). PRINCE has been live to end users since early 2024, with the agentic integration added later that year.

The article reframes the system's engineering through two lenses the team did not name at design time: **context engineering** (what information each model receives, what it does not, and how context moves between specialized steps) and **harness engineering** (the scaffolding around the models: orchestration, tool boundaries, state persistence, retries, fallbacks, validation, reflection loops, observability, and human review). The architecture is orchestrated with **LangGraph** and served via **FastAPI**, with a React conversational UI. It coordinates a **Researcher Agent**, **Reflection Agent**, and **Writer Agent** through a multi-stage workflow: Clarify User Intent → Think & Plan → Research (RAG + Text-to-SQL) → data-sufficiency validation → answer generation.

A central design theme is **context discipline**: larger context windows did not remove the need to be selective. Rather than treat the prompt as one big container, each stage receives only its relevant slice — planning context for Think & Plan, retrieval context for the Researcher, evidence context for the Reflection Agent, and synthesis context for the Writer. The system implements **three complementary reflection loops**: process reflection (Think & Plan — is the trajectory/tool choice/sequencing right?), data reflection (Reflection Agent — is the retrieved evidence sufficient and relevant?), and draft reflection (a Writer review loop — is the generated output complete, with no missing sections or inconsistent tables?).

Retrieval uses a **hybrid pipeline**: an LLM extracts keywords and a metadata filter (e.g. `eq(study_id, T123456-2)`) concurrently; a smaller fast model performs query expansion (n=5 paraphrases); a weighted hybrid search (0.7 semantic kNN / 0.3 keyword) runs in parallel over the metadata-filtered space to retrieve ~20 candidate chunks; a cross-encoder reranker (bge-reranker-large) narrows to the top 7; the final prompt grounds the answer with automatic citations. Text-to-SQL handles structured queries against Amazon Athena with dynamic schema injection, dynamic few-shot prompting from a semantic-layer example store, SELECT-only validation, a 50-row result cap, and up to 3 self-correcting retries on SQL errors.

The piece also covers **trust and resilience** mechanisms: granular hover-level citations (page number + exact quote), visible intermediate steps, RAGAS-based evaluation (daily live-traffic eval plus dataset eval on major changes), Langfuse observability, multi-provider LLM fallbacks, retries at both LLM-call and node level, state persistence (LangGraph checkpointer → Postgres for agent state, DynamoDB for app state), and a NER-driven metadata-correction utility with a confidence-score quarantine (high-confidence fields auto-update Athena; low-confidence fields are flagged for human review). The broader lesson: production-ready agentic AI comes not from better models or prompts alone but from engineering both the context the model sees and the harness within which it acts — and in regulated research, explicit control over context, state, recovery, reflection, and verification remains essential.

## Key Points

- **Search → Ask → Do evolution.** Search = unified metadata gateway over siloed reports; Ask = RAG over unstructured PDFs (incl. scanned historical docs); Do = multi-agent assistant that orchestrates tasks and drafts regulatory documents.
- **Stack:** LangGraph orchestration + FastAPI backend + React UI. Vector store in Amazon OpenSearch; structured data via Amazon Athena; agent state in PostgreSQL (LangGraph checkpointer), app-level state in DynamoDB; S3 data lake for source PDFs.
- **Three specialized agents:** Researcher (gathers evidence via RAG + Text-to-SQL), Reflection (validates data sufficiency), Writer (synthesizes the cited final answer).
- **Three reflection loops:** process reflection (Think & Plan — right trajectory/tool/sequence), data reflection (Reflection Agent — sufficient evidence), draft reflection (Writer review — complete output).
- **Context discipline / context engineering:** route the right context to the right agent at the right time, not one big prompt. Text-to-SQL injects only relevant schema; Reflection Agent gets question + evidence (not full history); Writer gets curated chunks + citation constraints (not raw retrieval). Moving from a monolith to this structured workflow let each agent be evaluated, debugged, and improved in isolation.
- **Hybrid retrieval pipeline:** keyword extraction + concurrent metadata-filter generation + query expansion (n=5) + parallel weighted hybrid search (0.7 semantic kNN / 0.3 keyword) → ~20 chunks → cross-encoder rerank (bge-reranker-large) → top 7 → grounded answer with automatic citations. Metadata pre-filtering shrinks the search space from millions of vectors to tens–hundreds.
- **Text-to-SQL:** dynamic relevant-schema injection; dynamic few-shot examples retrieved from a semantic-layer vector collection; always include study ID/title columns; SELECT-only validation (DELETE/INSERT/UPDATE blocked); 50-record cap; up to 3 error-feedback self-correction retries. An earlier LLM-review-of-SQL step was removed because it flagged valid queries.
- **Think & Plan ("thinking space," inspired by Anthropic's Think tool):** dramatically improved tool-selection accuracy as the tool count grew and domain boundaries overlapped; enables multi-step orchestration where one tool's output informs the next.
- **Harness engineering for resilience:** retries at LLM-call and node level; error context passed back so agents can re-plan; state persistence enables resume-from-failed-node and user-initiated retries that skip completed steps; LLM fallbacks across providers (internal GenAI platforms expose OpenAI/Anthropic/Google/open-source models behind a unified OpenAI-compatible endpoint); LangGraph as the control layer defining who can act, which tools, where to pause.
- **Trust:** granular citations (hover any sentence → link to source doc, page number, exact quote), visible intermediate steps/queries/tools, and human-in-the-loop. Regulatory drafts are always for expert review; final submissions authored/approved by qualified personnel.
- **Evaluation & monitoring:** RAGAS metrics (Faithfulness, Answer Relevancy, Context Relevancy, Answer Accuracy, Semantic Similarity); dataset eval on major workflow/prompt/model changes; live-traffic eval daily as a batch job; CloudWatch for system health; Langfuse for traces and eval data. Evaluate at multiple workflow stages (testing-pyramid analogy), not just end-to-end.
- **Data quality via NER:** a utility reads study PDFs to extract entities (study IDs, compounds, species, routes, dosages, clinical findings) and generate annotations; a confidence-score system auto-updates Athena for high-confidence fields and quarantines low-confidence fields for human review.
- **Evolving toward domain-specific sub-agents:** a flat tool list on one Researcher becomes unmanageable as domains (toxicology, pharmacology) grow; the proposed architecture gives each domain its own toolset (e.g. tox RAG + tox metadata SQL) and prompt instructions, with the top-level Researcher acting as a router/coordinator.
- **Iterative philosophy:** ship early for feedback; optimize for accuracy/performance first (even at higher cost), optimize cost only after accuracy is achieved.

## Short Quoted Excerpts

- "Reliability comes from engineering both the context the model sees and the harness within which the model acts."
- "PRINCE therefore avoids treating the prompt as one large container for all available information."
- "This gives PRINCE three complementary reflection loops. Process reflection checks whether the workflow is on the right path... Data reflection checks whether the gathered evidence is sufficient... Draft reflection checks whether the generated output is complete."
- "It routes the right context to the right capability at the right time."
- "As model capabilities improve, some parts of today's harness may become thinner or move into native model capabilities. But in enterprise research systems, especially where trust, traceability, and reviewability matter, explicit control over context, workflow state, recovery, reflection, and verification remains essential."

## Provenance Notes

- Primary source: Thoughtworks/martinfowler.com engineering case study (published 16 June 2026).
- A companion peer-reviewed paper in *Frontiers in Artificial Intelligence* (10.3389/frai.2025.1636809) covers product evolution and business impact in more detail.
- The author notes AI assistance was used for brainstorming, outlining, and language polishing during writing. Disclaimer: all activities conform to Bayer's data-governance and external-communication policies and do not constitute regulatory claims.
