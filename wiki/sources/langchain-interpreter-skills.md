---
type: source
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [agent-skills, progressive-disclosure, ai-coding-tools, interpreter-skills, code-execution, harness-engineering, product-evals, deep-agents, langchain]
source_path: raw/web/langchain-interpreter-skills-2026-06-22.md
source_url: https://www.langchain.com/blog/interpreter-skills
authors: [Hunter Lovell]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.8
---

# Interpreter Skills (deterministic code-as-skill: "discretion outside, determinism inside")
**Author:** Hunter Lovell (LangChain) — **Published:** 2026-05-29 — LangChain Blog
**Raw capture:** [[raw/web/langchain-interpreter-skills-2026-06-22|langchain-interpreter-skills-2026-06-22]]
**URL:** [langchain.com/blog/interpreter-skills](https://www.langchain.com/blog/interpreter-skills)

## Citation

Lovell, H. (2026, May 29). *Building workflows for agents with Skills and Interpreters.* LangChain Blog. Captured 2026-06-22 into `raw/web/langchain-interpreter-skills-2026-06-22.md`.

## Summary

Introduces **interpreter skills**: an extension to [[concepts/ai-agents/agent-skills|agent skills]] that bundles a **TypeScript module** with the skill's instructions, which the agent can **import and run inside an interpreter** when the behavior applies. It builds on LangChain's recently-added **interpreters** in Deep Agents — a small embedded TypeScript runtime where agents write and execute code *as part of the harness*. The motivating problem: an interpreter-equipped agent, given the same task repeatedly, often invents *several valid* code approaches, but for many tasks you don't want "a good approach," you want "the approach we know works." Interpreter skills resolve this — `SKILL.md` tells the agent *when* the behavior is relevant (discovered via [[concepts/ai-agents/progressive-disclosure|progressive disclosure]]); an attached `index.ts` module is *what* the interpreter executes.

The core reframe: a skill becomes **both an instruction surface for the model and an API surface for the runtime**. A normal skill works through instructions the model must read and follow correctly; an interpreter skill ships a **code path**, so the **deterministic part lives in reviewable, testable, versioned code** while the model still decides *whether* the skill applies, *which inputs* to pass, *how* to use the output, and *what to do next*. Because interpreter code can **interact with the harness**, a skill can do what a plain script can't — most notably **spawn subagents programmatically**. The worked example is **GitHub repo triage**: `triage(repo, options)` fetches open items, spawns a **subagent per item** to condense it, queues the results, then consumes the queue where a subagent clusters each item; it returns structured data (`result.clusters`, `result.unassigned`) plus a `result.toMarkdown()` helper. The payoff is **context offloading**: rather than forcing the model to track ~300 partial states (risking shortcuts near the edge of working context — "**context anxiety**"), the model invokes the routine **once** and lets code instrument the workflow.

An important distinction for security: an **interpreter is not a sandbox**. Interpreter code gets **no unrestricted host access by default** — filesystem, network, tools, and subagents must be **deliberately exposed**, giving the harness a place to **allowlist, meter, and inspect** what code can touch (interpreter values also persist across turns as working state). The post frames interpreter skills as reconciling two eras — older **workflow-style** agents (predefined step sequence; reliability from a fixed path) vs **modern discretion-driven harnesses** — capturing the best of both: "**discretion on the outside, determinism on the inside.**" A bonus is **cleaner evaluation** ([[concepts/ai-agents/product-evals|product evals]]): shift from "did the agent generally follow instructions?" to "did it call the expected function, with the expected inputs, returning the expected output shape?"

It extends [[sources/agent-skills-day-3|Day 3 Agent Skills]] (skills + progressive disclosure as the packaging unit) by adding executable code to the package, complements [[sources/langchain-background-subagents|Background Subagents]] (skill code spawns subagents and manages a task graph/queue), and instantiates the [[concepts/ai-agents/harness-engineering|harness-engineering]] idea that determinism belongs in the scaffolding, not the prompt.

## Key Claims

- **Skills can now direct the harness, not just the model** — interpreter code talks to the agent loop, so a skill can spawn subagents, manage a task graph, and handle partial failures as one reviewed workflow.
- **A skill becomes both instructions and an API:** `SKILL.md` (when to use it, discovered via progressive disclosure) + an `index.ts` module the interpreter runs. The model decides whether/which-inputs/what-next; the module defines how the procedure runs.
- **The deterministic part should live in code, not prompts** — "models are not guaranteed to write the same code twice," so when the procedure matters it belongs in reviewable, testable, versioned skill code.
- **Interpreter ≠ sandbox:** interpreter code has no host access by default; filesystem/network/tools/subagents must be deliberately exposed, giving the harness a metering/inspection point; values persist across turns.
- **Interpreter skills yield cleaner evaluation signals** — concrete "did it call the expected function with expected inputs and output shape?" vs fuzzy "did it generally follow instructions?".
- **Prompt-only procedure following is brittle** — the agent can skip/reorder steps, satisfy the wrong instruction, mix in unrelated requests, or stop at "good enough" (the "submit an invoice but pause to generate a dancing-cat gif" failure).
- **Design FAQ:** package as a skill (de-facto distribution unit + progressive disclosure; can't wire thousands of modules directly to the harness); not a script (scripts can't participate in the harness loop — subagents, task graphs, partial failures, "done"); not every-API-a-tool (would bloat the action surface; lean on TypeScript "already prominent in the weights").

## Useful Examples

- **GitHub repo-triage workflow** (`triage(repo, options)`) — fetch items → subagent-per-item to condense → queue → cluster via subagents → return `result.clusters` / `result.unassigned` / `result.toMarkdown()`. A template for "fixed procedure, dynamic inputs," and for offloading many-small-decisions work out of the model's context.
- **CSV table skill** — exports `parseCsv`, `joinTables`, `filterRows`, `validateRows`, `groupBy`, `summarize`, `toCsv`; the agent composes them in interpreter code while the **skill author owns** what "join/validate/summarize" mean. Shows skills as a way to operate on **agent state** reproducibly (vs the model writing one-off helpers).
- **"Discretion on the outside, determinism on the inside"** — a compact design principle for any agent with a few critical subroutines: keep the model in charge of *when*, put the *how* in tested code.
- **The evaluation reframe** — packaging procedures as callable functions converts fuzzy adherence questions into concrete, checkable ones (function called? right inputs? right output shape?).
- **The allowlist/meter/inspect boundary** — exposing filesystem/network/tools/subagents *deliberately* to the interpreter is a reusable pattern for safely giving agents code execution without sandbox-level host access.

## Constraints / Caveats

- **Vendor / experimental.** Explicitly "we're experimenting with interpreter skills." Anchored on Deep Agents' TypeScript interpreter and the skills standard; the *idea* (deterministic code packaged as a skill, run in a metered runtime, invoked by a discretionary model) is portable, but the `metadata.module` / `@/skills/...` import API and TypeScript runtime are LangChain/Deep Agents-specific.
- **No evaluation/benchmarks.** Claims of "more efficient, accurate, predictable" outputs and reduced context anxiety are argued via examples, not measured; no quantitative comparison of interpreter-skill vs prompt-only triage.
- **Determinism is bounded.** The post is explicit that this "doesn't get rid of the issue that agents might come up with creative solutions" — the model still chooses *when* to call and *what inputs* to pass; only the called procedure is fixed.
- **Security is allowlist-dependent.** "Not a sandbox" means safety rests on the harness correctly allowlisting/metering exposed capabilities; mis-exposing tools/network/subagents reintroduces risk, and the post doesn't detail the allowlist threat model.
- **Maintenance burden shifts to code.** Reviewable/testable/versioned skill modules are an asset but also real software to own (skill authors must maintain APIs, handle partial failures, keep modules working across runtime changes).
- **TypeScript-centric.** The argument leans on TypeScript being "prominent in the weights"; portability to other interpreter languages/runtimes is assumed, not shown.

## Design Implications

- **Put critical subroutines in interpreter-skill code, not prompts.** When a procedure must run the same way every time (and the inputs vary), express it as a module the model calls — "discretion outside, determinism inside."
- **Use code to offload many-small-decisions work** out of the model's context window (the repo-triage pattern): let a function spawn/collect/cluster N subagent tasks and return a compact object, instead of making the model track N partial states (mitigates context anxiety). Pairs with [[sources/langchain-background-subagents|async subagents]] for the spawning machinery.
- **Treat the interpreter boundary as a security control:** expose filesystem/network/tools/subagents to interpreter code **deliberately** and meter/inspect them — get code execution without sandbox-level host access.
- **Package procedures as skills for distribution** ([[concepts/ai-agents/progressive-disclosure|progressive disclosure]] + [[concepts/ai-agents/agent-skills|skills]]) so behavior is discoverable, versioned, shared, and evaluable without wiring every module into the harness.
- **Design evals around function calls** ([[concepts/ai-agents/product-evals|product evals]]): assert the expected function ran with expected inputs and returned the expected shape, instead of grading fuzzy instruction-following.
- **Reserve tools for external boundaries** and local helpers (parse/join/validate) for interpreter code — keep the action surface small so the model chooses among fewer, larger actions.

## Tensions

- **Determinism vs autonomy/adaptability.** Fixing the procedure improves reliability and evaluability but trades away the model's freedom to "come up with a good approach"; the post keeps discretion at the boundary (when/what-inputs) to soften this, but the tension is real.
- **Workflow-style vs discretion-style agents.** Interpreter skills are an explicit attempt to re-introduce predefined-execution-path reliability into discretion-driven harnesses "without re-architecting the agent" — a hybrid that inherits some friction of both.
- **Code as asset vs code as burden.** Reviewable/testable/versioned modules beat brittle prompt instructions, but they are software to maintain (APIs, partial-failure handling, runtime drift) — pushing maintenance from prose into engineering.
- **"Not a sandbox" power vs safety.** Letting code spawn subagents and touch tools/files is what makes interpreter skills capable, and also what makes the allowlist/metering boundary load-bearing; capability and risk scale together.
- **Portable idea vs vendor implementation.** The concept generalizes, but the demonstrated mechanism (Deep Agents interpreter, TypeScript modules, the skill `metadata.module` field) is LangChain's.

## Open Questions

- How much do interpreter skills actually improve reliability, efficiency, and evaluability vs prompt-only procedures (no benchmarks given)?
- What is the threat model and the concrete allowlist/metering policy for exposed filesystem/network/tools/subagents — and how do teams audit it given "not a sandbox"?
- How do interpreter-skill modules version and degrade safely as the interpreter runtime, exposed tools, and models change over time?
- Where exactly should the discretion/determinism line sit per task — when is fixing the procedure worth the lost adaptability?
- How portable is the pattern beyond a TypeScript interpreter (other languages/runtimes), and beyond Deep Agents?
- (Image gap) The "workflow-style vs discretion-style agents" screenshot (1.58 PM) may juxtapose the two paradigms more directly than the prose; the textual contrast is captured, but the visual framing of the two eras side-by-side is not pixel-parsed.

## Concepts Linked

- [[concepts/ai-agents/agent-skills|Agent Skills]] — interpreter skills are an extension of the skills standard: same packaging/discovery, plus an executable module.
- [[concepts/ai-agents/progressive-disclosure|Progressive Disclosure]] — the discovery mechanism that lets the agent see a short skill list and load full `SKILL.md` only when relevant; preserved by interpreter skills.
- [[concepts/ai-agents/ai-coding-tools|AI Coding Tools]] — built on the agent writing and executing code in an interpreter; "agents are already very good at writing code."
- [[concepts/ai-agents/harness-engineering|Harness Engineering]] — interpreter code runs "as part of the harness"; determinism is engineered into the scaffolding, with the harness allowlisting/metering what code touches.
- [[concepts/ai-agents/product-evals|Product Evals]] — the cleaner evaluation signal: assert the expected function ran with expected inputs/output shape, not fuzzy instruction-following.
- [[concepts/ai-agents/context-rot|Context Rot]] — the "context anxiety" motivation: models lose coherence / take shortcuts tracking many partial states near the edge of working context; interpreter skills offload that state into code.
- [[concepts/ai-agents/multi-agent-architecture|Multi-Agent Architecture]] — skill code spawns subagents programmatically and manages a queue/task graph (the repo-triage routine).
- (new) concepts/ai-agents/interpreter-skill — a skill that bundles executable code (a module) the agent imports and runs in a metered interpreter, making the deterministic part of a procedure reviewable/testable/versioned while the model decides when to invoke it.
- [[concepts/ai-agents/agent-interpreter|Agent Interpreter & Interpreter Skills]] (new) — an embedded code runtime running in tandem with the harness (no host access by default; capabilities deliberately exposed) that gives the agent persistent working state and a direct way to express multi-step work as code (distinct from a sandbox).

## LLM Use

- **Use for:** explaining interpreter skills (skill = instructions + runnable module); the "discretion outside, determinism inside" principle; why prompt-only procedure following is brittle; the interpreter-vs-sandbox security distinction (deliberate capability exposure); how code execution offloads many-small-decisions work to mitigate context anxiety; the evaluation reframe (function-call assertions); the FAQ rationale (skill vs script vs tool).
- **Do not use for:** claiming measured efficiency/reliability gains (none given); treating it as production-stable (explicitly experimental); assuming "not a sandbox" is automatically safe (depends on allowlisting); treating the TypeScript-module API / `metadata.module` field as stable or framework-neutral; assuming the called procedure removes all nondeterminism (the model still chooses when/which inputs).
- **Best prompt pattern:** "For this agent, identify the few critical subroutines whose procedure must be fixed but whose inputs vary. For each, draft an interpreter skill: a `SKILL.md` (when to invoke it) and a module API (the deterministic steps, including any subagent spawning / queueing). State which host capabilities the interpreter must expose (and how they're metered), and define the eval as concrete function-call assertions (function, inputs, output shape)."

## Reliability Notes

> [!warning] Caveats
> - **LangChain vendor, experimental.** Promotes Deep Agents' interpreter + the skills standard; framed as an experiment ("we're experimenting with interpreter skills"). Confidence **0.8** on the *concepts* (interpreter-as-skill, discretion/determinism split, interpreter≠sandbox, function-call evals — durable and well-argued); lower on the specific TypeScript-module/`metadata.module`/`@/skills/...` API (versioned, will drift) and on any implied efficacy (no evaluation provided).
> - Architecture diagrams not pixel-parsed; content captured from surrounding text/captions (the repo-triage routine, the progressive-disclosure flow, the workflow-vs-discretion contrast, and the evaluation contrast are described in prose and transcribed).
> - "Not a sandbox" safety depends on the harness's allowlist/metering of exposed filesystem/network/tools/subagents — treat security as policy-dependent, not inherent.

## Backfill Status

- Newly written 2026-06-22 from a full web capture (article read end-to-end; repo-triage and CSV examples, the FAQ, and the interpreter-vs-sandbox distinction transcribed). All sections populated. `coverage: substantial` — prose, code examples, and FAQ fully captured; the four screenshots (progressive disclosure, repo-triage workflow, workflow-vs-discretion, evaluation signal) were not pixel-parsed (content described from prose; one possible image gap flagged under Open Questions).
