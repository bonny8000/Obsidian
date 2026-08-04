---
source_url: https://www.boongranii.dev/posts/cursor-pointer-debate
captured: 2026-08-04
title: "클릭 가능한 요소에 cursor: pointer를 써야 할까? (Should Clickable Elements Use cursor: pointer?)"
authors: [Boongranii]
published: 2026-06-04
publisher: boongranii.dev (personal frontend blog)
language: ko
format: opinion essay with implementation guidance
---

# Should Clickable Elements Use `cursor: pointer`? — Boongranii

**Author:** Boongranii, Korean frontend developer, personal blog. Stated reading time 5 minutes.
**Published:** 2026-06-04 · **Captured:** 2026-08-04

AI-written extraction. No full-text reproduction; short quoted phrases only, with translation.

---

## The trigger

The author noticed that **shadcn/ui ships buttons with `cursor: default`**, which felt wrong. Tracing why leads to a long-running disagreement.

## The specification position

The **W3C CSS cursor specification** defines `pointer` as indicating **a link** — not a button, not a form control. Native OS applications (macOS, Windows) do not change the cursor over buttons. On the letter of the spec and on platform convention, `cursor: default` on a `<button>` is correct.

## The two camps

| Camp | Named advocate | Argument |
| --- | --- | --- |
| **Prescriptivist** | **Adam Silver**, essay "Buttons shouldn't have a hand cursor" | *"버튼은 생김새 자체로 클릭 가능함을 전달해야 한다"* — *a button should convey clickability through its appearance alone.* If it needs a cursor to look clickable, the visual design has failed. |
| **Pragmatist** | **Chris Coyier** (CSS-Tricks) | Twenty-plus years of web use have trained `pointer` = clickable. *"웹은 OS가 아니다"* — *the web is not an OS.* Coyier circulated a CSS snippet applying `pointer` to every clickable element. |

Also positioned: the **Tailwind CSS team** — v4 changed the preflight default from `cursor: pointer` to `cursor: default` on buttons, to align with native OS behaviour. **shadcn/ui maintainers** initially declined to restore it at component level and pointed users to a global CSS override.

## The affordance argument

The author invokes affordance theory — *"이 물건을 어떻게 사용해야 하는지 직관적으로 알려주는 단서"* (*a cue that intuitively tells you how to use the thing*), with the standard door-handle example — then makes the load-bearing move: the prescriptivist position **assumes strong visual affordance**, and contemporary UI often does not have it.

> "시각적 어포던스가 약해요" — *the visual affordance is weak.*

Cases where visual affordance is genuinely thin:

```jsx
// text-only button
<button className="text-sm text-gray-600 hover:text-gray-900">필터 초기화</button>

// ghost button, hairline border
<button className="border border-gray-200 rounded-md px-3 py-1">취소</button>

// whole card is the click target
<div onClick={handleClick} className="rounded-lg p-4 bg-white shadow-sm">
  <h3>프로젝트 이름</h3>
  <p>설명...</p>
</div>
```

The card case is the strongest: nothing about a card announces that the whole surface is a target.

## The community-signal evidence

Repeated shadcn/ui GitHub issues after the Tailwind v4 change, cited by number:

- **#7501** — "button cursor-pointer or not?"
- **#7223** — "Button does not have cursor-pointer by default"
- **#6843** — Tailwind v4 cursor behaviour
- **#7279** — toggle/checkbox missing pointer

> "커서가 안 바뀌어서 누를 수 있는지 모르겠다는 글이 계속 올라온다"
> — *posts keep appearing saying they can't tell it's clickable because the cursor doesn't change.*

The author treats the recurrence of the issue as the evidence: users kept filing it, which is a signal of real friction rather than a preference.

## Recommended implementation

```css
@layer base {
  a, button, [role='button'], input[type='submit'],
  input[type='reset'], input[type='button'], label[for],
  select, summary, [onclick] {
    cursor: pointer;
  }

  [disabled], [aria-disabled='true'] {
    cursor: not-allowed;
  }
}
```

Note the second rule: disabled state gets `not-allowed`, so the cursor carries availability as well as interactivity.

Component-level equivalent:

```jsx
<Button className="cursor-pointer">저장</Button>
<Card className="cursor-pointer" onClick={handleClick}>...</Card>
<Button disabled className="cursor-not-allowed">저장</Button>
```

## Accessibility argument

Not every user perceives a subtle hover colour change; a cursor change is close to universally detectable. The author frames the cursor as cheap redundant feedback — no performance cost, no side effects.

**Note:** no formal accessibility research or usability study is cited. The accessibility claim is the author's reasoning, not a finding.

## Conclusion

> "결국 UX는 스펙이 아니라 사용자를 위한 거잖아요"
> — *in the end UX is for users, not for the spec.*

> "사람들이 20년 넘게 pointer = 클릭 가능으로 익혀왔잖아요. 이걸 '스펙에 안 맞으니까' 빼버리는 건 사용자가 아니라 스펙을 위한 결정"
> — *people have learned pointer = clickable for over twenty years. Removing it because it doesn't match the spec is a decision made for the spec, not for the user.*

## Limits the author concedes

- The W3C spec and native OS convention do support the prescriptivist reading.
- The prescriptivist argument holds under *ideal* visual design; the author's case rests on real projects falling short of that.
- No controlled study is offered — the evidence is community reports and personal observation.
