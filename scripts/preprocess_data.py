import pandas as pd

# Load dataset
DATASET_FILE = "../data/original/data_cocktails.csv"  # Update file path if necessary
df = pd.read_csv(DATASET_FILE)

print("Loaded dataset successfully.")

# ---------------------- Drinks DataFrame ----------------------
# Select only necessary columns
drinks_df = df[['strDrink', 'strCategory', 'strGlass', 'strInstructions']]

# Drop duplicates to ensure each drink appears only once
drinks_df = drinks_df.drop_duplicates(subset=['strDrink'])

# Rename columns to match SQL schema
drinks_df = drinks_df.rename(columns={
    'strDrink': 'name',
    'strCategory': 'category',
    'strGlass': 'glass_type',
    'strInstructions': 'instructions'
})

print("Drinks DataFrame (Unique Drinks):")
print(drinks_df.head())

# ---------------------- Ingredients DataFrame ----------------------
# Extract only relevant columns
ingredients_df = df[['strIngredients', 'Alc_type', 'Basic_taste']]

# Drop duplicates to ensure each ingredient is unique
ingredients_df = ingredients_df.drop_duplicates(subset=['strIngredients'])

# Rename columns for SQL schema
ingredients_df = ingredients_df.rename(columns={
    'strIngredients': 'name',
    'Alc_type': 'alcohol_type',
    'Basic_taste': 'taste'
})
print(ingredients_df.head())

# Remove any empty ingredient names
ingredients_df = ingredients_df[ingredients_df['name'].str.strip() != '']

print("\n🔹 Ingredients DataFrame (Unique Ingredients with Alc Type & Taste):")
print(ingredients_df.head())

# ---------------------- Drink-Ingredients DataFrame ----------------------
drink_ingredients_df = df[['strDrink', 'strIngredients', 'strMeasures', 'Value_ml']].dropna()

# Rename columns for SQL schema
drink_ingredients_df = drink_ingredients_df.rename(columns={
    'strDrink': 'drink_name',
    'strIngredients': 'ingredient_name',
    'strMeasures': 'measurement_oz',
    'Value_ml': 'measurement_ml'
})

print("\n🔹 Drink-Ingredients DataFrame (Mapping Drinks to Ingredients):")
print(drink_ingredients_df.head())
# ---------------------- Save DataFrames ----------------------
drinks_df.to_csv("../data/processed/drinks.csv", index=False)
ingredients_df.to_csv("../data/processed/ingredients.csv", index=False)
drink_ingredients_df.to_csv("../data/processed/drink_ingredients.csv", index=False)

print("\n✅ Data processing completed. DataFrames saved.")
