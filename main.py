from DAL.DatabaseHelper import DatabaseHelper
from DAL.Movie_Entity.MovieDal import MovieDal
from DAL.Tweet_Entity.TweetDal import TweetDal


def onStartup():
    print("Welcome to MOW!\n")
    print("We are gonna help you estimate your desired movie opening weekend revenue according to Twitter\n")
    print("Please enter the Movie_Entity Name\n")
    movie_name = input()
    print("We are on it!\n Loading...\n")
    dal = MovieDal()
    data = dal.getMovie(name)


if __name__ == '__main__':
    # onStartup()
    name = "Spider-man"
    dal = MovieDal()
    data = dal.getMovie(name)
    print(data)

    dal = TweetDal()
    data = dal.getMovieTweets(data.id)
    for tweet in data:
        print(tweet)


