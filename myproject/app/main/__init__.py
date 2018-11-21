# -*- coding: utf-8 -*-

from flask import Blutprint

main = Blueprint('main', __name__)

from .import views, errors
