from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# ---------------------- Drink Model ----------------------
class Drink(db.Model):
    __tablename__ = 'drinks'

    name = db.Column(db.String(100), primary_key=True)  # Use name as primary key
    category = db.Column(db.String(50))
    glass_type = db.Column(db.String(50))
    instructions = db.Column(db.Text)
    image_url = db.Column(db.String(255))  # Optional for storing drink images

    # Relationship: One drink has many ingredients (many-to-many)
    ingredients = db.relationship('DrinkIngredient', back_populates='drink')

    def __repr__(self):
        return f"<Drink {self.name} ({self.category})>"


# ---------------------- Ingredient Model ----------------------
class Ingredient(db.Model):
    __tablename__ = 'ingredients'

    name = db.Column(db.String(100), primary_key=True)  # Use name as primary key
    alcohol_type = db.Column(db.String(50))  # Alcoholic / Non-Alcoholic
    taste = db.Column(db.String(50))  # Sweet, Bitter, Sour, etc.

    # Relationship: One ingredient belongs to many drinks (many-to-many)
    drinks = db.relationship('DrinkIngredient', back_populates='ingredient')

    def __repr__(self):
        return f"<Ingredient {self.name}>"


# ---------------------- Drink-Ingredient Association Table ----------------------
class DrinkIngredient(db.Model):
    __tablename__ = 'drink_ingredients'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    drink_name = db.Column(db.String(100), db.ForeignKey('drinks.name'), nullable=False)
    ingredient_name = db.Column(db.String(100), db.ForeignKey('ingredients.name'), nullable=False)
    measurement_oz = db.Column(db.String(50))  # Measurement in ounces
    measurement_ml = db.Column(db.Float)  # Measurement in milliliters

    # Define relationships
    drink = db.relationship('Drink', back_populates='ingredients')
    ingredient = db.relationship('Ingredient', back_populates='drinks')

    def __repr__(self):
        return f"<DrinkIngredient {self.drink_name} - {self.ingredient_name} ({self.measurement_ml}ml)>"
