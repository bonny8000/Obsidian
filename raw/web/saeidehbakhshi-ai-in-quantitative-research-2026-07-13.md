---
title: "AI in Quantitative Research"
source: "https://saeidehbakhshi.substack.com/p/ai-in-quantitative-research"
date: "2026-07-13"
tags:
  - article
  - ai
  - quantitative-research
---
***A note before we start:** I recently wrote a methodological deep dive on [state of AI in qualitative research](https://saeidehbakhshi.substack.com/p/ai-in-qualitative-research-a-map) and many people reached out and asked me to write a similar map for quantitative research. This is my attempt and it is fairly long.*

For much of the field’s history, quantitative work was constrained by knowledge of methods and execution. Someone had to collect the right data or find the right table, understand its schema, clean the data, write the query, debug the join, choose and fit a model, make a chart, and prepare the readout. These steps required technical skill, access to specialized tools, and time. Generative and agentic systems are reducing that cost.

This is a real benefit because quantitative specialists have often become bottlenecks because the number of questions an organization wants answered is much larger than the number of people available to answer them. AI can reduce a meaningful share of this execution work. It also changes the basis on which quantitative specialists distinguish their contribution.

When many people can produce a query, chart, model, forecast, or classification, the artifact itself tells us less about the quality of the reasoning behind it. A technically correct analysis can still use the wrong population, encode a weak measure, condition on the wrong event, overlook a logging change, or support a narrower conclusion than the accompanying explanation suggests.

![](https://substackcdn.com/image/fetch/$s_!ghoD!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F91646a86-ed1c-4e27-8af2-002a1a44dc16_1448x993.png)

**An analysis is an artifact**: a query, table, model, chart, forecast, classification, or explanation. **Evidence is the connection between that artifact and the claim made from it.** That connection depends on how the data were produced, what the variables represent, which comparison gives the result meaning, what assumptions are required, and which sources of uncertainty remain.

> **AI is becoming very good at helping produce the artifact. That creates an opportunity for quantitative practitioners to spend more of their time on the surrounding work that determines whether the artifact is useful: specifying the question, constructing the measure, designing the comparison, validating model-derived variables, preserving the path through the analysis, and stating the conclusion at the level the design can support.**

## 1\. Producing the analysis is only part of answering the question

Consider a team asking why new-user retention declined. An AI system may identify relevant tables, define a cohort, generate SQL, compare segments, create a chart, fit a model, and summarize possible explanations. The workflow could save days of work and surface patterns a person may not have thought to examine.

The conclusion still depends on choices that have little to do with whether the SQL runs. A new user might mean account creation, first transaction, first successful session, or first meaningful use. Retention might mean reopening the product, completing a core action, or continuing to receive value. A logging change could alter the trend. An identity migration could affect cross-device stitching. A marketing campaign could change the mix of users. The system may have searched many segments and time windows before returning the clearest pattern.

**The chart may be accurate while the explanation remains unsettled.**

![](https://substackcdn.com/image/fetch/$s_!Pwz2!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe7c116d7-c633-482c-92e2-1f52c5677ebd_1448x1086.png)

These choices have always been part of quantitative work. They were often discovered during execution. Writing a query might reveal that two teams use different definitions of an active user. Cleaning survey data might show that respondents interpreted a scale differently than intended. Fitting a model might expose that a predictor is recorded only after the outcome. The challenge is to reduce the labor without allowing consequential definitions, exclusions, and assumptions to pass unnoticed.

**Current benchmarks show how much quantitative analysis depends on this context.**

[Spider 2.0](https://proceedings.iclr.cc/paper_files/paper/2025/hash/46c10f6c8ea5aa6f267bcdabcb123f97-Abstract-Conference.html) contains 632 realistic enterprise text-to-SQL workflows involving large schemas, multiple SQL dialects, and messy business context. An agent built on a strong reasoning model solved 21.3 percent of the tasks. That number will improve as systems and agent scaffolding mature, but the shape of the difficulty is instructive. The system had to find the relevant data, interpret organizational definitions, navigate complex environments, and coordinate several steps without losing the original question.

Similarly, on [StatQA](https://proceedings.neurips.cc/paper_files/paper/2024/file/729786203d330da046dd8091c2d92a66-Paper-Datasets_and_Benchmarks_Track.pdf), models were often better at recognizing familiar statistical tasks than at determining whether a method fit the variables, assumptions, and question. In [BLADE](https://aclanthology.org/2024.findings-emnlp.815/), systems frequently produced executable analyses while capturing only a fraction of the analytical decisions identified by experts.

These findings show why clear task definition and relevant context matter. Producing an analysis and determining what the analysis should represent remain connected but distinct parts of the work.

## 2\. The role AI plays determines how it should be validated

Studies of AI-assisted quantitative work can appear contradictory because they evaluate very different roles under the same broad question: did the model work?

Similar to my argument in how we should approach the [role of AI in qualitative research](https://open.substack.com/pub/saeidehbakhshi/p/ai-in-qualitative-research-a-map), I encourage us to pay attention to what role the system is playing, whether its output becomes part of the evidence, and what independent reference is available to check it.

AI may perform a constrained transformation, create a measure, expand an exploratory search, predict an outcome, or represent a population. Each use can be productive, but the validation requirements differ.

### 2.1 Constrained transformations

AI is already valuable for drafting SQL, transforming data, translating code, generating documentation, applying an explicit codebook, creating diagnostics, and producing a first visualization.

These tasks are well suited to assistance because the output can be checked against an external reference or ground truth. A [2026 working paper](https://www.iser.essex.ac.uk/research/publications/publication-589050) evaluated several LLM approaches on questions containing deliberately embedded problems. It identified 75% of the known issues with a small false-positive rate.

Text classification follows the same pattern. In a widely cited [PNAS study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10372638/), GPT-3.5 performed well on bounded tasks involving relevance, stance, topic, and framing, often matching or exceeding crowd-worker accuracy. Another study found that the strongest LLM approached human performance when coding open-ended election-survey responses into a [50-category codebook](https://journals.sagepub.com/doi/10.1177/20531680241231468).

These settings provide a source response, an explicit codebook, independently labeled cases, and an **observable error**.

### 2.2 Model-derived measurement

The stakes change once model output becomes a variable in the dataset.

Suppose a system converts customer-support messages into labels such as “confusing policy,” “resolution failure,” or “lack of transparency.” This can make large amounts of unstructured information available for quantitative study, allowing teams to estimate prevalence, compare groups, and examine relationships with later behavior.

The generated label is still a measure, and its errors enter the analysis.

A [NeurIPS paper on imperfect surrogate labels](https://proceedings.neurips.cc/paper_files/paper/2023/file/d862f7f5445255090de13b825b880d59-Paper-Conference.pdf) showed that directly substituting predicted labels into downstream analysis can produce biased estimates and invalid confidence intervals even when classification accuracy appears strong. What matters is how the errors relate to the quantity being estimated.

More promising approaches retain independent human evidence. A 2025 [confidence-driven inference method](https://aclanthology.org/2025.naacl-long.179/) used model confidence to allocate limited human annotation while preserving valid intervals in the tasks studied. Model output reduced labeling effort, while strategically collected reference data supported the final estimate.

> **This is an important direction for quantitative work. Models can help measure previously inaccessible constructs at much greater scale. Quantitative practitioners then need to determine how much reference data are required, where performance varies, and how uncertainty in the generated measure affects downstream conclusions.**

### 2.3 Exploration and forecasting

AI can also expand the set of possibilities a team considers.

A system can propose hypotheses, suggest interactions, identify unusual segments, rehearse survey questions, generate candidate features, forecast experimental outcomes, and scan large sets of metrics for changes.

A researcher might use it to anticipate how respondents could interpret a question. A data scientist might generate candidate model specifications. An experimentation team might compare forecasts before choosing what to test. An analyst might use it to surface unexpected shifts across hundreds of metrics.

These outputs direct attention and identify where additional analysis or data collection may be worthwhile. They can improve what a team chooses to study without being treated as final confirmation of the pattern or explanation they suggest.

### 2.4 Representing people and populations

The most demanding uses ask a model to represent people, populations, counterfactual outcomes, or causal explanations.

Synthetic respondents are a clear example. A model can complete a survey, react to a concept, adopt a persona, and produce a dataset with any requested subgroup balance. The result may be informative, but its relationship to the target population still has to be established.

This is very important and worth going deeper into separately.

## 3\. Synthetic data can rehearse, forecast, augment, or substitute

The appeal for synthetic respondents is easy to understand. Recruiting participants is slow and expensive. A model can produce responses in seconds. Those responses can sound thoughtful, generate realistic-looking distributions, and allow researchers to explore groups that would otherwise be costly to recruit.

A simulated sample is still a different source of information from a sample of people.

### 3.1 A plausible population is not an observed population

In a major [Political Analysis study](https://www.cambridge.org/core/journals/political-analysis/article/synthetic-replacements-for-human-survey-data-the-perils-of-large-language-models/B92267DC26195C7F36E63EA04A47D2FE), researchers generated more than 3.6 million model responses corresponding to 7,530 participants in the American National Election Studies. Some synthetic averages resembled the human survey averages. The models also produced too little variation, many regression relationships differed, and the results changed with prompt wording and model updates.

> **These differences matter because quantitative studies rarely aim only to recover a plausible average. We often care about distributions, relationships, subgroup differences, rare needs, threshold effects, behavioral constraints, and the gap between stated intention and later action. A system may reproduce a topline while representing the structure underneath it differently from the target population. The response process is also part of the measurement.**

An evaluation of [nine language models on established survey-response effects](https://aclanthology.org/2024.tacl-1.56/) found that the models generally did not reproduce human response-bias patterns and sometimes reacted to small perturbations that did not meaningfully change human answers. **A model can produce an answer that resembles a survey response without following the same process through which a person interprets a question, retrieves an experience, forms a judgment, and maps that judgment onto a scale.**

Adding demographic detail to a persona does not necessarily solve this problem. A [Nature Machine Intelligence study](https://www.nature.com/articles/s42256-025-00986-z) compared four models with 3,200 people across 16 identities. Model-generated representations sometimes misportrayed groups and compressed variation within them. A highly specific persona may appear individualized while still reflecting a simplified representation of the group.

Behavior is harder to reproduce than a plausible survey response. In a [2026 ACL study](https://aclanthology.org/2026.acl-long.2034/) based on 31,865 real online shopping sessions, the strongest prompt-only agents predicted the next recorded human action with 11.86 percent accuracy. Fine-tuning on real click-through behavior improved performance, but exact behavioral fidelity remained limited. This illustrate the difference between behavior that appears believable and behavior observed under real constraints.

### 3.2 Models may still be useful forecasters

Other research shows that models can be useful for forecasting human outcomes. A July 2026 [Nature study](https://www.nature.com/articles/s41586-026-10742-x) used GPT-4 to forecast results across 70 preregistered, nationally representative U.S. survey experiments covering 469 effects and 119,330 participants. The predicted effects correlated strongly with the observed effects and performed similarly to pooled human forecasts.

That capability could help researchers prioritize pilots, identify surprising outcomes, and decide which interventions deserve experimental capacity. The forecast informs empirical work, but it comes from a different process than the experiment itself.

### 3.3 The four roles of Synthetic data

I find it useful to distinguish four roles for synthetic data: rehearsal, forecasting, augmentation, and substitution.

#### Rehearsal

In rehearsal, also variations of this called as digital twins, synthetic participants help test an instrument, identify possible interpretations, broaden a hypothesis set, or surface overlooked questions.

#### Forecasting

In **forecasting**, a model estimates which result is likely or which intervention may be most promising, helping researchers allocate effort.

#### Augmentation

In **augmentation**, generated data are combined with real observations that provide calibration and correction. A [2026 ACL study of survey simulation with limited human data](https://aclanthology.org/2026.acl-long.498/) evaluated two panel surveys across nutrition, politics, and economics. Synthesis alone introduced biases ranging from 24 to 86 percent. Combining synthetic responses with statistical rectification based on reserved human responses reduced bias below 5 percent and increased effective sample size by as much as 14 percent in the studied settings. The real responses were central to the method. They allowed the synthetic data to be corrected and gave the final estimates an empirical reference.

#### Substitution

In **substitution**, generated observations stand in for observations from the target population. This requires much stronger evidence because the model is supplying the data on which the population claim depends. The evidence I reviewed does not yet support treating generated observations as a general substitute for observations from a target population. That may change in particular settings, but it needs to be demonstrated against real outcomes rather than inferred from the plausibility of the responses.

![](https://substackcdn.com/image/fetch/$s_!AW-x!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff8151540-5840-4815-a639-3deafe01e72b_1448x1086.png)

These roles may overlap, but they should not be treated as equivalent simply because they produce similar-looking rows.

### 3.5 Human-generated data are also changing

Even the category of human-generated data is becoming less clear. In a [2025 study of online research participants](https://journals.sagepub.com/doi/10.1177/00491241251327130), 34 percent reported using LLMs to help answer open-ended survey questions. The researchers found that model-generated answers were more homogeneous and, in several comparisons, more positive.

Participants may use AI for translation, accessibility, writing support, effort reduction, or social presentation. Excluding every assisted response would be difficult and may be undesirable in some settings. The observation nevertheless reflects a person working with a model, which may matter for interpretation.

**Provenance is therefore becoming part of measurement. Quantitative practitioners will increasingly need to distinguish among behaviorally observed, human-reported, AI-assisted, model-derived, simulated, and mixed evidence.**

Generating ten thousand rows does not create ten thousand independent observations from a population. Repeated generations may reduce simulation noise, but they do not automatically address population coverage, calibration, prompting, or model behavior.

## 4\. Faster exploration requires a visible analytical path

AI can examine more outcomes, windows, segments, exclusions, transformations, and model specifications than a person could reasonably evaluate by hand. That wider search can reveal patterns that would otherwise be missed. It can also obscure how the final result was selected.

Suppose a system examines five outcomes, four time windows, eight segments, several exclusion rules, and multiple models, then returns one clean chart with a conventional confidence interval. The interval describes uncertainty within the selected analysis. It does not usually account for the full search that produced it.

> **Researcher degrees of freedom are not new. AI increases the speed and scale at which they can be exercised.**

Many organizational questions create large search spaces. “Why did engagement fall?” may involve different behaviors, populations, periods, segments, models, and explanations. “What drives dissatisfaction?” may lead to many survey items, support experiences, behavioral events, and demographic comparisons. “Which users are likely to churn?” may produce an accurate prediction while saying little about what would prevent churn.

The system is expected to return something useful, and the team wants an answer it can act on. A good workflow should distinguish exploration from confirmation. Important decisions may still require a new holdout, replication, preregistration, or methods that account for multiple comparisons and model selection.

![](https://substackcdn.com/image/fetch/$s_!Q6NN!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc588b777-81b0-40b2-808d-7e9e5bf81df5_1448x1086.png)

Verification also becomes harder as a system produces more of the workflow. A [CHI study of 22 professional analysts](https://www.microsoft.com/en-us/research/publication/how-do-analysts-understand-and-verify-ai-assisted-data-analyses/) found that people moved among explanations, code, charts, and interactive tables to check AI-generated analyses. No single representation provided a sufficient audit trail. A chart might expose a strange distribution hidden by the prose. Code might reveal an unseen filter. A source table might show that a correct-looking result used the wrong unit of analysis.

A person reviewing the final slide is technically in the loop. That does not mean they have seen the choices that determined the result.

**As analytical production becomes faster, review has to be built into the workflow. Metric definitions, model-derived variables, exclusions, prompts, alternative specifications, and changes to the analytical plan should remain accessible when they materially affect the conclusion.**

The goal is to keep consequential choices from disappearing behind a polished final output.

## 5\. What quantitative experts should own

If analytical execution becomes widely accessible, quantitative practitioners will have a harder time defining their value through exclusive control of the tools.

SQL, modeling, survey design, experimentation, and visualization still matter. The ability to use these methods well will remain important, especially for complex or high-stakes work. What changes is that producing the first analytical artifact becomes a smaller share of the total contribution.

![](https://substackcdn.com/image/fetch/$s_!fPDy!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0a5499a9-12ad-485c-b356-2dc7d642ca67_1438x954.png)

I see four parts of quantitative work becoming more central.

### 5.1 Formulate the actual question

Many requests sound more defined than they are: measure trust, find the drivers of churn, explain a decline, or determine whether a launch worked.

Part of quantitative expertise is clarifying the population, outcome, comparison, time horizon, and decision before the analysis begins. AI can make it easier to move quickly from a broad request to a specific answer. The practitioner’s role is to make sure it is the right answer to the question the team needs to solve.

### 5.2 Treat measurement as part of the analysis

Organizations are likely to produce more metrics, scores, classifications, segments, and synthetic variables as AI-assisted analysis becomes common.

**The meaning of those measures cannot be assumed.**

An engagement metric may mostly reflect notifications. A trust score may combine confidence, safety, reliability, and familiarity in ways that obscure meaningful differences. A generated support label may work well in English and poorly in another language. A behavioral segment may be stable for three months and disappear after a product redesign.

**Quantitative practitioners will need to spend more time evaluating what a metric represents, how it changes across contexts and groups, and whether it is suitable for the decision being made.**

### 5.3 Build validation into recurring workflows

Reviewing every AI-assisted output by hand will not scale. The more durable contribution is to build validation into the systems that produce the analysis.

A team can maintain reference datasets for important classifiers. Recurring metrics can include checks for logging changes, missing events, and shifts in population composition. Experiment templates can require teams to specify primary outcomes and decision rules. Forecasts can be evaluated against observed results. Synthetic data can remain visibly separate from observed data. Exploratory tools can retain the set of tested analyses rather than showing only the selected result.

**Different fields will build different checks. The general principle is to make them repeatable and available at the point where the work is done.**

This allows AI to be used more widely without placing a quantitative specialist at the end of every workflow as a final approver.

### 5.4 Determine what the conclusion can say

The final product of an analysis is usually an inference for making claims.

A team may conclude that a feature increased retention, that a customer experience caused dissatisfaction, that a segment represents an unmet need, or that an intervention will improve an outcome. The language often becomes stronger as the finding moves away from the analyst and into a roadmap, strategy document, or leadership presentation.

Quantitative practitioners have an important role in keeping the statement connected to the design of the research. I’ve written about the practice of taking care of making claims [here](https://saeidehbakhshi.substack.com/p/the-discipline-of-making-claims-data). It’s on us to state the conclusion the design supports and identify the additional evidence a stronger one would need.

## 6\. Evidence engineering is the future of our role

I think of the work described throughout this piece as **evidence engineering**.

Evidence engineering includes specifying questions, constructing measures, validating model-derived variables, preserving the analytical path, and calibrating conclusions. It is not a new profession. It describes work that already exists across data science, analytics, experimentation, market research, quantitative research, statistics, and economics, and it becomes more visible as analysis is distributed more broadly.

A model may draft the first query, but someone has to confirm the denominator and unit of analysis. It may propose a segmentation, but someone has to determine whether the groups are stable, meaningful, and useful for a decision. It may classify unstructured data, but someone has to study the error and its effect on downstream estimates. It may forecast an experiment, but someone has to determine how much empirical evidence is still required. It may generate several explanations, but the team still needs data that can distinguish among them.

These responsibilities do not require quantitative specialists to reject automation or protect tasks that no longer need to be done manually. The value comes from using the new capability without losing the parts of the work that connect an output to reality.

**As more people become capable of producing an analysis, quantitative expertise becomes less about access to the tools and more about responsibility for what the analysis is allowed to mean.**

## References

In order of appearance:

1. Spider 2.0, a benchmark of 632 enterprise text-to-SQL workflows. ICLR 2025. [proceedings.iclr.cc](https://proceedings.iclr.cc/paper_files/paper/2025/hash/46c10f6c8ea5aa6f267bcdabcb123f97-Abstract-Conference.html)
2. StatQA, a benchmark for statistical method selection and application. NeurIPS 2024, Datasets and Benchmarks Track. [proceedings.neurips.cc](https://proceedings.neurips.cc/paper_files/paper/2024/file/729786203d330da046dd8091c2d92a66-Paper-Datasets_and_Benchmarks_Track.pdf)
3. BLADE, a benchmark evaluating agents on the analytical decisions in data-driven science. Findings of EMNLP 2024. [aclanthology.org](https://aclanthology.org/2024.findings-emnlp.815/)
4. Working paper evaluating LLM approaches to survey pretesting against questions with deliberately embedded problems. Institute for Social and Economic Research, University of Essex, 2026. [iser.essex.ac.uk](https://www.iser.essex.ac.uk/research/publications/publication-589050)
5. Study of GPT-3.5 performance on text-annotation tasks (relevance, stance, topic, framing) against crowd workers. PNAS, 2023. [pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC10372638/)
6. Study of LLM coding of open-ended election-survey responses into a 50-category codebook. Research & Politics, 2024. [journals.sagepub.com](https://journals.sagepub.com/doi/10.1177/20531680241231468)
7. Paper on bias and invalid confidence intervals from substituting imperfect surrogate labels into downstream analysis. NeurIPS 2023. [proceedings.neurips.cc](https://proceedings.neurips.cc/paper_files/paper/2023/file/d862f7f5445255090de13b825b880d59-Paper-Conference.pdf)
8. Confidence-driven inference method for allocating limited human annotation alongside model output. NAACL 2025. [aclanthology.org](https://aclanthology.org/2025.naacl-long.179/)
9. “Synthetic Replacements for Human Survey Data? The Perils of Large Language Models.” Political Analysis. [cambridge.org](https://www.cambridge.org/core/journals/political-analysis/article/synthetic-replacements-for-human-survey-data-the-perils-of-large-language-models/B92267DC26195C7F36E63EA04A47D2FE)
10. Evaluation of nine language models on established survey-response effects and response-bias patterns. TACL, 2024. [aclanthology.org](https://aclanthology.org/2024.tacl-1.56/)
11. Study comparing four models with 3,200 people across 16 identities on group portrayal and within-group variation. Nature Machine Intelligence, 2025. [nature.com](https://www.nature.com/articles/s42256-025-00986-z)
12. Study of agent prediction of human actions across 31,865 real online shopping sessions. ACL 2026. [aclanthology.org](https://aclanthology.org/2026.acl-long.2034/)
13. Study using GPT-4 to forecast results across 70 preregistered, nationally representative U.S. survey experiments. Nature, 2026. [nature.com](https://www.nature.com/articles/s41586-026-10742-x)
14. Study of survey simulation combining synthetic responses with statistical rectification from reserved human data. ACL 2026. [aclanthology.org](https://aclanthology.org/2026.acl-long.498/)
15. Study of LLM use among online research participants in open-ended survey responses. Sociological Methods & Research, 2025. [journals.sagepub.com](https://journals.sagepub.com/doi/10.1177/00491241251327130)
16. CausalPitfalls, a benchmark of LLM performance on confounding, selection bias, mediation, counterfactual reasoning, and external validity. arXiv, 2025. [arxiv.org](https://arxiv.org/abs/2505.13770)
17. “How Do Analysts Understand and Verify AI-Assisted Data Analyses?” Study of 22 professional analysts. Microsoft Research, CHI. [microsoft.com](https://www.microsoft.com/en-us/research/publication/how-do-analysts-understand-and-verify-ai-assisted-data-analyses/)