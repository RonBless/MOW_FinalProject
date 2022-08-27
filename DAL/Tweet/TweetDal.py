from DAL.DatabaseHelper import DatabaseHelper
from DAL.Tweet.TweetData import TweetData


class MovieDal:

    def getMovie(self, id):
        mydb = DatabaseHelper.getInstance()
        movies_collection = mydb.getMovies()
        movie = movies_collection.find_one({"_id": id})
        # Check for successful query
        if movie is None:
            return None
        return TweetData(movie["_id"], movie["message"], movie["likes"])