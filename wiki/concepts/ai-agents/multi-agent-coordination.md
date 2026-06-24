---
type: concept
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [concept, multi-agent, collaboration, coordination-gap, social-intelligence, evaluation]
sources: [hai-cooperbench-agent-teamwork]
confidence: 0.8
---

# Multi-Agent Coordination

> [!abstract] Summary
> The (currently weak) ability of multiple AI agents to collaborate on shared work. Evidence from CooperBench shows social/coordination intelligence — not coding skill — is the bottleneck.

> [!important] Why it Matters
> Much of the agentic-product vision assumes agents teaming up with each other and with humans. If two agents perform *worse* than one, that vision needs a different training and verification strategy, not just better models.

## 📝 Key Claims
- The "coordination gap" / "curse of coordination": today's best coding agents lose nearly half their capability when paired to share work.
- Giving agents a real-time channel to message each other had almost no effect — fluency masked failures rather than resolving them.
- Failures are social: ignoring a teammate's warning, overwriting their code, low-value status updates, unanswered questions, broken promises.
- A core confusion is spatial vs semantic coordination — *where* in the code to edit vs *what* to edit.
- Fix path: train agents for coordination and add verification (commitments/contracts, periodic integration checks), not just better prompts.

## 🔗 Related Concepts
- [[concepts/agent-experience/collaboration-patterns|Collaboration Patterns]]
- [[concepts/ai-agents/orchestrator-of-agents|Orchestrator of Agents]]
- [[concepts/ai-agents/managed-ai-agents|Managed AI Agents]]
- [[concepts/ai-agents/autonomous-ai-agent|Autonomous AI Agent]]
- [[concepts/agent-experience/trust-calibration|Trust Calibration]]

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> Single-orchestrator designs may currently outperform peer multi-agent designs for conflict-prone work. Evidence is a not-yet-peer-reviewed preprint (CooperBench).

## 📚 Sources
- [[sources/hai-cooperbench-agent-teamwork|HAI: AI Coding Agents Fail at Teamwork (CooperBench)]]

## ❓ Open Questions
- What training objectives actually teach coordination rather than coding skill?
- Do verification/contract mechanisms close the coordination gap in practice?
