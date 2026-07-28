---
type: analysis
status: active
created: 2026-07-28
updated: 2026-07-28
tags: [analysis, agentic-engineering, ai-agent, deterministic-workflows, guardrails, design-system, verification, reliability]
sources:
  - naver-d2-ai-hackathon-nstake
  - socar-parking-brain-knowledge-graph
  - polar-orbit-llm-safe-design-system
  - b2b-admin-web-accessibility
  - membership-inference-attack-explainer
confidence: 0.80
---

# Constraining AI by Construction — Synthesis of the 2026-07-28 Cluster

## Research Question

The [[wiki/analyses/2026-07-24-directing-agents-in-production|2026-07-24 memo]] concluded that **reliability is bought in code, not in prompts**, on the strength of a single production case. Five sources ingested on 2026-07-28 test that conclusion from five unrelated domains. The question here: **does the structural-constraint finding generalize, and what does "structural" actually mean once you have five instances?**

It generalizes. And the five instances turn out to be constraining five *different things* — which is the substance of this memo.

## Evidence Base

| Source | Domain | What it constrains | Evidence grade |
|---|---|---|---|
| [[wiki/sources/naver-d2-ai-hackathon-nstake\|NAVER D2 — NStake]] | Internal finance tooling | **Authority** — AI removed from deciding official numbers; access provisioned before generation | Prototype, 6 hours, richly reasoned, no measurement (0.87) |
| [[wiki/sources/socar-parking-brain-knowledge-graph\|SOCAR — parking-brain]] | Internal dev knowledge | **Context** — domain truth made addressable and provenance-carrying | Architecture with node counts, no outcome metric (0.83) |
| [[wiki/sources/polar-orbit-llm-safe-design-system\|Polar — Orbit]] | Design system / front-end | **Vocabulary** — off-system values made uncompilable | Qualitative, self-observed, no measurement (0.78) |
| [[wiki/sources/b2b-admin-web-accessibility\|rami_ — B2B accessibility]] | Front-end accessibility | **Measurement** — the audit instrument itself needed verification | Single concrete case with numbers (0.76) |
| [[wiki/sources/membership-inference-attack-explainer\|당근대장 — MIA]] | AI privacy/security | **The artifact** — what the trained model itself reveals | Secondary explainer, uncited primaries (0.74) |

Prior anchor, carried forward: [[wiki/sources/socar-self-healing-agents|SOCAR self-healing agents]] — production, two months, real metrics (0.88).

**Note the evidence shape.** Five sources, five domains, one direction — and **not one of them measures the benefit.** That combination is exactly what this memo has to reason carefully about: strong convergence, weak quantification.

## Synthesis

### 1. Five sources, five different objects of constraint

The 2026-07-24 memo's formulation was "reliability is bought in code." Too coarse. What these sources show is that the constraint gets applied at whichever layer the model would otherwise be trusted:

- **Authority** — NStake: identical input must give identical output, so the calculation leaves the model entirely. The LLM-generated monthly report was fast and demoed well; it produced varying wording on identical data, drifted from company format, and made official reporting dependent on model uptime. Classification and totals became explicit rules. AI stayed for explaining discrepancies and drafting inputs.
- **Access** — NStake again: the model receives only the entities the logged-in user may see, re-checked in the database on every request. Reading everything and masking the answer was explicitly rejected as unsafe.
- **Context** — parking-brain: the agent that reimplemented an existing API had no way to find it. The fix is a queryable graph with `sourceRef` pointers, not a better prompt.
- **Vocabulary** — Orbit: an LLM handed open utilities will pick `p-4` here and `p-5` there. Remove the arbitrary value from the type system and the wrong choice becomes unrepresentable.
- **Measurement** — rami_: an automated accessibility scan reported 168 missing `alt` attributes where **6** existed. Not a hallucination — a line-based grep against multi-line markup, trusted without verification.
- **The artifact** — MIA: even a correctly-behaving model is a disclosure surface, because it memorizes.

**The generalized rule:** *identify every place where the system currently trusts the model to behave, and replace trust with structure at that layer.* Prompting appears in none of the six.

### 2. The constraint sits on the acceptance criteria, not the generator

Polar states this most cleanly — *"The LLM is free to write anything it wants. We just make sure the only things that pass CI are things we'd be happy to ship"* — and every other source is doing the same thing under a different name. SOCAR's structured output schemas. NStake's per-request authorization re-check and explicit-confirmation gates. parking-brain's confidence threshold with a human approval queue.

