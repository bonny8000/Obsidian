---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.70
---

# What level of fidelity is appropriate before handing off to detailed UI design?

## Short Answer
Wireframes are ready for detailed UI design handoff when: (1) all key screens are represented with correct information hierarchy; (2) the primary user flow is navigable without ambiguity; (3) component slots are identified (even if not styled); and (4) the content model is stable (labels, data fields, empty states). Pixel fidelity and visual styling should not be present—those belong to the next stage.

## Evidence
- [[concepts/infrastructure-dev/wireframe-generation|Wireframe Generation]] — "Wireframes can be generated from upstream planning artifacts. Generated wireframes should be treated as drafts for review, not final UI. Linking wireframes to requirements improves traceability."
- [[concepts/product-management/ai-product-planning|AI Product Planning]] — "Planning quality depends on clear assumptions, target users, constraints, and validation." A wireframe that reflects these passes the readiness bar.
- [[concepts/infrastructure-dev/design-to-code-workflow|Design-to-Code Workflow]] — "A useful workflow includes design-system context, codebase context, browser verification, and human review." Wireframes feed into this; they must be precise enough to resolve component identity.
- [[sources/manyfast-homepage|Manyfast Product Website]] — "Planning documents can become machine-readable inputs for coding agents." The wireframe is the structural anchor for that machine-readable artifact.

## Follow-up Sources Needed
- A standard wireframe review checklist used by design teams before advancing to high-fidelity mockups.
