---
type: concept
status: active
created: 2026-07-31
updated: 2026-07-31
tags: [concept, infrastructure-dev, workflow-design, adoption, switching-cost, context-access, figma-plugin, cli, tool-design]
sources: [pxd-writone-ai-writing-assistant, karrot-kraft-design-system-agent]
confidence: 0.7
---

# In-Workflow AI Placement

> [!abstract] Summary
> Where an AI tool *lives* determines whether it gets used, largely independently of how good it is. Placing it inside the surface where the work already happens removes the switching cost that otherwise makes people skip it — and, less obviously, gives the tool access to context it cannot obtain from outside.

> [!important] Why it Matters
> [[wiki/sources/pxd-writone-ai-writing-assistant|Writone's]] founding observation is that companies invest heavily in UX Writing guidelines which then sit dormant as PDFs. Not because practitioners disagree with them — because checking one means leaving Figma, opening a hundred-page document, finding the rule, and coming back. *"UX Writing 검토의 필요성은 인지하지만, 그것을 위해 흐름을 끊는 전환 비용이 너무 크다"* — the need is recognised; the cost of breaking flow is too large. **The binding constraint on adoption was never capability.**

## 📝 Key Claims

- **Audit the workflow before choosing the surface.** Writone's team observed the actual sequence — planning → Figma → insert text → review → revise — and found the guideline check was not a stage in it but an interruption of it. That observation, not a capability assessment, decided the product's form. *"기술이 아닌 사람의 흐름에서 출발했기 때문에, 제품이 있어야 할 자리가 자연스럽게 결정되었다"* — starting from the human flow rather than the technology decided the product's place naturally.

- **Placement buys context, not just convenience.** This is the part that is easy to miss. Writone's Figma plugin can read **layer node information** and distinguish a button from a toast, applying component-specific rules — impossible from a web app. [[wiki/sources/karrot-kraft-design-system-agent|Kraft]] made the identical move for the identical reason: its hosted admin *"중고거래팀이 쓸 때랑 부동산팀이 쓸 때, 같은 결과가 나와요"* — served every team the same output, because being web-based it could not reach the user's project folder, policy documents, or conventions. Moving to a local CLI was a move to **acquire context**.

- **A general-purpose tool cannot hold institutional context, and that is structural.** Kraft's account of why Lovable/v0/Bolt failed is not about output quality — those tools build with their own component sets and cannot be told that a private icon package or token scale exists. The same limit applies to any AI tool sitting outside the environment it is meant to serve.

- **Seep into the workflow rather than replace it.** *"도구는 워크플로우를 바꾸려 하기보다, 워크플로우에 스며들어야 한다고 생각해요"* — a tool should seep into the workflow rather than try to change it. Kraft's stated next problems are all integration points: Figma → Kraft, Kraft results → team library, SEED compliance checks at PR review.

- **Two independent arrivals.** One team building a UX-writing assistant and one building a screen generator, in different companies and different problem domains, neither citing the other, both concluded that the tool's location was the decisive design question and both moved it *toward* the existing work surface.

## 🔗 Related Concepts

- [[wiki/concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]] — the context a well-placed tool can then read.
- [[wiki/concepts/ai-agents/context-engineering|Context Engineering]]
- [[wiki/concepts/ai-agents/local-first-agents|Local-First Agents]] — the same argument from the infrastructure side.
- [[wiki/concepts/ai-agents/agent-invocable-app-functions|Agent-Invocable App Functions]]
- [[wiki/concepts/infrastructure-dev/ai-readable-documentation|AI-Readable Documentation]] — the dormant-PDF problem is what this concept routes around.
- [[wiki/concepts/ai-agents/mcp-integration|MCP Integration]]
- [[wiki/concepts/infrastructure-dev/design-to-code-workflow|Design-to-Code Workflow]]

## ⚖️ Conflicts & Caveats

- **Neither source measures adoption.** Both argue placement drives adoption; neither reports an adoption figure before or after. The claim is coherent and well-motivated and remains **unevidenced**.
- **Placement trades reach for depth.** A Figma plugin serves people in Figma; a CLI serves people willing to run one. Kraft's admin version was abandoned specifically for the property — zero-install web access — that made it broadest. Neither source discusses who was lost.
- **In-workflow placement raises the automation-bias stakes.** A suggestion appearing inside the tool at the moment of work is easier to accept unreflectively than one requiring a deliberate check. [[wiki/concepts/agent-experience/willful-blindness|Willful blindness]] applies with more force, not less, and neither source measures acceptance rates.
- **Both are first-party accounts** by teams describing their own tools.
- **Plugin surfaces impose their own ceilings** — a host application's extension API decides what is possible, which is a dependency neither source examines.

## 📚 Sources

- [[wiki/sources/pxd-writone-ai-writing-assistant|pxd (2026): Writone]] — the switching-cost observation and the Figma-plugin decision
- [[wiki/sources/karrot-kraft-design-system-agent|Karrot (2026): Kraft]] — admin → CLI, made explicitly to acquire context

## ❓ Open Questions

- Does in-workflow placement actually raise usage, and by how much? Two sources assert it; neither counted.
- Does it raise uncritical acceptance at the same time — and if so, does the net effect on output quality stay positive?
- Who is excluded when a tool moves from a URL to a plugin or a CLI, and does the depth gained exceed the reach lost?
- Is there a placement that gets context access without depending on a host application's extension API?
