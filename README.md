# EC500 Project: Twitter Analyzer
Team Members: Donovan Jones, Luxuan Qi, and Erin Thomas

## Project Summary
The goal of this project is to use machine learning and the Twitter API to determine the "mood" of a tweet using keyword analysis and the location of the tweet.

## User Stories
- As someone who works in marketing for a business product, I want to better understand customers' feelings towards a product or brand.
- As someone who works in politics, I want to keep track of the political viewpoints of the public about important contemporary issues, like gun control.
- As someone who works in public health, I want to track the spread of epidemics.

## Software Architecture & Tech Stack
This application is divided into three components: the geolocation API (`geolocation.py`), tweet sentiment analyzer (`get_tweet_sentiment.py`), and front-end visualization (`app.py`).
### Geolocation API


### Tweet Sentiment Analysis
Our application analyzes sentiment of Tweets using TextBlob, a natural language processing (NLP) library for processing textual data. It assigns the text a polarity: greater than zero means the sentiment is positive, equal to zero means neutral, and less than zero is negative. We chose this library because it's simple and easy to use for basic sentiment analysis and does not require building test and training data with our own machine learning algorithm. 

### Front-End Data Visualization

## How to Run This Code

## References
* https://towardsdatascience.com/extracting-twitter-data-pre-processing-and-sentiment-analysis-using-python-3-0-7192bd8b47cf 
* https://www.toptal.com/python/twitter-data-mining-using-python
