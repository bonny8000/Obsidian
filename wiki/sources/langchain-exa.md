---
type: source
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [agentic-search, multi-agent, web-research-agent, context-engineering, structured-output, token-efficiency, langgraph, observability, langchain]
source_path: raw/web/langchain-exa-2026-06-22.md
source_url: https://www.langchain.com/blog/exa
authors: [The LangChain Team]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.78
---

# How Exa Built a Web Research Multi-Agent System (Planner / Tasks / Observer on LangGraph)
**Author:** The LangChain Team (case study; quote from Mark Pekala, Exa) — **Published:** 2025-06-30 — LangChain Blog (Case Studies)
**Raw capture:** [[raw/web/langchain-exa-2026-06-22|langchain-exa-2026-06-22]]
**URL:** [langchain.com/blog/exa](https://www.langchain.com/blog/exa)

## Citation

The LangChain Team. (2025, June 30). *How Exa built a Web Research Multi-Agent System with LangGraph and LangSmith.* LangChain Blog (Case Studies). Captured 2026-06-22 into `raw/web/langchain-exa-2026-06-22.md`. Notes design choices that "mirror" Anthropic's "Building a multi-agent research system" engineering post; quote from Mark Pekala, Software Engineer at Exa.

## Summary

A LangChain **case study** on how **Exa** — a high-quality search-API company — built a production **multi-agent web research system on LangGraph**, observed via **LangSmith**. Exa's newest product is a **deep research agent** that "autonomously explore[s] the web until it finds the structured information users need," handling **hundreds of queries per day** and returning structured results in **15 seconds to 3 minutes** by complexity. The post frames Exa's trajectory as an **evolution to agentic search**: search API → an **answers endpoint** (LLM reasoning + search) → a **deep research agent** ("their first truly agentic search API") — generalized as the industry trend RAG → Deep Research (and coding auto-complete → Q&A → async long-running agents). It also tells a **framework-adoption story**: the answers endpoint used **no framework**, but as the architecture grew complex Exa re-evaluated and **chose LangGraph**, which LangChain frames as a recurring pattern ("as architectures get more complex, LangGraph increasingly becomes the framework of choice").

The architecture is a **three-role multi-agent pattern built entirely on LangGraph**: a **Planner** that analyzes the query and **dynamically generates multiple parallel tasks**; independent **Tasks** that run specialized tools + reasoning (each receiving specific instructions, a **required JSON-schema output format**, and access to specialized Exa API tools); and an **Observer** that maintains **full context** across all planning, reasoning, outputs, and citations. The standout idea is **intentional context engineering**: the Observer has full visibility, but individual Tasks receive only the **final cleaned outputs** of other tasks — **not** their intermediate reasoning — so peers stay context-isolated while a supervisor retains the whole picture. The number of tasks **scales dynamically** with query complexity rather than following a rigid workflow.

Two design insights are explicitly borrowed from **Anthropic's multi-agent research system** (the Exa team read and built on it): (a) **search snippets vs full results** — reason over snippets first and fetch full page content only when snippets are insufficient, "significantly reduc[ing] token usage while preserving research quality" (the snippet/full swap is powered by the Exa API); and (b) **structured output** — structured **JSON at every level**, format specified at runtime via **function calling**, because Exa designed for **API consumption** (not consumer chat), where parseable output is critical. On tooling, the most valued **LangSmith** capability was **observability of token usage** ("super easy to set up," per Mark Pekala), giving visibility into **token consumption, caching rates, and reasoning tokens** that informed Exa's **production pricing**. Closing takeaways: start with observability; design for reusability; prioritize structured output; prefer dynamic task generation over rigid workflows.

This is the wiki's clearest worked example of a **production agentic web-search / deep-research system**, and a direct companion to [[sources/langchain-multi-agent-architecture|Multi-Agent Architecture]] (Exa's Planner-as-supervisor + parallel Tasks is essentially the "Subagents/Router with context isolation" pattern made real) and [[sources/langchain-box-ai-deep-agents|Box Deep Agents]] (another dynamic-spawn-plus-synthesis enterprise build). Its context-engineering and structured-output choices connect to [[concepts/infrastructure-dev/token-efficiency|token efficiency]] and agentic RAG; how you'd *test* such a system is covered by [[sources/langchain-evaluating-deep-agents|Evaluating Deep Agents]], and it shares the agentic-retrieval theme with [[sources/bayer-prince-reliable-agentic-ai|Bayer PRINCE]].

