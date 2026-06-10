---
type: project
status: active
created: 2026-06-01
updated: 2026-06-01
tags: [project, ai-agent, product-workflow, evaluation, workspace]
sources:
  - queries/2026-06-01-impressive-large-project-strategy
confidence: 0.82
---

# Project: Product Workflow Studio

## One-line Positioning

**Product Workflow Studio is a universal AI workspace that turns messy product context into structured work, then evaluates whether the output is complete, grounded, and usable.**

中文定位：

**一個把混亂產品脈絡轉成結構化 AI 輸出，並自動檢查品質、依據與可用性的工作流平台。**

## Product Thesis

Most AI tools stop at generation: "give me a PRD", "make a prototype", "summarize this research", "create a plan". The real problem is that product work is not finished when an artifact is generated. Teams still need to know:

- Did the AI understand the goal?
- Did it miss important requirements?
- Is the output grounded in the source material?
- Are assumptions and tradeoffs visible?
- Can another person continue the work?
- Is this good enough to use, review, or ship?

Product Workflow Studio solves this by combining **context capture**, **workflow planning**, **artifact generation**, and **quality evaluation** in one workspace.

## Target Users

Primary users:

- PMs turning fuzzy goals into structured requirements, workflow maps, and acceptance criteria.
- Designers turning briefs into flows, prototypes, UX checks, and design review notes.
- Researchers turning interviews, survey findings, or usability notes into evidence-grounded synthesis.
- Founders turning early ideas into MVP plans, experiment plans, landing pages, and investor/product narratives.
- Operations or CX teams turning repeated issues into SOPs, automation specs, and internal tooling requirements.

Secondary users:

- Engineers who need cleaner implementation briefs.
- Managers who need reviewable project plans and risk reports.
- Consultants or agencies who need repeatable client-facing deliverables.

## Product Principles

1. **Universal before vertical**  
   The platform should not be locked to UX, Figma, research, or a specific product category. UX/design can be the first module, but the core system must work for many product workflows.

2. **Evaluation is the differentiator**  
   The product is not impressive because it generates artifacts. It is impressive because it checks requirement coverage, grounding, logic, risk, and quality.

3. **Context should become reusable memory**  
   Every project should leave behind reusable context: goals, constraints, sources, decisions, rubrics, findings, and workflow patterns.

4. **Work should be inspectable**  
   AI should show what it used, what it assumed, what it skipped, and why it made choices.

5. **Calm surface, powerful depth**  
   The UI should feel approachable like a soft personal workspace, but expose a focused canvas and rigorous review system when users need serious work.

## Visual Direction

The visual style can combine two modes from the references:

### Mode A: Calm Memory Workspace

Inspired by the soft, spacious companion-style screen:

- warm off-white background,
- gentle pastel accents,
- left-side navigation,
- central stream of memory/project cards,
- right-side assistant or insight panel,
- rounded input bar,
- low-friction capture of thoughts, links, files, and goals.

Use this mode for:

- home,
- project memory,
- context capture,
- daily planning,
- saved insights,
- lightweight conversation.

### Mode B: Focus Canvas

Inspired by the dark grid editing workspace:

- black or near-black canvas,
- subtle grid,
- floating toolbar,
- right-side generation/review panel,
- bottom artifact/version strip,
- focused "Magic" action for AI operations,
- export and overview actions in the top right.

Use this mode for:

- workflow mapping,
- artifact generation,
- prototype/research/report editing,
- evaluation review,
- side-by-side comparison,
- presentation/export mode.

### Design Rule

The product should feel like:

> a calm personal workspace outside, a serious product operating room inside.

## Product Architecture: 1-4 Steps

## 1. Capture Context

### Goal

Help users collect messy product context and turn it into a clear working brief.

### User Problem

People begin product work with scattered material:

- rough ideas,
- PRDs,
- screenshots,
- Figma links,
- customer feedback,
- meeting notes,
- research notes,
- business constraints,
- competitor references,
- Slack or email fragments.

AI often generates weak output because the context is incomplete, mixed, or not structured.

### Core Features

#### 1.1 Project Inbox

A central place to drop:

- text notes,
- URLs,
- screenshots,
- files,
- meeting notes,
- research snippets,
- customer quotes,
- product requirements,
- design references.

Each item becomes a **Source Card** with:

- title,
- type,
- upload date,
- source owner,
- short summary,
- extracted claims,
- confidence,
- related goals,
- related workflows.

