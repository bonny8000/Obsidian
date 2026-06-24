---
source_url: https://www.langchain.com/blog/how-we-made-coding-agent-spend-predictable
captured: 2026-06-22
title: How We Made Coding Agent Spend Predictable
authors: [Martha Janicki]
published: 2026-06-15
publisher: LangChain Blog
---
# How We Made Coding Agent Spend Predictable
**Author:** Martha Janicki **Published:** 2026-06-15 — LangChain Blog (LangSmith)

## Summary

A LangChain engineering/dogfooding post on how the company brought its own AI/coding-agent spend under real-time control using **LangSmith LLM Gateway**. The premise: for years AI usage was easy to ignore in a budget (few teams, predictable usage, manageable bills), but three things changed at once — AI usage spread from a few teams to the whole company, the best models got more expensive, and agents became powerful enough to fire off dozens of model calls per task. The sharpest pain showed up in engineering: a single developer using coding agents heavily could rack up thousands of dollars in weekly spend before anyone noticed. Leadership needed to see spend *as it happened*, set limits by team and user, and prevent accidental runaway usage without blocking productive work.

The solution was to build LLM Gateway directly into the product the team uses daily and route every eligible coding-agent call (Claude Code, Codex, LangChain Deep Agents) through it, orchestrated centrally via MDM so individual users don't self-configure. Budgets can be set across organization, workspace, user, and API-key dimensions, on monthly/weekly/daily/hourly windows with per-person exceptions. Because Gateway is part of LangSmith, spend data is connected to tracing, observability, and evals — so cost can be tied to specific agents, calls, traces, and failure modes, not just a monthly bill. The post is candid about lessons from dogfooding: model pricing is more complex than a static table; not every client routes cleanly; and hard limits need a workflow (alerts + increase-requests) around them. Result: LLM costs have stayed within budget and spend is understood in real time rather than at month-end.

## Key Points

- **Why AI spend became hard to control:** usage went company-wide; top models got pricier; agents now make dozens of calls per task — so spend got harder to understand and control in real time.
- **The acute risk:** one developer on coding agents could generate thousands of dollars of weekly spend before anyone noticed.
- **Goal:** real-time visibility, limits by team/user, and prevention of accidental runaway usage *without* blocking productive work — peace of mind for both the VP of Engineering and Head of Finance.
- **LangSmith LLM Gateway** budgets across four dimensions: **Organization-wide, Workspace, User, API key**.
- **Default budgets** on **monthly, weekly, daily, and hourly** windows, with exceptions for projects needing higher usage.
- **Applied everywhere centrally possible:** coding agents via **Claude Code, Codex, or LangChain Deep Agents**; every eligible call routes through the Gateway, giving leadership a to-the-minute company-wide spend view. Rolled out centrally through **MDM** so users don't self-configure.
- **Connected to the LangSmith stack:** Gateway runs can be traced, attributed to users/keys, and analyzed alongside production data; reuses existing LangSmith OAuth, model management, and user management instead of a standalone proxy. Overspend can be inspected at the trace level and fed back into evals/observability to improve agent behavior.
- **Lesson 1 — pricing is a system, not a table:** static lookup tables go stale; accurate cost accounting must absorb caching, token-tier nuance, and frequent provider price changes; they're auditing calculation logic and building a rigorous update path.
- **Lesson 2 — not every client routes cleanly:** support varies by app/management. **Cursor** only exposed a per-user base-url swap covering Chat (not MDM-pushable); **Claude Desktop** could only pass through as a managed config, and enabling it shifted the app into a local agent in place of standard Chat (early-stage). Response: **measure the delta** between what Gateway captures vs what other enterprise provider settings capture (e.g., monthly Claude plans) so spend is accounted for even when traffic can't flow through Gateway.
- **Lesson 3 — hard limits need a workflow around them:** a cap with no runway just blocks work. Engineers wanted early warning before a limit and a fast, auditable way to raise it → moving to **tiered alerting** ahead of thresholds and a **paper-trailed budget-increase request flow**.
- **Result:** since the internal rollout, LLM costs have stayed within budget; spend is understood in real time, not just at month-end. LLM Gateway is in **private beta**.

## Diagrams (content from text/captions)

The post's only embedded images are the hero banner (`dark-77 characters max.png`), the author headshot, and related-post thumbnails — there are no explanatory architecture/data diagrams in the body, so there is no diagram content to recover beyond the prose above.

## Short Quotes

- "One developer using coding agents heavily could generate thousands of dollars in weekly spend before anyone noticed."
- "Model pricing is more complex than a static table... accurate cost accounting has to absorb caching, token-tier nuances and frequent provider prices changes."
- "A cap with no runway just blocks work."
- "The upside of Gateway is that there is more certainty with centralized control that I won't open my dashboard and see a surprise multi-thousand dollar bill." — Alex Lunev, VP of Engineering, LangChain
- "Spend is no longer something we only understand at the end of the month."
