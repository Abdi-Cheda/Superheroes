from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, Hero, Power, HeroPower  # This import might be better placed after the app and db initialization to avoid circular imports


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

# If you run into a circular import here, consider moving the imports to inside a function or right before they are used.


