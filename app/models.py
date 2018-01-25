# -*- coding: utf-8 -*-

from wekzeug.security import generate_password_hash, check_password_hash

class User(db.Model):

    password_hash = db.Column(db.String(128))
