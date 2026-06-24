---
source_url: https://www.langchain.com/blog/exa
captured: 2026-06-22
title: "How Exa built a Web Research Multi-Agent System with LangGraph and LangSmith"
authors: [The LangChain Team]
published: 2025-06-30
publisher: LangChain Blog
---

# How Exa built a Web Research Multi-Agent System with LangGraph and LangSmith

**Author / Company:** The LangChain Team (case study featuring Exa; quote from Mark Pekala, Software Engineer at Exa) **Published:** 2025-06-30 — LangChain Blog (Case Studies / Agent Architecture); ~4 min read

> Immutable capture. AI-written summary, key points, short quoted excerpts, and diagram content from surrounding text only — no full article text. See the source URL for the complete article.

## Summary

A LangChain **case study** on how **Exa** — known for its high-quality search API — built a production-ready **multi-agent web research system on LangGraph**, with **LangSmith** for observability. Exa's newest product is a **deep research agent** that "autonomously explores the web until it finds the structured information users need." It processes **hundreds of research queries daily**, returning structured results in **15 seconds to 3 minutes** depending on complexity.

The post frames Exa's path as an **evolution to agentic search**: Exa started with a **search API**, added an **answers endpoint** (LLM reasoning + search results), and arrived at a **deep research agent** — "their first truly agentic search API." LangChain generalizes this as an industry trend (RAG → Deep Research; coding auto-complete → Q&A → async long-running coding agents), and notes that the answers endpoint used **no framework**, but as the architecture grew more complex Exa re-evaluated and **chose LangGraph** — "as architectures get more complex, LangGraph increasingly becomes the framework of choice." (LangChain and Exa were prior partners via a popular open-source integration but had not collaborated on a product until now.)

**Architecture (multi-agent, entirely on LangGraph):** (1) **Planner** — analyzes the research query and **dynamically generates multiple parallel tasks**; (2) **Tasks** — independent research units that use specialized tools and reasoning; (3) **Observer** — maintains **full context** across all planning, reasoning, outputs, and citations. A key **context-engineering** choice: while the **Observer has full visibility**, individual **Tasks receive only the final cleaned outputs of other tasks, not intermediate reasoning states**. Unlike rigid workflows, the system **dynamically adjusts the number of tasks** to the query's complexity; each task gets specific instructions, a **required output format (always JSON schema)**, and access to specialized Exa API tools.

The post says many design choices **mirror Anthropic's multi-agent research system** (intentionally — the Exa team read and drew learnings from that post). Two highlighted insights: (a) **Search snippets vs full results** — the system first reasons over **search snippets** and only requests **full page content** when snippet-level reasoning is insufficient, "significantly reduc[ing] token usage while preserving research quality" (this snippet/full-content swap is powered by the Exa API); (b) **Structured output** — the agent maintains **structured JSON at every level** (format specified at runtime, generated via **function calling**), driven by the fact that Exa designed the system for **API consumption** rather than a consumer-facing chat tool, where a reliable output format is more critical.

**Observability:** the most critical LangSmith feature for Exa was observability, **especially around token usage** — quoted: *"The observability – understanding the token usage – that LangSmith provided was really important. It was also super easy to set up."* (Mark Pekala). Visibility into **token consumption, caching rates, and reasoning-token usage** informed Exa's **production pricing models** and cost-effective performance at scale. Closing **takeaways for teams**: (1) start with observability (token tracking/visibility is critical for production); (2) design for reusability (well-architected flows power multiple products); (3) prioritize structured output (API consumers need parseable results); (4) dynamic task generation (flexible task creation scales better than rigid workflows). Links to LangGraph docs and exa.ai.

## Key Points

- **Exa** = high-quality search API company; new product = a **deep research agent** that autonomously explores the web for **structured** info. **Hundreds of queries/day**; **15 s–3 min** to structured results by complexity. Built on **LangGraph**; observability via **LangSmith**.
- **Evolution to agentic search:** search API → **answers endpoint** (LLM reasoning + search) → **deep research agent** ("first truly agentic search API"). Mirrors the industry shift RAG → Deep Research (and auto-complete → Q&A → async coding agents).
- **Framework choice:** the answers endpoint used **no framework**; as the deep-research architecture got more complex, Exa re-evaluated and **chose LangGraph**. LangChain frames this as a recurring pattern ("as architectures get more complex, LangGraph increasingly becomes the framework of choice"). Prior partners via a popular open-source LangChain↔Exa integration; first product collaboration.
- **Multi-agent architecture (all on LangGraph), 3 roles:**
  - **Planner** — analyzes the query, **dynamically generates multiple parallel tasks**.
  - **Tasks** — independent research units with specialized tools + reasoning; each gets specific instructions, a **required JSON-schema output format**, and access to **specialized Exa API tools**.
  - **Observer** — maintains **full context** across all planning, reasoning, outputs, citations.
- **Intentional context engineering:** Observer has **full visibility**; individual Tasks receive **only the final cleaned outputs** of other tasks, **not intermediate reasoning states** (selective context isolation between peers, full context at the supervisor).
- **Dynamic scaling, not rigid workflows:** the system adjusts the **number of tasks** to query complexity, scaling from single-task to many parallel investigations.
- **Mirrors Anthropic's multi-agent research system** by design — the Exa team read that post and drew learnings; the case study lists their build-on-top insights.
- **Insight A — Search Snippets vs Full Results:** reason on **snippets first**, request **full page content only when snippets are insufficient** → "significantly reduces token usage while preserving research quality." Snippet/full-content swap **powered by the Exa API**.
- **Insight B — Structured Output:** **structured JSON at every level**, format **specified at runtime**, generated via **function calling**. Chosen because Exa built for **API consumption** (not consumer chat), where reliable/parseable output is critical.
- **Observability (LangSmith):** most critical feature was **observability, especially token usage** — "super easy to set up." Visibility into **token consumption, caching rates, reasoning-token usage** informed **production pricing models** and cost-effective scale.
- **Takeaways for teams building similar systems:** (1) **start with observability** (token tracking/system visibility critical for production); (2) **design for reusability** (well-architected flows power multiple products); (3) **prioritize structured output** (API consumers need reliable, parseable results); (4) **dynamic task generation** (flexible creation scales better than rigid workflows).
- **Quoted excerpt:** "The observability – understanding the token usage – that LangSmith provided was really important. It was also super easy to set up." — Mark Pekala, Software Engineer at Exa.

## Diagrams (content from text/captions)

The post embeds the article hero image and **one in-body architecture diagram** (`...Diagram.png`), plus related-post thumbnails — all bare `![]` images with **no alt text or caption**.

- **Exa research-agent architecture diagram** (`69cbaaabbf847dfe35ef4847_Diagram.png`, placed after the "Multi-agent architecture design" section): no caption. Content recoverable from surrounding prose — it depicts the **Planner → parallel Tasks → Observer** topology: a **Planner** that dynamically spawns multiple **parallel Task** units (each with its own instructions, JSON-schema output format, and specialized Exa API tools), and an **Observer** that maintains full context across all planning/reasoning/outputs/citations. The intentional context-engineering detail — Tasks see only other tasks' **final cleaned outputs**, not intermediate reasoning, while the Observer sees everything — is the key flow the diagram likely encodes. Exact boxes/arrows/labels are **not pixel-parsed**; reconstruction is from the article text. No metrics/eval charts present as image-only content.
