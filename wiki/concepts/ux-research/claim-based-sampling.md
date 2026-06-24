---
type: concept
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [concept, sampling, representativeness, selection-bias, validity, product-research]
sources: [bakhshi-representative-sample]
confidence: 0.85
---

# Claim-Based Sampling

> [!abstract] Summary
> A sample is not "representative" in the abstract — it is only more or less **adequate for a specific claim about a specific population**. Design the sample *backward from the claim* rather than matching the customer base on easy-to-quota demographics.

> [!important] Why it Matters
> Demographic representativeness is inherited from opinion polling, where demographics correlate with the outcome and population margins are known. In product research the outcomes (adoption, retention, willingness to pay, error recovery, trust after failure) are driven by behavioral/contextual variables — so a demographically "representative" sample can still be unrepresentative on what actually moves the result.

## 📝 Key Claims
- **Four claim types → four sampling logics:** *prevalence* (how common — don't select on the outcome), *existence* (does it happen — sample the tail, one case can suffice), *explanatory* (why — must include people who had the outcome, not survivors), *comparison* (group difference — recruit each group comparably).
- **Three failure modes:** balanced on the wrong variables; selected by the outcome (nonresponse/self-selection/survivorship); changing the claim after sampling (reading a detection study as a frequency study).
- More respondents reduce variance but **do not remove bias** — a larger self-selected sample is a precise number around the wrong answer.
- Track the layers: target population → sample frame → realized sample → respondents; every gap distorts a specific claim.

## 🔗 Related Concepts
- [[concepts/ux-research/participant-selection-criteria|Participant Selection Criteria]]
- [[concepts/ux-research/sample-size-for-usability-studies|Sample Size for Usability Studies]]
- [[concepts/ux-research/validity-and-decision-relevance|Validity and Decision Relevance]]
- [[concepts/ux-research/reliability-vs-validity|Reliability vs Validity]]
- [[concepts/ux-research/llm-user-proxy|LLM User Proxy]]
- [[concepts/ux-research/synthetic-survey-data|Synthetic Survey Data]]

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> Demographic quotas still matter for fairness, accessibility, regulated, or demographically-driven outcomes — the claim isn't "ignore demographics," it's "don't treat them as the default definition of representation."

## 📚 Sources
- [[sources/bakhshi-representative-sample|Bakhshi (2026): There Is No Such Thing as a Representative Sample]]

## ❓ Open Questions
- How to make "claim-first sampling" a lightweight team ritual?
- How to design recruitment when one study must support multiple claim types?
