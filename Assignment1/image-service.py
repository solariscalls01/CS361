import time
import os
import sys
import cv2



# # create the prng-service.txt file if it does not exist in the root folder
# # source for how to create text file if file does not exist in directory automatically
# # https://stackoverflow.com/questions/35807605/create-a-file-if-it-doesnt-exist
# if not os.path.exists("../CS361 Software Engineering 1/Assignment1/image-service.txt"):
#     with open('image-service.txt', 'w') as f:
#         # You can write initial content to the file if needed
#         f.write('File Created')
#     print(f'The file "image-service.txt" has been created.')
# else:
#     print(f'The file already exists.')


# Opens and reads the text file and erases the number that was previously generated
def generate_image_location():
    # section to read the contents from the text file
    with open('image-service.txt') as f:
        get_text = f.read()
        print(get_text)

        # this statement "writes" essentially erasing the content of the text file
        # Source on how to erase content in a text
        # file: https://stackoverflow.com/questions/2769061/how-to-erase-the-file-contents-of-text-file-in-python
        open('image-service.txt', 'w').close()

    # section to write the file location for the image files
    # source for opening image files in python:
    # https://www.askpython.com/python/examples/display-images-using-python
    with open('image-service.txt', 'w') as f:
        img_location = 'C:/Users/solar/Desktop/CS361 Software Engineering 1/Assignment1/img/cat' + str(get_text) + '.jpg'
        img = cv2.imread(img_location, cv2.IMREAD_ANYCOLOR)

        # imshow displays the window name and type. Concatenated string to appropriate file number
        cv2.imshow("cat" + str(get_text), img)

        # delay timer of 10000 milliseconds or 10 seconds
        cv2.waitKey(10000)



# set a time to delay for 3 seconds before running the program
time.sleep(3)
generate_image_location()
