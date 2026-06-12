---
type: map
status: active
created: 2026-06-10
updated: 2026-06-10
tags: [map, research-agenda, open-questions]
sources: []
confidence: 0.9
---

# Research Agenda — Open Questions Across the Wiki

Auto-harvested from `Open questions` sections of all concept pages (85 open, 70 already answered via query pages). Regenerate with `scripts/harvest_questions.py`. Pick a question, answer it with evidence, save to `wiki/queries/`, and mark the origin page `[Answered → ...]`.

## Recurring themes

1. **Where exactly does the human belong in AI-automated research?** — scoping vs. procedure, interpretation ownership, checkpoint design (recurs across ~15 pages).
2. **How to evaluate AI systems with UX rigor** — eval sample sizes, benchmark validity, treating AI runs as evaluators.
3. **What transfers from classic quant methods to AI-era research** — discovery models for eval runs, questionnaires for AI products.
4. **Robotics/spatial: trust, communication, and dataset constraints** for socially embedded machines.


## UX Research (37)

- Should wiki dashboards report CIs for any metric Bonny tracks from usability sessions? — [[concepts/ux-research/adjusted-wald-confidence-interval|adjusted-wald-confidence-interval]]
- How do we maintain "grounding" and prevent AI hallucinations during qualitative synthesis? — [[concepts/ux-research/ai-analysis|ai-analysis]]
- What is the best balance between AI speed and human-led thematic deep-dives? — [[concepts/ux-research/ai-analysis|ai-analysis]]
- What are the most effective prompting strategies or "probe policies" to reduce verbosity bias in AI-moderated interviews? — [[concepts/ux-research/ai-moderated-interviews|ai-moderated-interviews]]
- How does AI-assisted screening impact participant quality compared to manual screening? — [[concepts/ux-research/ai-recruitment|ai-recruitment]]
- To what extent can AI recruitment mitigate or introduce bias in research sampling? — [[concepts/ux-research/ai-recruitment|ai-recruitment]]
- Should AI-only issues be tracked as hypotheses until a human researcher verifies video evidence? — [[concepts/ux-research/ai-usability-false-alarm-triage|ai-usability-false-alarm-triage]]
- What minimum evidence checklist should the wiki use before accepting an AI-generated usability issue? — [[concepts/ux-research/ai-usability-false-alarm-triage|ai-usability-false-alarm-triage]]
- How do teams maintain research quality accountability when setup friction drops to near zero? — [[concepts/ux-research/automated-ut-setup|automated-ut-setup]]
- Is there a principled way to choose between participant-data-based automation (Athena pattern) and AI-judgment-based automation (Huribot pattern) depending on research question type? — [[concepts/ux-research/automated-ut-setup|automated-ut-setup]]
- Where exactly should the human checkpoint sit in an automated UT pipeline (setup, analysis, or reporting)? — [[concepts/ux-research/human-in-the-loop|human-in-the-loop]]
- Does Huribot's proprietary training on Toss data generalize as a pattern? How would other companies build equivalent tooling? — [[concepts/ux-research/huribot|huribot]]
- How does Toss measure whether Huribot's usability judgments are reliable (calibration against formal UT results)? — [[concepts/ux-research/huribot|huribot]]
- Will there be a "Huribot Story #2" with quantitative outcome data? — [[concepts/ux-research/huribot|huribot]]
- How should these criteria be converted into a reusable screener-review checklist for AI-generated UX research plans? — [[concepts/ux-research/participant-selection-criteria|participant-selection-criteria]]
- What is the primary NN/g article referenced by the post, and how does it define inclusion, exclusion, and diversity criteria? — [[concepts/ux-research/participant-selection-criteria|participant-selection-criteria]]
- Can the same model size AI-eval runs (how many eval cases to catch x% of failure modes at rate p)? — [[concepts/ux-research/problem-discovery-model|problem-discovery-model]]
- Should the wiki turn this into a checklist or spaced-learning plan? — [[concepts/ux-research/quant-uxr-learning-path|quant-uxr-learning-path]]
- Which pillar should become Bonny's next deliberate practice track? — [[concepts/ux-research/quant-uxr-learning-path|quant-uxr-learning-path]]
- How should this concept connect to ResearchOps intake and prioritization? — [[concepts/ux-research/quant-uxr-rigor|quant-uxr-rigor]]
- What lightweight rubric would distinguish "method complexity" from decision-useful rigor in Bonny's research outputs? — [[concepts/ux-research/quant-uxr-rigor|quant-uxr-rigor]]
- Which Conjointly KB pages should be promoted into standalone concept notes after deeper reading? — [[concepts/ux-research/research-methods-foundations|research-methods-foundations]]
- Which parts of this methods baseline should become explicit evaluation rubrics for AI-generated UX research plans? — [[concepts/ux-research/research-methods-foundations|research-methods-foundations]]
- How does ResearchOps integrate with specialized AI agents in the [[projects/product-workflow-studio|Product Workflow Studio]]? — [[concepts/ux-research/research-operations|research-operations]]
- What p is realistic for AI-moderated studies, where session quality differs from lab sessions? — [[concepts/ux-research/sample-size-for-usability-studies|sample-size-for-usability-studies]]
- Which questionnaire fits AI-product UX (where "task" boundaries blur)? UMUX-LITE for in-product pulses? — [[concepts/ux-research/standardized-usability-questionnaires|standardized-usability-questionnaires]]
- What validation standard would be required before using synthetic data in any product decision? — [[concepts/ux-research/synthetic-survey-data|synthetic-survey-data]]
- Which internal uses of synthetic survey data are acceptable as tooling tests rather than research evidence? — [[concepts/ux-research/synthetic-survey-data|synthetic-survey-data]]
- Does AI-generated UI increase or decrease the rate of usability debt accumulation? — [[concepts/ux-research/usability-debt|usability-debt]]
- How can we quantify usability debt in a way that parallels technical debt metrics? — [[concepts/ux-research/usability-debt|usability-debt]]
- How can we measure the impact of "micro-interactions" on high-level business KPIs? — [[concepts/ux-research/ux-metrics|ux-metrics]]
- What are the most effective "proxy metrics" for long-term user trust? — [[concepts/ux-research/ux-metrics|ux-metrics]]
- Build a small interactive calculator (HTML artifact) implementing the decision map? — [[concepts/ux-research/ux-statistics-decision-map|ux-statistics-decision-map]]
- What lightweight rubric should the wiki use to score decision relevance in AI-assisted research outputs? — [[concepts/ux-research/validity-and-decision-relevance|validity-and-decision-relevance]]
- Which ResearchOps mechanisms best preserve validity and decision relevance at scale? — [[concepts/ux-research/validity-and-decision-relevance|validity-and-decision-relevance]]
- How should AI-assisted research workflows separate procedural automation from human-owned scoping judgment? — [[concepts/ux-research/wicked-research-scoping|wicked-research-scoping]]
- What concrete signals should be used to evaluate wicked scoping in a research performance rubric? — [[concepts/ux-research/wicked-research-scoping|wicked-research-scoping]]