#### 1.2 Goal Clarifier

The assistant asks structured questions:

- What are you trying to create?
- Who is it for?
- What decision are you trying to make?
- What does success look like?
- What constraints must be respected?
- What existing material should be treated as source truth?

Output:

- project goal,
- target user,
- problem statement,
- success criteria,
- constraints,
- unknowns,
- required artifact type.

#### 1.3 Context Map

A lightweight graph that connects:

- sources,
- goals,
- user segments,
- requirements,
- constraints,
- open questions,
- decisions.

This is not only a knowledge graph for the user's own wiki. It is a project-level memory layer that any team can use.

#### 1.4 Memory Conversion

Users can press **Convert to Memory** to turn a useful conversation or source into structured project memory.

Memory types:

- requirement,
- insight,
- decision,
- constraint,
- user quote,
- risk,
- pattern,
- open question,
- reusable workflow.

### Main Screens

- Home / Workspace Stream
- Project Inbox
- Source Card Detail
- Goal Clarifier Chat
- Context Map
- Memory Library

### Output of Step 1

```text
Project Brief
Source Cards
Goal Statement
Constraints
Success Criteria
Open Questions
Reusable Memory
```

### MVP Scope

Must have:

- text input,
- file/link cards,
- goal clarifier,
- source summaries,
- project brief export.

Later:

- browser extension,
- Slack/Notion/Figma import,
- team comments,
- automatic source clustering.

## 2. Structure Workflow

### Goal

Turn project context into a structured workflow before generating the final artifact.

### User Problem

AI tools often jump directly from prompt to output. This skips the reasoning layer that product teams need:

- what steps are involved,
- what requirements map to which artifact section,
- where assumptions appear,
- what needs human review,
- what states or edge cases are missing.

### Core Features

#### 2.1 Workflow Builder

A canvas that creates a workflow from the brief.

Example workflow types:

- PRD to implementation plan,
- brief to prototype,
- research notes to insight report,
- customer issues to support SOP,
- product idea to MVP experiment,
- competitor references to positioning memo,
- dashboard request to metrics spec,
- launch goal to go-to-market checklist.

Each workflow contains:

- steps,
- inputs,
- outputs,
- owner,
- required evidence,
- quality checks,
- review gates.

#### 2.2 Artifact Planner

The system asks: "What should this workflow produce?"

Artifact types:

- PRD,
- UX flow,
- prototype,
- research synthesis,
- roadmap,
- experiment plan,
- dashboard spec,
- internal SOP,
- onboarding flow,
- content strategy,
- implementation brief,
- executive summary.

For each artifact, the system defines:

- required sections,
- quality rules,
- source dependencies,
- review criteria,
- export format.

#### 2.3 Assumption and Risk Detector

Before generation, the system identifies:

- missing requirements,
- conflicting sources,
- ambiguous goals,
- weak evidence,
- feasibility risks,
- stakeholder risks,
- user experience risks,
- technical unknowns.

#### 2.4 Rubric Setup

Users can select or customize evaluation rubrics.

Universal rubrics:

- requirement coverage,
- source grounding,
- logic consistency,
- clarity,
- feasibility,
- decision explainability,
- risk visibility.

Domain rubrics:

- UX quality,
- accessibility,
- localization,
- research integrity,
- product strategy,
- content quality,
- implementation readiness.

### Main Screens

- Workflow Canvas
- Artifact Planner
- Rubric Builder
- Assumption Review
- Human Review Gate

### Output of Step 2

```text
Workflow Map
Artifact Plan
Evaluation Rubric
Assumption List
Risk Register
Review Gates
```

### MVP Scope

Must have:

- workflow templates,
- artifact planner,
- assumptions list,
- simple rubric builder.

Later:

- visual node editor,
- reusable workflow marketplace,
- role-based review gates,
- workflow versioning.

## 3. Generate Artifact

### Goal

Generate a useful, reviewable artifact from the structured workflow, not from a raw prompt alone.

### User Problem

Generated output often looks polished but is hard to trust. Users need to see:

- which sources were used,
- which requirements were covered,
- which parts are generated,
- which parts need human review,
- how to revise the result.

### Core Features

#### 3.1 Artifact Studio

A focused generation workspace with:

- central canvas or document view,
- floating AI toolbar,
- right-side assistant panel,
- version history,
- source references,
- comments,
- review status.

#### 3.2 Magic Actions

Context-aware AI actions:

