# Source Capture: Likert Scaling

URL: https://conjointly.com/kb/likert-scaling/

Retrieved: 2026-06-08

Source collection: Conjointly Research Methods Knowledge Base

TOC title: Likert Scaling

TOC order: 66

TOC depth: 2

Author/site: William M.K. Trochim / Conjointly

Published: Not stated

Word count: 999

---

Like [Thurstone](https://conjointly.com/kb/thurstone-scaling/) or [Guttman](https://conjointly.com/kb/guttman-scaling/) Scaling, Likert Scaling is a [unidimensional scaling](https://conjointly.com/kb/general-issues-in-scaling/#unidimensional-or-multidimensional) method. Here, I’ll explain the basic steps in developing a Likert or “summative” scale.

### Defining the Focus

As in all scaling methods, the first step is to define what it is you are trying to measure. Because this is a unidimensional scaling method, it is assumed that the concept you want to measure is one-dimensional in nature. You might operationalize the definition as an instruction to the people who are going to create or generate the initial set of candidate items for your scale.

### Generating the Items

Next, you have to create the set of potential scale items. These should be items that can be rated on a `1-to-5` or `1-to-7` Disagree-Agree response scale. Sometimes you can create the items by yourself based on your intimate understanding of the subject matter. But, more often than not, it’s helpful to engage a number of people in the item creation step. For instance, you might use some form of brainstorming to create the items. It’s desirable to have as large a set of potential items as possible at this stage, about 80-100 would be best.

![](https://conjointly.com/img/kb/Assets/images/cardidea.gif)

### Rating the Items

The next step is to have a group of judges rate the items. Usually, you would use a 1-to-5 rating scale where:

1. Strongly unfavorable to the concept
2. Somewhat unfavorable to the concept
3. Undecided
4. Somewhat favorable to the concept
5. Strongly favorable to the concept

Notice that, as in other scaling methods, the judges are not telling you what they believe – they are judging how favorable each item is with respect to the construct of interest.

![](https://conjointly.com/img/kb/Assets/images/handwrte.gif)

### Selecting the Items

The next step is to compute the intercorrelations between all pairs of items, based on the ratings of the judges. In making judgements about which items to retain for the final scale there are several analyses you can do:

- **Throw out any items that have a low correlation with the total (summed) score across all items.** In most statistics packages it is relatively easy to compute this type of Item-Total correlation:
	- First, you create a new variable which is the sum of all of the individual items for each respondent.
		- Then, you include this variable in the correlation matrix computation (if you include it as the last variable in the list, the resulting Item-Total correlations will all be the last line of the correlation matrix and will be easy to spot).
		- How low should the correlation be for you to throw out the item? There is no fixed rule here – you might eliminate all items with a correlation with the total score less that `0.6`, for example.
- **For each item, get the average rating for the top quarter of judges and the bottom quarter.**
	- Then, do a [t-test](https://conjointly.com/kb/statistical-student-t-test/) of the differences between the mean value for the item for the top and bottom quarter judges.
		- Higher t-values mean that there is a greater difference between the highest and lowest judges. In more practical terms, items with higher t-values are better discriminators, so you want to keep these items.

In the end, you will have to use your judgement about which items are most sensibly retained. You want a relatively small number of items on your final scale (e.g. 10-15) and you want them to have high Item-Total correlations and high discrimination (e.g. high t-values).

### Administering the Scale

You’re now ready to use your Likert scale. Each respondent is asked to rate each item on some response scale. For instance, they could rate each item on a `1-to-5` response scale where:

1. Strongly disagree
2. Disagree
3. Undecided
4. Agree
5. Strongly agree

There are a variety possible response scales (`1-to-7`, `1-to-9`, `0-to-4`). All of these odd-numbered scales have a middle value is often labeled *Neutral* or *Undecided*. It is also possible to use a forced-choice response scale with an even number of responses and no middle neutral or undecided choice. In this situation, the respondent is forced to decide whether they lean more towards the agree or disagree end of the scale for each item.

The final score for the respondent on the scale is the sum of their ratings for all of the items (this is why this is sometimes called a “summated” scale). On some scales, you will have items that are reversed in meaning from the overall direction of the scale. These are called **reversal items**. You will need to reverse the response value for each of these items before summing for the total. That is, if the respondent gave a `1`, you make it a `5`; if they gave a `2` you make it a `4`; `3` ⇒ `3`; `4` ⇒ `2`; and, `5` ⇒ `1`.

## Example: The Employment Self Esteem Scale

Here’s an example of a ten-item Likert scale that attempts to estimate the level of self esteem a person has on the job. Notice that this instrument has no center or neutral point – the respondent has to declare whether he/she is in agreement or disagreement with the item.

> **Please rate how strongly you agree or disagree with each of the following statements** by placing a check mark in the appropriate box.

| Statement | ❌❌ Strongly Disagree | ❌ Somewhat Disagree | ✔ Somewhat Agree | ✔✔ Strongly Agree |
| --- | --- | --- | --- | --- |
| I feel good about my work on the job. |  |  |  |  |
| On the whole, I get along well with others at work. |  |  |  |  |
| I am proud of my ability to cope with difficulties at work. |  |  |  |  |
| When I feel uncomfortable at work, I know how to handle it. |  |  |  |  |
| I can tell that other people at work are glad to have me there. |  |  |  |  |
| I know I’ll be able to cope with work for as long as I want. |  |  |  |  |
| I am proud of my relationship with my supervisor at work. |  |  |  |  |
| I am confident that I can handle my job without constant assistance. |  |  |  |  |
| I feel like I make a useful contribution at work. |  |  |  |  |
| I can tell that my coworkers respect me. |  |  |  |  |
