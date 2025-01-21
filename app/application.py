from flask import Flask, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gzark1:mypassword@localhost/drinkdb'
db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    category = db.Column(db.String(50))
    glass_type = db.Column(db.String(50))
    ingredients = db.Column(db.Text)
    alcohol_type = db.Column(db.String(50))
    taste = db.Column(db.String(50))
    instructions = db.Column(db.Text)
    measurements = db.Column(db.Text)
    volume_ml = db.Column(db.Float)

    def __repr__(self):
        return f"<Drink {self.name} ({self.category})>"


@app.route('/')
def index():
    return 'Hello'

@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    output = []
    for drink in drinks:
        drink_data = {'id':drink.id, 'name': drink.name, 'description': drink.description}
        
        output.append(drink_data)
        

    return {"drinks": output}

@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {"name": drink.name, "description": drink.description}

@app.route('/drinks', methods = ['POST'])
def add_drink():
    drink = Drink(name=request.json['name'], description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id': drink.id}

@app.route('/drinks/<id>', methods = ['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {"error": "not found"}
    db.session.delete(drink)
    db.session.commit()
    return {"message": f"deleted {drink.name}!"}