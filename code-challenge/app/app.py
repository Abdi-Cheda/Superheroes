from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
db = SQLAlchemy(app)

from models import Hero, Power, HeroPower
from routes import hero_routes, power_routes

if __name__ == '__main__':
    app.run(debug=True, port=5001)
