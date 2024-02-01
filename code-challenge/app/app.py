from app import app
from app.models import Hero, Power, HeroPower  # Import models here to avoid circular imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True, port=5555)

    from app import routes  # Import routes after creating app to avoid circular import