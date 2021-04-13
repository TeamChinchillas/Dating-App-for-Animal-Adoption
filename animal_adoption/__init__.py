"""
Manages the creation of flask objects
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'JofJtRHKzQmFRXGI4v60'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['BASEDIR'] = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

db = SQLAlchemy()
db.init_app(app)

if not os.path.exists('db.sqlite'):
    with app.app_context():
        db.create_all()

from animal_adoption import routes
