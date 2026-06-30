---
type: source
status: active
created: 2026-06-26
updated: 2026-06-26
tags: [ai-agents, claude-code, agent-skills, context-engineering, harness-engineering, model-escalation, human-in-the-loop, ios-development, token-efficiency, spec-driven]
source_path: raw/web/heyratel-ios-ai-agent-environment-2026-06-26.md
source_url: https://medium.com/heyratel/%EB%8F%84%EA%B5%AC%EA%B0%80-%EC%95%84%EB%8B%88%EB%9D%BC-%EA%B8%B0%EC%A4%80%EC%9C%BC%EB%A1%9C-ios-%ED%8C%80%EC%9D%98-ai-%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8-%ED%99%98%EA%B2%BD-%EA%B5%AC%EC%B6%95%EA%B8%B0-d37625b00af2
authors: [Jinyoo (유진영)]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.8
---

# Jinyoo / HeyRatel (2026): Not a Tool but a Standard — An iOS Team's AI Agent Environment

**Author:** Jinyoo (유진영) — Ratel And Partners (라텔앤드파트너즈), HeyRatel on Medium, 2026-06.
**Raw capture:** [[raw/web/heyratel-ios-ai-agent-environment-2026-06-26|heyratel-ios-ai-agent-environment-2026-06-26]]
**URL:** [medium.com/heyratel/...ios-ai-agent-environment](https://medium.com/heyratel/%EB%8F%84%EA%B5%AC%EA%B0%80-%EC%95%84%EB%8B%88%EB%9D%BC-%EA%B8%B0%EC%A4%80%EC%9C%BC%EB%A1%9C-ios-%ED%8C%80%EC%9D%98-ai-%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8-%ED%99%98%EA%B2%BD-%EA%B5%AC%EC%B6%95%EA%B8%B0-d37625b00af2)

## Citation

Jinyoo (유진영). (2026, June). *Not a tool but a standard: How an iOS team built its AI agent environment* (도구가 아니라 기준으로: iOS 팀의 AI 에이전트 환경 구축기). HeyRatel, Medium. Captured 2026-06-26 into raw/web/heyratel-ios-ai-agent-environment-2026-06-26.md.

## Summary

A Korean iOS team's field report on building an AI-agent development environment around explicit decision *criteria* rather than tool availability. From four architecture principles — keep context small and clean, validate inefficiency before automating, build single-responsibility composable skills, and preserve inviolable human-judgment gates — the team assembled a Claude Code-centric stack: a main dialogue/architecture agent, a Sonnet-class `ios-developer` implementer, a `markdown-writer`, and a Codex second-opinion reviewer, all driven by distributed per-module CLAUDE.md files. Their guiding line is "the standard chooses the tools, not the other way round." Distinctive engineering choices include rejecting MCP for custom curl-based skills (to compress tokens), symlinking AGENTS.md to CLAUDE.md so Claude Code and Codex share one source of truth, and an "advisor" escalation protocol that lets the Sonnet implementer call Opus 4.8 only for high-stakes decisions. The whole flow composes into `mission-plan` and `mission-run` orchestrators, with humans gating every irreversible action (commits, merges, posted review comments).

## Key Claims

- **Standard over tool.** Automation scope ("what to automate, where to stop") is derived from criteria, not from which tools are trendy: "Tools don't set the standard; the standard chooses the tools."
- **Context Optimization is principle #1.** Keep model context small and clean because token cost scales roughly linearly with context size; this directly motivates distributed CLAUDE.md and token-compressing custom skills.
- **Single-responsibility skills.** "Each skill carries one responsibility" — narrow skills (`task`, `grill-me`, `epic`, `pr`, `pr-review`, `codex-opinion`) are easier to test and compose than monolithic agents; `mission-plan`/`mission-run` are the only orchestrators.
- **Human-judgment gates are inviolable.** Automation targets *mechanical* waste, never *judgment*; commits, PR merges, code reviews, and approvals are never auto-executed. `pr-review` explicitly never posts comments without user approval.
- **Custom skills over MCP.** The team deliberately did **not** adopt MCP wholesale; verbose MCP responses waste tokens, so they wrote custom curl-based Jira/Confluence/Figma skills that fetch only needed fields and summarize before feeding the model.
- **Symlinked instruction file.** `AGENTS.md` is a symbolic link to `CLAUDE.md`, so Claude Code and Codex read the identical instruction source and never drift apart.
- **Tiered model escalation ("advisor" mode).** The `ios-developer` runs on Sonnet but can call **Opus 4.8** for high-stakes decisions and escalates architecture-altering ambiguity to the main agent or human — holding quality high on a lighter model without paying Opus rates on every call.
- **Documentation as contract.** Spec/plan/task docs in a `Doc/` folder act as guardrails and record "why did we do this?" rationale to prevent design drift.

## Useful Examples

- **Distributed CLAUDE.md layout:** a shared root CLAUDE.md plus per-module files (`Projects/DesignSystem/CLAUDE.md`, `Projects/DataLayer/CLAUDE.md`, `Projects/Features/<module>/CLAUDE.md`), each ≤200 lines per Anthropic guidance — cited as cutting per-request context vs one ~1000-line file.
- **Symlink command:** `ln -s CLAUDE.md AGENTS.md` as the concrete drift-prevention mechanism across two different agent tools.
- **`grill-me` skill:** a structured-questioning skill that surfaces design ambiguity early and recommends options, forcing design lock-in *before* coding.
- **`epic` skill:** breaks a large feature into Phase-sized units that are testable, reversible, and individually shippable.
- **Process map (stage → automation → gate):** Assignment → `task` → none; Planning → `grill-me` + Codex → person decides; Implementation → `ios-developer` + Phase escalation → Codex + on-device test; Review → `pr-review` → user approval; PR → `pr` → human merges.
- **Two-pass flow:** `mission-plan` (collect Confluence+Figma, grill-me, epic creates multi-phase tickets/branches/plan doc) then `mission-run` per Phase (re-confirm, implement within Phase scope, capture decisions, device test + Codex review, auto PR title, rule-check, human approval).

## Constraints / Caveats

- **Single-source practitioner blog**, vendor-adjacent (the team uses and advocates Claude Code/Codex). Treat architecture choices as one team's working solution, not benchmarked best practice.
- **Metrics are directional, not measured.** Claims like "advisor mode reduced escalation frequency" and "custom skills save tokens vs MCP" are reported qualitatively; no numbers, baselines, or A/B data are given.
- **Implementation details not shown.** Actual CLAUDE.md/skill file contents are described, not published, so the "≤200 lines" and "one responsibility" claims can't be independently inspected from this source.
- **Anthropic-attributed guidance** ("≤200 lines", "token cost scales linearly with context") is paraphrased secondhand; verify against current primary guidance before treating as rule.
- Coverage is `substantial`, ingest level `standard` — strong on the design rationale, thin on quantitative outcomes.

## Design Implications

- **Lead with criteria, not tools.** Before adopting an agent or MCP server, write down what you are automating and why; let the standard select the tool — see [[concepts/ai-agents/criteria-driven-ai-adoption|Criteria-Driven AI Adoption]].
- **Engineer the harness, not just the prompt.** The team's leverage comes from distributed instruction files, narrow skills, and gates — the surrounding scaffold — exemplifying [[concepts/ai-agents/harness-engineering|Harness Engineering]] and [[concepts/ai-agents/agent-skills|Agent Skills]].
- **Treat context as a budget.** Keep per-request context small via per-module [[concepts/infrastructure-dev/claudemd-context|CLAUDE.md / AGENTS.md Context]] files and summarize tool output before it reaches the model — concrete [[concepts/ai-agents/context-engineering|Context Engineering]] and [[concepts/infrastructure-dev/token-efficiency|Token Efficiency]] practice, loaded only when relevant ([[concepts/ai-agents/progressive-disclosure|Progressive Disclosure]]).
- **Tier your models behind a gate.** Run cheap models by default and escalate to a frontier model only for high-stakes calls — a reusable [[concepts/ai-agents/model-escalation-gate|Model Escalation Gate]] pattern and a practical form of [[concepts/infrastructure-dev/agent-cost-control|Agent Cost Control]].
- **Keep humans on irreversible actions.** Bake [[concepts/ux-research/human-in-the-loop|Human-in-the-Loop]] gates into commits, merges, and posted comments; let automation own only mechanical, reversible steps.
- **Lock the spec before code.** `grill-me`/`epic`/`Doc/` enforce a lightweight [[concepts/ai-agents/spec-driven-development|Spec-Driven Development]] loop where ambiguity is resolved up front and decisions are recorded.
- **Compose specialists.** The agent roster + orchestrators are a working [[concepts/ai-agents/multi-agent-architecture|Multi-Agent Architecture]]; the symlinked instruction file enforces [[concepts/ai-agents/model-neutrality|Model Neutrality]] so Claude Code and Codex stay interchangeable on one source of truth.

## Tensions

- **Custom skills vs [[concepts/ai-agents/mcp-integration|MCP Integration]].** The team rejected MCP for token reasons, trading the ecosystem/standardization benefits of MCP for hand-maintained curl skills — the opposite of the prevailing "adopt MCP" advice; the right call depends on how much token pressure you actually face.
- **Lighter model + escalation vs simply using the strong model.** Advisor mode adds protocol complexity (when to escalate, to whom) to avoid Opus costs; for small teams the orchestration overhead may exceed the savings.
- **Up-front rigor vs velocity.** `grill-me`/`epic`/`Doc/` reduce rework but add ceremony before any code is written — valuable for ambiguous features, possibly heavy for trivial ones.
- **Single source of truth vs model-specific tuning.** Symlinking one instruction file guarantees parity but forecloses per-agent optimization where Claude Code and Codex might benefit from different guidance.

## Open Questions

- How much token/cost did custom skills and distributed CLAUDE.md actually save versus MCP and a monolithic instruction file?
- What are the concrete triggers in the escalation protocol — what makes a decision "architecture-altering" enough to call Opus or the human?
- Does the ≤200-line-per-file discipline hold as modules grow, or does it just push complexity into cross-file coordination?
- How portable is this stack beyond iOS/Swift teams using Jira+Confluence+Figma?
- At what team size does the orchestration overhead (advisor mode, two-pass mission flow) stop paying for itself?

## Concepts Linked

- [[concepts/ai-agents/criteria-driven-ai-adoption|Criteria-Driven AI Adoption]]
- [[concepts/ai-agents/model-escalation-gate|Model Escalation Gate]]
- [[concepts/ai-agents/harness-engineering|Harness Engineering]]
- [[concepts/ai-agents/agent-skills|Agent Skills]]
- [[concepts/infrastructure-dev/claudemd-context|CLAUDE.md / AGENTS.md Context]]
- [[concepts/ai-agents/progressive-disclosure|Progressive Disclosure]]
- [[concepts/ai-agents/context-engineering|Context Engineering]]
- [[concepts/ai-agents/multi-agent-architecture|Multi-Agent Architecture]]
- [[concepts/ai-agents/model-neutrality|Model Neutrality]]
- [[concepts/infrastructure-dev/token-efficiency|Token Efficiency]]
- [[concepts/ai-agents/mcp-integration|MCP Integration]]
- [[concepts/ai-agents/spec-driven-development|Spec-Driven Development]]
- [[concepts/ux-research/human-in-the-loop|Human-in-the-Loop]]
- [[concepts/infrastructure-dev/agent-cost-control|Agent Cost Control]]

## LLM Use

- **Use for:** designing an agentic coding environment (instruction-file layout, narrow composable skills, model tiering, human gates); arguing the "criteria before tools" stance; concrete patterns like symlinked CLAUDE.md/AGENTS.md, custom-skill-over-MCP token compression, and advisor-mode escalation.
- **Do not use for:** citing hard performance/cost numbers (none are given); claiming MCP is generally inferior (this is one team's token-driven trade-off); iOS/Swift specifics (the post is about agent process, not Swift).
- **Best prompt pattern:** "Using Jinyoo/HeyRatel's four principles (small context, validate-before-automate, single-responsibility skills, human-judgment gates), design an agent environment for <team/stack>: propose the CLAUDE.md layout, the skill set, the model-escalation gate, and exactly which actions stay human-gated."

## Reliability Notes

> [!warning] Caveats
> Confidence 0.8: the design rationale is coherent, internally consistent, and aligns with broadly accepted agent-engineering practice (small context, composable skills, human gates, model tiering), which is why it reads as reliable *as a design pattern*. But it is a single-source practitioner blog with vendor-adjacent framing and **no quantitative validation** — every efficiency/quality claim is directional. Use it for patterns and reasoning, not as evidence of measured outcomes.

## Backfill Status

- New 2026-06-26. All sections populated from a full-text fetch.
- Coverage/confidence would rise with: published file contents (CLAUDE.md/skills), measured token-and-escalation metrics, or a second independent team reporting the same patterns.
