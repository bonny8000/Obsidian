---
type: concept
status: active
created: 2026-06-17
updated: 2026-06-17
tags: [context-engineering, context-rot, failure-modes, agent-reliability, token-budget]
sources:
  - sources/agent-skills-day-3
  - sources/the-new-sdlc-with-vibe-coding-day-1
confidence: 0.88
---

# Context Rot

> [!abstract] Summary
> Performance degradation that happens silently as the model's input context grows, even when task difficulty is held constant. The most common production failure mode of agents — and the failure mode Skills, progressive disclosure, and DAG orchestration are designed to defeat.

> [!important] Why it Matters
> Most teams plan around the *capacity* of their context window. Context Rot says capacity is the wrong metric: a 1M-token window can show significant degradation at 50K tokens. The active context is a budget, and every token in front of the model takes attention from every other. If you do not architect around this, you ship demos that work and production systems that quietly underperform.

## 📝 Key Claims

- **Context overflow, not hallucination, is the most common production failure mode** of agents.
- **Lost in the Middle (Liu et al., TACL 2024)** — across multi-document QA and retrieval, performance is highest when relevant information sits at the start or end of input and degrades in the middle. A U-curve that holds even for models trained on long contexts.
- **Context Rot (Chroma Research, 2025)** — across 18 frontier models (Claude 4 Opus and Sonnet, Gemini 2.5, Qwen3), performance degrades as input grows even when task difficulty is held constant. **All models get worse**, and faster when relevant content is hard to distinguish from distractors.
- **Real agent context is the worst case** — tool outputs, half-relevant retrievals, and intermediate reasoning are among the worst kinds of noise.
- **MCPVerse** observed an 18.2% accuracy drop in Claude-4-Sonnet due to tool proliferation and context attention competition.
- **Co-loading amplifies the problem.** Agents in production co-load 5–15 Skills simultaneously. A Skill body that works perfectly in isolation can cause context rot when co-loaded.

## Three practical implications

1. **Capacity is the wrong metric.** A 1M-token window does not buy you 1M tokens of usable context.
2. **Active context is a budget, not a vessel.** Treat the system prompt the way infra teams treat memory: a finite resource, allocated deliberately.
3. **Architectural answers, not "use a longer window."** [[concepts/ai-agents/progressive-disclosure|Progressive Disclosure]], a [[concepts/ai-agents/agent-skills|Skills]] library, DAG orchestration with a file message bus, and tight Capability Profiles all keep active context small while keeping available capability effectively unbounded.

## How to apply

- Never evaluate a Skill purely in isolation. Test it co-loaded with 5–15 frequently-active Skills.
- When a Skill body exceeds 5,000 tokens, treat that as a smell — split or move detail to `references/`.
- For multi-step orchestration, pass *file or schema references* between agents, not the raw text history. (DAG + File Message Bus.)
- For repeated runs, watch for *demo-to-prod* gap: production performance typically drops 20–30% vs offline pass@1 numbers (ReliabilityBench).
- For long-running conversations, plan for context flushing between Capability Profile switches — the orchestrator should unload stale variables before swapping the new profile in.

## 🔗 Related Concepts

- [[concepts/ai-agents/progressive-disclosure|Progressive Disclosure]] — the architectural answer.
- [[concepts/ai-agents/agent-skills|Agent Skills]]
- [[concepts/ai-agents/memory-contamination|Memory Contamination]] — a related failure mode where stale context becomes hidden state.
- [[concepts/infrastructure-dev/token-efficiency|Token Efficiency]]
- [[concepts/ai-agents/harness-engineering|Harness Engineering]]
- [[concepts/ai-agents/long-horizon-tasks|Long-Horizon Tasks]]

## ⚖️ Conflicts & Caveats

> [!warning] Cited but unverified
> "All 18 frontier models degrade" and the specific MCPVerse 18.2% figure rest on individual studies cited inside Day-3. Treat as directionally robust; pair with internal evaluation before using as a hard threshold.

## 📚 Sources

- [[sources/agent-skills-day-3|Singhal et al. (2026): Agent Skills (Day 3)]] — Section 5 unpacks Lost in the Middle and Chroma Context Rot.
- [[sources/the-new-sdlc-with-vibe-coding-day-1|Osmani et al. (2026): The New SDLC With Vibe Coding (Day 1)]] — earlier framing as a system-prompt scaling problem.
- Liu et al. "Lost in the Middle" (TACL 2024).
- Chroma Research, "Context Rot" (2025).

## ❓ Open Questions

- Where on the curve does Bonny's typical agent session sit? Is the working assumption "we have plenty of context" actually true on long ingest sessions?
- For Wiki ingest workflows, when is loading `wiki/overview.md` + a source page already enough vs over-loading the context?
- Which co-loaded combinations of Skills should be eval-tested as a *suite* rather than individually?
