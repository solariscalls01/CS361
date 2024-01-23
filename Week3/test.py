import inquirer

questions = [
    inquirer.Text("name", message="Enter your name:"),
    inquirer.List("gender", message="Select your gender:", choices=["Male", "Female", "Other"]),
    inquirer.Confirm("confirm", message="Is the information correct?", default=True),
]

answers = inquirer.prompt(questions)

print("Answers:")
print(answers)
