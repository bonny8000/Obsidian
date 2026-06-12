# LLM-Wiki Operating Schema

This is the operating manual for AI agents working in this Obsidian vault. Read this file at the start of every vault-maintenance session, then use `AGENTS.md` as the detailed source of truth.

## Directory Structure

```text
LLM-Wiki/
|-- CLAUDE.md                 # this file - agent entry schema
|-- AGENTS.md                 # full operating rules
|-- index.md                  # top-level content catalog
|-- log.md                    # append-only chronological operations log
|-- raw/                      # immutable source documents - never modify
|   |-- files/                # local files and attachments
|   `-- web/                  # captured web sources
|-- scripts/                  # audit, lint, and backfill utilities
`-- wiki/
    |-- overview.md           # evolving synthesis of the whole knowledge base
    |-- index.md              # Obsidian dashboard and graph entry point
    |-- sources/              # one source record per ingested source
    |-- methods/              # one UX research method page per method
    |-- concepts/             # concepts, frameworks, theories, and principles
    |-- comparisons/          # comparison tables across methods/tools/claims
    |-- analyses/             # synthesized research memos and audits
    |-- maps/                 # topic maps and source-readiness dashboards
    |-- projects/             # active project plans
    |-- decisions/            # decision records
    |-- queries/              # open questions and future research prompts
    |-- logs/                 # generated and manual maintenance logs
    `-- _templates/           # page templates
```

## Operating Rules

- Preserve `raw/` exactly. Never edit raw captures; create or update wiki pages instead.
- Every source page must keep `ingest_level`, `coverage`, `llm_ready`, and `raw_preserved` honest.
- Use `wiki/sources/` for source-specific evidence, `wiki/concepts/` for reusable ideas, `wiki/methods/` for UX research methods, `wiki/comparisons/` for decision tables, and `wiki/analyses/` for synthesized memos.
- When adding a UX research method, connect it to at least one source and one concept. If evidence is thin, mark the page as partial rather than overstating confidence.
- Update `index.md`, `wiki/index.md`, `wiki/overview.md`, and `log.md` after meaningful ingest or structural changes.

## LLM Use Pattern

1. Start from `index.md` or `wiki/overview.md`.
2. Choose only sources where `llm_ready: true` for grounded synthesis.
3. Use partial sources for ideation only, then return to `raw/` before making recommendations.
4. For UX research work, move in this order: research question -> method page -> comparison page -> source records -> analysis memo.
5. Record major maintenance in `log.md` and `wiki/logs/change-log.md`.

