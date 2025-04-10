import json

def quiz_creator():
    filename = "the_ultimate_quiz_data.txt"

    print("\n🔥 Welcome to the Ultimate Quiz Creator! 🔥\n")

    with open(filename, "w") as file: