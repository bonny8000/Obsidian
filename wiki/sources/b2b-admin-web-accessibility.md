---
type: source
status: active
created: 2026-07-28
updated: 2026-07-28
tags: [accessibility, wcag, b2b-admin, front-end, ai-assisted-audit, verification, claudemd, case-study]
source_path: raw/web/ramirami-b2b-admin-web-accessibility-2026-07-28.md
source_url: https://ramirami.tistory.com/m/234
authors: [rami_]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.76
---

# rami_ (2026): Applying Web Accessibility to a B2B Admin Service

## Citation

rami_, 「B2B 어드민 서비스에 웹 접근성 적용하기」 *(Applying web accessibility to B2B admin services)*, **Tech Epilogue** (Tistory), 2026-07-27.

**Source type:** First-party front-end engineering work log with concrete before/after counts.
**Raw capture:** [[raw/web/ramirami-b2b-admin-web-accessibility-2026-07-28|ramirami-b2b-admin-web-accessibility-2026-07-28]]

## Summary

Two things make this small post worth a source page. First, an under-argued case: **accessibility pays back better in B2B admin tools than in consumer commerce**, because the same operators repeat the same tasks daily, so each interaction improvement compounds instead of amortizing across one-time visitors.

Second — and more transferable — a clean instance of **AI-assisted audit producing badly wrong counts**. An automated scan reported 168 missing `alt` attributes and 166 missing `th` tags. Manual verification found **6 and 141**. The cause was mundane: line-based grep against multi-line attribute formatting. That is a 28× overcount on one metric, discovered only by opening the files.

## Key Claims

- **WCAG's POUR principles** — Perceivable, Operable, Understandable, Robust — benefit all users, not only users with disabilities.
- **Repetition changes the accessibility business case.** Table-heavy interfaces used daily by the same operators make keyboard operability and labeling a throughput improvement, not just a compliance item. Icon-only buttons without labels force repeated mouse navigation; screen readers cannot distinguish data types without header associations.
- **Automated scan results must be verified by opening the files.** Line-based searches over multi-line markup produce large false-positive counts.
- **Accessibility rules belong in agent-facing team documentation** (`CLAUDE.md`) to prevent regression, rather than in a checklist a person is expected to remember.
- **Implementation order used:** keyboard operability → form labels → icon labels.
- **Partial assurance is honest assurance.** Pre-commit ESLint and a zero-missing-`alt` audit are described as giving only partial coverage.

## Useful Examples

| Automated scan reported | Actual after manual verification |
|---|---|
| 168 missing `alt` attributes | **6** |
| 166 missing `th` tags | **141** |

- **One-line high-value fix:** `<html lang>` changed from `en` to `ko` on a Korean-language service — trivially small, and it changes screen-reader pronunciation for the entire application.
- **`aria-label` on icon-only buttons** — download, delete, refresh.
- **`scope="col"` on table headers** so data cells are structurally associated, which is what makes a data table navigable rather than a grid of unlabeled values.
- **Decorative vs. meaningful images:** `alt=""` for decorative; i18n-managed alt text for meaningful — reusing existing localization keys before creating new ones.

## Constraints / Caveats

- **Single codebase, single team, no measurement of the claimed benefit.** The "compounding daily speed" argument is plausible and well-reasoned but not measured — no task-time study, no operator feedback data.
- **The grep discrepancy is formatting-specific.** The author says so directly: the gap arose from this codebase's multi-line attribute style. The *lesson* generalizes; the ratio does not.
- **Initial implementation, not comprehensive coverage.** Keyboard, labels, and table semantics were addressed; contrast, focus management, live regions, and error handling are not discussed.
- **No screen-reader testing reported** with actual assistive-technology users — the changes are structurally correct but their experienced effect is unverified.
- **`th` count went from 166 to 141**, i.e. most of that finding was real. Only the `alt` finding was a dramatic overcount, so this is one bad metric, not a wholesale indictment of automated scanning.
- Ingested from an AI-generated extraction, not a verbatim read.

