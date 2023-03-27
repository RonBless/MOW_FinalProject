from Backend.GlobalSettings import GlobalSettings
from flask import Flask
from Backend.Regression_Model.Regression_model import RegModel

# def onStartup():
#     print("Welcome to MOW!\n")
#     print("We are going to help you estimate your desired movie opening weekend revenue according to Twitter\n")
#     print("Please enter the Movie_Entity Name\n")
#     movie_name = input()
#     print("We are on it!\n Loading...\n")
#     dal = MovieDal()
#     data = dal.getMovie(name)

GlobalSettings.getInstance()
reg_model = RegModel.getInstance()
reg_model.TestModel()
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return '<p>Hello, World!</p>'
#
#
# app.run()
