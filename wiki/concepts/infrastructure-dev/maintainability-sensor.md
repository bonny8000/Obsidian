---
type: concept
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [concept, maintainability, sensors, static-analysis, coding-agents, internal-quality]
sources: [fowler-sensors-coding-agents]
confidence: 0.85
---

# Maintainability Sensor

> [!abstract] Summary
> A feedback signal — computational (deterministic) or inferential (LLM-based) — that monitors the internal quality of an AI-generated codebase and lets the agent self-correct before issues reach human eyes.

> [!important] Why it Matters
> Internal-quality problems hurt agents the way they hurt humans: an agent in a tangled codebase looks in the wrong place, duplicates code, or loads more context than a task needs. Without sensors plus review, agents compound inadvertent technical debt.

## 📝 Key Claims
- Two families: computational sensors (type checker, ESLint, dependency rules, tests, mutation testing) and inferential sensors (LLM modularity/security/data-handling reviews).
- Computational sensors shine at the file/function level; cross-file modularity and coupling need an inferential sensor to add semantic interpretation and weigh trade-offs.
- Embed self-correction guidance in the sensor's error message (a "good kind of prompt injection") so the agent can fix or justifiably suppress a warning.
- Coding agents make a clean static-analysis baseline newly feasible (cheap custom rules; reviewable, reasoned suppressions).
- Risks: false sense of security, sensor conflicts (e.g., max-lines pushing complexity into prop chains), and feedback overload spiraling into over-refactoring.

## 🔗 Related Concepts
- [[concepts/ai-agents/harness-engineering|Harness Engineering]]
- [[concepts/ai-agents/model-harness|Model Harness]]
- [[concepts/infrastructure-dev/agentic-technical-debt|Agentic Technical Debt]]
- [[concepts/infrastructure-dev/mutation-testing|Mutation Testing]]
- [[concepts/infrastructure-dev/knowledge-linting|Knowledge Linting]]

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> Static-analysis has historically been underused because of management overhead and its limits on semantic quality; sensors are not a substitute for human review or coupling expertise.

## 📚 Sources
- [[sources/fowler-sensors-coding-agents|Böckeler (2026): Maintainability Sensors for Coding Agents]]

## ❓ Open Questions
- How should guides and sensors be balanced — once sensors are trusted, which guides can be deleted?
- Can inferential reviews run on just the changed files, earlier in the pipeline?
