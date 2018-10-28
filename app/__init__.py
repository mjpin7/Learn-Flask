from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Creates the flask app object as an instance of the clas Flask
app = Flask(__name__)

# Tell flask to apply the configs from the config file
app.config.from_object(Config)

# Database object and migration engine
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models