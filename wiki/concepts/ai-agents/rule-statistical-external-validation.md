---
type: concept
status: active
created: 2026-07-28
updated: 2026-07-28
tags: [concept, ai-agent, validation, data-quality, human-in-the-loop, triage, deterministic-workflows]
sources: [naver-d2-ai-hackathon-nstake]
confidence: 0.78
---

# Rule / Statistical / eXternal Validation (R-S-X)

> [!abstract] Summary
> A three-way split of validation findings by **what kind of authority the system has over them**: **Rule** — decidable by explicit rule, so the system is right; **Statistical** — a signal that narrows where a human looks first, asserting nothing; **eXternal** — a difference against another source of truth, where the system must *not* decide and a human confirms. Not everything a validator surfaces can honestly be called an error.

> [!important] Why it Matters
> A validation system that labels every finding an "error" fails in both directions at once: it over-claims certainty on the things it cannot know, and it hands the user an undifferentiated queue with no ordering. The R-S-X split fixes both — it tells the user *how much to trust each finding* as part of the finding. [[wiki/sources/naver-d2-ai-hackathon-nstake|NStake's]] team credits this separation with much of the system's perceived trustworthiness, and it is the cleanest small pattern in the 2026-07-28 cluster for placing AI, statistics, and rules in one pipeline without confusing their authority.

## 📝 Key Claims

- **Rule findings are assertions.** Ownership percentages that do not total correctly, a missing exchange rate, a transaction dated after liquidation — these are decidable by explicit rule, and the system should state them as facts.
- **Statistical findings are attention-narrowing, not fault-finding.** An unusually large transaction amount or an abrupt share-count change does not establish error. Its job is to shorten the list a human reviews first. This is precisely the band where "narrowing what to check matters more than being right" — the condition under which the source assigns work to AI or a statistical model.
- **External findings must not be auto-resolved.** When an internal value differs from an external disclosure, the difference may be a different as-of date, an unreflected recent transaction, or a genuinely different definition. Declaring either side wrong — or silently correcting — destroys the reconciliation's value.
- **The classification is part of the finding.** Surfacing *how the system knows* alongside *what it found* is what lets a user act on it in one pass.
- **Every class needs a disposition path.** Findings a user cannot correct or mark "no issue" become a second to-do list rather than a service — the same [[wiki/concepts/ai-agents/workflow-completeness|workflow completeness]] failure the source names elsewhere.

## The split

| Class | System's authority | Example | Correct disposition |
|---|---|---|---|
| **Rule** | Decides | Ownership total mismatch; missing exchange rate; transaction after liquidation | Assert as error; block or flag definitively |
| **Statistical** | Suggests | Unusually large amount; abrupt share-count change | Rank for human attention; assert nothing |
| **eXternal** | Reports only | Internal value ≠ external disclosure | Present both sides with as-of dates; human confirms |

## Where this generalizes

The pattern is not finance-specific. It applies wherever a system validates data it does not fully own:

- **Research data validation** — schema violations (Rule) vs. outlier responses (Statistical) vs. disagreement with a prior study or analytics (eXternal).
- **Content and design linting** — token violations (Rule) vs. unusual composition (Statistical) vs. divergence from a Figma source (eXternal).
- **Analytics reconciliation** — impossible values (Rule) vs. anomalous trends (Statistical) vs. mismatch against a billing system (eXternal).

The test for placing a finding: *if the system is wrong about this, what happens?* Rule-class errors are cheap to be wrong about because they are checkable. External-class auto-decisions are expensive because both sides may be correct.

## ⚖️ Conflicts & Caveats

> [!warning] Single-source pattern from a prototype
> This comes from one six-hour hackathon project in a domain (equity arithmetic) with unusually clean rule boundaries. The three classes are a well-reasoned design, not a validated taxonomy — and no source tests whether users actually read the classification or treat all three the same.

> [!warning] The boundary between Rule and Statistical is a judgment call
> "Ownership totals must sum correctly" is clearly Rule. "This amount is unusually large" is clearly Statistical. In between sit thresholds that *look* like rules but encode assumptions — and misfiling one of those as Rule means the system asserts something it should have suggested.

> [!warning] External findings accumulate
> A reconciliation class that the system cannot resolve grows monotonically unless humans work it down. NStake's own remaining work includes automated reconciliation against the internal finance ledger, which suggests the eXternal queue was the unfinished part.

> [!warning] Statistical signals need calibration nobody reports
> "Unusually large" requires a threshold, and no false-positive rate is given. A statistical class that fires too often becomes noise and trains users to ignore the tier that was supposed to direct their attention.

## 🔗 Related Concepts

- [[wiki/concepts/infrastructure-dev/deterministic-ai-workflows|Deterministic AI Workflows]] — the parent principle: stable checks belong in rules, not in a model.
- [[wiki/concepts/ai-agents/workflow-completeness|Workflow Completeness]] — why each class needs a disposition path, not just a surface.
- [[wiki/concepts/ai-agents/permission-boundary-guardrails|Permission-Boundary Guardrails]] — the sibling pattern from the same source.
- [[wiki/concepts/ai-agents/agent-verifiers|Agent Verifiers]] — independent validation of agent output.
- [[wiki/concepts/ux-research/research-data-validation|Research Data Validation]] — the closest UX-research analogue.
- [[wiki/concepts/ai-agents/approval-gate|Approval Gate]] — where eXternal findings terminate.
- [[wiki/concepts/agent-experience/trust-calibration|Trust Calibration]] — surfacing how much confidence a finding deserves is a trust-calibration mechanism.
- [[wiki/concepts/ai-agents/product-evals|Product Evals]]

## 📚 Sources

- [[wiki/sources/naver-d2-ai-hackathon-nstake|NAVER D2 (2026): What the Winning AI Hackathon Team Did *Not* Delegate to AI]] — sole source for the R/S/X split and the "not everything is an error" argument.

## ❓ Open Questions

- Do users actually treat the three classes differently, or does a mixed queue collapse into one review behavior?
- What false-positive rate makes a Statistical tier useful rather than ignorable?
- How should the eXternal queue be bounded so it does not grow without limit?
- Is a fourth class needed for findings the system suspects are *stale* rather than wrong — the [[wiki/concepts/infrastructure-dev/domain-knowledge-graph|knowledge-graph]] recency problem in validation form?
- Does the split survive in a domain with no clean Rule class at all?
