---
type: source
status: active
created: 2026-06-17
updated: 2026-06-17
tags: [agent-skills, progressive-disclosure, procedural-memory, context-rot, evaluation, meta-skills, agentic-engineering]
source_path: raw/Agent-Skills-Day-3.pdf
authors: [Tanvi Singhal, Gabriela Hernandez Larios, Debanshu Dus, Lavi Nigam, Smitha Kolan]
sources: []
ingest_level: deep
coverage: full
llm_ready: true
raw_preserved: true
confidence: 0.92
---

# Agent Skills (Day 3)

**Authors:** Tanvi Singhal, Gabriela Hernandez Larios, Debanshu Dus, Lavi Nigam, Smitha Kolan (curated/edited by Shubham Saboo; designed by Michael Lanning)
**Date:** May 2026
**Raw file:** [[raw/Agent-Skills-Day-3.pdf|Agent Skills (Day 3) — PDF]]
**Series:** Day 3 of a three-paper arc. Day 1 = [[sources/the-new-sdlc-with-vibe-coding-day-1|The New SDLC With Vibe Coding]]; Day 2 = [[sources/agent-tools-interoperability-day-2|Agent Tools & Interoperability]].

## Executive Summary

Agent Skills are a folder anchored by a `SKILL.md` file (optionally with `scripts/`, `references/`, `assets/`) that gives a general-purpose agent on-demand specialist competence without bloating its context. The paper frames Skills as the first credible **procedural memory** primitive for LLM agents, argues they collapse many multi-agent designs to "single-agent-with-skills," and treats them as the durable unit of improvement once foundation models commoditize. The architecture, evaluation discipline, meta-skill loop, composition primitives (DAG orchestration, Capability Profiles), and a retail case study together make the case that **the format is settled; the work is just beginning**.

Five frameworks worth carrying out of this paper:

- **Progressive Disclosure (3 levels):** metadata always loaded, body on trigger, bundled resources only when referenced. Anthropic example: 150K → 2K active tokens (~98% reduction).
- **Four Skill Failure Modes:** Trigger Failure, Execution Failure, Token Budget Failure, Regression (SkillsBench 2025 found 19% of skills *actively degrade* capability).
- **Evaluation Toolkit (5 patterns):** Eval-as-Unit-Test, Golden Dataset, LLM-as-Judge, Adversarial / Red-Team, Canary / Shadow Mode.
- **Read / Draft / Act Graduation Ladder:** progressive authority gates (read-only → human-reviewed draft → action-allowed with pass^k).
- **Composition Primitives:** DAG Orchestration with a File Message Bus, Capability Profiles as swappable persona+tool bundles, Canonical Skill Taxonomy (Generator, Reviewer & Gate, Pipeline, Inversion & Recovery, Domain Context Wrappers).

## Key Concepts

### What an Agent Skill is

A Skill is a folder with `SKILL.md` (YAML frontmatter + markdown body) plus optional `scripts/`, `references/`, `assets/`. The format is now an open standard at `agentskills.io`, adopted across major coding agents, AI chatbots, and agent frameworks.

- **Name:** snake_case directory, kebab-case skill name, prefer gerund form (`managing-databases`, not `database-manager`). Avoid generic (`utils`, `tools`) or vendor-locked (`claude-*`) names.
- **Description:** the *routing algorithm* — the only thing the model sees to decide whether to load the skill. State what it does + when to use + when NOT to use. 200 chars for API, 1024 chars in YAML, ~50 words for most authors.
- **Scripts:** deterministic work (parsing, math, formatting) lives here.
- **References:** knowledge that loads only when the body needs it (domain principles, edge-case handling).
- **Assets:** templates, schemas, output scaffolds.

Skills emerge through two paths:

- **Path A — Translating what you already know.** Subject-matter experts (compliance officer with a 30-page runbook, HR manager with onboarding guides) turn institutional knowledge into a SKILL.md. No coding required.
- **Path B — Crystallizing what the agent just did.** A successful trajectory becomes a skill. The agent drafts; the human reviews. This is the on-ramp to meta-skills (Section 6).

### Progressive Disclosure (the architectural answer to context rot)

Skills load in three levels:

1. **Metadata (name + description)** is *always* in the agent's context. ~50 tokens per skill.
2. **SKILL.md body** loads only when the skill triggers. ~2,000 tokens active.
3. **Bundled resources (`scripts/`, `references/`, `assets/`)** load strictly on demand. Scripts execute without polluting the token window.

