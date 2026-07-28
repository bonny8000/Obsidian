---
type: comparison
status: active
created: 2026-07-28
updated: 2026-07-28
tags: [ai-agent, delegation, deterministic-workflows, guardrails, reliability, decision-table, agentic-engineering]
sources:
  - sources/naver-d2-ai-hackathon-nstake
  - sources/socar-self-healing-agents
  - sources/socar-parking-brain-knowledge-graph
  - sources/polar-orbit-llm-safe-design-system
  - sources/b2b-admin-web-accessibility
  - sources/spec-driven-development-exit-strategy
confidence: 0.82
---

# Comparison: Delegate to a Model vs. Determinize in Code

## Decision Question

For a given unit of work, do I hand it to a **model**, express it as an **explicit rule or type**, or route it to a **human** — and what evidence supports each placement?

This table answers the open item the [[wiki/analyses/2026-07-24-directing-agents-in-production|2026-07-24 memo]] deferred: *when to constrain vs. when to delegate.* Three sources landed on 2026-07-28 that make it answerable.

## Criteria

- **Reproducibility requirement** — must identical input produce identical output?
- **Consequence of being wrong** — recoverable, expensive, or externally binding?
- **Verifiability** — can the output be checked independently, and by what?
- **Who is accountable** for the result.
- **Evidence grade** behind the placement.

## Matrix

| Work characteristic | Placement | Mechanism | Evidence |
|---|---|---|---|
| **Identical input must give identical output** | Explicit rules and code | Rule engine; no model in the path | NStake removed the LLM from monthly-report generation after identical data produced varying wording and format drift **(prototype, reasoned)** |
| **Officially computing amounts, quantities, ratios** | Deterministic calculation | Shared calculation used by every surface (screen and export) | NStake: classification into investment / disposal / change and all totals became explicit rules **(prototype)** |
| **Feeds financial or legal judgment** | Rule-based processing **+ human approval** | Approval gate before commit | NStake **(prototype)**; SOCAR Draft-PRs-only **(2 months production, real metrics)** |
| **Output must conform to a fixed vocabulary** | Types + lint + CI gate | Make violations uncompilable; CI as contract | Polar Orbit: typed tokens, banned raw HTML layout, `light-dark()` in-token **(qualitative, no measurement)** |
| **Irreversible action** (send / write / deploy / delete) | Human approval, gated on **reversibility not confidence** | Explicit confirmation at the tool boundary | Convergent across SOCAR, OpenWorker, NStake **(independent arrival from unrelated motives)** |
| **Access to data and tools** | Authorization layer **before** the model | Provision only the current user's scope; re-check per request | NStake's six boundaries; SOCAR credential isolation via closure **(prototype + production)** |
| **Stable organizational facts** (what exists, what a term means) | Retrieval from a derived, provenance-carrying store | Knowledge graph with `sourceRef` + recency warnings, queried before implementing | SOCAR parking-brain: ~100 seeds + ~17k derived nodes, hourly **(architecture, no outcome metric)** |
| **Narrowing where a human should look** | AI or statistical model | Signals that rank attention and assert nothing | NStake's **Statistical** validation class **(prototype)** |
| **Multiple phrasings acceptable** | Generative AI | Direct generation | NStake **(prototype)** |
| **User will re-review the result anyway** | AI-assisted draft | Generate a draft, human edits | NStake; NN/g's planning-stage endorsements **(practitioner authority)** |
| **Explaining a complex finding legibly** | Generative AI | Natural-language explanation over deterministic results | NStake kept AI for explaining discrepancies **(prototype)** |
| **Unfamiliar domain, need to understand fast** | Generative AI, with human judgment retained | Model as evaluator / design partner | NStake's four AI roles **(prototype)** |
| **Judging what counts as success** | Human, always | Criteria authored by people, then AI checks against them | NStake: *"the standards for the work must be set by people"* **(reasoned)** |
| **Measuring or counting something structural** | Parser / AST — **not** line-based search or model estimate | Verify counts by opening the artifacts | rami_: automated scan said 168 missing `alt`, actual **6** **(single concrete case)** |
| **Behavioral observation** (what a user did, not said) | Human | Direct observation | NN/g: no AI tool can properly watch a usability test **(practitioner authority, time-stamped)** |

## Recommendation Pattern

