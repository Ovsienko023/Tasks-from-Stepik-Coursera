from flask import Flask
from config import Config

from flask_login import LoginManager #login


app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)

from app import routes, models