> Token math: 50 skills as a single system prompt ≈ 15,000 tokens *every turn*. As a Skills library ≈ 4,000 tokens of descriptions + 2,000-token body of the one active skill = ~6,000 tokens, with 49 other bodies on disk. Anthropic published a workflow converted from ~150,000 active tokens to ~2,000 (98%+ reduction).

> Three practical implications: (1) **capacity is the wrong metric** (a 1M-token window can degrade noticeably at 50K); (2) **active context is a budget**, not a vessel — every token in front of the model takes attention from every other; (3) **Skills resolve the constraint** by keeping active context small while available capability stays effectively unbounded.

### Why Skills became popular so fast — four friction points

1. **Too many instructions, worse results** — context rot from giant system prompts.
2. **Knowing how, not just knowing what** — LLMs had episodic and semantic memory analogs but no procedural memory. Skills fill that gap.
3. **Multi-agent overload** — many systems built multi-agent by default can be elegantly simplified to single-agent-with-skills.
4. **Portability** — a folder with a markdown file is a remarkably lightweight, vendor-neutral primitive.

> "Agent Skills do not kill multi-agent architectures." Multi-agent remains right for genuine parallelism, real capability boundaries (different access / security postures / external systems), hierarchical decomposition with abstraction breaks, adversarial check-and-balance setups, sub-agent intercommunication, or heterogeneous models.

### Skills vs. MCP vs. AGENTS.md (these compose, they do not compete)

- **MCP** is about *reach* — an MCP server connects the agent to an external system (Drive, Salesforce, BigQuery, internal API).
- **A Skill** is about *know-how* — it teaches the agent how to think about a particular kind of work. When a Skill needs data, it tells the agent to call a tool, typically one provided by an MCP server.
- **AGENTS.md** is *always* loaded within the project; Skills load on demand. Cleanest setup: keep AGENTS.md tight (conventions, stack, build commands) and use it as a router into the Skills library with a short catalog at the bottom.
- **One-line mental model:** *System prompt = instinct. AGENTS.md = project README. Tools / MCP = hands. RAG = library. Skills = the runbook the experienced colleague hands you on day one, and that the AI never forgets.*

### Three install paradigms (the format is shared; the install path is not)

1. **The File Drop (Coding Agents & CLIs):** drop folder into a hidden directory; emerging convention around `.agents/skills/` at project root. Symlink managers like `skillport` or `openskills` route a central library to every tool's expected location.
2. **The UI Install (Web & Enterprise Workspaces):** upload through a visual registry; routing handled behind the scenes.
3. **The Programmatic Route (Custom Frameworks):** load skills via code — e.g. Google ADK's `SkillToolset` class, which auto-generates `load_skill` routing tools under the hood.

### Four Failure Modes of Skills (SkillsBench 2025)

A benchmark of 84 real-world agent tasks found **19% performed worse with a skill than without one** — these are not neutral noise; they actively degrade capability. The failures are predictable:

1. **Trigger Failure** — wrong skill fires, or the right one stays silent. Surfaces in routing logs.
2. **Execution Failure** — skill triggers correctly but produces wrong output or errant tool calls. Surfaces in output quality.
3. **Token Budget Failure** — a massive skill body crowds the context window, degrading unrelated turns. Surfaces under realistic context load.
4. **Regression** — a newly added skill overlaps with an existing one, breaking previously working routing. Surfaces only when the full library is exercised together.

### The Evaluation Toolkit — five complementary patterns

| Pattern | Description | Failure mode addressed | When required |
| --- | --- | --- | --- |
| Eval-as-Unit-Test | Test file for the skill in CI on every change (e.g. three JSON eval cases via `agenteval`; failing test blocks merges) | All | Every skill, every change |
| Golden Dataset | Curated, versioned (input, expected output) pairs stored with the skill (e.g. 30 representative queries) | Execution, Trigger | Draft tier and above |
| LLM-as-Judge | A peer model evaluates output against a rubric at scale; swap positions to neutralize ordering bias | Execution | Read-only and draft |
| Adversarial / Red-Team | Systematic probing — one rephrasing and one negative-boundary case per positive trigger (`agentregress` flags regressions) | Trigger, Execution | Before action-allowed graduation |
| Canary / Shadow Mode | Shadow = parallel offline comparison; Canary = 1% live traffic monitored via `selftune` for 24h | Regression | Before each action-allowed release |

