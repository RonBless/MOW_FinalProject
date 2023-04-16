from pymongo import MongoClient


class DatabaseHelper:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if DatabaseHelper.__instance is None:
            DatabaseHelper()
        return DatabaseHelper.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if DatabaseHelper.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            DatabaseHelper.__instance = self
            self.client = MongoClient(
                "mongodb+srv://ronb:AfekaFinalsProject@mowdb.6vqlus6.mongodb.net/?retryWrites=true&w=majority")
            self.db = self.client.Mow
            self.tweets = self.db.Tweet
            self.movies = self.db.Movie
            self.models = self.db.Model
            # self.movies.delete_many({})
            if self.movies.count_documents({}) == 0:
                self.InitializeDatabase()

    # Will go over each movie and extract the Tweets about the movie
    def InitializeDatabase(self):
        return

    def getMovies(self):
        return self.movies

    def getTweets(self):
        return self.tweets

    def getModels(self):
        return self.models

    def saveMovie(self, movie):
        self.movies.insert_one(movie.__dic__())

    def saveModel(self, model):
        self.models.insert_one(model.__dic__())





 # ********** POST Action in DB in Tweet_Entity Table **********
# post = {"_id": 1, "name": "tim", "score": 5}
# collection.insert_one(post)

# ********** GET Action in DB in Tweet_Entity Table **********
# query = .find_one({"name": "tim"})
# print(query)
# for result in query:
#     print(result)

# ********** Delete Action in DB in Tweet_Entity Table **********
# collection.delete_one({"_id": 1})
