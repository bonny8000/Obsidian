# LLM-Wiki

A personal, AI-maintained knowledge base built on Obsidian — where raw source evidence is preserved and AI agents compile it into a durable, linked Markdown wiki.

> Think of Obsidian as the visual IDE, this folder as the knowledge codebase, and the AI agent as the librarian + compiler.

---

## What this is

- **`raw/`** preserves source evidence — PDFs, web captures, transcripts, notes. Immutable; never edited in place.
- **`wiki/`** is the AI-maintained synthesis layer — concept pages, methods, comparisons, analyses, maps, projects, decisions.
- **`CLAUDE.md` + `AGENTS.md`** are the operating manual AI agents follow. Every ingest preserves provenance, links concepts, updates indexes, and logs the change.

The goal is **compounding knowledge**: every source that comes in becomes citable, linkable evidence; every concept earns its place; nothing important disappears at the end of a session.

---

## Open in Obsidian

```text
D:\Obsidian\LLM-Wiki
```

Everything lives on the `D:` drive. Don't create or sync a copy under `C:\Users\bonny_chen`.

---

## Directory map

```text
LLM-Wiki/
├── CLAUDE.md            # entry schema for AI agents
├── AGENTS.md            # full operating rules
├── index.md             # top-level content catalog
├── log.md               # append-only operations log
├── README.md            # this file
├── raw/                 # immutable source material
│   ├── *.pdf            # books, whitepapers, decks
│   ├── files/           # local attachments
│   └── web/             # captured web sources
├── scripts/             # audit / lint / backfill utilities
└── wiki/
    ├── overview.md      # evolving synthesis of the whole base
    ├── index.md         # Obsidian dashboard + graph entry
    ├── sources/         # one page per ingested source
    ├── concepts/        # durable concepts grouped by cluster
    ├── methods/         # UX research method pages
    ├── comparisons/     # decision matrices
    ├── analyses/        # synthesized memos
    ├── maps/            # topic maps + dashboards
    ├── playbooks/       # operational checklists
    ├── projects/        # active initiatives
    ├── decisions/       # UX/Product Decision Records
    ├── queries/         # saved Q&A
    ├── logs/            # change log + lint reports
    └── _templates/      # reusable page templates
```

---

## What's inside

| Cluster | Pages | Focus |
| --- | --- | --- |
| UX research | 70 concepts + 14 methods | Quant + qual rigor, statistics, ResearchOps, AI-assisted research |
| AI agents & agentic engineering | 42 concepts | Agent Skills, MCP, AGENTS.md, DESIGN.md, harness engineering, memory |
| Infrastructure & design systems | 39 concepts | AI-native design systems, design-to-code, tokens, knowledge linting |
| Product management | 21 concepts | AI-native PM, product taste, role convergence |
| Robotics & spatial AI | 29 concepts | Physical AI, embodied learning, robotics supply chain |
| Agent experience (AX) | 8 concepts | Trust calibration, transparency, proactivity, mental-model onboarding |
| **Sources** | **84** | **66 marked `llm_ready: true`** |

Plus 13 topic maps, 3 comparison matrices, 1 analysis memo, 4 playbooks, 8 projects, 73 saved queries, and 2 decision records.

Start from **[wiki/overview.md](wiki/overview.md)** for the synthesis view, **[wiki/index.md](wiki/index.md)** for the Obsidian dashboard, or **[index.md](index.md)** for the top-level catalog.

---

## How to use it

1. **Drop a source into `raw/`** — a PDF, a web clipping, a transcript, anything to be remembered.
2. **Ask an AI agent to ingest it** — e.g. *"Ingest the new file in raw/ into the wiki"*. The agent reads it, creates a source page, updates or creates concept pages, links the graph, and logs the change.
3. **Read the compiled wiki in Obsidian** — use the graph view to inspect concept relationships; jump between maps, methods, and sources via wikilinks.
4. **Query the wiki when you need an answer** — e.g. *"What does the wiki say about Bayesian credible intervals?"*. Grounded answers cite source pages and raw files.

### Useful prompts

```text
Ingest everything new in raw/ into the wiki.
```

```text
Query the wiki: what are the main design implications of Agent Skills?
```

```text
Lint the wiki and fix low-risk issues.
```

```text
Create a topic map for the current wiki.
```

---

## Recent ingests

- **2026-06-17** — Agentic engineering trilogy (SDLC Day-1, Interoperability Day-2, Agent Skills Day-3); Atlassian DESIGN.md + Context Engine pair; MeasuringU 5-pack (TAC-10 screening, synthetic users review, credible vs confidence intervals, Bayes priors, banner tables). Plus 11 new concepts and a four-primitive routing comparison ([Skills vs MCP vs AGENTS.md vs DESIGN.md](wiki/comparisons/skills-vs-mcp-vs-agents-md.md)).
- **2026-06-16** — Detailed MeasuringU n ≥ 30 statistics ingest; Small-N UX Statistics Checklist playbook.
- **2026-06-12** — Vault moved to `D:\Obsidian\LLM-Wiki`; UX research workspace schema, Agent Experience cluster, foundational AX sources (Lee & See, Horvitz, Amershi), Quant UXR book trio rebuilt from full PDFs.

Full history in [log.md](log.md) and [wiki/logs/change-log.md](wiki/logs/change-log.md).

---

## For AI agents

- Read **[CLAUDE.md](CLAUDE.md)** first — the entry schema.
- Then **[AGENTS.md](AGENTS.md)** — full operating rules covering ingest, project, query, and lint workflows.
- Preserve `raw/`. Update existing pages before creating duplicates. Record meaningful changes in `log.md` and `wiki/logs/change-log.md`.
