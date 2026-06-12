---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.66
---

# How should agent actions be attributed when both human and agent contribute to the same artifact?

## Short Answer
The wiki evidence supports a layered attribution model: the human retains authorship and accountability for the artifact's purpose, claims, and decisions; the agent is logged as a contributor for the operations it performed (drafts, links, edits). In practice, commit history (Git) or an audit log records agent actions, while the human sign-off marks which version is the authoritative one.

## Evidence
- [[concepts/ai-agents/agent-identity|Agent Identity]] — "Agent identity supports traceability and permission management. Long-running design or research agents need scoped access rather than broad ambient access. Identity works with logging, review, and policy enforcement."
- [[concepts/infrastructure-dev/cloud-ai-governance|Cloud AI Governance]] — "Identity, logging, encryption, access control, and procurement workflows affect production readiness." Logging is the operational mechanism for attribution.
- [[concepts/infrastructure-dev/enterprise-ai-agent-platform|Enterprise AI Agent Platform]] — "Design teams may use these platforms to connect research, feedback, design systems, and implementation workflows." Enterprise platforms model this as tracked agent sessions with human approval gates.
- [[concepts/ux-research/research-ethics|Research Ethics]] — "Researcher accountability remains necessary when AI is involved." The human's accountability is preserved through sign-off, not by hiding the agent's contribution.

## Follow-up Sources Needed
- Established legal or organizational standards for AI contribution attribution in professional deliverables.
- Whether Git commit co-authorship metadata (e.g., `Co-Authored-By`) is sufficient for agent attribution in design artifacts.
