---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.66
---

# Which governance features are mandatory before design teams can use enterprise agents with sensitive research data?

## Short Answer
Mandatory governance features before using enterprise agents with sensitive UX research data are: (1) access control with participant data scoped to authorized team members only; (2) audit logging of every agent action that touches participant data; (3) data residency compliance (data stays in approved regions); (4) the ability to delete agent access to a dataset after a project ends; and (5) an incident response path for accidental data exposure.

## Evidence
- [[concepts/infrastructure-dev/enterprise-ai-agent-platform|Enterprise AI Agent Platform]] — "Agent workflows become higher-risk in enterprise contexts because they touch data, tools, permissions, and accountability."
- [[concepts/infrastructure-dev/cloud-ai-governance|Cloud AI Governance]] — "Identity, logging, encryption, access control, and procurement workflows affect production readiness."
- [[concepts/ux-research/research-ethics|Research Ethics]] — "Researcher accountability remains necessary when AI is involved." Participant data adds legal and ethical obligations beyond standard enterprise data.
- [[sources/brunch-ghidesigner-472|Brunch: Google Gemini Enterprise for UXUI Design]] — "Enterprise AI agent platforms can integrate research data, design systems, feedback, and workflows in a governed environment."

## Follow-up Sources Needed
- Specific GDPR, HIPAA, or IRB requirements that apply to AI-processed UX research participant data at the enterprise level.
