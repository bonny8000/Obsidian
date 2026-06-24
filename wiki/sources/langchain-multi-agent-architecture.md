---
type: source
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [multi-agent-coordination, orchestrator-of-agents, agent-skills, progressive-disclosure, context-engineering, token-efficiency, agent-architecture, langchain, ai-agent-workflow]
source_path: raw/web/langchain-multi-agent-architecture-2026-06-22.md
source_url: https://www.langchain.com/blog/choosing-the-right-multi-agent-architecture
authors: [Sydney Runkle]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.8
---

# Choosing the Right Multi-Agent Architecture (Subagents / Skills / Handoffs / Router)
**Author:** Sydney Runkle (LangChain) — **Published:** 2026-01-14 — LangChain Blog
**Raw capture:** [[raw/web/langchain-multi-agent-architecture-2026-06-22|langchain-multi-agent-architecture-2026-06-22]]
**URL:** [langchain.com/blog/choosing-the-right-multi-agent-architecture](https://www.langchain.com/blog/choosing-the-right-multi-agent-architecture)

## Citation

Runkle, S. (2026, January 14). *Choosing the Right Multi-Agent Architecture.* LangChain Blog. Captured 2026-06-22 into `raw/web/langchain-multi-agent-architecture-2026-06-22.md`. Cites Anthropic's "Building a multi-agent research system" engineering post for the 90.2% figure.

## Summary

A vendor decision guide for **when** to adopt a multi-agent architecture and **which** of four patterns to use. The strong default is **single-agent**: most tasks are best handled by one agent with well-designed tools, which is simpler to build, reason about, and debug. Multi-agent becomes justified only under two scaling pressures: **context management** (specialized per-capability knowledge won't fit one prompt; you need to selectively surface information as agents work) and **distributed development** (separate teams owning capabilities with clear boundaries, which a monolithic prompt can't accommodate).

The four patterns:
- **Subagents** — centralized orchestration: a supervisor calls stateless subagents *as tools*, giving strong **context isolation** and centralized routing, at the cost of **+1 model call** per interaction (results flow back through the supervisor).
- **Skills** — progressive disclosure: a *single* agent loads prompt-driven specializations on demand (name/description → full context → deeper files). The author calls it a **"quasi-multi-agent"** pattern; its risk is **token bloat** as loaded skills accumulate in conversation history.
- **Handoffs** — state-driven transitions: the active agent changes via handoff tool calls that mutate shared state surviving across turns; the **most stateful** pattern, good for staged/sequential flows.
- **Router** — parallel dispatch + synthesis: a (typically **stateless**) routing step classifies input, fans out to specialized agents in parallel, and synthesizes results.

The post backs multi-agent with Anthropic's research system (Opus 4 lead + Sonnet 4 subagents beat single Opus 4 by **90.2%** via parallel reasoning across separate context windows), supplies a requirements→pattern decision table, a capability star-table, and three performance scenarios with model-call/token counts (headline: **Subagents process ~67% fewer tokens than Skills on a multi-domain query** thanks to context isolation). It closes with the maxim **"Add tools before adding agents"** and a nudge toward Deep Agents (subagents+skills) and LangSmith.

This is the clearest map in the wiki of the *space* of multi-agent patterns and their cost/state tradeoffs. It should be read against [[sources/hai-cooperbench-agent-teamwork|CooperBench]], which is the empirical counterweight: paired coding agents *underperform* a solo agent on conflict-prone work, so the optimistic "multi-agent helps" framing here is contingent on the coordination being engineered (a supervisor with context isolation, not two peers negotiating).

## Key Claims

- **Start single.** "Many agentic tasks are best handled by a single agent with well-designed tools. You should start here." Multi-agent answers two specific pressures, not a default ambition.
- **Two pressures trigger multi-agent:** context management (selective information surfacing because windows aren't infinite / latency isn't zero) and distributed development (independent team ownership of capabilities).
- **Multi-agent can beat single-agent** in those conditions: Anthropic's Opus 4 lead + Sonnet 4 subagents outperformed single Opus 4 by **90.2%** on internal research evals via parallel reasoning across separate context windows.
- **Subagents = centralized orchestration, stateless subagents-as-tools, strong context isolation, parallelizable, +1 model call.** Best for multiple distinct domains needing centralized control where subagents needn't talk to the user.
- **Skills = single agent, progressive disclosure, prompt-driven specializations loaded on demand.** A "quasi-multi-agent architecture." Lightweight, supports distributed development + direct user interaction, but **context accumulates → token bloat** on later calls.
- **Handoffs = state-driven, active-agent transitions via tool calls, state survives turns.** Most stateful; best for sequential/staged workflows where capabilities unlock after preconditions.
- **Router = stateless parallel dispatch + synthesis.** Best for distinct verticals and parallel multi-source queries; repeated routing overhead if you need conversation history (mitigate by wrapping the router as a tool inside a stateful agent).
- **Performance is pattern-dependent:** stateful patterns (Skills, Handoffs) save 40–50% of calls on repeat requests; parallel patterns (Subagents, Router) are most token-efficient on multi-domain work; **Subagents ≈ 67% fewer tokens than Skills** on the 3-language comparison via context isolation.
- **"Add tools before adding agents."** Graduate to multi-agent only at clear limits; Deep Agents offers an out-of-the-box subagents+skills implementation.

## Useful Examples

- **The four-pattern taxonomy itself** — a reusable vocabulary (Subagents / Skills / Handoffs / Router) for classifying any multi-agent design by coordination style, state model, and sequential unlocking.
- **Requirements → pattern decision table** — maps concrete needs to patterns: distinct domains + parallel → Subagents; many specializations + lightweight composition → Skills; sequential state transitions + user conversation throughout → Handoffs; distinct verticals + parallel multi-source + synthesis → Router. A copyable selection checklist.
- **The +1-model-call insight for Subagents** — a concrete, transferable cost model: centralized control via results-flow-back-through-supervisor costs exactly one extra call per interaction.
- **Skills as "quasi-multi-agent"** — a useful reframing: progressive disclosure gives multi-agent-like distributed development and context control from a *single* agent, trading agent-instance management for prompt-driven loading (and token-bloat risk).
- **The multi-domain token comparison** (Python/JS/Rust, ~2000 tokens/agent): Subagents ~9K vs Skills ~15K tokens — a concrete demonstration of how context isolation beats context accumulation at scale.
- **"Buy coffee" repeat-request scenario** — shows stateful patterns (Skills, Handoffs) saving ~40% of calls on a repeated turn while Subagents holds flat cost via stateless isolation.

## Constraints / Caveats

- **Vendor engineering blog.** LangChain promotes its own stack (Deep Agents for subagents+skills; LangSmith for observability/eval). The framework is sound but the framing favors LangChain primitives.
- **Performance numbers are LangChain's own scenario analysis,** not an independent benchmark. The model-call and token counts come from three small representative scenarios ("buy coffee," a 3-language comparison) with stated assumptions (~2000 tokens/agent); treat as illustrative, not measured production results.
- **The 90.2% figure is Anthropic's, on Anthropic's internal research evals** — domain-specific (research/search tasks) and not necessarily generalizable to other multi-agent workloads.
- **Optimistic about multi-agent benefit.** The post assumes coordination overhead is manageable; it does not engage with evidence that naive multi-agent collaboration can *degrade* capability (see Tensions / CooperBench).
- **Patterns are not mutually exclusive.** Deep Agents combines subagents + skills; routers can be wrapped as tools inside stateful agents — real systems mix patterns, which the clean taxonomy understates.

## Design Implications

- **Default to a single agent + good tools.** Treat "add an agent" as a last resort after "add a tool"; only escalate to multi-agent under genuine context-management or team-ownership pressure.
- **Choose the pattern by state + parallelism needs:** need context isolation and parallel domain work → Subagents; need lightweight, user-facing specialization → Skills; need sequential state-carrying conversation → Handoffs; need parallel multi-source synthesis → Router.
- **Budget the Subagents tax.** If you adopt centralized orchestration, plan for +1 model call per interaction and higher latency as the price of context isolation and control.
- **Watch Skills for [[concepts/ai-agents/context-rot|context bloat]].** Progressive disclosure is cheap to start but accumulates loaded context in history; instrument token growth on long conversations.
- **For multi-domain, large-context work, prefer parallel patterns** (Subagents/Router) for [[concepts/infrastructure-dev/token-efficiency|token efficiency]] over Skills' context accumulation.
- **Engineer the coordination, don't assume it.** Because peer-to-peer agent coordination is fragile (CooperBench), prefer a supervisor/router that imposes structure and isolation over agents left to negotiate.

## Tensions

- **Optimistic multi-agent vs the coordination gap.** This post says multi-agent "performs better" (Anthropic 90.2%); [[sources/hai-cooperbench-agent-teamwork|CooperBench]] finds two coding agents collaborating do *worse* than one (the "curse of coordination," ~half the capability lost), and that chat between agents barely helps. **Reconciliation:** LangChain's winning patterns are *supervisor-mediated* (Subagents) or *stateless-parallel* (Router) with strong context isolation — i.e. coordination is centralized and engineered, not negotiated between peers. CooperBench tests exactly the un-engineered peer case the post implicitly warns against ("add tools before adding agents"). The two are consistent only if you read this post as "multi-agent helps *when orchestration is centralized and isolated*."
- **Context isolation (Subagents) vs context continuity (Handoffs/Skills).** Isolation buys token efficiency and clean reasoning but loses cross-turn memory; continuity buys fluid conversation but accumulates/bloats context. No pattern is universally best.
- **More agents vs more tools.** The post's own advice ("add tools before adding agents") sits in tension with the multi-agent enthusiasm of the rest of the piece — agents are framed as the answer, yet most teams should stop at tools.
- **Lightweight Skills vs constrained Subagents.** Skills give direct user interaction and easy distributed development but can't *enforce constraints* between capabilities; Subagents enforce control at the cost of user-directness and an extra call.
- **Vendor neutrality vs product placement.** The patterns are framework-agnostic ideas, but the post routes each toward LangChain's Deep Agents / LangSmith.

## Open Questions

- Does the ~67% token advantage of Subagents over Skills hold beyond the 3-language toy scenario, at realistic domain counts and context sizes?
- At what concrete thresholds (domains, team count, prompt size, latency budget) should a team actually cross from single-agent to each pattern? The post gives qualitative triggers, not thresholds.
- How do these patterns fare on **conflict-prone** work specifically (CooperBench's regime), where overlapping edits cause collisions — does Subagents' isolation actually prevent the coordination gap?
- How well does the clean four-pattern taxonomy survive in production systems that *mix* patterns (e.g. Deep Agents = subagents+skills; router-as-tool)?
- (Image gap) The per-pattern architecture diagrams may encode message/state flow details (e.g. exactly which arrows are parallel vs sequential, where state is written) not fully spelled out in prose; the mermaid performance diagrams referenced as living in LangChain's docs are not captured here.

## Concepts Linked

- [[concepts/ai-agents/multi-agent-coordination|Multi-Agent Coordination]] — the core subject: coordinating specialized agents (and the cost/state tradeoffs of doing so).
- [[concepts/ai-agents/orchestrator-of-agents|Orchestrator of Agents]] — the Subagents pattern (supervisor calling subagents as tools) and the Router pattern are concrete orchestration designs.
- [[concepts/ai-agents/agent-skills|Agent Skills]] — the Skills pattern: prompt-driven specializations loaded on demand.
- [[concepts/ai-agents/progressive-disclosure|Progressive Disclosure]] — the mechanism behind Skills (name/description → full context → deeper files).
- [[concepts/ai-agents/context-engineering|Context Engineering]] — the "context management" pressure and per-pattern context isolation vs accumulation.
- [[concepts/ai-agents/context-rot|Context Rot]] — Skills' token-bloat-on-accumulation failure mode.
- [[concepts/infrastructure-dev/token-efficiency|Token Efficiency]] — the model-call/token performance analysis (Subagents ~67% fewer tokens than Skills).
- [[concepts/ai-agents/ai-agent-workflow|AI Agent Workflow]] — patterns for structuring agentic task coordination and sequential unlocking.
- [[concepts/ai-agents/harness-engineering|Harness Engineering]] — choosing an architecture is part of designing the harness around the model(s).
- [[concepts/ux-research/human-in-the-loop|Human-in-the-Loop]] — Handoffs/staged flows and supervisor control are natural points for human checkpoints.
- [[concepts/ai-agents/multi-agent-architecture|Multi-Agent Architecture]] (new) — the four-pattern umbrella; Subagents: — centralized orchestration where a supervisor calls stateless subagents as tools for context isolation, at +1 model call.
- (new) concepts/ai-agents/handoff-pattern — state-driven transition of the *active* agent via handoff tool calls, with state surviving across turns.
- (new) concepts/ai-agents/router-pattern — stateless classify → parallel-dispatch → synthesize coordination of specialized agents.

## LLM Use

- **Use for:** deciding whether a task needs multi-agent at all; selecting among Subagents/Skills/Handoffs/Router by state + parallelism + team-ownership needs; reasoning about the cost (extra model calls) and token tradeoffs of each pattern; arguing the "start single, add tools before agents" discipline.
- **Do not use for:** citing the performance numbers as measured benchmarks (they are LangChain scenario estimates) or the 90.2% as a general multi-agent result (it is Anthropic-internal, research-domain); claiming multi-agent is reliably better than single-agent (pair with CooperBench's counter-evidence); treating the four patterns as mutually exclusive.
- **Best prompt pattern:** "Using LangChain's four-pattern framework (Subagents / Skills / Handoffs / Router), classify this system's needs (distinct domains? parallel? sequential state? team ownership? direct user interaction?), recommend a pattern, state its cost/state tradeoff, and stress-test it against CooperBench's coordination-gap finding — would peer coordination collide here, and does the chosen pattern's isolation prevent it?"

## Reliability Notes

> [!warning] Caveats
> - **LangChain vendor engineering blog.** Promotes LangChain/LangGraph/Deep Agents/LangSmith. Confidence **0.8** on the patterns and the qualitative framework (well-reasoned and broadly consistent with the field); lower on the specific performance figures, which are LangChain's own small-scenario analysis rather than an independent benchmark.
> - Architecture diagrams not pixel-parsed; content captured from surrounding text/tables.
> - The 90.2% multi-agent advantage is attributed to **Anthropic's** internal research evals — domain-specific, not a general claim.
> - **Tension to flag when synthesizing:** this post's optimistic multi-agent stance must be balanced against [[sources/hai-cooperbench-agent-teamwork|CooperBench]] (paired agents underperform a solo agent on conflict-prone work). They reconcile only if multi-agent benefit is read as conditional on *centralized, isolated* orchestration.

## Backfill Status

- Newly written 2026-06-22 from a full web capture (article read end-to-end; all tables transcribed into the raw capture). All sections populated. `coverage: substantial` — prose and tables fully captured; the per-pattern architecture diagrams and the docs-linked mermaid performance diagrams were not pixel-parsed.