This resolves something the 2026-07-24 memo left slightly muddled. That memo's two-axis model was *latitude in reasoning, bounds on action*. The sharper version: **the generator stays free; the acceptance gate gets narrow.** NStake's team let the model reason about unfamiliar finance concepts and explain complex discrepancies — genuine latitude — while removing its authority over the numbers. Those are not in tension because they are not the same layer.

### 3. Convergence is now strong enough to treat as settled; efficacy is not

Six sources across production browser automation, internal finance tooling, developer knowledge management, design systems, accessibility engineering, and ML privacy all conclude that safeguards must be structural rather than instructed. They cite each other zero times. Independent arrival at the same conclusion from unrelated pressures is the strongest signal available that a pattern is load-bearing.

But: **only one of the six measures anything.** SOCAR's self-healing agents post has two months of production numbers. The other five report a prevented failure, a qualitative improvement, or a design rationale. Nobody built the same system both ways.

So the honest statement is narrower than it looks. Well supported: *these teams encountered specific failures and structural constraints addressed them.* Not established: *that constraint architectures produce better outcomes than the alternatives*, or what they cost relative to what they save. Every determinize decision in the [[wiki/comparisons/delegate-vs-determinize|comparison table]] is a reasoned judgment backed by an observed failure — which is real evidence, and is not measurement.

### 4. Verification by execution is the cluster's most transferable rule

NStake: *"verify AI-generated code by actual execution results, not by its explanation."* They hit this twice — features the agent reported complete that were never wired into a user flow, and reset code that ran against the wrong database.

rami_ generalizes it past agents entirely. The 168-vs-6 overcount was not a model failure; it was a *tool* failure trusted without checking. Note the asymmetry that makes this honest: the `th` finding was 141 real out of 166 reported. One unreliable instrument, not an indictment of automated scanning — and the fix is the same choice parking-brain made independently, **parse the structure rather than search the lines.**

The rule that survives: *any report about the state of the world — from a model, a script, or a grep — is a claim, and claims about structured artifacts need structural instruments.*

### 5. Context provisioning is a constraint problem, not an abundance problem

Two sources contradict "give the agent more context," from opposite directions.

NStake found that **as documents accumulated, understanding degraded** — terms and as-of dates mixed, authority became ambiguous, existing screens conflicted with actual business rules. What they needed was *judgment criteria, not volume*: which document is authoritative, what wins when values differ, who decides exceptions, what is auto-applied versus human-checked.

parking-brain found the same thing quantitatively: **~50% of wiki content was irrelevant**, and ingesting comprehensively *destroyed credibility* in the answers. Their fix is structural filtering plus confidence gates plus an approval queue.

Both point at the same object — [[wiki/concepts/ai-agents/context-rot|context rot]] — and both fix it by *curation with provenance* rather than retrieval volume. There is one live methodological conflict inside this: parking-brain **tried LLM extraction of concepts and abandoned it** as too noisy, reverting to ~100 hand-written seeds, which directly contradicts the pre-ontology approach anchoring [[wiki/concepts/infrastructure-dev/organizational-ontology|Organizational Ontology]]. The difference may be input type (code vs. speech) rather than a real disagreement. No source settles it.

### 6. Every constraint architecture in this cluster charges maintenance

Named explicitly, because it is the counterargument the sources under-weight:

| Source | Standing cost |
|---|---|
| SOCAR self-healing | Baseline schema upkeep per operator |
| parking-brain | ~100 seeds hand-curated; hourly regeneration over 17k nodes; human approval queue |
| Orbit | Token additions **weekly**; every lint-disable treated as a defect to fix |
| NStake | Rule authoring for every official calculation |

Four for four. **The break-even volume is stated by none of them.** Below some threshold the architecture costs more than the failures it prevents, and no source in this wiki says where that threshold is. This is the most important unmeasured quantity in the cluster.

### 7. The design bottleneck moved, and nobody predicted it

An aside worth recording because it cuts against the prevailing assumption. NStake's three developers generated the entire UI in one hour — around a cute steak character in browns and beiges, loading screen included. Wrong for a finance team whose Excel used **cell color as meaning** (yellow, gray, pale blue = information state, not decoration). What those users needed was familiarity, trust, formality, professionalism.

Switching to the NAVER design system took repeated correction, some assets had to be redrawn by hand, and **design became the development bottleneck while the team waited on PNGs.** Generation was instant; judgment about the audience was not, and refinement was slower than building from a known system would have been. AI accelerated exploration and drafting and was not the final judge.

## Implications

