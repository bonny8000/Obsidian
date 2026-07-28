---
type: source
status: active
created: 2026-07-28
updated: 2026-07-28
tags: [agentic-engineering, ai-agent, deterministic-workflows, human-in-the-loop, guardrails, authorization, case-study, hackathon, design-system, ax, finance]
source_path: raw/web/naver-d2-ai-hackathon-nstake-2026-07-28.md
source_url: https://d2.naver.com/helloworld/4821538
authors: [장동원, 유석모, 서정은, 남궁은경]
sources: []
ingest_level: deep
coverage: full
llm_ready: true
raw_preserved: true
confidence: 0.87
---

# NAVER D2 (2026): What the Winning AI Hackathon Team Did *Not* Delegate to AI

## Citation

장동원, 유석모, 서정은 & 남궁은경, 「[AI 해커톤 후기] AI 해커톤 1위 팀이 AI에게 맡기지 않은 것」 *(What the 1st-place AI hackathon team did not delegate to AI)*, **NAVER D2 — Hello World**, 2026-07-24.

**Source type:** First-party engineering retrospective from a cross-functional team (NAVER Cloud IT Service, 네이버앱 서비스, Creative&Experience, 콘텐츠 서비스), written after winning an internal hackathon.
**Raw capture:** [[raw/web/naver-d2-ai-hackathon-nstake-2026-07-28|naver-d2-ai-hackathon-nstake-2026-07-28]]
**Coverage note:** `coverage: full` — the complete Korean article text was retrieved via the D2 content API and read end-to-end, including all tables and the incident section. Nothing was skimmed.

## Summary

Four people, six hours, one internal finance problem: replace 17 staff members' separate Excel files for equity/shareholding management with an LLM + MCP platform (**NStake**). It won every evaluation round. The article is valuable not for the win but because it is organized around the **inverse** question — the team documents, with specifics, each place they took work *away* from the model, and why.

The three decisive moves: (1) they reframed the problem from "replace Excel" to "explain how each number was produced"; (2) they **removed AI from computing official numbers** after the generated monthly report proved non-reproducible; (3) they placed guardrails at the **authorization boundary before the model**, not as a filter on its output. A destructive-code incident during the event supplies the strongest evidence for (3).

## Key Claims

- **The problem was explainability, not storage.** Consolidating values into a database makes collection easy but does not make the values trustworthy. A stored "30% ownership" cannot say *why* it is 30% — that requires the ordered transaction history that produced it. Restated problem: *it is hard to explain what transactions produced the current number and on what basis it can be trusted.*
- **Same input must always yield the same result → rules, not models.** Official report classification and totals are not a wording problem. The LLM-generated monthly report was fast and demoed well but produced varying wording on identical data, drifted from company reporting format, and made official report generation dependent on model connectivity. Classification and totals became explicit rules shared by screen and Excel export; **AI was removed from deciding official numbers.**
- **Guardrails begin at the request, not the response.** Letting the AI read everything and mask part of the final answer was judged unsafe. From the start the model receives only the entities the logged-in user may see and only the tools they may run. Data authorization is re-checked **in the DB on every request** — trusting neither the token nor the model's judgment.
- **Privilege and execution control outrank hallucination as a risk.** The worst incident was not a wrong number: reset code written for local test data ran against the **shared development database**. Recovery took **over 20 minutes** of a 6-hour event, and the same execution repeated until the dangerous code was fully removed.
- **"The feature exists" ≠ "the work gets done."** Functions and files existed and AI reported features complete while they were never wired into the user's flow. Completion was redefined as the user being able to finish login → entity check → transaction entry → save → validate → review mismatch → disposition → state and report update.
- **More documents made AI understanding worse, not better.** As material accumulated, terms and as-of dates mixed and authority became ambiguous. What was needed was **judgment criteria, not volume** — and those criteria cannot be delegated.
- **Workflow completeness beat feature count** in both the LLM's evaluation and the humans'. The authors attribute the result to all features sharing one flow (입력 → 검증 → 판단 → 처리 → 결과 생성), not to any single AI capability.

## Useful Examples

**The delegation table** (the most directly reusable artifact in the source):

