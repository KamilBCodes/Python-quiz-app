def welcome_message():
    print("Welcome to the Python Quiz!")
    print("Test your knowledge of Python by answering the following 10 questions with 'True' or 'False'.\n")

def ask_question(question, correct_answer):
    while True:
        user_input = input(f"{question} (True/False): ").strip().lower()
        if user_input in ['true', 'false']:
            return user_input == correct_answer.lower()
        else:
            print("Invalid input. Please enter 'True' or 'False'.")

def display_score(score, total):
    print("\nQuiz Completed!")
    print(f"Your score: {score} out of {total}")

def thank_you_message():
    print("\nThank you for taking the Python Quiz. Goodbye!")

def main():
    welcome_message()
    
    # The correct answers
    quiz_questions = [
        {"question": "Python is a statically typed language.", "answer": "False"},
        {"question": "Indentation is significant in Python.", "answer": "True"},
        {"question": "Python supports multiple inheritance.", "answer": "True"},
        {"question": "Lists in Python are immutable.", "answer": "False"},
        {"question": "The 'lambda' keyword is used to create anonymous functions in Python.", "answer": "True"},
        {"question": "Python was created by Guido van Rossum.", "answer": "True"},
        {"question": "The '==' operator in Python compares object identity.", "answer": "False"},
        {"question": "In Python, 'None' is equivalent to 0.", "answer": "False"},
        {"question": "Python supports both procedural and object-oriented programming.", "answer": "True"},
        {"question": "The 'pass' statement in Python is used as a placeholder for future code.", "answer": "True"}
    ]
    
    score = 0
    total_questions = len(quiz_questions)
    
    for idx, item in enumerate(quiz_questions, start=1):
        print(f"Question {idx}:")
        if ask_question(item["question"], item["answer"]):
            score += 1
        print()

    display_score(score, total_questions)
    thank_you_message()

if __name__ == "__main__":
    main()
