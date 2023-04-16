from Backend.DAL.BaseDal import BaseDal
from Backend.DAL.Model_Entity.ModelData import ModelData


class ModelDal(BaseDal):
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if ModelDal.__instance is None:
            ModelDal()
        return ModelDal.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if ModelDal.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            super().__init__()
            ModelDal.__instance = self

    def getModel(self, name):
        models_collection = self.db.getModels()
        model = models_collection.find_one({"name": name})
        # Check for successful query
        if model is None:
            return None
        return ModelData(model["name"], model["model"], model["date"], model["genre_categories"],
                         model["rating_categories"], model["standard_scaler"], model["mape"])

    def save(self, model):
        self.db.saveModel(model)
