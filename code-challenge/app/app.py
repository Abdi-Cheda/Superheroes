from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import jsonify, request
from models import Hero, Power, HeroPower,db
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACKING_MODIFICATIONS'] = False
CORS(app)

migrate=Migrate(app,db)
db.init_app(app)

@app.route('/')
def home():
    return "<h1>HELLO!</h1>"

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = [hero.serialize() for hero in Hero.query.all()]
    return jsonify(heroes)


@app.route('/heroes/<int:hero_id>', methods=['GET'])
def get_hero(hero_id):
    hero = Hero.query.get_or_404(hero_id)
    return jsonify(hero.serialize())

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = [power.serialize() for power in Power.query.all()]
    return jsonify(powers)

@app.route('/powers/<int:power_id>', methods=['GET'])
def get_power(power_id):
    power = Power.query.get_or_404(power_id)
    return jsonify(power.serialize())


if __name__ == '__main__':
    app.run(port=3001, debug=True)