import json
import os

def convert_rating_int(rating):
    if rating.isdigit():
        ratingInt = int(rating)
    else:
        ratingInt = len(rating)
    return ratingInt

def name_rating(directory, key):
    """
    Function to get the rating and create a dictionary pair of the recipe name and rating.
    :param directory: located in the data folder
    :param key: Int value that will be used for the search within the directory JSON files
    :return: list of dictionary values that contain ratings for meals with the key being
    the name of the recipe and value is the rating
    """
    keyInt = convert_rating_int(key)
    #print("key= ",keyInt)

    results = []
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r") as file:
                data = json.load(file)
                for item in data['recipes']:
                    recipe_name = item['name']
                    if "rating" in item:
                       rating_value = item['rating']
                       rating_value_int = convert_rating_int(rating_value)
                       if keyInt == rating_value_int:
                           data = item['name']
                           results.append({recipe_name: rating_value})

    return results
# Example usage:
directory = "data/"  # Specify the directory containing your JSON files
#search_key = "rating"  # Specify the key you want to search for
# if a user enters the rating as int like 4, 3, 2,
#Example
#search_key = "4"

search_key = "***"
results = name_rating(directory, search_key)
print(results)

