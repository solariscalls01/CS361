import time




#TODO 1: UI should write "run" to prng-service.txt in order for the prng.py to read the contents of the file and
# generate the random number to be fed to the image-service.txt
while True:
    user_input = input('Select "1" if you would like to generate a random cat image or "2" to exit the program: \n')
    if user_input == "1":
        with open("prng-service.txt", 'w') as f:
            f.write("run")
            f.close()

        print("... Generating a random number to fetch...")
        exec(open("prng.py").read())
    else:
        print("Quitting the program")
        break



#TODO 2: UI reads the contents from the prng-service.txt and should save the contents of that file to a variable





#TODO 3: UI writes this number and feeds it to the image-service.txt





#TODO 4: Image-service.py reads the value from the image-service.txt and the path number should correspond to the
# random number that was generated (e.g., C:\Users\solar\Desktop\CS361 Software Engineering 1\Assignment1\img/cat1.jpg
# where the number in cat corresponds to the random number