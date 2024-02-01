from app import app
from app.models import Hero, Power, HeroPower  # Import models here to avoid circular imports

if __name__ == '__main__':
    app.run(debug=True, port=5555)