| Work characteristic | Applied approach |
|---|---|
| Same input must always give the same result | Explicit rules and code |
| Officially computing amounts, quantities, ratios | Deterministic calculation |
| Used directly for financial/legal judgment | Rule-based processing + human approval |
| Multiple phrasings acceptable | Generative AI |
| User can re-review the result | AI-assisted draft generation |
| Narrowing what to check matters more than being right | AI or statistical model |

**The Rule / Statistical / eXternal validation split:**

| Class | Meaning |
|---|---|
| **Rule** | Decidable by explicit rule — ownership totals, missing exchange rate, transaction after liquidation |
| **Statistical** | Narrows what a human looks at first without asserting error — unusual amounts, abrupt share-count changes |
| **eXternal** | Internal vs. external-disclosure difference where the system must *not* decide; a human confirms |

**The six authorization boundaries:** short-lived AI/MCP token after SSO carrying minimal identity · per-request DB re-check of role and entity scope · separate policies for read / LLM-query / write / admin · explicit user confirmation before state changes · sensitive-data masking, input length limits, no credentials in logs · append-only audit log.

**The post-incident principles:** no admin privileges by default for AI tooling · clearly separate local/dev/prod · re-confirm target environment before deletion or large change · explicit approval for destructive operations · confirm backup and recoverability before feature development · **verify AI-generated code by actual execution results, not by its explanation.**

**The design reversal.** One hour in, three developers had generated the whole UI around a cute steak character in browns and beiges, loading screen included. For a finance team whose Excel used cell color as *meaning* (yellow, gray, pale blue = information state and purpose, not decoration), the need was familiarity, trust, formality, professionalism. They switched to the NAVER design system — neutral base, NAVER green accent, calm ERP style. With principles in `design.md` AI produced tone and drafts fast, but reaching the target level took repeated correction, some assets had to be redrawn, and **design became the development bottleneck** while the team waited on PNGs.

**Process inversion:** plan → design → dev → QA was effectively reversed. Each discipline pre-planned its own area, and because AI produced prototypes instantly, implementing first and fixing together beat waiting for a finished spec. **Pair prompting** — two dev environments per team, multiple people writing prompts and reviewing output together — replaced one person accepting AI output alone.

**AI as evaluator, not just generator.** Four roles: evaluator (structuring problem and success criteria), design partner (comparing options), implementation assistant, verifier (finding doc↔code mismatches). Per-feature loop: short design doc → implement → collect test evidence (screenshots, logs) → reflect into deck and README → re-verify docs against actual execution. Recurring checks became a checklist: is the feature described in the presentation actually in the code? is there security-risky behavior? is a partial implementation being described as complete?

## Constraints / Caveats

- **Six-hour hackathon prototype, not production.** The authors are explicit: remaining work includes automated reconciliation with the internal finance ledger, production-grade MCP authentication, dev/prod separation, transaction guarantees, audit-log retention and monitoring, and automated tests.
- **The win is weak evidence for the method.** The authors themselves note score gaps among top teams were small, so no single feature or document decided it. Treat the ranking as corroborating, not proving, the workflow-completeness thesis.
- **Domain is unusually rule-friendly.** Equity arithmetic has genuinely deterministic answers. The "move official numbers to rules" prescription is strongest where a correct answer exists and weakest for judgment-heavy domains.
- **One organization, one team, one event.** No baseline, no control, no measurement beyond the evaluation ranking.
- **The 20-minute incident is self-reported** and its root cause is stated as multi-factor (excess tooling privilege, insufficient environment separation, no pre-deletion check) — usefully honest, but not independently examined.
- **Design-system adoption is NAVER-specific**; the transferable claim is "use the design language your users already trust," not "use NAVER's."

## Design Implications

- **Write the delegation table before writing features.** Classify each unit of work by whether identical input must give identical output, whether it feeds legal/financial judgment, and whether the user can re-review — then assign rules, deterministic calculation, human approval, or generation accordingly.
- **Separate "error" into decidable / suspicious / human-judgment.** The R/S/X split prevents a system from either over-claiming certainty or dumping an undifferentiated review queue on the user. Statistical signals narrow attention rather than asserting fault.
- **Store the events, derive the state.** Recording the transactions that produce a number, then computing current state, makes divergence between computed and stored state a *check item* instead of a silent error.
- **Scope the agent's context at authorization time.** Provision only the entities and tools the current user may access before the model sees anything. Post-hoc masking of a full-visibility answer is not a boundary.
- **Judge completion by user flow, not artifact existence.** A file, a function, or a model's report of success are all insufficient evidence that anyone's work can be finished.
- **Give AI the success criteria, then use it to check against them.** Defining what success is remains human; repeatedly verifying results against it is delegable.
- **Prototype speed is not prototype judgment.** Fast generated UI must still be re-judged against the users' existing information conventions.

