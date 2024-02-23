import random
import time

# Expert Japanese Quiz

def run():
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


run()
