---
type: comparison
status: active
created: 2026-07-31
updated: 2026-07-31
tags: [comparison, decision-table, constraint-by-construction, guardrails, design-system, agentic-engineering, evals, schema]
sources:
  - karrot-kraft-design-system-agent
  - polar-orbit-llm-safe-design-system
  - maily-product-makers-guardrails
  - socar-self-healing-agents
  - naver-d2-ai-hackathon-nstake
confidence: 0.74
---

# Where to Put the Constraint

## Decision question

**When you need a generative system to stay inside institutional rules, at which layer do you enforce it?** Every source in this vault's constraint cluster agrees the prompt is the wrong answer. They disagree — mostly without noticing each other — about what the right one is. This table lays the options side by side.

The five layers below are not alternatives so much as positions on a pipeline: **prompt → schema → capability → type system / CI → post-hoc scorer.** A mature system usually holds several. The question is which one carries the weight for a given rule.

## Criteria

- **Bindingness** — can a determined generator produce non-compliant output anyway?
- **Failure timing** — how early is a violation caught? Earlier is cheaper.
- **Expressiveness cost** — what legitimate output does the constraint also forbid?
- **Standing cost** — what does it cost to build and to keep true as the system changes?
- **Explains itself** — does a violation tell you *what* was wrong and *where*?

## Matrix

| Layer | Bindingness | Fails at | Expressiveness cost | Standing cost | Explains itself | Evidence in this vault |
|---|---|---|---|---|---|---|
| **Prompt / system instructions** | **None.** Universally rejected. Circumvented by "ignore previous instructions"; silently forgotten across long outputs | generation, sometimes never | none | trivial | no | [[wiki/sources/maily-product-makers-guardrails|#24]] calls it *"가장 약한 방어선"* — the weakest line; [[wiki/concepts/infrastructure-dev/agent-defense-in-depth|defense in depth]] independently: *"prompt it not to do that" is not a control* |
| **Schema / intermediate representation** | **High for what the schema covers.** A field that only accepts semantic token names cannot hold a hex value | before code exists | medium — no way to express a deliberate exception | medium: schema + validator + drift risk vs. the code | **yes** — validation points at a field | [[wiki/sources/karrot-kraft-design-system-agent|Kraft's DesignSpec]] |
| **Capability removal / tool boundary** | **Absolute for the removed action.** Not a rule about behaviour; the action does not exist | never happens | high — the capability is gone for everyone in that mode | low once built | n/a — there is nothing to explain | [[wiki/sources/naver-d2-ai-hackathon-nstake|NStake's]] six authorization boundaries; [[wiki/sources/socar-self-healing-agents|SOCAR's]] credential closure; Kraft's Plan mode without `runCodingAgent` |
| **Type system + CI** | **High.** Wrong output does not compile or does not merge | compile / CI | medium-high — bans a syntax surface; needs escape hatches (`Box as="nav"`) | high to build, low to run; **rots with the design system** | partly — a type error names the site, not the intent | [[wiki/sources/polar-orbit-llm-safe-design-system|Polar Orbit]] |
| **Post-hoc scoring / moderation** | **Low-to-medium.** Output already exists; you are deciding whether to accept it | after generation | low — nothing is forbidden up front | **highest**: scorers drift, LLM-based ones cost per run and are themselves unvalidated | **yes, best in class** — a score says how far off and where | Kraft's [[wiki/concepts/ai-agents/generated-output-scoring|11 scorers]]; #24's [[wiki/concepts/ai-agents/layered-content-guardrails|moderation APIs]] |

## Recommendation pattern

**Route by what kind of rule it is.**

1. **Is it a rule about an *action* that must never happen?** → **Capability removal.** Do not score it, do not instruct it. If the agent must never deploy, never delete, never see a credential, the boundary is the tool list. This is the only layer with no failure mode, and four independent sources converge on it.

2. **Is it a rule with one correct answer, decidable from the artifact?** (which token, which component, which format) → **Schema, or type system + CI.** Choose by where the artifact lives: if the agent produces a plan before it produces code, put it in the **schema** and fail before the code exists; if it emits code directly, put it in the **type system** and let CI hold the line. Polar's rule of thumb — *"the only things that pass CI are things we'd be happy to ship"* — applies to both.

3. **Is it a rule requiring judgment?** (is this pattern right for this screen; is this response harmful) → **Post-hoc scoring**, and split the suite: run mechanical checks mechanically, and spend model calls only on the genuinely qualitative. Kraft's 7-deterministic / 4-LLM split is the reference implementation.

4. **Never carry weight in the prompt.** Instructions may *guide*, but nothing should depend on them.

**Two cross-cutting rules the sources agree on:**

- **Bound the repair loop.** Kraft allows two self-corrections before re-verification. An unbounded retry against a failing validator burns budget and hides the failure.
- **Budget the false positive.** Every binding layer over-blocks. #24 names *"과차단"* (over-refusal) as the price of its strongest layer; Polar needs `as` props to restore semantics its ban removed. **A constraint layer without an escape hatch and an owner for its false positives is not finished.**

## Source evidence

- [[wiki/sources/karrot-kraft-design-system-agent|Karrot (2026): Kraft]] — schema, capability removal, and scoring in one system; the fullest single implementation here.
- [[wiki/sources/polar-orbit-llm-safe-design-system|Polar (2026): Orbit]] — type system and CI; the cleanest statement of the underlying principle.
- [[wiki/sources/maily-product-makers-guardrails|Product Makers Note (2026, #24)]] — layered content moderation, and the honest naming of over-refusal.
- [[wiki/sources/socar-self-healing-agents|SOCAR (2026)]] — capability removal in production, with the cluster's only real outcome numbers behind it.
- [[wiki/sources/naver-d2-ai-hackathon-nstake|NAVER D2 (2026): NStake]] — authorization boundaries placed before the model rather than after it.

## ⚖️ Caveats

- **The comparison is analytic, not empirical.** No source tests two layers against each other, so the bindingness and cost columns are reasoned from how each mechanism works — not measured.
- **Only SOCAR reports outcome numbers.** Kraft, Polar, and #24 all describe architecture without measuring effect; see [[wiki/analyses/2026-07-31-constraint-architectures-converge|the batch analysis]] on why that pattern matters.
- **No source states a break-even volume** for any layer, so "standing cost" is directional only.
- **Layers may not be independent.** Nothing here establishes that stacking two catches more than the stronger one alone.

## 🔗 Related

- [[wiki/comparisons/delegate-vs-determinize|Delegate to a Model vs. Determinize in Code]] — the prior decision: *whether* a model should own the step at all. This table assumes that answer is yes and asks where the leash attaches.
- [[wiki/concepts/infrastructure-dev/llm-safe-design-system|LLM-Safe Design System]]
- [[wiki/concepts/ai-agents/design-spec-intermediate-representation|Design Spec as Intermediate Representation]]
- [[wiki/concepts/ai-agents/generated-output-scoring|Generated-Output Scoring]]
- [[wiki/concepts/ai-agents/layered-content-guardrails|Layered Content Guardrails]]
- [[wiki/concepts/ai-agents/permission-boundary-guardrails|Permission-Boundary Guardrails]]
- [[wiki/analyses/2026-07-31-constraint-architectures-converge|Constraint Architectures Converge (2026-07-31)]]