## Key Claims

- **Exa shipped a deep research agent** that autonomously explores the web for **structured** info; **hundreds of queries/day**; **15 s–3 min** to structured results by complexity. Built **entirely on LangGraph**; observed via **LangSmith**.
- **Evolution to agentic search:** search API → **answers endpoint** (LLM reasoning + search) → **deep research agent** ("first truly agentic search API"). Mirrors RAG → Deep Research industry-wide.
- **Framework adoption:** answers endpoint used **no framework**; growing complexity led Exa to **choose LangGraph**. (Prior LangChain↔Exa open-source integration; first product collaboration.)
- **Three-role architecture (all LangGraph):** **Planner** (analyzes query, dynamically generates parallel tasks) · **Tasks** (independent research units; specialized tools + reasoning; each gets instructions, a required **JSON-schema** output, specialized Exa API tools) · **Observer** (maintains **full context** across planning/reasoning/outputs/citations).
- **Intentional context engineering:** Observer has full visibility; **Tasks receive only other tasks' final cleaned outputs, not intermediate reasoning states** → peer context isolation + supervisor full-context.
- **Dynamic, not rigid:** the **number of tasks scales with query complexity**, from single-task to many parallel investigations.
- **Mirrors Anthropic's multi-agent research system** by design; the post lists Exa's build-on-top insights.
- **Search snippets vs full results:** reason over **snippets first**, fetch **full content only when insufficient** → "significantly reduces token usage while preserving research quality"; swap **powered by the Exa API**.
- **Structured output:** structured **JSON at every level**, runtime-specified format via **function calling**, because the system targets **API consumption** (reliable/parseable output critical) rather than consumer chat.
- **Observability (LangSmith):** most critical feature = **token-usage observability** ("super easy to set up"); visibility into **token consumption, caching rates, reasoning-token usage** informed **production pricing models** and cost-effective scale.
- **Takeaways:** (1) start with observability; (2) design for reusability (one well-architected flow → multiple products); (3) prioritize structured output; (4) dynamic task generation scales better than rigid workflows.

## Useful Examples

