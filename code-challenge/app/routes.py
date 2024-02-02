# from flask import jsonify, request
# from models import Hero, Power, HeroPower
# from app import app

# @app.route('/')
# def home():
#     return "HELLO!"

# @app.route('/heroes', methods=['GET'])
# def get_heroes():
#     heroes = Hero.query.all()
#     return jsonify([hero.serialize() for hero in heroes])

# @app.route('/heroes/<int:hero_id>', methods=['GET'])
# def get_hero(hero_id):
#     hero = Hero.query.get_or_404(hero_id)
#     return jsonify(hero.serialize())

# @app.route('/powers', methods=['GET'])
# def get_powers():
#     powers = Power.query.all()
#     return jsonify([power.serialize() for power in powers])

# @app.route('/powers/<int:power_id>', methods=['GET'])
# def get_power(power_id):
#     power = Power.query.get_or_404(power_id)
#     return jsonify(power.serialize())