

def cbt_quiz():
    print("Welcome to the Computer-Based Test (CBT)!")
    print("Answer the following questions:\n")

    
    questions = [
        {
            "question": "1. What is the capital of Nigeria?\n(a) Lagos\n(b) Abuja\n(c) Oyo\n(d) Benin",
            "answer": "b"
        },
        {
            "question": "2. Which planet is known as the Red Planet?\n(a) Earth\n(b) Jupiter\n(c) Mars\n(d) Saturn",
            "answer": "c"
        },
        {
            "question": "3. Python is a...\n(a) Snake\n(b) Programming Language\n(c) Game\n(d) Car",
            "answer": "b"
        },
        {
            "question": "4. The largest ocean in the world is?\n(a) Atlantic\n(b) Indian\n(c) Pacific\n(d) Arctic",
            "answer": "c"
        },
        {
            "question": "5. 2 + 2 * 2 = ?\n(a) 6\n(b) 8\n(c) 4\n(d) 10",
            "answer": "a"
        }
    ]

    score = 0  


    for q in questions:
        print(q["question"])
        answer = input("Your answer: ").lower().strip()  
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was '{q['answer']}'.\n")

    
    print("Quiz Completed!")
    print(f"Your final score is {score}/{len(questions)}")


cbt_quiz()
