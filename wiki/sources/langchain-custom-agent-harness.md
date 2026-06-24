---
type: source
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [harness-engineering, model-harness, context-engineering, agentic-engineering, mcp-integration, human-in-the-loop, token-efficiency, langchain, agent-architecture]
source_path: raw/web/langchain-custom-agent-harness-2026-06-22.md
source_url: https://www.langchain.com/blog/how-to-build-a-custom-agent-harness
authors: [Sydney Runkle]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.8
---

# How to Build a Custom Agent Harness (agent = model + harness; middleware)
**Author:** Sydney Runkle (LangChain) — **Published:** 2026-06-03 — LangChain Blog
**Raw capture:** [[raw/web/langchain-custom-agent-harness-2026-06-22|langchain-custom-agent-harness-2026-06-22]]
**URL:** [langchain.com/blog/how-to-build-a-custom-agent-harness](https://www.langchain.com/blog/how-to-build-a-custom-agent-harness)

## Citation

Runkle, S. (2026, June 3). *How to Build a Custom Agent Harness.* LangChain Blog. Captured 2026-06-22 into `raw/web/langchain-custom-agent-harness-2026-06-22.md`.

## Summary

A how-to that gives the wiki its sharpest working definition of a [[concepts/ai-agents/model-harness|harness]]: **"the scaffolding around the model that connects it to the real world,"** compressed to the equation **agent = model + harness**. Two assumptions drive the whole piece: (1) an agent is only as good as the context provided to the model, and (2) the harness's job is to provide the right context to the model **at every step**. Building a useful agent is therefore mostly **customization** — connecting the model to the right context, data, and environment for the task.

The base primitive is LangChain's **`create_agent`** (model + tools + system prompt → working loop). The post draws a philosophical contrast: **pre-assembled, opinionated harnesses** like **Deep Agents** and the **Claude Agent SDK** ship a full middleware stack (memory, context management, sandboxing) to reach production fast and work for most cases — versus `create_agent`, which is **purposefully minimalistic** (compared to Pi), implementing only the core loop and exposing **middleware** as the customization mechanism.

**Middleware** hooks the loop at before/after model calls, before/after tool calls, startup, and teardown; each piece handles one concern and composes freely. It adds capability via four levers: **deterministic logic** (business/policy logic, dynamic model swap, prompt adjustment, history compaction), **tools** (full lifecycle — setup/teardown/registration), **custom state** (cross-hook counters/flags/data), and **stream handlers** (filter/inject/route output events to UI, audit, monitoring). The centerpiece is a **capability→middleware table** mapping eight production concerns — context overflow, memory, environment actions, delegation/subagents, transient failures, policy/PII, steering, cost — to concrete prebuilt middleware. It closes on **task–harness fit**: how well the harness matches the task's real demands (context, failure modes, policies, environment), with "a customer-service harness looks very different from a long-running coding harness," and notes every LangChain-built agent (GTM agent, async coding agent open-swe, Fleet) is `create_agent` + a task-tailored middleware stack.

This is the most direct elaboration in the wiki of [[concepts/ai-agents/harness-engineering|Harness Engineering]] / [[concepts/ai-agents/model-harness|Model Harness]]: it decomposes "the harness" into concrete, composable middleware concerns. It pairs with [[sources/langchain-loop-engineering|The Art of Loop Engineering]] (which zooms *out* to the stacked outer loops) and operationalizes the abstract context/harness lens of [[sources/bayer-prince-reliable-agentic-ai|Bayer PRINCE]].

## Key Claims

- **Harness = the scaffolding around the model that connects it to the real world; agent = model + harness.**
- **An agent is only as good as the context provided;** the harness's single job is to deliver the right context to the model at every step. Building agents is therefore mostly customization.
- **`create_agent` is the base harness primitive** (model + tools + system prompt) and is *purposefully minimalistic*, exposing **middleware** as the customization point — vs Deep Agents / Claude Agent SDK, which are pre-assembled opinionated stacks (memory, context management, sandboxing) for fast production.
- **Middleware hooks the loop** at before/after model calls, before/after tool calls, startup, and teardown; each handles one concern and composes freely.
- **Four middleware levers:** deterministic logic (policy/business logic, dynamic model swap, prompt edits, history compaction), tools (full lifecycle management), custom state (track values across hooks), stream handlers (transform/route the output stream).
- **Reusability:** middleware bundles related logic into composable, sharable units; the same middleware reused across an org's agents lets new agents inherit battle-tested behavior.
- **Eight production capabilities map to specific middleware** (see the table): context overflow → Summarization/ContextEditing; memory → Filesystem/Memory/Skills; environment → ShellTool/Filesystem/CodeInterpreter; delegation → SubAgent/AsyncSubAgent/TodoList; failures → ToolRetry/ModelRetry/ModelFallback; policy → PII/HumanInTheLoop; steering → HumanInTheLoop; cost → ModelCallLimit/ToolCallLimit/PromptCaching.
- **Task–harness fit determines agent quality:** match the harness to the task's context, failure modes, policies, and environment; a customer-service harness ≠ a long-running coding harness.

## Useful Examples

- **The equation `agent = model + harness`** — a compact, transferable framing that separates the (swappable) model from the (task-specific, engineered) scaffolding.
- **The capability→middleware table** — a reusable production checklist: for any agent, walk the eight concerns (context overflow, memory, environment, delegation, failures, policy, steering, cost) and decide which to instrument. Even framework-agnostic, it enumerates what a "complete" harness addresses.
- **Pre-assembled vs minimalistic harness contrast** — Deep Agents / Claude Agent SDK (opinionated, fast to production) vs `create_agent`/Pi (minimal, maximally configurable): a useful decision axis when picking a starting harness.
- **Middleware as composable, org-reusable units** — write `PIIMiddleware` or `ModelFallbackMiddleware` once, reuse across every agent so new agents inherit tested behavior; an organizational-leverage pattern.
- **The four levers (logic / tools / state / stream)** — a vocabulary for *where* customization lives: anything that "can't or shouldn't live in a prompt" goes in deterministic-logic middleware (policy, dynamic control), not the system prompt.
- **`create_agent(model=..., tools=..., system_prompt=...)`** — the minimal working-agent snippet.

## Constraints / Caveats

- **Vendor how-to.** The entire piece is anchored on LangChain's `create_agent` + middleware; the *concepts* (harness, middleware hooks, task fit) are portable, the *API* is LangChain-specific. Notably it also positions the **Claude Agent SDK** as a pre-assembled alternative.
- **No evaluation.** It is a design/how-to article — no benchmarks, no before/after metrics, no evidence that a given middleware mix improves outcomes. Claims like "more creative solutions, often with greater token efficiency" (filesystem/execution access) are asserted, not measured.
- **Composability is presented as frictionless.** "Each piece handles one concern and composes freely" understates real ordering/interaction issues (e.g. summarization vs context-editing vs PII redaction ordering, retry vs human-in-the-loop interplay).
- **Middleware list is a snapshot.** The named middleware (SummarizationMiddleware, etc.) reflect LangChain's current library and will drift; treat the *categories* as durable, the specific class names as versioned.
- **"Right context at every step" is the hard part, left abstract.** The post asserts the harness should deliver the right context but, unlike PRINCE, gives no concrete retrieval/routing recipe for *deciding* what context is right.

## Design Implications

- **Separate model from harness in your design.** Treat the model as swappable and concentrate engineering effort on the harness; "the best agents are built with harnesses that tightly fit the task," not just capable models.
- **Choose a starting harness by configurability need:** pre-assembled (Deep Agents / Claude Agent SDK) for speed and common cases; minimalistic (`create_agent` + custom middleware) when you need bespoke prompting, business logic, or guardrails.
- **Use the eight-capability table as a coverage checklist** when hardening an agent for production: context overflow, memory, environment, delegation, failures, policy, steering, cost.
- **Put policy/PII/approval logic in middleware, not the prompt** — anything that must fire on every call regardless of model behavior belongs in deterministic-logic or [[concepts/ux-research/human-in-the-loop|human-in-the-loop]] middleware.
- **Manage tool lifecycles in middleware** (setup/teardown/registration) when tools have dependencies or need initialization — keeps tool config next to its governing logic. Connects to [[concepts/ai-agents/mcp-integration|MCP integration]] where external tools/servers must be wired in cleanly.
- **Build middleware as org-reusable units** so new agents inherit tested context-management, fallback, PII, and cost-control behavior instead of rebuilding it.
- **Design for [[concepts/ai-agents/context-engineering|context engineering]] explicitly:** the harness's job is delivering the right context every step (Summarization/ContextEditing for overflow, Memory/Skills for knowledge) — instrument [[concepts/infrastructure-dev/token-efficiency|token efficiency]] via PromptCaching and call limits.

## Tensions

- **Pre-assembled (fast, opinionated) vs minimalistic (configurable, more work).** Deep Agents / Claude Agent SDK get you to production fast but constrain customization; `create_agent` + middleware is maximally flexible but requires assembling the stack yourself.
- **"Composes freely" vs real middleware interactions.** Isolated single-concern pieces are the ideal, but ordering and interaction effects (summarization vs PII redaction vs context editing; retries vs human gates) are real and unaddressed.
- **Autonomy vs control.** The harness exists partly to *constrain* the model (policy, steering, human-in-the-loop, call limits) — the same theme as [[sources/bayer-prince-reliable-agentic-ai|PRINCE]] ("more reliable than an unconstrained autonomous agent"). More capable models invite more autonomy; the harness is where you claw control back.
- **Generic scaffolding vs task–harness fit.** The post sells reusable middleware *and* insists harnesses must tightly fit each task — reuse and bespoke fit pull in opposite directions; the resolution (compose reusable pieces into a task-specific stack) is plausible but not free.
- **Model-swappability vs harness coupling.** "agent = model + harness" implies clean separation, but real middleware (compaction, caching, prompt edits) is often tuned to a specific model's behavior.
- **Vendor portability.** The harness/middleware ideas are general; the recommended implementation is LangChain (with Claude Agent SDK as the named opinionated peer).

## Open Questions

- How does the harness actually *decide* what context is "right" at each step? The post asserts this is the job but gives no routing/retrieval recipe (contrast PRINCE's concrete context-per-agent routing).
- What are the real composition/ordering rules when multiple middleware touch the same message stream or state?
- Which capabilities matter most for which task types — is there an empirical mapping from task profile (long-running? sensitive? complex?) to the minimal middleware set?
- How portable are these patterns off LangChain, and how do they compare concretely to the Claude Agent SDK's pre-assembled stack?
- (Image gap) The middleware-hooks diagram pins the *exact* insertion points (before/after model call, before/after tool call, startup, teardown) and how middleware blocks clamp onto them — the prose lists them but the diagram conveys the loop topology more precisely than captured text can.

## Concepts Linked

- [[concepts/ai-agents/harness-engineering|Harness Engineering]] — this source's core subject: engineering the scaffolding around the model; deepens the concept with concrete middleware decomposition.
- [[concepts/ai-agents/model-harness|Model Harness]] — the explicit definition "agent = model + harness"; the harness as everything around the model that delivers context and control.
- [[concepts/ai-agents/context-engineering|Context Engineering]] — "the job of a harness is to provide the right context to the model at every step"; Summarization/ContextEditing/Memory/Skills middleware are context tooling.
- [[concepts/infrastructure-dev/agentic-engineering|Agentic Engineering]] — middleware as composable, reusable engineering units for building agents.
- [[concepts/ai-agents/mcp-integration|MCP Integration]] — tool-lifecycle middleware (setup/teardown/registration) is where external tools/servers get wired into the loop.
- [[concepts/ux-research/human-in-the-loop|Human-in-the-Loop]] — HumanInTheLoopMiddleware for policy gates and steering before consequential actions.
- [[concepts/infrastructure-dev/token-efficiency|Token Efficiency]] — PromptCaching, ModelCallLimit, ToolCallLimit middleware; filesystem/execution access framed as more token-efficient.
- [[concepts/ai-agents/context-rot|Context Rot]] — SummarizationMiddleware / ContextEditingMiddleware exist to prevent long-session context overflow.
- [[concepts/ai-agents/orchestrator-of-agents|Orchestrator of Agents]] — SubAgentMiddleware / AsyncSubAgentMiddleware / TodoListMiddleware implement delegation to subagents.
- [[concepts/ai-agents/agent-middleware|Agent Middleware]] (new) — composable hooks into the agent loop (before/after model & tool calls, startup, teardown) that add capability via deterministic logic, tools, custom state, and stream handlers.
- (new) concepts/ai-agents/task-harness-fit — the quality lever that an agent's usefulness depends on how well its harness matches the task's context, failures, policies, and environment.

## LLM Use

- **Use for:** defining what a harness is (agent = model + harness); decomposing a harness into concrete capabilities/middleware; choosing between pre-assembled (Deep Agents / Claude Agent SDK) and minimalistic (`create_agent`) starting points; deciding what belongs in middleware vs the prompt (policy, dynamic control, lifecycle); a production-hardening checklist (the eight-capability table).
- **Do not use for:** claiming measured outcomes from any middleware mix (none given); assuming middleware composes without ordering/interaction effects; treating specific middleware class names as stable across versions; deriving *how* to choose the right context (the post asserts the goal, not the method).
- **Best prompt pattern:** "Given this agent's task (context needs, failure modes, policies, environment), design its harness as `create_agent` + a middleware stack. Walk the eight capabilities (context overflow, memory, environment, delegation, failures, policy, steering, cost), pick the middleware for each, and state what stays in the prompt vs what must live in deterministic-logic/human-in-the-loop middleware — then note any composition-ordering risks."

## Reliability Notes

> [!warning] Caveats
> - **LangChain vendor how-to.** Promotes LangChain/LangGraph/Deep Agents/LangSmith and `create_agent`+middleware (also names the Claude Agent SDK as a pre-assembled peer). Confidence **0.8** on the harness/middleware *concepts and the capability taxonomy* (durable, well-structured); lower on specific middleware class names (versioned/will drift) and on any implied efficacy (no evaluation provided).
> - Architecture diagrams not pixel-parsed; content captured from surrounding text/tables (incl. the verbatim capability→middleware table).
> - The "right context at every step" goal is asserted but the *method* for choosing context is left abstract — pair with [[sources/bayer-prince-reliable-agentic-ai|PRINCE]] for a concrete context-routing recipe.

## Backfill Status

- Newly written 2026-06-22 from a full web capture (article read end-to-end; capability→middleware table and code snippet transcribed). All sections populated. `coverage: substantial` — prose, table, and snippet fully captured; the core-loop, agent=model+harness, and middleware-hooks diagrams were not pixel-parsed.
