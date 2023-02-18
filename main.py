from DAL.Movie_Entity.MovieDal import MovieDal
from Twitter.TwitterAPI import TwitterAPI


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
    # name = "Spider-man: No Way Home"
    # dal = MovieDal()
    # data = dal.getMovie(name)
    # print(data)
    #
    # dal = TweetDal()
    # data = dal.getMovieTweets(data.name)
    # for tweet in data:
    #     print(tweet)

    twitter_api = TwitterAPI.getInstance()
    twitter_api.setLimit(1)
    tweets_list = twitter_api.getTweets("Spider-man: No Way Home", "2021-01-01", "2021-12-16")