## AI Agents (13)

- What are the primary "ethical controller" frameworks needed for Agentic AI? — [[concepts/ai-agents/agentic-ai|agentic-ai]]
- Does the "thinking partner" role satisfy the methodological integrity requirements that the SAGE authors would impose on reflexive thematic analysis specifically? — [[concepts/ai-agents/ai-as-thinking-partner|ai-as-thinking-partner]]
- What procedural guardrails distinguish legitimate thinking-partner use from rationalized AI-as-analyst use? — [[concepts/ai-agents/ai-as-thinking-partner|ai-as-thinking-partner]]
- Which AI coding tools should be compared for Bonny's actual workflow? (insufficient evidence in wiki — external comparison needed) — [[concepts/ai-agents/ai-coding-tools|ai-coding-tools]]
- How well can bots understand complex user contexts vs. simple pattern matching? — [[concepts/ai-agents/ai-inspection-bot|ai-inspection-bot]]
- Which OpenAI capabilities are generally available versus limited preview on Bedrock? (insufficient evidence in wiki ??requires official AWS/OpenAI documentation) — [[concepts/ai-agents/amazon-bedrock|amazon-bedrock]]
- What official Anthropic documentation confirms the current capabilities and availability of Claude Design? (insufficient evidence in wiki — requires official Anthropic documentation) — [[concepts/ai-agents/claude-design|claude-design]]
- How does Codex on Bedrock differ operationally from local Codex CLI usage? (insufficient evidence in wiki — requires official AWS/OpenAI documentation) — [[concepts/ai-agents/codex-on-bedrock|codex-on-bedrock]]
- How will Gemini 3.5's performance in real-world "long-horizon" tasks compare to competitors like Claude or GPT-5? (insufficient evidence in wiki — requires independent benchmarks not yet collected) — [[concepts/ai-agents/gemini-3-5|gemini-3-5]]
- Does SkillOpt generalize to non-code, qualitative skill documents (e.g., research protocols, wiki maintenance instructions)? — [[concepts/ai-agents/skillopt|skillopt]]
- How does the textual learning-rate budget interact with skill complexity? Is there a risk of over-fitting skills to specific benchmarks? — [[concepts/ai-agents/skillopt|skillopt]]
- How sensitive are results to the quality of the optimizer model? Could a weaker optimizer degrade skills? — [[concepts/ai-agents/skillopt|skillopt]]
- What is the cost of running the optimizer model at training time vs. the inference savings at deployment? — [[concepts/ai-agents/skillopt|skillopt]]

