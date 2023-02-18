from DAL.BaseDal import BaseDal
from DAL.DatabaseHelper import DatabaseHelper
from DAL.Movie_Entity.MovieData import MovieData


class MovieDal(BaseDal):

    def getMovie(self, name):
        mydb = DatabaseHelper.getInstance()
        movies_collection = mydb.getMovies()
        movie = movies_collection.find_one({"name": name})
        # Check for successful query
        if movie is None:
            return None
        return MovieData(movie["name"], movie["earnings"], movie["release_date"])

    def save(self, entity):
        self.db.getMovies().insert_one(entity.__dic__())