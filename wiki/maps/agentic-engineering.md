---
type: map
status: active
created: 2026-06-22
updated: 2026-07-07
tags: [map, agentic-engineering, agents, harness, moc]
sources:
  - the-new-sdlc-with-vibe-coding-day-1
  - agent-tools-interoperability-day-2
  - agent-skills-day-3
  - vibe-coding-agent-security-evaluation-day-4
  - spec-driven-production-development-day-5
  - bayer-prince-reliable-agentic-ai
  - fowler-sensors-coding-agents
  - hai-cooperbench-agent-teamwork
  - langchain-multi-agent-architecture
  - langchain-agent-middleware
  - clova-merit-post-training
  - eopla-magazine-44341-0-person-company
confidence: 0.86
---

# Agentic Engineering (Map of Content)

> [!abstract] Entry point
> The single navigation hub for how this vault thinks about **building reliable AI agents**. Start here, pick a cluster, then drill into concepts and source records.

## Core Idea

The throughline across every source here: **a raw model is not an agent — it becomes one only when wrapped in a *harness*.** Reliability comes not from a bigger model or a cleverer prompt, but from two disciplines:

- **Context engineering** — what each step sees, what it doesn't, and how context flows between steps.
- **Harness engineering** — the scaffolding *around* the model: orchestration, loops, middleware, retries/fallbacks, verification, observability, security, identity, and cost control.

Recurring meta-theme of the vault: **"looks done / fast / satisfying ≠ reliable."** Agentic engineering is the set of practices that turn a non-deterministic model into a manageable system.

## The Spine: Agentic Engineering Series (Day 1–5)

- [[sources/the-new-sdlc-with-vibe-coding-day-1|Day 1 — The New SDLC With Vibe Coding]] (context/factory/harness, conductor vs orchestrator)
- [[sources/agent-tools-interoperability-day-2|Day 2 — Agent Tools & Interoperability]] (MCP / A2A / A2UI / AP2 / UCP)
- [[sources/agent-skills-day-3|Day 3 — Agent Skills]] (procedural memory, progressive disclosure, eval toolkit)
- [[sources/vibe-coding-agent-security-evaluation-day-4|Day 4 — Security & Evaluation]] (7-pillar security; Security vs Evaluation axes)
- [[sources/spec-driven-production-development-day-5|Day 5 — Spec-Driven Production-Grade Development]] ("vibe coding ≠ vibe in production")

**Foundational case study:** [[sources/bayer-prince-reliable-agentic-ai|Bayer PRINCE]] (agentic RAG + harness engineering, on LangGraph) · **code-quality side:** [[sources/fowler-sensors-coding-agents|Böckeler: Maintainability Sensors]].

## Concept Clusters

### Harness, loops & middleware
- [[concepts/ai-agents/harness-engineering|Harness Engineering]] · [[concepts/ai-agents/model-harness|Model Harness]]
- [[concepts/ai-agents/loop-engineering|Loop Engineering]] · [[concepts/ai-agents/agent-middleware|Agent Middleware]] · [[concepts/ai-agents/loop-optimization|Loop Optimization]]
- [[concepts/ai-agents/context-engineering|Context Engineering]] · [[concepts/ai-agents/context-rot|Context Rot]]

### Multi-agent & orchestration
- [[concepts/ai-agents/multi-agent-architecture|Multi-Agent Architecture]] (subagents / skills / handoffs / router)
- [[concepts/ai-agents/deep-agents|Deep Agents]] · [[concepts/ai-agents/async-subagents|Async / Background Subagents]]
- [[concepts/ai-agents/orchestrator-of-agents|Orchestrator of Agents]] · [[concepts/ai-agents/agentic-rag|Agentic RAG]]
- ⚠️ counter-evidence: [[concepts/ai-agents/multi-agent-coordination|Multi-Agent Coordination]] (the coordination gap)

### Capabilities & skills
- [[concepts/ai-agents/agent-skills|Agent Skills]] · [[concepts/ai-agents/progressive-disclosure|Progressive Disclosure]]
- [[concepts/ai-agents/agent-interpreter|Agent Interpreter & Interpreter Skills]] · [[concepts/ai-agents/agentic-search|Agentic Search]]
- [[concepts/ai-agents/mcp-integration|MCP Integration]]

### Evaluation & reliability
- [[concepts/ai-agents/agent-verifiers|Agent Verifiers]] (LLM-as-judge) · [[concepts/ai-agents/agent-trajectory-evaluation|Agent Trajectory Evaluation]]
- [[concepts/ai-agents/vibe-coding-agent-evaluation|Vibe-Coding Agent Evaluation]] · [[concepts/ai-agents/product-evals|Product Evals]] · [[concepts/ux-research/ai-evals|AI Evals]]
- [[concepts/infrastructure-dev/maintainability-sensor|Maintainability Sensor]] · [[concepts/infrastructure-dev/mutation-testing|Mutation Testing]]

