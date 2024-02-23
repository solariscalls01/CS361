import random
import time

#TODO 1
# If a user selects the beginner option (e.g., "1"), UI app should write to a text file indicating "1".
# write a program that is able to read the text file command and interpret the results and create the quiz according
# to the selection the user has made. Create separate microsrvices for beginner, intermediate, advanced

with open("quiz_microservice.txt", 'r') as f:
    data = f.read()
    print(data)


#TODO 2
# create a general if/ then quiz program. The microsrvice quiz runs on its own, and does not send information back to the UI until
# the quiz is completed. It should display the question, followed by the multiple choice questions. After all the questions are asked,
# it tallys the total scores if the user guesses correctly and displays the total correct score. Send the information back to the UI displaying the score
# from the UI

#reference: https://realpython.com/python-quiz-application/

def beginner_quiz():
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

def intermediate_quiz():
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
        "Uchi (ウチ)": ["Home", "Apartment", "Boat", "Dog"],
        "Eki (エキ)": ["Train Station", "Car", "Motorcycle", "Airplane"],
        "Okashi (オカシ)": ["Sweets", "Chips", "Candy", "Ice Cream"],
        "Kasa (カサ)": ["Umbrella", "Cane", "Chair", "Table"],
        "Kitsune (キツネ)": ["Fox", "Cat", "Cow", "Deer"],
        "Kuruma (クルマ)": ['Car', "Bicycle", "Motorcycle", "Skateboard"],
        "Sensei (センセイ)": ["Teacher", "Student", "Friend", "Principle"],
        "Natsu (ナツ)": ["Summer", "Winter", "Fall", "Spring"]
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

def advanced_quiz():
    intro = "Expert QUIZ! You will be presented with a Japanese word written in Japanese and 4 options in English.  " \
            "\nYour task is to select the correct English option for the given Japanese word." \
            "\nThe Expert level will test your skills for Japanese vocabulary written in Kanji.\n\n"

    ready = "You will be given 10 Questions in Katana and your job will be to find the correct translation in English. \nARE YOU READY?\n\n"

    # variable to count current correct answers
    correct = 0

    print(intro)
    print(ready)

    # answers will always be at the 0 index. Questions will then be shuffled after correct answer variable has been set
    questions = {
        "Hito (人) " : ['Person', 'Child', 'Dog', 'Cat'],
        "Nihon (日本)": ["Japan", "Korea", "China", "Europe"],
        "Gakkou (学校)": ["School", "Work", "Market", "Shopping Mall"],
        "Ashita (明日)": ["Tomorrow", "Today", "Yesterday", "Next Week"],
        "Hon (本)": ["Book", "News Paper", "Magazine", "Notebook"],
        "Isha (医者)": ["Doctor", "Nurse", "Patient", "Pharmacist"],
        "Ame (雨)": ["Rain", "Sun", "Wind", "Snow"],
        "Hana (花)": ['Flower', "Butterfly", "Tree", "Bird"],
        "Kinyoubi (金曜日)": ["Friday", "Saturday", "Monday", "Tuesday"],
        "Taberu (べる)": ["To Eat", "To Drink", "To Sleep", "To Run"]
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


