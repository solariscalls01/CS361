import json

# Function to recursively remove curly braces {} and square brackets [] from a dictionary
def remove_braces(data):
    if isinstance(data, dict):
        return {key: remove_braces(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [remove_braces(item) for item in data]
    else:
        return data

# Load the JSON file
with open('chinese_recipes.json') as f:
    recipes_data = json.load(f)

# Remove curly braces and square brackets
recipes_data = remove_braces(recipes_data)

# Print the number of recipes
print(len(recipes_data['recipes']))

# Print the names of the recipes
for recipe in recipes_data['recipes']:
    print(recipe['name'])

# Function to unpack a dictionary if multiple subvalues in an JSON object. Used if JSON object starts with dict first
def unpack_dict(obj):
    if isinstance(amount, dict):
        for k, v in amount.items():
            if isinstance(v, list):
                print(f'- {ingredient}')
                for items in v:
                    print(f'\t- {items}')
            elif isinstance(obj, dict):
                for key, value in obj.items():
                    print(f'-{key}: {value}')
                    # else:
                    #     unpack_dict(obj)

        # print(ingredient, amount)
    else:
        print(f"- {ingredient}: {amount}")

# Function to unpack a list if multiple subvalues in JSON object. Used if JSON object starts with a list first
def unpack_list(obj):
    if isinstance(amount, list):
        pass


# Access the recipes
for recipe in recipes_data['recipes']:
    # Print recipe details
    print("Recipe Name:", recipe['name'])
    print("Description:", recipe['description'])

    # Print ingredients
    print("Ingredients:")
    # iterate_json(recipe['ingredients'])
    for ingredient, amount in recipe['ingredients'].items():
        # Section checks if there are any more dictionaries in the key value pair
        # reference: https://www.delftstack.com/howto/python/iterate-through-json-python/
        print(ingredient)
        unpack_dict(amount)
        # if isinstance(amount, dict):
        #     for k,v in amount.items():
        #         if isinstance(v, list):
        #             print(f'- {ingredient}')
        #             for items in v:
        #                 print(f'\t- {items}')
        #     # print(ingredient, amount)
        # else:
        #     print(f"- {ingredient}: {amount}")


    # # Print instructions
    # print("Instructions:")
    # for step, instruction in enumerate(recipe['instructions'], start=1):
    #     print(f"{step}. {instruction}")
    #
    # # Print servings, prep time, and cook time
    # print("Servings:", recipe['servings'])
    # print("Prep Time:", recipe['prep_time'])
    # print("Cook Time:", recipe['cook_time'])
    #
    # print("\n")
