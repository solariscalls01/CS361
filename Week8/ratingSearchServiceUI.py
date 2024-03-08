import time
import sys
import subprocess

# UI takes user command
print("Please enter the rating: ")
ratingInput = str(input())
file1 = open("rating.txt", "r+")
file1.write(ratingInput)
time.sleep(1)
file1.close()

with open("rating.txt", "r+") as f:
    rating = f.readline()
    print("Rating Entered:" + rating)
    f.close()

#Execute searchRecipeRating.py service

print("Search Service is generating the result.")
print("Press enter 1 to see the search result. Enter 2 to quit.")
uInput = input()
if (uInput == str(1)):
    file3 = open("searchResult.txt", "r+")
    print("Search Result:")
    data = file3.read()
    print(data)
    time.sleep(2)

    #Delete file contents
    file1 = open("rating.txt", "r+")
    file1.seek(0)
    file1.truncate()
    file3.seek(0)
    file3.truncate(0)
    file3.close()

elif (uInput == str(2)):
    # Delete file contents and quit
    file1 = open("rating.txt", "r+")
    file2 = open("searchResult.txt", "r+")
    file1.seek(0)
    file1.truncate()
    file1.seek(0)
    file2.truncate()
    file2.close()
    exit()
else:
    print("unknown option")




