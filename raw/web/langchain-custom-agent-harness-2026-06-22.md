---
source_url: https://www.langchain.com/blog/how-to-build-a-custom-agent-harness
captured: 2026-06-22
title: How to Build a Custom Agent Harness
authors: [Sydney Runkle]
published: 2026-06-03
publisher: LangChain Blog
---

# How to Build a Custom Agent Harness
**Author:** Sydney Runkle — **Published:** 2026-06-03 — LangChain Blog

> Immutable capture. AI-written summary, key points, short quoted excerpts, and diagram-content notes only — no full article text. See the source URL for the complete article. Reading time: ~6 min.

## Summary

A how-to that defines the **harness** as "the scaffolding around the model that connects it to the real world," and frames agent-building as primarily an exercise in **customization** — connecting the model to the right context, data, and environment(s) for the task. The post's compact definition: **agent = model + harness**. Two working assumptions drive everything: (1) an agent is only as good as the context provided to the model, and (2) the job of a harness is to provide the right context to the model **at every step**. So building a useful agent means building a harness that's great at delivering the right context for the given task.

The base harness primitive is LangChain's **`create_agent`** — pass a model, tools, and a system prompt and you have a working agent loop. The post contrasts two philosophies of harness: pre-assembled, opinionated harnesses like **Deep Agents** and the **Claude Agent SDK** that ship a middleware stack (memory, context management, sandboxing, etc.) to reach production fast and work for most cases — versus `create_agent`, which is **purposefully minimalistic** (compared to Pi, a highly configurable coding-agent harness): it implements only the core agent loop and exposes **middleware** as the customization primitive.

**Middleware** hooks into the agent loop at each step — before/after model calls, before/after tool calls, at agent startup and teardown — with each piece handling one concern and composing freely. Middleware adds capabilities via four levers that often work together: **deterministic logic** (business logic, policy enforcement, dynamic agent control — swap model by task complexity, adjust prompt, edit message history during compaction); **tools** (manage the full tool lifecycle — setup, teardown, registration — handing the agent a clean toolset, keeping config near governing logic); **custom state** (extend the agent's state with properties to track counters/flags across hooks and share data between hooks); and **stream handlers** (intercept/transform the output stream — filter events, inject metadata, route event types to different consumers like a UI, audit log, or monitoring system). The value: customization at any point in the loop, bundled into composable, sharable, reusable units (the same middleware can be reused across every agent in an org so new agents inherit battle-tested behavior).

The post's centerpiece is a **capability→middleware table** (captured below) mapping eight production concerns (context overflow, memory, environment actions, delegation, transient failures, policy, steering, cost) to specific prebuilt middleware. It closes on **task–harness fit**: how well a harness matches the actual demands of the task (context it needs, failures it'll hit, policies it must enforce, environment it operates in) — "a harness for a customer service agent looks very different from one built for a long-running coding agent." Every agent LangChain builds (GTM agent, async coding agent open-swe, Fleet no-code builder) is `create_agent` plus a task-tailored middleware stack. "The best agents aren't just built with capable models, they're built with harnesses that tightly fit the task."

## Key Points

- **Definition:** harness = scaffolding around the model that connects it to the real world; **agent = model + harness**.
- **Two assumptions:** an agent is only as good as the context it's given; the harness's job is to deliver the right context at every step.
- **`create_agent`** is LangChain's base harness primitive (model + tools + system prompt → working loop); **purposefully minimalistic**, exposing **middleware** for customization. Contrast: Deep Agents / Claude Agent SDK ship opinionated pre-assembled middleware stacks (memory, context management, sandboxing) for fast production.
- **Middleware hooks the loop** at before/after model calls, before/after tool calls, startup, teardown; each handles one concern and composes.
- **Four middleware levers:** deterministic logic (policy, dynamic model/prompt swap, history compaction), tools (full lifecycle), custom state (cross-hook counters/flags/data), stream handlers (filter/inject/route output events).
- **Reusability:** middleware bundles related logic into composable, sharable units; one piece can be reused across every agent in an org so new agents inherit tested behavior.
- **Task–harness fit** is the central quality lever: match the harness to the task's context, failure modes, policies, and environment. Customer-service vs long-running coding agents need very different harnesses.
- **`create_agent` snippet (verbatim):** `create_agent(model="anthropic:claude-sonnet-4-6", tools=tools, system_prompt="you are a helpful assistant...")`.

