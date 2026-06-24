---
source_url: https://www.langchain.com/blog/choosing-the-right-multi-agent-architecture
captured: 2026-06-22
title: Choosing the Right Multi-Agent Architecture
authors: [Sydney Runkle]
published: 2026-01-14
publisher: LangChain Blog
---

# Choosing the Right Multi-Agent Architecture
**Author:** Sydney Runkle — **Published:** 2026-01-14 — LangChain Blog

> Immutable capture. AI-written summary, key points, short quoted excerpts, and diagram-content notes only — no full article text. See the source URL for the complete article. Reading time: ~7 min.

## Summary

A decision guide for when and how to adopt multi-agent architectures. The thesis is conservative: most tasks are best served by **a single agent with well-designed tools**, and teams should start there because single agents are simpler to build, reason about, and debug. Multi-agent designs become justified only when two pressures emerge as an application scales and teams try to combine sprawling capabilities into one coherent interface:

1. **Context management** — specialized knowledge for each capability doesn't fit comfortably in a single prompt; if context windows were infinite and latency zero you could include everything upfront, but in practice you need strategies to selectively surface information as agents work.
2. **Distributed development** — different teams develop and maintain each capability independently, with clear boundaries and ownership; a single monolithic prompt becomes hard to manage across team boundaries.

The post cites Anthropic's multi-agent research system as evidence that multi-agent helps in these situations: a system with **Claude Opus 4 as lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2%** on internal research evaluations, because distributing work across agents with separate context windows enabled parallel reasoning a single agent couldn't achieve.

It then lays out **four architectural patterns** — Subagents, Skills, Handoffs, Router — each differing in task coordination, state management, and "sequential unlocking." It provides a requirements→pattern decision table, a capability-support star table, and three performance scenarios (one-shot, repeat, multi-domain) with model-call and token counts. The closing guidance: start with a single agent and good prompt engineering, **"add tools before adding agents,"** and graduate to multi-agent patterns only at clear limits. LangChain products are positioned throughout (Deep Agents for out-of-the-box subagents+skills; LangSmith for observability/eval).

## Key Points

