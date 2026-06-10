---
type: concept
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [ai-agent, optimization, llm, skill-system, research, self-improvement]
sources:
  - sources/arxiv-2605-23904
confidence: 0.88
---

# Text-Space Optimization

## Summary

Text-space optimization is the idea of treating natural-language documents ??such as agent skill instructions, prompts, or process descriptions ??as learnable parameters that can be improved via a systematic optimization process, analogous to how neural network weights are updated in parameter-space during gradient descent.

## Why It Matters

Most LLM-based systems treat text documents as static configuration. Text-space optimization reframes them as dynamic objects that can be trained. This opens a new category of meta-learning: instead of improving model weights (which requires retraining), you improve the external knowledge and instructions the model operates on. Since document updates have zero inference-time overhead, this can be more practical than fine-tuning for many applications.

## Key Claims

- The framing of "text documents as external weights" draws a direct analogy between weight-space optimization (gradient descent) and text-space optimization (bounded edit proposals from a meta-model).
- Effective text-space optimizers need analogues to core deep-learning concepts: learning rate (edit aggressiveness), epochs (update rounds), and validation sets (gatekeeping).
- Rejected-edit storage prevents the optimizer from wasting compute re-trying ineffective changes ??analogous to momentum or adaptive learning rate mechanisms.
- At deployment, optimized text documents are plain text: no runtime cost difference from hand-crafted equivalents.
- SkillOpt is the concrete instantiation of this concept in the agent-skills domain (see [[concepts/ai-agents/skillopt|SkillOpt]]).

## Analogy Table

| Deep-Learning Concept | Text-Space Equivalent |
|---|---|
| Model weights | Skill / prompt document content |
| Gradient | Scored rollout failure signal |
| Optimizer (Adam, SGD) | Optimizer LLM (proposes text edits) |
| Learning rate | Textual edit-aggressiveness budget |
| Training epoch | Optimization round over rollout batch |
| Validation loss | Held-out test score gate |
| Weight-space regularization | Edit boundedness constraints (add/delete/replace only) |

## Scope

Text-space optimization applies wherever:
1. An external text document controls agent behavior (skills, system prompts, playbooks, wiki pages).
2. There is a measurable performance signal (task success, score, human rating).
3. The document can be iteratively revised without redeploying model weights.

## Related Concepts

- [[concepts/ai-agents/skillopt|SkillOpt]]
- [[concepts/ai-agents/skill-system|Skill System]]
- [[concepts/ai-agents/self-improving-agent-workflows|Self-Improving Agent Workflows]]
- [[concepts/ai-agents/agent-memory|Agent Memory]]
- [[concepts/ai-agents/product-evals|Product Evals]]
- [[concepts/product-management/compounding-knowledge|Compounding Knowledge]]

## Sources

- [[sources/arxiv-2605-23904|arXiv 2605.23904: SkillOpt]]

## Open Questions

- Is text-space optimization applicable to wiki maintenance instructions (like this vault's AGENTS.md)? Could the ingest workflow itself be SkillOpt-optimized?
- What are the failure modes when the edit-proposing optimizer model is misaligned with the true objective?
- How does this relate to prompt-engineering as a field ??is text-space optimization just rigorous automated prompt engineering?

