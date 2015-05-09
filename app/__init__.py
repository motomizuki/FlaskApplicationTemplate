# -*- coding: utf-8 -*-
__author__ = 'motomizuki'

from flask import Flask
from flask.ext.pymongo import PyMongo


class DefaultSettings:
    """
    settings of flask application
    """
    DEBUG = True
    HOST = '127.0.0.1'
    PORT = '8888'
    SECRET_KEY = 'secret_key'

    """
    settings of mongo database
    """
    # MONGO_URI = ""
    # MONGO_HOST = ""
    # MONGO_PORT = ""
    MONGO_DBNAME = "test"
    # MONGO_USERNAME = ""
    # MONGO_PASSWORD = ""


# flask app
app = Flask(__name__)
app.config.from_object(DefaultSettings)

# database setting
mongo = PyMongo(app)

# register view modules
# app.register_blueprint(module, url_prefix='/hoge')
