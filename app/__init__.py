from flask import Flask
from config import Config

# Creates the flask app object as an instance of the clas Flask
app = Flask(__name__)

# Tell flask to apply the configs from the config file
app.config.from_object(Config)

from app import routes