## Tensions

- **Reinforces [[wiki/sources/socar-self-healing-agents|SOCAR's]] "constrain, don't liberate" position** with an independent case in a different domain — one of the gaps the [[wiki/analyses/2026-07-24-directing-agents-in-production|2026-07-24 memo]] explicitly asked to fill. Note the evidence grade is lower (hackathon, not two months of production).
- **Against [[wiki/sources/ai-as-senior-hire-not-intern|"AI as a senior hire"]]:** here the team explicitly *removed* the model from the highest-stakes decision. Consistent with the two-axis reading — reasoning latitude retained (understanding unfamiliar finance domain, explaining discrepancies), action bounds tightened (no authority over official numbers).
- **Against "give the agent more context."** This source directly contradicts the naive version: more documents degraded understanding by mixing terms, as-of dates, and authority. Aligns with [[wiki/concepts/ai-agents/context-rot|Context Rot]] and against document-dumping.
- **Prompt-level safety vs. structural safety.** The source rejects "write *don't show unauthorized data* in the prompt" as a safety policy. This is the same claim as SOCAR's "hallucination is a code problem," extended from output validation to *access provisioning*.
- **Speed vs. trust in design.** AI made prototypes instant, and instant prototypes were wrong for the audience. The bottleneck moved to design refinement — an inversion of the usual assumption that AI relieves design load.

## Open Questions

- Would the "official numbers by rule" boundary hold in a domain where no deterministic correct answer exists?
- The team hit a destructive-execution incident in six hours with four experienced engineers. What is the base rate of this class of incident in normal agentic development, and what tooling catches it?
- Does pair prompting measurably improve output quality, or did it mainly distribute review load?
- At what point does the "judgment criteria over document volume" rule become formalizable — i.e. is the criteria set itself a maintainable artifact, or does it drift like the documents it replaces?

## Concepts Linked from This Source

- [[wiki/concepts/ai-agents/permission-boundary-guardrails|Permission-Boundary Guardrails]]
- [[wiki/concepts/ai-agents/rule-statistical-external-validation|Rule / Statistical / External Validation]]
- [[wiki/concepts/ai-agents/workflow-completeness|Workflow Completeness]]
- [[wiki/concepts/infrastructure-dev/deterministic-ai-workflows|Deterministic AI Workflows]]
- [[wiki/concepts/ai-agents/zero-trust-agent-development|Zero-Trust Agent Development]]
- [[wiki/concepts/infrastructure-dev/agent-defense-in-depth|Agent Defense in Depth]]
- [[wiki/concepts/ai-agents/approval-gate|Approval Gate]]
- [[wiki/concepts/ai-agents/context-rot|Context Rot]]
- [[wiki/concepts/product-management/role-convergence|Role Convergence]]

## LLM Use

The **best single source in this wiki for the question "what should AI *not* do?"** Cite it for: the delegation table, the R/S/X validation split, authorization-boundary guardrails, and the "feature exists vs. work gets done" completion test. Pair it with [[wiki/sources/socar-self-healing-agents|SOCAR self-healing agents]] when arguing for constraint — the two are independent cases from different domains reaching the same conclusion. Prefer SOCAR when production-grade numbers are needed; prefer this one when the argument is about *where the boundary goes*.

Use with care for anything about measured outcomes — the hackathon ranking is not an efficacy measurement.

## Reliability Notes

- **First-party retrospective, read in full**, with unusually honest failure reporting (a self-inflicted shared-DB wipe, design becoming a bottleneck, an initial approach they abandoned). Self-critical detail of this kind raises credibility.
- **Confidence 0.87** rather than higher: the design *reasoning* is well evidenced and internally consistent, but there is no measurement — six hours, one team, one problem, and a ranking the authors themselves discount.
- Multi-author across four different NAVER organizations, which reduces single-perspective risk.
- Figures (17 staff, 20 minutes, 1st in 4 of 5 re-runs) are self-reported. Re-verify against the original before external citation.
