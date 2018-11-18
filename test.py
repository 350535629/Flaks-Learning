# -*- coding: utf-8 -*-
#! /usr/bin/env python3

from flask import *
from flask.ext.script import Manager

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1> Hello, %s!!</h1>' % user_agent

@app.route('/user/<name>')
def user(name):
    if name == 'ice':
        abort(404)
    return '<h1> Hello, user %s!</h1>' % name

@app.route('/user/noname')
def noname():
    return '<h1> Sorry</h1>', 400

manager = Manager(app)
if __name__ == '__main__':
    manager.run()
