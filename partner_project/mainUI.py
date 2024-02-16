import os.path
import time
import random
from pathlib import Path
import sys
import subprocess

print("Hello Welcome to the Japanese Vocabulary Quiz program. \n")

uInput = ' '
print("Please enter 1 if you want to try or 2 to quit. 3 for the information on this program.\n")
while uInput != '2':
         uInput = input("your choice: ")
         if (uInput == str(1)):
            print("You will be navigated to the start quiz screen")
            theproc = subprocess.Popen([sys.executable, "quizUI1.py"])
            theproc.communicate()
         elif (uInput == str(2)):
            print("Quit this program")
            exit()
         elif (uInput == str(3)):
            file = open('aboutProgram.txt', 'r')
            content = file.read()
            print(content)
            file.close
         else:
            print("Please enter a correct option: 1, 2, 3")