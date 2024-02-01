from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.models import Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Import models after db is created to avoid circular imports
from app.models import Hero, Power, HeroPower
