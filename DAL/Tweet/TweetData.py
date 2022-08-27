

class TweetData:
    def __init__(self, id, message, likes, replies, shares):
        self.id = id
        self.message = message
        self.likes = likes
        self.replies = replies
        self.shares = shares

    def __str__(self):
        return "id:{} ,message: {}\n, Likes: {}\n".format(self.id, self.message, self.likes)