## Product Management (9)

- How does "continuous discovery" differ from discrete discovery phases in long-term roadmapping? — [[concepts/product-management/discovery-phase|discovery-phase]]
- What are the risks of "over-discovering" in a high-velocity AI startup environment? — [[concepts/product-management/discovery-phase|discovery-phase]]
- Re-read raw source and restore the original extracted claims (lost). — [[concepts/product-management/fpa-central|fpa-central]]
- How do "agile" roadmaps differ in their receptivity to long-form qualitative research? — [[concepts/product-management/product-roadmap|product-roadmap]]
- What are the best tools for visualizing a "discovery-first" roadmap? — [[concepts/product-management/product-roadmap|product-roadmap]]
- What examples in Bonny's work show strong versus weak product taste? (insufficient evidence in wiki — requires Bonny's own work portfolio, not in wiki) — [[concepts/product-management/product-taste|product-taste]]
- How does the ratio of researchers to PMs/Engineers affect the strategy for influence? — [[concepts/product-management/research-influence|research-influence]]
- What are the specific patterns of "ignored research" in AI-native product development? — [[concepts/product-management/research-influence|research-influence]]
- Will "token subsidies" become a standard corporate benefit? (insufficient evidence in wiki ??this is a speculative future trend not grounded in current wiki sources) — [[concepts/product-management/tokenomics|tokenomics]]

## Infrastructure & Dev (14)

