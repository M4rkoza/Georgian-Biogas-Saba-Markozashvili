from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

application = Flask(__name__, template_folder='template')
application.config["SECRET_KEY"] = ("t9027d|vA=@dQk/")
application.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

database = SQLAlchemy(application)
login_manager = LoginManager(application)

