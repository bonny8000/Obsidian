---
source_url: https://www.langchain.com/blog/building-box-ai-how-an-enterprise-content-platform-went-ai-native-with-deep-agents
captured: 2026-06-22
title: "Building Box AI: How an Enterprise Content Platform Went AI-Native with Deep Agents"
authors: [Sofia Sulikowski]
published: 2026-06-12
publisher: LangChain Blog
---

# Building Box AI: How an Enterprise Content Platform Went AI-Native with Deep Agents

**Author / Company:** Sofia Sulikowski (LangChain), reporting on Box — featuring Sesh Jalagam (Principal AI Architect, Box) and Shubhro Roy (AI Engineering Leader, Box) **Published:** 2026-06-12 — LangChain Blog (Case Studies)

> Immutable capture. AI-written summary, key points, short quoted excerpts, and diagram content from surrounding text only — no full article text. See the source URL for the complete article.

## Summary

A LangChain customer-story / case study describing how **Box** — the intelligent content management platform "trusted by 100,000+ enterprises" — built its **Box Agent** (part of Box AI) on LangChain's **Deep Agents** framework to go "AI-native." The Box Agent searches across an enterprise's entire content library, synthesizes findings across thousands of documents, and produces reports and analysis, all while respecting Box's existing security and permissions model.

The post traces an evolution. The first Box Agent answered questions within a **single document**. Box then added **Knowledge Hubs**, a RAG-based layer letting users query across a defined knowledge source. But users began asking increasingly complex, cross-domain questions (e.g. a bioscience team synthesizing a body of research before a new study; a legal team pulling all contracts over a value threshold from the past decade and assessing them against a risk rubric). Standard Q&A was not enough, so Box needed an **agentic architecture**.

Box evaluated multiple frameworks and chose **Deep Agents** for two reasons: (1) **complete model agnosticism** — Box lets customers choose LLM providers (OpenAI, Anthropic, Google, others), and that flexibility had to be preserved at the platform level, which Deep Agents' model abstraction layer handled via provider-agnostic routing; and (2) **speed of iteration** — the open agent harness let Box focus engineering on enterprise-specific problems rather than rebuilding core agent infrastructure, "unlocking 3x speed of iteration."

The core architecture is a **recursive parent/child model where both the parent and all children are Deep Agents**. The parent (the **Global Agent**) receives a request, classifies intent, and decides whether to handle it directly or spawn child agents to distribute work. Child agents are expressed as **tools** to the parent, keeping the invocation surface uniform whether the parent runs a keyword search or delegates to a freshly spawned sub-agent. This was a deliberate evolution away from an earlier architecture with **hardcoded, specialized sub-agents** (a dedicated search agent, QA agent, and compose agent) that created unnecessary latency. Simple requests are handled directly by the parent ("It doesn't even need to come up with a plan"); complex requests trigger a plan and a fan-out. Child agents run with **isolated context windows** and report back through a **middleware layer**. Because children are spawned dynamically rather than predefined, the system handles tasks Box's product teams never explicitly designed for — the Global Agent decides at runtime which children to create and what tools to give them.

Both parent and child have access to the **same full tool registry** (BM25 keyword search, vector search, structured Q&A over spreadsheets, file operations, and more). Rather than dynamically selecting a tool subset per request, Box found that as use cases expanded, the models were better at choosing tools than any static routing logic.

The **middleware** (Deep Agents middleware that intercepts model and tool calls) provides three functions: (1) **citation generation** as a parallel process during response streaming (citations are ready to attach by the time the answer completes, using embedding-based matching with logic to distribute citations across sources — so the user is never interrupted); (2) **prompt caching** injected on multi-turn conversations to reduce cost and latency as history accumulates; and (3) **context management** — when conversation history exceeds **170,000 tokens**, middleware automatically summarizes it to prevent context overflow without changing agent logic. Middleware also serves as the **communication channel between parent and child agents** — a child writes its results through middleware, and the parent and other children can read and act on them.

