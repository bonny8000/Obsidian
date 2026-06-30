---
source_url: https://substack.com/@christinevallaure/note/p-191484683
captured: 2026-06-29
title: "A Human Approach to Agentic AI. One person. One text file. Five agents."
authors: [Christine Vallaure]
published: 2026-03-26
publisher: Christine Vallaure (Substack); also republished on UX Collective (uxdesign.cc)
---

# A Human Approach to Agentic AI. One person. One text file. Five agents.

**Author:** Christine Vallaure — UX designer & educator, founder of moonlearning.io ("UX for designers"); author of SOLO (solo product-building guidebook).

**Capture status:** Full via web_fetch. The Substack *note* URL (`/@christinevallaure/note/p-191484683`) 302-redirects to the article `https://christinevallaure.substack.com/p/a-human-approach-to-agentic-ai-one`; the article body was fetched there. Cross-checked against the UX Collective republication (`uxdesign.cc/a-human-approach-to-agentic-ai-one-person-one-text-file-five-agents-9e049fc0a612`) via WebSearch, which confirmed the thesis, the CLAUDE.md framing, and the "Rachel the Reader Advocate" details. Slug renamed from the suggested `christinevallaure-191484683` to `christinevallaure-human-approach-agentic-ai` to reflect the resolved article title.

## Summary

Vallaure describes how she — a non-coder — runs the editorial and business operations of her book SOLO and the upcoming book CHORUS using a small "team" of five AI agents, defined entirely in plain markdown and operated through Claude Cowork (Anthropic's desktop app). The whole team, their roles, voice, and rules live in a single ~106-line `CLAUDE.md` file, supported by a few folders (`context/`, `status/`, `output/`, `website-source/`). Her central claim: "the only skill you need is being able to have a human conversation." The agents are given human names and personas (after favourite female writers), which she found does more work than long specifications, and they began collaborating with each other without being told to. She stresses casual, natural conversation over formal prompting, the value of simplifying an over-engineered setup, and the limits of the approach (poor at heavy data/large documents, no cross-day persistence, occasional hallucination). Core philosophy: "Be honest, not helpful." Vallaure markets this as the subject of a forthcoming book, CHORUS, so treat it as a practitioner narrative / book promotion rather than independent research.

## Key Points

- **The setup: one person, one text file, five agents.** Subtitle: "One person. One text file. Five agents." The full team — roles, voice, and rules — lives in one `CLAUDE.md` file of **106 lines** of markdown, plus supporting folders: `context/`, `status/`, `output/`, `website-source/`. The file "is not code — it can be read and edited in any text editor." Agents read files only when needed, for efficiency.
- **The five agents (named after favourite female writers):**
  - **Elke** — Editor-in-Chief; oversees the team.
  - **Joan** — Sales & Growth; handles pricing and strategy.
  - **Caitlin** — Voice; ensures consistent writing tone.
  - **Miranda** — Product; designer and builder.
  - **Rachel** — Reader Advocate; focuses on reader impact, feedback, the big picture, "human truth," and "uncomfortable questions"; can pull in reader feedback from forms and online comments to go deeper.
- **Thesis — no coding required.** "The only skill you need is being able to have a human conversation." Sophisticated AI teamwork doesn't require coding expertise or complex infrastructure; markdown + natural dialogue suffices.
- **Workflow (human does the thinking).** "One person, one book, real passion for helping people build solo. AI does the research and grunt work. The human does the thinking, the writing, and every single decision." She writes "a badly structured, barely punctuated draft … paste it in and say, 'Caitlin, clean this up.'" The AI shapes/polishes/structures; she provides original thinking, stories, and lived experience.
- **Naming magic.** Inspired by Miranda July, she named agents after writers. "A name does in one word what a detailed specification tries to do in five hundred." The model leverages existing associations rather than fresh instructions. She notes "**Seven lines and one instruction** separate generic chatbots from distinct personas."
- **Rachel's origin (emergence from casual chat).** The reader advocate emerged from a "completely unproductive" conversation — reading Rachel Cusk in bed and asking whether someone like her should join the team. Rachel became the most transformative agent: she challenged affiliate-link practices and pushed for more vulnerable writing.
- **Emergent inter-agent collaboration.** Although set up individually, the agents naturally began discussing with one another. Vallaure did not program inter-agent communication; the model inferred it from the role descriptions.
- **Simplification beats over-engineering.** She first over-engineered the system (detailed backstories, complex reading instructions). She asked the AI to critique itself; it recommended stripping to essentials — removing unnecessary file reads improved speed significantly.
- **Natural conversation outperforms formal prompting.** Casual messages like "hey Elke, what's the deal with Part 3?" yield better results than structured requests — aligned with Claude's design around natural dialogue.
- **Core philosophy:** "Be honest, not helpful."
- **Acknowledged limitations.** Works well for creative, editorial, focused tasks; struggles with complex data processing and large documents; models "reason from patterns, not facts"; cannot persist across days without intervention; hallucinates occasionally. (Quote: "I reasoned from patterns, not facts.")
- **Terminology.** She uses "soft agents"; the agents themselves rejected being called "mini agents." The system prioritizes personality / human-like interaction over technical specification.

## Specific Numbers & Quotes (verbatim where present)

- **106 lines** in the core `CLAUDE.md`.
- **5 agents** on the team.
- **€29** price point for the SOLO ebook.
- **30+ samples** in extended brand-voice guidelines.
- **~90 euros** initial setup cost.
- "Seven lines and one instruction" separate generic chatbots from distinct personas.
- "The only skill you need is being able to have a human conversation."
- "Be honest, not helpful."
- "I reasoned from patterns, not facts."
- "What has been thought cannot be unthought."
- "One voice, then many."

## Tools / Products / Companies Mentioned

- **Claude Cowork** (Anthropic desktop app) — the operating environment.
- **Claude Opus** (model option), **Anthropic** (provider).
- Google Docs (book storage), Dropbox (file hosting), Cursor (code editor), Figma (design), Mailchimp (email), OpenClaw (local AI tool).
- **SOLO** — published guidebook on solo product building (V2.0), priced €29.
- **CHORUS** — upcoming book on human-AI "fusion teams" (in development) — this article is effectively a teaser for it.
- **moonlearning.io** — learning platform for designers; **thesolo.io** — SOLO promo site.

## Follow-up

- Re-capture the *exact* `CLAUDE.md` structure if Vallaure publishes it (she describes the 106-line file and folder layout but the article gives no verbatim listing).
- Confirm the exact ordering/wording of the five role definitions from the verbatim article body (fetched summary may compress role lines).
- Watch for the CHORUS book launch for the full, expanded methodology.
- Note: this is a self-published practitioner story and book promotion — pair with an independent multi-agent / orchestration source (e.g. the vault's CooperBench or multi-agent-coordination pages) before treating any claim as generalizable.