- **The Planner / Tasks / Observer pattern** — a transferable web-research-agent topology: a supervisor that dynamically fans out parallel research tasks, with a separate context-keeper across the whole run. A concrete instance of supervisor-mediated multi-agent (cf. the Subagents/Router patterns in [[sources/langchain-multi-agent-architecture|Multi-Agent Architecture]]).
- **Selective inter-task context** — Tasks see only peers' **final cleaned outputs**, not intermediate reasoning, while the Observer sees everything. A reusable rule for cutting cross-agent token cost and noise without losing global coherence.
- **Snippet-first, full-content-on-demand retrieval** — reason on search snippets and escalate to full page crawl only when snippets are insufficient; a concrete token-efficiency lever for agentic search (powered here by the Exa API's swap capability).
- **JSON-schema output at every level via function calling** — designing the agent for **API consumption** (format specified at runtime) rather than free-text reports, when downstream consumers need parseable results.
- **Dynamic task count tied to query complexity** — scale parallelism to the problem instead of a fixed workflow; the lever that lets one system serve simple single-task and complex multi-faceted queries.
- **Token-usage observability driving pricing** — using LangSmith visibility into token consumption / caching / reasoning tokens to set production **pricing models** — a build-to-business-model bridge for API products.

## Constraints / Caveats

- **Vendor + customer case-study genre.** A LangChain blog about an Exa product built on LangGraph/LangSmith — promotional on both sides. Likely a partner/integration piece (LangChain and Exa are long-standing integration partners). Treat as a credible architecture sketch, not independent evaluation; **note the vendor lens** (confidence 0.78).
- **Only operational metrics, no quality metrics.** The figures given are **hundreds of queries/day** and **15 s–3 min** latency. There are **no** accuracy, citation-precision, hallucination, token-cost, or user-satisfaction numbers — the "significantly reduces token usage while preserving research quality" claim is unquantified.
- **"Mirrors Anthropic's system" is by the authors' own account** — design lineage is asserted, with no head-to-head comparison or independent validation of which choices mattered.
- **Architectural depth is moderate.** Planner/Tasks/Observer roles and the context rule are described, but error handling, retries, task-failure recovery, citation generation mechanics, and how the Observer arbitrates conflicting task outputs are not detailed.
- **Short post (~4 min).** Higher-level than the Box or Verifiers pieces; several specifics (e.g. how dynamic task count is decided) are stated, not shown.

## Design Implications

- **For [[concepts/ai-agents/agentic-rag|agentic RAG]] / web research:** prefer a **Planner → parallel Tasks → Observer** shape over a rigid pipeline; let the planner size parallelism to query complexity and keep a full-context supervisor for coherence and citations.
- **For [[concepts/infrastructure-dev/token-efficiency|token efficiency]]:** adopt **snippet-first retrieval** (escalate to full content only when needed) and **selective inter-agent context** (share final cleaned outputs, not intermediate reasoning) — two independent levers that cut tokens without obvious quality loss.
- **For API-consumed agents:** enforce **structured JSON output at every level** via function calling with a runtime-specified schema; reliability of format matters more than prose quality when the consumer is another system.
- **For [[concepts/ai-agents/multi-agent-architecture|multi-agent architecture]]:** Exa validates the supervisor-mediated, context-isolated pattern in production — coordination is engineered (Planner orchestrates, peers isolated), not negotiated, consistent with "engineer the coordination" guidance.
- **For [[concepts/ai-agents/mcp-integration|tool/integration design]]:** expose retrieval as **specialized API tools** to each task (snippet vs full-content as a first-class capability) so token/latency tradeoffs are controllable per task rather than hardcoded.
- **For productionizing:** **start with observability** — instrument token consumption, caching, and reasoning tokens early; it both stabilizes the system and can directly inform pricing.

## Tensions

- **Snippet-first efficiency vs research completeness.** Reasoning on snippets saves tokens but risks missing detail that only full-page content reveals; "preserving research quality" is asserted, not measured, so the snippet/full threshold is an unquantified quality–cost tradeoff.
- **Context isolation (peers see only cleaned outputs) vs cross-task awareness.** Hiding intermediate reasoning cuts tokens/noise but can prevent a task from catching another's error or reusing a useful partial — the Observer is the only safeguard, and its arbitration is undescribed.
- **Dynamic task generation (flexibility) vs predictability/cost control.** Sizing task count to query complexity scales gracefully but makes per-query cost and latency variable and harder to bound — relevant since the same post leans on token observability for pricing.
- **Structured-JSON-everywhere vs expressiveness.** Always-structured output is ideal for API consumers but can constrain open-ended research synthesis that a free-text report might capture better — Exa accepts this because it built for API consumption, not human chat.
- **Vendor framing vs independent evidence.** "LangGraph increasingly becomes the framework of choice" and "mirrors Anthropic's great system" are persuasive narrative; neither is independently substantiated here.

## Open Questions

- What are the **quality outcomes** (answer accuracy, citation precision, hallucination rate, completeness) of Exa's deep research agent? None are disclosed — only throughput and latency.
- **How much** does snippet-first retrieval actually save, and what is the **quality cost** at the snippet→full-content threshold? ("Significantly reduces token usage while preserving research quality" is unquantified.)
- How does the **Planner decide the number of tasks**, and how is that decision evaluated/bounded for cost and latency?
- How does the **Observer arbitrate conflicting or low-quality Task outputs**, and how are citations generated and attributed across parallel tasks?
- What are the **failure-handling semantics** (task timeout/error/retry) in a system promising 15 s–3 min responses at hundreds/day?
- **Image gap:** the in-body architecture diagram (`...Diagram.png`) is a bare `![]` with no alt text or caption; its exact Planner→Tasks→Observer boxes/arrows and the precise context-flow (which outputs cross between tasks vs to the Observer) are not text-recoverable beyond the prose reconstruction. No metric/eval charts are present as image-only content.

## Concepts Linked

- [[concepts/ai-agents/agentic-rag|Agentic RAG]] — an agentic web-research/retrieval system: plan → parallel search Tasks → synthesis, evolved from RAG toward Deep Research.
- [[concepts/ai-agents/multi-agent-architecture|Multi-Agent Architecture]] — the Planner (supervisor) + parallel Tasks + Observer is a concrete supervisor-mediated, context-isolated multi-agent design.
- [[concepts/ai-agents/mcp-integration|MCP / Tool Integration]] — Tasks call **specialized Exa API tools** (incl. snippet-vs-full-content swap) as their action surface; relevant to how agents consume external retrieval tools.
- [[concepts/ai-agents/ai-news-intermediary|AI News Intermediary]] — an autonomous web-research agent that retrieves, synthesizes, and structures web information sits in the same space as AI intermediaries that mediate access to web content/news.
- [[concepts/infrastructure-dev/token-efficiency|Token Efficiency]] — snippet-first retrieval and share-only-cleaned-outputs context engineering as token-reduction levers; LangSmith token-usage observability.
- [[concepts/ai-agents/long-horizon-tasks|Long-Horizon Tasks]] — a long-running, multi-step research agent (15 s–3 min, many parallel tasks) tackling complex web-research queries.
- [[concepts/ai-agents/agentic-search|Agentic Search]] (new) — autonomous, agent-driven web search that plans, runs multiple parallel retrieval tasks, and returns structured findings (the "search API → answers → deep research agent" evolution), as opposed to single-shot search or static RAG.

## LLM Use

- **Use for:** designing agentic web-research / deep-research systems (Planner/Tasks/Observer); supervisor-mediated multi-agent with selective inter-task context; snippet-first-then-full-content retrieval as a token lever; structured-JSON-output-for-API-consumption design; using token observability to inform pricing; the "no framework → LangGraph as complexity grows" adoption narrative.
- **Do not use for:** quoting quality/accuracy outcomes (none given — only throughput/latency); quantifying the token savings or the snippet/full-content quality tradeoff; treating "mirrors Anthropic" as validated equivalence; describing Exa's error handling or Observer arbitration (undetailed); citing the post as independent (it is a partner/vendor case study).
- **Best prompt pattern:** "Using Exa's Planner/Tasks/Observer design, sketch an agentic web-research system: how the Planner sizes parallel tasks to query complexity, what context each Task shares vs hides (final cleaned outputs only), where snippet-first vs full-content retrieval fires, and the runtime JSON schema for API output — then flag every place dynamic task count makes cost/latency hard to bound and where the lack of quality metrics limits confidence."

## Reliability Notes

> [!warning] Caveats
> - **Vendor + customer-story lens (likely a partner/integration piece).** LangChain blog about an Exa product built on LangGraph/LangSmith; LangChain and Exa are long-standing integration partners. Treat as a credible architecture sketch, not independent evaluation. Confidence **0.78** overall: ~0.8 on the described architecture/context-engineering patterns (concretely stated), lower on the (unquantified) token-savings/quality claims and the "framework of choice"/"mirrors Anthropic" framing.
> - **Only operational metrics** (hundreds of queries/day; 15 s–3 min latency). **No** quality, accuracy, citation-precision, token-cost, or satisfaction numbers; "preserves research quality" is asserted.
> - **Design lineage is self-reported** ("mirrors Anthropic's system") with no head-to-head comparison.
> - Architecture diagrams not pixel-parsed; content captured from surrounding text/tables. The in-body architecture diagram is a bare `![]` image with no alt/caption; Planner→Tasks→Observer topology reconstructed from prose. No metric/eval charts present as image-only content.

## Backfill Status

- Newly written 2026-06-22 from a full web capture (article read end-to-end via web_fetch). All sections populated. No prior thin version to upgrade. `coverage: substantial` for the architecture, context-engineering, and structured-output patterns; quality/outcome metrics remain unavailable in-source. Bare-image architecture diagram reconstructed from text (no image-only metrics).
