# Source Capture: Data Preparation

URL: https://conjointly.com/kb/data-preparation/

Retrieved: 2026-06-08

Source collection: Conjointly Research Methods Knowledge Base

TOC title: Data Preparation

TOC order: 106

TOC depth: 1

Author/site: William M.K. Trochim / Conjointly

Published: Not stated

Word count: 1244

---

Data Preparation involves checking or logging the data in; checking the data for accuracy; entering the data into the computer; transforming the data, and developing and documenting a database structure that integrates the various measures.

## Logging the Data

In any research project you may have data coming from a number of different sources at different times:

- mail surveys returns
- coded interview data
- pretest or posttest data
- observational data

In all but the simplest of studies, you need to set up a procedure for logging the information and keeping track of it until you are ready to do a comprehensive data analysis. Different researchers differ in how they prefer to keep track of incoming data. In most cases, you will want to set up a database that enables you to assess at any time what data is already in and what is still outstanding. You could do this with any standard computerized database program (e.g. Microsoft Access, Claris Filemaker), although this requires familiarity with such programs. or, you can accomplish this using standard statistical programs (e.g. SPSS, SAS, Minitab, Datadesk) and running simple descriptive analyses to get reports on data status. It is also critical that the data analyst retain the original data records for a reasonable period of time – returned surveys, field notes, test protocols, and so on. Most professional researchers will retain such records for at least 5-7 years. For important or expensive studies, the original data might be stored in a data archive. The data analyst should always be able to trace a result from a data analysis back to the original forms on which the data was collected. A database for logging incoming data is a critical component in good research record-keeping.

## Checking the Data For Accuracy

As soon as data is received you should screen it for accuracy. In some circumstances doing this right away will allow you to go back to the sample to clarify any problems or errors. There are several questions you should ask as part of this initial data screening:

- Are the responses legible/readable?
- Are all important questions answered?
- Are the responses complete?
- Is all relevant contextual information included (e.g. data, time, place, researcher)?

In most social research, quality of measurement is a major issue. Assuring that the data collection process does not contribute inaccuracies will help assure the overall quality of subsequent analyses.

## Developing a Database Structure

The database structure is the manner in which you intend to store the data for the study so that it can be accessed in subsequent data analyses. You might use the same structure you used for logging in the data or, in large complex studies, you might have one structure for logging data and another for storing it. As mentioned above, there are generally two options for storing data on computer – database programs and statistical programs. Usually database programs are the more complex of the two to learn and operate, but they allow the analyst greater flexibility in manipulating the data.

In every research project, you should generate a printed **codebook** that describes the data and indicates where and how it can be accessed. Minimally the codebook should include the following items for each variable:

- variable name
- variable description
- variable format (number, data, text)
- instrument/method of collection
- date collected
- respondent or group
- variable location (in database)
- notes

The codebook is an indispensable tool for the analysis team. Together with the database, it should provide comprehensive documentation that enables other researchers who might subsequently want to analyze the data to do so without any additional information.

## Entering the Data into the Computer

There are a wide variety of ways to enter the data into the computer for analysis. Probably the easiest is to just type the data in directly. In order to assure a high level of data accuracy, the analyst should use a procedure called **double entry**. In this procedure you enter the data once. Then, you use a special program that allows you to enter the data a second time and checks each second entry against the first. If there is a discrepancy, the program notifies the user and allows the user to determine the correct entry. This double entry procedure significantly reduces entry errors. However, these double entry programs are not widely available and require some training. An alternative is to enter the data once and set up a procedure for checking the data for accuracy. For instance, you might spot check records on a random basis. Once the data have been entered, you will use various programs to summarize the data that allow you to check that all the data are within acceptable limits and boundaries. For instance, such summaries will enable you to easily spot whether there are persons whose age is `601` or who have a `7` entered where you expect a `1` -to- `5` response.

## Data Transformations

Once the data have been entered it is almost always necessary to transform the raw data into variables that are usable in the analyses. There are a wide variety of transformations that you might perform. Some of the more common are:

### Missing values

Many analysis programs automatically treat blank values as missing. In others, you need to designate specific values to represent missing values. For instance, you might use a value of -99 to indicate that the item is missing. You need to check the specific program you are using to determine how to handle missing values.

### Item reversals

On scales and surveys, we sometimes use [reversal items](https://conjointly.com/kb/likert-scaling/) to help reduce the possibility of a response set. When you analyze the data, you want all scores for scale items to be in the same direction where high scores mean the same thing and low scores mean the same thing. In these cases, you have to reverse the ratings for some of the scale items.

For instance, let’s say you had a five point response scale for a self esteem measure where `1` meant strongly disagree and `5` meant strongly agree. One item is “I generally feel good about myself.” If the respondent strongly agrees with this item they will put a `5` and this value would be indicative of higher self esteem. Alternatively, consider an item like “Sometimes I feel like I’m not worth much as a person.” Here, if a respondent strongly agrees by rating this a `5` it would indicate low self esteem. To compare these two items, we would reverse the scores of one of them (probably we’d reverse the latter item so that high values will always indicate higher self esteem). We want a transformation where if the original value was `1` it’s changed to `5`, `2` is changed to `4`, `3` remains the same, `4` is changed to `2` and `5` is changed to `1`. While you could program these changes as separate statements in most program, it’s easier to do this with a simple formula like:

In our example, the High Value for the scale is `5`, so to get the new (transformed) scale value, we simply subtract each Original Value from `6` (i.e. `5 + 1`).

### Scale totals

Once you’ve transformed any individual scale items you will often want to add or average across individual items to get a total score for the scale.

For many variables you will want to collapse them into categories. For instance, you may want to collapse income estimates (in dollar amounts) into income ranges.
