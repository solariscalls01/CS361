import requests


def get_recipe(recipe_name):
    # Replace 'YOUR_API_KEY' with your actual Spoonacular API key
    api_key = 'a1cbcd3f6480414cac18be66fea0d547'

    # Send a GET request to the Spoonacular API to search for recipes
    response = requests.get(f'https://api.spoonacular.com/recipes/search?query={recipe_name}&apiKey={api_key}')

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Check if any recipes were found
        if data['results']:
            # Get the ID of the first recipe found
            recipe_id = data['results'][0]['id']

            # Send a GET request to the Spoonacular API to retrieve the details of the recipe
            recipe_response = requests.get(
                f'https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={api_key}')

            # Check if the request was successful (status code 200)
            if recipe_response.status_code == 200:
                # Parse the JSON response
                recipe_data = recipe_response.json()

                # Print the recipe details
                print(f"Recipe: {recipe_data['title']}")
                print(f"URL: {recipe_data['sourceUrl']}")
                print("Ingredients:")
                for ingredient in recipe_data['extendedIngredients']:
                    print(f"- {ingredient['original']}")
            else:
                print(f"Failed to get recipe details. Status code: {recipe_response.status_code}")
        else:
            print("No recipes found.")
    else:
        print(f"Failed to search for recipes. Status code: {response.status_code}")


if __name__ == '__main__':
    # Prompt the user to enter a recipe name
    recipe_name = input("Enter the name of the recipe: ")
    get_recipe(recipe_name)