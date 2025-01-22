from flask import Flask, request, jsonify
from flask_migrate import Migrate
from app.models import db, Drink, Ingredient, DrinkIngredient  # Import models

# Initialize Flask App
app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gzark1:mypassword@localhost/drinkdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # To prevent warnings

# Initialize Database and Migrations
db.init_app(app)
migrate = Migrate(app, db)

# ---------------------- Routes ----------------------

@app.route('/')
def index():
    return 'Hello! Welcome to the Drinks API.'

@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    output = [
        {"name": drink.name, "category": drink.category, "glass_type": drink.glass_type, "instructions": drink.instructions}
        for drink in drinks
    ]
    return jsonify({"drinks": output})

@app.route('/drinks/<string:name>')
def get_drink(name):
    drink = Drink.query.get_or_404(name)
    return jsonify({
        "name": drink.name,
        "category": drink.category,
        "glass_type": drink.glass_type,
        "instructions": drink.instructions,
        "ingredients": [
            {"name": di.ingredient_name, "measurement_ml": di.measurement_ml, "measurement_oz": di.measurement_oz}
            for di in drink.ingredients
        ]
    })

@app.route('/drinks', methods=['POST'])
def add_drink():
    data = request.json
    if not data or 'name' not in data:
        return jsonify({"error": "Invalid request"}), 400

    new_drink = Drink(
        name=data['name'],
        category=data.get('category', ''),
        glass_type=data.get('glass_type', ''),
        instructions=data.get('instructions', ''),
    )
    db.session.add(new_drink)
    db.session.commit()
    return jsonify({"message": "Drink added!", "name": new_drink.name})

@app.route('/drinks/<string:name>', methods=['DELETE'])
def delete_drink(name):
    drink = Drink.query.get(name)
    if not drink:
        return jsonify({"error": "Drink not found"}), 404

    db.session.delete(drink)
    db.session.commit()
    return jsonify({"message": f"Deleted {drink.name}!"})

# ---------------------- Flask App Run ----------------------
if __name__ == "__main__":
    app.run(debug=True)
