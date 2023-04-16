import time
import pandas as pd
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from Backend.GlobalSettings import GlobalSettings
from Backend.Scripts.ExtractMovieTweets import getMovieTweets


# Create us a training data set of 300 movies since 2016, with 'name', 'imdbID', 'released' (released date),
# 'half_year_back' (half a year before the released date), and 'opening_weekend' (our target)
def createTrainingDatasetFromScratch():
    url = GlobalSettings.raw_data_url
    df = pd.read_csv(url)

    df = df[df['year'] >= 2010]
    df.drop(['score', 'votes', 'director', 'writer', 'star', 'company', 'runtime', 'gross',
             'year'], axis=1, inplace=True)
    df = df[df['country'] == 'United States']
    df = df.drop(['country'], axis=1)
    df.loc[:, 'released'] = df['released'].apply(format_date)
    df = df.dropna()

    df.loc[:, 'released'] = pd.to_datetime(df['released'])  # Convert date column to datetime if not already
    df.loc[:, 'released_minus1'] = df['released'] - pd.Timedelta('1 day')
    half_year = pd.Timedelta(days=365 / 2)  # Calculate half a year in days
    df.loc[:, 'half_year_back'] = (df['released'] - half_year).dt.strftime('%Y-%m-%d')

    df.loc[:, 'imdbID'] = df['name'].apply(lambda x: get_imdbID(x))
    df.dropna(inplace=True)

    df.loc[:, 'opening_weekend'] = df['imdbID'].apply(lambda x: get_opening_weekend(x))
    df = df.reset_index(drop=True)

    df.to_csv("Movies_without_tweets_dataset.csv", index=False)


def format_date(date_string):
    try:
        date_obj = datetime.strptime(date_string.split(" (")[0], "%B %d, %Y")
        return date_obj.strftime("%Y-%m-%d")
    except ValueError:
        return None


def get_imdbID(movie):
    # Make the request to the API Using premium key
    response = requests.get(f'http://www.omdbapi.com/?t={movie}&apikey=81da4569')
    data = response.json()

    # Check if the response has a "BoxOffice" key
    if "BoxOffice" in data:
        # Extract the opening weekend revenue from the "BoxOffice" value
        box_office = data["imdbID"]
        imdb_id = box_office.split()[0]
        return imdb_id
    else:
        # If the response doesn't have a "BoxOffice" key, return None
        return None


# Convert '1,200,321$' to 1200321
def convert_currency_string_to_int(currency_str):
    return int(''.join(filter(str.isdigit, currency_str)))


# Get the opening weekend for a movie from box office mojo website using its imdbID
def get_opening_weekend(movie_id):
    url = f'https://www.boxofficemojo.com/title/{movie_id.replace(" ", "-")}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # find all links that contain "/weekend?ref_=bo_tt_gr#table" in their URL
    links = soup.find_all("a", href=lambda href: href and "/weekend?ref_=bo_tt_gr#table" in href)

    # extract the link text from each link
    if len(links) > 0:
        return convert_currency_string_to_int(links[0].text)
    time.sleep(10)
    return None


def add_Tweets_data_to_movies(url=GlobalSettings.getInstance().movies_without_tweets_url):
    df = pd.read_csv(url)
    df = df.assign(**{'positive_tweets': 0, 'negative_tweets': 0, 'positive_likes': 0, 'negative_likes': 0,
                      'positive_comments': 0, 'negative_comments': 0, 'positive_shares': 0, 'negative_shares': 0,
                      'avg_positive_score': 0, 'avg_negative_score': 0})

    for index, row in df.iterrows():
        positive_tweets, negative_tweets, positive_likes, negative_likes, positive_comments, negative_comments, \
            positive_shares, negative_shares, avg_positive_score, avg_negative_score = \
            getMovieTweets(row['name'], row['half_year_back'], row['released_minus1'])

        df.at[index, 'positive_tweets'] = positive_tweets
        df.at[index, 'negative_tweets'] = negative_tweets
        df.at[index, 'positive_likes'] = positive_likes
        df.at[index, 'negative_likes'] = negative_likes
        df.at[index, 'positive_comments'] = positive_comments
        df.at[index, 'negative_comments'] = negative_comments
        df.at[index, 'positive_shares'] = positive_shares
        df.at[index, 'negative_shares'] = negative_shares
        df.at[index, 'avg_positive_score'] = avg_positive_score
        df.at[index, 'avg_negative_score'] = avg_negative_score
        print(row['name'], positive_tweets + negative_tweets)
        df.to_csv('Training_Dataset_movies_2010_{}.csv'.format(index), index=False)
