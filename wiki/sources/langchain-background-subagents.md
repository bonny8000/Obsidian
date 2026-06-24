---
type: source
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [multi-agent-architecture, orchestrator-of-agents, deep-agents, long-horizon-tasks, agent-middleware, async-subagents, agent-protocol, langchain]
source_path: raw/web/langchain-background-subagents-2026-06-22.md
source_url: https://www.langchain.com/blog/running-subagents-in-the-background
authors: [Hunter Lovell, Colin Francis]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.8
---

# Running Subagents in the Background (async subagents — "fire-and-steer")
**Author:** Hunter Lovell, Colin Francis (LangChain) — **Published:** 2026-04-16 — LangChain Blog
**Raw capture:** [[raw/web/langchain-background-subagents-2026-06-22|langchain-background-subagents-2026-06-22]]
**URL:** [langchain.com/blog/running-subagents-in-the-background](https://www.langchain.com/blog/running-subagents-in-the-background)

## Citation

Lovell, H., & Francis, C. (2026, April 16). *Running Subagents in the Background.* LangChain Blog. Captured 2026-06-22 into `raw/web/langchain-background-subagents-2026-06-22.md`.

## Summary

Announces **async subagents** in **Deep Agents**: subagents that run in the background instead of synchronously blocking the supervisor. The post's value is its sharp diagnosis of where the standard **inline subagent** pattern (the [[concepts/ai-agents/multi-agent-architecture|subagents pattern]]) breaks down on **[[concepts/ai-agents/long-horizon-tasks|long-horizon tasks]]**, and a concrete alternative.

A subagent is an agent a supervisor delegates scoped work to — it gets instructions, relevant tools, and returns a summary. It is a **context-engineering pattern** adopted broadly for two reasons: agents perform better when work is split into smaller tasks (the supervisor understands the problem, organizes tasks, coordinates workers), and irrelevant sub-task detail is kept out of the supervisor's context. But because tool calls in an agent loop are **synchronous**, an inline subagent **deadlocks** the supervisor for the task's full duration — if it takes an hour, you wait an hour before interacting with the agent. Inline subagents also block three coordination channels: **user input** (steer / re-prioritize mid-flight), **cross-subagent results** (one subagent's output informing another), and **partial progress** (course-correcting before completion). "The supervisor fires off a subagent and hopes for the best."

**Async subagents** flip this: the supervisor launches a task, gets a **task ID immediately**, and keeps working. Because subagents are **stateful with their own thread**, the supervisor can send follow-ups, course-correct, or cancel — **"fire-and-steer," not "fire-and-forget."** Mechanically, one blocking tool call is replaced by a **task-queue tool set** (`start_async_task`, `check_async_task`, `update_async_task`, `cancel_async_task`, `list_async_tasks`) the supervisor uses inside its reasoning loop. Crucially, async subagents are **separate, individually addressable agents** (own process, own state) rather than "a function of the parent agent," so a run can scale to **hundreds or thousands** of subagents. This is built on **Agent Protocol**, a framework-agnostic remote-agent API spec (endpoints for threads, runs, status polling, updates, long-term memory), which buys **deployment flexibility**: run on LangSmith deployments or self-host — the supervisor manages the lifecycle through the same interface either way.

It pairs directly with [[sources/langchain-custom-agent-harness|Custom Agent Harness]] (whose capability→middleware table lists `AsyncSubAgentMiddleware` for delegation) and extends the supervisor/subagent worldview of [[sources/langchain-multi-agent-architecture|LangChain Multi-Agent Architecture]] from synchronous to asynchronous orchestration.

## Key Claims

- **Inline subagents block the supervisor for the task's whole duration** — synchronous tool calls mean the supervisor can't respond to users, coordinate other work, or course-correct until the subagent returns.
- **Inline subagents block three coordination channels:** user input, cross-subagent results, and partial progress — "all-or-nothing" turns with no mid-task updates or graceful partial-failure handling.
- **Async subagents return a task ID immediately**, keeping the supervisor in control: launch many in parallel, keep talking to the user, send mid-task updates, cancel stale work.
- **They are separate, individually addressable agents** (own process + state), not in-process functions of the parent; this is what lets runs scale to hundreds/thousands of subagents.
- **They are built on Agent Protocol** (a framework-agnostic remote-agent API spec) → deployment flexibility (LangSmith-managed *or* self-hosted) with no platform lock-in; the supervisor uses one standard interface regardless of where the subagent runs.
- **Deep Agents integration is a drop-in:** add an async subagent spec to the `subagents` list and mix freely with inline subagents; LangSmith uses a `graphId` in `langgraph.json`, self-hosted uses a `url`.

## Useful Examples

- **The five management tools as a task queue** — `start_async_task` / `check_async_task` / `update_async_task` / `cancel_async_task` / `list_async_tasks`. A reusable mental model: model async delegation as a queue the supervisor polls and steers, not a blocking call. The tool *names* are LangChain's; the *queue-of-background-tasks* shape is portable.
- **"Fire-and-steer" vs "fire-and-forget"** — a compact framing for the difference between stateful, cancellable, updatable background work and dispatch-and-pray delegation.
- **Inline vs async decision axis** — inline subagents (shared process/state, simple, fine for fast low-stakes sub-tasks) vs async (separate agents, steerable, scale to thousands, needed for long/complex runs). They can be mixed in one agent.
- **Agent Protocol as the portability seam** — defining standard endpoints (threads, runs, status, updates, memory) is what decouples *who orchestrates* from *where the worker runs* (managed vs self-hosted).

## Constraints / Caveats

- **Vendor announcement.** Anchored on Deep Agents + Agent Protocol + (optionally) LangSmith deployments. The *concept* (async/background subagents, fire-and-steer, the task-queue tool model) is portable; the specific tool names, `subagents` spec, and `langgraph.json`/`graphId` API are LangChain-specific.
- **No evaluation.** A design/announcement post — no benchmarks, latency/throughput numbers, or cost comparisons between inline and async. "Scale to hundreds or thousands of subagents" is asserted, not measured.
- **New operational surface.** Async subagents as separate processes/services introduce orchestration concerns the post only gestures at — task lifecycle management, partial-failure semantics, polling overhead, and (self-hosted) running and observing a fleet of agent servers.
- **Coordination is now the supervisor's burden.** Unblocking the supervisor means it must actively manage many in-flight tasks (when to poll, when to cancel, how to reconcile results) — the post shows the tools but not a robust supervisor strategy for using them at scale.

## Design Implications

- **For long-running agents, prefer async subagents** so the supervisor stays interactive (user steering, mid-task updates) instead of deadlocking on a single delegated call. Connects to [[sources/langchain-loop-engineering|Loop Engineering]]'s stacked-loops view: the human/steering loop must stay live while inner work proceeds.
- **Treat delegation as a queue, not a call.** Design the supervisor to start tasks, poll status, send follow-ups, and cancel — implemented via [[concepts/ai-agents/agent-middleware|agent middleware]] (`AsyncSubAgentMiddleware`) rather than baked into the prompt.
- **Use Agent Protocol (or an equivalent) as a portability seam** when subagents may live on different infrastructure — keep the orchestration interface stable so workers can be managed or self-hosted without changing the supervisor.
- **Mix inline and async deliberately:** inline for fast, low-stakes, tightly-coupled sub-tasks; async for long-running, independently-scalable, steerable work.
- **Keep subagent context scoped** (the original rationale): split work so the supervisor isn't burdened with irrelevant sub-task detail — a [[concepts/ai-agents/context-engineering|context-engineering]] move that async preserves while removing the blocking cost.

## Tensions

- **Inline simplicity vs async control.** Inline subagents are simpler (shared process/state, one tool call) but block and don't scale; async subagents are steerable and scalable but add a separate-process/protocol layer and orchestration burden.
- **Unblocking the supervisor vs new coordination complexity.** Making the supervisor non-blocking solves the deadlock but shifts the hard problem to *managing many concurrent tasks well* — when to poll, cancel, and reconcile — which the post doesn't fully resolve.
- **"Fire-and-steer" autonomy vs oversight.** More concurrent background agents mean more autonomous work in flight at once; staying in control (steering/cancelling) requires the supervisor (or a human) to actually watch — echoing the autonomy-vs-control theme in [[sources/bayer-prince-reliable-agentic-ai|PRINCE]].
- **Portability claim vs vendor implementation.** Agent Protocol is framed as framework-agnostic, but the end-to-end path demonstrated (Deep Agents + LangSmith / the `subagents` spec) is LangChain's.

## Open Questions

- What is the real cost/latency profile of async vs inline subagents, and at what task length/complexity does async start to pay off?
- What are the failure and consistency semantics when hundreds of stateful background subagents run concurrently (partial failures, retries, ordering, result reconciliation)?
- What supervisor strategy reliably manages a large task queue (polling cadence, cancellation policy, when to wait vs proceed) — and can that strategy itself be packaged as reusable middleware?
- How interoperable is Agent Protocol with non-LangChain agents in practice (genuine cross-framework orchestration vs LangChain-to-LangChain)?
- (Image gap) The hero/management illustration is decorative and adds no technical detail beyond the title; the supervisor↔N-subagents topology is described in prose (five queue tools, separate processes) rather than conveyed by a parsed diagram.

## Concepts Linked

- [[concepts/ai-agents/multi-agent-architecture|Multi-Agent Architecture]] — the supervisor/subagent (delegation) pattern this post extends from synchronous to asynchronous.
- [[concepts/ai-agents/orchestrator-of-agents|Orchestrator of Agents]] — the supervisor orchestrating background subagents via a task-queue tool set is the orchestrator pattern made async.
- [[concepts/ai-agents/deep-agents|Deep Agents]] — the harness that ships async subagents; the concrete host for this feature.
- [[concepts/ai-agents/long-horizon-tasks|Long-Horizon Tasks]] — the motivating context: hour-plus, complex tasks where blocking inline subagents break down.
- [[concepts/ai-agents/agent-middleware|Agent Middleware]] — `AsyncSubAgentMiddleware` is how async delegation is wired into the agent loop (see the capability→middleware table in Custom Agent Harness).
- [[concepts/ai-agents/multi-agent-coordination|Multi-Agent Coordination]] — the three coordination channels (user input, cross-subagent results, partial progress) and the queue model are coordination mechanics.
- [[concepts/ai-agents/context-engineering|Context Engineering]] — scoping subagent context to keep irrelevant detail out of the supervisor is the original rationale the pattern preserves.
- [[concepts/ai-agents/async-subagents|Async / Background Subagents]] (new) — background, stateful, individually-addressable subagents the supervisor launches non-blockingly (task ID returned immediately) and can update/cancel ("fire-and-steer").
- (new) concepts/ai-agents/agent-protocol — a framework-agnostic API spec for managing remote agents (threads, runs, status, updates, memory) that decouples orchestration from where a subagent is deployed.

## LLM Use

- **Use for:** explaining why synchronous/inline subagents deadlock a supervisor on long tasks; the "fire-and-steer" model and its five queue tools; the inline-vs-async decision axis; how a portability layer (Agent Protocol) decouples orchestration from deployment; how async delegation is wired via middleware.
- **Do not use for:** claiming measured performance/cost benefits (none given); assuming async orchestration is free of coordination/failure complexity; treating the specific tool names / `langgraph.json` API as stable or framework-neutral; asserting genuine cross-framework Agent Protocol interop beyond LangChain.
- **Best prompt pattern:** "For this long-running agent, decide which sub-tasks should be inline vs async subagents. For the async ones, sketch the supervisor's queue strategy (start / check / update / cancel / list), the partial-failure handling, and where the workers are deployed (managed vs self-hosted via Agent Protocol) — and note the coordination risks of running many concurrently."

## Reliability Notes

> [!warning] Caveats
> - **LangChain vendor announcement.** Promotes Deep Agents, Agent Protocol, and LangSmith deployments. Confidence **0.8** on the *concepts* (async/background subagents, fire-and-steer, task-queue delegation, orchestration-vs-deployment decoupling — durable and well-argued); lower on specific tool names / `subagents` spec / `langgraph.json` API (versioned, will drift) and on any implied scale/perf benefit (no evaluation provided).
> - Architecture diagrams not pixel-parsed; content captured from surrounding text/tables (the five management tools and the queue model are stated verbatim in the prose; the hero image is decorative).
> - Cross-framework portability is asserted via Agent Protocol but only demonstrated within LangChain — treat "framework-agnostic" as a design goal, not a verified property here.

## Backfill Status

- Newly written 2026-06-22 from a full web capture (article read end-to-end; the five management tools and the inline-vs-async failure analysis transcribed). All sections populated. `coverage: substantial` — prose, tool table, and code-spec details captured; the decorative hero/management illustrations were not pixel-parsed (no technical content beyond the prose).
