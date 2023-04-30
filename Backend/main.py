import pandas as pd
from Backend.DAL.Movie_Entity.MovieDal import MovieDal
from Backend.GlobalSettings import GlobalSettings
from Backend.InputOutputMethods import *
from Backend.Regression_Model.Regression_model import RegModel
from Backend.Scripts.ExtractMovieTweets import getMovieTweets
from Backend.Scripts.InitializeTrainingDataset import add_Tweets_data_to_movies


def getInputFromUser():
    print("Welcome to MOW!\n")
    print("We are going to help you estimate your desired movie opening weekend revenue according to Twitter traffic\n")

    # Test Code
    name = "John Wick: Chapter 4"
    date = "23/03/2023"
    genre = "Action"
    rating = "R"
    budget = 100000000

    # Production Code
    # name = receiveName()
    # date = receiveReleaseDate()
    # genre = receiveGenre()
    # rating = receiveAgeRating()
    # budget = receiveBudget()

    print("We are on it!")
    return name, date, genre, rating, budget


def preprocessData(name, date, genre, rating, budget):
    df = pd.read_csv(g_settings.training_url)
    df = df.drop(index=df.index)    # Drop all rows
    df.loc[len(df)] = {'name': name, 'rating': rating, 'genre': genre, 'released': date, 'budget': budget}
    df['released'] = pd.to_datetime(df['released'], dayfirst=True)  # Convert date column to datetime if not already
    df['released_minus1'] = df['released'] - pd.Timedelta('1 day')
    half_year = pd.Timedelta(days=365 / 2)  # Calculate half a year in days
    df['half_year_back'] = (df['released'] - half_year).dt.strftime('%Y-%m-%d')
    df['half_year_back'] = df['half_year_back'].astype(str)     # Convert back to string
    df['released_minus1'] = df['released_minus1'].astype(str)     # Convert back to string

    df.fillna(0)
    df.to_csv(g_settings.request_path, index=False)
    add_Tweets_data_to_movies(g_settings.request_path, g_settings.request_path)


def getMovieOpeningWeekend():
    reg_model = RegModel.getInstance()
    result = reg_model.Predict(g_settings.request_path)


def onStartup():
    reg_model = RegModel.getInstance()
    name, date, genre, rating, budget = getInputFromUser()
    preprocessData(name, date, genre, rating, budget)
    getMovieOpeningWeekend()


g_settings = GlobalSettings.getInstance()
onStartup()
# onStartup()

