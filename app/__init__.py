from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging 
from logging.handlers import SMTPHandler, RotatingFileHandler
import os

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

# If the app is not in debug mode, then enable the email logger
if not app.debug:
    if app.config['MAIL_SERVER']:

        # Get the auth and security if set in env
        auth = None
        if app.config['MAIL_USERNAME' or app.config['MAIL_PASSWORD']]:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        
        # Set the mail handler based on the env vars
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='MyBlog Error',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    # This creates an error log file in the logs directory
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/myblog.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    
    app.logger.setLevel(logging.INFO)
    app.logger.info('MyBlog startup')

from app import routes, models, errors