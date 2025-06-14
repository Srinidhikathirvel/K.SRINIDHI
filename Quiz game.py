# Simple Quiz Game in Python

def ask_question(question, options, correct_option):
    print("\n" + question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    
    try:
        answer = int(input("Enter your answer (1-4): "))
        if options[answer - 1].lower() == correct_option.lower():
            print("✅ Correct!")
            return True
        else:
            print(f"❌ Wrong! The correct answer is: {correct_option}")
            return False
    except (IndexError, ValueError):
        print("Invalid input. Please enter a number between 1 and 4.")
        return False

def quiz_game():
    print("🎮 Welcome to the Quiz Game!")
    score = 0
    
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Berlin", "Paris", "Madrid"],
            "answer": "Paris"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Venus"],
            "answer": "Mars"
        },
        {
            "question": "Who wrote 'Hamlet'?",
            "options": ["Leo Tolstoy", "William Shakespeare", "Mark Twain", "Charles Dickens"],
            "answer": "William Shakespeare"
        },
        {
            "question": "What is the smallest prime number?",
            "options": ["0", "1", "2", "3"],
            "answer": "2"
        }
    ]

    for q in questions:
        if ask_question(q["question"], q["options"], q["answer"]):
            score += 1

    print(f"\n🏁 Quiz Over! You scored {score} out of {len(questions)}.")

# Start the game
quiz_game()