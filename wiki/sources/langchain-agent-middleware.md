---
type: source
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [agent-middleware, harness-engineering, model-harness, context-engineering, human-in-the-loop, composability, langchain, langchain-1-0, agent-architecture]
source_path: raw/web/langchain-agent-middleware-2026-06-22.md
source_url: https://www.langchain.com/blog/agent-middleware
authors: [The LangChain Team]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.8
---

# Agent Middleware (LangChain 1.0 — the canonical Middleware abstraction)
**Author:** The LangChain Team — **Published:** 2025-09-08 — LangChain Blog
**Raw capture:** [[raw/web/langchain-agent-middleware-2026-06-22|langchain-agent-middleware-2026-06-22]]
**URL:** [langchain.com/blog/agent-middleware](https://www.langchain.com/blog/agent-middleware)

## Citation

The LangChain Team. (2025, September 8). *Agent Middleware.* LangChain Blog. Captured 2026-06-22 into `raw/web/langchain-agent-middleware-2026-06-22.md`.

## Summary

This is **the canonical/origin source** for the existing concept [[concepts/ai-agents/agent-middleware|Agent Middleware]] — the post that introduces the **`Middleware`** abstraction in **LangChain 1.0**. It argues that the core agent is simple (a model, a prompt, a list of tools, run in a loop that calls tools and appends messages until the model stops), and that 100s of frameworks share this abstraction — yet all suffer the same flaw: they don't give developers enough control over [[concepts/ai-agents/context-engineering|context engineering]], so developers "graduate off" the abstraction into custom code for any non-trivial use case.

The diagnosed root cause is context engineering: "the context that goes into the model determines what comes out of it," so reliability demands **full control over the model's input**. As complexity rises, developers want control over three things — the agent's **state** (beyond messages), **what exactly goes into the model**, and the **sequence of steps**. LangChain's two-year incremental answer (runtime config, arbitrary state schemas, prompt-returning and message-list-returning functions, a **pre-model hook**, a **post-model hook**, and a per-call model-selection function) delivered customization but produced a sprawl of **interdependent parameters** that were hard to coordinate, combine, or ship as off-the-shelf variants.

**`Middleware`** consolidates this. The loop keeps a model node and a tool node, but middleware can specify three hooks: **`before_model`** (update state / jump nodes before the model call), **`after_model`** (same, after the model call — enables human-in-the-loop and guardrails), and **`modify_model_request`** (per-request override of tools, prompt, message list, model, model settings, output format, and tool choice). Multiple middleware **compose like web-server middleware**: sequentially inbound (`before_model` → `modify_model_request`), in **reverse order outbound** (`after_model`). Middleware can also declare **custom state schemas and tools**. Strategically, middleware is positioned to **unify LangChain's separate agent architectures** (supervisor, swarm, bigtool, deepagents, reflection — verified replicable as middleware) and is delivered with off-the-shelf + community middleware ("collections of nodes to plug into LangGraph agents"). The alpha ships three reference middleware already used internally: **Human-in-the-loop** (`after_model`), **Summarization** (`before_model`), and **Anthropic Prompt Caching** (`modify_model_request`).

This origin post is the foundation that [[sources/langchain-custom-agent-harness|Custom Agent Harness]] and [[sources/langchain-loop-engineering|Loop Engineering]] build on: where this post names the three model-centric hooks plus custom state/tools, the later how-to describes a fuller hook set (also before/after tool calls, startup/teardown) and the capability→middleware table. It also grounds the [[concepts/ai-agents/harness-engineering|harness-engineering]] / [[concepts/ai-agents/model-harness|model-harness]] thesis that the engineering effort lives in the scaffolding around a swappable model.

## Key Claims

- **The core agent abstraction is simple** (model + prompt + tools, run in a loop) and ubiquitous, but **hard to make production-reliable** — so developers abandon frameworks for custom code on non-trivial tasks.
- **The root cause is context engineering:** the model's input determines its output, so reliability requires full control over what goes into the model.
- **As complexity grows, you need control over three things:** richer agent state, exactly what enters the model, and the sequence of steps.
- **The pre-`Middleware` approach** (runtime config + state schemas + prompt/message functions + pre/post-model hooks + dynamic model function) was powerful but produced **interdependent, hard-to-combine parameters**.
- **`Middleware` defines three hooks:** `before_model`, `after_model`, and `modify_model_request` (the last can override tools, prompt, messages, model, settings, output format, and tool choice — for that request only).
- **Composition is web-server-style:** sequential inbound (`before_model` → `modify_model_request`), reverse-order outbound (`after_model`); middleware can also add custom state and tools.
- **Middleware will unify LangChain's separate agent architectures** (supervisor, swarm, bigtool, deepagents, reflection) — verified replicable as middleware — and ship as off-the-shelf + community collections.
- **Three reference middleware in the alpha:** Human-in-the-loop (`after_model`), Summarization (`before_model`), Anthropic Prompt Caching (`modify_model_request`).

## Useful Examples

- **The three hooks as a vocabulary** — `before_model` / `after_model` / `modify_model_request` give precise names for *where* customization attaches to the loop. The first two for state changes / control flow (summarization, guardrails, human gates); the third for per-request shaping of the model call.
- **Web-server-middleware composition model** — "inbound in order, outbound in reverse" is a transferable mental model for reasoning about how stacked middleware interact (and a hint at ordering pitfalls).
- **The three reference middleware** as concrete patterns: Summarization (before_model) for context overflow, Human-in-the-loop (after_model) for approval gates, Prompt Caching (modify_model_request) for cost — a minimal but illustrative starter set.
- **"Replicate architectures as middleware"** — the claim that supervisor/swarm/bigtool/deepagents/reflection can all be expressed via middleware reframes "agent architecture" as "a stack of middleware over one core loop," a powerful unifying lens.

## Constraints / Caveats

- **Vendor announcement (LangChain 1.0 alpha).** The *concept* (composable hooks for context engineering) is portable; the API (`before_model` / `after_model` / `modify_model_request`, LangGraph nodes) is LangChain-specific and was alpha at publication.
- **No evaluation.** A design/announcement post — no benchmarks or before/after reliability metrics; the production-reliability benefit is argued, not measured.
- **Origin-version hook set is narrower than later posts.** This post specifies three model-centric hooks (plus custom state/tools); later LangChain posts describe additional hooks (before/after tool calls, startup/teardown). Treat the *three named here* as the 1.0 foundation, not the full current surface.
- **Composition "like web servers" understates interaction effects.** Sequential-in / reverse-out is clean in principle, but ordering matters (e.g., summarization vs prompt-caching vs guardrails) and the post doesn't address conflict resolution among many middleware.
- **Alpha API drift.** Install commands and exact signatures (`pip install --pre -U langchain`, `langchain@next`) reflect an alpha; specifics will change.

## Design Implications

- **Customize the harness via middleware, not parameter sprawl.** Bundle each cross-cutting concern (summarization, caching, guardrails, human gates) into a single composable hook instead of accumulating interdependent agent parameters — the [[concepts/ai-agents/harness-engineering|harness-engineering]] move.
- **Put policy/approval logic in `after_model` middleware** ([[concepts/ux-research/human-in-the-loop|human-in-the-loop]]) and **per-request shaping in `modify_model_request`** (dynamic model/tools/prompt), keeping the prompt itself lean.
- **Reason explicitly about composition order.** Because middleware run inbound-in-order / outbound-in-reverse, decide ordering deliberately (e.g., summarize before caching; redact before the model sees messages).
- **Treat "agent architecture" as a middleware stack.** If supervisor/swarm/deepagents reduce to middleware, then choosing an architecture becomes choosing and ordering middleware over one core loop — a unifying design stance.
- **Use middleware as the context-engineering control point** ([[concepts/ai-agents/context-engineering|context engineering]]): `before_model` to manage what accumulates (summarization), `modify_model_request` to control exactly what each call sees.

## Tensions

- **Simple core loop vs production reliability.** The same abstraction that makes agents trivial to start is the one developers abandon under complexity; middleware is the bid to make the simple abstraction survive production without forking.
- **Customization power vs coordination cost.** The pre-middleware parameter approach proved that more control knobs become interdependent and unmanageable; middleware claims to fix this via composition, but composition introduces its own ordering/interaction subtleties.
- **Unify-everything ambition vs leaky specifics.** Replicating supervisor/swarm/bigtool/deepagents as middleware is elegant, but each architecture's nuances (e.g., async delegation, see [[sources/langchain-background-subagents|Background Subagents]]) may not collapse cleanly into three model-centric hooks.
- **Portable concept vs vendor API.** "Context engineering needs full control" is universal; the demonstrated mechanism is LangChain/LangGraph-specific.

## Open Questions

- How are ordering/interaction conflicts among many middleware resolved in practice (e.g., summarization vs prompt-caching vs PII redaction touching the same messages)?
- How does the origin three-hook set map onto the later, fuller hook set (before/after tool calls, startup/teardown) — and what migration cost does that evolution impose?
- Is there evidence that the middleware abstraction actually reduces "graduating off the framework," or do complex agents still drop to custom code?
- How faithfully do supervisor/swarm/bigtool/deepagents/reflection reduce to middleware, and where does the abstraction leak?
- (Image gap) The two screenshots are the *only* place the loop topology and the precise inbound/outbound hook placement are drawn; the prose lists the three hooks and the web-server ordering, but the diagrams pin where each hook clamps onto the model/tool nodes more precisely than the captured text.

## Concepts Linked

- [[concepts/ai-agents/agent-middleware|Agent Middleware]] — **this source is the canonical/origin reference** for the concept: composable hooks (`before_model`, `after_model`, `modify_model_request`) over the agent loop, plus custom state and tools, for context-engineering control.
- [[concepts/ai-agents/harness-engineering|Harness Engineering]] — middleware is the mechanism for engineering the scaffolding around the model without forking the core loop.
- [[concepts/ai-agents/model-harness|Model Harness]] — reinforces "the model is simple; the harness around it is where reliability is engineered."
- [[concepts/ai-agents/context-engineering|Context Engineering]] — the post's stated root cause: full control over the model's input; `before_model` and `modify_model_request` are the control points.
- [[concepts/ai-agents/loop-engineering|Loop Engineering]] — middleware modifies the inner agent loop; this is the loop's customization layer.
- [[concepts/ux-research/human-in-the-loop|Human-in-the-Loop]] — the reference Human-in-the-loop middleware uses `after_model` to add approval interrupts on tool calls.
- [[concepts/infrastructure-dev/token-efficiency|Token Efficiency]] — the Anthropic Prompt Caching reference middleware (`modify_model_request`) is a cost/token-efficiency lever.
- [[concepts/ai-agents/context-rot|Context Rot]] — the Summarization reference middleware (`before_model`) summarizes accumulated messages past a threshold to prevent overflow.

## LLM Use

- **Use for:** defining the `Middleware` abstraction and its three origin hooks; explaining *why* context engineering motivates middleware (full control over model input); the web-server-style composition model; the idea that agent architectures can be expressed as middleware stacks; mapping the three reference middleware (summarization / human-in-the-loop / prompt caching) to concerns.
- **Do not use for:** claiming measured production-reliability gains (none given); treating the three model-centric hooks as the complete current hook set (later posts add more); assuming middleware composes without ordering effects; treating the alpha API/install commands as stable.
- **Best prompt pattern:** "Express this agent's cross-cutting needs as LangChain middleware. For each concern, choose the hook (`before_model` for state/summarization, `after_model` for guardrails/human-in-the-loop, `modify_model_request` for per-call model/tool/prompt shaping), state the composition order (inbound-in-order, outbound-in-reverse), and flag any interactions between middleware touching the same messages or state."

## Reliability Notes

> [!warning] Caveats
> - **LangChain vendor announcement (1.0 alpha).** Promotes LangChain/LangGraph 1.0 and the `Middleware` abstraction (with Human-in-the-loop, Summarization, Anthropic Prompt Caching as shipped examples). Confidence **0.8** on the *concept and hook model* (durable, and this is the origin definition); lower on exact API/signatures (alpha; later posts already describe a broader hook set) and on the unverified "unify all architectures" / production-reliability claims (asserted, not evaluated).
> - Architecture diagrams not pixel-parsed; content captured from surrounding text/tables (the three hooks and web-server ordering are stated verbatim; the two screenshots depict the loop and hook placement).
> - This origin post names **three** model-centric hooks; treat that as the LangChain 1.0 baseline, not the full evolved surface — cross-check [[sources/langchain-custom-agent-harness|Custom Agent Harness]] for the fuller hook set and the capability→middleware table.

## Backfill Status

- Newly written 2026-06-22 from a full web capture (article read end-to-end; the three hooks, composition order, and three reference middleware transcribed). All sections populated. `coverage: substantial` — prose and hook semantics fully captured; the two loop/hook screenshots were not pixel-parsed (topology described from prose). Designated the canonical source for [[concepts/ai-agents/agent-middleware|Agent Middleware]].
