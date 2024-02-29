from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from .models import db, Power, Hero, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACKING_MODIFICATIONS'] = False

migrate=Migrate(app,db)
db.init_app(app)

@app.route("/")
def home():
    return "Hello World!!!"

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([{
        'id': hero.id,
        'name': hero.name,
        'super_name': hero.super_name,
        'powers': [power.serialize() for power in hero.hero_powers]
    } for hero in heroes])

@app.route('/heroes/<int:hero_id>', methods=['GET'])
def get_hero(hero_id):
    hero = Hero.query.get_or_404(hero_id)
    return jsonify({
        'id': hero.id,
        'name': hero.name,
        'super_name': hero.super_name,
        'powers': [power.serialize() for power in hero.hero_powers]
    })

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([{
        'id': power.id,
        'name': power.name,
        'description': power.description
    } for power in powers])

@app.route('/powers/<int:power_id>', methods=['GET'])
def get_power(power_id):
    power = Power.query.get_or_404(power_id)
    return jsonify({
        'id': power.id,
        'name': power.name,
        'description': power.description
    })

@app.route('/hero_powers', methods=['GET'])
def get_hero_powers():
    hero_powers = HeroPower.query.all()
    return jsonify([{
        'id': hero_power.id,
        'strength': hero_power.strength,
        'hero_id': hero_power.hero_id,
        'power_id': hero_power.power_id
    } for hero_power in hero_powers])

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    hero_id = data.get('hero_id')
    power_id = data.get('power_id')
    strength = data.get('strength')

    if hero_id is None or power_id is None or strength is None:
        return make_response(jsonify({'errors': ['Missing required data']}), 400)

    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)

    if not hero or not power:
        return make_response(jsonify({'errors': ['Hero or Power not found']}), 404)

    new_hero_power = HeroPower(hero=hero, power=power, strength=strength)

    try:
        db.session.add(new_hero_power)
        db.session.commit()
        return jsonify({
            'id': hero.id,
            'name': hero.name,
            'super_name': hero.super_name,
            'powers': [{
                'id': power.id,
                'name': power.name,
                'description': power.description
            }]
        }), 201
    except Exception as e:
        return make_response(jsonify({'errors': [str(e)]}), 400)

if __name__ == '__main__':
    app.run(port=5000)
