---
type: concept
status: draft
created: 2026-05-21
updated: 2026-05-21
tags: [concept, data-modeling, ontology]
sources: [sources/hsol-ai-portfolio-6]
confidence: 0.9
---

# Palantir Foundry Ontology

## Summary
An ontology framework used by Palantir Foundry to define how data is structured as objects and relationships. In the context of the [[sources/hsol-ai-portfolio-6|LLM Wiki]], it refers to the adoption of these enterprise meta-types for personal data management.

> [!important] Why it Matters
> Using a rigorous ontology prevents personal knowledge bases from becoming disorganized. It provides a stable schema that AI agents can use to navigate and query the vault with higher precision.

## Meta-types Structure

```mermaid
graph TD
    A[Ontology] --> B[Object Layer]
    A --> C[Action Layer]
    A --> D[Interface Layer]
    
    B --> B1[Object Type]
    B --> B2[Property]
    B --> B3[Link Type]
    
    C --> C1[Action Type]
    
    D --> D1[Interface]
    
    class A,B,C,D internal-link;
```

## Key Claims
- The ontology consists of eight meta-types: **Object Type, Object, Property, Link Type, Link, Action Type, Action, and Interface**.
- Objects represent entities (e.g., a Project, a Company), while Links define the relationships between them.

## Related Concepts
- [[concepts/infrastructure-dev/object-backend|Object Backend]]
- [[concepts/infrastructure-dev/object-graph-mapping|Object-Graph Mapping]]

## Sources
- [[sources/hsol-ai-portfolio-6|AI Portfolio Making (6): A Data Model for a Person]]
