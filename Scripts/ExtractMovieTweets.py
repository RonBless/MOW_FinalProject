from NLP.NLP_Module import NLP
from Twitter.TwitterAPI import TwitterAPI
from threading import Thread, Lock
import concurrent.futures


# def getMovieTweets(name, start_date, end_date):
#     twitter = TwitterAPI.getInstance()
#     tweets_list = twitter.getTweets(name, start_date, end_date)
#     positive_tweets = 0
#     negative_tweets = 0
#     positive_likes = 0
#     negative_likes = 0
#     positive_comments = 0
#     negative_comments = 0
#     positive_shares = 0
#     negative_shares = 0
#     avg_positive_score = 0
#     avg_negative_score = 0
#     nlp = NLP.getInstance()
#     for tweet in tweets_list:
#         result = nlp.predict(tweet.message)
#         match (result[0]):
#             case 'POSITIVE':
#                 positive_tweets += 1
#                 positive_likes += tweet.likes
#                 positive_comments += tweet.replies
#                 positive_shares += tweet.shares
#                 avg_positive_score += result[1]
#             case 'NEGATIVE':
#                 negative_tweets += 1
#                 negative_likes += tweet.likes
#                 negative_comments += tweet.replies
#                 negative_shares += tweet.shares
#                 avg_negative_score += result[1]
#
#     if positive_tweets > 0:
#         avg_positive_score = avg_positive_score / positive_tweets
#     if negative_tweets > 0:
#         avg_negative_score = avg_negative_score / negative_tweets
#
#     return positive_tweets, negative_tweets, positive_likes, negative_likes, positive_comments, negative_comments,\
#         positive_shares, negative_shares, avg_positive_score, avg_negative_score

def process_tweet(tweet, nlp, counters, lock):
    result = nlp.predict(tweet.message)
    sentiment = result[0].lower()
    lock.acquire()
    counters[sentiment]['tweets'] += 1
    counters[sentiment]['likes'] += tweet.likes
    counters[sentiment]['comments'] += tweet.replies
    counters[sentiment]['shares'] += tweet.shares
    counters[sentiment]['score'] += result[1]
    lock.release()


def getMovieTweets(name, start_date, end_date):
    twitter = TwitterAPI.getInstance()
    tweets_list = twitter.getTweets(name, start_date, end_date)
    nlp = NLP.getInstance()

    counters = {
        'positive': {'tweets': 0, 'likes': 0, 'comments': 0, 'shares': 0, 'score': 0},
        'negative': {'tweets': 0, 'likes': 0, 'comments': 0, 'shares': 0, 'score': 0}
    }

    lock = Lock()

    # Create a ThreadPoolExecutor with 4 worker threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
        # Submit tasks to the executor for each tweet in the generator, up to the maximum number of results
        tasks = [executor.submit(process_tweet, tweet, nlp, counters, lock) for i, tweet in enumerate(tweets_list)]
        # Wait for all tasks to complete
        concurrent.futures.wait(tasks)

    avg_positive_score =\
        counters['positive']['score'] / counters['positive']['tweets'] if counters['positive']['tweets'] > 0 else 0
    avg_negative_score =\
        counters['negative']['score'] / counters['negative']['tweets'] if counters['negative']['tweets'] > 0 else 0

    return (
        counters['positive']['tweets'],
        counters['negative']['tweets'],
        counters['positive']['likes'],
        counters['negative']['likes'],
        counters['positive']['comments'],
        counters['negative']['comments'],
        counters['positive']['shares'],
        counters['negative']['shares'],
        avg_positive_score,
        avg_negative_score
    )


