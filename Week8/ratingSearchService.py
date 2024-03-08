import json
import os
import time
def convert_rating_int(rating):
    """
    Function to convert the rating input from user to an integer.  For example, if user enter ***,
    this function converts to 3.
    :param rating which user entered either *** format or an integer
    :return an integer number
    """
    if rating.isdigit():
        ratingInt = int(rating)
    else:
        ratingInt = len(rating)
    return ratingInt

def search_recipe_rating(directory, key):
    """
    Function to return rating and recipe name pairs.
    :param directory which contains .json file from API
    :param key an integer which is mapped to "rating" value for a recipe
    :return lists which contains the recipe name with the rating which is the same as the value of key
    """

    keyInt = key

    results = []
    for file in os.listdir(directory):
        if file.endswith(".json"):
            filepath = os.path.join(directory, file)
            with open(filepath, "r") as jsonFile:
                data = json.load(jsonFile)
                for item in data['recipes']:
                    recipe_name = item['name']
                    if "rating" in item:
                       rating_value = item['rating']
                       rating_value_int = convert_rating_int(rating_value)
                       if keyInt == rating_value_int:
                           results.append({recipe_name: rating_value})

    return results

def write_result(file, list):
    """
    Function to write items in a list in a file.
    :param file a pointer to a file
    :param list a list object
    """
    for item in range(len(list)):
       file.write(str(list[item]))
       file.write('\n')

#main script
while True:
    directory = "data/"

    file1 = open("rating.txt")
    ratingInput = file1.readline()
    rating = convert_rating_int(ratingInput)
    if 0 < rating < 6:
        resultList = search_recipe_rating(directory, rating)
        file2 = open("searchResult.txt", "r+")
        write_result(file2, resultList)
        file2.close()
        time.sleep(2)
        with open("SearchResult.txt") as f:
            f = open("searchResult.txt", "r+")
            line = f.read()
            print("Search completed. Result:")
            print(line)
            f.close()
    else:
        print("incorrect option")
    break


