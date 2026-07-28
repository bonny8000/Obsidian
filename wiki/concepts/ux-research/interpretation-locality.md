---
type: concept
status: active
created: 2026-07-28
updated: 2026-07-28
tags: [concept, ux-research, org-design, insights-function, shared-state, role-convergence, synthesis]
sources: [uxr-market-research-data-science-reorg]
confidence: 0.68
---

# Interpretation Locality

> [!abstract] Summary
> The condition where each research function analyzes **its own data stream through its own interpretive frame**, so conclusions stay siloed no matter what the org chart says. Papas's diagnosis of why the "insights department" consolidations of the 2010s failed: they merged reporting lines and left interpretation local, which changed who people reported to and nothing about how evidence combined.

> [!important] Why it Matters
> It relocates the problem from **structure** to **epistemics**, which makes it actionable at any scale. A reorg is not a merger if interpretation stays local. And the same failure occurs inside a single practitioner who holds qualitative findings, survey results, and analytics in three separate mental files with three different standards of proof — no reorg available, same incoherence.

## 📝 Key Claims

- **The divisions are accidental, not designed.** UXR, market research, and user-facing data science grew from different lineages — usability/HCI, marketing, instrumentation/engineering — and calcified around distinct data streams and reporting lines. *"Nobody ever decided that understanding customers should be split three ways. It accreted, hire by hire."*
- **Reporting-line mergers do not dissolve interpretation locality.** The 2010s insights departments are the control case: consolidation without shared interpretation produced no synthesis.
- **Shared state is the proposed dissolvent** — a unified, **dated, confidence-weighted** knowledge base about users. Once evidence carries provenance and confidence in one place, separate interpretation gates become incoherent.
- **Plural collection, singular assessment** is the target shape, modeled on intelligence-community practice: distinct collection disciplines feeding one assessment process.
- **Tooling friction was the fence.** *"The fence was mostly tooling friction, and the friction is exactly what the models dissolved."* AI lowered the technical barrier that kept practitioners inside one discipline.
- **Two outcomes look identical in the announcement.** Cost-driven consolidation orphans interpretation responsibility to whatever tool is nearest; capability-driven consolidation keeps collection crafts plural while unifying assessment. They "look identical in the announcement and nothing alike three years later."

## The diagnostic test

For any insights function, merged or not:

1. **Does evidence from different methods carry comparable provenance?** Date, source, confidence, scope.
2. **Is there one place where conflicting signals are reconciled**, or does each stream reach its own conclusion?
3. **Does anyone own interpretation**, by name — or does it default to whichever tool produced the last chart?
4. **Can a claim be traced to its evidence** across method boundaries?

Failing 1–2 means interpretation is still local regardless of reporting structure. Failing 3 is Papas's cost-driven failure mode in progress.

## This vault as an instance

Worth naming, since it is the closest available test of the shared-state claim: this wiki implements much of what Papas describes as the dissolvent — `confidence:` fields, `updated:` dates, `sourceRef`-style provenance to `raw/`, explicit conflict recording rather than silent merging, and one interpretation layer (`wiki/analyses/`) across method families. The mechanism is at least constructible. Whether it changes organizational behavior is a separate and untested question.

## ⚖️ Conflicts & Caveats

> [!warning] Diagnostic content is much stronger than the predictive content
> The anchor source attaches this diagnosis to a **three-year prediction** that UXR, market research, and data science merge into one discipline. That prediction has no stated derivation — no adoption curve, survey, or case. Interpretation locality stands on its own reasoning; the timeline does not. Use the former, discard the latter.

> [!warning] The mechanism is deferred
> How shared state is actually built and maintained — schema, confidence model, update cadence, conflict resolution — is promised in a later installment and not in the source. Until it publishes, the essay asserts a cause it does not describe.

> [!warning] Direct conflict with the role-split thesis
> [[wiki/concepts/ux-research/uxr-role-split|Newton's UXR Role Split]] argues research is **splitting** into three roles as production cost collapses; Papas argues three disciplines are **merging** for the same underlying reason. Both cite AI-driven cost collapse; they predict opposite structural outcomes. **Neither is settled.** A reconciliation neither author proposes: splitting *within* a unified insights function — roles diverging while disciplines converge.

> [!warning] Selection effect in the diagnosis
> Failed insights-department mergers are recalled; successful ones, if any exist, are not examined. The diagnosis may be correct and still be built on a biased sample.

> [!warning] Unaddressed headcount question
> If interpretation becomes the scarce skill, does the merged function need as many people? Neither this source nor [[wiki/sources/when-research-gets-faster|Venkat]] addresses it, and it is the question a practitioner actually cares about.

## 🔗 Related Concepts

- [[wiki/concepts/ux-research/uxr-role-split|UXR Role Split]] — the directly conflicting thesis.
- [[wiki/concepts/product-management/role-convergence|Role Convergence]] — the same AI-lowers-barriers argument applied to product roles; this concept supplies better vocabulary for its failure mode.
- [[wiki/concepts/ux-research/quant-uxr-role-identity|Quant UXR Role Identity]]
- [[wiki/concepts/ux-research/democratization-of-insights|Democratization of Insights]] — what happens when interpretation is distributed rather than unified.
- [[wiki/concepts/ux-research/research-operations|Research Operations]] — where shared-state infrastructure would live.
- [[wiki/concepts/product-management/research-influence|Research Influence]]
- [[wiki/concepts/product-management/insight-to-execution-gap|Insight to Execution Gap]] — the downstream sibling: interpretation unified but still not acted on.
- [[wiki/concepts/infrastructure-dev/domain-knowledge-graph|Domain Knowledge Graph]] — the engineering-side instance of dated, provenance-carrying shared state.
- [[wiki/concepts/infrastructure-dev/llm-wiki|LLM Wiki]] — the mechanism this vault implements.
- [[wiki/concepts/ux-research/senior-uxr-career-paths|Senior UXR Career Paths]]

## 📚 Sources

- [[wiki/sources/uxr-market-research-data-science-reorg|Papas (2026): UXR, Market Research, and Data Science Walk Into a Reorg]] — sole source: locality of interpretation, the shared-state mechanism, the two-outcomes distinction. Opinion essay, no data; part 2 of a series.

## ❓ Open Questions

- What does shared state concretely require — schema, confidence model, update cadence, conflict resolution? Deferred to the source's part 3.
- Has any organization actually unified interpretation across UXR / MR / DS, and what happened to craft quality?
- Are role split and role merger both occurring — roles splitting *inside* a unified function?
- What observable would falsify the merger thesis?
- Does a shared-state knowledge base change decisions, or only make disagreement more visible?
