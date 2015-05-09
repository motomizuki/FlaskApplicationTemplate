# -*- coding: utf-8 -*-
__author__ = 'motomizuki'

from flask import Blueprint
module = Blueprint('index', __name__)

@module.route('/')
def index():
    return 'Hello flask!'
