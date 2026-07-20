---
type: map
status: active
created: 2026-06-12
updated: 2026-07-02
tags: [map, llm-ready, source-index]
sources: []
confidence: 1.0
---

# LLM-Ready Source Index

This map tracks whether source pages are ready to support LLM-assisted ideation, synthesis, and decision drafting.

## Status Summary

- Total source pages: 154
- LLM-ready source pages: 132
- Deep / standard / light / detailed: 27 / 113 / 11 / 1
- Legacy source pages without an `ingest_level`: 2
- Partial coverage sources needing deeper ingest: 22

## How to Use

- Prefer `llm_ready: true` and `coverage: substantial` or `coverage: full` when asking an LLM for grounded ideation.
- Use `light` or `partial` sources for exploration only, then return to raw evidence before making decisions.
- Promote sources by filling examples, caveats, tensions, open questions, and concept links from the raw material.

## Source Readiness Table

| Source | Level | Coverage | LLM ready | Raw preserved | Deepening focus |
| --- | --- | --- | --- | --- | --- |
| [[sources/qualtrics-market-research-trends-2026|Qualtrics (2026): 2026 Qualtrics Market Research Trends Report]] | `standard` | `substantial` | `true` | `true` | global researcher survey; study leadership vs contributor disconnect |
| [[sources/eopla-magazine-44341-0-person-company|비주류VC (2026): Humans only toss missions: The '0-Person Company' debate sparked by Matrix]] | `standard` | `substantial` | `true` | `true` | early beta runtime; analyze startup paradigm shift and legal boundaries |
| [[sources/hbs-working-knowledge-ai-advice-willful-blindness|Chan (2026): When AI Gives Advice, Employees Rarely Ask Why]] | `standard` | `substantial` | `true` | `true` | randomized experiment; audit willful blindness in human checkpoints |
| [[sources/arxiv-2606.30660-value-sensitive-conversational-ai|Maurya (2026): Value-Sensitive Conversational AI for Low-Literacy Surveys]] | `deep` | `full` | `true` | `true` | full preprint preserved; replicate with randomization and AI disclosure |
| [[sources/clova-merit-post-training|CLOVA: MERIT Conflict-Aware Post-Training]] | `standard` | `substantial` | `true` | `true` | first-party explainer; use the paper and code for implementation |
| [[sources/kakao-vc-upsell-design|Kakao Ventures: Upsell Design Through Value, Reassurance, and Convenience]] | `standard` | `substantial` | `true` | `true` | product framework; validate economics, trust, and legal boundaries |
| [[sources/sangwook-typescript-6-migration-troubleshooting|Sangwook Han: TypeScript 6 Migration Troubleshooting]] | `standard` | `substantial` | `true` | `true` | practitioner case; verify tool-specific migration against current versions |
| [[sources/agent-skills-day-3|Agent Skills (Day 3)]] | `deep` | `full` | `true` | `true` | ready for grounded ideation |
| [[sources/agent-tools-interoperability-day-2|Agent Tools & Interoperability]] | `unclassified` | `unknown` | `false` | `unknown` | legacy source needs readiness metadata |
| [[sources/atlassian-design-md|Atlassian: DESIGN.md — Portable Design Context in Practice]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/atlassian-design-system-context-engine|Atlassian: Building the Context Engine for the AI Era]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/measuringu-banner-tables|MeasuringU: How to Use Banner Tables to Present Survey Results]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/measuringu-bayes-priors-uxr|MeasuringU: Bayes' Law in UX Research — The Power and Perils of Priors]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/measuringu-credible-vs-confidence-intervals|MeasuringU: Credible vs. Confidence Intervals]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/measuringu-synthetic-users-review|MeasuringU: A Review of Experiments with Synthetic Users]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/measuringu-tac10-screening|MeasuringU: Using the TAC-10 for Screening and Data Cleaning]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/the-new-sdlc-with-vibe-coding-day-1|The New SDLC With Vibe Coding]] | `unclassified` | `unknown` | `false` | `unknown` | legacy source needs readiness metadata |
| [[sources/andru-saksena-adobe-haic-2025|Adobe HAIC Framework (Andru & Saksena, 2025)]] | `deep` | `partial` | `false` | `false` | raw provenance, raw-based expansion |
| [[sources/arxiv-2605-23904|Source: arXiv 2605.23904 ??SkillOpt]] | `deep` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/brunch-ghidesigner-487|AI Designer LLM Wiki Article]] | `deep` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/brunch-ghidesigner-489|Source: 3 Competencies for UX/UI Designers in the Agentic AI Era]] | `deep` | `partial` | `false` | `false` | raw provenance, raw-based expansion |
| [[sources/carl-pearson-quant-uxr-self-study-resources|Carl Pearson: Learn Quantitative UX Research]] | `deep` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/chapman-rodden-quant-uxr-2023|Quantitative User Experience Research]] | `deep` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/conjointly-research-methods-kb|Conjointly Research Methods Knowledge Base]] | `deep` | `full` | `true` | `true` | ready for grounded ideation |
| [[sources/cooper-about-face-4-2014|About Face 4: The Essentials of Interaction Design]] | `deep` | `partial` | `false` | `false` | raw provenance, raw-based expansion, concept links |
| [[sources/founders-playbook-2026|Source: Founder's Playbook: Building an AI-Native Startup (2026)]] | `deep` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/garrett-elements-ux-2011|The Elements of User Experience (2nd ed.)]] | `deep` | `partial` | `false` | `false` | raw provenance, raw-based expansion, concept links |
| [[sources/gerhard-norton-vr-usability-2022|VR Usability (Gerhard & Norton, 2022)]] | `deep` | `partial` | `false` | `false` | raw provenance, raw-based expansion, concept links |
| [[sources/how-to-ai-uxr-2026|How To AI UXR: The ResearchOps Review (2026)]] | `deep` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/lennys-podcast-ai-hardware-boom-caitlin-kalinowski|Lenny's Podcast: Beginning of the AI Hardware Boom]] | `deep` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/lennys-podcast-cat-wu-ai-pm-claude-code|Lenny's Podcast: Cat Wu on AI-Native Product Management]] | `deep` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/measuringu-senior-uxr-years|Source: How Many Years Does It Take to Become a Senior UX Researcher?]] | `deep` | `partial` | `false` | `false` | raw provenance, raw-based expansion |
| [[sources/research-that-scales-towsey-2024|Research That Scales: The Research Operations Handbook]] | `deep` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/sauro-lewis-quantifying-ux-2016|Quantifying the User Experience: Practical Statistics for User Research (2nd ed.)]] | `deep` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/tullis-albert-measuring-ux-2013|Measuring the User Experience (2nd ed.)]] | `deep` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/user-interviews-ai-assistant|User Interviews AI Assistant]] | `deep` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/brunch-ghidesigner-495|디자인조이 AI와 함께 연 매출 수십억 원을 달성하다.]] | `light` | `partial` | `false` | `false` | raw provenance, raw-based expansion, concept links |
| [[sources/brunch-ghidesigner-496|블록(Block) 가장 파격적인 'AI 네이티브' 조직 전환]] | `light` | `partial` | `false` | `false` | raw provenance, raw-based expansion, concept links |
| [[sources/brunch-ghidesigner-498|앤트로픽, 클로드 오퍼스 4.8을 출시하다.]] | `light` | `partial` | `false` | `false` | raw provenance, raw-based expansion, concept links |
| [[sources/microsoft-web-iq|Microsoft Web IQ: AI-Native Grounding APIs]] | `light` | `partial` | `false` | `false` | raw provenance, raw-based expansion, concept links |
| [[sources/openai-codex-workflow|OpenAI Codex: Every Role, Tool, and Workflow]] | `light` | `partial` | `false` | `false` | raw provenance, raw-based expansion, concept links |
| [[sources/amershi-2019-human-ai-guidelines|Amershi et al. (2019): Guidelines for Human-AI Interaction]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/arxiv-2410-24221|EgoMimic]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/arxiv-2505-21864|DexUMI]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/arxiv-2509-04443v1|EMMA]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/arxiv-2509-19626|EgoBridge]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/arxiv-2512-22414|Human-to-Robot Transfer in VLA Models]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/arxiv-2602-06949|DreamDojo]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/arxiv-2602-16710|EgoScale]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/arxiv-2604-07607|EgoVerse]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/brunch-ghidesigner-472|Brunch: Google Gemini Enterprise for UXUI Design]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/brunch-ghidesigner-482|Vibe Design and Coding with Claude Design and Claude Code]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/brunch-ghidesigner-483|SpaceX, Cursor, and AI Platform Strategy]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/brunch-ghidesigner-486|Hermes Agent AI for Designers]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/brunch-ghidesigner-497|Brunch: Gemini Spark - New Leader of Agentic AI]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/bucketplace-2026-05-06-ai-for-designers|Source: How Designers Use AI (Bucketplace)]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/bucketplace-2026-05-08-financial-data-lake|Source: Unlocking Finance to the Data Lake (Bucketplace)]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/bucketplace-pretendard-jp-2026-04-17|Bucketplace — Pretendard JP in a Multi-Country Android App]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/ditoday-claude-design-uiux-workflow|Digital iNSIGHT: Claude Design and UI/UX Workflow]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/figma-you-never-stop-cultivating-taste|Figma: You Never Stop Cultivating Taste]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/geeknews-kagi-translate-linkedin|Kagi Translate: LinkedIn Style AI]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/gemini-3-5-launch|Source: Introducing Gemini 3.5: Cutting-Edge Intelligence with Action]] | `standard` | `partial` | `false` | `false` | raw provenance, raw-based expansion |
| [[sources/google-io-2026-agentic-gemini|Source: Google I/O 2026: The Beginning of the Agentic Gemini Era]] | `standard` | `partial` | `false` | `false` | raw provenance, raw-based expansion |
| [[sources/horvitz-1999-mixed-initiative|Horvitz (1999): Principles of Mixed-Initiative User Interfaces]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/hsol-ai-portfolio-6|AI Portfolio Making (6): A Data Model for a Person]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/lee-see-2004-trust-in-automation|Lee & See (2004): Trust in Automation — Designing for Appropriate Reliance]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/linkedin-user-selection-criteria|LinkedIn: Is This User Really Our User?]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/manyfast-homepage|Manyfast — AI Software Planning from PRD to Wireframes]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/mashdigi-aws-openai-bedrock-codex|Mashdigi: AWS and OpenAI Bedrock Collaboration]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/measuringu-ai-real-ui-problems-hallucinations|MeasuringU: Does AI Find Real UI Problems or Just Hallucinations?]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/measuringu-ai-usability-problem-analysis-video|MeasuringU: AI Reliability for Finding UI Problems]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/measuringu-statistics-30-participants|MeasuringU: Do Statistics Really Require 30 Participants?]] | `detailed` | `detailed` | `true` | `true` | ready for small-n UX statistics reasoning |
| [[sources/medium-harizlim-ai-qualitative-research-2026|Hariz Lim — AI in Qualitative Research: "If you're using AI as an analysis tool, you're doing it wrong"]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/meta-research-medium-publication|Meta Research Medium Publication]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/naverlabs-blog-10034251|NAVER LABS: Robot Elevator Boarding Acceptance]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/naverlabs-blog-34515|NAVER LABS: AI and Space]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/naverlabs-blog-34958|NAVER LABS: Future City Infrastructure]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/nngroup-research-recommendations-roadmap|Research Recommendations and the Roadmap]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/nvidia-nemotron-personas|NVIDIA Nemotron-Personas Datasets]] | `standard` | `partial` | `false` | `false` | raw provenance, raw-based expansion |
| [[sources/pxd-color-token-design-2026|pxd: Color Token Design Patterns]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/pxd-story-ai-insights|pxd story: AI & UX Insights]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/quantuxblog|Quantitative UX Research Blog]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/rapport-labs-ai-ux-writing|AI UX Writing Principles (Rapport Labs)]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/saeidehbakhshi-long-accommodation|Saeideh Bakhshi: The Long Accommodation]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/saeidehbakhshi-the-fallacy-of-depth-at-scale|The Fallacy of Depth at Scale]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/saeidehbakhshi-wicked-work-ai-unbundles-research|Saeideh Bakhshi: The Wicked Work That Surfaces When AI Unbundles Research]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/sage-10778004251401851-genai-reflexive-qualitative-research|SAGE: Rejecting GenAI for Reflexive Qualitative Research]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/teams-message-1778509897273|Microsoft Teams Message Placeholder]] | `standard` | `partial` | `false` | `true` | raw-based expansion, concept links |
| [[sources/theaxlabs-contaminated-memory-performance|AX LABS: Contaminated Memory Eats Away Performance]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/toss-tech-research-platform-ai|Source: Toss Tech ??Huribot Story #1]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/zdnet-dell-ai-native|Source: Dell Vice Chairman Jeff Clarke: "AI-Native Transition"]] | `standard` | `partial` | `false` | `false` | raw provenance, raw-based expansion |
| [[sources/atlassian-ai-prototyping-handshakes|Atlassian: Handoffs into Handshakes (AI Prototyping at Scale)]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/figma-mcp-server-four-ways|Figma: 4 Ways We're Using Our MCP Server]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/aidesign-guide-catalog|The AI Design Guide (Resource Directory)]] | `light` | `partial` | `false` | `true` | resource pointer; not citable evidence |
| [[sources/bayer-prince-reliable-agentic-ai|Bayer PRINCE: Building Reliable Agentic AI Systems]] | `deep` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/fowler-sensors-coding-agents|Böckeler: Maintainability Sensors for Coding Agents]] | `deep` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/hai-cooperbench-agent-teamwork|CooperBench: AI Coding Agents Fail at Teamwork]] | `standard` | `substantial` | `true` | `true` | preprint write-up; verify vs arXiv 2601.13295 |
| [[sources/hai-headlines-ai-news-audit|Real-Time Audit of Six Commercial News Chatbots]] | `standard` | `substantial` | `true` | `true` | preprint write-up; verify vs arXiv 2605.22785 |
| [[sources/guanjie-li-llm-user-proxy|Li: What LLMs Can and Cannot Find in Interview Transcripts]] | `deep` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/nngroup-design-process-compressed|NN/g: Design Process Isn't Dead, It's Compressed]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/trevor-calabro-ux-research-as-a-service|Calabro: UX Research as a Service]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/ada-kim-satisfaction-vs-benefit-ai|Kim: Satisfaction vs Actual Benefit in AI Use]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/kevin-newton-uxr-three-jobs|Newton (2026): UX Research Is Splitting Into Three Jobs]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/acm-dis2026-algorithmic-self-portraits|Lee et al. (2026): Algorithmic Self-Portraits (TubeLens), DIS '26]] | `standard` | `substantial` | `true` | `true` | full ingest (PDF preserved); deepen findings on demand |
| [[sources/ipsos-trust-ultimate-wireframe|Ipsos: Trust as the Ultimate Wireframe]] | `light` | `partial` | `false` | `true` | Ceros report not rendered; thesis only |
| [[sources/vibe-coding-agent-security-evaluation-day-4|Day 4 — Vibe Coding Agent Security & Evaluation]] | `deep` | `substantial` | `true` | `true` | security half deep; deepen evaluation half |
| [[sources/spec-driven-production-development-day-5|Day 5 — Spec-Driven Production-Grade Development]] | `deep` | `substantial` | `true` | `true` | first half deep; deepen zero-trust/policy section |
| [[sources/bakhshi-representative-sample|Bakhshi (2026): There Is No Such Thing as a Representative Sample]] | `standard` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/bakhshi-ai-in-qualitative-research-map|Bakhshi (2026): AI in Qualitative Research — A Map]] | `deep` | `substantial` | `true` | `true` | ready for grounded ideation |
| [[sources/svenja-pieritz-positioning-experiment|Pieritz (2026): Positioning Experiment (relevance vs intent)]] | `standard` | `substantial` | `true` | `true` | directional; underpowered self-study |
| [[sources/myrealtrip-polaris-cancellation-recommendation|Myrealtrip "Polaris": Cancellation → Next Trip]] | `standard` | `substantial` | `true` | `true` | ~70% lift is observational, not causal |
| [[sources/yozm-ai-prd|Yozm IT (2026): What an AI PRD Must Do Differently]] | `standard` | `substantial` | `true` | `true` | full via summary; verbatim re-capture optional |
| [[sources/langchain-multi-agent-architecture|LangChain: Choosing the Right Multi-Agent Architecture]] | `standard` | `substantial` | `true` | `true` | vendor blog; 4 patterns + scenario perf |
| [[sources/langchain-loop-engineering|LangChain: The Art of Loop Engineering]] | `standard` | `substantial` | `true` | `true` | vendor blog |
| [[sources/langchain-custom-agent-harness|LangChain: How to Build a Custom Agent Harness]] | `standard` | `substantial` | `true` | `true` | vendor blog; deepens harness-engineering |
| [[sources/langchain-verifiers-legal-agents|LangChain: Designing Efficient Verifiers for Legal Agents]] | `standard` | `substantial` | `true` | `true` | vendor blog; cost/RL charts image-only |
| [[sources/langchain-predictable-coding-agent-spend|LangChain: Making Coding-Agent Spend Predictable]] | `standard` | `substantial` | `true` | `true` | vendor blog |
| [[sources/langchain-model-neutrality|LangChain: Why Model Neutrality Matters More Than Cloud]] | `standard` | `substantial` | `true` | `true` | vendor blog |
| [[sources/langchain-box-ai-deep-agents|Box × LangChain: AI-Native with Deep Agents]] | `standard` | `substantial` | `true` | `true` | customer story; no independent metrics |
| [[sources/langchain-lyft-support-agent-platform|Lyft × LangChain: Self-Serve Support Agent Platform]] | `standard` | `substantial` | `true` | `true` | customer story; baseline-metrics table image-only |
| [[sources/langchain-agent-middleware|LangChain: Agent Middleware (1.0 origin post)]] | `standard` | `substantial` | `true` | `true` | canonical source for the Agent Middleware concept |
| [[sources/langchain-background-subagents|LangChain: Running Subagents in the Background]] | `standard` | `substantial` | `true` | `true` | vendor blog |
| [[sources/langchain-interpreter-skills|LangChain: Interpreter Skills]] | `standard` | `substantial` | `true` | `true` | vendor blog |
| [[sources/langchain-agent-authorization|LangChain: Two Types of Agent Authorization]] | `standard` | `substantial` | `true` | `true` | maps to Day-4 confused-deputy / identity |
| [[sources/langchain-eu-ai-act|LangChain: LangSmith / OSS & the EU AI Act]] | `standard` | `substantial` | `true` | `true` | governance; article-crosswalk table captured |
| [[sources/langchain-evaluating-deep-agents|LangChain: Evaluating Deep Agents]] | `standard` | `substantial` | `true` | `true` | vendor blog; 3×3 eval matrix |
| [[sources/langchain-exa|Exa × LangChain: Agentic Search]] | `standard` | `substantial` | `true` | `true` | partner story; ops metrics only, no quality numbers |
| [[sources/measuringu-types-of-synthetic-users|MeasuringU (2026): Types of Synthetic Users]] | `standard` | `substantial` | `true` | `true` | provisional 5-type taxonomy; verbatim defs optional |
| [[sources/dusskapark-product-designer-codex|Park (2026): How Far Can a Designer Build with Codex?]] | `standard` | `substantial` | `true` | `true` | single strong case study; no metrics |
| [[sources/toss-tossplace-ai-surf-day|TossPlace (2026): AI Surf Day (EP.2)]] | `standard` | `substantial` | `true` | `true` | EP.2 body JS-blocked; reconstructed from Toss Tech companion |
| [[sources/google-good-seo-is-good-geo|Kraham / Google (2026): Good SEO is Good GEO]] | `standard` | `substantial` | `true` | `true` | first-party Google; cross-engine claims unproven |
| [[sources/yozm-obsidian-llm-wiki-secondbrain|Gom's IT Blog (2026): Obsidian LLM Wiki (this vault's blueprint)]] | `standard` | `substantial` | `true` | `true` | meta-source for this vault's architecture |
| [[sources/maily-product-makers-planning-harness|Product Makers Note (2026): Planning Harness]] | `standard` | `substantial` | `true` | `true` | practitioner how-to; efficacy unproven |
| [[sources/kakao-vc-ai-input-modality|Kakao Ventures (2026): Input Modality on Wearables]] | `standard` | `substantial` | `true` | `true` | VC thesis; framing lens, no market data |
| [[sources/theaxlabs-hanwha-life-claude-code-pbl|AX LABS × Hanwha Life (2026): 6-week Claude Code PBL]] | `standard` | `substantial` | `true` | `true` | vendor case; success-biased, no hard metrics |
| [[sources/carrotcap-naver|Naver blog carrotcap (post 224326504833)]] | `light` | `partial` | `false` | `false` | host blocked + unindexed; needs user-supplied text |
| [[sources/imweb-safe-llm-generated-sql|Imweb (2026): How to Safely Use SQL Written by AI]] | `standard` | `substantial` | `true` | `true` | deterministic Text-to-SQL safety harness; vendor CBT metrics |
| [[sources/naverlabs-europe-divine-encoder|Naver Labs Europe: DIVINE Universal Encoder]] | `standard` | `substantial` | `true` | `true` | multi-teacher distillation; vendor metrics, original URL pending |
| [[sources/lennys-newsletter-new-inner-game|Hudson (2026): The New Inner Game]] | `standard` | `substantial` | `true` | `true` | ~75% captured (self-talk how-to paywalled); coaching essay |
| [[sources/heyratel-ios-ai-agent-environment|HeyRatel (2026): Not a Tool but a Standard (iOS agent env)]] | `standard` | `substantial` | `true` | `true` | single-team field report; qualitative, no metrics |
| [[sources/datarize-intelligence-to-autonomy|Datarize (2026): From Intelligence to Autonomy]] | `standard` | `substantial` | `true` | `true` | vendor marketing; ROAS/lift unaudited |
| [[sources/yozm-tiro-ax-ontology|Yozm × The Plato (2026): Ontology for AX from Meeting Records (Tiro)]] | `standard` | `substantial` | `true` | `true` | branded content; vendor metrics unverified |
| [[sources/hai-algorithmic-hiring-bias|Stanford HAI (2026): AI Hiring Bias & Systemic Rejection]] | `standard` | `substantial` | `true` | `true` | news write-up; verify figures vs paper |
| [[sources/brunch-ponyodesign-llm-wiki-clone|ponyodesign (2026): Self-Mirroring Obsidian LLM Wiki]] | `standard` | `substantial` | `true` | `true` | personal blog; qualitative |
| [[sources/voiceofuser-inhouse-digital-twins-blueprint|The Voice of User (2026): In-House Digital-Twins Blueprint]] | `standard` | `substantial` | `true` | `true` | strong build+validation recipe; embedded study figures untraced to primaries |
| [[sources/kakao-vc-ai-companion-relationship|Kakao Ventures (2026): AI Companion — Relationship Depth Determines the BM]] | `standard` | `substantial` | `true` | `true` | VC thesis; thin hard data (Neuro-sama 160k figure is the article's own) |
| [[sources/uxfolio-ai-ux-design|UXfolio (2026): AI UX Design — Strategic Blueprint]] | `standard` | `substantial` | `true` | `true` | vendor/promotional; framework & vocabulary, not evidence |
| [[sources/drs2026-generative-events-design-ontology|Yu & Zhao (2026): Generative Events (DRS2026)]] | `light` | `partial` | `true` | `true` | abstract-only; full PDF not ingested |
| [[sources/opencut-open-source-video-editor|OpenCut: Open-Source Video Editor (OpenAlternative listing)]] | `light` | `partial` | `true` | `true` | off-theme tool listing; repo/site not captured directly |
| [[sources/brox-digital-twins-market-research|Brox (2026): 60,000 "digital twins" of real people (VentureBeat)]] | `light` | `partial` | `false` | `true` | vendor-PR; body blocked (403/429), reconstructed; numbers are company claims, no independent validation |
| [[sources/christinevallaure-agentic-ai-design-systems|Vallaure (2026): Agentic AI, Design Systems & Figma — A Practical Guide]] | `standard` | `substantial` | `true` | `true` | practitioner checklist; Figma-specific, time-sensitive, soft commercial incentive |
| [[sources/christinevallaure-a2ui-generative-ui|Vallaure (2026): A2UI Under the Hood — Radically Adaptive UI]] | `standard` | `substantial` | `true` | `true` | designer primer on the A2UI generative-UI protocol; emerging spec |
| [[sources/christinevallaure-hypertokens|Vallaure (2026): What Are Hypertokens? (coined by Jake Albaugh, Config 2026)]] | `standard` | `substantial` | `true` | `true` | forward-looking/unshipped; benefit claim is a single demo |
| [[sources/christinevallaure-human-approach-agentic-ai|Vallaure (2026): A Human Approach to Agentic AI — One Person, One File, Five Agents]] | `standard` | `substantial` | `true` | `true` | practitioner n=1 narrative; book teaser |
