from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from flask import jsonify, request
db = SQLAlchemy()
from app import app

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

class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    super_name = db.Column(db.String(100), nullable=False)
    hero_powers = db.relationship('HeroPower', back_populates='hero')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'super_name': self.super_name,
            'powers': [power.serialize() for power in self.hero_powers]
        }

class Power(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    hero_powers = db.relationship('HeroPower', back_populates='power')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

class HeroPower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(50), nullable=False, server_default='Average')
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('power.id'), nullable=False)
    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='hero_powers')

    @validates('strength')
    def validate_strength(self, key, strength):
        assert strength in ['Strong', 'Weak', 'Average']
        return strength

    def serialize(self):
        return {
            'strength': self.strength,
            'power': self.power.serialize()
        }