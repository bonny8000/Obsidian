---
type: source
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [harness-engineering, coding-agents, static-analysis, eslint, mutation-testing, code-maintainability, agentic-technical-debt, sensors, inferential-review]
source_path: raw/web/fowler-sensors-coding-agents-2026-06-22.md
source_url: https://martinfowler.com/articles/sensors-for-coding-agents.html
authors: [Birgitta Böckeler]
sources: []
ingest_level: deep
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.9
---

# Böckeler: Maintainability Sensors for Coding Agents

**Authors:** Birgitta Böckeler (Distinguished Engineer, AI-assisted delivery, Thoughtworks)
**Published:** 2026-05-27 — martinfowler.com (Thoughtworks engineering)
**Raw capture:** [[raw/web/fowler-sensors-coding-agents-2026-06-22|fowler-sensors-coding-agents-2026-06-22]]
**URL:** [martinfowler.com/articles/sensors-for-coding-agents.html](https://martinfowler.com/articles/sensors-for-coding-agents.html)
**Companion piece:** Böckeler's earlier *harness engineering for coding agent users* (the guides + sensors mental model this article operationalizes).

## Citation

Böckeler, B. (2026, May 27). *Maintainability sensors for coding agents.* martinfowler.com. Captured 2026-06-22 into `raw/web/fowler-sensors-coding-agents-2026-06-22.md`.

## Summary

A hands-on, experiment-driven follow-up to Böckeler's [[concepts/ai-agents/harness-engineering|harness engineering]] model, which frames a coding-agent harness as a system of **guides** (instructions) and **sensors** (feedback that lets the agent self-correct before issues reach humans). This article focuses on **sensors that keep an AI-generated codebase maintainable**. The test bed is a TypeScript / Next.js / React analytics dashboard she rebuilt from scratch with AI and deliberately *without* maintainability guides, to isolate what sensor feedback alone can achieve.

The central distinction is **computational sensors** (deterministic — type checker, ESLint, Semgrep/SAST, dependency-cruiser, coverage, mutation testing, GitLeaks) vs **inferential sensors** (LLM-based reviews — security, data-handling, dependency-freshness, modularity/coupling). Sensors run at four points: **in-session** (continuous fast feedback), **CI pipeline** (re-run on clean infra after integration), **scheduled** (catch slow drift), and **production** (runtime feedback).

The headline finding: **computational sensors shine at the file/function level, but cross-file concerns (modularity, coupling) need an inferential LLM sensor** for semantic interpretation and trade-off judgment. Two techniques stand out: a **custom ESLint formatter that injects self-correction guidance** (and lets the agent suppress-with-reason or slightly raise a threshold instead of a binary choice), and **mutation testing (Stryker)** to catch missing assertions where coverage misleads. This is the practical, code-side counterpart to the system-side harness work in [[sources/bayer-prince-reliable-agentic-ai|the Bayer PRINCE case study]] (same publisher and genre).

## Key Claims

- **Sensors enable self-correction.** A sensor gives the agent feedback so it fixes issues before they reach human eyes; guides + sensors together are the harness.
- **Computational vs inferential sensors** is the organizing split. Computational/deterministic: type checker, ESLint, Semgrep (SAST), dependency-cruiser, coverage, mutation testing, GitLeaks. Inferential/LLM: security review, data-handling review, dependency-freshness, modularity & coupling review.
- **Four run locations:** in-session (continuous), CI pipeline (clean-infra confirmation), scheduled (drift), production (runtime).
- **Top ESLint targets for AI failure modes:** max arguments, file length, function length, cyclomatic complexity — none in the default preset, so they must be configured. Plugins targeting agent failure modes are emerging (e.g. Factory's eslint-plugin).
- **Self-correction guidance via a custom ESLint formatter** ("a good kind of prompt injection"): override default messages; let the agent **suppress with a stated reason** or **slightly raise a threshold** (rule re-fires only if it worsens) rather than face binary suppress-or-comply. This finally makes a clean linting baseline feasible — suppressions stay visible and reviewable.
- **The agent's exceptions are a code-review starting point.** Evidence the messages matter: the agent kept raising the cyclomatic-complexity threshold *because that rule alone lacked self-correction guidance*; adding guidance changed its behavior.
- **dependency-cruiser layered rules work as live sensors.** Enforcing e.g. "`clients` never imports `services`": AI absorbed the steep config cost, violated rules a few times, then self-corrected. But they only express what imports/file-names/folders can capture.
- **Raw coupling metrics are largely NOT useful to AI alone.** Given only CLI coupling data, the LLM produced "lackluster" findings — flagging a deliberate DI factory and a legitimate shared zod schema as "god modules." *Good* vs *bad* coupling is really *appropriate* vs not, which needs context the import graph lacks. More useful for human risk-triage (impact radius of changed files) or to help a review agent prioritize tokens.
- **Inferential AI modularity review (Vlad Khononov's "Modularity Skills") found real debt:** duplicate route code (3 near-identical endpoint files), inconsistent backend calls (a third page reimplemented a shared hook), request params repeated at every level (one change touched **40+ files**), and misplaced auth/mock-fallback logic inside the wiring factory. It also correctly recognized purposeful "hub" modules. Running it twice surfaced an extra issue.
- **Coverage misleads; mutation testing catches missing assertions.** `mappers.ts`: 100% statement / 75% branch coverage but no unit tests and **13 surviving Stryker mutants** — "coverage tells us a line was executed, but not that its impact was verified." Mutation testing is resource-intensive (run incrementally/manually); a custom query script keeps Stryker's huge JSON out of the agent's context.
- **The test suite is a regression sensor:** a failing pre-existing test forces "did I break it, or am I intentionally changing behavior?" The article scopes to test *effectiveness*, explicitly not test *correctness*.
- **Without human review AND inferential AI reviews, the agent compounds inadvertent [[concepts/infrastructure-dev/agentic-technical-debt|technical debt]].**

## Useful Examples

- **The custom ESLint self-correction message for `no-explicit-any`** — tells the agent to make a judgment call and, if it declines a type, suppress with `// eslint-disable-next-line @typescript-eslint/no-explicit-any -- (reason)`. A directly copyable pattern.
- **The "suppress-with-reason OR slightly raise threshold" policy** — a reusable design for keeping a clean static-analysis baseline with an AI collaborator instead of binary suppress/comply.
- **dependency-cruiser layered rule** (`clients-no-services`) with an expanded self-correction error message that recaps the whole layering concept — a model for turning a lint error into agent guidance.
- **The mutation-testing `mappers.ts` story** (100% statement coverage, 0 unit tests, 13 survivors) — the canonical illustration that coverage ≠ effectiveness.
- **The `query_stryker.py` helper** (summary / files / hotspots / tests subcommands, `--changed` for git-diff scope) — pattern for keeping a large tool report queryable without clogging the agent's context ("AI helped me help AI").
- **The "40+ files for one date-range change" finding** — a concrete symptom that "request parameters repeated at every level" is real debt, and what triggers the inferential review's recommendation to wrap params in an object.
- **The coupling-analyser CLI + report prompt** — example of grounding an LLM report in deterministic tool output (still produced lackluster findings, which is itself the lesson).

## Constraints / Caveats

- **Single-app, single-author experiment.** Findings come from one TypeScript/Next.js/React app rebuilt by one engineer; they are well-reasoned practitioner observations, not controlled study results.
- **Scoped to maintainability / internal quality** (and within testing, to *effectiveness*, not correctness). Functional correctness and architectural fitness are explicitly out of scope.
- **Stack-specific tooling.** ESLint, dependency-cruiser, Stryker, Semgrep, and a custom coupling analyser are TypeScript-ecosystem choices; the *principles* transfer but the specific tools may not.
- **Models/harnesses dated.** Experiments used Cursor / Claude Code / OpenCode with Claude Sonnet, Claude Opus 4.7, and Cursor composer-2 — conclusions (especially "coupling data not useful to AI") may shift with stronger models.
- **Several conclusions are tentative** by the author's own framing — "remains to be seen," "I haven't got useful observations yet," open questions on guides-vs-sensors balance.

## Design Implications

- **Build self-correction INTO sensor messages.** A lint/dependency error should carry context the agent can act on — treat sensor output as prompt-injectable guidance, not just a red mark.
- **Allow reasoned suppression / threshold nudges** to keep a clean baseline maintainable with an AI collaborator, and **review the agent's exceptions first** during code review — they are a high-signal triage list.
- **Use computational sensors for file/function hygiene** (max args, file/function length, cyclomatic complexity, dependency-direction rules) and **reserve inferential (LLM) sensors for cross-file modularity/coupling** where semantic judgment and trade-offs are needed.
- **Do not trust coverage as a quality signal.** Add mutation testing (incrementally) to catch missing assertions, especially when leaning on AI-generated end-to-end/acceptance tests that inflate coverage without strong assertions.
- **Run inferential reviews more than once** when it matters — repeated LLM analyses surface additional issues.
- **For [[concepts/infrastructure-dev/agentic-technical-debt|agentic technical debt]]:** without both human review and inferential AI reviews, agents silently compound debt; sensors plus periodic AI modularity reviews are a practical "garbage collection" loop. Relates to [[concepts/infrastructure-dev/knowledge-linting|knowledge linting]] as the codebase analog.

## Tensions

- **False sense of security vs real assurance.** More green sensors can create an "illusion of quality"; static analysis has real limits and was historically distrusted as a simplified quality proxy.
- **Feedback signal vs feedback overload.** Each new rule set surfaced a mix of real and irrelevant issues; too much can send the agent into "over-engineered refactoring spirals." (Mirrors the "remove the LLM-review-of-SQL loop" lesson in [[sources/bayer-prince-reliable-agentic-ai|the Bayer PRINCE case study]].)
- **Conflicts between sensors.** `max-lines` / `max-lines-per-function` pushed complexity *out of* functions and *into* long component property chains — fixing one metric worsened another. More such trade-offs likely lurk.
- **Computational vs inferential.** Deterministic sensors are cheap, fast, and unambiguous but shallow; inferential sensors are deeper and context-aware but slower, non-deterministic, and can misjudge legitimate patterns (the "god module" false alarms).
- **Guides vs sensors (open balance).** Once a set of sensors is trusted, which guides can be deleted? Do sensors make weaker models viable? How are guides and sensors kept consistent? Unresolved.
- **Human review realism.** Reviewing all AI-generated unit tests is unrealistic/unsustainable, yet skipping review risks tests that pass but verify the wrong thing — mutation testing addresses effectiveness but not correctness.

## Open Questions

- Do better models change the verdict that raw coupling data is "not useful to AI"?
- How should conflicting sensors (e.g. file-length vs prop-chain complexity) be arbitrated — can an agent make consistent trade-offs?
- What is the right guides-vs-sensors balance, and which guides become deletable once sensors are trusted?
- Can the inferential modularity review be applied to just the changed files in a commit, to shift it earlier (into CI) rather than as a scheduled job?
- How do you prevent feedback overload from driving over-engineering?
- Separate hard problem (out of scope here): how to detect when AI-generated tests assert the *wrong* behavior (test correctness, not just effectiveness)?

## Concepts Linked

- [[concepts/ai-agents/harness-engineering|Harness Engineering]] — the guides + sensors model this article operationalizes on the code side.
- [[concepts/infrastructure-dev/agentic-technical-debt|Agentic Technical Debt]] — what unsupervised agents compound without sensors and inferential review; the article is a concrete demonstration.
- [[concepts/ai-agents/ai-coding-tools|AI Coding Tools]] — Cursor / Claude Code / OpenCode as the base harnesses under test.
- [[concepts/infrastructure-dev/knowledge-linting|Knowledge Linting]] — sibling idea: automated linting/health-checking as a feedback loop (here applied to a codebase rather than a knowledge base).
- [[concepts/infrastructure-dev/token-efficiency|Token Efficiency]] — the `query_stryker.py` pattern (and grounding LLM reports in deterministic tool output) to avoid clogging the agent's context window.
- [[concepts/ux-research/human-in-the-loop|Human-in-the-Loop]] — sensors improve review trust but "are not a magical solution to take the human totally out of the loop."
- [[concepts/ai-agents/model-harness|Model Harness]] — sensors are part of the scaffolding around the model that increases reliable output.
- [[concepts/ai-agents/context-rot|Context Rot]] — motivation for keeping large tool reports out of the agent's context.
- (new) concepts/infrastructure-dev/computational-vs-inferential-sensors — the article's core taxonomy: deterministic (static analysis, tests) vs LLM-based (semantic reviews) feedback, and which maintainability concerns each is suited to.
- [[concepts/infrastructure-dev/mutation-testing|Mutation Testing]] (new) — introducing small code mutations to find missing assertions where coverage misleads (catches "tests that run code but verify nothing").
- (new) concepts/infrastructure-dev/self-correction-guidance — embedding actionable, prompt-injectable guidance into sensor/lint error messages so an agent can fix or reasonably suppress.
- [[concepts/infrastructure-dev/maintainability-sensor|Maintainability Sensor]] (new) — a feedback signal (computational or inferential) that monitors internal quality / maintainability of an AI-generated codebase.

## LLM Use

- **Use for:** designing a coding-agent sensor stack (what to run in-session vs CI vs scheduled vs production); writing self-correcting lint/dependency rules; deciding when to use deterministic static analysis vs an inferential LLM modularity review; arguing for mutation testing over coverage; framing how agents compound technical debt without feedback loops.
- **Do not use for:** claiming raw coupling metrics are universally useless to AI (model-dependent, single-experiment); treating the specific TypeScript tools as the only option; quoting it on test *correctness* (explicitly out of scope) or on functional/architectural fitness.
- **Best prompt pattern:** "Using Böckeler's computational-vs-inferential sensor taxonomy, design a maintainability harness for my [stack] coding agent. For each concern (file/function hygiene, dependency direction, cross-file modularity, regression safety), pick computational or inferential sensors, say where each runs (in-session/CI/scheduled/production), and write self-correction guidance for the top rules."

## Reliability Notes

> [!warning] Caveats
> - **Single practitioner, single app, single ecosystem** (one engineer, one TypeScript/Next.js/React project). High-credibility Thoughtworks engineering observations, but not a controlled study — confidence **0.9** on the qualitative patterns and techniques, lower on any claim read as a general law (e.g. "coupling data is not useful to AI" is model- and context-dependent).
> - **Scoped to maintainability and test effectiveness** — not correctness, functional behavior, or architectural fitness.
> - **Tooling and models are point-in-time** (Cursor/Claude Code/OpenCode; Claude Sonnet/Opus 4.7; composer-2). Re-verify the "coupling data" verdict against newer models.
> - **Some conclusions are explicitly tentative** (guides-vs-sensors balance, sensor conflicts) — treat as open hypotheses.

## Backfill Status

- Newly written 2026-06-22 from a full web capture (article read end-to-end). All sections populated. No prior thin version to upgrade. `coverage: substantial` (deep read of a single-app practitioner experiment; broader generalization across stacks/models remains untested).
