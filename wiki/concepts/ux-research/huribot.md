---
type: concept
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [ux-research, ai-assistant, usability-testing, toss, fintech, design-tools]
sources:
  - sources/toss-tech-research-platform-ai
confidence: 0.95
---

# Huribot

## Summary

Huribot is an AI usability assistant developed by Toss (the Korean fintech super-app) that enables designers to conduct rapid lightweight usability checks by uploading screen images and asking questions. It returns feedback in seconds rather than the ~1 hour required to set up a traditional user testing session.

## Why It Matters

Huribot is a concrete, production example of AI-assisted usability testing deployed at a major consumer product company. It addresses a well-documented barrier: designers frequently skip small, informal usability checks because the overhead of even lightweight testing is too high. By collapsing that overhead to near zero, Huribot changes when and how often usability questions get asked.

## Key Claims

- Reduces usability check time from ~1 hour (minimum UT setup) to seconds for lightweight questions.
- Trained on Toss-specific user data ??not a generic foundation model; responses reflect actual Toss user behavior patterns.
- Positioned as a **"check" tool**, not a replacement for formal user research. Formal UT is reserved for deeper validation.
- Catches issues such as misleading graphics, dark patterns, and unclear messaging during early design iteration.
- Operated via image upload + natural language question ??generated response.

## Development Approach

Toss used a **three-phase prompting workflow** to build Huribot:

| Phase | Focus |
|---|---|
| Pre-Prompting | Narrow the problem; define goals; build team consensus on AI's role |
| During Prompting | Validate value with a lightweight chatbot prototype and real designer users; iterate prompts on real usage |
| Post-Prompting | Define MVP features; finalize: image upload, question input, response generation |

## Related Concepts

- [[concepts/ux-research/automated-ut-setup|Automated UT Setup]]
- [[concepts/ux-research/ux-research-automation|UX Research Automation]]
- [[concepts/ux-research/ai-usability-analysis|AI Usability Analysis]]
- [[concepts/ux-research/design-research-automation|Design Research Automation]]
- [[concepts/ux-research/human-in-the-loop|Human-in-the-loop]]
- [[concepts/ai-agents/athena-mcp|Athena MCP]] ??parallel example from Bucketplace; also reduces UT setup overhead

## Sources

- [[sources/toss-tech-research-platform-ai|Toss Tech: Huribot Story #1]]

## Open Questions

- Does Huribot's proprietary training on Toss data generalize as a pattern? How would other companies build equivalent tooling?
- How does Toss measure whether Huribot's usability judgments are reliable (calibration against formal UT results)?
- Will there be a "Huribot Story #2" with quantitative outcome data?

