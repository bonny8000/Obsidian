---
source_url: https://www.nngroup.com/articles/ux-context-design/
captured: 2026-08-04
title: "UX-Context Design: Using UX Knowledge to Inform AI-Generated Design"
authors: [Tony Alicea]
published: 2026-07-24
publisher: Nielsen Norman Group
language: en
format: practitioner article proposing a named practice
---

# UX-Context Design — Nielsen Norman Group

**Author:** Tony Alicea, Nielsen Norman Group.
**Published:** 2026-07-24 · **Captured:** 2026-08-04

AI-written extraction. No full-text reproduction; short quoted phrases only.

---

## Thesis

As AI generates more of the interface work, the primary deliverable of UX shifts from documents written to persuade humans to **context curated to steer machines**. The named practice:

> **UX-Context Design** — *"The practice of discovering and curating what an organization knows and wants into the context that guides everything its AI tools generate: from who its users are and the world they live in, to how a product should look and behave."*

## Argument chain

1. Models without context produce middle-of-the-road output.
2. Design is no longer produced only by designers — *"In many organizations, designers are no longer the only people producing designs."*
3. Therefore traditional UX deliverables must be rebuilt as machine-readable artifacts.
4. `DESIGN.md` is the existing proof that the format works.
5. A hypothetical `UX.md` would extend it from visual system to research and behaviour.
6. Effective context is shaped differently from a handoff document.
7. Research insight then reaches the whole organisation through the AI rather than through meetings.

## Key claims

- **Context steers rather than instructs.** *"Context enables you to avoid middle-of-the-road output."* / *"Context leans a model's output in a particular direction."*
- **Persuasion artifacts are the wrong shape.** *"A persona has a stock photo … the model does not need persuading, it needs the underlying reasoning."*
- **The success criterion changes.** *"Its success is measured by whether AI output improves, not by whether stakeholders are convinced."*
- **There is no handoff.** *"Never finished. New research updates it, and so does watching what the AI gets wrong."* — the AI's failures become a research input.
- Requirements for an AI-ready deliverable: machine-readable, curated by a skilled human, and available across the organisation.

## The proposed `UX.md`

Five components:

| Component | Content |
| --- | --- |
| Research synthesis | Insights expressed as actionable constraints |
| Interaction standards | Behavioural guidelines |
| Glossary | Domain vocabulary as users actually say it |
| User models | Expertise, concerns, goals, pain points |
| World models | Context of use — the circumstances that affect usage |

## Examples given

- **House-builder analogy.** A builder who never meets the family defaults to an average two-storey house and misses wheelchair access or a home office. Same failure mode as an uncontexted model.
- **`DESIGN.md` (Google Labs, April 2026).** Open file format holding machine-readable design-system values — colours, type sizes, spacing, radii — alongside human-readable guidance on application and accessibility. Cited as the working precedent.
- **Glossary.** *"If your users say 'case' and are confused by 'ticket,' the AI should know that."*
- **World model — nurses.** Users interrupted mid-task while working a hospital floor.
- **World model — claims.** Filing a claim after an accident is a stressed context, not the routine one.

## Evidence

- *"Our experiments suggest that curated UX context improves AI-generated UI"* — no methodology, sample, baseline, or comparison disclosed.
- *"Many teams are already practicing UX-context design in some form"* — supported only by a link to another article.
- No quantitative data anywhere in the piece.

## Open questions the article itself raises

- Which traditional artifacts actually improve AI output?
- How much raw research data is the right amount?
- What metrics measure context efficacy?
- How do the answers shift as models improve?
- Is there a context saturation threshold?
- How is this maintained and scaled over time?

Stated temporal caveat: *"A curation decision made for today's models may be wrong for next year's."*

## Recommendations

- Don't wait for the research: *"You don't need to wait for the answers to all these questions to engage in UX-context design."*
- Extract sample user insights into plain markdown files.
- Make them visible to the team's AI tools.
- Convert the design system to a machine-readable format.
- Store context alongside product code; update continuously.
- Watch whether generated output improves — that is the measurement.
