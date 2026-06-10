---
type: log
status: active
created: 2026-05-21
updated: 2026-05-27
tags: [log, lint, maintenance]
sources: []
confidence: 1.0
---

# Wiki Health Report (2026-05-27)

> [!abstract] Overview
> Full audit of vault structure, link integrity, orphan pages, and metadata compliance. Run after 5 ingest sessions since the previous lint (2026-05-21). Also includes the first Open Questions synthesis pass, which created 72 query pages in `wiki/queries/`.

## ?? Vault Stats

| Folder | Count |
|---|---|
| `wiki/concepts/` | 136 pages |
| `wiki/sources/` | 43 pages |
| `wiki/maps/` | 9 pages |
| `wiki/queries/` | 72 pages (new ??created this session) |
| `wiki/logs/` | 11 pages |
| Frontmatter compliance | **100%** |

---

## ? Resolved Since Last Lint (2026-05-21)

The following broken links from the previous report are **now resolved** ??pages were created during subsequent ingest sessions:

- `[[concepts/infrastructure-dev/on-premise-ai]]` ??- `[[concepts/infrastructure-dev/edge-ai]]` ??- `[[concepts/ux-research/human-in-the-loop]]` ??- `[[concepts/ux-research/ux-writing-tf]]` ??- `[[concepts/ai-agents/long-horizon-tasks]]` ??- `[[concepts/ai-agents/ai-inspection-bot]]` ??- `[[concepts/ai-agents/harness-engineering]]` ??
---

## ? Critical: Broken Links (18 missing concept pages)

The following concepts are referenced in source or concept pages but **do not have a concept page yet**:

> [!danger] Missing Concept Pages
> 1. `[[concepts/infrastructure-dev/agentic-engineering]]` ??referenced in `sources/brunch-ghidesigner-489.md`
> 2. `[[concepts/infrastructure-dev/agentic-technical-debt]]` ??referenced in `sources/founders-playbook-2026.md`
> 3. `[[concepts/ux-research/ai-persona-replication]]` ??referenced in `concepts/contextual-translation.md`, `sources/geeknews-kagi-translate-linkedin.md`
> 4. `[[concepts/antigravity]]` ??referenced in `sources/google-io-2026-agentic-gemini.md`
> 5. `[[concepts/ux-research/automated-ut-setup]]` ??referenced in `concepts/athena-mcp.md`, `sources/bucketplace-2026-05-06-ai-for-designers.md`
> 6. `[[concepts/ux-research/ax-ai-experience]]` ??referenced in `sources/pxd-story-ai-insights.md`
> 7. `[[concepts/infrastructure-dev/claudemd-context]]` ??referenced in `concepts/10-person-unicorn.md` (multiple times)
> 8. `[[concepts/product-management/contribution-margin-operations]]` ??referenced in `sources/bucketplace-2026-05-08-financial-data-lake.md`
> 9. `[[concepts/corporate-jargon]]` ??referenced in `concepts/contextual-translation.md`
> 10. `[[concepts/infrastructure-dev/figma-make]]` ??referenced in `sources/bucketplace-2026-05-06-ai-for-designers.md`
> 11. `[[concepts/product-management/finance-da]]` ??referenced in `concepts/nexus-data-lake.md`, `sources/bucketplace-2026-05-08-financial-data-lake.md`
> 12. `[[concepts/frontier-safety-framework]]` ??referenced in `concepts/gemini-3-5.md`, `sources/gemini-3-5-launch.md`
> 13. `[[concepts/ai-agents/gemini-spark]]` ??referenced in `concepts/gemini-3-5.md`, `sources/google-io-2026-agentic-gemini.md`
> 14. `[[concepts/ux-research/generative-ui]]` ??referenced in `sources/google-io-2026-agentic-gemini.md`
> 15. `[[concepts/infrastructure-dev/scaffold-design-system]]` ??referenced in `sources/pxd-story-ai-insights.md`
> 16. `[[concepts/product-management/stakeholder-management]]` ??referenced in `concepts/senior-ux-researcher.md`, `sources/measuringu-senior-uxr-years.md`
> 17. `[[concepts/infrastructure-dev/token-efficiency]]` ??referenced in `concepts/tokenomics.md`
> 18. `[[concepts/ux-research/ux-career-progression]]` ??referenced in `concepts/senior-ux-researcher.md`, `sources/measuringu-senior-uxr-years.md`

**Recommended action:** Use the `concept.md` template to create stub pages for any of these you want to expand. Low-priority ones (e.g. `corporate-jargon`, `antigravity`) can remain as stubs.

---

## ? Warning: Orphan Concept Pages (11 pages)

The following concept pages exist but are **not linked from any other wiki page**. They were likely created during an ingest but not added to `wiki/index.md` or any map:

> [!warning] Unlinked Concepts (UX Research cluster ??likely from a batch ingest)
> 1. `concepts/behavioral-sequence-analysis.md`
> 2. `concepts/five-planes-of-ux.md`
> 3. `concepts/goal-directed-design.md`
> 4. `concepts/heart-framework.md`
> 5. `concepts/maxdiff-prioritization.md`
> 6. `concepts/physiological-ux-research.md`
> 7. `concepts/quant-uxr-role-identity.md`
> 8. `concepts/self-reported-ux-metrics.md`
> 9. `concepts/senior-uxr-career-paths.md`
> 10. `concepts/ux-performance-benchmarking.md`
> 11. `concepts/ux-research-matrix.md`

**Recommended action:** Add these to `wiki/index.md` under the "AI UX Research Methods" cluster, and link them from `wiki/maps/ai-ux-research-methods.md`. They are all thematically coherent ??this looks like a complete UX metrics / research methods cluster that just never got wired into the index.

---

## ? New This Session: Open Questions Synthesis

- **96 open questions** found across 93 concept pages
- **72 answered** using existing wiki evidence ??saved to `wiki/queries/2026-05-27-*.md`
- **24 left open** (require external sources, personal portfolio, or live data not in the wiki)
- All concept pages updated with `[Answered ??[[queries/...]]]` backlinks

---

## ??儭?Recommended Next Actions (Priority Order)

1. **Wire orphan UX concepts into index and maps** ??11 pages, all thematically grouped, likely 10 minutes of work.
2. **Create stub pages for high-value broken links** ??Priority: `claudemd-context`, `figma-make`, `generative-ui`, `token-efficiency`, `agentic-engineering`.
3. **Review 72 new query pages** ??Browse `wiki/queries/` in Obsidian. Promote strong answers into the relevant concept pages as permanent claims.
4. **Run next ingest for unprocessed `raw/` files** ??check `raw/2026-05-27-*.md` to confirm all were processed.

