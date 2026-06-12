# Source Capture: Randomized Block Designs

URL: https://conjointly.com/kb/randomized-block-designs/

Retrieved: 2026-06-08

Source collection: Conjointly Research Methods Knowledge Base

TOC title: Randomized Block Designs

TOC order: 91

TOC depth: 2

Author/site: William M.K. Trochim / Conjointly

Published: Not stated

Word count: 844

---

The Randomized Block Design is research design’s equivalent to [stratified random sampling](https://conjointly.com/kb/probability-sampling/). Like stratified sampling, randomized block designs are constructed to reduce noise or variance in the data (see [Classifying the Experimental Designs](https://conjointly.com/kb/classifying-experimental-designs/)). How do they do it? They require that the researcher divide the sample into relatively homogeneous subgroups or blocks (analogous to “strata” in stratified sampling). Then, the experimental design you want to implement is implemented within each block or homogeneous subgroup. The key idea is that the variability within each block is less than the variability of the entire sample. Thus each estimate of the treatment effect within a block is more efficient than estimates across the entire sample. And, when we pool these more efficient estimates across blocks, we should get an overall more efficient estimate than we would without blocking.

![](https://conjointly.com/img/kb/Assets/images/expblk.gif)

Here, we can see a simple example. Let’s assume that we originally intended to conduct a simple posttest-only randomized experimental design. But, we recognize that our sample has several intact or homogeneous subgroups. For instance, in a study of college students, we might expect that students are relatively homogeneous with respect to class or year. So, we decide to block the sample into four groups: freshman, sophomore, junior, and senior. If our hunch is correct, that the variability within class is less than the variability for the entire sample, we will probably get more powerful estimates of the treatment effect within each block (see the discussion on [Statistical Power](https://conjointly.com/kb/statistical-power/)). Within each of our four blocks, we would implement the simple post-only randomized experiment.

Notice a couple of things about this strategy. First, to an external observer, it may not be apparent that you are blocking. You would be implementing the same design in each block. And, there is no reason that the people in different blocks need to be segregated or separated from each other. In other words, blocking doesn’t necessarily affect anything that you do with the research participants. Instead, blocking is a strategy for grouping people in your data analysis in order to reduce noise – it is an **analysis** strategy. Second, you will only benefit from a blocking design if you are correct in your hunch that the blocks are more homogeneous than the entire sample is. If you are wrong – if different college-level classes aren’t relatively homogeneous with respect to your measures – you will actually be hurt by blocking (you’ll get a less powerful estimate of the treatment effect). How do you know if blocking is a good idea? You need to consider carefully whether the groups are relatively homogeneous. If you are measuring political attitudes, for instance, is it reasonable to believe that freshmen are more like each other than they are like sophomores or juniors? Would they be more homogeneous with respect to measures related to drug abuse? Ultimately the decision to block involves judgment on the part of the researcher.

## How Blocking Reduces Noise

So how does blocking work to reduce noise in the data? To see how it works, you have to begin by thinking about the non-blocked study. The figure shows the pretest-posttest distribution for a hypothetical pre-post randomized experimental design. We use the ‘X’ symbol to indicate a program group case and the ‘O’ symbol for a comparison group member. You can see that for any specific pretest value, the program group tends to outscore the comparison group by about 10 points on the posttest. That is, there is about a 10-point posttest mean difference.

![](https://conjointly.com/img/kb/Assets/images/expblk2.gif)

Now, let’s consider an example where we divide the sample into three relatively homogeneous blocks. To see what happens graphically, we’ll use the pretest measure to block. This will assure that the groups are very homogeneous. Let’s look at what is happening within the third block. Notice that the mean difference is still the same as it was for the entire sample – about 10 points within each block. But also notice that the variability of the posttest is much less than it was for the entire sample.

![](https://conjointly.com/img/kb/Assets/images/expblk3.gif)

Remember that the treatment effect estimate is a signal-to-noise ratio. The signal in this case is the mean difference. The noise is the variability. The two figures show that we haven’t changed the signal in moving to blocking ⁠— there is still about a 10-point posttest difference. But, we have changed the noise ⁠— the variability on the posttest is much smaller within each block that it is for the entire sample. So, the treatment effect will have less noise for the same signal.

It should be clear from the graphs that the blocking design in this case will yield the stronger treatment effect. But this is true only because we did a good job assuring that the blocks were homogeneous. If the blocks weren’t homogeneous ⁠— their variability was as large as the entire sample’s ⁠— we would actually get worse estimates than in the simple randomized experimental case. We’ll see how to analyze data from a randomized block design in the [Statistical Analysis of the Randomized Block Design](https://conjointly.com/kb/randomized-block-analysis/).
