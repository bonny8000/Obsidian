---
type: source
status: active
created: 2026-05-21
tags: [source, ai-portfolio, data-modeling, ontology]
sources: [raw/web/hsol-ai-portfolio-6.md]
updated: 2026-06-12
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 1.0
---

# AI Portfolio Making (6): A Data Model for a Person

## Citation

Lim, H. (2026). *AI ?秒?渠收??諤篣?(6) ???禺???諻??木???域??諈刺*. hsol.im.
URL: https://hsol.im/ai-%ED%8F%AC%ED%8A%B8%ED%8F%B4%EB%A6%AC%EC%98%A4-%EB%A7%8C%EB%93%A4%EA%B8%B0-6-%ED%95%9C-%EC%82%AC%EB%9E%8C%EC%9D%84-%EB%B0%9B%EC%95%84%EB%93%A4%EC%9D%B4%EB%8A%94-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%AA%A8%EB%8D%B8-08a991b00299

## Source Type

Blog Post (Korean)

## Location

`raw/web/hsol-ai-portfolio-6.md`

## Summary

The article describes a method for structuring a personal "AI portfolio" by adopting the **Palantir Foundry Object Backend** data model. The goal is to move beyond the limitations of simple tables (Notion) and unstructured notes (Obsidian) by creating a formal ontology of objects and links. This allows the author to treat their career history as a queryable graph, enabling more precise reflection and a "deterministic" website UI.

## Key Claims

- Personal history is better modeled as a graph of objects than as a collection of notes or a flat table.
- Adopting enterprise data ontologies (like Palantir Foundry's) for personal knowledge management (PKM) improves data integrity and queryability.
- A "Deterministic UI" means the portfolio's website is a direct function of the underlying data vault.
- Structured data enables "Graph Traversal for Retrospection," allowing for more accurate recall of past projects and decisions.

## Concepts Linked

- [[concepts/infrastructure-dev/palantir-foundry-ontology|Palantir Foundry Ontology]]
- [[concepts/infrastructure-dev/object-backend|Object Backend]]
- [[concepts/infrastructure-dev/object-graph-mapping|Object-Graph Mapping]]
- [[concepts/infrastructure-dev/objectview|ObjectView]]
- [[concepts/ai-agents/1-person-vault|1-Person Vault]]
- [[concepts/infrastructure-dev/deterministic-ui|Deterministic UI]]
- [[concepts/infrastructure-dev/graph-based-retrospection|Graph-based Retrospection]]

## Useful Examples

- Current example source: use examples, tables, cases, or named artifacts already present elsewhere in this note; otherwise return to `raw/web/hsol-ai-portfolio-6.md` before asking an LLM for concrete examples.

## Constraints / Caveats

- Coverage is `substantial` and ingest level is `standard`; do not treat this source as fully digested unless `coverage: full`.
- Claims should be checked against `raw/web/hsol-ai-portfolio-6.md` when used for recommendations, metrics, or external-facing work.

## Reliability Notes

- Coverage is `substantial` and ingest level is `deep`; do not treat this source as fully digested unless `coverage: full`.
- Claims should be checked against `raw/web/hsol-ai-portfolio-6.md` when used for recommendations, metrics, or external-facing work.

- Coverage is `substantial` and ingest level is `standard`; do not treat this source as fully digested unless `coverage: full`.

Primary source for the author's personal experiment. Uses established enterprise concepts from Palantir Foundry as a framework.

## Design Implications

- Use this source to shape AI-agent workflow, toolchain, and automation prompts.
- Connect it with [[concepts/infrastructure-dev/palantir-foundry-ontology]], [[concepts/infrastructure-dev/object-backend]], [[concepts/infrastructure-dev/object-graph-mapping]], [[concepts/infrastructure-dev/objectview]] before turning it into a project recommendation.

## Tensions

- Backfill note: source-specific tensions were not separately extracted in the earlier ingest. Compare this source with related concepts and maps before treating its framing as settled.

## Open Questions

- What evidence, examples, or counterexamples should be extracted from the raw source before marking this as `coverage: full`?
- Which linked concept would change most if this source were contradicted?

## LLM Use

- **Use for:** AI-agent workflow, toolchain, and automation prompts.
- **Do not use for:** unsupported exact claims beyond the source note's `substantial` coverage.
- **Best prompt pattern:** Ask the LLM to combine this source with its linked concepts, then verify any specific claim against the raw source before final use.

## Backfill Status

- Retrofitted on 2026-06-12 by `scripts/backfill_llm_ready.py` from the existing source note.
- This standardizes the note for LLM use; it does not by itself mean the raw source has been fully re-read.
