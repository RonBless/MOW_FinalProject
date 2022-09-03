import tweepy
import configparser
import sys
import os
import snscrape.modules.twitter as sntwitter
import pandas as pd
import DAL

sys.path.append(os.path.abspath("TweetData"))

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# search tweets
keyword = 'Spider-man'
limit = 300
tweets = tweepy.Cursor(api.search_tweets, q=keyword, count=100, tweet_mode='extended').items(limit) #returns messages from twitter - up to 300 items

data = []
for tweet in tweets:
    data.append([tweet.full_text, tweet.favorite_count,  tweet.retweet_count])

print(data)


# query = "(from:elonmusk) until:2020-01-01 since:2010-01-01"
# tweets = []
# limit = 20
#
# for tweet in sntwitter.TwitterSearchScraper(query).get_items():
#
#     # print(vars(tweet))
#     # break
#     if len(tweets) == limit:
#         break
#     else:
#         tweets.append([tweet.date, tweet.user.username, tweet.content])
#
# print(tweets)