1. **Enumerate the trust points before adding an agent.** For each, ask: authority, access, context, vocabulary, measurement, or artifact? Then replace trust with structure at that layer. This is the actionable form of the whole cluster.
2. **Apply the reproducibility test first.** *Must identical input produce identical output?* If yes, the work leaves the model. Sharpest single test available, and it needs no further analysis.
3. **Provision access before generating.** Scoping context at authorization time is a boundary; masking a full-visibility answer is not.
4. **Constrain the acceptance gate, not the generator.** Types, schemas, CI, and independent validators. Leave reasoning latitude intact.
5. **Verify by execution and by structural instruments.** Never accept a model's account of its own work, and never accept a line-based count of a structured artifact.
6. **Curate context with provenance and recency, and say what you dropped.** More documents is not more context.
7. **Price the constraint before adopting it.** Ask what it will cost weekly, and what volume of prevented failure justifies that. No source will tell you; estimate it locally.
8. **Do not expect AI to relieve design judgment.** Expect it to relieve design *drafting*, and budget for the refinement that follows.

## Risks & Counterpoints

- **One prototype carries too much of this memo.** NStake supplies the delegation table, the R/S/X split, the authorization boundaries, and the workflow-completeness test — from six hours of work by four people, with no measurement. It is corroborated *in direction* by SOCAR's production case, but if NStake's reasoning is wrong, several sections weaken at once.
- **Rule-friendly domains are over-represented.** Equity arithmetic, design tokens, integration repair, and accessibility markup all have checkable right answers. The cluster says little about judgment-heavy work — which is where the delegation question is hardest and where the "determinize it" prescription may simply not apply.
- **Convergence could be a selection effect.** These are all first-party engineering posts, a genre that rewards a clear lesson learned. Teams that tried open-ended agency and succeeded quietly do not write this post. The convergence is real; the sample is not random.
- **Constraint architectures could be over-fitting to 2026 model limitations.** Every source is engineering around present-day unreliability. If models become substantially more reliable, some of this becomes needless ceremony — though the *reversibility* gating logic survives regardless, since it never depended on model quality.
- **Approval-gate fatigue is still unaddressed** — the same gap the 2026-07-24 memo named. This cluster routes *more* work to human approval (per-request authorization, explicit confirmation for state changes, external-validation queues) and still no source tests what happens when gates fire constantly. It remains the largest open risk, and it remains a UX problem.
- **MIA is anchored on a secondary explainer** with uncited primaries. The concept is sound and the checklist is usable; the page is not citation-grade until NIST guidance or Shokri et al. (2017) is ingested directly.
- **Two sources are from SOCAR**, so the six sources are not six independent organizations.

## Next Research Actions

- [ ] **Find one source that measures a constraint architecture's cost against its benefit.** This is now the cluster's single biggest hole — six sources agree on direction and none quantifies the trade.
- [ ] **Source evidence on approval-gate fatigue.** Carried over unresolved from 2026-07-24 and now more urgent, since this cluster adds gates. Natural UX research question.
- [ ] **Ingest a primary source for [[wiki/concepts/ai-agents/membership-inference-attack|MIA]]** — NIST AI privacy guidance and/or Shokri et al. (2017).
- [ ] **Resolve the extraction conflict** between parking-brain's rejection of LLM concept extraction and the pre-ontology approach in [[wiki/concepts/infrastructure-dev/organizational-ontology|Organizational Ontology]]. Is it input type, or LLM extraction as such?
- [ ] **Backfill [[wiki/sources/google-natively-adaptive-interfaces|Google NAI]]** (sub-guides unfetched) and resolve whether agent adaptation raises or lowers the need for underlying accessibility semantics.
- [ ] **Find a judgment-heavy domain case** — somewhere with no deterministic right answer — to test whether the determinize prescription has a boundary.
- [ ] Re-verify NStake and parking-brain figures against the originals before any external citation.

## Related

- [[wiki/comparisons/delegate-vs-determinize|Comparison: Delegate to a Model vs. Determinize in Code]] — the decision table this memo supports.
- [[wiki/analyses/2026-07-24-directing-agents-in-production|Analysis: How Much Latitude Should an Agent Get?]] — the memo this one extends and partially answers.
- [[wiki/concepts/infrastructure-dev/deterministic-ai-workflows|Deterministic AI Workflows]]
- [[wiki/concepts/ai-agents/permission-boundary-guardrails|Permission-Boundary Guardrails]]
- [[wiki/concepts/infrastructure-dev/llm-safe-design-system|LLM-Safe Design System]]
- [[wiki/concepts/infrastructure-dev/domain-knowledge-graph|Domain Knowledge Graph]]
- [[wiki/concepts/ai-agents/rule-statistical-external-validation|Rule / Statistical / eXternal Validation]]
- [[wiki/concepts/ai-agents/workflow-completeness|Workflow Completeness]]
- [[wiki/concepts/ai-agents/membership-inference-attack|Membership Inference Attack]]
