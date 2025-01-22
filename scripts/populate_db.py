import pandas as pd
from sqlalchemy import create_engine
from app.models import db, Drink, Ingredient, DrinkIngredient
from app.application import app  # Import Flask app

# Database connection setup
DB_URI = "postgresql://gzark1:mypassword@localhost/drinkdb"
engine = create_engine(DB_URI)

# Load CSV files
drinks_df = pd.read_csv("data/processed/drinks.csv")
ingredients_df = pd.read_csv("data/processed/ingredients.csv")
drink_ingredients_df = pd.read_csv("data/processed/drink_ingredients.csv")

print("✅ Loaded CSV files successfully.")

# ---------------------- Insert Data into PostgreSQL ----------------------
def insert_data():
    with app.app_context():  # Ensure Flask app context for SQLAlchemy
        # Insert Ingredients
        for _, row in ingredients_df.iterrows():
            if not Ingredient.query.get(row["name"]):  # Avoid duplicates
                ingredient = Ingredient(
                    name=row["name"],
                    alcohol_type=row.get("alcohol_type", ""),
                    taste=row.get("taste", ""),
                )
                db.session.add(ingredient)

        # Insert Drinks
        for _, row in drinks_df.iterrows():
            if not Drink.query.get(row["name"]):  # Avoid duplicates
                drink = Drink(
                    name=row["name"],
                    category=row.get("category", ""),
                    glass_type=row.get("glass_type", ""),
                    instructions=row.get("instructions", ""),
                    image_url=row.get("image_url", ""),
                )
                db.session.add(drink)

        # Insert Drink-Ingredient Relationships
        for _, row in drink_ingredients_df.iterrows():
            if not DrinkIngredient.query.filter_by(
                drink_name=row["drink_name"], ingredient_name=row["ingredient_name"]
            ).first():
                drink_ingredient = DrinkIngredient(
                    drink_name=row["drink_name"],
                    ingredient_name=row["ingredient_name"],
                    measurement_oz=row.get("measurement_oz", ""),
                    measurement_ml=row.get("measurement_ml", 0),
                )
                db.session.add(drink_ingredient)

        db.session.commit()
        print("✅ Data inserted into the database successfully.")

# Run the data insertion
if __name__ == "__main__":
    insert_data()
