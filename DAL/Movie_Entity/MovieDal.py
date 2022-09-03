from DAL.DatabaseHelper import DatabaseHelper
from DAL.Movie_Entity.MovieData import MovieData


class MovieDal:

    def getMovie(self, name):
        mydb = DatabaseHelper.getInstance()
        movies_collection = mydb.getMovies()
        movie = movies_collection.find_one({"name": name})
        # Check for successful query
        if movie is None:
            return None
        return MovieData(movie["_id"], movie["name"], movie["earnings"])

