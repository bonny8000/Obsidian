---
type: query
status: active
created: 2026-06-01
updated: 2026-06-01
tags: [portfolio, ai-agent, ux-strategy, project-idea]
sources:
  - projects/ai-to-figma-evaluation
  - maps/ai-design-agent-workflows
  - maps/ai-native-product-management
  - concepts/ai-agents/agent-memory
  - concepts/ai-agents/product-evals
confidence: 0.78
---

# Impressive Large Project Strategy

## Question

Bonny asks: "我要做甚麼樣的大專案才可以像這樣看起來很厲害？"

Reference impression: a mature AI coding/workspace repo with structured docs, agent context, evaluation tasks, examples, scripts, source code, and private workspace notes.

## Short Answer

The strongest project direction is not a large standalone app. It should be a **system-level AI workflow project** with:

- a real product/design problem,
- durable docs and operating rules,
- working automation,
- evaluation criteria,
- examples and test cases,
- an Obsidian-backed research memory,
- a public-facing demo or case study.

Best fit after Bonny's clarification: **Product Workflow Studio: A Universal AI Agent Evaluation Workspace**.

This project should not be limited to Bonny's wiki, UX design, Figma, or a specific product category. It should be a domain-agnostic workspace where any product team can define a workflow, provide source material, generate artifacts, and evaluate whether the AI output meets the team's quality rules.

The UX/design version can be the first example module, but the platform should support other domains such as onboarding, dashboards, internal tools, commerce flows, support operations, research synthesis, documentation, and product planning.

## Why This Looks Impressive

It looks senior because it demonstrates orchestration, not just execution:

- **Product thinking:** defines a real workflow problem for designers, PMs, and frontend teams.
- **System design:** separates source material, prompts, agent context, evaluation rules, examples, and generated outputs.
- **Research grounding:** connects to UX research, AI-native product management, design automation, and eval methodology.
- **Technical credibility:** includes scripts, tests, visual regression, Figma integration, and prototype generation.
- **Operational maturity:** has `docs/`, `evals/`, `examples/`, `scripts/`, `src/`, `test-results/`, `AGENTS.md`, and project logs.

## Recommended Project Shape

Working title:

**Product Workflow Studio: A Universal AI Agent Evaluation Workspace**

Core user:

- Any product builder, PM, designer, researcher, founder, or operations owner who wants to verify whether AI-generated work actually follows the intended goals, constraints, quality rules, and business context.

Core workflow:

1. Input a PRD, brief, source notes, screenshots, files, research findings, workflows, or product constraints.
2. Generate structured intermediate specs:
   - flow map,
   - screen inventory,
   - component rationale,
   - UX rules,
   - edge states,
   - design-system constraints.
3. Generate a useful artifact, such as an interactive prototype, review report, workflow spec, research synthesis, dashboard plan, content system, or implementation brief.
4. Run evaluation:
   - missing requirements,
   - logic gaps,
   - unclear assumptions,
   - contradiction with source material,
   - UX or content quality risks,
   - visual or layout issues when applicable,
   - accessibility or localization risks when applicable,
   - AI decision explanation quality.
5. Output a review report and improvement plan.

## Repo / Workspace Structure

```text
ax-studio/
  AGENTS.md
  README.md
  docs/
    agent-context.md
    architecture/
    guides/
    reference/
    strategy/
  examples/
    rog-reward-flow/
    dashboard-redesign/
    ai-agent-onboarding/
  evals/
    visual-regression/
    ux-rule-checks/
    prompt-quality/
    decision-explainability/
  prompts/
    prd-to-flow.md
    flow-to-prototype.md
    prototype-review.md
  scripts/
    run-eval.ts
    capture-screenshot.ts
    compare-layout.ts
  src/
    prototype-runner/
    figma-adapter/
    report-generator/
  test-results/
  wiki-sync/
```

Optional private companion workspace:

```text
ax-studio-notes/
  agent-memory/
  current-state/
  workflows/
  history/
  task-plans/
  conversations/
  tool-understanding/
```

## Portfolio Narrative

The public story should not be "I built an AI tool." It should be:

> I built a research-backed evaluation workspace for AI-generated UX. It turns PRDs and design references into prototypes, then checks whether the AI respected product logic, UX rules, visual constraints, and explainability requirements.

This is stronger than a normal portfolio project because it shows:

- product strategy,
- UX methodology,
- AI workflow design,
- engineering literacy,
- evaluation rigor,
- documentation culture.

## Candidate Project Variants

### 1. Product Workflow Studio: Universal AI Agent Evaluation Platform

Best overall fit. Combines Bonny's AI-to-Figma work, PRD-to-code workflow, design review automation, and agent workflow research, but generalizes them into a platform that can evaluate any AI-assisted product workflow.

Outputs:

- working local tool,
- domain templates,
- example projects,
- eval reports,
- public case study,
- optional Obsidian knowledge map.

### 2. LLM Wiki OS

Turns this Obsidian vault into a polished AI knowledge operating system:

- raw source ingestion,
- source cards,
- concept graph,
- saved queries,
- project decision records,
- lint/audit reports,
- visual dashboard,
- agent memory protocol.

This is especially strong if positioned as "a personal AI research infrastructure for product strategy."

### 3. AI UX Research Evaluation Bench

A benchmark/workbench for testing how well LLMs analyze usability sessions, survey findings, or design problems.

Outputs:

- dataset examples,
- analysis rubric,
- inter-rater comparison,
- model output audits,
- research integrity guidelines.

### 4. Agentic Design System QA

A tool that checks whether generated UI follows a design system:

- typography,
- spacing,
- component usage,
- states,
- localization,
- accessibility,
- screenshot comparisons.

This is narrower but very credible for frontend/design-system audiences.

## Minimum Impressive Version

Do not start with everything. Build a polished 4-week version:

1. Pick one workflow: PRD + screenshot to prototype review.
2. Build 3 example cases.
3. Define 10 evaluation rules.
4. Generate before/after reports.
5. Publish docs and architecture.
6. Record a 2-minute demo.

The project looks impressive when the repo proves that the system can be repeated, evaluated, and explained.

## Evidence

- [[projects/ai-to-figma-evaluation|AI-to-Figma Evaluation Pipeline]] already contains the strongest seed: PRD parsing, Figma replication, visual regression, and AI decision explainability.
- [[decisions/dual-track-review-prd-to-code|Dual-track PRD-to-Code Review]] supports the idea that AI should generate intermediate UX artifacts before rendering interactive code.
- [[maps/ai-design-agent-workflows|AI Design Agent Workflows]] frames this as a workflow-level problem rather than a single-tool problem.
- [[maps/ai-native-product-management|AI-Native Product Management]] supports the narrative of shipping velocity plus evaluation and product taste.
- [[concepts/ai-agents/product-evals|Product Evals]] and [[concepts/ai-agents/agent-memory|Agent Memory]] support the need for repeatable evaluation and durable context.

## Reusable Notes Added

This query can become a project page for **Product Workflow Studio** or be split into:

- a project brief,
- a repo architecture spec,
- an evaluation rubric,
- a portfolio case-study outline.

## Follow-Up Sources Needed

- Strong examples of open-source AI agent repos with excellent docs/evals.
- Examples of design-to-code evaluation benchmarks.
- Examples of portfolio case studies that present internal tools as strategic systems.