- generate first draft,
- improve structure,
- fill missing section,
- simplify language,
- convert to presentation,
- turn into checklist,
- create user flow,
- create implementation brief,
- create prototype,
- create executive summary,
- compare with source,
- explain decision.

#### 3.3 Multi-format Output

The platform should support multiple artifact outputs:

- Markdown doc,
- slide outline,
- structured PRD,
- HTML prototype,
- UX flow,
- issue/task list,
- evaluation report,
- SOP,
- research report,
- CSV-style requirement table.

#### 3.4 Version Strip

Like the slide thumbnails in the reference image, show generated versions at the bottom:

- v1 generated draft,
- v2 after constraints,
- v3 after review,
- v4 export-ready.

Each version shows:

- score,
- changed sections,
- unresolved issues,
- reviewer notes.

#### 3.5 Role Agents

Instead of one generic assistant, the product can simulate several review roles:

- Product Strategist,
- User Advocate,
- Research Auditor,
- Design Reviewer,
- Technical Feasibility Reviewer,
- Business Risk Reviewer,
- Editor.

The user can turn roles on or off depending on the workflow.

### Main Screens

- Artifact Studio
- Magic Toolbar
- Version Strip
- Source Reference Panel
- Role Agent Panel
- Export Modal

### Output of Step 3

```text
Generated Artifact
Source References
Version History
Reviewer Notes
Decision Explanations
Export Package
```

### MVP Scope

Must have:

- Markdown artifact generation,
- source-linked sections,
- version history,
- role-based review comments,
- export to Markdown/HTML.

Later:

- interactive prototypes,
- slide deck generation,
- Figma export,
- Jira/Linear ticket export,
- Notion/Google Docs sync.

## 4. Evaluate and Improve

### Goal

Score the generated artifact against the original goal, source material, and selected quality rubric.

### User Problem

Most AI outputs sound confident. Product teams need a way to ask:

- Is it complete?
- Is it true to the source?
- Is it internally consistent?
- Is it useful for the next person?
- What should be fixed first?

### Core Features

#### 4.1 Evaluation Engine

Runs checks across:

- requirement coverage,
- source grounding,
- contradiction detection,
- missing assumptions,
- unclear ownership,
- vague language,
- feasibility gaps,
- risk visibility,
- domain-specific quality.

#### 4.2 Scorecard

Each artifact receives a scorecard:

```text
Requirement Coverage: 84
Source Grounding: 77
Logic Consistency: 91
Clarity: 82
Feasibility: 68
Decision Explainability: 73
Overall Readiness: Reviewable
```

Readiness levels:

- Draft,
- Reviewable,
- Decision-ready,
- Implementation-ready,
- Publish-ready.

#### 4.3 Findings List

Findings are sorted by severity:

- P0: cannot use until fixed,
- P1: major issue,
- P2: moderate issue,
- P3: polish or suggestion.

Each finding includes:

- issue,
- evidence,
- affected section,
- suggested fix,
- confidence,
- owner.

#### 4.4 Improve Loop

Users can apply fixes:

- rewrite selected section,
- add missing requirement,
- ask for source evidence,
- split assumptions,
- create follow-up task,
- send to human reviewer,
- regenerate with constraints.

#### 4.5 Learning Memory

After review, the system saves:

- accepted decisions,
- rejected outputs,
- recurring issues,
- preferred phrasing,
- team quality rules,
- reusable workflow patterns.

This makes future projects better without locking the product to one user's private wiki.

### Main Screens

- Evaluation Dashboard
- Scorecard
- Findings List
- Evidence Viewer
- Improve Loop
- Team Memory Settings

### Output of Step 4

```text
Evaluation Report
Severity-ranked Findings
Improvement Tasks
Final Artifact
Reusable Team Memory
Workflow Template
```

### MVP Scope

Must have:

- requirement coverage check,
- source grounding check,
- severity-ranked findings,
- improvement suggestions,
- final report export.

Later:

- automated browser testing,
- visual regression,
- accessibility audit,
- benchmark datasets,
- team-level quality analytics.

## Core Product Modules

### 1. Workspace

The user's home base:

- projects,
- recent memories,
- active workflows,
- saved artifacts,
- unresolved findings,
- team quality rules.

### 2. Context Engine

Turns messy input into structured material:

- source parsing,
- claim extraction,
- goal clarification,
- requirement detection,
- memory creation.

### 3. Workflow Engine

Turns context into process:

- workflow templates,
- step definitions,
- artifact plans,
- review gates,
- role agents.

