import snscrape.modules.twitter as sntwitter
from Tweet_Entity.TweetData import TweetData


query = "(spiderman) until:2022-01-01 since:2010-01-01"
limit = 2 #unlimited - just change the number accordingly
idCount = 1
movieId = 1 #spiderman
count = 0

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if limit == count:
        break
    else:
        Data = TweetData(idCount, movieId, tweet.content, tweet.likeCount, tweet.replyCount, tweet.retweetCount)
        count = count + 1
        print(Data)


def example_for_extraction():
    query_e = "(spiderman) until:2022-01-01 since:2010-01-01"
    tweets_e = []
    limit_e = 2  # unlimited - just change the number accordingly

    for tweet_e in sntwitter.TwitterSearchScraper(query_e).get_items():
        if len(tweets_e) == limit_e:
            break
        else:
            tweets_e.append([tweet_e.url, tweet_e.date, tweet_e.user.username, tweet_e.content, tweet_e.likeCount, tweet_e.retweetCount, tweet_e.replyCount, tweet_e.quoteCount])

    print(tweets_e)

