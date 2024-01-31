from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from random import randint, choice
from app import create_app  # Adjust the import path according to your project structure
from models import db  # Adjust the import path as necessary


app = create_app()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

with app.app_context():
    # Now you can work with the database
    db.create_all()

class Power(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250))

class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    super_name = db.Column(db.String(100), nullable=False)

class HeroPower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('power.id'), nullable=False)
    strength = db.Column(db.String(50))
# Create the tables
db.create_all()

# Seeding the database
def seed_data():
    print("🦸‍♀️ Seeding powers...")
    powers = [
        {"name": "super strength", "description": "gives the wielder super-human strengths"},
        {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
        {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
        {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
    ]

    for power in powers:
        db.session.add(Power(**power))

    print("🦸‍♀️ Seeding heroes...")
    heroes = [
        {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
        {"name": "Doreen Green", "super_name": "Squirrel Girl"},
        # Add the rest of your heroes here...
    ]

    for hero in heroes:
        db.session.add(Hero(**hero))

    db.session.commit()

    print("🦸‍♀️ Adding powers to heroes...")

    strengths = ["Strong", "Weak", "Average"]
    heroes = Hero.query.all()
    for hero in heroes:
        for _ in range(randint(1, 3)):  # Assuming you've imported randint from random
            power = Power.query.order_by(func.random()).first()  # For SQLite
            hero_power = HeroPower(hero_id=hero.id, power_id=power.id, strength=choice(strengths))  # Assuming you've imported choice from random
            db.session.add(hero_power)

    db.session.commit()

    print("🦸‍♀️ Done seeding!")

if __name__ == '__main__':
    seed_data()