- Should APCA-style contrast checks become part of the local design-review automation rubric? — [[concepts/infrastructure-dev/color-token-architecture|color-token-architecture]]
- Which color-token structure best fits ASUS/ROG multi-brand, multi-theme, and localization constraints? — [[concepts/infrastructure-dev/color-token-architecture|color-token-architecture]]
- Which adaptation metrics best predict real robot success? (insufficient evidence in wiki — requires quantitative studies beyond current source summaries) — [[concepts/infrastructure-dev/domain-adaptation|domain-adaptation]]
- What fallback chain should be documented for each target platform? (insufficient evidence in wiki — requires platform-specific font stack documentation for Android, iOS, web) — [[concepts/infrastructure-dev/font-fallback|font-fallback]]
- What is a reliable automated test for glyph-coverage regressions across locales? — [[concepts/infrastructure-dev/font-subsetting|font-subsetting]]
- Which Obsidian plugins should be enabled after the basic workflow is stable? (insufficient evidence in wiki ??requires Obsidian plugin ecosystem knowledge not yet collected) — [[concepts/infrastructure-dev/llm-wiki|llm-wiki]]
- Which locales in Bonny's current products lack locale-specific visual QA? — [[concepts/infrastructure-dev/localization-ux|localization-ux]]
- Which planning benchmarks are appropriate for egocentric-video-trained robot world models? (insufficient evidence in wiki — requires benchmark survey beyond current source summaries) — [[concepts/infrastructure-dev/model-based-planning|model-based-planning]]
- How to best automate the mapping between `modern-web-guidance` patterns and specific custom component libraries (e.g., "FE Database")? (insufficient evidence in wiki ??requires FE Database documentation not yet collected) — [[concepts/infrastructure-dev/modern-web-guidance|modern-web-guidance]]
- Which languages and glyph ranges must Bonny's design systems explicitly support? (insufficient evidence in wiki — requires Bonny's specific project scope information not in wiki) — [[concepts/infrastructure-dev/multilingual-app-typography|multilingual-app-typography]]
- How does scalability compare to cloud-native AI at the enterprise level? — [[concepts/infrastructure-dev/on-premise-ai|on-premise-ai]]
- How does this relate to prompt-engineering as a field ??is text-space optimization just rigorous automated prompt engineering? — [[concepts/infrastructure-dev/text-space-optimization|text-space-optimization]]
- Is text-space optimization applicable to wiki maintenance instructions (like this vault's AGENTS.md)? Could the ingest workflow itself be SkillOpt-optimized? — [[concepts/infrastructure-dev/text-space-optimization|text-space-optimization]]
- What are the failure modes when the edit-proposing optimizer model is misaligned with the true objective? — [[concepts/infrastructure-dev/text-space-optimization|text-space-optimization]]

## Robotics & Spatial AI (12)

- Which AI hardware categories have real demand versus narrative momentum? (insufficient evidence in wiki — market data needed) — [[concepts/robotics-spatial/ai-hardware-boom|ai-hardware-boom]]
- Which manipulation skills transfer across hands with different degrees of freedom? (insufficient evidence in wiki — requires detailed paper reading beyond source summaries) — [[concepts/robotics-spatial/dexterous-manipulation|dexterous-manipulation]]
- How much human data is useful before robot-specific data becomes the limiting factor? (insufficient evidence in wiki — requires quantitative threshold data from full papers) — [[concepts/robotics-spatial/egocentric-human-data|egocentric-human-data]]
- Which annotations are necessary for each downstream robot task? (insufficient evidence in wiki — requires detailed task-by-task analysis from full papers) — [[concepts/robotics-spatial/egocentric-human-data|egocentric-human-data]]
- What interview loops best evaluate hardware systems judgment? (insufficient evidence in wiki ??requires hiring practice sources not yet collected) — [[concepts/robotics-spatial/hardware-team-hiring|hardware-team-hiring]]
- Which transfer mechanisms are robust across robot embodiments rather than task-specific? (insufficient evidence in wiki — requires cross-embodiment comparison studies beyond current source summaries) — [[concepts/robotics-spatial/human-to-robot-transfer|human-to-robot-transfer]]
- How much mobile context must be represented for transfer from human movement to robot movement? (insufficient evidence in wiki — requires quantitative mobile context analysis from full papers) — [[concepts/robotics-spatial/mobile-manipulation|mobile-manipulation]]
- What licensing and privacy constraints apply to egocentric human robot-learning data? (insufficient evidence in wiki — licensing and privacy terms for specific datasets require external legal/dataset documentation not present in sources) — [[concepts/robotics-spatial/robot-learning-dataset|robot-learning-dataset]]
- Which robotics components are true bottlenecks versus temporary constraints? (insufficient evidence in wiki — supply chain specifics require current industry/market data not present in sources) — [[concepts/robotics-spatial/robotics-supply-chain|robotics-supply-chain]]
- Which smart-city claims are backed by deployed services versus pilot narratives? (insufficient evidence in wiki — distinguishing deployed from pilot requires external NAVER LABS service status documentation not present in sources) — [[concepts/robotics-spatial/smart-city-ai|smart-city-ai]]
- Which NAVER LABS research papers correspond to each spatial AI technique mentioned in the blog articles? (insufficient evidence in wiki — paper-to-technique mapping requires the actual NAVER LABS research paper list, not available in current blog sources) — [[concepts/robotics-spatial/spatial-ai|spatial-ai]]
- Which datasets or benchmarks best evaluate visual localization in crowded indoor spaces? (insufficient evidence in wiki — benchmark comparison requires external computer vision literature not present in current sources) — [[concepts/robotics-spatial/visual-localization|visual-localization]]
