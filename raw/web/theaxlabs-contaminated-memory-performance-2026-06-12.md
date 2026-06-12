# Source Card: AX LABS - Contaminated Memory Eats Away Performance

URL: https://theaxlabs.com/blog/%EC%98%A4%EC%97%BC%EB%90%9C-%EA%B8%B0%EC%96%B5%EC%9D%80-%EC%84%B1%EA%B3%BC%EB%A5%BC-%EA%B0%89%EC%95%84%EB%A8%B9%EB%8A%94%EB%8B%A4

Retrieved: 2026-06-12

Source type: AI agent operations article

Publisher: AX LABS

Author: AX LABS

Published: 2026-06-08

Original title: 오염된 기억은 성과를 갉아먹는다

English working title: Contaminated Memory Eats Away Performance

Extractor notes:

- Defuddle succeeded locally on 2026-06-12.
- The original article is Korean. This card preserves metadata, links, and an AI-written English summary rather than reproducing the full article text.
- Web verification confirmed the page title, publication metadata, and core claims on 2026-06-12.

## Summary

The article argues that agent memory quality should be evaluated as a lifecycle problem, not as a simple retrieval-rate problem. In demos, memory looks useful because the agent recognizes past conversations, preferences, and repeated instructions. In production, memory can become contaminated when wrong summaries, old exceptions, or the agent's own unsupported inferences are written into long-term memory and later reused as if they were facts.

The article frames recall quality as resistance to contamination. Useful memory systems must track how memory is searched, injected into context, used in answers and tool calls, and updated or deleted after execution.

## Extracted Claims

- Memory evaluation should inspect the path from memory retrieval to context injection, use, and update, not just the final answer.
- Agent memory should retrieve only contextually appropriate memories and discard stale ones.
- Memory contamination often begins at write time when transient reasoning or unsupported summaries are promoted into durable memory.
- Evaluation leakage, solution contamination, and grader gaming are useful analogies for memory contamination.
- Memory write gates should distinguish user statements, system records, and agent inference.
- Memory promotion criteria should separate one-off conversation facts from repeated operational rules.
- Conflict handling should record whether a new memory replaces, coexists with, or invalidates an older memory.
- Drift can hide behind average recall scores; replay tests should compare empty memory vs. real memory, inject known contamination candidates, alter time order, and use canary memories.
- Memory debugging should find which retrieved memory and which constraint made the failure unrecoverable.
- Trace, tool call, state, and memory-update logs are necessary for reliable memory evaluation.

## Referenced Sources

- Hu et al., Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions: https://arxiv.org/abs/2507.05257
- NIST CAISI, Cheating On AI Agent Evaluations: https://www.nist.gov/blogs/caisi-research-blog/cheating-ai-agent-evaluations
- Microsoft Research, AgentRx framework: https://www.microsoft.com/en-us/research/blog/systematic-debugging-for-ai-agents-introducing-the-agentrx-framework/
- OpenAI trace grading documentation: https://developers.openai.com/api/docs/guides/trace-grading
- LangChain, Evaluating Deep Agents: https://www.langchain.com/blog/evaluating-deep-agents-our-learnings
- Microsoft Foundry memory article: https://devblogs.microsoft.com/foundry/introducing-memory-in-foundry-agent-service/

