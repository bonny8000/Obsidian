---
type: concept
status: active
created: 2026-06-17
updated: 2026-06-17
tags: [ux-research, surveys, banner-table, cross-tabulation, segmentation, market-research, reporting, deliverable]
sources:
  - sources/measuringu-banner-tables
confidence: 0.88
---

# Banner Table

> [!abstract] Summary
> A wide tabular survey deliverable with **metrics in rows (the *stub*)** and **demographic / behavioral segments in columns (the *banner*)**. Compresses many cross-tabulations into a single scannable view; the standard market-research format for segmented survey results. Terminology traces to the 1949 U.S. Census Bureau *Manual of Tabular Presentation*. Underused in UX research, but earns its keep on large surveys where segmentation is decision-relevant.

> [!important] Why it Matters
> Single-number survey summaries hide segment-level signal. Banner tables surface differences across age, gender, income, behavior, and locale at a glance — exactly the cuts that drive product decisions for global or segmented audiences. They also encourage stakeholders to ask better questions ("why is LinkedIn 94% reluctant on political content?") instead of arguing about the headline number.

## 📝 Key Claims

- A banner table = **stub (rows = metrics)** + **banner (columns = segments)**. Each cell is a metric value for a metric × segment combination.
- The format was standardized in 20th-century survey practice and is the **default market-research deliverable** for segmented surveys.
- **Weighted and unweighted columns should appear side by side.** Market research treats weighted as official; unweighted is kept for QC and transparency.
- Underused in UX research, but valuable when:
  - Sample sizes support multiple data splits.
  - Multiple demographic / behavioral segments are decision-relevant.
  - Stakeholders need a standardized, repeatable side-by-side format.
- **Best practices (with rationale):**
  1. **Freeze panes** — top row + left columns lock during horizontal scrolling.
  2. **Include both unweighted *n* and weighted *n*** — without them, cells lie.
  3. **Visual separation between banner groups** — empty columns with light fill help readers parse structure.
  4. **Define metric direction** — make explicit whether a larger % is positive (top-box) or negative (bottom-box).
- **R toolkit:** `openxlsx` (Excel I/O), `dplyr` (frame manipulation), `tidyr` (tidy data). Deterministic, repeatable — a strong [[concepts/ai-agents/agent-skills|Agent Skill]] candidate.

## Use When

- Large-scale segmentation surveys (n typically in the hundreds or thousands).
- Multiple demographic / behavioral cuts are stakeholder priorities.
- A repeatable, standardized deliverable is expected (e.g. tracking studies).
- Side-by-side metric comparison across segments adds decision value.

## Avoid When

- Small-sample surveys where splits produce unreliable cell-level estimates.
- Qualitative or small-scale studies — the format adds friction without payoff.
- A chart or visualization would communicate the finding faster.
- A single-metric deliverable is enough.

## 🔗 Related Concepts

- [[concepts/ux-research/standardized-usability-questionnaires|Standardized Usability Questionnaires]]
- [[concepts/ux-research/self-reported-ux-metrics|Self-Reported UX Metrics]]
- [[concepts/ux-research/participant-selection-criteria|Participant Selection Criteria]]
- [[concepts/ux-research/quant-uxr-rigor|Quant UXR Rigor]]
- [[concepts/ux-research/survey-data-quality-screening|Survey Data Quality Screening]] — screened data feeds the banner table.
- [[concepts/ai-agents/agent-skills|Agent Skills]] — banner-table generation is deterministic, repeatable Skill territory.

## ⚖️ Conflicts & Caveats

> [!warning] Per-cell sample size
> A banner with 6 platforms × 6 age bins × 6 income bins quickly produces cells with very small *n*. The article doesn't enforce a minimum; treat weighted *n* < 30 in a cell as a flag.

> [!warning] Comprehensiveness vs noise
> A banner with 20 segments shows everything *and* hides the signal in clutter. Curate segment selection to the decisions at hand.

## 📚 Sources

- [[sources/measuringu-banner-tables|MeasuringU: How to Use Banner Tables to Present Survey Results]] (Lewis & Sauro, 2026) — primary source.

## ❓ Open Questions

- For Bonny's vault: should every large-survey ingest also produce a banner-table export by default?
- What is the right per-cell minimum *n* before a banner cell should be reported (vs masked)?
- Is there a clean agentic / AI workflow that consumes a banner table and surfaces the 3 most decision-relevant segments? (Skill candidate.)
- How should AI moderators interpret banner-table results when generating follow-up qualitative interview guides?
