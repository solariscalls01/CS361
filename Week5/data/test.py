import json

# Load the JSON file
with open('chinese_recipes.json') as f:
    recipes_data = json.load(f)

# Access the recipes
for recipe in recipes_data['recipes']:
    print("Recipe Name:", recipe['name'])
    print("Description:", recipe['description'])
    print("Ingredients:")
    for ingredient, amount in recipe['ingredients'].items():
        print(f"- {ingredient}: {amount}")
    print("Instructions:")
    for step, instruction in enumerate(recipe['instructions'], start=1):
        print(f"{step}. {instruction}")
    print("Servings:", recipe['servings'])
    print("Prep Time:", recipe['prep_time'])
    print("Cook Time:", recipe['cook_time'])
    print("\n")
