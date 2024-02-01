from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
db = SQLAlchemy(app)

from models import Hero, Power, HeroPower  # This import might be better placed after the app and db initialization to avoid circular imports

