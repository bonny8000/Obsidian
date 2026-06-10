---
type: concept
status: active
created: 2026-06-10
updated: 2026-06-10
tags: [concept, statistics, quant-ux, formative-research]
sources: [sauro-lewis-quantifying-ux-2016]
confidence: 0.9
---

# Problem Discovery Model

## Summary

The probabilistic model behind formative usability testing: the chance of seeing a problem at least once in n sessions is 1 − (1 − p)ⁿ. History: Chapanis/Al-Awar (1981) small-iteration testing → Virzi (1990/92) and Nielsen & Landauer (1993) Monte Carlo studies (p averaged 0.31–0.37) → Nielsen's popularized "5 users" rule.

## Why it matters

This model is the quantitative backbone for deciding when to stop testing and when to iterate — and it transfers to any defect-discovery context (heuristic evaluation, [[concepts/ux-research/ai-usability-analysis|AI usability analysis]], even agent eval runs).

## Key claims

- Discovery likelihood depends jointly on p and n; quoting n alone ("we tested 5 users") says nothing without an assumption about p. (conf 0.95)
- Published p values vary 0.12–0.58 across studies — discovery rates are study- and product-specific. (conf 0.9)
- Iteration beats raw n: fixing high-p problems early raises effective discovery of later rounds. (conf 0.85)

## Related concepts

- [[concepts/ux-research/sample-size-for-usability-studies|Sample Size for Usability Studies]]
- [[concepts/ux-research/evaluator-effect|Evaluator Effect]]
- [[concepts/ux-research/any-2-agreement|Any-2 Agreement]]

## Sources

- [[sources/sauro-lewis-quantifying-ux-2016|Sauro & Lewis (2016)]], ch. 7.

## Open questions

- Can the same model size AI-eval runs (how many eval cases to catch x% of failure modes at rate p)?
