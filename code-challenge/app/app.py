from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize Flask app
app = Flask(__name__)
app.config.from_object('config.Config')

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import models and routes
with app.app_context():
    from models import *  # Import models
    import routes  # Import routes

if __name__ == '__main__':
    app.run(debug=True)
