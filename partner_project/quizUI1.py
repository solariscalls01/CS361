import sys
import subprocess

print("Please enter your selection: ")
print("1. Beginner")
print("2. Intermediate")
print("3. Advanced")
print("4. Return to the Main menu")
print("5. Access to the About program")
print("6. Quit")
uInput = ' '
while uInput != "6":
#UI calls Service to start quiz screen
        uInput = input("your choice: ")
        if (uInput == str(1)):
                print("You will be navigated to the Beginner level.")

                # SECTION WHERE MICROSERVICE IS CALLED.
                with open("quiz_microservice.txt", 'w') as f:
                        f.write('run')
                        f.close()
                theproc = subprocess.Popen([sys.executable, "microsrvc_beginner.py"])
                theproc.communicate()
        elif (uInput == str(2)):
                print("You will be navigated to the Intermediate level.")
                with open("quiz_microservice.txt", 'w') as f:
                        f.write('run')
                        f.close()
                theproc = subprocess.Popen([sys.executable, "microsrvc_intermediate.py"])
                theproc.communicate()
        elif (uInput == str(3)):
                print("You will be navigate to the Advanced level.")
                with open("quiz_microservice.txt", 'w') as f:
                        f.write('run')
                        f.close()
                theproc = subprocess.Popen([sys.executable, "microsrvc_advanced.py"])
                theproc.communicate()
        elif (uInput == str(4)):
                print("You will be returned to the Main menu.")
                theproc = subprocess.Popen([sys.executable, "mainUI.py"])
                theproc.communicate()
        elif (uInput == str(5)):
                print("You will be navigate to the About program information.")
                file = open('aboutProgram.txt', 'r')
                content = file.read()
                print(content)
                file.close
        elif (uInput == str(6)):
                exit()
        else:
           print("Please enter a correct option: 1, 2, 3, 4, 5, or 6")