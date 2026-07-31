---
type: analysis
status: active
created: 2026-07-31
updated: 2026-07-31
tags: [analysis, constraint-by-construction, design-system, guardrails, agentic-engineering, evals, measurement-gap, harness, workflow-placement]
sources:
  - karrot-kraft-design-system-agent
  - pxd-writone-ai-writing-assistant
  - maily-product-makers-guardrails
  - polar-orbit-llm-safe-design-system
  - naver-d2-ai-hackathon-nstake
  - socar-self-healing-agents
confidence: 0.72
---

# Constraint Architectures Converge — and Still Nobody Measures Them

## Research question

Three months ago this vault recorded a principle from a single source: *constrain the acceptance criteria, not the generator.* Since then the constraint cluster has grown to eight sources across five organisations and four problem domains. **Does the convergence hold up, what does it add, and what is it still missing?**

## Evidence base

Six sources carry this memo; three are new in this batch.

| Source | Domain | New? | What it contributes |
|---|---|---|---|
| [[wiki/sources/karrot-kraft-design-system-agent|Karrot: Kraft]] (0.80) | screen generation from a design system | **new** | schema + capability removal + 11 scorers + cross-session memory, in one system; a multi-agent negative result |
| [[wiki/sources/pxd-writone-ai-writing-assistant|pxd: Writone]] (0.65) | UX writing guidelines | **new** | placement as the adoption constraint; rule-based RAG; citation-grade transparency |
| [[wiki/sources/maily-product-makers-guardrails|Product Makers Note #24]] (0.68) | content safety | **new** | three-layer guardrail model; over-refusal named honestly |
| [[wiki/sources/polar-orbit-llm-safe-design-system|Polar Orbit]] (0.78) | design system styling | | typed tokens, banned syntax, CI as contract |
| [[wiki/sources/naver-d2-ai-hackathon-nstake|NAVER D2: NStake]] (0.87) | financial correctness | | authorization boundaries before the model |
| [[wiki/sources/socar-self-healing-agents|SOCAR]] (0.85) | production reliability | | structural containment, **with outcome numbers** |

## Synthesis

### 1. The convergence is real, and it is now independent enough to weight

[[wiki/sources/karrot-kraft-design-system-agent|Karrot]] arrived at Polar Orbit's principle without arriving at Polar Orbit's mechanism. Polar makes an off-system value **uncompilable** — typed tokens, banned raw layout syntax, CI as a contract. Karrot makes it **unrepresentable in the plan** — a `DesignSpec` schema whose `designTokens` field accepts `bg.layerDefault` and cannot hold `#FF6F0F`. Different layer, different tooling, different country, same conclusion: *the generator stays free; the gate gets narrow.*

That now holds across styling (Polar), screen structure (Karrot), authorization (NStake), production reliability (SOCAR), and content safety (#24). Five domains, five organisations, none citing another. This is about as strong as convergent evidence gets without anyone running an experiment.

The reframing worth carrying is Karrot's, because it is the most portable:

> *"The question was not 'shall we have AI draw the screen?' but 'which decisions do we delegate to AI?'"*

**The unit of automation is the decision, not the artifact.** That sentence does more work than any of the mechanisms, because it survives changes in tooling.

### 2. Karrot extends the principle in two genuinely new directions

Everything before this batch enforced constraints as a **binary gate** — it compiles or it does not, the tool exists or it does not. Karrot adds two things the vault did not have:

**Scoring rather than gating.** Eleven [[wiki/concepts/ai-agents/generated-output-scoring|scorers]] rate each generated screen. The reusable part is not the count but the **split by what the check needs**: seven are deterministic static analyses (is this a semantic token or a hex value?) and four are LLM calls reserved for judgment (is this interaction pattern right for this screen type?). A gate answers pass/fail; a score answers *how far off, and where*, which is what lets the agent self-correct — bounded, in Kraft's case, at two attempts.

**Cumulative rather than authored.** Decisions append to a per-session log; patterns repeating above a threshold are auto-promoted into per-domain principles; new sessions read them back. The constraint set grows from **use** rather than only from **authorship**. That is a different maintenance model for institutional knowledge than any other source here proposes.

Both are architecturally interesting. Neither is evidenced — see below.

### 3. The human moved to the decision point, not the production point

Read across the three new sources and one placement is consistent:

- **Writone:** *"AI는 선택지를 제시하고, 판단은 사람이 합니다"* — AI presents options, the person judges.
- **#24:** the model scores; *"where to post the gatekeeper and how sensitive to make it is the planner's job."*
- **Kraft:** Plan mode sharpens the design and stops — with the code tool **absent from its tool list**, not merely discouraged.

Kraft's version is the strongest form of [[wiki/concepts/ai-agents/approval-gate|approval gate]] in this vault, because it is not a rule the agent follows but a capability it lacks. A mode without the tool cannot be talked past. Approval-gate convergence is now **five sources deep**, from five unrelated motives.

The unexamined risk is unchanged and now more acute: **no source in this cluster has ever tested a gate under fatigue.** More gates keep arriving; nobody measures what happens when they fire constantly.

### 4. The load-bearing finding: the measurement gap is now a property of the field, not an accident

The 2026-07-28 memo flagged that every constraint architecture in the cluster charges standing maintenance and none states its break-even. Three sources later, that is unchanged — and the pattern has become the finding.

- **Kraft:** no adoption count, no cycle-time comparison, no eval-score distribution. A tool whose entire justification is consistency **reports no consistency metric.**
- **Writone:** no adoption, no accuracy, no compliance-rate change, no failure cases at all.
- **#24:** no block rates, no over-refusal rates, no false-positive figures. The 0.7 threshold is admittedly arbitrary.

Only **SOCAR** has ever put numbers behind a constraint architecture in this vault (4 hours → under 5 minutes; 7,267 recoveries). One source out of eight.

This matters more than it looks. Every one of these architectures is **expensive**: eleven scorers with four model calls per run, seven skill files, a memory store, a schema plus its validator, a moderation subscription with a red-team loop. All are justified against a counterfactual — "output would otherwise be inconsistent" — that **nobody has measured**. The honest position is that this cluster has produced a well-argued, internally consistent, independently convergent body of *design reasoning* with almost no *evidence of effect*.

That is not a reason to discard it. Convergence across five unrelated domains is genuine information. It is a reason to state plainly what kind of information it is: **these teams agree on what good architecture looks like; none of them has shown it works.**

### 5. Two sources also converge on placement — and it cuts against the cluster

Writone and Kraft independently concluded that **where the tool lives** decides whether it is used, and that moving it into the existing work surface buys **context**, not just convenience. Writone became a Figma plugin because the guideline check happens inside Figma and leaving is what kills it; Kraft moved from hosted admin to local CLI because a web app *"gives the used-goods team and the real-estate team the same result"* — it could not reach the project folder. See [[wiki/concepts/infrastructure-dev/in-workflow-ai-placement|In-Workflow AI Placement]].

The tension worth recording: **in-workflow placement raises the automation-bias stakes.** A suggestion appearing at the moment of work is easier to accept unreflectively than one requiring a deliberate check. [[wiki/concepts/agent-experience/willful-blindness|Willful blindness]] applies with more force, not less. Neither source measures acceptance rates, so neither can see its own risk.

## Implications

1. **Route the constraint by the kind of rule.** Actions that must never happen → remove the capability. Rules with one correct answer → schema or type system. Rules needing judgment → post-hoc scoring, with the deterministic checks split out. Never carry weight in the prompt. Full table: [[wiki/comparisons/where-to-put-the-constraint|Where to Put the Constraint]].
2. **Split your scorers by what the check requires.** Most compliance checking is mechanical and should never cost a model call.
3. **Enforce approval by removing the capability**, not by instructing restraint.
4. **Bound the self-repair loop.** Two attempts, then escalate.
5. **Budget the false positive.** Every binding layer over-blocks; a layer without an escape hatch and an owner for its false positives is unfinished.
6. **If you build one of these, measure it** — a before/after consistency rate or rework rate would make you the second team in this vault with evidence, and the first in design tooling.

## Risks and counterpoints

- **The measurement gap is this memo's own largest exposure.** Five of six sources report no outcome. The synthesis is therefore about *converging design reasoning*, and any claim that these architectures **work** is unsupported by the material here.
- **Four of six sources are first-party accounts** by the teams that built the thing, on their own blogs. Selection is severe: nobody publishes the constraint architecture they abandoned. Karrot's multi-agent reversal is the sole negative result, and it is qualitative.
- **Regional concentration.** Five of six are Korean industry sources. The consistency may partly reflect a shared engineering-blog culture rather than independent discovery.
- **The convergence may be weaker than it looks.** "Constrain the gate, not the generator" is general enough that several distinct practices fit it. Polar's type system and #24's moderation API are doing quite different work; calling both the same principle risks retrofitting a pattern.
- **Cost is systematically unreported.** Every source describes what it built; none says what it cost or what it would take to abandon.
- **#24 is a tutorial, not a case**, and its option space omits structural containment entirely — the approach the better-evidenced sources in this cluster actually use.

## Next research actions

1. **Find any source that measures a constraint architecture's benefit against its cost.** This has been the cluster's top gap since 2026-07-28 and is now three sources more urgent.
2. **Find evidence on approval-gate fatigue.** Five convergent sources, zero measurements, and the pattern keeps adding gates.
3. **Ingest parts 2–4 of the Product Makers Note series** — especially part 3 (human-in-the-loop), which lands on this vault's densest cluster.
4. **Look for a published eval-score distribution** from any design-system generation tool. One would convert this entire cluster from architecture to evidence.
5. **Find a non-Korean, non-first-party account** of a constraint architecture, to test whether the convergence survives outside this publishing culture.

## Related

- [[wiki/analyses/2026-07-28-constraining-ai-by-construction|Constraining AI by Construction (2026-07-28)]] — the parent memo; this one extends it with three sources and confirms its open gap is structural.
- [[wiki/comparisons/where-to-put-the-constraint|Where to Put the Constraint]] — the decision table this memo argues for.
- [[wiki/comparisons/delegate-vs-determinize|Delegate to a Model vs. Determinize in Code]] — the prior question.
- [[wiki/concepts/infrastructure-dev/llm-safe-design-system|LLM-Safe Design System]] · [[wiki/concepts/ai-agents/generated-output-scoring|Generated-Output Scoring]] · [[wiki/concepts/ai-agents/design-spec-intermediate-representation|Design Spec as Intermediate Representation]] · [[wiki/concepts/ai-agents/layered-content-guardrails|Layered Content Guardrails]] · [[wiki/concepts/infrastructure-dev/in-workflow-ai-placement|In-Workflow AI Placement]]

## Not in this memo

Two sources from this batch — [[wiki/sources/carl-pearson-minimally-technical-reporting|Pearson on reporting depth]] and [[wiki/sources/smashing-matching-ai-modality-user-intent|Yocco on modality]] — form a separate two-source pairing, below the threshold for their own memo. Their shared thesis is worth recording for when it reaches five: **the artifact must be shaped to the receiver's cognitive state, not to the producer's convenience** — Yocco against defaulting to chat because LLMs speak, Pearson against defaulting to the appendix because that is what the analysis produced. Neither cites the other; the pairing is this vault's inference.
