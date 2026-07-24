---
type: concept
status: active
created: 2026-07-24
updated: 2026-07-24
tags: [concept, ai-agent, delegation, management-model, agent-experience, ai]
sources: [ai-as-senior-hire-not-intern]
confidence: 0.7
---

# AI as a Senior Hire

> [!abstract] Summary
> A delegation model that briefs an agent the way you would brief an **experienced colleague** — outcome, constraints, and room to solve — rather than the way you would brief an intern, with prescribed steps. The claim is that over-specification actively suppresses the problem-solving capability that makes the system worth using.

> [!important] Why it Matters
> The prevailing "army of interns" metaphor sets the wrong default. It misplaces where the systems are strong, and it frames the human contribution as supervision of the unskilled — which quietly devalues the domain expertise that actually determines whether the output is any good.

## 📝 Key Claims

- **Brief with intent, not procedure.** "Imbue it with intentions" rather than prescribing steps.
- **The intern framing fails twice** — wrong model of capability, and corrosive to how teams value expertise.
- **Capability arrives discontinuously**, so adoption plans built on smooth extrapolation misfire.
- **"Sensitivity" over "taste"** — attunement to human needs, product quality and teammate welfare is proposed as the durable skill as generation gets cheap.
- Adoption works **bottom-up and expected-but-not-mandatory**, with leadership accountable for pulling what works into real iteration cycles.

## ⚖️ Conflicts & Caveats

> [!warning] Contradicted by production evidence
> [[wiki/sources/socar-self-healing-agents|SOCAR's production deployment]] achieved its results by **removing** agent discretion, not granting it — sequential constrained stages beat open-ended agency, decisively. The reconciliation this wiki holds: **seniority of briefing is compatible with tight bounds on action.** Give latitude in *how to reason*; give none in *what may be executed*. Consequence decides which dominates — the higher the blast radius, the more the SOCAR posture wins.

> [!warning] The metaphor breaks on accountability
> A senior hire carries responsibility for outcomes. An agent cannot. The framing improves the *briefing* model while silently breaking the *responsibility* model — the human remains fully accountable regardless of how senior the briefing style.

> [!note] Unmeasured
> Single practitioner opinion. No task class has been identified where micro-specification measurably loses, which is what would make this falsifiable.

## 🔗 Related Concepts

- [[wiki/concepts/ai-agents/jagged-frontier|Jagged Frontier]] — why the seniority illusion breaks intermittently
- [[wiki/concepts/infrastructure-dev/agent-defense-in-depth|Agent Defense in Depth]] — the counterweight
- [[wiki/concepts/ai-agents/interview-first-elicitation|Interview-First Elicitation]] — arguably the opposite tactic
- [[wiki/concepts/ux-research/human-in-the-loop|Human in the Loop]]
- [[wiki/concepts/ai-agents/context-engineering|Context Engineering]]

## 📚 Sources

- [[wiki/sources/ai-as-senior-hire-not-intern|Ozenc & Holbrook (2026): AI as a Senior Hire, Not an Intern]]

## ❓ Open Questions

- Does this survive contact with high-consequence domains, where procedure exists precisely to constrain judgment?
- Is the review burden a transitional cost or the permanent shape of the work?
- What task class would falsify it?
