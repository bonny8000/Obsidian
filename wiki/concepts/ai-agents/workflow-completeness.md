---
type: concept
status: active
created: 2026-07-28
updated: 2026-07-28
tags: [concept, ai-agent, definition-of-done, verification, vibe-coding, agentic-technical-debt, product-quality]
sources: [naver-d2-ai-hackathon-nstake]
confidence: 0.80
---

# Workflow Completeness

> [!abstract] Summary
> Completion measured by whether a user can finish their work end to end — not by whether the function, file, or feature exists. An agent will report a feature complete when the code is present and never wired into the flow where someone presses a button and sees a result. The correct definition of done is a **traversable path**, and the correct unit of quality is **flow completeness rather than feature count**.

> [!important] Why it Matters
> This is the failure mode that makes agent-generated work look finished and behave unfinished. [[wiki/sources/naver-d2-ai-hackathon-nstake|NStake's]] team hit it directly: functions and files existed, the agent described features as complete, and some were never connected to the user's path. Their correction generalizes past agents entirely — *"verify AI-generated code by actual execution results, not by its explanation."* The same team credits flow completeness, not feature count, for winning every evaluation round, human and LLM alike.

## 📝 Key Claims

- **Artifact existence is not evidence of completion.** A file, a function, and a model's report of success are all compatible with nothing working.
- **Define done as a traversable path.** NStake's test: login → confirm assigned entity → enter transaction → save → validate → review mismatch → disposition → state and report update. If any hop is missing, nothing is done.
- **Demo-visible features and work-finishing features are different sets.** Natural-language query, dashboards, and auto-generated reports demo well and do not finish anyone's job. Identifying the difference early is what reprioritized their build.
- **A surfaced problem the user cannot dispose of is not a feature.** Finding a mismatch without the ability to correct it or mark it "no issue" produces one more list to work, not a service. Every surface needs a disposition path.
- **Untraceable output cannot be used officially.** If a report figure cannot be traced to the transactions that produced it, it is unusable regardless of correctness.
- **The yardstick moves from count to completeness.** Their explicit shift: *"our standard moved from the number of features to the completeness of the workflow."* All features sharing one flow — enter → validate → judge → dispose → generate — is what they credit, not any single AI capability.
- **Verify by execution, not by explanation.** The agent's account of what it built is the least reliable evidence available about what it built.

## The completion test

For any agent-delivered feature, ask in order:

1. **Can a user reach it?** Is it wired into a real entry point, not only callable?
2. **Can they finish?** Does the path continue to a terminal state, or does it dead-end at a surfaced problem?
3. **Can they dispose of what it surfaces?** Correct it, dismiss it, or mark it resolved.
4. **Can the result be traced?** Does the output explain what produced it?
5. **Was this verified by running it**, not by reading the agent's summary?

Anything failing 1–4 is incomplete regardless of what exists in the repository. Anything only verified at step 5 by explanation is unverified.

## ⚖️ Conflicts & Caveats

> [!warning] Single source, prototype scale
> One six-hour hackathon project. The pattern is intuitive and matches wide practitioner experience, but there is no measurement here — no defect rate, no comparison against a feature-count-driven build.

> [!warning] The win is weak support
> NStake placed first in every round, but its own authors note score gaps among top teams were small and no single feature or document decided it. The ranking corroborates the flow-completeness thesis; it does not establish it.

> [!warning] Flow completeness can under-serve exploration
> Demanding a traversable path for everything discourages the throwaway prototype that exists to answer a question. The discipline belongs to work meant to be used, not to work meant to be learned from — a distinction the source does not draw because a hackathon collapses it.

> [!warning] Says nothing about how to detect this automatically
> Every check above is manual. Nothing in this wiki describes an automated test for "the feature exists but is unreachable," which is exactly the gap that makes the failure mode persistent.

## 🔗 Related Concepts

- [[wiki/concepts/ai-agents/rule-statistical-external-validation|Rule / Statistical / eXternal Validation]] — the sibling pattern; every validation class needs a disposition path, which is this concept applied to findings.
- [[wiki/concepts/infrastructure-dev/agentic-technical-debt|Agentic Technical Debt]] — unreachable generated code is a principal source of it.
- [[wiki/concepts/ai-agents/vibe-coding|Vibe Coding]] / [[wiki/concepts/ai-agents/vibe-coding-agent-evaluation|Vibe Coding Agent Evaluation]] — the practice this failure mode is endemic to.
- [[wiki/concepts/ai-agents/agent-verifiers|Agent Verifiers]] — independent verification instead of self-report.
- [[wiki/concepts/ai-agents/product-evals|Product Evals]]
- [[wiki/concepts/ux-research/decision-contract|Decision Contract]] — the research-side analogue: define what would count as finished before starting.
- [[wiki/concepts/infrastructure-dev/deterministic-ai-workflows|Deterministic AI Workflows]]
- [[wiki/concepts/product-management/shipping-velocity|Shipping Velocity]] — what feature-count thinking optimizes, and what this concept corrects.

## 📚 Sources

- [[wiki/sources/naver-d2-ai-hackathon-nstake|NAVER D2 (2026): What the Winning AI Hackathon Team Did *Not* Delegate to AI]] — sole source: the "feature exists vs. work gets done" distinction, the traversable-path definition, and the count-to-completeness shift.
- [[wiki/sources/b2b-admin-web-accessibility|rami_ (2026): Applying Web Accessibility to a B2B Admin Service]] — adjacent instance in measurement rather than code: an automated count reported 168 missing `alt` attributes where 6 existed, discovered only by opening the files. Verify by inspection, not by the tool's report.

## ❓ Open Questions

- Can "exists but unreachable" be detected automatically — by route coverage, entry-point analysis, or end-to-end test generation?
- Does flow-completeness discipline slow delivery enough to matter, or does it mostly reorder work?
- Where is the line between work that must be flow-complete and prototypes that legitimately should not be?
- Do LLM evaluators reliably reward flow completeness, or did NStake's first-place LLM ranking reflect documentation quality instead?
