# -*- coding: utf-8 -*-
#! /usr/bin/env python3

from flask import *
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'I am Ice'
bootstrap = Bootstrap(app)

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.et('name'))

@app.route('/user/<name>')
def user(name):
    if name == 'ice':
        abort(404)
    return render_template('user.html', name=name)

@app.route('/user/noname')
def noname():
    return '<h1> Sorry</h1>', 400

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
manager = Manager(app)
if __name__ == '__main__':
    manager.run()