## Design Implications

- **Prioritize accessibility work by repetition, not by traffic.** An internal tool with 20 daily operators can justify more interaction investment per user than a page with 20,000 monthly visitors.
- **Verify every automated audit count against source files before reporting it.** A count is a claim; grep over structured markup is not a reliable instrument for it.
- **Prefer AST- or parser-based scanning over line-based search** for anything markup-structural. This is the same lesson [[wiki/sources/socar-parking-brain-knowledge-graph|SOCAR]] applied by choosing AST analysis for code extraction.
- **Put accessibility constraints in the agent context file**, so generated code is accessible by default rather than corrected downstream. Aligns with [[wiki/concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]]'s position that accessibility belongs in the context layer, not in QA.
- **Fix `lang` first.** Highest ratio of effect to effort in the whole post.
- **State coverage honestly.** "Pre-commit lint gives partial assurance" is the correct way to report an accessibility posture; "we have zero missing alt attributes" is not.

## Tensions

- **Sits inside the 2026-07-28 cluster's central theme from an unexpected angle.** SOCAR, NStake, and Polar all argue that AI output must be structurally constrained and independently validated. This source shows the same principle applied to **AI-assisted measurement**: the audit itself needed independent verification. The failure was not a hallucination — it was a badly chosen tool trusted without checking.
- **Against "automate the accessibility audit" as a complete answer.** Automated scanning found real issues *and* a 28× overcount on the same run. Both facts are needed.
- **With [[wiki/sources/veronikapj-whats-new-android-2026|Android 2026]]:** that source notes an accessibility semantic audit is what makes agent-driven **Computer Control** work — accessibility semantics become the interface agents navigate. Two independent 2026 sources point at accessibility metadata acquiring a second consumer.
- **Weak-evidence caution:** the B2B-payback argument is the post's most interesting claim and its least supported one. Use it as a hypothesis worth testing, not a finding.

## Open Questions

- Does accessibility work in high-repetition internal tools produce measurable task-time improvement? A natural, small, and genuinely useful UX research study — and this wiki has no evidence for it.
- What is the reliable false-positive rate for line-based versus AST-based accessibility scanning?
- Do accessibility rules in `CLAUDE.md` actually prevent regression in generated code, and how would you measure that?
- Which accessibility constraints are best expressed as lint rules (structural) versus context-file guidance (judgment)?

## Concepts Linked from This Source

- [[wiki/concepts/ux-research/web-accessibility-pour|Web Accessibility (POUR)]]
- [[wiki/concepts/infrastructure-dev/claudemd-context|CLAUDE.md / AGENTS.md Context]]
- [[wiki/concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]]
- [[wiki/concepts/infrastructure-dev/knowledge-linting|Knowledge Linting]]
- [[wiki/concepts/ai-agents/workflow-completeness|Workflow Completeness]]

## LLM Use

Cite for two things: **the B2B-admin accessibility payback argument** (as a hypothesis), and **the grep-versus-reality verification lesson** (as a concrete cautionary example with numbers). The second is the more valuable and more general — it is the cleanest small example in this wiki of an AI-assisted measurement that was confidently wrong in a way only file-level inspection caught.

Also usable as a starter checklist for a B2B admin accessibility pass: `lang`, keyboard operability, form labels, icon `aria-label`, `scope="col"`, decorative-vs-meaningful `alt`.

## Reliability Notes

- **First-party work log with self-correcting detail** — the author reports their own tooling's overcount, which is the mark of a trustworthy work log.
- **Confidence 0.76:** the implementation facts are verifiable and specific; the headline business argument is unmeasured, the scope is one codebase, and no assistive-technology user testing is reported.
- Small blog, single author, no independent corroboration of the B2B payback claim in this wiki.
- Ingested from an AI-generated extraction; the 168/6 and 166/141 figures should be re-verified against the original before external citation.
