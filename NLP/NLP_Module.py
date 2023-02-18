from Twitter.TwitterAPI import TwitterAPI
from transformers import pipeline


class NLP:
    __instance = None

    # Singleton implementation
    @staticmethod
    def getInstance():
        """ Static access method. """
        if NLP.__instance is None:
            NLP()
        return NLP.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if NLP.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            NLP.__instance = self
            self.module = pipeline("sentiment-analysis", model="siebert/sentiment-roberta-large-english")

    def predict(self, message):
        result = self.module(message)[0]
        return result['label'], result['score']