On velocity: building Box AI previously meant building "completely from the ground up." With the Deep Agents stack, Box can ship a new agent in "a couple of weeks." Within the platform itself, the first (hardcoded specialized sub-agent) architecture took roughly **3 months** to develop and ship; the recursive parent/child architecture that followed shipped **4x faster**. The roadmap aims at an agent with "the institutional knowledge of a tenured employee" — richer memory and knowledge composition, the ability to run offline in the background collecting and surfacing information, and deeper communication with internal teams and external systems. The post links to a companion Box engineering blog (blog.box.com/how-box-built-its-ai-agent-langgraph).

## Key Points

- **Box** = intelligent content management platform, 100,000+ enterprises; **Box Agent** (part of Box AI) is built on **Deep Agents**, LangChain's open-source framework for "long-running agents for complex tasks."
- **Capability ladder:** single-document Q&A → Knowledge Hubs (RAG over a defined knowledge source) → agentic cross-enterprise search + multi-document synthesis + structured report generation.
- **Two framework-selection requirements:** (1) complete **model agnosticism** (customers choose OpenAI / Anthropic / Google / others; preserved via Deep Agents' model abstraction layer + provider-agnostic routing); (2) **speed of iteration** (open agent harness → "3x speed of iteration"; "full control of all the pieces, while building on a forward-looking framework").
- **Recursive parent/child architecture:** parent = **Global Agent**; both parent and children are Deep Agents. Parent classifies intent and either handles directly or spawns children. **Children are expressed as tools** to the parent (uniform invocation surface).
- **Dynamic, not hardcoded, sub-agents.** Earlier architecture hardcoded a search agent + QA agent + compose agent, creating unnecessary latency. New design spawns children at runtime, so the system handles tasks product teams never explicitly designed for.
- **Worked complex example:** "pull all contracts from the last 10 years with values exceeding a threshold and evaluate them against a risk rubric" → Global Agent makes a plan and fans out: one child searches for documents, another retrieves the rubric in parallel, a third synthesizes/analyzes once the first two complete. All run with **isolated context windows**, reporting back via middleware.
- **Shared full tool registry** for both parent and children: BM25 keyword search, vector search, structured Q&A over spreadsheets, file operations, more. Box let the **model** choose tools rather than static routing — models proved better at tool selection as use cases grew.
- **Middleware (intercepts model + tool calls) provides three functions:**
  - **Citation generation** — runs as a parallel process during response streaming; embedding-based source matching with logic to distribute citations across multiple sources; never interrupts the user.
  - **Prompt caching** — injected on multi-turn conversations to cut cost and latency.
  - **Context management** — auto-summarizes conversation history when it exceeds **170,000 tokens**, preventing overflow without changing agent logic.
- **Middleware = parent↔child communication channel.** A child writes results through middleware; parent and other children read and act on them. This is how intermediate artifacts flow within a single execution.
- **Velocity results:** new agent shippable in "a couple of weeks" (vs building from the ground up previously). First (hardcoded) architecture took ~3 months; recursive parent/child architecture shipped **4x faster**.
- **Roadmap:** an agent with "the institutional knowledge of a tenured employee" — richer memory and knowledge composition, offline/background information collection, deeper communication with internal teams and external systems.
- **Security framing:** all capabilities operate "while respecting Box's existing security and permissions model." (Stated, not detailed.)

## Diagrams (content from text/captions)

The post embeds one in-body architecture diagram with no alt text (`![]` bare image: `box-agent-architecture 1.png`), plus the article hero image and related-post thumbnails (not content-bearing).

- **Box Agent architecture diagram** (`6a2c3ad82abed12030d74c4d_box-agent-architecture 1.png`, placed after the parent/child architecture section): no caption is provided. Its content is recoverable from the surrounding prose — it depicts the **recursive parent/child Deep Agent topology**: a **Global Agent (parent)** that classifies intent and either acts directly or **spawns child agents (themselves Deep Agents)** which are **exposed back to the parent as tools**; each child runs with an **isolated context window**; children and parent communicate through a **middleware layer**; both parent and children draw on the **same shared tool registry** (BM25 keyword search, vector search, structured spreadsheet Q&A, file operations). The fan-out example (search child + rubric-retrieval child in parallel → synthesis child) illustrates the runtime topology. Exact boxes/arrows/labels in the rendered image are **not pixel-parsed**; this reconstruction is from the article text.
