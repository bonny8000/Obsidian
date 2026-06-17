---
type: concept
status: active
created: 2026-06-17
updated: 2026-06-17
tags: [agent-memory, procedural-memory, cognitive-typology, agent-skills]
sources:
  - sources/agent-skills-day-3
confidence: 0.85
---

# Procedural Memory

> [!abstract] Summary
> The "knowing how" complement to episodic memory ("what happened") and semantic memory ("facts"). LLM agents have had analogs for the latter two — conversation history and pre-training — but lacked a credible way to remember *how to do things step by step* until Agent Skills emerged as a procedural memory primitive.

> [!important] Why it Matters
> Treating Skills as procedural memory clarifies what they are *for* and what they *are not*. Skills are not facts to look up (semantic memory / RAG) or session state to recall (episodic memory / conversation history); they are workflows the agent re-runs. The procedural framing is what justifies versioning Skills, testing them like code, and pushing them through a Read/Draft/Act graduation ladder.

## 📝 Key Claims

- LLMs have **reasonable analogs for episodic memory** (conversation history, session logs) and **semantic memory** (pre-training, RAG).
- They have **lacked a procedural memory primitive** until Agent Skills emerged. Skills are the first credible candidate.
- Procedural memory is *how to do things step by step*, not what is true or what just happened.
- Procedural memory degrades differently from declarative knowledge: it benefits from repetition, verification gates, and incremental refinement (this is what makes the meta-skills loop and [[concepts/ai-agents/skillopt|SkillOpt]] possible).
- Procedural memory is *owned* in a way that declarative memory often is not — each skill has a named author, a versioned folder, and an accountable domain team. This solves a governance gap that hand-written system prompts left wide open.

## How to apply

- When a workflow is genuinely a *procedure* (steps, decisions, tools, output format), it deserves a Skill, not a longer system prompt or a RAG entry.
- When the information is *facts about the world* with no step-by-step structure, prefer RAG (semantic memory) or a wiki entry.
- When the content is *what happened in this session*, leave it in conversation history (episodic memory) or a session log.
- When a skill description starts to describe facts ("Stripe charges 2.9% + 30¢ per US card transaction…"), the facts probably belong in `references/`, not in the description or body.

## 🔗 Related Concepts

- [[concepts/ai-agents/agent-skills|Agent Skills]] — the format implementation of procedural memory for LLM agents.
- [[concepts/ai-agents/skill-system|Skill System]] — the broader pattern.
- [[concepts/ai-agents/skillopt|SkillOpt]] — text-space optimizer that treats Skills as trainable procedural memory.
- [[concepts/ai-agents/agent-memory|Agent Memory]] — the parent concept.
- [[concepts/ai-agents/memory-contamination|Memory Contamination]] — the parallel risk in declarative memory.
- [[concepts/ai-agents/self-improving-agent-workflows|Self-Improving Agent Workflows]] — meta-skills that improve procedural memory over time.

## ⚖️ Conflicts & Caveats

> [!warning] Framing, not cognitive science
> The "episodic / semantic / procedural" typology is borrowed from human memory literature (Tulving). It is useful framing for designing LLM agent systems but should not be read as a literal cognitive claim about LLMs.

## 📚 Sources

- [[sources/agent-skills-day-3|Singhal et al. (2026): Agent Skills (Day 3)]] — Section 1, framing Skills as procedural memory.

## ❓ Open Questions

- Does an LLM Wiki's `wiki/concepts/` cluster sit closer to semantic memory or to procedural memory in this typology? Or both, depending on how the page is structured?
- What is the analog for *meta-cognition* — knowing which procedural memory to invoke? Currently the description field plays that role; is there a better primitive?
