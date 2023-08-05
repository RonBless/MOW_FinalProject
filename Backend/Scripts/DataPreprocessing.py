import pandas as pd
from sklearn.preprocessing import StandardScaler


def PreprocessTrainingData(url):
    df = pd.read_csv(url)

    x, y = FeatureSelectionAndCreation(df)

    # get all the categories from the training data frame
    genre_categories = pd.Categorical(x['genre']).categories
    rating_categories = pd.Categorical(x['rating']).categories

    # Normalization
    x_norm, sc = NormalizeData(x)

    # Encoding
    df_encoded = Encoding(x)

    # Merge categorical and numeric fields
    x = x_norm.join(df_encoded)
    return x, y, genre_categories, rating_categories, sc


def FeatureSelectionAndCreation(df):
    # Remove unnecessary fields
    df.drop(columns=['name', 'released', 'released_minus1', 'half_year_back',
                     'imdbID'], inplace=True)

    # Create new feature named 'total_tweets' from 'positive_tweets' and 'negative_tweets'
    df['total_tweets'] = df['positive_tweets'] + df['negative_tweets']

    # Remove all movies with no tweets and no rating
    df = df[df['total_tweets'] != 0]
    df = df[df['rating'] != 'Not Rated']

    # Separate training and target data
    x = df.drop('opening_weekend', axis=1)
    y = df['opening_weekend']
    x.reset_index(drop=True, inplace=True)
    y.reset_index(drop=True, inplace=True)
    return x, y


def NormalizeData(x, sc=None):
    numerical_df = x.drop(['genre', 'rating'], axis=1)

    # Train
    if sc is None:
        sc = StandardScaler()
        x_norm = sc.fit_transform(numerical_df)
        return pd.DataFrame(x_norm, columns=numerical_df.columns), sc
    # Test
    else:
        x_norm = sc.transform(numerical_df)
        return pd.DataFrame(x_norm, columns=numerical_df.columns)


def Encoding(x):
    df_categories = x[['genre', 'rating']].copy()
    return pd.get_dummies(df_categories, columns=['genre', 'rating'])


def PreprocessTestData(url, genre_categories, rating_categories, standard_scaler):
    df_test = pd.read_csv(url)

    x, y = FeatureSelectionAndCreation(df_test)
    # add the categories to the test data frame
    x['genre'] = pd.Categorical(x['genre'], categories=genre_categories)
    x['rating'] = pd.Categorical(x['rating'], categories=rating_categories)

    # Normalization
    x_norm = NormalizeData(x, standard_scaler)
    # Encoding
    df_encoded = Encoding(x)

    # Merge categorical and numeric fields
    x = x_norm.join(df_encoded)

    return x, y


