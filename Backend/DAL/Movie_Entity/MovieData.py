from Backend.DAL.BaseData import BaseData


class MovieData(BaseData):

    def __init__(self, name, opening_weekend, release_date,  rating, genre, budget, positive_tweets, negative_tweets, positive_likes, negative_likes,
                 positive_comments, negative_comments, positive_shares, negative_shares, avg_positive_score,
                 avg_negative_score):
        self.name = name
        self.opening_weekend = opening_weekend
        self.release_date = release_date
        self.rating = rating
        self.genre = genre
        self.budget = budget
        self.positive_tweets = positive_tweets
        self.negative_tweets = negative_tweets
        self.positive_likes = positive_likes
        self.negative_likes = negative_likes
        self.positive_comments = positive_comments
        self.negative_comments = negative_comments
        self.positive_shares = positive_shares
        self.negative_shares = negative_shares
        self.avg_positive_score = avg_positive_score
        self.avg_negative_score = avg_negative_score

    def __str__(self):
        return "name: {}, Opening week earnings: {}\n" \
               "positive tweets: {}, negative tweets: {}\n" \
               "positive likes: {}, negative likes: {}\n" \
               "positive comments: {}, negative_comments: {}\n" \
               "positive shares: {}, negative_shares: {}\n" \
               "avg_positive_score: {}, avg_negative_score: {}\n" \
            .format(self.name, self.opening_weekend, self.positive_tweets, self.negative_tweets, self.positive_likes,
                    self.negative_likes, self.positive_comments, self.negative_comments, self.positive_shares,
                    self.negative_shares, self.avg_positive_score, self.avg_negative_score)

    def __dic__(self):
        return {'name': self.name,
                'release_date': self.release_date,
                'rating': self.rating,
                'genre': self.genre,
                'budget': self.budget,
                'opening_weekend': self.opening_weekend,
                'positive_tweets': self.positive_tweets,
                'negative_tweets': self.negative_tweets,
                'positive_likes': self.positive_likes,
                'negative_likes': self.negative_likes,
                'positive_comments': self.positive_comments,
                'negative_comments': self.negative_comments,
                'positive_shares': self.positive_shares,
                'negative_shares': self.negative_shares,
                'avg_positive_score': self.avg_positive_score,
                'avg_negative_score': self.avg_negative_score,
                }
