from Backend.NLP.NLP_Model import NLP
from Backend.Twitter.TwitterAPI import TwitterAPI


def getMovieTweets(name, start_date, end_date):
    twitter = TwitterAPI.getInstance()
    tweets_list = twitter.getTweets(name, start_date, end_date)
    positive_tweets = 0
    negative_tweets = 0
    positive_likes = 0
    negative_likes = 0
    positive_comments = 0
    negative_comments = 0
    positive_shares = 0
    negative_shares = 0
    avg_positive_score = 0
    avg_negative_score = 0
    nlp = NLP.getInstance()
    for tweet in tweets_list:
        result = nlp.predict(tweet.message)
        match (result[0]):
            case 'POSITIVE':
                positive_tweets += 1
                positive_likes += tweet.likes
                positive_comments += tweet.replies
                positive_shares += tweet.shares
                avg_positive_score += result[1]
            case 'NEGATIVE':
                negative_tweets += 1
                negative_likes += tweet.likes
                negative_comments += tweet.replies
                negative_shares += tweet.shares
                avg_negative_score += result[1]

    if positive_tweets > 0:
        avg_positive_score = avg_positive_score / positive_tweets
    if negative_tweets > 0:
        avg_negative_score = avg_negative_score / negative_tweets

    return positive_tweets, negative_tweets, positive_likes, negative_likes, positive_comments, negative_comments,\
        positive_shares, negative_shares, avg_positive_score, avg_negative_score
