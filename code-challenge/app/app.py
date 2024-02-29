from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACKING_MODIFICATIONS'] = False
CORS(app)

migrate=Migrate(app)

if __name__ == '__main__':
    app.run(port=3000, debug=True)