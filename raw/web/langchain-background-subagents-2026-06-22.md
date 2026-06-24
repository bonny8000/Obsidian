---
source_url: https://www.langchain.com/blog/running-subagents-in-the-background
captured: 2026-06-22
title: Running Subagents in the Background
authors: [Hunter Lovell, Colin Francis]
published: 2026-04-16
publisher: LangChain Blog
---

# Running Subagents in the Background
**Author:** Hunter Lovell, Colin Francis — **Published:** 2026-04-16 — LangChain Blog

> Immutable capture. AI-written summary, key points, short quoted excerpts, and diagram-content notes only — no full article text. See the source URL for the complete article.

## Summary

Announces **async subagents** shipped to **Deep Agents**: a pattern that lets a supervisor agent run delegated work in the background instead of blocking on it. The post diagnoses the limits of **inline (synchronous) subagents** — the established context-engineering pattern where a supervisor delegates scoped work to a subagent that gets instructions, tools, and returns a summary. Inline subagents work because (1) agents perform better when work is broken into smaller tasks (a supervisor understands the problem, organizes tasks, coordinates workers) and (2) not all detail of a small task matters to the larger objective, so splitting into focused independent runs hides unnecessary context from the supervisor.

But as agents take on longer, more complex tasks, inline subagents break down in three ways. **(1) Deadlock while subagents work:** subagents are called via a tool given to the supervisor, and because tool calls in an agent loop are synchronous, the supervisor can't reason about anything else until the tool returns the subagent's response — if a subagent takes an hour, you wait an hour before interacting with the agent again. **(2) New information is hard to coordinate:** three channels matter to a working agent — *user input* (steer, add context, change priorities mid-flight), *results from other work* (one subagent's output should inform another's), and *partial progress* (course-correct before a task finishes) — and inline subagents block all three (supervisor blocked so user can't talk to it; no concurrent runs so no cross-pollination; turns are all-or-nothing so no mid-task updates or graceful partial-failure handling). "The supervisor fires off a subagent and hopes for the best."

**Async subagents** run in the background: the supervisor launches a task, gets a **task ID back immediately**, and continues working — talking to the user, kicking off more subagents, making progress elsewhere. Because subagents are **stateful and maintain their own conversation thread**, the supervisor can send follow-up instructions, course-correct mid-task, or cancel work no longer needed. The framing: **less "fire-and-forget," more "fire-and-steer."** Mechanically, instead of one blocking tool call per subagent, the supervisor gets a set of **management tools that work like a task queue** (`start_async_task`, `check_async_task`, `update_async_task`, `cancel_async_task`, `list_async_tasks`), used naturally inside its reasoning loop. Whereas traditional subagents are "really just a function of the parent agent" (share a process, share state, exist only inside the supervisor's execution loop), async subagents are **separate, individually addressable agents** that run in their own process, maintain their own state, and can scale to runs calling **hundreds or thousands of subagents**.

That separation requires more than in-process function calls, so async subagents are built on **Agent Protocol** — a framework-agnostic API specification for managing remote agents, defining standard endpoints for creating threads, launching runs, polling status, sending updates, and managing long-term memory. The **key benefit is deployment flexibility**: run async subagents on LangSmith deployments (managed) or self-host them on your own infrastructure; the supervisor doesn't care where the subagent lives — it sends a task, gets a task ID, and manages the lifecycle through the same standard interface either way. Usage in Deep Agents is "as simple as swapping an async subagent spec into the `subagents` list," and async and inline subagents can be mixed freely. With LangSmith deployments, you register agents in `langgraph.json` (referencing a `graphId`); because a subagent is a separate agent, the supervisor gets the async management tools automatically. Self-hosted, the supervisor connects via a `url` instead of a `graphId`, and the server implements the Agent Protocol endpoints (a complete example ships a Hono server, Postgres-backed state, and Docker Compose).

## Key Points

- **Inline subagents block the supervisor for the task's duration** — tool calls in an agent loop are synchronous, so the supervisor can't respond to users, coordinate other work, or course-correct until the subagent finishes (a real problem at hour-plus tasks).
- **A subagent** = an agent a supervisor delegates scoped work to; it gets instructions, relevant tools, returns a summary. Adopted broadly because work splits better (supervisor organizes + coordinates workers) and irrelevant sub-task detail is hidden from the supervisor (a context-engineering pattern).
- **Three failure channels of inline subagents:** user input, cross-subagent results, and partial progress are all blocked.
- **Async subagents return a task ID immediately**, so supervisors stay in control — launch many in parallel, keep talking to the user, send mid-task updates, or cancel stale work: "fire-and-steer" not "fire-and-forget."
- **Management tools (task queue):** `start_async_task`, `check_async_task`, `update_async_task`, `cancel_async_task`, `list_async_tasks`.
- **Async subagents are separate, individually addressable agents** — own process, own state — scaling to hundreds/thousands of subagents, vs inline subagents which share the parent's process/state and exist only in its loop.
- **Built on Agent Protocol** (framework-agnostic remote-agent API spec; endpoints for threads, runs, status polling, updates, long-term memory) → **deployment flexibility**: LangSmith-managed or self-hosted, same interface either way; not locked into one platform.
- **Deep Agents integration:** swap an async subagent spec into the `subagents` list; mix freely with inline. LangSmith uses `graphId` in `langgraph.json`; self-hosted uses a `url` to a server implementing Agent Protocol endpoints.

## Short Quoted Excerpts

- "Inline subagents block the supervisor agent for the duration of the task."
- "Async subagents return a task ID immediately, so supervisors stay in control."
- "Think of it less like 'fire-and-forget' and more like 'fire-and-steer.'"
- "Traditional subagents are really just a function of the parent agent — they share a process, they share state, and they only exist inside the supervisor's execution loop."
- "The supervisor doesn't care where the subagent lives. It sends a task, gets a task ID, and manages the lifecycle through the same standard interface either way."

## Diagrams (content captured from text/captions)

The post includes a header illustration and a hero diagram, both returned as bare `![](url)` with no alt text; content reconstructed from the surrounding prose.

- *Header / hero image* — a banner illustration for the post (decorative); conveys no technical content beyond the title.
- *Async-subagent management diagram (implied by the tool table)* — the supervisor holds a task queue and interacts with several background subagents via the five management tools (`start`/`check`/`update`/`cancel`/`list`), each subagent running in its own process/state, reachable through Agent Protocol whether on LangSmith or self-hosted. The prose specifies the five tools and the queue model; any pixel-level topology (arrows from supervisor to N subagents) is inferred, not captured.

## Provenance Notes
- Primary source: LangChain engineering blog (vendor). Authors Hunter Lovell and Colin Francis. Published 2026-04-16.
- Vendor lens: anchored on Deep Agents + Agent Protocol + (optionally) LangSmith deployments; the *async-subagent / fire-and-steer* concept is portable, the specific tool names and `langgraph.json`/`graphId` API are LangChain-specific.
- Cites the official async-subagents docs, the Agent Protocol spec/API reference (github.com/langchain-ai/agent-protocol), and a complete self-hosted example (Hono + Postgres + Docker Compose).
