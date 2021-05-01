"""
Manages the creation of flask objects
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

static_dir = os.path.join(os.path.dirname(__file__), 'front_end/build')
app = Flask(__name__, static_folder=static_dir, static_url_path='')

app.config['SECRET_KEY'] = 'JofJtRHKzQmFRXGI4v60'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['BASEDIR'] = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

db = SQLAlchemy()
db.init_app(app)

from animal_adoption.models.db import *

if not os.path.exists('db.sqlite') and os.environ.get('ENV', None) != 'prod':
    with app.app_context():
        db.create_all()

from animal_adoption import routes
