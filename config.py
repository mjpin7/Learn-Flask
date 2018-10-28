import os

# Configures a config class with the class variables being the config settings
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secretpass'