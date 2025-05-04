# import JSON module to work with the ultimate quiz data saved in JSON format
import json

# function to load quiz data and run the quiz
def run_quiz():
    filename = "the_ultimate_quiz_data.txt"

    print("\n🧠 Welcome to The Ultimate Quiz Game! 🧠\n")

# exception handling to try to open the quiz data or if the file doesn't exist, show error and exit
    try:
        with open(filename, "r") as file:
            questions = file.readlines()
    except FileNotFoundError:
        print("❌ Quiz file not found! Please create the quiz first.")
        return

score = 0
total = len(questions)

for i, line in enumerate(questions, 1):
    try:
        question_data = json.loads(line)
    except json.JSONDecodeError:
        print(f"Skipping invalid question format on line {i}")
        continue