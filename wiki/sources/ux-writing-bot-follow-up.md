---
type: source
status: active
created: 2026-07-27
updated: 2026-07-27
tags: [source, ux-writing, documentation, ai, retrieval]
sources:
  - raw/web/2026-07-27-ux-writing-bot-follow-up.md
confidence: 0.75
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
---

# UX라이팅봇 후속편 - 잘 쓴 문서가 AI한테 스킵당하는 이유

## Citation

Product Makers Note, “[21호] UX라이팅봇 후속편 - 잘 쓴 문서가 AI한테 스킵당하는 이유,” Maily, retrieved 2026-07-27. [Original article](https://maily.so/makersnote/posts/xyow3pw9r28)

## Source Type

Practitioner newsletter case report about AI-readable reference documentation.

## Location

`raw/web/2026-07-27-ux-writing-bot-follow-up.md`

## Summary

The follow-up examines why a human-quality reference document can still be skipped by an AI writing assistant. It reframes documentation quality as a combination of clarity, structure, retrievability, and operational boundaries.

## Key Claims

- Human readability does not guarantee machine usability.
- Reference documents need explicit structure and retrieval cues.
- Fixing the knowledge layer can outperform adding more prompt instructions.

## Useful Examples

- Separate rules, examples, exceptions, and decision boundaries.
- Make the right reference easy to select at the moment of generation.

## Constraints / Caveats

This is an experience report, not a controlled retrieval evaluation.

## Design Implications

Treat AI-facing documentation as an interface: predictable structure, scoped rules, examples, and feedback loops should be designed deliberately.

## Tensions

More structure improves retrieval but can make documents harder for humans to browse if the information architecture is over-engineered.

## Open Questions

- Which document structures consistently improve retrieval and rule application?
- How should reference content be tested as it evolves?

## Concepts Linked

- [[concepts/infrastructure-dev/ai-readable-documentation|AI-Readable Documentation]]
- [[concepts/infrastructure-dev/design-md|Design.md as Context Infrastructure]]

## LLM Use

Use this source when designing style guides, design specs, and reference docs for AI agents. Ask for a retrieval test and a rule-application test, not only a prose review.

## Reliability Notes

The source supports workflow hypotheses and practical documentation patterns; performance claims require local testing.

## Backfill Status

New source page created from the resolved Maily page.

