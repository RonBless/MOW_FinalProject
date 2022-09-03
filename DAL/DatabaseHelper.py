from pymongo import MongoClient


class DatabaseHelper:
    __instance = None

    @staticmethod
    def getInstance(): #singleton - we want to connect to the db only once
        """ Static access method. """
        if DatabaseHelper.__instance is None:
            DatabaseHelper()  #call constructor
        return DatabaseHelper.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if DatabaseHelper.__instance is not None:
            raise Exception("This class is a singleton!")
        else: #if the class doesn't exist, we create it
            DatabaseHelper.__instance = self
            self.client = MongoClient(
                "mongodb+srv://ronb:759r759R@mowdb.6vqlus6.mongodb.net/?retryWrites=true&w=majority")
            self.db = self.client.Mow
            self.tweets = self.db.Tweet
            self.movies = self.db.Movie
            if self.movies is None:
                self.InitializeDatabase()

    def InitializeDatabase(self):
        return

    def getMovies(self):
        return self.movies

    def getTweets(self):
        return self.tweets




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
