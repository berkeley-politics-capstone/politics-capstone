---
title: Measuring Hype
layout: template
filename: hype
--- 

# Measuring Hype

Understanding the 2020 campaign requires analyzing multiple different sources of information in order to create a holistic view of this election. Our team has worked to identify and gather the data that will allow us to understand the hype surrounding a candidate.
<br/>

**Donations** <br/>
Tracking donations provided to a candidates campaign allows us to see more than just a total amount of money raised. It allows us to understand the frequency of small donations by individuals, which could mean increased hype surrounding that candidate. <br/>
*Data source: [Federal Election Commission (FEC)](https://www.fec.gov/)*
<br/>

**Media Coverage** <br/>
News outlets are a major source of information for Americans looking to understand more about the election. Summarizing this data, we look to understand which candidates are receiving the most news coverage across all major networks and which may be trending in the right direction. <br/>
*Data source: [GDELT Television API](https://blog.gdeltproject.org/gdelt-2-0-television-api-debuts/)*
<br/>

**Polling** <br/>
Polls allow us to get an understanding of where candidates rank relative to each other based off a sample of the American population. While polls may change drastically over time, we can still combine our understanding of polls with our other data sources to better evaluate candidate hype. <br/>
*Data source: [FiveThirtyEight Polling Data](https://github.com/fivethirtyeight/data/tree/master/polls)*
<br/>

**Articles & Comments** <br/>
Internet based articles grants us a sense of what the media is discussing online. Similarly, internet users who wish to discuss these events can choose to take to a forum like Reddit to add their comments. By using natural language processing techniques, we can get a sense of what is being discussed online by both the media and the voters, and how this influences the Hype Machine. <br/>
*Data source: [Reddit](https://www.reddit.com) for links to articles, comments*
<br/>

**Curated Dataset** <br/>
We have produced two datasets from the above sources which are freely availible to download as CSVs. The 2020 democratic primary contains data for Donnations, Media Coverage, Polling, and [LDA topic models](https://berkeley-politics-capstone.github.io/politics-capstone/2019/07/29/modeling-political-topics.html) from news on r/politics. The 2016 republican primary contains everything except for the LDA topics. <br/>
*2020 Democrats: [AWS](https://berkeley-politics-capstone.s3.amazonaws.com/dem20_dataset.csv) for links to articles, comments*
*2016 Republicans: [AWS](https://berkeley-politics-capstone.s3.amazonaws.com/rep16_dataset.csv)*
<br/>

