# Import the json module to format and store the ultimate quiz data as JSON.
import json

def quiz_creator():
    filename = "the_ultimate_quiz_data.txt"

    print("\n🔥 Welcome to the Ultimate Quiz Creator! 🔥\n")

    with open(filename, "w") as file:
        while True:
            questions = input("\nEnter your question: ")

            choices = {}
            for option in ['a', 'b', 'c', 'd']:
                choices[option] = input(f"Enter choice {option.upper()}: ")

            correct_answer = input("Enter the correct answer (a, b, c, or d): ").lower()
            while correct_answer not in choices:
                print("Invalid choice. Please enter a valid option (a, b, c, or d).")
                correct_answer = input("Enter the correct answer: ").lower()

            question_data = {
                "question": questions,
                "choices": choices,
                "answer": correct_answer
            }

            file.write(json.dumps(question_data) + "\n")

            another = input("\nDo you want to add another question? (yes/no): ").lower()
            if another != "yes":
                print("\n✅ All questions have been saved to 'quiz_data.txt'. ✅")
                break


if __name__ == "__main__":
    quiz_creator()
