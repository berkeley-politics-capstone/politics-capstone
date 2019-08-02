---
layout: template
title:  "Modeling Political Topics from News Articles and Reddit Comments"
---

During the election cycle, we assume that candidates have much control over the narrative of what they want to discuss, as it relates to their platform and their competitors. Yet, this is not the case. The media heavily influences the topics that are discussed during the election, whether the candidates brought it up or not. Furthermore, we as voters are bringing up topics that are relevant to us on places such as internet forums. What are these topics and how do they contribute to the Hype Machine? We’ve used natural language processing techniques to discover topics mentioned by the media and by voters on the Internet, and how they've influenced the primary election.

## What is Topic Modeling?

[Topic modeling](https://en.wikipedia.org/wiki/Topic_model) is a technique that clusters a collection of texts (such as sentences, paragraphs, and articles) into groups that are distinguished from one another by what these texts' topics are. The model that we use for our analysis, [Latent Dirichlet Allocation (LDA)](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation), will compute a probability of how each textual example is associated with each cluster. While LDA and topic modeling can't tell us directly what the topic of each cluster is, we have the tools and background necessary to discern this for ourselves.

We used two main sets of textual data to discover topics brought up during the beginning of the Democratic party's 2020 primary election cycle. The first set are internet news articles related to the 2020 primary, so that we can understand what topics the media is interested in. The second set are comments from political and candidate specific subsections of Reddit (i.e. [/r/politics](https://www.reddit.com/r/politics)), in which users are discussing politically related news articles or other media. Comments help us understand what topics that internet-saavy voters may be discussing. More information about data munging and modeling can be found in the [Methodology](#methodology) section.

## News Articles

tk

## Reddit Comments

tk

## Methodology

### Datasets

We identified Reddit, and particularly politically related subreddits, as a rich source containing URLs to news articles that users will link to, as well as discussion about either those URLs, or other politically related topics that they would have in non-link posts called "self posts".  For two time frames, the 2016 Republican primary (January 1, 2015 to May 31, 2016, just before Donald Trump was announced as the Republican nominee) and the 2020 Democratic primary (January 1, 2019 to July 15, 2019), we would look at content in /r/politics and the candidate of the specific party's subreddits, if it existed. Examples include /r/KasichforPresident for the 2016 dataset, and/r/tulsi for the 2020 dataset. Because Donald Trump has been fundraising for re-election in 2020, we pulled content from r/The_Donald for both datasets. 

We used [Pushshift Reddit API](https://github.com/pushshift/api) to gather the data. For News Articles, we gathered link posts, the URL to the article, number of comments, and cumulative karma score. From there, we used [news-please](https://github.com/fhamborg/news-please) to scrape the article text from the URLs. For Reddit Comments, we gathered all comments posted in the subreddits of interest for the dates specified, as well as cumulative karma score of each comment.

### Cleaning and Pre-processing

(Some nuances about news articles here?)

Raw reddit comments are left in there markdown forms, so the text had to be scraped of this formatting and converted to regular text. Comments may also be deleted or removed at a later time, which will be indicated by a [deleted] or [removed] in their comment body. These comments were removed from the dataset. Since karma score is a unique feature of Reddit, in which popular links and comments are "upvoted" and unpopular links and comments are "downvoted", we wanted to provide this community feedback in our dataset. We did this by duplicating comments based on the log of their karma score. The most popular comments were duplicated up to ten times. Any comments less than 0 karma were removed. Finally, Reddit comments are featured in a tree structure, where the parent of the tree is in direct response to the link or main post, while children are typically in response to other comments. We chose to only keep the parent comments in order to reduce [topic divergence.](https://cs224d.stanford.edu/reports/ChowHong.pdf)

For both articles and comments, text was stemmed, lemmatized, and converted to a corpus of [Bag of Words](https://en.wikipedia.org/wiki/Bag-of-words_model) for use in the model.

### Modeling


