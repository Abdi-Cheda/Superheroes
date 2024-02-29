# Superheroes API

This is a simple Flask API for managing superheroes and their powers. It allows users to retrieve information about heroes, powers, and their relationships.

## Setup

1. Clone the repository:

git clone https://github.com/Abdi-Cheda/superheroes-api.git

2. Install dependencies:

pip install -r requirements.txt

3. Initialize the database:

python
from app import db
db.create_all()
exit()

4. Seed the database with sample data:

python seed.py

5. Run the application:

flask run

The application will be running on `http://localhost:5000/`.

## Endpoints

### Heroes

#### Get all heroes

GET /heroes

#### Response:
```json
[
    {
        "id": 1,
        "name": "Kamala Khan",
        "super_name": "Ms. Marvel",
        "powers": [
            {
                "strength": "Strong",
                "power": {
                    "id": 1,
                    "name": "Super Strength",
                    "description": "Gives the wielder super-human strengths"
                }
            },
            ...
        ]
    },
    ...
]
Get a specific hero
GET /heroes/<hero_id>
Response:
json
{
    "id": 1,
    "name": "Kamala Khan",
    "super_name": "Ms. Marvel",
    "powers": [
        {
            "strength": "Strong",
            "power": {
                "id": 1,
                "name": "Super Strength",
                "description": "Gives the wielder super-human strengths"
            }
        },
        ...
    ]
}
Powers
Get all powers
GET /powers
Response:
json
[
    {
        "id": 1,
        "name": "Super Strength",
        "description": "Gives the wielder super-human strengths"
    },
    ...
]
Get a specific power
GET /powers/<power_id>
Response:

json
{
    "id": 1,
    "name": "Super Strength",
    "description": "Gives the wielder super-human strengths"
}
Author
Abdirahman Cheda

License
This project is licensed under the MIT License.

[Abdi Cheda](https://github.com/Abdi-Cheda).