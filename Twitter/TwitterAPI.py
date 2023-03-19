import snscrape.modules.twitter as sntwitter
from DAL.Tweet_Entity.TweetData import TweetData
import concurrent.futures


class TwitterAPI:
    __instance = None

    # Singleton Implementation
    @staticmethod
    def getInstance():
        """ Static access method. """
        if TwitterAPI.__instance is None:
            TwitterAPI()
        return TwitterAPI.__instance

    def __init__(self, limit=100000):
        """ Virtually private constructor. """
        if TwitterAPI.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            TwitterAPI.__instance = self
            self.limit = limit
            self.language_filter = 'lang:en '

    def setLimit(self, limit):
        self.limit = limit

    @staticmethod
    def process_tweet(movie_name, tweet, tweets):
        data = TweetData(movie_name, tweet.rawContent, tweet.likeCount, tweet.replyCount, tweet.retweetCount)
        tweets.append(data)

    def getTweets(self, movie_name, start_date, end_date):
        # Define search phrases
        search_phrases = [
            f'("#{movie_name.replace(",", "").replace(" ", "").replace("-", "").replace(":", "")}Movie")',
            # f'("{movie_name} in Cinemas")',
            f'("The {movie_name} Movie")',
            # f'("The new {movie_name} Movie")',
            f'({movie_name} Trailer)',
            # f'({movie_name} new Trailer)',
            # f'(Poster for {movie_name} )',

        ]
        query = "(" + " OR ".join(search_phrases) + ") since:" + start_date + " until:" + end_date
        count = 0
        tweets: list[TweetData] = []
        scrapper = sntwitter.TwitterSearchScraper(self.language_filter + query).get_items()

        # Create a ThreadPoolExecutor with 16 worker threads
        with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
            # Submit tasks to the executor for each tweet in the generator, up to the maximum number of results
            tasks = [executor.submit(self.process_tweet, movie_name, tweet, tweets) for i, tweet in enumerate(scrapper)
                     if i < self.limit]
            # Wait for all tasks to complete
            concurrent.futures.wait(tasks)

        # for tweet in scrapper:
        #     if self.limit == count:
        #         break
        #     else:
        #         data = TweetData(movie_name, tweet.rawContent, tweet.likeCount, tweet.replyCount,
        #                          tweet.retweetCount)
        #         count = count + 1
        #         tweets.append(data)

        return tweets





