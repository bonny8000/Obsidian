---
type: concept
status: active
created: 2026-05-18
updated: 2026-05-18
tags: [ai-agent, identity, governance, security]
sources:
  - sources/brunch-ghidesigner-472
confidence: 0.66
---

# Agent Identity

## Summary

Agent identity is the practice of giving an AI agent a distinct, auditable identity that can be granted permissions, tracked in logs, and governed separately from human users.

## Why It Matters

Agents that edit files, access tools, or retrieve sensitive information need accountability. A distinct identity helps organizations know what an agent did, under whose authorization, and with which permissions.

## Key Claims

- Agent identity supports traceability and permission management.
- Long-running design or research agents need scoped access rather than broad ambient access.
- Identity works with logging, review, and policy enforcement.

## Related Concepts

- [[concepts/infrastructure-dev/enterprise-ai-agent-platform|Enterprise AI Agent Platform]]
- [[concepts/infrastructure-dev/cloud-ai-governance|Cloud AI Governance]]
- [[concepts/ai-agents/managed-ai-agents|Managed AI Agents]]

## Sources

- [[sources/brunch-ghidesigner-472|Brunch: Google Gemini Enterprise for UXUI Design]]

## Open Questions

- [Answered → [[queries/2026-05-27-agent-attribution-shared-artifact|Query Page]]] How should agent actions be attributed when both human and agent contribute to the same artifact?

