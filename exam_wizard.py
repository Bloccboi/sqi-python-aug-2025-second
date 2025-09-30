
questions = [
    {
        "question": "1. Explain the process of photosynthesis.",
        "keywords": {
            "photosynthesis": 2,
            "light energy": 1,
            "chemical energy": 1,
            "chloroplast": 2,
            "chlorophyll": 1,
            "carbon dioxide": 1,
            "water": 1,
            "glucose": 1,
            "oxygen": 1,
            "ATP": 1
        }
    },
    {
        "question": "2. Describe the process of digestion in humans.",
        "keywords": {
            "digestion": 2,
            "mouth": 1,
            "stomach": 2,
            "intestine": 2,
            "enzymes": 2,
            "nutrients": 2,
            "absorption": 2,
            "food": 1,
            "energy": 1
        }
    },
    {
        "question": "3. Describe the process of the water cycle.",
        "keywords": {
            "evaporation": 2,
            "condensation": 2,
            "precipitation": 2,
            "collection": 1,
            "transpiration": 1,
            "water vapor": 1
        }
    },
    {
        "question": "4. Explain the difference between RAM and ROM.",
        "keywords": {
            "RAM": 2,
            "ROM": 2,
            "volatile": 2,
            "non-volatile": 2,
            "temporary": 1,
            "permanent": 1,
            "memory": 1
        }
    },
    {
        "question": "5. What are the advantages of using the internet?",
        "keywords": {
            "communication": 2,
            "information": 2,
            "education": 1,
            "entertainment": 1,
            "business": 1,
            "global": 1
        }
    }
]

score = 0
max_score = sum(sum(q["keywords"].values()) for q in questions)

print("=== Welcome to Exam Wizard ===\n")
for q in questions:
    print(q["question"])
    answer = input("Your answer: ").lower()
    
    
    question_score = 0
    for keyword, weight in q["keywords"].items():
        if keyword.lower() in answer:
            question_score += weight
    
    score += question_score
    print(f"Score for this question: {question_score}/{sum(q['keywords'].values())}\n")

print("=== Exam Finished ===")
print(f"Your total score: {score}/{max_score}")
