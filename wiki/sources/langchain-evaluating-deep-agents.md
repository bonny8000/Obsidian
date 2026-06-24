---
type: source
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [deep-agents, agent-evaluation, trajectory-evaluation, llm-as-judge, single-step-evals, eval-environments, langsmith, agent-architecture, langchain]
source_path: raw/web/langchain-evaluating-deep-agents-2026-06-22.md
source_url: https://www.langchain.com/blog/evaluating-deep-agents-our-learnings
authors: [The LangChain Team]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.8
---

# Evaluating Deep Agents: Our Learnings (Trajectory / Single-Step / Full-Turn / Multi-Turn Evals)
**Author:** The LangChain Team — **Published:** 2025-12-03 — LangChain Blog (Deep Agents / Tutorials & How-Tos)
**Raw capture:** [[raw/web/langchain-evaluating-deep-agents-2026-06-22|langchain-evaluating-deep-agents-2026-06-22]]
**URL:** [langchain.com/blog/evaluating-deep-agents-our-learnings](https://www.langchain.com/blog/evaluating-deep-agents-our-learnings)

## Citation

The LangChain Team. (2025, December 3). *Evaluating Deep Agents: Our Learnings.* LangChain Blog. Captured 2026-06-22 into `raw/web/langchain-evaluating-deep-agents-2026-06-22.md`. Learnings drawn from shipping four Deep Agents apps (DeepAgents CLI, LangSmith Assist, Personal Email Assistant, Agent Builder); references LangSmith Pytest/Vitest integrations and the Harbor eval environment.

## Summary

A practitioner post on **how to evaluate long-running, stateful deep agents**, distilled from writing eval suites for **four applications LangChain shipped on the Deep Agents harness in one month** (DeepAgents CLI, LangSmith Assist, a per-user-learning Personal Email Assistant, and the no-code Agent Builder). The core argument is that **deep agents break the assumptions of traditional LLM evaluation**: classic eval runs every datapoint through the same application logic and scores each output with the same evaluator, but deep agents emit more than a final message and their "success criteria" are frequently **per-datapoint**, requiring assertions against **trajectory** (tool sequence + tool args), **final response**, and **other state** (files, artifacts).

The post supplies a small but useful vocabulary — three **ways to run an agent** for eval (**single step**: constrain the core loop to one turn to validate the next action; **full turn**: run end-to-end on one input across many tool-call iterations; **multiple turns**: run repeatedly to simulate a multi-turn conversation) crossed with three **things to test** (trajectory, final response, other state) — and five operational learnings. (1) **Bespoke per-datapoint test logic in code**, with a calendar-scheduler memory example (`edit_file` on `memories.md` + confirmation in final message + content check via regex *or* LLM-as-judge), supported by LangSmith Pytest/Vitest. (2) **Single-step evals are valuable and cheap** — ~half of LangChain's cases; regressions cluster at individual decision points; LangGraph's `interrupt_before=["tools"]` inspects a single tool call without running the full sequence (and saves tokens). (3) **Full turns give the complete picture** — trajectory checks (a tool fired *at some point*, order-independent), final-response checks (best for open-ended coding/research), and state checks (read the files a coding agent wrote; assert a research agent found the right sources). (4) **Multi-turn evals must be "kept on rails"** via conditional logic (check after each turn; fail early on deviation) rather than hardcoded input chains. (5) **Eval environments must reset per test** (Harbor's Docker/sandbox for TerminalBench; a temp dir per DeepAgents-CLI test) and **API calls should be mocked/replayed** (`vcr` for Python; proxied `fetch` for JS) or evals go flaky and expensive.

This is the wiki's clearest worked guide to **evaluating agentic, long-horizon systems**, and the methodological complement to LangChain's own architecture pieces: it tells you how to *test* the recursive parent/child agents of [[sources/langchain-box-ai-deep-agents|Box Deep Agents]] and the Planner/Tasks/Observer system of [[sources/langchain-exa|Exa]], and it sits alongside the verifier/LLM-as-judge cost-engineering of [[sources/langchain-verifiers-legal-agents|Verifiers for Legal Agents]] and the eval-pyramid framing in [[sources/bayer-prince-reliable-agentic-ai|Bayer PRINCE]] and [[sources/vibe-coding-agent-security-evaluation-day-4|Day 4 Security & Evaluation]].

## Key Claims

- **Deep agents break traditional LLM eval.** Classic flow = one dataset, one evaluator, every datapoint scored identically. Deep agents need to test more than the final message, and success criteria are often **specific to each datapoint** (assertions against trajectory, final message, and state).
- **Two crossed taxonomies.** *Ways to run an agent:* **single step** (one core-loop turn → next action), **full turn** (end-to-end on one input, many tool-call iterations), **multiple turns** (repeat in full → simulate multi-turn conversation). *Things to test:* **trajectory** (tool sequence + arguments), **final response**, **other state** (files/artifacts).
- **Learning #1 — write bespoke per-datapoint test logic (code).** Each case carries its own criteria; assert against trajectory/final-message/state. LangSmith Pytest/Vitest support this and auto-log each case to an experiment with debuggable traces.
- **Learning #2 — single-step evals are valuable and efficient.** ~half of their cases; good for "did it call the right tool with the right args?"; **regressions often occur at individual decision points, not across full sequences**; LangGraph `interrupt_before=["tools"]` inspects one step (catches issues early, saves tokens).
- **Learning #3 — full turns give a complete picture** ("integration tests" vs single-step "unit tests"). Three modes: **trajectory** (tool called *at some point*, timing-agnostic), **final response** (quality matters more for open-ended coding/research), **other state** (test files a coding agent wrote; assert a research agent found the right links/sources).
- **Learning #4 — multi-turn evals must be kept on rails.** Hardcoded input sequences break on deviation; use conditional logic (run a turn, check, proceed-or-fail-early), or seed initial state to test a later turn in isolation — avoids modeling every branch.
- **Learning #5 — environment setup matters.** Deep agents are stateful/long-running and need **fresh, reproducible environments per run** or evals go flaky. Harbor = Dockerized/sandboxed env for TerminalBench; DeepAgents CLI = lightweight temp dir per test.
- **Tip — mock/replay external API calls.** Live services are slow/expensive (LangSmith Assist hits real LangSmith APIs); record + replay HTTP (`vcr` for Python; proxy `fetch` via a Hono app for JS) → faster, cheaper, debuggable.
- **You likely need only a subset of these patterns;** keep the eval framework flexible.

## Useful Examples

- **The 3×3 eval matrix** (single-step / full-turn / multi-turn × trajectory / final-response / other-state) — a reusable scaffold for deciding *how to run* and *what to assert* when evaluating any agentic system, not just deep agents.
- **The calendar-scheduler memory test** — a concrete bespoke-assertion recipe: (a) trajectory assert `edit_file` was called on `memories.md`; (b) LLM-as-judge that the final message confirmed the update; (c) state check that `memories.md` actually contains "9am" (regex) or passes a holistic LLM-as-judge. Shows mixing deterministic + LLM-judge assertions in one test.
- **Single-step via `interrupt_before=["tools"]`** — a transferable pattern: stop the agent before the tool node, inspect message history / tool-call args, assert on the decision without paying for a full run.
- **Order-independent trajectory assertion** ("a particular tool was called *at some point*") — the right check for tasks like scheduling where the agent legitimately needs a variable number of tool calls.
- **State-as-output evals** — for coding agents, read and test the written files; for research agents, assert the right links/sources were found — when the artifact, not the chat reply, is the deliverable.
- **On-rails multi-turn pattern** — conditional Pytest/Vitest logic that checks each turn and fails early on deviation, instead of brittle hardcoded conversation scripts.
- **Reproducible eval environments + request mocking** — Harbor (Docker/sandbox) vs temp-dir-per-test, plus `vcr`/proxied-`fetch` replay, as the operational backbone that keeps agent evals deterministic.

## Constraints / Caveats

- **Vendor engineering blog.** LangChain promoting its own stack — Deep Agents harness, LangGraph (`interrupt_before`, streaming), and LangSmith Pytest/Vitest testing integrations. The *patterns* are framework-agnostic; the *tooling* is LangChain's.
- **Qualitative, not benchmarked.** The only quantitative claim is "**about half** of our test cases were single-step." No accuracy, flakiness-reduction, cost, or coverage numbers are reported for the patterns themselves — these are experience-based learnings, not measured results.
- **Examples are illustrative.** The calendar-scheduler memory case and the code snippets are toy/representative; the post does not share the actual eval suites for the four production apps or their pass rates.
- **LLM-as-judge is invoked but not characterized here.** It is used in the worked example without discussion of judge reliability/cost — the verifier-design tradeoffs are covered in the companion [[sources/langchain-verifiers-legal-agents|Verifiers for Legal Agents]], not here.
- **Source typos** in two sentences (e.g. "environments that resets per test") — content is clear but the post is lightly edited.
- **Scope = how to test, not what "good" is.** It catalogs eval mechanics; it does not define target thresholds or what passing means for a given domain.

## Design Implications

- **For [[concepts/ai-agents/product-evals|product evals]] of agents:** stop assuming one-evaluator-fits-all; budget for **per-datapoint, code-level assertions** that test trajectory and state, not just the final message.
- **For [[concepts/ai-agents/long-horizon-tasks|long-horizon tasks]]:** layer evals like a test pyramid — many cheap **single-step** "unit" checks at decision points, fewer **full-turn** "integration" checks for end-state quality, selective **multi-turn** checks for realistic flows.
- **For trajectory vs outcome:** choose the assertion to the task — **trajectory/tool-call** checks for procedural correctness (right tool, right args, order-independent), **final-response** checks for open-ended generation (coding/research), **state** checks when the artifact is the deliverable.
- **For [[concepts/ai-agents/harness-engineering|harness engineering]]:** build in the ability to **run an agent for a single step** (interrupt before tools) and to **seed arbitrary initial state** — these are prerequisites for cheap, targeted agent evals.
- **For reliability/reproducibility:** treat the **eval environment** as part of the system — reset per test (Docker/sandbox or temp dir) and **mock/replay external APIs** so agent evals are deterministic, fast, and cheap.
- **For evaluating the architectures elsewhere in the wiki:** apply single-step evals to the spawn-or-handle decision of [[sources/langchain-box-ai-deep-agents|Box]]'s Global Agent and the Planner's task-generation in [[sources/langchain-exa|Exa]]; apply state/trajectory evals to their multi-document synthesis outputs.

## Tensions

- **Trajectory vs final-response evals.** Trajectory checks catch decision-point regressions but can be brittle to legitimate path variation; final-response checks tolerate path variation but can miss *how* the agent got there (and lean on LLM-as-judge). The post recommends both, but they pull in opposite directions on what "correct" means.
- **Bespoke per-datapoint tests vs scalability.** Per-case success criteria give precision but are labor-intensive to author and maintain — in tension with the "one dataset, one evaluator" economy of traditional eval. The post does not address how this scales to thousands of cases.
- **Single-step efficiency vs end-to-end realism.** Single-step evals are cheap and pinpoint regressions but validate decisions in isolation; real failures can be emergent across a full trajectory. Coverage requires both, raising total eval cost/complexity.
- **On-rails multi-turn vs realistic free-form interaction.** Keeping multi-turn tests "on rails" (fail early on deviation) makes them tractable but constrains them away from the open-ended, branching conversations real users produce — you test a narrowed slice of behavior.
- **Mocked/replayed environments vs production fidelity.** Recorded API replay makes evals fast and deterministic but can drift from live API behavior, so green evals may not reflect real external-system state.

## Open Questions

- How do **bespoke per-datapoint evals scale** to large datasets — is there tooling to template/share assertions, or does authoring cost grow linearly with cases?
- What are the **reliability and cost characteristics of the LLM-as-judge** steps used here? (Deferred to [[sources/langchain-verifiers-legal-agents|Verifiers for Legal Agents]].)
- How is **trajectory "correctness" scored** when multiple valid tool sequences exist — beyond "a tool was called at some point," is there partial credit or distance scoring?
- What **flakiness/coverage improvement** did reset-per-test environments and request mocking actually deliver? (No before/after numbers.)
- How do these patterns extend to **multi-agent** systems (parent/child as in [[sources/langchain-box-ai-deep-agents|Box]], Planner/Tasks/Observer as in [[sources/langchain-exa|Exa]]) where trajectory spans several agents and isolated context windows?
- **Image gap:** all in-body figures are bare `![]` images with no alt text or captions; the two glossary diagrams and the per-learning illustrations are reconstructed from prose. No metric/eval charts are present as image-only content (the load-bearing technical detail is in the two inline code snippets, which are text-captured).

## Concepts Linked

- [[concepts/ai-agents/deep-agents|Deep Agents]] — the subject: evaluating long-running, stateful agents built on the Deep Agents harness (DeepAgents CLI, LangSmith Assist, Email Assistant, Agent Builder).
- [[concepts/ai-agents/product-evals|Product Evals]] — practical eval engineering for shipped agent products (per-datapoint assertions, LangSmith Pytest/Vitest, traces).
- [[concepts/ux-research/ai-evals|AI Evals]] — methods for evaluating AI/LLM systems: trajectory, final-response, and state scoring; LLM-as-judge vs deterministic checks.
- [[concepts/ai-agents/vibe-coding-agent-evaluation|Vibe-Coding Agent Evaluation]] — DeepAgents CLI / coding-agent evals (read-and-test-the-files state evaluation; reset-per-test environments via Harbor/temp dirs).
- [[concepts/ai-agents/agent-verifiers|Agent Verifiers]] — the LLM-as-judge assertions used in the worked example are verifier components (cost/design tradeoffs deferred to the Harvey/Verifiers post).
- [[concepts/ai-agents/long-horizon-tasks|Long-Horizon Tasks]] — single-step vs full-turn vs multi-turn maps onto evaluating multi-step, long-running agent behavior.
- [[concepts/ai-agents/harness-engineering|Harness Engineering]] — single-step interruption (`interrupt_before`), state seeding, and reproducible environments are harness affordances that make eval possible.
- [[concepts/ai-agents/agent-trajectory-evaluation|Agent Trajectory Evaluation]] (new) — evaluating an agent by the sequence of tools it calls and the arguments it generates (vs final-output scoring); includes single-step decision checks and order-independent "tool-called-at-some-point" assertions.

## LLM Use

- **Use for:** designing eval suites for long-running/stateful agents; choosing *how to run* (single-step / full-turn / multi-turn) and *what to assert* (trajectory / final-response / state); justifying per-datapoint bespoke assertions; the `interrupt_before=["tools"]` single-step technique; on-rails multi-turn test design; reproducible eval-environment + API-mocking practices.
- **Do not use for:** quoting performance/accuracy numbers (only "~half of cases were single-step" is given); claiming a specific flakiness or cost reduction from these practices; treating it as a guide to *what good looks like* (it covers mechanics, not target thresholds); LLM-as-judge reliability specifics (see Verifiers for Legal Agents).
- **Best prompt pattern:** "Using LangChain's deep-agent eval matrix, design an eval plan for [agent]: list single-step checks at its key decision points, the full-turn trajectory/final-response/state assertions, any on-rails multi-turn flows, and the per-datapoint success criteria — then specify the reproducible environment (reset strategy + which external APIs to mock/replay)."

## Reliability Notes

> [!warning] Caveats
> - **Vendor lens.** LangChain engineering blog promoting Deep Agents, LangGraph, and LangSmith testing integrations. The eval *patterns* are framework-agnostic and credible; the *tooling references* favor LangChain primitives. Confidence **0.8** on the patterns/taxonomy (clear, well-reasoned, broadly applicable); lower on any implied effectiveness, since the post is qualitative (only "~half of cases were single-step" is quantified).
> - **No independent benchmarks or outcome metrics** for the practices themselves — these are experience-based learnings from four internal apps, not measured results.
> - **Examples are illustrative** (calendar-scheduler memory case, toy code snippets); the actual production eval suites and their pass rates are not shared.
> - Architecture diagrams not pixel-parsed; content captured from surrounding text/tables. All in-body figures are bare `![]` images with no alt/caption; the load-bearing technical content is in two text-captured code snippets, and no metric/eval charts exist as image-only content.

## Backfill Status

- Newly written 2026-06-22 from a full web capture (article read end-to-end via web_fetch; both code snippets transcribed into the raw capture). All sections populated. No prior thin version to upgrade. `coverage: substantial` — prose, glossary, and code snippets fully captured; bare-image figures reconstructed from text (no image-only metrics). LLM-as-judge cost/reliability detail intentionally left to the companion Verifiers source.
