# from sqlalchemy.orm import validates
# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()

# class Hero(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     super_name = db.Column(db.String(100), nullable=False)
#     powers = db.relationship('HeroPower', back_populates='hero', lazy='dynamic')

#     def serialize(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'super_name': self.super_name,
#             'powers': [power.serialize() for power in self.powers]
#         }

# class Power(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.String(255), nullable=False)
#     heroes = db.relationship('HeroPower', back_populates='power', lazy='dynamic')

#     def serialize(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'description': self.description
#         }

# class HeroPower(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     strength = db.Column(db.String(50), nullable=False)
#     hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'), nullable=False)
#     power_id = db.Column(db.Integer, db.ForeignKey('power.id'), nullable=False)
#     hero = db.relationship('Hero', back_populates='powers')
#     power = db.relationship('Power', back_populates='heroes')

#     @validates('strength')
#     def validate_strength(self, key, strength):
#         assert strength in ['Strong', 'Weak', 'Average']
#         return strength

#     def serialize(self):
#         return {
#             'strength': self.strength,
#             'power': self.power.serialize()
#         }
    




from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Hero(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    powers = relationship("HeroPower", back_populates="hero")

class Power(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    heroes = relationship("HeroPower", back_populates="power")

class HeroPower(db.Model):
    id = Column(Integer, primary_key=True)
    hero_id = Column(Integer, ForeignKey('hero.id'), nullable=False)
    power_id = Column(Integer, ForeignKey('power.id'), nullable=False)
    hero = relationship("Hero", back_populates="powers")
    power = relationship("Power", back_populates="heroes")
