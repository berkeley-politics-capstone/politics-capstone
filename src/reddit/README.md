# Reddit API

Exploration of using the Reddit API for our politics capstone project

## Requirements

[PRAW: The Python Reddit API Wrapper](https://praw.readthedocs.io/en/latest/index.html) is used for this section of the project and supports Python 2.7+. You can install the package using `pip`.

`pip install praw` 

There exists a `config.txt` file, an INI file which should sit in the same directory as the notebook. This file holds the necessary credentials to use the Reddit API. It should be structured using the sample below:

```{txt}
[reddit]
client_id = 14 character string listed just under “personal use script” for the desired developed application
client_secret = 27 character string listed adjacent to secret for the application
password = Reddit account password
username = Reddit account username
```
