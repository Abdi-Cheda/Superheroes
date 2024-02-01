from flask import jsonify, request, Blueprint
from models import Hero, Power, HeroPower

hero_routes = Blueprint('hero_routes', __name__)
power_routes = Blueprint('power_routes', __name__)

@hero_routes.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.serialize() for hero in heroes])

@hero_routes.route('/heroes/<int:hero_id>', methods=['GET'])
def get_hero(hero_id):
    hero = Hero.query.get_or_404(hero_id)
    return jsonify(hero.serialize())

@power_routes.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.serialize() for power in powers])

@power_routes.route('/powers/<int:power_id>', methods=['GET'])
def get_power(power_id):
    power = Power.query.get_or_40