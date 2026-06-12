---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.70
---

# What is the right release cadence for Bonny's own wiki automation experiments?

## Short Answer
Run automation experiments on a one-week cadence: ship a small automation change, use it daily for a week, then decide whether to keep, adjust, or remove it before shipping the next one. This prevents automation debt from accumulating and keeps the feedback loop short. The Cat Wu source's principle??a prototype that is never used daily creates little leverage"?ets the bar: an experiment that is not used daily within two weeks should be paused.

## Evidence
- [[concepts/product-management/shipping-velocity|Shipping Velocity]] ??"AI product timelines can shrink from months to weeks or days. Velocity should be paired with user feedback loops and quality checks, not treated as output volume alone."
- [[concepts/ai-agents/agentic-work-automation|Agentic Work Automation]] ??"The goal is to push workflows toward trustable, repeatable execution with clear verification. A prototype that is never used daily creates little leverage."
- [[concepts/product-management/research-preview|Research Preview]] ??"Research Preview can lower internal friction by reducing the perceived cost of shipping. It works best when paired with fast iteration and clear communication." Treating wiki automation experiments as personal research previews is the right framing.
- [[sources/lennys-podcast-cat-wu-ai-pm-claude-code|Lenny's Podcast: Cat Wu on AI-Native PM]] ??"Define the current user task, ship quickly, collect feedback, and keep adjusting the product as model behavior changes."

## Follow-up Sources Needed
- A log template for recording per-week automation experiment outcomes in the wiki.

