# -*- coding: utf-8 -*-
__author__ = 'motomizuki'

from flask import Flask
from flask.ext.pymongo import PyMongo

from app.views import project_index


# flask app
app = Flask(__name__)
app.config.from_object("config")

# database setting
mongo = PyMongo(app)

# register view modules
app.register_blueprint(project_index.module)
# app.register_blueprint(module, url_prefix='/hoge')
