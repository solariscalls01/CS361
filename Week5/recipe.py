import json
import time
import os
import inquirer
import requests
import ASCII_Art

#### VARIABLES ####

introduction = "Welcome to the Food Recipe App! Explore delicious recipes with us. From simple to sophisticated, we're\n here to make your cooking experience enjoyable and rewarding. " \
               "Happy cooking!\n\n\n"

closing_statement = "Thank you for choosing Food Recipe App! We appreciate your support and hope our recipes bring joy to your kitchen. Happy cooking!"


# used for getting the name and preparation times
directory = "data/"  # Specify the directory containing your JSON files
search_key = "prep_time"  # Specify the key you want to search for

############## Load JSON files ################
### CHINESE RECIPE ####
with open('data/chinese_recipes.json') as chinese:
    chinese_recipes = json.load(chinese)

get_chinese_recipe_length = len(chinese_recipes['recipes'])

### THAI RECIPE ###
with open('data/thai_recipes.json') as thai:
    thai_recipes = json.load(thai)

get_thai_recipe_length = len(thai_recipes['recipes'])

### Mexican RECIPE ###
with open('data/mexican_recipes.json') as mexican:
    mexican_recipes = json.load(mexican)

get_mexican_recipe_length = len(mexican_recipes['recipes'])

### AMERICAN RECIPE ###
with open('data/american_recipes.json') as american:
    american_recipes = json.load(american)

get_american_recipe_length = len(american_recipes['recipes'])

#####################################################
#####################################################

def main_menu():
    print(ASCII_Art.logo)
    print(introduction)
    # Function to generate the main menu to allow users to return to this section if item is selected
    while True:
        choice = select_item()

        if choice['menu'] == "Asian Recipes":
            asian_menu()
        elif choice['menu'] == "Mexican Recipes":
            mexican_menu()
        elif choice['menu'] == "American Recipes":
            american_menu()
        elif choice['menu'] == "Random Recipe":
            get_random_recipe()
        elif choice['menu'] == "Choose by Preparation Time":
            filter_by_time()
        else:
            print(closing_statement)
            break