> **The trigger is the first gate.** Vercel's production analysis found a **56% non-invocation rate** for skills expected to activate consistently. More critically, a skill stripped of its instructions scored 58%, while the agent without the skill scored 63% — a poorly-designed skill *subtracts* 5 percentage points of capability. In the same study, a passive AGENTS.md index achieved a 100% pass rate against a 53% baseline. **Skills are for narrow action-specific workflows; global context belongs in passive always-accessible documentation.**

Industry-standard target: **90% trigger accuracy**. The SKILL.md description must pass four checks: testable specificity (3 positive + 3 negative triggers), clarity, execution fidelity (real, not aspirational), rephrasing stability.

### Output quality and tool trajectory

Once a skill triggers, test the **final output** and the **tool trajectory** separately. Latitude (March 2026) found final-output-only scoring passes 20–40% more cases than trajectory-aware scoring — those are instances where the agent reached the correct answer via incorrect tool calls. Tolerable read-only; critical for action-allowed.

Google ADK eval framework offers three trajectory modes: `EXACT`, `IN_ORDER`, `ANY_ORDER`. Read-only skills can use `ANY_ORDER`; action-allowed require `IN_ORDER` or `EXACT`.

### Evaluation Driven Development (EDD)

Invert the workflow: write three JSON eval cases (input, expected tools, expected output) **before** drafting SKILL.md. Forces a functional spec upfront.

```json
{
    "case_id": "refund_dup_charge_001",
    "input": "I was charged twice for order #4521 last Tuesday",
    "expected_skill": "refund_processor",
    "expected_tool_calls": [
        {"tool": "lookup_order", "args": {"order_id": "4521"}},
        {"tool": "check_duplicate_charge", "args": {"order_id": "4521"}}
    ],
    "expected_output_format": "confirmation_with_refund_id",
    "rubric": ["acknowledges duplicate", "cites order id", "provides next step"]
}
```

### The Read / Draft / Act Graduation Ladder

Skills must graduate through tiers of authority:

- **Read-Only:** LLM-as-Judge eval; 90% trigger accuracy.
- **Draft-Only (Human Review):** Golden dataset of 20+ cases; human approval.
- **Action-Allowed:** Full adversarial red-teaming; sustained success across multiple runs (not just a single lucky pass); zero rollback events; sustained pass^k.

`pass^k` measures consistent success — running the eval `k` times and requiring success on *every* run. On tau-bench (Yao et al., 2024), GPT-4o scored 61% on pass^1 but dropped below 25% on pass^8. Single-run success is a poor predictor of production reliability.

Two calibration warnings: **Production Degradation** (ReliabilityBench shows production drops 20–30% vs offline pass@1); **Simulation Bias** (optimistic bias up to 9% — the "Lost in Simulation" finding).

### Token budget: isolation is a trap

Production agents co-load 5–15 skills simultaneously. A skill body exceeding 5,000 tokens might work perfectly alone, but it causes context rot when co-loaded. MCPVerse noted an 18.2% accuracy drop in Claude-4-Sonnet from tool proliferation and attention competition. Chroma Research (2025) found all frontier models degrade as input grows.

**Two-Tiered Assert Framework:** validate underlying tool code independently; audit `SKILL.md` triggers across multiple model families to catch brittle, architecture-locked descriptions.

### Eval coverage checklist (graduation gate)

A skill is "evaluated" only when ALL FOUR are satisfied — any failure holds it at the draft tier regardless of happy-path performance:

- **Trigger:** positive AND negative test cases; 90% trigger accuracy.
- **Execution:** correct outputs across a representative range of inputs.
- **Regression:** adding this skill causes zero drops in the existing library.
- **Token budget:** co-loaded with 5–15 frequently-active skills, does not degrade unrelated turns.

### Skills as the unit of improvement

A reverse-engineering of Claude Code v2.1.88 (Liu, Zhao, Shang, Shen, 2026; companion site `ccunpacked.dev`) found that **98.4% of the codebase is operational infrastructure** (permission classifiers, context compaction pipelines, subagent delegation, session storage) and only 1.6% is the agent loop itself. As foundation models converge on baseline reasoning, the differentiator becomes the deterministic engineering around the model — and inside that, the unit that gets composed and reused is the Skill.

