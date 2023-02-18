from DAL.BaseDal import BaseDal
from DAL.DatabaseHelper import DatabaseHelper
from DAL.Tweet_Entity.TweetData import TweetData


class TweetDal(BaseDal):

    def getMovieTweets(self, movie_name):
        tweet_collection = self.db.getTweets()
        all_documents = tweet_collection.find({"movie_name": movie_name})
        # Check for successful query
        if all_documents is None:
            return None
        all_tweets = []
        for document in all_documents:
            all_tweets.append(TweetData(document["movie_name"], document["message"], document["likes"],
                                        document["replies"], document["shares"]))
        return all_tweets

    # override abstract method
    def save(self, entity):
        self.db.getTweets().insert_one(entity.__dic__())

