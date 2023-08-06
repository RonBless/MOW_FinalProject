import json

import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import mean_absolute_percentage_error
from datetime import datetime
from Backend.DAL.Model_Entity.ModelDal import ModelDal
from Backend.DAL.Model_Entity.ModelData import ModelData
from Backend.GlobalSettings import GlobalSettings
import pickle
from Backend.Scripts.DataPreprocessing import PreprocessTrainingData, PreprocessTestData
from sklearn.metrics import mean_absolute_error, mean_squared_error


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
                self.name = model_data.name
                self.date = model_data.date
                self.genre_categories = model_data.genre_categories
                self.rating_categories = model_data.rating_categories
                self.mape = model_data.mape
                self.model = pickle.loads(model_data.model)
                self.standard_scaler = pickle.loads(model_data.standard_scaler)
            else:
                self.name = GlobalSettings.getInstance().model_name
                self.x_train, self.y_train, self.genre_categories, self.rating_categories, self.standard_scaler\
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
        self.x_test, self.y_test = PreprocessTestData(test_url,
                                                      self.genre_categories,
                                                      self.rating_categories,
                                                      self.standard_scaler)

        # predict using the trained model
        y_pred = self.model.predict(self.x_test)

        # y_true: actual values, y_pred: predicted values

        # calculate the MAE
        mae = mean_absolute_error(self.y_test, y_pred)
        print("MAE", mae)

        # calculate the RMSE
        rmse = mean_squared_error(self.y_test, y_pred, squared=False)
        print("RMSE", rmse)

        # calculate the MAPE
        self.mape = mean_absolute_percentage_error(self.y_test, y_pred)
        print("MAPE:", self.mape)

    def SaveModel(self):
        # serialize the NN model to a byte string
        serialize_model = pickle.dumps(self.model)
        serialize_sc = pickle.dumps(self.standard_scaler)

        dal = ModelDal.getInstance()

        dal.save(ModelData(self.name,
                           serialize_model,
                           self.date,
                           self.genre_categories.tolist(),
                           self.rating_categories.tolist(),
                           serialize_sc,
                           self.mape))

    def Predict(self, url):
        df = pd.read_csv(url)
        print(df)
        x_req, y_req = PreprocessTestData(url, self.genre_categories, self.rating_categories, self.standard_scaler)
        y = self.model.predict(x_req)
        print("Predicted Opening Weekend Revenue:", y[0][0], '$')
        return y

    def PredictWithError(self, url):
        df = pd.read_csv(url)
        print(df)
        x_req, y_req = PreprocessTestData(url, self.genre_categories, self.rating_categories, self.standard_scaler)
        y_pred = self.model.predict(x_req)
        print("Predicted Opening Weekend Revenue:", y_pred[0][0], '$')

        # calculate the MAPE
        mape = mean_absolute_percentage_error(y_req, y_pred)
        print("% Error From the actual revenue:", mape*100)
        return y_pred
