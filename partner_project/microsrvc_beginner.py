import time
import random

#reference: https://realpython.com/python-quiz-application/

def beginner_quiz():
    with open("quiz_microservice.txt", 'r') as f:
        data = f.read()
        print(data)

        if data == "run":
            print("Running Beginner Quiz Microservice!")
            count_to_three()
            intro = "Beginner QUIZ! You will be presented with a Japanese word written in Japanese and 4 options in English.  " \
                    "\nYour task is to select the correct English option for the given Japanese word." \
                    "\nThe Beignner level will test your skills for Japanese vocabulary written in Hiragana.\n\n"

            ready = "You will be given 10 Questions in Hiragana and your job will be to find the correct translation in English. \nARE YOU READY?\n\n"

            # variable to count current correct answers
            correct = 0

            print(intro)
            print(ready)

            # answers will always be at the 0 index. Questions will then be shuffled after correct answer variable has been set
            questions = {
                "Aoi (あおい) " : ['Blue', 'Red', 'Yellow', 'Black'],
                "Inu (いぬ)": ["Dog", "Cat", "Bird", "Fish"],
                "Uchi (うち)": ["Home", "Apartment", "Boat", "Dog"],
                "Eki (えき)": ["Train Station", "Car", "Motorcycle", "Airplane"],
                "Okashi (おかし)": ["Sweets", "Chips", "Candy", "Ice Cream"],
                "Kasa (かさ)": ["Umbrella", "Cane", "Chair", "Table"],
                "Kitsune (きつね)": ["Fox", "Cat", "Cow", "Deer"],
                "Kuruma (くるま)": ['Car', "Bicycle", "Motorcycle", "Skateboard"],
                "Sensei (せんせい)": ["Teacher", "Student", "Friend", "Principle"],
                "Natsu (なつ)": ["Summer", "Winter", "Fall", "Spring"]
            }

            for question, answer in questions.items():
                correct_answer = answer[0]
                print(f'What is the correct word for {question}?')

                # Shuffle the answers
                random.shuffle(answer)
                for label, choice in enumerate(answer, start=1):
                    print(f' {label}) {choice}')

                # user selects the number which is the index for the answer.
                response_label = int(input("--> "))
                response = answer[response_label -1]

                if correct_answer == response:
                    correct +=1
                    print("Correct!")
                    print(f'Total Score = {correct}\n')
                    time.sleep(1)
                else:
                    print(f'That is incorrect! The answer is {correct_answer}\n')

            print(f"Your final score for this quiz is {correct} / {len(questions)}. Good luck on the next try!")

            # write the quiz score to the text file
            with open('score.txt', 'w') as d:
                d.write(f"Student Scored: {correct}/ {len(questions)} (BEGINNER SCORE)")
                d.close()

def count_to_three():
    i = "******"
    count = 5
    for index in range(5):
        print(i[0:count])
        count -= 1
        time.sleep(0.7)  # Pause for 1 second between prints
    print("\n")

beginner_quiz()