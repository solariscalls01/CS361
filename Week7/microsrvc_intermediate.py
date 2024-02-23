import random
import time

# Intermediate Japanese Quiz

def run():
    intro = "Intermediate QUIZ! You will be presented with a Japanese word written in Japanese and 4 options in English.  " \
            "\nYour task is to select the correct English option for the given Japanese word." \
            "\nThe Intermediate level will test your skills for Japanese vocabulary written in Katakana.\n\n"

    ready = "You will be given 10 Questions in Katana and your job will be to find the correct translation in English. \nARE YOU READY?\n\n"

    # variable to count current correct answers
    correct = 0

    print(intro)
    print(ready)

    # answers will always be at the 0 index. Questions will then be shuffled after correct answer variable has been set
    questions = {
        "Aoi (アオイ) " : ['Blue', 'Red', 'Yellow', 'Black'],
        "Inu (イヌ )": ["Dog", "Cat", "Bird", "Fish"],
        "Uchi (ウチ )": ["Home", "Apartment", "Boat", "Dog"],
        "Eki (エキ )": ["Train Station", "Car", "Motorcycle", "Airplane"],
        "Okashi (オカシ )": ["Sweets", "Chips", "Candy", "Ice Cream"],
        "Kasa (カサ )": ["Umbrella", "Cane", "Chair", "Table"],
        "Kitsune (キツネ )": ["Fox", "Cat", "Cow", "Deer"],
        "Kuruma (クルマ )": ['Car', "Bicycle", "Motorcycle", "Skateboard"],
        "Sensei (センセイ )": ["Teacher", "Student", "Friend", "Principle"],
        "Natsu (ナツ )": ["Summer", "Winter", "Fall", "Spring"]
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


run()
