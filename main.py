from DAL.DatabaseHelper import DatabaseHelper
from DAL.Movie_Entity.MovieDal import MovieDal
from DAL.Tweet_Entity.TweetDal import TweetDal
from NLP.NLP_Module import NLP
from Scripts.InitializeTrainingDataset import add_Tweets_data_to_movies
from Twitter.TwitterAPI import TwitterAPI


# def onStartup():
#     print("Welcome to MOW!\n")
#     print("We are going to help you estimate your desired movie opening weekend revenue according to Twitter\n")
#     print("Please enter the Movie_Entity Name\n")
#     movie_name = input()
#     print("We are on it!\n Loading...\n")
#     dal = MovieDal()
#     data = dal.getMovie(name)


if __name__ == '__main__':
    # onStartup()
    # dal = MovieDal()
    # name = "Spider-man: No Way Home"
    # data = dal.getMovie(name)
    # print(data)
    #
    # dal = TweetDal()
    # data = dal.getMovieTweets(data.name)
    # for tweet in data:
    #     print(tweet)
    #
    #
    # nlp = NLP.getInstance()
    #
    #twitter_api.setLimit(10)

    # twitter_api = TwitterAPI.getInstance()
    # tweets_list = twitter_api.getTweets("ThereWill Be Blood", "2007-07-26", "2008-01-24")
    # for t in tweets_list:
    #     print(t.message)

    add_Tweets_data_to_movies()