### Security, identity & governance
- [[concepts/ai-agents/agent-security-architecture|Agent Security Architecture]] (7 pillars) · [[concepts/ai-agents/agent-authorization|Agent Authorization]]
- [[concepts/ai-agents/red-blue-green-agent-teaming|Red/Blue/Green Agent Teaming]] · [[concepts/ai-agents/slopsquatting|Slopsquatting]]
- [[concepts/ai-agents/zero-trust-agent-development|Zero-Trust Agent Development]] · [[concepts/infrastructure-dev/eu-ai-act-compliance|EU AI Act Compliance]] · [[concepts/infrastructure-dev/cloud-ai-governance|Cloud AI Governance]]

### Economics & portability
- [[concepts/infrastructure-dev/agent-cost-control|Agent Cost Control]] · [[concepts/ai-agents/model-neutrality|Model Neutrality]]
- [[concepts/infrastructure-dev/token-efficiency|Token Efficiency]] · [[concepts/product-management/tokenomics|Tokenomics]]

### Training and model composition
- [[concepts/ai-agents/conflict-aware-instruction-tuning|Conflict-Aware Instruction Tuning]] — dataset-gradient conflict map → balanced independent tuning → one-shot merge
- [[sources/clova-merit-post-training|CLOVA MERIT]] — first-party ICML 2026 explainer with arXiv-verified method and headline result

### Spec, process & content
- [[concepts/ai-agents/spec-driven-development|Spec-Driven Development]] · [[concepts/product-management/ai-prd|AI PRD]]
- [[concepts/infrastructure-dev/agentic-content|Agentic Content]] · [[concepts/infrastructure-dev/claudemd-context|CLAUDE.md / AGENTS.md Context]] · [[concepts/infrastructure-dev/design-md|DESIGN.md]]

### Platforms, adoption & roles
- [[concepts/infrastructure-dev/enterprise-ai-agent-platform|Enterprise AI Agent Platform]] · [[concepts/infrastructure-dev/self-serve-agent-platform|Self-Serve Agent Platform]] · [[concepts/ai-agents/managed-ai-agents|Managed AI Agents]]
- [[concepts/product-management/ai-native-stack|AI-Native Stack]] · [[concepts/product-management/role-convergence|Role Convergence]]
- [[concepts/ai-agents/zero-person-company|Zero-Person Company]] · [[concepts/ai-agents/autonomous-company-runtime|Autonomous Company Runtime]]

## LangChain Source Library (15)

*Architecture & build:* [[sources/langchain-multi-agent-architecture|Multi-Agent Architecture]] · [[sources/langchain-loop-engineering|Loop Engineering]] · [[sources/langchain-custom-agent-harness|Custom Agent Harness]] · [[sources/langchain-agent-middleware|Agent Middleware (1.0 origin)]] · [[sources/langchain-background-subagents|Background Subagents]] · [[sources/langchain-interpreter-skills|Interpreter Skills]] · [[sources/langchain-box-ai-deep-agents|Box: Deep Agents]]
*Reliability, security & governance:* [[sources/langchain-verifiers-legal-agents|Verifiers for Legal Agents]] · [[sources/langchain-agent-authorization|Agent Authorization]] · [[sources/langchain-eu-ai-act|LangSmith & the EU AI Act]] · [[sources/langchain-evaluating-deep-agents|Evaluating Deep Agents]]
*Economics, portability & integration:* [[sources/langchain-predictable-coding-agent-spend|Predictable Agent Spend]] · [[sources/langchain-model-neutrality|Model Neutrality]] · [[sources/langchain-exa|Exa: Agentic Search]]
*Platform case study:* [[sources/langchain-lyft-support-agent-platform|Lyft: Self-Serve Support Platform]]

## Through-threads & Tensions

- **Multi-agent optimism vs the coordination gap.** LangChain's [[sources/langchain-multi-agent-architecture|four patterns]] (and Anthropic's 90.2% result) vs [[sources/hai-cooperbench-agent-teamwork|CooperBench]]'s "two agents do worse." Resolution: gains come from **centralized, context-isolated orchestration** (supervisor / router), not peer negotiation.
- **Velocity vs control.** Every harness/security/cost concept is a way to reconcile vibe-coding speed with production reliability (Day 4 security harness; Day 5 zero-trust; [[concepts/infrastructure-dev/agent-cost-control|cost control]]).
- **"Looks done ≠ reliable."** [[concepts/ai-agents/agent-verifiers|Verifiers]] / [[concepts/ai-agents/agent-trajectory-evaluation|trajectory evals]] / [[concepts/product-management/ai-prd|Eval Plans]] exist because passing tests, compiling, or satisfying a user can all mask a bad outcome.
- **Loops/reflection must earn their place.** Bayer PRINCE *removed* a net-negative reflection loop; Böckeler warns of feedback-overload — see [[concepts/ai-agents/loop-engineering|Loop Engineering]].
- **Identity is a poor static perimeter.** [[concepts/ai-agents/agent-authorization|Agent authorization]] + [[concepts/ai-agents/agent-security-architecture|zero ambient authority]] + JIT scoping.

## How To Use With An LLM

1. Start from this map → pick the cluster matching your problem (build / multi-agent / eval / security / cost / spec / platform).
2. Open the concept page for the framing, then its linked **source records** (prefer `llm_ready: true`) for evidence.
3. For any multi-agent design, stress-test it against the **coordination gap** before trusting it.
4. For anything shipping to production, require an **Eval Plan + failure definition + cost + security** pass (Day 4 / Day 5 / AI PRD).
