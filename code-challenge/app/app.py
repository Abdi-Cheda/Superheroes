# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask import jsonify

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from models import Hero, Power, HeroPower  # Import models here to avoid circular imports

def setup_routes(app):
    @app.route('/heroes', methods=['GET'])
    def get_heroes():
        from models import Hero  # Import within the function to avoid circular imports
        heroes = Hero.query.all()
        return jsonify([hero.serialize() for hero in heroes])
    # Define other routes similarly
        # Import routes
        from routes import setup_routes
        setup_routes(app)

    return app