## Short Quoted Excerpts

- "A harness is the scaffolding around the model that connects it to the real world."
- "agent = model + harness"
- "1. An agent is only as good as the context provided to the model. 2. The job of a harness is to provide context to the model at every step."
- "`create_agent` … is purposefully minimalistic … it just implements the core agent loop, and it exposes middleware as a primitive for customization."
- "The best agents aren't just built with capable models, they're built with harnesses that tightly fit the task."

## Diagrams (content captured from text/captions)

The post includes several screenshots/diagrams, all returned as bare `![](url)` with no alt text; reconstructed from prose.

- *Core agent loop diagram* — a model node calling tools in a loop until it completes a task and returns a result (the same fundamental loop as in "The Art of Loop Engineering," Loop 1).
- *agent = model + harness diagram* — depicts the model wrapped by the harness "scaffolding" layer that connects it to the real world (context, data, environments).
- *Middleware hooks diagram* — shows the agent loop with middleware insertion points at before/after model call, before/after tool call, startup, and teardown; each middleware is a composable block clamped onto a hook point.

**Capability → middleware table (verbatim — the article's centerpiece):**
| Capability | Why it matters | Middleware |
| --- | --- | --- |
| Prevent context overflow | Long-running sessions accumulate message history fast; without intervention it overflows the context window | SummarizationMiddleware, ContextEditingMiddleware |
| Access and update memory | Load relevant knowledge at startup, write it back at end of run; lets the agent improve from real usage | FilesystemMiddleware, MemoryMiddleware, SkillsMiddleware |
| Take actions in an environment | A fixed toolset limits the agent; filesystem + execution environment unlocks more creative, often more token-efficient solutions | ShellToolMiddleware, FilesystemMiddleware, CodeInterpreterMiddleware |
| Delegate tasks | Subagents handle complex sub-tasks with clean context windows; a todo list tracks progress across a long run | SubAgentMiddleware, AsyncSubAgentMiddleware, TodoListMiddleware |
| Handle transient failures | Models and tools fail unpredictably; production agents need retry with backoff and fallbacks when a model is unavailable | ToolRetryMiddleware, ModelRetryMiddleware, ModelFallbackMiddleware |
| Enforce policies | PII handling, compliance checks, approval gates must fire on every call regardless of what the model does — they don't belong in a prompt | PIIMiddleware, HumanInTheLoopMiddleware |
| Steer the agent | Full autonomy isn't always appropriate; pause before consequential actions and wait for a human to approve/reject/redirect | HumanInTheLoopMiddleware |
| Control costs | Prompt caching reduces token spend on long tasks; call limits prevent runaway cost | ModelCallLimitMiddleware, ToolCallLimitMiddleware, PromptCachingMiddleware |

## Provenance Notes
- Primary source: LangChain engineering blog (vendor). Author Sydney Runkle. Published 2026-06-03.
- Vendor lens: the entire how-to is anchored on `create_agent` + LangChain middleware; positions Deep Agents and (notably) the Claude Agent SDK as the opinionated pre-assembled alternatives, and Pi as the "highly configurable" reference point.
- Companion to "The Art of Loop Engineering" (same author, same docs-agent worldview); this post zooms into Loop 1's internals (the harness/middleware), where Loop Engineering zooms out to the stacked outer loops.
- Acknowledgements: hwchase17, huntlovell, masondrxy, Vtrivedy10.
