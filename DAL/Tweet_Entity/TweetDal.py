from DAL.DatabaseHelper import DatabaseHelper
from DAL.Tweet_Entity.TweetData import TweetData


class TweetDal:

    def getMovieTweets(self, movie_id):
        mydb = DatabaseHelper.getInstance()
        tweet_collection = mydb.getTweets()
        allDocuments = tweet_collection.find({"movieId": movie_id})
        # Check for successful query
        if allDocuments is None:
            return None
        allTweets = []
        for document in allDocuments:
            allTweets.append(TweetData(document["_id"], document["movieId"], document["message"], document["likes"], document["replies"], document["shares"]))
        return allTweets