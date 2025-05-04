# import JSON module to work with the ultimate quiz data saved in JSON format
import json

# function to load quiz data and run the quiz
def run_quiz():
    filename = "the_ultimate_quiz_data.txt"

    print("\n🧠 Welcome to The Ultimate Quiz Game! 🧠\n")

    try:
        with open(filename, "r") as file:
            questions = file.readlines()
    except FileNotFoundError:
        print("❌ Quiz file not found! Please create the quiz first.")
        return