| Improvement style | Cycle time | Failure mode | Who can do it | Context tax |
| --- | --- | --- | --- | --- |
| Model swap | Days to weeks | Regression in unrelated tasks | ML/platform team | None (weights-based) |
| System-prompt edit | Minutes to hours | Context rot, instruction conflict | Whoever owns the prompt file | Static (every turn pays) |
| Fine-tune | Weeks to months | Catastrophic forgetting, overfitting | ML team only | None (weights-based) |
| **New skill** | **Hours to days** | **Bounded to matching turns** | **Any domain team** | **Dynamic (on-demand when triggered)** |

### Context overflow — the failure mode that breaks demos

Most common production failure mode of agents is *not* hallucination — it is **context overflow**: the model receiving more context than it can effectively use and degrading silently. Two research strands ground this:

- **Lost in the Middle (Liu et al., TACL 2024):** U-curve of performance — best when relevant info is at the start or end of input; degrades in the middle. Holds even for models trained on long contexts.
- **Context Rot (Chroma Research, 2025):** Across 18 frontier models (Claude 4 Opus/Sonnet, Gemini 2.5, Qwen3), performance degrades as input grows even when task difficulty is held constant. Noise typical of real agent contexts (tool outputs, half-relevant retrievals, intermediate reasoning) is among the worst.

### Meta-Skills (four buckets)

Skills whose job is to author, evaluate, or improve other skills:

