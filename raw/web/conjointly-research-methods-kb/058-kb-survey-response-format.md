# Source Capture: Response Format

URL: https://conjointly.com/kb/survey-response-format/

Retrieved: 2026-06-08

Source collection: Conjointly Research Methods Knowledge Base

TOC title: Response Format

TOC order: 58

TOC depth: 3

Author/site: William M.K. Trochim / Conjointly

Published: Not stated

Word count: 1061

---

The response format is how you collect the answer from the respondent. Let’s start with a simple distinction between what we’ll call **unstructured** response formats and **structured response formats**. \[*On this page, I’ll use standard web-based form fields to show you how various response formats might look on the web. If you want to see how these are generated, select the View Source option on your web browser.*\]

## Structured Response Formats

Structured formats help the respondent to respond more easily and help the researcher to accumulate and summarize responses more efficiently. But, they can also constrain the respondent and limit the researcher’s ability to understand what the respondent really means. There are many different structured response formats, each with its own strengths and weaknesses. We’ll review the major ones here.

### Fill-In-The-Blank

One of the simplest response formats is a blank line. A blank line can be used for a number of different response types. For instance:

> **Please enter your gender:**

Here, the respondent would probably put a check mark or an X next to the response. This is also an example of a **dichotomous** response, because it only has two possible values. Other common dichotomous responses are True/False and Yes/No. Here’s another common use of a fill-in-the-blank response format:

> **Please enter your preference for the following candidates where ‘1’ = your first choice, ‘2’ = your second choice, and so on.**
> 
> Robert Dole
> 
> Colin Powell
> 
> Bill Clinton
> 
> Al Gore

In this example, the respondent writes a number in each blank. Notice that here, we expect the respondent to place a number on every blank, whereas in the previous example, we expect to respondent to choose only one. Then, of course, there’s the classic:

> **NAME: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

And here’s the same fill-in-the-blank response item in web format:

> **NAME:**

Of course, there’s always the classic fill-in-the-blank test item:

> **One of President Lincoln’s most famous speeches, the Address, only lasted a few minutes when delivered.**

### Check The Answer

The respondent places a check next to the response(s). The simplest form would be the example given above where we ask the person to indicate their gender. Sometimes, we supply a box that the person can fill in with an ‘X’ (which is sort of a variation on the check mark. Here’s a web version of the checkbox:

> **
> 
> Please check if you have the following item on the computer you use most:
> 
> **

Notice that in this example, it is possible for you to check more than one response. By convention, we usually use the checkmark format when we want to allow the respondent to select multiple items.

We sometimes refer to this as a **multi-option variable**. You have to be careful when you analyze data from a multi-option variable. Because the respondent can select any of the options, you have to treat this type of variable in your analysis *as though each option is a separate variable*. For instance, for each option we would normally enter either a `0` if the respondent did not check it or a `1` if the respondent did check it. For the example above, if the respondent had only a modem and CD-ROM drive, we would enter the sequence `1`, `0`, `1`, `0`, `0`. There is a very important reason why you should code this variable as either `0` or `1` when you enter the data. If you do, and you want to determine what percent of your sample has a modem, all you have to do is compute the average of the `0's` and `1's` for the modem variable. For instance, if you have `10` respondents and only `3` have a modem, the average would be `3/10 = .30 or 30%`, which is the percent who checked that item.

The example above is also a good example of a checklist item. Whenever you use a checklist, you want to be sure that you ask the following questions:

- Are all of the alternatives covered?
- Is the list of reasonable length?
- Is the wording impartial?
- Is the form of the response easy, uniform?

Sometimes you may not be sure that you have covered all of the possible responses in a checklist. If that is the case, you should probably allow the respondent to write in any other options that may apply.

### Circle The Answer

Sometimes the respondent is asked to circle an item to indicate their response. Usually, we are asking them to circle a number. For instance, we might have the following:

![](https://conjointly.com/img/kb/Assets/images/circresp.gif)

In computer contexts, it’s not feasible to have respondents circle a response. In this case, we tend to use an option button:

> **
> 
> Capital punishment is the best way to deal with convicted murderers.
> 
> **

Notice that you can only check one option at a time. The rule of thumb is that you ask someone to circle an item or click on a button when you only want them to be able to select one of the options. In contrast to the multi-option variable described above, we refer to this type of item as a **single-option variable** – even though the respondent has multiple *choices*, they can only select one of them. We would analyze this as a single variable that can take the integer values from `1 to 5`.

## Unstructured Response Formats

While there is a wide variety of structured response formats, there are relatively few unstructured ones. What is an unstructured response format? Generally, it’s written text. If the respondent (or interviewer) writes down text as the response, you’ve got an unstructured response format. These can vary from short comment boxes to the transcript of an interview.

In almost every short questionnaire, there’s one or more short text field questions. One of the most frequent goes something like this:

> **Please add any other comments:**

Actually, there’s really not much more to text-based response formats of this type than writing the prompt and allowing enough space for a reasonable response.

Transcripts are an entirely different matter. There, the transcriber has to decide whether to transcribe every word or only record major ideas, thoughts, quotes, etc. In detailed transcriptions, you may also need to distinguish different speakers (e.g. the interviewer and respondent) and have a standard convention for indicating comments about what’s going on in the [interview](https://conjointly.com/kb/conducting-research-interviews/), including non-conversational events that take place and thoughts of the interviewer.
