---
source_url: https://www.langchain.com/blog/the-art-of-loop-engineering
captured: 2026-06-22
title: The Art of Loop Engineering
authors: [Sydney Runkle]
published: 2026-06-16
publisher: LangChain Blog
---

# The Art of Loop Engineering
**Author:** Sydney Runkle — **Published:** 2026-06-16 — LangChain Blog

> Immutable capture. AI-written summary, key points, short quoted excerpts, and diagram-content notes only — no full article text. See the source URL for the complete article. Reading time: ~7 min.

## Summary

A framework for designing the agent loop as a *stack of nested loops* rather than a single model→tool→observation cycle. The premise: getting agents to do valuable work reliably takes more than a good model — it requires a carefully designed **harness** fit to a set of tasks. The core agent algorithm is simple ("give the LLM context and let it call tools in a loop until it's done"), but it is far from the only loop. Building on Swyx's "loopcraft: the art of stacking loops," the post defines **four levels** that stack and reach inside one another, then maps each to LangChain primitives. A single running example — LangChain's internal **docs-writer agent** — threads through all four levels.

The four loops:
1. **Loop 1 — The Agent:** a model calling tools in a loop until the task is complete. Tools give it power to act (clone repos, read files, write docs, open PRs). Implemented by `create_agent`.
2. **Level 2 — Verification loop:** wrap the agent in a **grader** that checks output against a rubric and, on failure, sends the result back with feedback. Graders can be **deterministic or agentic** (LLM-as-judge). For the docs agent: run tests after each attempt — links resolve, CI passes, diff is scoped to the request. Tradeoff: adds latency/cost per run; worth it when quality > speed (most production cases). Implemented by `RubricMiddleware` or an `after_agent` hook.
3. **Level 3 — Event-driven loop:** connect the agent to its ecosystem so it runs **in the background**, triggered by events (a new document, a schedule/cron, a webhook). The agent becomes a component running continuously inside a larger system, not something invoked manually. Supported by LangSmith Deployment (crons/webhooks) or Fleet channels/schedules (the docs agent fires on messages in a `#docs-plz` Slack channel). Cites "heartbeats" in openclaw as an always-on, proactive pattern.
4. **Level 4 — Hill-climbing loop:** automate **improvement**, not just work. Every run produces a **trace** (what the model did, tools called, grader feedback); an **analysis agent** runs over traces and **rewrites the harness config** (prompt/tool/grader tweaks). The key move: the return arrow doesn't just loop to the top — it **reaches inside and updates the inner agent loop directly**, so each outer cycle makes inner loops more effective. Implemented by LangSmith Engine. Forward-looking: traces can also feed RL fine-tuning for open-weight models, or improve memory/retrieved-skills — "the loop is the pattern; what it optimizes is up to you."

A recurring theme is **human oversight at every level**: require human input before sensitive actions in the agent loop; a human as grader in the verification loop; human approval of outputs in the application loop; human review of harness improvements before deployment. Closing argument: focus is shifting from loops 1–2 (well understood) to loops 3–4, "where value compounds by embedding agents into your ecosystem." Cites Satya Nadella's framing that companies building learning loops early — "where human judgment and token capital compound together" — gain hard-to-replicate advantage. Names Steipete, Boris, and Andrej Karpathy as arriving at the same conclusion: "the potential in agents is in the loops you build around them."

## Key Points

- **An agent is a model calling tools in a loop**; reliability comes from the harness around it, fit to the task — not from the model alone.
- **Loops stack** (loopcraft, per Swyx): Agent → Verification → Event-driven → Hill-climbing.
- **Verification loop = grader + feedback + retry.** Graders are deterministic (tests, link checks, scope checks) or agentic (LLM-as-judge). Tradeoff: latency/cost vs quality.
- **Event-driven loop = triggers** (new doc, cron, webhook) that make the agent an always-on background component, not a manual invocation.
- **Hill-climbing loop = trace-driven self-improvement:** an analysis agent reads production traces and rewrites prompts/tools/graders. The feedback arrow reaches *inside* the agent loop, compounding gains each cycle. Can extend to RL fine-tuning and memory/skill improvement.
- **Human-in-the-loop is a first-class primitive at all four levels** (input gate, grader, output approval, harness-change review).
- **Strategic emphasis:** loops 1–2 are mature; the leverage is in 3–4 — embedding agents in the ecosystem and continuously improving them against your criteria.
- **LangChain primitive map:** Loop 1 → `create_agent` (any supported model); Loop 2 → `RubricMiddleware`; Loop 3 → LangSmith Deployment (cron/webhooks) or Fleet channels; Loop 4 → LangSmith Engine.

## Short Quoted Excerpts

- "The core agent algorithm is simple: give the LLM context and let it call tools in a loop until it's done."
- "The first three loops automate work. The fourth (and arguably most important) automates improvement!"
- "The key move here is that the return arrow doesn't just loop back to the top — it reaches inside and updates the agent loop directly. Each cycle of the outer loop makes the inner loops more effective."
- "The loop is the pattern; what it optimizes is up to you."
- "the potential in agents is in the loops you build around them."
- (Satya Nadella, quoted) companies that "build learning loops early, where human judgment and token capital compound together, will build an advantage that's hard to replicate."

## Diagrams (content captured from text/captions)

The post is heavily diagram-driven: a generic schematic for each of the four loops plus a parallel docs-writer-agent instantiation of each. web_fetch returned all as bare `![](url)` with no alt text; reconstructed from prose. There is a final tabular recap (captured verbatim below) that summarizes the diagram content.

- *Loop 1 (generic + docs-writer):* a single model node looping through tool calls until done. Docs-writer version: request → plan/draft → tools (clone repo, read files, write docs, open PR) → loop.
- *Loop 2 (generic + docs-writer):* the Loop-1 box wrapped by a grader node; on failure, an arrow returns the output to the model with feedback; on pass, it exits. Docs-writer version: grader runs tests (links resolve, CI passes, diff scoped) after each attempt.
- *Loop 3 (generic + docs-writer):* an external event source (document/cron/webhook) feeding into the agent, which writes back to a real system. Docs-writer version: a Slack `#docs-plz` channel event fires the agent.
- *Loop 4 (generic + docs-writer):* production traces flowing to an analysis agent whose output arrow reaches *inside* the agent loop to update prompt/tool/grader config. Docs-writer version: LangSmith Engine runs over docs-agent traces; when multiple traces signal a problem, it files an issue to change the offending prompt/tool.

**Recap table (verbatim — summarizes the four diagrams):**
| Loop | What it does | Impact | LangChain primitive |
| --- | --- | --- | --- |
| 1. Agent loop | Model calls tools repeatedly until a task is complete | Automate work | `create_agent`, any LangChain-supported model |
| 2. Verification loop | Agent runs, output scored against a rubric, retried with feedback if it fails | Ensure work quality and correctness | `RubricMiddleware` |
| 3. Event driven loop | Events trigger agent runs that update a real system | Automated work at scale | LangSmith Deployment with cron triggers / webhooks, or Fleet channels |
| 4. Hill climbing loop | Traces from production runs feed an analysis agent that improves the harness config | Harness improvements | LangSmith Engine |

## Provenance Notes
- Primary source: LangChain engineering blog (vendor). Author Sydney Runkle. Published 2026-06-16.
- Builds explicitly on Swyx's "loopcraft" essay (Latent Space) and references openclaw "heartbeats."
- Vendor lens: each loop is mapped to a LangChain/LangSmith product (`create_agent`, RubricMiddleware, LangSmith Deployment/Engine, Fleet).
- Acknowledgements: Vivek, Mason, Harrison (hwchase17), Hunter.
