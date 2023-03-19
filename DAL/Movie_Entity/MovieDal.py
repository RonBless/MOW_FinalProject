from DAL.BaseDal import BaseDal
from DAL.DatabaseHelper import DatabaseHelper
from DAL.Movie_Entity.MovieData import MovieData


class MovieDal(BaseDal):
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if MovieDal.__instance is None:
            MovieDal()
        return MovieDal.__instance

    def __init__(self):
        super.__init__()
        """ Virtually private constructor. """
        if MovieDal.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            MovieDal.__instance = self

    def getMovie(self, name):
        movies_collection = self.db.getMovies()
        movie = movies_collection.find_one({"name": name})
        # Check for successful query
        if movie is None:
            return None
        return MovieData(movie["name"], movie["opening_weekend"], movie["positive_tweets"], movie["negative_tweets"],
                         movie["positive_likes"], movie["negative_likes"], movie["positive_comments"],
                         movie["negative_comments"], movie["positive_shares"], movie["negative_shares"],
                         movie["avg_positive_score"], movie["avg_negative_score"])

    def save(self, movie):
        self.db.saveMovie(movie)
