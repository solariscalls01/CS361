import json
import time
import os
import inquirer
import random

#### VARIABLES ####
ascii_art = """

 _______  _______  _______  ______     ______    _______  _______  ___   _______  _______ 
|       ||       ||       ||      |   |    _ |  |       ||       ||   | |       ||       |
|    ___||   _   ||   _   ||  _    |  |   | ||  |    ___||       ||   | |    _  ||    ___|
|   |___ |  | |  ||  | |  || | |   |  |   |_||_ |   |___ |       ||   | |   |_| ||   |___ 
|    ___||  |_|  ||  |_|  || |_|   |  |    __  ||    ___||      _||   | |    ___||    ___|
|   |    |       ||       ||       |  |   |  | ||   |___ |     |_ |   | |   |    |   |___ 
|___|    |_______||_______||______|   |___|  |_||_______||_______||___| |___|    |_______|

"""

introduction = "Welcome to the Food Recipe App! Explore delicious recipes with us. From simple to sophisticated, we're\n here to make your cooking experience enjoyable and rewarding. " \
               "Happy cooking!\n\n\n"

closing_statement = "Thank you for choosing Food Recipe App! We appreciate your support and hope our recipes bring joy to your kitchen. Happy cooking!"

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
    print(ascii_art)
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
        else:
            print(closing_statement)
            break

def select_item():
    # function to select an item from the inquirer library
    questions = [
        inquirer.List('menu',
                      message="Which cuisine would you like to make today?",
                      choices=['Asian Recipes', 'Mexican Recipes', 'American Recipes', 'Random Recipe', 'Quit'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers

#######################################################################################
############################ RECIPE FUNCTIONS #########################################
#######################################################################################

def asian_menu():
    print("Let's take a look at some of the Asian Recipes we have available!\n\n")
    questions = [
        inquirer.List('cuisine',
                      message="Which Asian recipes would you like to try today? "
                              "Currently we only have 2 recipes available.",
                      choices=['Chinese', 'Thai', '<-- Back', "MAIN MENU"])
    ]
    answer = inquirer.prompt(questions)

    print(answer)
    # choice selection for if user selects chinese
    if answer['cuisine'] == 'Chinese':

        questions = [
            inquirer.List('recipe',
                          message=f'Currently there are {get_chinese_recipe_length} cuisines available.'
                                  f'Here is what we have on selection',
                          choices=['Fried Rice', 'Orange Chicken', 'Beef Broccoli', '<-- Back', "MAIN MENU"])
        ]
        choice = inquirer.prompt(questions)

        if choice['recipe'] == '<-- Back':
            asian_menu()
        elif choice['recipe'] == "MAIN MENU":
            return_to_main()

        print_json(chinese_recipes, choice)

    elif answer['cuisine'] == 'Thai':
        questions = [
            inquirer.List('recipe',
                          message=f'Currently there are {get_thai_recipe_length} cuisines available.'
                                  f'Here is what we have on selection',
                          choices=['Green Curry', 'Satay Chicken', 'Pad Thai', '<-- Back', "MAIN MENU"])
        ]
        choice = inquirer.prompt(questions)

        if choice['recipe'] == '<-- Back':
            asian_menu()
        elif choice['recipe'] == "MAIN MENU":
            return_to_main()

        print_json(thai_recipes, choice)

    elif answer['cuisine'] == '<-- Back':
        select_item()

    # Takes user back to main menu if no appropriate choices are made
    else:
        return_to_main()


def mexican_menu():
    print("Let's take a look at some of the Mexican Recipes we have available!\n\n")
    questions = [
        inquirer.List('recipe',
                      message=f'Currently there are {get_mexican_recipe_length} cuisines available.'
                              f'Here is what we have on selection',
                      choices=['Chicken Quesadillas', 'Enchiladas', 'Tortas', '<-- Back', "MAIN MENU"])
    ]
    choice = inquirer.prompt(questions)

    if choice['recipe'] == '<-- Back':
        main_menu()
    elif choice['recipe'] == "MAIN MENU":
        return_to_main()

    print_json(mexican_recipes, choice)


def american_menu():
    print("Let's take a look at some of the American Recipes we have available!\n\n")
    questions = [
        inquirer.List('recipe',
                      message=f'Currently there are {get_american_recipe_length} cuisines available.'
                              f'Here is what we have on selection',
                      choices=['Hamburgers', 'Spaghetti and Meatballs', '<-- Back', "MAIN MENU"])
    ]
    choice = inquirer.prompt(questions)
    if choice['recipe'] == '<-- Back':
        main_menu()
    elif choice['recipe'] == "MAIN MENU":
        return_to_main()

    print_json(american_recipes, choice)

#######################################################################################
#######################################################################################
#######################################################################################


#######################################################################################
################# USER INTERFACE FUNCTIONS ############################################
#######################################################################################
def get_random_recipe():
    # Maybe utilize a random num generator to return a random recipe from one of the 3 dishes. Set variable maybe?
    print("random selected")

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


# Counter to simulate loading time when returning to main menu
def count_to_three():
    i = "******"
    count = 5
    for index in range(5):
        print(i[0:count])
        count -= 1
        time.sleep(0.5)  # Pause for 1 second between prints
    print("\n\n\n")


def return_to_main():
    print("** Going back to the main menu **")
    count_to_three()
    clear_screen()
    main_menu()

# function to clear the screen when a user returns back to the main menu
def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')

if __name__ == '__main__':
    # Prompt the user to enter a recipe name
    main_menu()