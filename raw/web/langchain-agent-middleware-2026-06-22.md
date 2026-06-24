---
source_url: https://www.langchain.com/blog/agent-middleware
captured: 2026-06-22
title: Agent Middleware
authors: [The LangChain Team]
published: 2025-09-08
publisher: LangChain Blog
---

# Agent Middleware
**Author:** The LangChain Team — **Published:** 2025-09-08 — LangChain Blog

> Immutable capture. AI-written summary, key points, short quoted excerpts, and diagram-content notes only — no full article text. See the source URL for the complete article. Reading time: ~5 min.

## Summary

The canonical introduction of the **`Middleware`** abstraction in **LangChain 1.0**. The post opens by stating that the **core agent components are simple** — a model, a prompt, and a list of tools — and the **core agent algorithm is equally simple**: the user invokes the agent with an input message, and the agent runs in a loop, calling tools and appending AI/tool messages to its state, until it decides to stop calling tools and finish. LangChain had this agent in November 2022, and over three years "100s of frameworks have popped up with similar abstractions." The problem: while a basic agent is easy to stand up, it is **hard to make this abstraction flexible enough to bring to production**, and developers routinely "graduate off" the abstraction (drop to custom code) for any non-trivial use case.

The diagnosed root cause is **context engineering**: "the context that goes into the model determines what comes out of it," so to make an agent reliable you need **full control over what goes into the model**. As complexity rises you want more control over three things: (1) the agent's **state** (more than just messages), (2) **what exactly goes into the model**, and (3) **the sequence of steps** run. The post recounts LangChain's incremental journey to support this over ~two years — runtime config (connection strings, read-only user info), arbitrary state schemas, a function returning the prompt (dynamic prompts), a function returning the full message list, a **"pre model hook"** (run a step before the model; update state or jump to another node — enables summarization of long conversations), a **"post model hook"** (run after the model; enables human-in-the-loop and guardrails), and a function that returns the model to use per call (dynamic model switching and dynamic tool calling). This delivered high customization **but** produced a large number of agent parameters that **depended on each other** (hard to coordinate), and were hard to combine or ship as off-the-shelf variants.

**`Middleware`** is LangChain 1.0's answer. The core loop still has a model node and a tool node, but middleware can specify three hooks: **`before_model`** (runs before model calls; can update state or jump to other nodes), **`after_model`** (runs after model calls; can update state or jump to other nodes), and **`modify_model_request`** (runs before model calls; lets the user modify — *for that request only* — the tools, prompt, message list, model, model settings, output format, and tool choice). You can provide **multiple middleware**, and they **run like middleware in web servers**: sequentially on the way *in* to the model call (`before_model`, then `modify_model_request`), and in **reverse sequential order on the way back** (`after_model`). Middleware can **also specify custom state schemas and tools**. LangChain commits to shipping **off-the-shelf middleware** plus a maintained **list of community middleware** — explicitly framed as the long-requested "collections of nodes to plug into LangGraph agents." Strategically, middleware will **unify LangChain's separate agent abstractions** (supervisor, swarm, bigtool, deepagents, reflection, and more): they've verified these architectures can be replicated using Middleware. The alpha ships **three reference middleware** already used in internal agents: **Human-in-the-loop** (`after_model` — off-the-shelf interrupts to get human feedback on tool calls), **Summarization** (`before_model` — summarize messages once they pass a threshold), and **Anthropic Prompt Caching** (`modify_model_request` — add prompt-caching tags to messages). Try it via `pip install --pre -U langchain` or `npm install langchain@next`.

## Key Points

- **Core agent = model + prompt + list of tools**, run in a simple loop (call tools, append messages) until the model stops calling tools. Easy to start; **hard to make production-reliable**, so devs drop to custom code for non-trivial cases.
- **Root cause = context engineering:** what goes into the model determines the output, so reliability requires full control over the model's input.
- **Three things you want more control over as complexity rises:** the agent's state (beyond messages), exactly what goes into the model, and the sequence of steps.
- **Prior approach** was a growing pile of agent parameters (runtime config, custom state schemas, prompt/message-list functions, pre/post model hooks, dynamic model function) — powerful but **interdependent and hard to combine**.
- **`Middleware` (LangChain 1.0)** keeps the model+tool loop and adds three hooks: **`before_model`**, **`after_model`**, and **`modify_model_request`** (per-request override of tools, prompt, messages, model, settings, output format, tool choice).
- **Composition order:** multiple middleware run sequentially inbound (`before_model` → `modify_model_request`) and in **reverse order outbound** (`after_model`) — like web-server middleware. Middleware can also declare **custom state schemas and tools**.
- **Off-the-shelf + community middleware** planned; middleware will **unify LangChain's separate agent architectures** (supervisor, swarm, bigtool, deepagents, reflection — verified replicable via middleware).
- **Three reference middleware in the alpha:** Human-in-the-loop (`after_model`), Summarization (`before_model`), Anthropic Prompt Caching (`modify_model_request`).

## Short Quoted Excerpts

- "LangChain has had agent abstractions for nearly three years. There are now probably 100s of agent frameworks with the same core abstraction. They all suffer from the same downsides … they do not give the developer enough control over context engineering when needed, leading to developers graduating off of the abstraction for any non-trivial use case."
- "The answer is context engineering. The context that goes into the model determines what comes out of it."
- "Middleware can now specify: `before_model` … `after_model` … `modify_model_request`."
- "They will run as middleware runs in web servers: sequentially on the way in to the model call (`before_model`, `modify_model_request`), and in reverse sequential order on the way back (`after_model`)."
- "For a while, developers have asked for collections of nodes to plug into LangGraph agents. This is exactly that."

## Diagrams (content captured from text/captions)

The post includes a header image and two screenshots, all returned as bare `![](url)` with no alt text; content reconstructed from prose.

- *Header image* — branded post illustration (decorative).
- *Core agent loop screenshot (Screenshot 2025-09-08 at 9.17.11 PM)* — depicts the simple loop described in text: user input → model node → (if tool calls) tool node → back to model, looping until the model finishes with no tool calls; AI/tool messages accumulate in state.
- *Middleware hooks screenshot (Screenshot 2025-09-08 at 9.17.21 PM)* — depicts the same model-node/tool-node loop with middleware insertion points: `before_model` and `modify_model_request` on the inbound path to the model call, and `after_model` on the outbound path; multiple middleware nest like web-server middleware (inbound in order, outbound in reverse order).

## Provenance Notes
- Primary source: LangChain engineering blog (vendor). Author: The LangChain Team. Published 2025-09-08 (LangChain 1.0 alpha announcement).
- This is the **canonical/origin post** for the `Middleware` abstraction; the hooks named here (`before_model`, `after_model`, `modify_model_request`) are the foundation later how-tos (e.g., "How to Build a Custom Agent Harness," "The Art of Loop Engineering") build on. Note later posts describe a fuller hook set (also before/after tool calls, startup/teardown); this origin post specifies the three model-centric hooks plus custom state and tools.
- Links throughout to the LangChain middleware docs (docs.langchain.com/oss/python/langchain/middleware) and the "rise of context engineering" post.
- Try-it commands: `pip install --pre -U langchain` (Python), `npm install langchain@next` (JavaScript).
