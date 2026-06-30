---
type: concept
status: active
created: 2026-06-26
updated: 2026-06-26
tags: [model-escalation-gate, model-tiering, agent-cost-control, advisor-mode, human-in-the-loop]
sources:
  - sources/heyratel-ios-ai-agent-environment
confidence: 0.75
---

# Model Escalation Gate

## Summary

A **model escalation gate** runs a cheaper model by default and escalates to a frontier model — or to a human — only for high-stakes or ambiguous decisions. The HeyRatel iOS team's instance: an `ios-developer` agent on Sonnet operates in an **"advisor" mode** where it can call **Opus 4.8** for high-stakes calls and escalates architecture-altering ambiguity to the main agent or the human, holding quality high without paying frontier rates on every step.

## Why It Matters

Using the strongest model everywhere is expensive; using only a cheap model risks quality on the decisions that matter. A gate resolves the tension: spend the expensive model (or human attention) precisely where stakes justify it. It's a concrete, reusable pattern for [[concepts/infrastructure-dev/agent-cost-control|agent cost control]] and a sibling of the Read/Draft/Act graduation idea — earn autonomy/spend by stakes, not by default.

## Key Claims

- **Cheap-by-default, escalate-by-stakes.** A lighter model handles routine work; a frontier model or human is invoked only on high-stakes/ambiguous decisions.
- **"Advisor" mode.** The implementer can *consult* a stronger model for a decision rather than either deciding alone or being fully upgraded — a middle path between model tiers.
- **Escalation to humans, too.** Architecture-altering or irreversible decisions route up to the human gate, not just to a bigger model.
- **Reported effect:** advisor mode reduced escalation frequency after rollout (directional, unmeasured) — i.e. consulting up-front avoided downstream rework.
- **Needs explicit triggers.** The gate only works if "high-stakes" / "architecture-altering" are defined; vague triggers either over-escalate (cost) or under-escalate (quality).

## Related Concepts

- [[concepts/infrastructure-dev/agent-cost-control|Agent Cost Control]] — escalation gating is a primary cost-control mechanism.
- [[concepts/ai-agents/model-neutrality|Model Neutrality]] — being able to swap model tiers cleanly is what makes gating practical.
- [[concepts/ai-agents/criteria-driven-ai-adoption|Criteria-Driven AI Adoption]] — the gate is a specific adoption criterion for *when* to spend more.
- [[concepts/ux-research/human-in-the-loop|Human-in-the-Loop]] — the top tier of escalation is human judgment.
- [[concepts/ai-agents/harness-engineering|Harness Engineering]] — the gate is part of the surrounding scaffold, not the prompt.
- [[concepts/ai-agents/multi-agent-architecture|Multi-Agent Architecture]] — escalation across agents/models is a coordination pattern.

## Conflicts & Caveats

> [!warning] Protocol overhead
> The gate adds complexity (deciding when/whom to escalate). For small teams or simple tasks, that orchestration overhead may exceed the model-cost savings — sometimes just using the strong model is cheaper end-to-end. Effect claims are qualitative.

## Sources

- [[sources/heyratel-ios-ai-agent-environment|Jinyoo / HeyRatel (2026): Not a Tool but a Standard]]

## Open Questions

- What concrete signals should trigger escalation, and can they be detected automatically?
- At what team size / task complexity does a gate stop paying for its overhead?
- How do you keep a cheap model from *failing to recognize* that a decision is high-stakes (the meta-judgment problem)?