def select_item():
    # function to select an item from the inquirer library
    questions = [
        inquirer.List('menu',
                      message="Which cuisine would you like to make today?",
                      choices=['Asian Recipes', 'Mexican Recipes', 'American Recipes', 'Random Recipe', "Choose by Preparation Time", 'Quit'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers

#######################################################################################
############################ RECIPE FUNCTIONS #########################################
#######################################################################################

def asian_menu():
    print(ASCII_Art.asian_ASCII)
    print("Let's take a look at some of the Asian Recipes we have available!\n\n")
    questions = [
        inquirer.List('cuisine',
                      message="Which Asian recipes would you like to try today? "
                              "Currently we only have 2 recipes available.",
                      choices=['Chinese', 'Thai', '<-- Back', "MAIN MENU"])
    ]
    answer = inquirer.prompt(questions)

    # choice selection for if user selects chinese
    if answer['cuisine'] == 'Chinese':

        questions = [
            inquirer.List('recipe',
                          message=f'Currently there are {get_chinese_recipe_length} cuisines available.'
                                  f'Here is what we have on selection',
                          choices=['Fried Rice', 'Orange Chicken', 'Beef Broccoli', 'Chow Mein', 'General Tso Chicken', '<-- Back', "MAIN MENU"])
        ]
        choice = inquirer.prompt(questions)

        if choice['recipe'] == '<-- Back':
            asian_menu()
        elif choice['recipe'] == "MAIN MENU":
            return_to_main()

        clear_screen()
        print_json(chinese_recipes, choice)
        question = [
            inquirer.List('confirm',
                          message="Would you like to see any other recipes?",
                          choices=['Yes', 'No'])
        ]

        response = inquirer.prompt(question)
        if response['confirm'] == "Yes":
            asian_menu()
        else:
            return_to_main()

    elif answer['cuisine'] == 'Thai':
        questions = [
            inquirer.List('recipe',
                          message=f'Currently there are {get_thai_recipe_length} cuisines available.'
                                  f'Here is what we have on selection',
                          choices=['Green Curry', 'Satay Chicken', 'Pad Thai', 'Tom Yum Soup', '<-- Back', "MAIN MENU"])
        ]
        choice = inquirer.prompt(questions)

        if choice['recipe'] == '<-- Back':
            asian_menu()
        elif choice['recipe'] == "MAIN MENU":
            return_to_main()

        clear_screen()
        print_json(thai_recipes, choice)

        question = [
            inquirer.List('confirm',
                          message="Would you like to see any other recipes?",
                          choices=['Yes', 'No'])
        ]

        response = inquirer.prompt(question)
        if response['confirm'] == "Yes":
            asian_menu()
        else:
            return_to_main()

    elif answer['cuisine'] == '<-- Back':
        select_item()

    # Takes user back to main menu if no appropriate choices are made
    else:
        return_to_main()


def mexican_menu():
    print(ASCII_Art.mexican_ASCII)
    print("Let's take a look at some of the Mexican Recipes we have available!\n\n")
    questions = [
        inquirer.List('recipe',
                      message=f'Currently there are {get_mexican_recipe_length} cuisines available.'
                              f'Here is what we have on selection',
                      choices=['Chicken Quesadillas', 'Enchiladas', 'Tortas', 'Ceviche', 'Burritos', '<-- Back', "MAIN MENU"])
    ]
    choice = inquirer.prompt(questions)

    if choice['recipe'] == '<-- Back':
        main_menu()
    elif choice['recipe'] == "MAIN MENU":
        return_to_main()

    clear_screen()
    print_json(mexican_recipes, choice)

    question = [
        inquirer.List('confirm',
                      message="Would you like to see any other recipes?",
                      choices=['Yes', 'No'])
    ]

    response = inquirer.prompt(question)
    if response['confirm'] == "Yes":
        mexican_menu()
    else:
        return_to_main()


def american_menu():
    print(ASCII_Art.american_ASCII)
    print("Let's take a look at some of the American Recipes we have available!\n\n")
    questions = [
        inquirer.List('recipe',
                      message=f'Currently there are {get_american_recipe_length} cuisines available.'
                              f'Here is what we have on selection',
                      choices=['Hamburgers', 'Spaghetti and Meatballs', 'Spinach and Artichoke Dip', 'Pastrami Sandwich', '<-- Back', "MAIN MENU"])
    ]
    
    choice = inquirer.prompt(questions)
    if choice['recipe'] == '<-- Back':
        main_menu()
    elif choice['recipe'] == "MAIN MENU":
        return_to_main()

    # clear the screen in order to improve general visibility after showing the recipe
    clear_screen()
    print_json(american_recipes, choice)

    question = [
        inquirer.List('confirm',
                      message="Would you like to see any other recipes?",
                      choices=['Yes', 'No'])
    ]

    response = inquirer.prompt(question)
    if response['confirm'] == "Yes":
        american_menu()
    else:
        return_to_main()

def get_random_recipe():
    print("Getting your random recipe from the internet...")
    count_to_three()
    response = requests.get('https://www.themealdb.com/api/json/v1/1/random.php')
    data = response.json()
    print(f"Recipe: {data['meals'][0]['strMeal']}")
    print(f"\nIngredients:")
    count = 1
    get_ingredients = data['meals'][0]

    # loop to extract the ingredients and measures from random recipe JSON API from: https://www.themealdb.com/api/json/v1/1/random.php
    for ingredient in get_ingredients:
        if ("strIngredient") in ingredient:
            # conditional to exit as strIngredient does not > 20
            if "strIngredient21" in ingredient:
                break
            count += 1
            # section to break out of loop if empty lines are detected
            if get_ingredients['strIngredient' + str(count)] == "" or get_ingredients['strIngredient' + str(count)] is None:
                break
            print(f"\t-{get_ingredients['strIngredient' + str(count)]}: {get_ingredients['strMeasure' + str(count)]}")
    print("\n")

    # split the ingredients paragraph into a list and use for loop to print out each individual line
    list_text = (get_ingredients['strInstructions'].split("."))
    # print(list_text)
    for instruction in list_text:
        if "\r" in instruction:
            instruction = instruction.replace("\r", "-")
            print(instruction)
        else:
            print(f'- {instruction}')

    print("\n\n")

    question = [
        inquirer.List('question',
                      message= "Would you like another random recipe?",
                      choices=["Yes", "No"])
    ]
    answer = inquirer.prompt(question)

    if answer['question'] == "Yes":
        clear_screen()
        get_random_recipe()
    else:
        clear_screen()
        return_to_main()
        
def filter_by_time():
    """
    Function to filter and return names of recipes by preparation time.
    :return:
    """
    filtered_items = []
    get_prep_time = name_prep_time(directory, search_key)
    print("Find a recipe based off of the preparation time and the recipe name \n"
          "will be displayed in the list below\n\n")
    question = [
        inquirer.Text('prep_time', message="Choose prep time")
    ]
    answer = inquirer.prompt(question)

    if answer['prep_time'].strip() == "":
        print("Input cannot be empty. Please input a proper time.\n")
        filter_by_time()
    if not answer['prep_time'].isnumeric():
        print("Please only put numbers in the search. \n")
        filter_by_time()

    # First extract the dictionary values from the list
    for recipe in get_prep_time:
        for key, value in recipe.items():
            if isinstance(value, int) and value <= int(answer['prep_time']):
                filtered_items.append(key)

    if not filtered_items:
        print("There are currently no items that match that time frame.\n\n")
    else:
        print(f"\nThese are the current recipes that take {answer['prep_time']} minutes to make")
            # Print the list of items based off of filter criteria
        for recipe_names in filtered_items:

            print(f'\t-{recipe_names}')

    question1 = [
        inquirer.List('confirm', message="Would you like to select another time frame?",
                      choices=['Yes', 'No'])
    ]

    response = inquirer.prompt(question1)
    if response['confirm'] == "Yes":
        filter_by_time()
    else:
        clear_screen()
        return_to_main()


#######################################################################################
#######################################################################################
#######################################################################################


#######################################################################################
################# USER INTERFACE FUNCTIONS ############################################
#######################################################################################
def print_json(dict, choice):
    for recipe in dict['recipes']:
        if recipe['name'] == choice['recipe']:
            print("Recipe Name:", recipe['name'])
            print("Description:", recipe['description'])
            print("\n\nIngredients:")
            for ingredient, amount in recipe['ingredients'].items():
                print(f"- {ingredient}: {amount}")
            print("\n\nInstructions:")
            for step, instruction in enumerate(recipe['instructions'], start=1):
                print(f"{step}. {instruction}")
            print("\nServings:", recipe['servings'])
            print("\n\nPrep Time:", recipe['prep_time'])
            print("Cook Time:", recipe['cook_time'])
            print("\n")

def name_prep_time(directory, key):
    """
    Function to get the preparation times and create a dictionary pair of the recipe name and prep time.
    :param directory: located in the data folder
    :param key: The string value that will be used for the search within the directory JSON files
    :return: list of dictionary values that contain all of the preparation times for meals with the key being
    the name of the recipe and value is the prep time
    """
    results = []
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r") as file:
                data = json.load(file)
                for item in data['recipes']:
                    recipe_name = item['name']
                    prep_time_value = item['prep_time']
                    if key in item:
                        data = item['name']
                        results.append({recipe_name: prep_time_value})

    for items in results:
        for key, value in items.items():
            # get the value of the first item in the value to be able to convert that value to an integer
            get_string_value = value.split()[0]
            convert_to_minutes = int(get_string_value)
            items[key] = convert_to_minutes

    return results


# Counter to simulate loading time when returning to main menu
def count_to_three():
    i = "******"
    count = 5
    for index in range(5):
        print(i[0:count])
        count -= 1
        time.sleep(0.3)  # Pause for 1 second between prints
    print("\n")


def return_to_main():
    print("** Going back to the main menu **")
    count_to_three()
    clear_screen()
    main_menu()

# function to clear the screen when a user returns to the main menu
def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')

if __name__ == '__main__':
    # Prompt the user to enter a recipe name
    main_menu()