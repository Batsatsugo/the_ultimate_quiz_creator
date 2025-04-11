# import the json module to format and store the ultimate quiz data as JSON.
import json

# Function to create and save the ultimate quiz questions
def quiz_creator():
    filename = "the_ultimate_quiz_data.txt"

# print the title of the ultimate quiz creator
    print("\n🔥 Welcome to the Ultimate Quiz Creator! 🔥\n")

# open the file in write mode
    with open(filename, "w") as file:
        while True: # initialize an infinite loop to allow multiple questions to be added
            questions = input("\nEnter your question: ") # prompt user to enter a quiz question

# dictionary to store multiple-choice options
            choices = {}
            for option in ['a', 'b', 'c', 'd']:
                choices[option] = input(f"Enter choice {option.upper()}: ")

# ask user for the correct answer
            correct_answer = input("Enter the correct answer (a, b, c, or d): ").lower()

# validate that the correct answer is one of the provided choices
            while correct_answer not in choices:
                print("Invalid choice. Please enter a valid option (a, b, c, or d).")
                correct_answer = input("Enter the correct answer: ").lower()

# store the question and answers in a dictionary
            question_data = {
                "question": questions,
                "choices": choices,
                "answer": correct_answer
            }

# convert the dictionary to a JSON string and write it to the file
            file.write(json.dumps(question_data) + "\n")

# ask the user if they want to add another question
            another = input("\nDo you want to add another question? (yes/no): ").lower()

# if the user doesn't enter "yes", exit the loop
            if another != "yes":
                print("\n✅ All questions have been saved to 'quiz_data.txt'. ✅")
                break

# run the quiz creator only if this script is executed directly
if __name__ == "__main__":
    quiz_creator()
