from app import app, db, Power, Hero, HeroPower, Hero
from random import choice

def add_sample_data():
    with app.app_context():
        print("Deleting existing data...")
        HeroPower.query.delete()
        Power.query.delete()
        Hero.query.delete()
        db.session.commit()

        print("Adding sample powers...")
        powers_data = [
            {"name": "Super Strength", "description": "Gives the wielder super-human strengths"},
            {"name": "Flight", "description": "Gives the wielder the ability to fly through the skies at supersonic speed"},
            {"name": "Super Human Senses", "description": "Allows the wielder to use her senses at a super-human level"},
            {"name": "Elasticity", "description": "Can stretch the human body to extreme lengths"}
        ]

        for power_data in powers_data:
            power = Power(**power_data)
            db.session.add(power)

        db.session.commit()

        print("Adding sample heroes...")
        heroes_data = [
            {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
            {"name": "Doreen Green", "super_name": "Squirrel Girl"},
        ]

        for hero_data in heroes_data:
            hero = Hero(**hero_data)
            db.session.add(hero)

        db.session.commit()

        print("Creating hero-power associations...")
        strengths = ["Strong", "Weak", "Average"]
        heroes = Hero.query.all()

        for hero in heroes:
            for _ in range(1, 4):
                power = Power.query.order_by(db.func.random()).first()
                strength = choice(strengths)
                hero_power = HeroPower(hero=hero, power=power, strength=strength)
                db.session.add(hero_power)

        db.session.commit()

        print("Sample data added successfully!")

if __name__ == "__main__":
    add_sample_data()
