from Backend.DAL.BaseData import BaseData


class ModelData(BaseData):

    def __init__(self, name, model_byte_string, date, genre_categories, rating_categories,
                 standard_scaler_model_byte_string, mape):
        self.name = name
        self.model = model_byte_string
        self.date = date
        self.genre_categories = genre_categories
        self.rating_categories = rating_categories
        self.standard_scaler = standard_scaler_model_byte_string
        self.mape = mape

    def __str__(self):
        return "name: {}, Last trained at: {}, Test Score: {}%".format(self.name, self.date, 100 - self.mape)

    def __dic__(self):
        return {'name': self.name,
                'model': self.model,
                'date': self.date,
                'genre_categories': self.genre_categories,
                'rating_categories': self.rating_categories,
                'standard_scaler': self.standard_scaler,
                'mape': self.mape}
