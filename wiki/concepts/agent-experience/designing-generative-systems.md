---
type: concept
status: active
created: 2026-07-30
updated: 2026-07-30
tags: [concept, agent-experience, generative-ui, design-practice, role-convergence, review-surface, product-taste]
sources: [designer-builder-collapse, naver-d2-ai-hackathon-nstake]
confidence: 0.62
---

# Designing Generative Systems

> [!abstract] Summary
> The shift from designing **fixed interfaces** to designing the **system that generates them** — where the designed artifact becomes constraints, vocabulary, and a review surface rather than screens, and the design act moves from *construction* to *review and approval*.

> [!important] Why it Matters
> If interfaces are generated rather than drawn, the leverage moves to whatever bounds the generation — the token vocabulary, the component catalog, the constraints that make wrong output impossible. That is the same conclusion [[wiki/concepts/infrastructure-dev/llm-safe-design-system|LLM-Safe Design System]] reached from the engineering side, arrived at here from a designer's frustration with chat interfaces. It also relocates the profession's daily work onto a surface — review — that nobody has designed.

## 📝 Key Claims

- **Chat is not the endpoint.** Text-heavy interfaces cause user fatigue; visual, interactive *generated* interfaces are the stated frontier — and frontier labs have not yet delivered on it.
- **The design act becomes review.** As generation handles construction, approving and correcting becomes the work.
- **Taste is the differentiator** from AI, developed through creative side projects. Asserted, not defined.
- **Prototyping collapses into designing.** A reusable prototyping kit (the anchor source used a Claude-based one) makes interactive prototypes a minutes-scale activity, which changes when in the process design decisions get made.
- **Automation should be proposed, not configured.** Systems that observe work patterns and suggest automations, rather than requiring manual workflow construction. Explicitly aspirational.
- **Speed of generation is not speed of judgment.** See the counter-evidence below — this is the claim the concept most needs.

## What the designed artifact becomes

| Old artifact | New artifact |
|---|---|
| Screens and flows | Constraints and vocabulary the generator must use |
| Component library for humans to assemble | Machine-readable catalog that bounds what can be produced |
| Spec handed to engineering | Review surface where generated output is accepted or rejected |
| Design review as a meeting | Design review as the primary production activity |

## ⚖️ Conflicts & Caveats

> [!warning] Directly contradicted on prototyping speed
> The anchor source treats fast generated prototypes as the win. [[wiki/sources/naver-d2-ai-hackathon-nstake|NStake]] reports the opposite outcome from an actual project: three developers generated an entire UI in one hour — around a cute character theme, for a finance team whose spreadsheets used **cell colour as meaning**. It was wrong for the audience, and refinement toward a trusted corporate design language made **design the development bottleneck** while the team waited on assets.
>
> The reconciliation: **generation converged, audience judgment did not.** Prototyping speed is real; the unautomated remainder is knowing what the users' existing conventions mean — which is arguably what "taste" names, and which the anchor source leaves undefined.

> [!warning] Single practitioner, strong selection effect
> One unusually technical designer at a large tech company with time for side projects. No data, no cohort. Whether the collapse reaches designers without engineering fluency or slack time is untested, and that is most designers.

> [!warning] The review surface inherits the fatigue problem
> If design becomes approval, it inherits the largest unsolved problem in this vault's agent work: a gate that fires constantly trains reflexive approval. See [[wiki/concepts/ai-agents/approval-gate|Approval Gate]]. Nobody has designed a review surface for high-volume generated UI, and no source measures what happens to quality under that load.

> [!warning] Accountability is unaddressed
> The construction-to-approval shift moves the *work* and says nothing about the *responsibility*. When a generated interface ships and fails, the reviewer is accountable for output they did not compose — a position with no established practice around it.

> [!warning] Aspirational content flagged
> Automation-observing systems are undemonstrated; generated interfaces are an expectation the interviewee notes has not been met. Treat both as direction, not capability.

## 🔗 Related Concepts

- [[wiki/concepts/infrastructure-dev/llm-safe-design-system|LLM-Safe Design System]] — the engineering-side arrival at the same conclusion: bound the generator's vocabulary.
- [[wiki/concepts/agent-experience/a2ui-protocol|A2UI Protocol]] — the protocol version of agent-composed UI from a machine-readable catalog.
- [[wiki/concepts/infrastructure-dev/component-catalog|Component Catalog]] — the palette that becomes the design ceiling.
- [[wiki/concepts/agent-experience/natively-adaptive-interfaces|Natively Adaptive Interfaces]] — per-interaction adaptation as the same bet from the accessibility direction.
- [[wiki/concepts/ai-agents/vibe-design|Vibe Design]]
- [[wiki/concepts/infrastructure-dev/ai-prototyping|AI Prototyping]]
- [[wiki/concepts/product-management/product-taste|Product Taste]] — the named differentiator, still undefined.
- [[wiki/concepts/product-management/role-convergence|Role Convergence]] — the designer-builder collapse as one instance.
- [[wiki/concepts/ai-agents/approval-gate|Approval Gate]] — where the review surface meets the fatigue problem.
- [[wiki/concepts/infrastructure-dev/deterministic-ui|Deterministic UI]]

## 📚 Sources

- [[wiki/sources/designer-builder-collapse|Ozenc & Yousefi (2026): The Designer-Builder]] — the shift, the prototyping kit, taste-as-differentiator, review-as-design-act. Single practitioner interview, no data.
- [[wiki/sources/naver-d2-ai-hackathon-nstake|NAVER D2 (2026): NStake]] — the counter-evidence on generation speed versus audience judgment, and the design bottleneck.

## ❓ Open Questions

- What does a good review surface for generated UI look like? Nobody in this vault has designed one.
- What is "taste" operationally — how would you assess it in a portfolio or teach it?
- Does the shift stratify the design profession by technical fluency?
- Who is accountable when generated output ships and fails — reviewer or generator?
- Is there a measurable quality difference between designed-and-built and designed-and-generated interfaces? No source measures this.