### 4. Artifact Engine

Creates outputs:

- docs,
- plans,
- flows,
- reports,
- prototypes,
- specs,
- task lists.

### 5. Evaluation Engine

Checks quality:

- requirement coverage,
- grounding,
- logic,
- completeness,
- feasibility,
- clarity,
- domain-specific rules.

### 6. Memory Engine

Learns from work:

- decisions,
- rejected outputs,
- recurring issues,
- style preferences,
- quality standards,
- reusable workflows.

## Key Objects / Data Model

```text
Workspace
  Project
    Source
    Goal
    Constraint
    Requirement
    Workflow
      Step
      Input
      Output
      ReviewGate
    Artifact
      Version
      Section
      SourceReference
    Rubric
      Criterion
      Score
    Finding
      Severity
      Evidence
      SuggestedFix
    Memory
      Type
      Confidence
      ReuseScope
```

## Information Architecture

```text
Home
  Projects
  Memories
  Templates
  Evaluations
  Settings

Project
  Inbox
  Brief
  Context Map
  Workflow
  Artifact Studio
  Evaluation
  Exports

Templates
  Product Planning
  UX / Design
  Research
  Operations
  Content
  Engineering Handoff
```

## Example Use Cases

### Use Case 1: PM Creates a PRD

Input:

- product idea,
- customer feedback,
- business goal,
- constraints.

Output:

- PRD,
- requirement table,
- acceptance criteria,
- risk list,
- evaluation report.

### Use Case 2: Designer Creates a Flow

Input:

- UX brief,
- screenshots,
- design rules,
- user segment.

Output:

- user flow,
- screen inventory,
- interaction states,
- prototype plan,
- UX findings.

### Use Case 3: Researcher Synthesizes Interviews

Input:

- interview notes,
- survey summary,
- research question.

Output:

- insight report,
- evidence table,
- theme map,
- confidence notes,
- follow-up research questions.

### Use Case 4: Founder Plans an MVP

Input:

- idea,
- target market,
- competitor links,
- constraints.

Output:

- MVP scope,
- experiment plan,
- landing page brief,
- success metrics,
- launch checklist.

### Use Case 5: Ops Team Creates an SOP

Input:

- repeated support issue,
- internal process notes,
- policy constraints.

Output:

- SOP,
- escalation rules,
- automation opportunities,
- training checklist,
- risk review.

## MVP Definition

### MVP Goal

Build a working local web app that proves the full loop:

```text
Capture context -> structure workflow -> generate artifact -> evaluate artifact
```

### MVP Feature Set

Must ship:

- project creation,
- source card input,
- goal clarifier,
- workflow template picker,
- artifact planner,
- Markdown artifact generation,
- requirement coverage evaluation,
- source grounding evaluation,
- severity-ranked findings,
- exportable report.

Nice to have:

- dark focus canvas,
- role agent reviews,
- version strip,
- visual comparison for design artifacts,
- Obsidian sync.

Not in MVP:

- full team collaboration,
- complex permissions,
- marketplace,
- real-time multiplayer,
- native Figma plugin,
- enterprise admin.

## 4-phase Build Plan

## Phase 1: Product Skeleton

Purpose:

- prove the product concept and interaction model.

Build:

- landing-free app shell,
- project workspace,
- context inbox,
- source card model,
- goal clarifier,
- project brief generation.

Deliverable:

- user can create a project, add context, and generate a structured brief.

## Phase 2: Workflow and Artifact Studio

Purpose:

- turn context into a repeatable workflow and artifact.

Build:

- workflow template picker,
- artifact planner,
- artifact studio,
- magic actions,
- version strip,
- Markdown/HTML export.

Deliverable:

- user can generate a PRD, research report, SOP, or prototype plan from structured context.

## Phase 3: Evaluation Engine

Purpose:

- make the product meaningfully different from generic chat tools.

Build:

- rubric builder,
- requirement coverage check,
- source grounding check,
- logic consistency check,
- severity findings,
- scorecard,
- improve loop.

Deliverable:

- user can see what is missing, weak, unsupported, or risky in the AI output.

## Phase 4: Memory and Templates

Purpose:

- make the system reusable across teams and domains.

Build:

- reusable team memory,
- workflow templates,
- accepted/rejected output memory,
- quality rule library,
- template gallery,
- example projects.

Deliverable:

- user can reuse a proven workflow and improve future outputs based on previous reviews.

