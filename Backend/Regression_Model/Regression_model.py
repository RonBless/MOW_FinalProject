from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import mean_absolute_percentage_error
from datetime import datetime
from Backend.DAL.Model_Entity.ModelDal import ModelDal
from Backend.DAL.Model_Entity.ModelData import ModelData
from Backend.GlobalSettings import GlobalSettings
import pickle
from Backend.Scripts.DataPreprocessing import PreprocessTrainingData, PreprocessTestData


class RegModel:
    __instance = None

    # Singleton implementation
    @staticmethod
    def getInstance():
        """ Static access method. """
        if RegModel.__instance is None:
            RegModel()
        return RegModel.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if RegModel.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            RegModel.__instance = self
            dal = ModelDal.getInstance()
            model_data = dal.getModel(GlobalSettings.getInstance().model_name)
            self.url = GlobalSettings.getInstance().training_url
            self.x_test = None
            self.y_test = None
            if model_data is not None:
                print("Model_data is not None")
                self.name = model_data.name
                self.date = model_data.date
                self.genre_categories = model_data.genre_categories
                self.rating_categories = model_data.rating_categories
                self.mape = model_data.mape
                self.model = pickle.loads(model_data.byte_string)
            else:
                self.name = GlobalSettings.getInstance().model_name
                self.x_train, self.y_train, self.genre_categories, self.rating_categories\
                    = PreprocessTrainingData(self.url)
                self.model = Sequential()
                # The Input Layer :
                self.model.add(
                    Dense(128, kernel_initializer='normal', input_dim=self.x_train.shape[1], activation='relu'))

                # The Hidden Layers :
                self.model.add(Dense(256, kernel_initializer='normal', activation='relu'))
                self.model.add(Dense(256, kernel_initializer='normal', activation='relu'))
                self.model.add(Dense(256, kernel_initializer='normal', activation='relu'))

                # The Output Layer :
                self.model.add(Dense(1, kernel_initializer='normal', activation='linear'))
                # Compile the network :
                self.model.compile(loss='mean_absolute_error', optimizer='adam', metrics=['mean_absolute_error'])

                self.TrainModel()
                self.TestModel()
                self.SaveModel()

    def TrainModel(self, x_train=None, y_train=None):
        if x_train is not None and y_train is not None:
            self.x_train = x_train
            self.y_train = y_train
        if self.x_train is not None and self.y_train is not None:
            self.model.fit(self.x_train,
                           self.y_train,
                           epochs=250,
                           batch_size=25,
                           validation_split=0.2)
            self.date = datetime.now().strftime('%d/%m/%Y')
        else:
            print("No training data was provided, Couldn't preform a training session")

    def TestModel(self):
        test_url = GlobalSettings.getInstance().test_url
        self.x_test, self.y_test = PreprocessTestData(test_url, self.genre_categories, self.rating_categories)

        # predict using the trained model
        y_pred = self.model.predict(self.x_test)

        # calculate the MAPE
        self.mape = mean_absolute_percentage_error(self.y_test, y_pred)

        print("MAPE:", self.mape)

    def SaveModel(self):
        # serialize the NN model to a byte string
        serialize_model = pickle.dumps(self.model)

        dal = ModelDal.getInstance()

        dal.save(ModelData(self.name,
                           serialize_model,
                           self.date,
                           self.genre_categories.tolist(),
                           self.rating_categories.tolist(),
                           self.mape))
