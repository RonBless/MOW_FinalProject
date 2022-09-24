import snscrape.modules.twitter as sntwitter

query = "(spiderman) until:2022-01-01 since:2010-01-01"
tweets = []
limit = 100 #unlimited - just change the number accordingly

for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.url, tweet.date, tweet.user.username, tweet.content, tweet.likeCount, tweet.retweetCount, tweet.replyCount, tweet.quoteCount])

print(tweets)