## Example Templates to Include

Initial template set:

- Product Idea to MVP Plan
- PRD to Implementation Brief
- UX Brief to Prototype Plan
- Research Notes to Insight Report
- Customer Feedback to Opportunity Map
- Support Issue to SOP
- Dashboard Request to Metrics Spec
- Launch Goal to Go-to-market Checklist

## Evaluation Criteria Library

Universal:

- goal alignment,
- requirement coverage,
- source grounding,
- internal consistency,
- clarity,
- actionability,
- feasibility,
- risk visibility,
- assumption visibility.

Product:

- user value,
- business alignment,
- scope discipline,
- success metric quality,
- prioritization logic.

UX:

- flow completeness,
- state coverage,
- accessibility risk,
- localization risk,
- interaction clarity,
- visual hierarchy.

Research:

- evidence strength,
- claim support,
- participant quote traceability,
- interpretation vs fact separation,
- confidence labeling.

Operations:

- ownership clarity,
- escalation logic,
- exception handling,
- compliance risk,
- training readiness.

## Technical Plan

Recommended stack for a polished MVP:

```text
Frontend: Next.js or Vite React
Styling: Tailwind + shadcn-style primitives
Canvas: React Flow or tldraw-style canvas for workflow maps
Storage: local SQLite or Postgres
LLM: provider-agnostic adapter
Exports: Markdown, HTML, PDF later
Testing: Playwright for UI flows
Evaluation: rubric prompts + deterministic checks where possible
```

Repo shape:

```text
product-workflow-studio/
  README.md
  AGENTS.md
  docs/
    agent-context.md
    product-spec.md
    architecture.md
    evaluation-model.md
  examples/
    product-idea-to-mvp/
    research-notes-to-insights/
    support-issue-to-sop/
    ux-brief-to-prototype/
  prompts/
    clarify-goal.md
    build-workflow.md
    generate-artifact.md
    evaluate-artifact.md
  evals/
    requirement-coverage/
    source-grounding/
    logic-consistency/
  src/
    app/
    components/
    workflow-engine/
    artifact-engine/
    evaluation-engine/
    memory-engine/
  test-results/
```

## Success Metrics

Product quality metrics:

- time from messy input to structured brief,
- percentage of requirements covered in generated artifacts,
- number of unsupported claims caught,
- number of missing assumptions surfaced,
- artifact readiness score before and after improve loop,
- user acceptance rate of suggested fixes.

User value metrics:

- repeat usage across different workflows,
- number of templates reused,
- number of artifacts exported,
- number of team quality rules created,
- reduction in manual review time.

Portfolio metrics:

- 3 polished example projects,
- 1 public demo video,
- 1 architecture write-up,
- 1 evaluation-method write-up,
- 1 interactive prototype,
- 1 before/after artifact comparison.

## Open Questions

- Should the first demo focus on PM workflows, UX workflows, or research workflows?
- Should the product feel more like a calm memory app first or a dark professional canvas first?
- Should the MVP be local-first or team/cloud-first?
- How much of evaluation should be deterministic versus LLM-judged?
- Should Obsidian sync be an optional export, or a core early feature?

## Linked Concepts

- [[concepts/ai-agents/agent-memory|Agent Memory]]
- [[concepts/ai-agents/product-evals|Product Evals]]
- [[concepts/ai-agents/ai-agent-workflow|AI Agent Workflow]]
- [[concepts/product-management/ai-native-product-management|AI-Native Product Management]]
- [[concepts/ai-agents/planning-to-code-workflow|Planning-to-Code Workflow]]
- [[concepts/infrastructure-dev/design-review-automation|Design Review Automation]]
- [[concepts/ai-agents/interactive-specs|Interactive Specs]]

## Key Decisions

- Product should be domain-agnostic, not limited to Bonny's personal LLM Wiki.
- UX/design should be an example module, not the entire product boundary.
- Evaluation should be the main differentiator.
- Memory should be reusable at project/team level, not only as private notes.

## Tasks & Next Steps

- [ ] Choose first demo workflow.
- [ ] Write a one-page PRD for the MVP.
- [ ] Define 8 initial templates.
- [ ] Define the first 10 universal evaluation criteria.
- [ ] Sketch the three core screens: Home, Workflow Canvas, Evaluation Report.
- [ ] Build a static prototype.
- [ ] Build the local MVP loop: context -> workflow -> artifact -> evaluation.
- [ ] Prepare 3 public example projects.
