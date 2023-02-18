import snscrape.modules.twitter as sntwitter
from Tweet_Entity.TweetData import TweetData


class TwitterAPI:
    __instance = None

    # Singleton Implementation
    @staticmethod
    def getInstance():
        """ Static access method. """
        if TwitterAPI.__instance is None:
            TwitterAPI()
        return TwitterAPI.__instance

    def __init__(self, limit=100):
        """ Virtually private constructor. """
        if TwitterAPI.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            TwitterAPI.__instance = self
            self.limit = limit
            self.language_filter = 'lang:en '

    def setLimit(self, limit):
        self.limit = limit

    def getTweets(self, movie_name, start_date, end_date):
        query = "(#" + movie_name + ") since:" + start_date + " until:" + end_date
        count = 0
        tweets: list[TweetData] = []
        scrapper = sntwitter.TwitterSearchScraper(self.language_filter + query)
        for tweet in scrapper.get_items():
            if self.limit == count:
                break
            else:
                data = TweetData(movie_name, tweet.rawContent, tweet.likeCount, tweet.replyCount,
                                 tweet.retweetCount)
                count = count + 1
                tweets.append(data)
                print(data)
        return tweets


twitter_api = TwitterAPI.getInstance()
tweets_list = twitter_api.getTweets("Spider-man: No Way Home", "2021-01-01", "2021-12-16")
