AI applications are only as good as the information they reason from. Without fresh, high-quality web data, they are less dependable. Today, Microsoft is launching [Web IQ](https://aka.ms/WebIQ): a suite of AI-native grounding APIs built for the agentic era, connecting AI systems and agents to fresh, real-world intelligence from across the web — including web pages, news, images, and videos.  
  
The systems that define the agentic era will be the ones that can retrieve fresh, authoritative evidence quickly, transform it into useful context, and do so within the latency and efficiency budgets that multi-step reasoning demands.  
  
Model capability alone no longer determines whether an AI system is useful. What matters is how effectively the full system connects models to the world, including information created after models were trained, and information too vast to encode in model weights.  
  
Web IQ is a search engine for AI systems. Where Bing was built to help people search the web, Web IQ is built to help AI agents find the right information, turn it into useful evidence, and use it inside reasoning. Unlike other APIs that layer on top of fragile infrastructure, Web IQ is a new kind of search system, one that delivers the right evidence with the speed, quality, and efficiency modern agents require.  
  
It builds on years of learning from Bing, but it required a major ground-up re-architecture to meet the demands of agentic workloads.

## Built on Bing, Re-Architected for the Agentic Era

Web IQ starts from the foundation Microsoft has been building for decades: the Bing global index and ecosystem. Grounding quality depends on the breadth, freshness, and trustworthiness of the world representation underneath it – something that is achieved by building on Bing’s expansive reach.  
  
But the agentic era asks fundamentally different questions of the stack. Agents do not issue a single search and stop. They retrieve repeatedly, reason over evidence, adapt to new information, and operate inside tight latency budgets. Meeting those requirements could not be solved by tuning a single component. It required re-architecting the system from the ground up from indexing and retrieval to ranking, passage selection, and orchestration so every layer is aligned around the needs of inference-time grounding. That is the core idea behind Web IQ: preserve the strengths of Bing’s foundation while redesigning the grounding stack to serve as the execution fabric for AI agents.  
  
![Shows the high-level architecture of Web IQ](https://blogs.bing.com/getmedia/c3d2bb9e-757b-4b60-935b-a9ddcec68c4a/WebIQ1.png)

### At the base of this system is something that predates Web IQ by many years: the Bing global index and ecosystem.

Evolving beyond a large crawl, it is a continuously refined representation of the web, built over decades through a combination of infrastructure, partnership, and discipline. It reflects millions of decisions about what to include, how to rank it, how to ensure freshness, and how to maintain trust.  
  
That discipline extends to how we participate in the open web itself. Web IQ inherits Bing’s long-standing commitment to the conventions and evolving standards of the internet ecosystem, including honoring robots exclusion protocols, publisher controls, and access preferences that govern how content can be discovered, accessed, and used. We are actively engaging with the broader ecosystem through the IETF and other industry forums to help evolve interoperable standards for the AI era. Our goal is to be a sincere and trusted participant in the open web — one that respects publisher choice and helps sustain a healthy ecosystem for content providers, advertisers, developers, and users alike.  
  
The role of that foundation is often underestimated. Grounding systems cannot exceed the quality of the world they observe. If the index is incomplete, stale, or unreliable, no amount of modeling can compensate. Web IQ begins from the premise that grounding quality is anchored in the quality of the underlying corpus and that corpus must be global, fresh, honor publisher preferences by default, and continuously evolving.

### On top of that foundation sits the model layer, where we made a different kind of decision.

Rather than building a large collection of specialized models, we focused on a **small number of models that are world-class and tightly integrated into the system**. These models serve distinct but coordinated roles: they analyze content, they represent it in embedding space, and they rank and select it for use inside inference.  
  
One of the central components here is [our best-in-class embedding model](https://blogs.bing.com/search/April-2026/Microsoft-Open-Sources-Industry-Leading-Embedding-Model), which defines how information is projected into a space where semantic similarity becomes computationally tractable. That decision alone has far-reaching consequences; the quality of embeddings determines not just recall during retrieval, but the *shape of the candidate space that every downstream component operates on*. We have built it to be competitive at the top of public benchmarks, but its role inside Web IQ is more pragmatic: when we search, we search the right neighborhood of the information space.  
  
The embedding model is one part of the system. Alongside it are models that are optimized for content understanding and ranking, trained not for isolated metrics but for **how their outputs are used inside LLM-driven reasoning****.** That alignment, between model objectives and system objectives, is what allows the stack to behave coherently under load.

### Beneath the model layer, the problem changes character.

Grounding is no longer about semantics alone. It becomes a **distributed systems problem at scale** and this is where a great deal of our earlier work becomes relevant, particularly with systems like **DiskANN**. DiskANN changed the practical limits of nearest neighbor search by making it possible to operate over large, disk-resident vector spaces without sacrificing latency, removing the need to trade recall for memory footprint.  
  
In Web IQ, this work is extended into a broader retrieval fabric. Retrieval is executed across distributed partitions, routed globally, and tightly optimized to meet latency constraints. Networking, data placement, and execution paths are all part of the design space – and they matter, because grounding is not a one-time operation. It is executed repeatedly within agentic workflows and at that scale, even small inefficiencies compound.  
  
What happens after retrieval is equally consequential. Web IQ does not just return documents; it returns passages and structured evidence objects. Models do not need documents, they need *information* and documents are often a poor proxy for that. By operating at the level of passages, we can concentrate useful signal while eliminating irrelevant context, producing a much higher ratio of information to tokens.  
  
This is why we often summarize the system with a simple principle: **fewer tokens in, better answers out, lower cost per call.** Cost is only part of it. The deeper value is **maintaining** **precision in reasoning** under constrained contexts.

### At the top of the stack sits the orchestration layer, where the system comes together.

Queries are interpreted, retrieval is fanned out, results are merged, filtered, and transformed into evidence. Modalities are combined, trade-offs are enforced, and the system adapts to the structure of the request. What makes this layer different from traditional systems is that it’s just not an outer API layer. It is part of the **execution loop of an AI agent**. Latency here is not just user-visible but structurally significant: determining whether a system can afford to take multiple reasoning steps or must compress everything into a single attempt. That constraint shapes everything above it.

## Quality, Latency, Token Density, and the Right Operating Points

When grounding becomes part of an agent’s execution loop, the core challenge is no longer retrieval in isolation. The system has to operate at the right point across latency, grounding quality, and token efficiency, because those three factors together determine whether multi-step reasoning is practical in the real world.  
  
Quality is the first dimension. A grounding system also has to return evidence that actually satisfies user intent: complete, fresh, authoritative, and useful for downstream reasoning. We measure that with **GDSAT**, or grounding satisfaction – a metric, that unlike traditional relevance scores, captures whether the grounding truly meets user intent across completeness, freshness, and authority. Across production query sets, Web IQ consistently achieves higher grounding satisfaction than alternative systems in comparable configurations, which matters because it translates directly into greater user trust and stronger downstream outcomes.  
  
![Bar chart shows Web IQ grounding satisfaction compared to competitors](https://blogs.bing.com/getmedia/1b77c90a-c0a8-4b22-8e3c-651f18ecf117/WebIQ_GDSAT2.png?width=600&height=374)  
*Source: 3K Global, Blind Queries sampled from prod, Config: 10 results, 10K chars per result (or equivalent).*  
  
Speed is also imperative. It determines whether an agent can afford multiple retrieval-and-reasoning steps or must collapse everything into a single attempt. Web IQ is designed for production-scale speed, operating at sub-165ms p95 latency and, in our internal comparisons, nearly 2.5× faster than the next best alternative from the previous cohort of competitors under similar conditions.  
  
![Bar Graph shows Web IQ P95 latency compared to competitors](https://blogs.bing.com/getmedia/1f587b19-547c-4a69-8972-db59ce5077d0/WebIQ_P95Latency2.png?width=600&height=374)  
*From VMs hosted in 5 DCs: West US2, North Central US, East US2, North Europe, South Korea. P95 numbers are averaged across DCs for the cohort of competitors. Unique queries were used for avoiding cache hits. Config: 10 results, 10K chars per result.*  
  
The third variable is token efficiency, which determines whether the system can scale economically. Every token sent to the model carries both a cost and a latency implication. By operating on passage-level evidence and maintaining high information density per token, Web IQ reduces how much context is required to achieve a given level of quality.  
  
![Graph shows Web IQ token efficiency compared to competitors](https://blogs.bing.com/getmedia/6a25743c-36c6-4099-8081-1852fb9b4994/WebIQ_TokenEfficiency3.png?width=1200&height=728)

*Source: 3K Query set (Global, Prod sampled). Web results: 10, 15, 20. #Chars: 3K, 5K, 10K, 20k per result (or equivalent).*

The result is a system designed to move the frontier on all three dimensions at once: lower latency, higher grounding satisfaction, and fewer tokens per call.

## Architecture and Design Principles

The architecture of Web IQ follows a few core principles.

- **G** **rounding is a full-stack systems problem.** Trustworthy outputs depend on aligning every layer, from corpus quality and retrieval to ranking and orchestration.
- **F** **oundation matters.** A global and fresh corpus is essential for trustworthy grounding, which is why the Bing foundation remains so important even as the system above it is re-architected.
- **T** **he right evidence unit is the passage** or structured evidence object that maximizes information density while minimizing token cost.
- **R** **eal operating points define the system.** Latency, quality, and token constraints determine whether agents work reliably in practice, and the architecture is engineered around them.

The agentic web will be built by systems that can reason against the world as it actually is: fresh, contested, and constantly changing. That requires more than a model with a search tool attached. It requires a grounding layer engineered for the speed, quality, and economics of inference-time retrieval, built on a foundation the open web can trust.  
  
That is what Web IQ is built to be, and where we believe the next decade of AI infrastructure is heading.  
  
Find out more information about Web IQ, including how to express interest, [here](https://aka.ms/WebIQ).  
  
Knut Risvik  
Distinguished Engineer, Search & AI