

class TweetData:
    def __init__(self, id, movieId, message, likes, replies, shares):
        self.id = id
        self.movieId = movieId
        self.message = message
        self.likes = likes
        self.replies = replies
        self.shares = shares

    def __str__(self):
        return "Message: {},\n Likes: {},\n Replies: {},\n Shares: {},\n".format(self.message, self.likes, self.replies, self.shares)
