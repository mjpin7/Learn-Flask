import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Configures a config class with the class variables being the config settings
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secretpass'

    # Configs for sql alchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False