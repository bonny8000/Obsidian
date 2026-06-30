---
type: concept
status: active
created: 2026-06-26
updated: 2026-06-26
tags: [criteria-driven-ai-adoption, ai-adoption, automation-boundary, harness-engineering, human-judgment-gates]
sources:
  - sources/heyratel-ios-ai-agent-environment
confidence: 0.75
---

# Criteria-Driven AI Adoption

## Summary

**Criteria-driven AI adoption** means deciding *what to automate and where to stop* from explicit, written-down decision criteria — not from tool availability or hype. The slogan from the HeyRatel iOS team: **"the standard chooses the tools, not the other way round."** Adoption starts from principles (what's worth automating, what must stay human) and only then selects the agents/skills/MCP servers that fit.

## Why It Matters

The default failure mode is tool-driven adoption: a team adopts an agent or MCP server because it's trendy, then discovers it automates the wrong things, bloats context, or quietly makes decisions that should have been human. Inverting the order — criteria first, tools second — keeps automation aimed at genuine, repeated waste and preserves human judgment where it matters. It is the governance layer that sits above [[concepts/ai-agents/harness-engineering|harness engineering]] and [[concepts/ai-agents/agent-skills|skills]].

## Key Claims

- **Standard over tool.** Derive automation scope from criteria; let the standard select the tool.
- **Validate inefficiency before automating.** Only automate proven, repeated pain points — not assumed ones.
- **Automate mechanical waste, never judgment.** Irreversible decisions (commits, merges, code review, approvals) stay human-gated; "automation targets mechanical waste, not judgment."
- **Composability as a criterion.** Prefer many narrow, single-responsibility skills over monolithic agents, because they're testable and recombinable.
- **Context as a budget.** "Keep context small and clean" is a first-class adoption criterion, since token cost scales ~linearly with context size — motivating distributed instruction files and tool-output compression.
- **Concrete dissent it licenses:** the team rejected MCP for token reasons and built custom skills — a criteria-driven *no* to a popular tool.

## Related Concepts

- [[concepts/ai-agents/harness-engineering|Harness Engineering]] — criteria-driven adoption is the policy layer that decides what the harness should contain.
- [[concepts/ai-agents/agent-skills|Agent Skills]] — the single-responsibility unit adoption decisions resolve to.
- [[concepts/ai-agents/model-escalation-gate|Model Escalation Gate]] — a specific criterion for *when* to spend a stronger model/human.
- [[concepts/infrastructure-dev/ai-adoption-culture|AI Adoption Culture]] — the org-enablement counterpart (how teams build capability); this concept is the per-decision discipline.
- [[concepts/infrastructure-dev/claudemd-context|CLAUDE.md / AGENTS.md Context]] — where the criteria get encoded as durable instructions.
- [[concepts/ai-agents/model-neutrality|Model Neutrality]] — keeping tools interchangeable so criteria, not lock-in, drive choice.

## Conflicts & Caveats

> [!warning] One team, qualitative
> A single practitioner blog with no metrics; "criteria first" is intuitive but its payoff is unmeasured here. Criteria can also ossify — what's "not worth automating" today may flip as tools improve, so the criteria themselves need revisiting.

## Sources

- [[sources/heyratel-ios-ai-agent-environment|Jinyoo / HeyRatel (2026): Not a Tool but a Standard]]

## Open Questions

- What's the minimal set of criteria a team should write down before adopting agents?
- How often should adoption criteria be re-evaluated as model/tool capability changes?
- Where does criteria-driven restraint tip into under-adoption (missing real leverage)?
