---
type: concept
status: active
created: 2026-05-25
updated: 2026-05-25
tags: [architecture, ai-native, infrastructure, ai-product-management]
sources: [sources/founders-playbook-2026]
confidence: 1.0
---

# 🏗️ AI-Native Stack

The **AI-Native Stack** is a three-layer architectural framework defined in [[sources/founders-playbook-2026|The Founder's Playbook (2026)]]. It distinguishes between startups that simply "add AI" and those that are "AI-first."

## The Three Layers
1. **Model Layer:** The choice between proprietary models (e.g., Claude, Gemini) and fine-tuned open-source alternatives. Focuses on capability, latency, and cost.
2. **Infrastructure Layer:** The "connective tissue" (like MCP, vector databases, and evaluation harnesses) that allows models to interact with data and tools.
3. **Application Layer:** The user-facing interface that leverages agentic capabilities to solve specific problems.

## Key Principles
- **Design for Agency:** The stack should support autonomous agents performing tasks, not just answering questions.
- **Data Flywheels:** Each layer should contribute to a feedback loop that improves the model's performance over time.
- **Interoperability:** Use of standards like [[concepts/ai-agents/mcp-integration|MCP]] to ensure the stack remains flexible.

## Related Concepts
- [[concepts/ux-research/designing-for-agency|Designing for Agency]]
- [[concepts/ai-agents/mcp-integration|MCP Integration]]
- [[concepts/ai-agents/agentic-ai|Agentic AI]]
