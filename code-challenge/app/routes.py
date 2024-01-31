from flask import jsonify, request
# from app import app, db
from models import Hero, Power, HeroPower
from app import  app, db

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.serialize() for hero in heroes])

@app.route('/heroes/<int:hero_id>', methods=['GET'])
def get_hero(hero_id):
    hero = Hero.query.get_or_404(hero_id)
    return jsonify(hero.serialize())

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.serialize() for power in powers])

@app.route('/powers/<int:power_id>', methods=['GET'])
def get_power(power_id):
    power = Power.query.get_or_404(power_id)
    return jsonify(power.serialize())

@app.route('/powers/<int:power_id>', methods=['PATCH'])
def update_power(power_id):
    power = Power.query.get_or_404(power_id)
    data = request.get_json()
    description = data.get('description', '')
    if len(description) >= 20:
        power.description = description
        db.session.commit()
        return jsonify(power.serialize())
    else:
        return jsonify({"errors": ["Description must be at least 20 characters long."]}), 400

@app.route('/hero_powers', methods=['POST'])
def add_hero_power():
    data = request.get_json()
    strength = data.get('strength')
    power_id = data.get('power_id')
    hero_id = data.get('hero_id')
    
    new_hero_power = HeroPower(strength=strength, power_id=power_id, hero_id=hero_id)
    db.session.add(new_hero_power)
    db.session.commit()
    return jsonify(Hero.query.get_or_404(hero_id).serialize())
