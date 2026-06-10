---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.64
---

# How should design teams document infrastructure constraints in AI-enabled workflows?

## Short Answer
Design teams should document infrastructure constraints as part of the workflow specification, not as a separate IT document. For each AI-enabled design workflow, note: which data it accesses, where that data is processed (cloud region, on-premise), what the access control requirements are, and what fails or slows down when infrastructure limits are hit. This keeps infrastructure context visible to the people designing and using the workflow.

## Evidence
- [[concepts/infrastructure-dev/enterprise-ai-infrastructureEnterprise AI Infrastructure]] ??"Infrastructure choices affect which AI workflows design teams can safely use. Agentic AI adoption depends on infrastructure, not only model capability."
- [[concepts/infrastructure-dev/cloud-ai-governanceCloud AI Governance]] ??"Claims about cloud governance should be verified against official cloud provider documentation." Documentation is the mechanism for that verification.
- [[concepts/ai-agents/agent-identityAgent Identity]] ??"Long-running design or research agents need scoped access rather than broad ambient access." The scope needs to be written down somewhere the team can find it.
- [[sources/mashdigi-aws-openai-bedrock-codex|Mashdigi: AWS and OpenAI Bedrock Collaboration]] ??"Bedrock matters for design teams when AI workflows must operate inside enterprise security boundaries." Security boundaries are a documentation requirement.

## Follow-up Sources Needed
- A template for per-workflow infrastructure constraint cards suitable for design team wikis or Notion docs.

