# LLM Wiki Operating Instructions

You are maintaining a local Obsidian-compatible LLM Wiki for Bonny.

The goal is to turn raw source material into a durable, interlinked Markdown knowledge base. Treat Obsidian as the visual IDE, this folder as the knowledge codebase, and the AI agent as the librarian/compiler.

## Directory Contract

- `raw/`: immutable source material. Read from this folder, but do not edit, move, rename, or delete files here unless Bonny explicitly asks.
- `wiki/`: AI-maintained Markdown wiki. Create and update files here.
- `wiki/overview.md`: high-level synthesis of the whole knowledge base.
- `wiki/sources/`: one page per source, summarizing provenance and useful claims.
- `wiki/concepts/`: one page per durable concept, pattern, person, tool, framework, or decision.
- `wiki/maps/`: index pages, topic maps, timelines, comparison tables, and graph summaries.
- `wiki/methods/`: one page per UX research method, with use cases, procedure, outputs, quality bar, and LLM assistance guidance.
- `wiki/comparisons/`: decision tables that compare methods, tools, risks, claims, or research approaches.
- `wiki/analyses/`: synthesized research memos, audits, and project-facing interpretations.
- `wiki/canvases/`: Obsidian Canvas diagrams for architecture, workflows, and graph navigation; diagrams are navigation, not evidence.
- `wiki/playbooks/`: reusable operational gates and decision checklists.
- `wiki/queries/`: saved answers to important questions.
- `wiki/projects/`: active, ongoing, or completed UX/Product initiatives and experiments.
- `wiki/decisions/`: Lightweight UX/Product Decision Records (UXDRs) documenting choices and evidence.
- `wiki/drafts/`: staging area for pages awaiting review under the Safe Ingest Promotion Workflow; promote to their final folder after approval.
- `wiki/logs/`: ingest logs, lint reports, and maintenance records.
- `wiki/_templates/`: reusable page templates.

## Core Rules

1. Preserve source truth. Never let a synthesized wiki page become the only evidence for a claim.
2. Prefer small linked pages over long unstructured notes.
3. Use Obsidian links for important relationships, for example `[[concepts/llm-wiki|LLM Wiki]]`.
4. Every substantive claim should have provenance: source page, raw file path or URL, date observed, and confidence.
5. Separate facts from interpretations. Label weak, inferred, or speculative claims.
6. Update existing pages before creating duplicates.
7. Log meaningful changes in `log.md` and `wiki/logs/change-log.md`.
8. Do not delete wiki pages without first recording why, unless Bonny explicitly asks for cleanup.
9. Use the [[wiki/playbooks/safe-ingest-promotion-workflow|Safe Ingest Promotion Workflow]] for draft, review, apply, and validation gates. Human approval is required for high-risk claims, destructive graph edits, external publishing, or consent/privacy-sensitive material.
10. Any script that edits more than ~5 wiki pages must follow the [[wiki/playbooks/safe-script-maintenance|Safe Script Maintenance playbook]]: dry-run, spot-check, apply on a clean git tree, re-audit, idempotence check, and a change-log entry.
11. Prefer synthesis over accumulation: when an ingest brings a cluster to roughly five related sources, create or update an analysis memo in `wiki/analyses/` (and a decision table in `wiki/comparisons/` if the cluster informs a choice) instead of only adding more source pages.
12. Update `README.md` (including current count tables and shape metrics), `index.md`, `wiki/index.md`, `wiki/overview.md`, `log.md`, and `wiki/logs/change-log.md` whenever new files are added, updated, or ingested.
13. After every user-requested vault change, run the relevant validation checks, review git status and git diff, commit all in-scope changes with a concise message, and push directly to origin/main. Never force-push or rewrite history; if unrelated changes are present or push fails, stop and report before staging or retrying.

## Naming

- Use lowercase kebab-case filenames.
- Use date prefixes for logs and saved query outputs when useful: `2026-05-18-topic.md`.
- Keep filenames stable once linked.
- Prefer descriptive page titles in the first H1.
- Canonical wiki-link form for new or edited links: vault-rooted path without leading slash, e.g. `[[wiki/concepts/ux-research/cognitive-load|Cognitive Load]]`. Normalize old-style links opportunistically when touching a page; never as a standalone bulk rewrite. See [[wiki/decisions/2026-07-20-link-path-convention|the decision record]].

## Standard Frontmatter

Use this frontmatter for wiki pages when applicable:

```yaml
---
type: concept | source | map | query | log | project | decision
status: draft | active | on-hold | completed | superseded
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: []
sources: []
confidence: 0.0
---
```

Source pages must also include these LLM-readiness fields:

```yaml
ingest_level: light | standard | deep
coverage: partial | substantial | full
llm_ready: true | false
raw_preserved: true | false
```

Use `light` for metadata, summary, and a few reusable ideas. Use `standard` when the source has raw provenance, key claims, caveats, linked concepts, and at least one use case for future reasoning. Use `deep` for books, PDFs, research-method references, source families, transcripts, or sources Bonny expects to cite repeatedly. Do not mark `coverage: full` unless the raw source was read or captured end-to-end and the source page says what was covered.

