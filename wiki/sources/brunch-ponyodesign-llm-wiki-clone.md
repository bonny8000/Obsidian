---
type: source
status: active
created: 2026-06-26
updated: 2026-06-26
tags: [llm-wiki, ai-maintained-wiki, personal-knowledge-management, obsidian, agent-memory, context-engineering, second-brain, note-taking, first-person-account]
source_path: raw/web/brunch-ponyodesign-llm-wiki-clone-2026-06-26.md
source_url: https://brunch.co.kr/@ponyodesign/16
authors: [ponyodesign]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
confidence: 0.75
raw_preserved: true
---

# ponyodesign (2026): I Created a Clone of Myself That Knows Me Best

**Author:** ponyodesign (a designer, writing from professional design practice) — Brunch (brunch.co.kr), 2026-06-10.
**Raw capture:** [[raw/web/brunch-ponyodesign-llm-wiki-clone-2026-06-26|brunch-ponyodesign-llm-wiki-clone-2026-06-26]]
**URL:** [brunch.co.kr/@ponyodesign/16](https://brunch.co.kr/@ponyodesign/16)

## Citation

ponyodesign. (2026, June 10). *I Created a Clone of Myself That Knows Me Best* (나를 가장 잘 아는 분신을 만들었다). Brunch. https://brunch.co.kr/@ponyodesign/16. Captured 2026-06-26 into raw/web/brunch-ponyodesign-llm-wiki-clone-2026-06-26.md.

## Summary

A first-person account by a working designer of building an "LLM Wiki" — a persistent external memory that lets an AI act as a clone of its owner. The trigger was the recurring tax of re-explaining context to AI across sessions and the fear of forgetting *why* past decisions were made. The author's solution was to migrate three years of notes (Notion, meeting records, ideation) into Obsidian markdown and bulk-upload the whole history to the AI. The central, deliberately anticlimactic claim is that the clone emerged not from an elaborate system but from sustained low-friction note-taking: "Grand systems didn't create the clone. Lazy note-taking did." The resulting assistant references past decisions, flags circular thinking, and maintains a consistent narrative — which the author finds "slightly terrifying but reassuring." This source is notable because its governing analogy — *Obsidian is the IDE, AI is the programmer, the wiki is the codebase* — is the same premise on which this very LLM-Wiki vault operates.

## Key Claims

- **Consistency beats sophistication:** the clone came from *lazy*, sustained note-taking over three years, not from a grand system. Friction and overhead are framed as the primary reason knowledge systems fail.
- **External memory is the unlock:** the value is not a smarter model but an accumulated, portable record the model can read — the **wiki is the persistent context layer**.
- **Plain-text, local-first, lightweight linking** is what made a 3-year commitment survivable; database overhead would have killed adoption.
- **Division of labor:** the **human only captures**; the AI extracts patterns, links, and summarizes. Structuring is automated, capture is manual.
- **AI as a continuity guard, not just a generator:** the clone catches **circular thinking** ("you thought this way last year too") and reinforces prior decisions, providing narrative consistency across time.
- **Bulk-upload bootstrapping:** the entire history was fed to the AI in one pass, and a "summarize everything you know about me, export as markdown" prompt was used to consolidate the AI's understanding back into the vault.
- **Self-mirroring framing:** the **IDE / programmer / codebase analogy** treats personal knowledge work as a software-engineering loop — the same architecture this vault is built on.

## Useful Examples

- **Bootstrapping prompt:** "Summarize everything you know about me so far, export as markdown" — used to crystallize accumulated AI context into a durable vault artifact.
- **Meeting loop:** meeting → transcript → AI summarization → Obsidian archive → context for the *next* meeting, so the next meeting starts from accumulated ground instead of re-explaining.
- **Migration path:** ~3 years of Notion notes, meeting records, and ideation docs consolidated into Obsidian markdown, then bulk-uploaded.
- **Tool stack:** Obsidian (storage + linking), Claude (clone/reasoning + consistency check), GPT (summarization/retrieval).
- **Governing analogy:** "Obsidian is the IDE, AI is the programmer, the wiki is the codebase."

## Constraints / Caveats

- **Single-source, qualitative, first-person blog post** — no metrics, no code, no folder structure, no evaluation. Treat as an experience report and design inspiration, not evidence.
- **Korean-language personal Brunch blog**; fetched fully, but persuasive/narrative framing means claims (e.g., "remembers better than I do") are subjective, not measured.
- **Mechanism is under-specified:** the post implies a one-time bulk upload but does not describe an ongoing retrieval/indexing mechanism, so it is unclear whether "clone" behavior survives context-window limits or requires re-upload per session.
- **Survivorship framing:** "lazy note-taking is enough" is the author's retrospective read of a *successful* 3-year habit; it under-counts the discipline of capturing consistently at all.

## Design Implications

- Validates the core bet of [[concepts/infrastructure-dev/llm-wiki|LLM Wiki]] from an independent practitioner: a portable plain-text vault is a stronger lever than a cleverer model, because it is the **persistent context** the model reads.
- Supports an [[concepts/ai-agents/ai-maintained-wiki|AI-Maintained Wiki]] division of labor — human captures, agent structures/links/summarizes — as the way to keep a [[concepts/ai-agents/1-person-vault|1-Person Vault]] alive without overhead killing the habit.
- The 3-year arc is a concrete instance of [[concepts/product-management/compounding-knowledge|Compounding Knowledge]]: value accrues from sustained low-friction capture, and the AI's recall eventually exceeds the human's.
- Reframes the vault as durable [[concepts/ai-agents/agent-memory|Agent Memory]] and the bulk-upload-plus-summarize move as [[concepts/ai-agents/context-engineering|Context Engineering]]: bootstrapping a model's working understanding of a person from an accumulated record.
- Practical takeaway for Bonny's own LLM-Wiki: minimize capture friction first; let the agent own structuring; treat the AI as a consistency guard against revisiting settled decisions.

## Tensions

- **Friction-free vs. structured:** "lazy note-taking is enough" sits in tension with this vault's house style (strict frontmatter, honest coverage/confidence, concept linking). The author optimizes capture; an [[concepts/ai-agents/ai-maintained-wiki|AI-Maintained Wiki]] pushes structure onto the agent — both can be true, but the boundary of who structures what is the live design question.
- **Consistency guard vs. creative drift:** an AI that reinforces past decisions and flags "you thought this last year" can entrench a position as easily as it prevents thrash — the same mechanism that gives continuity can resist needed change.
- **Bulk upload vs. retrieval:** dumping a whole history into context conflicts with disciplined [[concepts/ai-agents/context-engineering|Context Engineering]] (curate what the model sees); cheap context windows make bulk-upload viable today but may not scale or stay reliable.

## Open Questions

- Does the "clone" behavior persist across sessions and model changes, or does it depend on re-uploading the vault each time?
- At what vault size does bulk upload break down, and when does selective retrieval become necessary?
- How much of the success is the tooling vs. the rare discipline of capturing consistently for three years?
- Does an AI consistency guard measurably reduce wasted re-work, or mainly produce a *feeling* of continuity?

## Concepts Linked

- [[concepts/infrastructure-dev/llm-wiki|LLM Wiki]]
- [[concepts/ai-agents/ai-maintained-wiki|AI-Maintained Wiki]]
- [[concepts/ai-agents/1-person-vault|1-Person Vault]]
- [[concepts/product-management/compounding-knowledge|Compounding Knowledge]]
- [[concepts/ai-agents/agent-memory|Agent Memory]]
- [[concepts/ai-agents/context-engineering|Context Engineering]]

## LLM Use

- **Use for:** motivating the LLM-Wiki / personal-knowledge-vault pattern; the friction-vs-consistency argument; the human-captures / AI-structures division of labor; the "AI as consistency guard" and bulk-upload bootstrapping ideas; an independent practitioner echo of this vault's own thesis.
- **Do not use for:** any quantitative claim, implementation spec, retrieval architecture, or evaluation — there is none. Do not cite it as evidence that "lazy note-taking is sufficient"; it is one successful anecdote.
- **Best prompt pattern:** "Using ponyodesign's LLM-Wiki account, argue why minimizing capture friction and offloading structuring to an AI is the key to a sustainable personal knowledge vault — then list the failure modes (mechanism under-specified, survivorship, consistency-guard entrenchment)."

## Reliability Notes

> [!warning] Caveats
> Confidence 0.75: the source was fetched in full and the account is internally coherent and directly on-topic for this vault's premise, so the *ideas* are reliable to summarize. But it is a single qualitative first-person blog post with no metrics, code, or mechanism detail — treat every claim as experiential, not evidential, and note the survivorship bias in "lazy note-taking was enough."

## Backfill Status

- Coverage would rise if the author publishes implementation specifics (folder/linking conventions, automation scripts, how bulk upload is chunked, ongoing retrieval mechanism) — re-capture then.
- Confidence would rise if the "clone remembers better than I do" claim were corroborated by a second independent practitioner account or any measurement of re-work reduction.