**1. Ask the reproducibility question first.** *Must identical input produce identical output?* If yes, the work leaves the model — no further analysis needed. This is the single sharpest test in the table, and it is the one NStake used to remove AI from official report generation.

**2. Then ask about consequence, not confidence.** Every source that names a gating rule gates on **reversibility**. Model confidence appears nowhere as a legitimate gate criterion in any source in this wiki.

**3. Then ask what checks the output.** Three answers, in descending strength:
- **A type or schema** — the violation cannot be expressed (Polar).
- **An independent validator** — computed state compared against stored state (NStake), or observation compared against a baseline schema (SOCAR).
- **A human reading it** — weakest, and subject to fatigue.

If the answer is "the model says it's fine," there is no check. *Verify AI-generated code by execution results, not by its explanation.*

**4. Provision access before generating, not after.** Scoping context at authorization time is a boundary; masking a full-visibility answer is not.

**5. Delegate freely where being wrong is cheap and visible.** Drafts, explanations, attention-ranking, and exploration of unfamiliar domains are the well-evidenced delegable band — because the human is already in the loop by construction.

## Where the table is weakest

- **Most cells rest on one six-hour prototype.** NStake carries a disproportionate share. It is corroborated in direction by SOCAR's production case, but the specific placements are reasoned, not measured.
- **No source measures the counterfactual.** Nobody built the same system both ways. Every "determinize this" placement is a design judgment supported by an observed failure, not by a comparison.
- **The rule-friendly-domain bias is real.** Equity arithmetic, design tokens, and integration repair all have checkable right answers. The table says little about judgment-heavy work where no deterministic answer exists — which is where the delegation question is actually hardest.
- **Constraint costs are named nowhere in this table.** Every determinize placement carries maintenance: rule authoring (NStake), baseline schemas (SOCAR), weekly token additions (Polar), seed curation (parking-brain). The break-even volume is unstated in all four sources.
- **Approval-gate fatigue remains unaddressed.** The table routes a great deal to human approval and no source tests what happens when gates fire constantly.

## Source Evidence

| Source | Grade | Contribution |
|---|---|---|
| [[wiki/sources/socar-self-healing-agents\|SOCAR: self-healing agents]] | **Production, 2 months, metrics (0.88)** | Reversibility gating; structural over instructed safeguards; Draft-PRs-only |
| [[wiki/sources/naver-d2-ai-hackathon-nstake\|NAVER D2: NStake]] | Prototype, richly reasoned (0.87) | The delegation table; R/S/X validation; authorization boundaries; workflow completeness |
| [[wiki/sources/socar-parking-brain-knowledge-graph\|SOCAR: parking-brain]] | Architecture, no metrics (0.83) | Retrieval placement for stable organizational facts; provenance and recency |
| [[wiki/sources/polar-orbit-llm-safe-design-system\|Polar: Orbit]] | Qualitative (0.78) | Type-and-CI foreclosure; constrain acceptance, not the generator |
| [[wiki/sources/nngroup-accelerating-research-with-ai\|NN/g: research with AI]] | Practitioner authority (0.88) | Language-vs-behavior as the delegation predictor in research work |
| [[wiki/sources/b2b-admin-web-accessibility\|rami_: B2B accessibility]] | Single case (0.76) | Measurement instruments need verification too |
| [[wiki/sources/spec-driven-development-exit-strategy\|Eisele: spec exit strategy]] | Argument + one eval (0.80) | Scale process weight to consequence |

## Related

- [[wiki/analyses/2026-07-28-constraining-ai-by-construction|Analysis: Constraining AI by Construction (2026-07-28)]] — the synthesis this table supports.
- [[wiki/analyses/2026-07-24-directing-agents-in-production|Analysis: How Much Latitude Should an Agent Get? (2026-07-24)]] — the memo that requested this table.
- [[wiki/concepts/infrastructure-dev/deterministic-ai-workflows|Deterministic AI Workflows]]
- [[wiki/concepts/ai-agents/rule-statistical-external-validation|Rule / Statistical / eXternal Validation]]
- [[wiki/concepts/ai-agents/permission-boundary-guardrails|Permission-Boundary Guardrails]]
- [[wiki/concepts/infrastructure-dev/llm-safe-design-system|LLM-Safe Design System]]
- [[wiki/concepts/ai-agents/workflow-completeness|Workflow Completeness]]
- [[wiki/concepts/ai-agents/approval-gate|Approval Gate]]
