from Twitter.TwitterAPI import TwitterAPI
from transformers import pipeline

sentiment_analysis = pipeline("sentiment-analysis", model="siebert/sentiment-roberta-large-english")

twitter_api = TwitterAPI.getInstance()
twitter_api.setLimit(1)
tweets_list = twitter_api.getTweets("Spider-man: No Way Home", "2021-01-01", "2021-12-16")

print(sentiment_analysis(tweets_list[0].message))
