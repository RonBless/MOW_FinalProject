from DAL.BaseData import BaseData


class ModelData(BaseData):

    def __init__(self, name, byte_string, date, genre_categories, rating_categories, mape):
        self.name = name
        self.byte_string = byte_string
        self.date = date
        self.genre_categories = genre_categories
        self.rating_categories = rating_categories
        self.mape = mape

    def __str__(self):
        return "name: {}, Last trained at: {}, Test Score: {}%".format(self.name, self.date, 100 - self.mape)

    def __dic__(self):
        return {'name': self.name,
                'byte_string': self.byte_string,
                'date': self.date,
                'genre_categories': self.genre_categories,
                'rating_categories': self.rating_categories,
                'mape': self.mape}

