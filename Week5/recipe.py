import json

import inquirer
import random
import data

# VARIABLES
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

# Loading JSON files

print(ascii_art)
print(introduction)

def main_menu():
    # Function to generate the main menu to allow users to return to this section if item is selected
    while True:
        choice = select_item()
        print(choice)

        if choice['menu'] == "Asian Recipes":
            asian_menu()
        elif choice['menu'] == "Mexican Recipes":
            mexican_menu()
        elif choice['menu'] == "American Recipes":
            american_recipes()
        elif choice['menu'] == "Random Recipe":
            get_random_recipe()
        else:
            print(closing_statement)
            break

def select_item():
    # function to select an item from the inquirer library
    questions = [
        inquirer.List('menu',
                      message="Which cuisine would you like today?",
                      choices=['Asian Recipes', 'Mexican Recipes', 'American Recipes', 'Random Recipe', 'Quit'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers

def asian_menu():
    print("asian selected")

def mexican_menu():
    print("mexican selected")

def american_recipes():
    print("american selected")

def get_random_recipe():
    # Maybe utilize a random num generator to return a random recipe from one of the 3 dishes. Set variable maybe?
    print("random selected")


main_menu()