- **Default to a single agent.** Multi-agent is a response to context-management and distributed-development pressures, not a starting point.
- **Anthropic evidence:** Opus 4 lead + Sonnet 4 subagents beat single Opus 4 by **90.2%** on internal research evals via parallel reasoning across separate context windows.
- **Subagents (centralized orchestration):** a supervisor agent calls specialized subagents *as tools*. Main agent holds conversation context; subagents are **stateless** → strong **context isolation**. Centralized control (all routing through main agent); can invoke subagents in parallel. **Key tradeoff: +1 model call per interaction** (results flow back through main agent → latency/token cost). Best for multiple distinct domains needing centralized control where subagents need not talk to the user directly (e.g. personal assistants coordinating calendar/email/CRM; research systems delegating to domain experts). Deep Agents gives an out-of-the-box implementation.
- **Skills (progressive disclosure):** a *single* agent loads specialized prompts/knowledge **on-demand**. Skills are prompt-driven specializations packaged as directories (instructions, scripts, resources). At startup the agent knows only skill **names + descriptions**; it loads full context when a skill becomes relevant; additional files provide a third level of detail discovered as needed. Author calls it (controversially) a **"quasi-multi-agent architecture"** — single agent, but with distributed development + fine-grained context control via a lighter, prompt-driven method. **Key tradeoff: context accumulates in conversation history as skills load → token bloat on subsequent calls.** Provides simplicity + direct user interaction. Best for single agents with many specializations, no need to enforce constraints between capabilities, team-distributed skill ownership (coding agents, creative assistants).
- **Handoffs (state-driven transitions):** the **active agent changes dynamically** based on conversation context; each agent can transfer to others via tool calling. Calling a handoff tool **updates state** that determines the next agent (switch agent, or change the current agent's system prompt + available tools). **State survives across turns** → sequential workflows. **Key tradeoff: most stateful → careful state management required**; enables fluid multi-turn conversations where context carries forward. Best for staged customer-support flows, multi-stage conversational experiences, sequential constraints where capabilities unlock after preconditions are met.
- **Router (parallel dispatch + synthesis):** a routing step classifies input and directs it to specialized agents, executing in parallel and synthesizing results. Router decomposes the query, invokes **zero or more** specialized agents in parallel, synthesizes a coherent response. **Typically stateless** (each request independent). **Key tradeoff: stateless = consistent per-request performance but repeated routing overhead if you need conversation history** (mitigate by wrapping the router as a tool inside a stateful conversational agent). Best for distinct verticals/knowledge domains, parallel multi-source queries, result synthesis (enterprise knowledge bases, multi-vertical support).
- **Getting started:** "Start with a single agent and good prompt engineering. **Add tools before adding agents.** Graduate to multi-agent patterns only when you hit clear limits." Deep Agents combines subagents + skills out of the box for complex task planning.

## Short Quoted Excerpts

- "Many agentic tasks are best handled by a single agent with well-designed tools. You should start here."
- "If context windows were infinite and latency was zero, you could include all relevant information upfront. In practice, you need strategies to selectively surface information as agents work."
- "perhaps controversially, we consider skills to be a quasi-multi-agent architecture."
- "In this scenario, Subagents processes 67% fewer tokens overall compared to Skills due to context isolation."
- "Start with a single agent and good prompt engineering. Add tools before adding agents."

## Diagrams (content captured from text/captions)

The post contains a hero image plus one architecture diagram per pattern (Subagents, Skills, Handoffs, Router) and one diagram per performance scenario. web_fetch returned all as bare `![](url)` with no alt text; content is reconstructed from the surrounding prose and the tables, which are detailed.

**Per-pattern architecture diagrams** (one each, captioned only by the section prose):
- *Subagents diagram* — illustrates a central supervisor/main agent that calls subagents as tools; results flow back up through the supervisor (the source of the +1 model call). Subagents are stateless boxes with isolated context.
- *Skills diagram* — illustrates one agent that loads skill bundles (name/description → full context → deeper files) on demand; progressive-disclosure layering.
- *Handoffs diagram* — illustrates the active agent transferring control to another agent via a handoff tool that mutates shared state across turns.
- *Router diagram* — illustrates a routing/classification step fanning out to multiple specialized agents in parallel, then a synthesis step combining results.

**Requirements → pattern decision table** (verbatim mapping):
| Your requirements | Pattern |
| --- | --- |
| Multiple distinct domains (calendar, email, CRM), need parallel execution | Subagents |
| Single agent with many possible specializations, lightweight composition | Skills |
| Sequential workflow with state transitions, agent converses with user throughout | Handoffs |
| Distinct verticals, query multiple sources in parallel and synthesize results | Router |

**Capability-support table** (⭐ = degree of support, — = not supported):
| Pattern | Distributed development | Parallelization | Multi-hop | Direct user interaction |
| --- | --- | --- | --- | --- |
| Subagents | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐ |
| Skills | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Handoffs | — | — | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Router | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | — | ⭐⭐⭐ |
(Definitions: distributed development = can teams maintain components independently; parallelization = can agents run concurrently; multi-hop = supports calling subagents in series; direct user interaction = can subagents converse with the user directly.)

**Performance scenario tables** (each scenario also had a mermaid-style diagram in the post; full breakdown is in LangChain's multi-agent performance docs):
- *Scenario 1 — one-shot ("buy coffee"):* Subagents = 4 model calls (results flow back through main agent); Skills / Handoffs / Router = 3 each (direct execution). Insight: Subagents pays +1 call for centralized control.
- *Scenario 2 — repeat request ("buy coffee" then "buy coffee again"):* Subagents Turn-2 = 4 calls, total 8 (no gain); Skills = 2 / total 5 (40% gain); Handoffs = 2 / total 5 (40% gain); Router = 3 / total 6 (25% gain). Insight: stateful patterns (Handoffs, Skills) save 40–50% on repeats; Subagents holds consistent cost via stateless isolation.
- *Scenario 3 — multi-domain ("Compare Python, JavaScript, and Rust for web development," ~2000 tokens of docs per language agent):* Subagents = 5 calls / **~9K tokens** (each subagent isolated); Skills = 3 calls / **~15K tokens** (context accumulation); Handoffs = 7+ calls / ~14K+ tokens (sequential, can't parallelize consultation); Router = 5 calls / **~9K tokens** (parallel). Insight: parallel patterns (Subagents, Router) are most token-efficient; **Subagents processes ~67% fewer tokens than Skills** because context isolation avoids the bloat of loading multiple skills into one conversation.

**Performance summary table** (✅ = optimal, — = not optimal):
| Pattern | Single requests | Repeat requests | Parallel execution | Large-context domains |
| --- | --- | --- | --- | --- |
| Subagents | — | — | ✅ | ✅ |
| Skills | ✅ | ✅ | — | — |
| Handoffs | ✅ | ✅ | — | — |
| Router | ✅ | — | ✅ | ✅ |

## Provenance Notes
- Primary source: LangChain engineering blog (vendor). Author Sydney Runkle. Published 2026-01-14.
- Vendor lens: promotes Deep Agents (subagents+skills) and LangSmith (observability/eval). Performance numbers are LangChain's own analysis of representative scenarios, not an independent benchmark.
- The 90.2% figure is attributed to Anthropic's "multi-agent research system" engineering post (linked from the article).
