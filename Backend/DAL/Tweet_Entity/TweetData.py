from DAL.BaseData import BaseData


class TweetData(BaseData):
    def __init__(self, movie_name, message, likes, replies, shares):
        self.movie_name = movie_name
        self.message = message
        self.likes = likes
        self.replies = replies
        self.shares = shares

    def __str__(self):
        return "Message: {},\n Likes: {},\n Replies: {},\n Shares: {},\n".format(self.message, self.likes, self.replies, self.shares)

    def __dic__(self):
        return {'movie_name': self.movie_name,
                'message': self.message,
                'likes': self.likes,
                'replies': self.replies,
                'shares': self.shares
                }
