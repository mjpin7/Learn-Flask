from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Creates the flask app object as an instance of the clas Flask
app = Flask(__name__)

# Tell flask to apply the configs from the config file
app.config.from_object(Config)

# Database object and migration engine
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Login manager initialization
login = LoginManager(app)
# Sets the login view, this is used for forcing users to login to view certain pages
login.login_view = 'login'

from app import routes, models, errors