import random
import time
import os

# generate a random number using the random library of numbers 1 through 7
randomNum = str(random.randint(1, 7))

# create the prng-service.txt file if it does not exist in the root folder
# source for how to create text file if file does not exist in directory automatically
# https://stackoverflow.com/questions/35807605/create-a-file-if-it-doesnt-exist
if not os.path.exists("../CS361 Software Engineering 1/Assignment1/prng-service.txt"):
    with open('prng-service.txt', 'w') as f:
        # You can write initial content to the file if needed
        f.write('File Created')
    print(f'The file "prng-service.txt" has been created.')
else:
    print(f'The file already exists.')

# Opens and reads the text file and erases the number that was previously generated
def generate_number():
    # section to read the contents from the text file
    with open('prng-service.txt') as f:
        get_text = f.read()
        print(get_text)

        # this statement "writes" essentially erasing the content of the text file
        # Source on how to erase content in a text
        # file: https://stackoverflow.com/questions/2769061/how-to-erase-the-file-contents-of-text-file-in-python
        open('prng-service.txt', 'w').close()

    # section to write the random number generated to the text file
    with open('prng-service.txt', 'w') as f:
        f.write(randomNum)
        print(randomNum)
        f.close()

#set a time to delay for 3 seconds before running the program
time.sleep(3)
generate_number()