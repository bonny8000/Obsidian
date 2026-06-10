---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.72
---

# What feedback from each wiki ingest should be saved as a rule for the next ingest?

## Short Answer
After each ingest, four types of feedback are worth saving as rules: (1) bad links or missing concept pages that the agent created without evidence; (2) concepts that were silently merged or split incorrectly; (3) source claims that were misclassified with too-high confidence; and (4) successful relationship patterns between concepts that should be repeated. These map to the harness review cycle described in the Cat Wu source.

## Evidence
- [[concepts/ai-agents/self-improving-agent-workflowsSelf-Improving Agent Workflows]] ??"Feedback should be incorporated into future runs so the same mistake does not recur. Self-improvement depends on durable memory, skills, evals, or explicit process updates."
- [[concepts/ai-agents/model-harnessModel Harness]] ??"Harness features can compensate for current model weaknesses. New model launches should trigger a review of system prompts and product crutches." Ingest rules are a harness artifact.
- [[concepts/ai-agents/model-introspectionModel Introspection]] ??"Asking the model why it made a mistake can reveal likely friction in the harness. Introspection helps identify whether failures came from prompts, tools, delegation, or missing verification."
- [[concepts/infrastructure-dev/knowledge-lintingKnowledge Linting]] ??Linting after ingest can surface structural failures (orphan pages, broken links) that become the rule candidates.

## Follow-up Sources Needed
- A concrete rule-log format and where to store it (AGENTS.md, a separate log, or a dedicated rules concept page).