## Ingest Workflow

When Bonny says "ingest", "compile", "add this to the wiki", or places new material in `raw/`:

1. Inventory the relevant raw files.
2. Read the source material enough to identify claims, entities, concepts, methods, and decisions.
3. Create or update a source page in `wiki/sources/`.
4. Set `ingest_level`, `coverage`, `llm_ready`, and `raw_preserved` honestly.
5. Fill the LLM-ready source sections: `Key Claims`, `Useful Examples`, `Constraints / Caveats`, `Design Implications`, `Tensions`, `Open Questions`, `Concepts Linked`, `LLM Use`, and `Reliability Notes`.
6. Create or update concept pages in `wiki/concepts/`.
7. If the source changes UX research practice, update the relevant method page in `wiki/methods/`.
8. If the source helps choose between approaches, update a comparison page in `wiki/comparisons/`.
9. If multiple sources are synthesized into a recommendation, create or update an analysis memo in `wiki/analyses/`.
10. Add backlinks between source, concept, method, comparison, and analysis pages.
11. Update `wiki/overview.md`, `wiki/index.md`, and any relevant map in `wiki/maps/`.
12. Record the ingest in `log.md` and `wiki/logs/change-log.md`.
13. Report what changed and what remains uncertain.
14. When a workflow is easier to understand visually, update `wiki/canvases/` and link the Canvas from a map page. Validate Canvas JSON and edge endpoints before completion.

Do not paste copyrighted articles in full. Store a link, citation metadata, short excerpt only when necessary, and an AI-written summary.

## Project Workflow

When Bonny mentions an active project, goal, or experiment:

1. Create or update a project page in `wiki/projects/` using `wiki/_templates/project-template.md`.
2. Link the project to relevant `wiki/concepts/` to ground the work in existing evidence.
3. If a decision is made, create a Decision Record in `wiki/decisions/` using `wiki/_templates/decision-record.md`.
4. Ensure every decision links to at least one concept or source as justification.
5. Update `wiki/index.md` to reflect the current active project status.

## Query Workflow

When Bonny asks a question about the knowledge base:

1. Search `wiki/` first.
2. Use `raw/` only to verify or fill gaps.
3. Answer with citations to wiki pages and source paths or URLs.
4. If the answer creates reusable knowledge, save it in `wiki/queries/` and link it from relevant concept pages.
5. If the wiki lacks enough evidence, say so plainly and propose the next source to ingest.

## Lint Workflow

When Bonny says "lint", "health check", "clean up", or "audit the wiki":

1. Find orphaned concept pages.
2. Find broken Obsidian links.
3. Find duplicate or near-duplicate pages.
4. Find claims without sources.
5. Find conflicts between pages or outdated claims.
6. Find important recurring terms that do not yet have concept pages.
7. Write results to `wiki/logs/lint-report.md`.
8. Apply low-risk fixes directly, and list higher-risk fixes for Bonny to approve.

## Conflict Handling

When sources disagree:

- Do not silently merge the conflict away.
- Add a `Conflicts / caveats` section to affected pages.
- Prefer newer and primary sources when recency matters.
- Record superseded claims instead of deleting them.
- Use confidence scores:
  - `0.90-1.00`: directly supported by primary or repeated reliable sources.
  - `0.70-0.89`: well supported but missing one verification step.
  - `0.40-0.69`: plausible but partial, contextual, or inferred.
  - `0.00-0.39`: weak, speculative, or contradicted.

## Page Shape

Concept pages should usually contain:

- Summary
- Why it matters
- Key claims
- Related concepts
- Sources
- Open questions

Source pages should usually contain:

- Citation
- Source type
- Location in `raw/` or URL
- Summary
- Key claims
- Useful examples
- Constraints / caveats
- Design implications
- Tensions
- Open questions
- Concepts linked from this source
- LLM use guidance
- Reliability notes
- Backfill status when the note was upgraded from an older, thinner source page

Method pages should usually contain:

- Purpose
- Use When
- Avoid When
- Inputs
- Procedure
- Outputs
- Quality Bar
- LLM Assistance
- Related Concepts
- Source Evidence

Comparison pages should usually contain:

- Decision question
- Criteria
- Matrix
- Recommendation pattern
- Source evidence

Analysis pages should usually contain:

- Research question
- Evidence base
- Synthesis
- Implications
- Risks and counterpoints
- Next research actions

Query pages should usually contain:

- Question
- Short answer
- Evidence
- Reusable notes added to the wiki
- Follow-up sources needed

Project pages should usually contain:

- Objectives
- Current Status
- Linked Concepts (from `wiki/concepts/`)
- Key Decisions (linked to `wiki/decisions/`)
- Tasks & Next Steps

Decision pages should usually contain:

- Context & Background
- Options Considered
- Decision Made
- Evidence & Justification (links to `wiki/concepts/` or `wiki/sources/`)
- Consequences & Next Steps

## Local Tooling

Use fast local search when possible:

- `rg --files wiki raw`
- `rg "term" wiki raw`
- `git diff` if the vault is version controlled

Prefer structured edits to ad hoc rewriting. Keep unrelated files untouched.
