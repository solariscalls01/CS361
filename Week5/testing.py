import json
import os

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

# Example usage:
directory = "data/"  # Specify the directory containing your JSON files
search_key = "prep_time"  # Specify the key you want to search for

results = name_prep_time(directory, search_key)
print(results)



# def filter_keys_by_value_less_than_20(dictionary):
#     filtered_keys = []
#     for key, value in dictionary.items():
#         if isinstance(value, int) and value < 20:
#             filtered_keys.append(key)
#     return filtered_keys
#
# # Example dictionary
# my_dict = {'key1': 10, 'key2': 25, 'key3': 15, 'key4': 30}
#
# # Get keys with values less than 20
# keys_with_value_less_than_20 = filter_keys_by_value_less_than_20(my_dict)
#
# print("Keys with values less than 20:")
# print(keys_with_value_less_than_20)
def filter_by_time():
    """
    Function to filter and return recipes by preparation time.
    :return:
    """
    get_prep_time = name_prep_time(directory, search_key)
    # First extract the dictionary values from the list
    filtered_items = []
    for recipe in get_prep_time:
        for key, value in recipe.items():
            if isinstance(value, int) and value < 20:
                filtered_items.append(key)
    return filtered_items

print(filter_by_time())