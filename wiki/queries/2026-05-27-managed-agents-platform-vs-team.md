---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.66
---

# What should be managed by the platform versus controlled by the team?

## Short Answer
The platform should manage: identity, authentication, logging, data encryption, compute, model routing, and compliance boundaries. The team should control: agent instructions (prompts, skills), task scope, tool permissions per agent, review gates, and which outputs are trusted without human sign-off. This split preserves organizational governance while keeping operational flexibility in the team's hands.

## Evidence
- [[concepts/ai-agents/managed-ai-agents|Managed AI Agents]] — "Managed agents reduce the burden of assembling runtime components manually. Enterprise teams may prefer managed agents when sensitive data and compliance are involved."
- [[concepts/ai-agents/agent-identity|Agent Identity]] — "Agent identity supports traceability and permission management. Long-running design or research agents need scoped access rather than broad ambient access."
- [[concepts/infrastructure-dev/enterprise-ai-agent-platform|Enterprise AI Agent Platform]] — "Enterprise agent platforms are framed as a move from experimentation to production operations."
- [[concepts/infrastructure-dev/cloud-ai-governance|Cloud AI Governance]] — "Identity, logging, encryption, access control, and procurement workflows affect production readiness." These are the platform layer items.

## Follow-up Sources Needed
- Enterprise AI agent platform documentation from Google Vertex, Amazon Bedrock, or Microsoft Azure AI Studio on the platform-vs-team control boundary.
