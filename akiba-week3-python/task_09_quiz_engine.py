# Quiz questions
questions = [
    {
        "question": "1. What is the capital of Ethiopia?",
        "options": ["A. Hawassa", "B. Addis Ababa", "C. Dire Dawa", "D. Mekelle"],
        "answer": "B"
    },
    {
        "question": "2. Which language is used for web development?",
        "options": ["A. HTML", "B. All of these", "C. CSS", "D. JavaScript"],
        "answer": "B"
    },
    {
        "question": "3. What is 5 * 5?",
        "options": ["A. 10", "B. 20", "C. 25", "D. 30"],
        "answer": "C"
    },
    {
        "question": "4. Which data type stores True or False?",
        "options": ["A. String", "B. Boolean", "C. List", "D. Integer"],
        "answer": "B"
    },
    {
        "question": "5. Which keyword defines a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C"
    }
]


def display_question(question):
    print("\n" + question["question"])

    for option in question["options"]:
        print(option)


def validate_answer(answer):
    return answer.upper() in ["A", "B", "C", "D"]


def check_answer(answer, correct_answer):
    return answer.upper() == correct_answer


def update_score(score, correct):
    if correct:
        return score + 1
    return score


def display_results(score, total):
    incorrect = total - score
    percentage = (score / total) * 100

    print("\n--- QUIZ RESULTS ---")
    print("Correct answers:", score)
    print("Incorrect answers:", incorrect)
    print("Final score:", score, "/", total)
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 80:
        print("Category: Excellent!")
    elif percentage >= 60:
        print("Category: Good!")
    elif percentage >= 40:
        print("Category: Fair!")
    else:
        print("Category: Needs improvement.")


def play_quiz():
    score = 0

    for question in questions:
        display_question(question)

        answer = input("Your answer (A-D): ").strip()

        while not validate_answer(answer):
            print("Invalid option! Please enter A, B, C, or D.")
            answer = input("Your answer: ").strip()

        if check_answer(answer, question["answer"]):
            print("Correct!")
            score = update_score(score, True)
        else:
            print("Incorrect!")

    display_results(score, len(questions))


while True:
    play_quiz()

    again = input("\nDo you want to play again? (yes/no): ").strip().lower()

    if again != "yes":
        print("Thanks for playing!")
        break