1. **Authoring** — take a workflow description, produce a draft SKILL.md (Google ADK's "skill factory" pattern via SkillToolset; Anthropic's `skill-creator`).
2. **Assisted authoring from traces** — watch the agent succeed a few times, turn the trace into a skill. Human's job shifts from writing to confirming.
3. **Improvement** — take an existing skill + failing eval cases and propose edits (Saboo's `SkillOptimizer`; Anthropic's description-optimization loop; Karpathy's `autoresearch` pattern — bounded experiment, keep change only if metric improves).
4. **Library evolution** — agent finishes a task it had no skill for, notices it just solved a recurring problem, proposes adding a skill (Voyager-style, Schmid's `self-learning-skill`).

**Habits that have held up:**

- Anything an agent writes enters at the **draft tier**, regardless of meta-skill confidence.
- Keep a human in the loop for the first few edits — agents overfit descriptions or break downstream skills they didn't know existed; a human catches that in 30 seconds.
- Don't start with meta-skills. Get manual authoring working first. The fastest way to a bad library is pointing an agent at an empty folder and asking it to generate fifty skills.

### Composition primitives

**DAG Orchestration** replaces brittle prompt chaining:

- **Decoupled State** — state doesn't rely on accumulating execution history in the prompt.
- **File Message Bus** — the DAG controller orchestrates handoffs by passing structured schema references between subagent nodes.
- **Protected Attention** — abstracting payload from the model's text input prevents context bloat and preserves capacity.

**Capability Profiles** — swappable, version-controlled bundles defining:

- Active skills and tool access.
- System instructions and operational guardrails.
- Automated workflows and subagent topologies.
- LLM parameters (model choice, temperature).

During execution, the orchestrator unloads previous system instructions and flushes stale variables before swapping the new profile in. Strict teardown and rebuild prevents context loss.

**Canonical Skill Taxonomy** — discrete engineering capabilities map to DAG node functions:

- **Generator** — convert user intent into structured artifacts.
- **Reviewer & Gate** — deterministic gates blocking execution if validation fails.
- **Pipeline** — orchestrate linear paths within the broader DAG.
- **Inversion & Recovery** — force the agent to clarify assumption before execution.
- **Domain Context Wrappers** — reference nodes teaching domain conventions.

### Context Debt and Shifting Intelligence Left

Skills burn model attention — a scarce resource. When authors attempt deterministic behavior at runtime by bloating skill descriptions (e.g. "ALWAYS DO X"), they accumulate **Context Debt**. Models learn to ignore capitalized imperatives exactly as developers ignore walls of warning text.

The fix: **Shift Intelligence Left** — distill subjective judgments into skills, push logic out of the LLM prompt into testable scripts. Replace negative LLM instructions with deterministic software constraints that make invalid actions impossible.

### Architectural Tradeoffs

| Architecture | Mechanism | Primary benefit | Best for |
| --- | --- | --- | --- |
| Linear Pipelines | Sequential text passing between fixed nodes | Low engineering overhead, rapid prototyping | Single-domain, low-complexity generative tasks |
| DAG Orchestration | Graph-based parallel execution with file-bus state via schema references | Cycle prevention and strict context isolation | Multi-agent workflows requiring high reliability |
| Capability Profiles | Swappable, version-controlled parameter and tool bundles | Rapid persona switching with lifecycle memory purging | Role-based deployment and domain-specific agents |

### Skill source trust defaults

By early 2026, public skill marketplaces had crossed 40,000 listings. Three categories of source, with different operational stances:

| Source | Trust default | Examples | Who maintains it |
| --- | --- | --- | --- |
| First-party vendor | Trust by default; pin a version | `google/agents-cli`, `google/skills`, `google-gemini/gemini-skills`, `anthropics/skills`, `stripe/ai`, `microsoft/skills` | Team that built the underlying product |
| Organization-curated | Trust within the org; review on adoption | `your-org/retail-skills`, `your-org/finance-skills` (private) | Your own domain teams, PR review |
| Community | Audit before adopting; pin aggressively | `VoltAgent/awesome-agent-skills`, SkillsMP marketplace, `addyosmani/agent-skills`, individual GitHub repos | Volunteer authors, varying maintenance |

> Three heuristics: (1) prefer first-party skills for vendor-specific tools, (2) pin everything you depend on, (3) audit before adopting — a skill is code that runs in your context.

### The Google Agents CLI worked example

Google's Agents CLI is a CLI + skills package for the full ADK agent lifecycle on Google Cloud. **One `uvx` command installs seven skills** into the developer's existing coding agent, covering scaffold, ADK code, eval, deploy, publish, and observability. The same seven skills work across Claude Code, Codex CLI, Antigravity, and any compliant agent.

Three properties generalize:

- **The expertise lives in the skills, not the runtime.** The runtime is commoditized; the seven skills are the durable asset.
- **The skills package composes with what you already use.** Capabilities plug into existing tooling, not another portal.
- **The full lifecycle ships as skills.** Every stage that once needed its own tooling now fits the skills format.

### Appendix B — Retail Case Study (Domain Expertise as Code)

Retail is the canonical case because brand expertise lives stuck in three places AI has struggled to reach: senior buyers/merchandisers/category managers' heads, 30-page operational runbooks no one reads, and Slack threads from 2023. Skills capture this in a form the company's customer surfaces actually use.

Three-layer architecture: thin customer surfaces (web chat, mobile app, in-store kiosk, voice agent) → agent runtime + orchestrator → data and tools plane (product catalog, live inventory, customer profile, KB, vector search).

The runtime is generic (ADK, Claude Agent SDK, etc.); the **Skills are what carry the brand's expertise to the customer**.

Illustrative skill library for a major home-improvement retailer:

- `project-guidance` — turns "how do I tile a shower?" into a step-by-step plan with structural dependencies and common-mistake callouts. Owner: trades knowledge team. Read-only.
- `materials-list` — produces a grouped bill-of-materials including likely-forgotten items. Owner: Pro merchandising. Draft-only.
- `review-summarize` — pros, cons, common use cases from long reviews. Owner: personalization. Read-only.
- `delivery-window` — computes last-mile options and ETAs. Owner: fulfillment. Read-only.
- `return-policy` — encodes return rules and dozens of exceptions. Owner: customer service. Read-only. Promotion to action-allowed (issuing a refund) requires a separate skill with tighter review.

**Why this is harder to compete with than a custom agent:** the runtime has commoditized. The Skills library encodes the company's accumulated patterns. A retailer that invests in custom agents but neglects its Skills library invests in the part competitors will reach for free.

> **Cold start:** take the most experienced practitioner aside for an hour. Ask them to narrate three workflows they do regularly. Record it. The transcript is almost literally the first draft of three skills.

## Useful Examples

- **The cafe-preparation Skill** — illustrative folder layout (SKILL.md + `scripts/calc_quantities.py`, `convert_to_ingredients.py` + `references/menu_and_recipes.md`, `minimums.md` + `assets/prep_sheet_template.md`, `shopping_list_template.md`). Shows the canonical structure and the gerund-form naming.
- **Logistics company with 100 process variants** — worked comparison of one-giant-prompt vs RAG vs 100-subagents vs one-agent-with-100-skills. The Skills option costs ~100 × 50 = ~5,000 tokens of always-loaded metadata; logistics carries strong activation cues (SKU, origin, weight, hazmat, SLA) so descriptions stay sharp; adding the 101st variant is a new folder, not a new deployment.
- **Anthropic's first two Skills** were for reading PDFs and creating slides — the friction that produced the format.
- **`refund_dup_charge_001` JSON eval case** — minimal EDD case with `input`, `expected_skill`, `expected_tool_calls`, `expected_output_format`, `rubric`.
- **Gemini SDK skill** (Google Developers Blog) — reports the developer skill improving Gemini 3.1 Pro from 28.2% to 96.6% on SDK code generation across 117 prompts.

## Constraints / Caveats

- Several arXiv references (SkillsBench `2602.12670`, ReliabilityBench `2601.06112`, "Lost in Simulation" `2601.17087`, MCPVerse `2508.16260`) appear to use 2026-vintage IDs and were not independently verified during this ingest.
- The "Vercel found 56% non-invocation rate" and "skill subtracts 5 points of capability" results come from one production study (`vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals`). Single-vendor evidence; pair with internal evaluation before generalizing.
- The "98.4% operational infrastructure / 1.6% agent loop" claim about Claude Code v2.1.88 comes from a single reverse-engineering exercise. Striking, plausible, but not independently corroborated within this paper.
- "Skills do not kill multi-agent architectures" is repeatedly stated but the boundary cases (genuine parallelism, capability boundaries, etc.) are listed without quantified guidance.
- Some endnote URLs (2 vs 22, 17 vs 27 in the body) are slightly cross-referenced; trust the citation names over the numerical IDs.
- The paper is a vendor-curated thought-leadership piece (Google-affiliated authorship + Saboo curation). Read its recommendations as well-reasoned community consensus, not peer-reviewed empirical work.

## Design Implications

- **For Bonny's LLM Wiki maintenance agent:** treat repeated procedures (ingest, lint, source-page backfill, query answering) as candidates for SKILL.md. The vault already separates raw / wiki / log; the missing layer is skill descriptions wired to the right operations.
- **For internal AOCC AI Hub-style assistants:** apply the four-failure-mode lens before shipping any new skill. Trigger accuracy ≥ 90% with 3 positive + 3 negative cases is the bar.
- **For UX-research-tooling agents:** keep AGENTS.md as the always-on project context and reserve Skills for narrow, action-specific workflows (sample-size calc, MaxDiff design, study-template generation). Vercel's "AGENTS.md outperforms Skills" result reinforces this split.
- **For multi-tool environments:** when a workflow requires data, write a Skill that *calls* an MCP server. Don't reinvent MCP as scripts inside a Skill.
- **For governance-sensitive features:** apply the Read / Draft / Act ladder explicitly. Any action that mutates external state should require pass^k and human review before graduation.
- **For demo-to-prod gap planning:** budget for the 20–30% production-vs-offline-pass@1 degradation up front. Offline numbers are not production numbers.

## Tensions

- **Vercel's finding that AGENTS.md beats Skills in some setups** vs the paper's general bullishness on Skills. Resolution per the paper: Skills are for narrow action-specific workflows; global context belongs in passive AGENTS.md. But this is a fault line worth tracking — it predicts where teams will mis-apply Skills.
- **"One agent with skills" simplification vs multi-agent for parallelism/security boundaries.** The paper says both, but the boundary is fuzzy. Treat it as "default to skills unless you can name a specific multi-agent-only reason."
- **Meta-skills enthusiasm vs the failure mode of agent-edited libraries.** Self-improving libraries quietly degrade without solid trigger/regression tests. The paper concedes this and recommends keeping humans in the loop for the first edits.
- **Trajectory-aware vs final-output-only scoring.** Final-output scoring inflates pass rates 20–40% but masks irreversible-side-effect risk in action-allowed skills. Tradeoff between evaluation cost and trustworthiness.
- **The paper situates Skills as "the unit of improvement"** while [[sources/the-new-sdlc-with-vibe-coding-day-1|Day 1]] positions context engineering as the wider craft. Reconcile: Skills are the *primitive*; context engineering is the practice that picks when to use one.

## Open Questions

- Which of Bonny's recurring AOCC AI Hub or LLM Wiki workflows have strong enough activation cues to make good Skills? (Candidates: source-page backfill, lint, gap-audit, MaxDiff study setup, sample-size routing.)
- How does `SkillOpt` (already in the vault via [[concepts/ai-agents/skillopt|SkillOpt]]) compare with Anthropic's `skill-creator` description-optimization loop on the same task?
- Does the "98.4% operational infrastructure" claim hold for Anthropic's own Claude Code v2.x line, or is it specific to the reverse-engineered fork?
- What is the right pass^k threshold for action-allowed skills in low-stakes vs regulated domains?
- Can the retail Skills library pattern transfer cleanly to internal enterprise tooling (HR, finance, IT) where the "brand expertise" is replaced by "internal policy expertise"?
- Where should Bonny put a personal Skills library so it works across Claude Code, Codex, Antigravity, and Cursor — central directory + symlinks, or duplicated per tool?

## Concepts Linked

- [[concepts/ai-agents/agent-skills|Agent Skills]] (new — the format itself)
- [[concepts/ai-agents/progressive-disclosure|Progressive Disclosure]] (new)
- [[concepts/ai-agents/context-rot|Context Rot]] (new)
- [[concepts/ai-agents/procedural-memory|Procedural Memory]] (new)
- [[concepts/ai-agents/skill-system|Skill System]] (existing — upgraded with Day-3 evidence)
- [[concepts/ai-agents/skillopt|SkillOpt]]
- [[concepts/ai-agents/self-improving-agent-workflows|Self-Improving Agent Workflows]]
- [[concepts/ai-agents/agent-memory|Agent Memory]]
- [[concepts/ai-agents/model-harness|Model Harness]]
- [[concepts/ai-agents/harness-engineering|Harness Engineering]]
- [[concepts/ai-agents/mcp-integration|MCP Integration]]
- [[concepts/infrastructure-dev/claudemd-context|CLAUDE.md / AGENTS.md Context]]
- [[concepts/ai-agents/vibe-coding|Vibe Coding]]
- [[concepts/infrastructure-dev/agentic-engineering|Agentic Engineering]]
- [[concepts/ai-agents/orchestrator-of-agents|Orchestrator of Agents]]
- [[concepts/ai-agents/product-evals|Product Evals]]
- [[comparisons/skills-vs-mcp-vs-agents-md|Comparison: Skills vs MCP vs AGENTS.md]]

## LLM Use

- **Use for:** designing Skills, drafting SKILL.md descriptions, planning evaluation suites (the four checks + five patterns), making the Skills-vs-MCP-vs-AGENTS.md routing decision, framing meta-skills risk, budgeting tokens for co-loaded Skills libraries, justifying a single-agent-with-skills design over multi-agent.
- **Do not use for:** detailed engineering of MCP servers (defer to [[sources/agent-tools-interoperability-day-2|Day 2]]), high-level SDLC framing (defer to [[sources/the-new-sdlc-with-vibe-coding-day-1|Day 1]]), or peer-reviewed empirical claims (this is a curated thought-leadership paper, not academic literature).
- **Best prompt pattern:** "Using Agent Skills (Day 3) as the procedural-memory frame, design a Skill for X with name, description (3 positive + 3 negative triggers), folder structure, and a JSON eval case in EDD form. Decide its tier on the Read/Draft/Act ladder and list the evaluation patterns required for graduation."

## Reliability Notes

> [!warning] Caveats
> - **Vendor lens:** Google-affiliated authorship plus Saboo (`awesome-llm-apps` author). High-quality synthesis, but emphasizes Google ADK / Anthropic / OpenAI ecosystems. Verify cross-vendor specifics independently.
> - **Forward-dated citations:** Many cited arXiv IDs are 2026-vintage (e.g. `2601.06112`, `2602.12670`, `2602.08004`). These were not independently checked during this ingest.
> - **Single-study generalizations:** Vercel's AGENTS.md vs Skills numbers and the Claude Code reverse-engineering result are striking but each rest on one source.
> - **Confidence:** 0.92 on synthesis structure (frameworks, ladders, taxonomy) and Bonny-facing design implications; 0.70 on specific percentage/pass@k numbers; 0.85 on the cross-vendor adoption / tool ecosystem claims.

## Backfill Status

- Newly written 2026-06-17 from a clean full-PDF read. All sections populated. No prior thin version to upgrade.
