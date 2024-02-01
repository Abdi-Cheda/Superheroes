from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow all origins for simplicity; you can configure this according to your needs
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
db = SQLAlchemy(app)

from routes import hero_routes, power_routes

app.register_blueprint(hero_routes)
app.register_blueprint(power_routes)

if __name__ == '__main__':
    app.run(debug=True)
