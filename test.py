# -*- coding: utf-8 -*-
#! /usr/bin/env python3

from flask import *
from flask_script import Manager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    if name == 'ice':
        abort(404)
    return render_template('user.html', name=name)

@app.route('/user/noname')
def noname():
    return '<h1> Sorry</h1>', 400

manager = Manager(app)
if __name__ == '__main__':
    manager.run()
