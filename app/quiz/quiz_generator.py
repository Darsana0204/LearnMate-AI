from nltk.tokenize import sent_tokenize
import random

text = """
Machine Learning is a subset of Artificial Intelligence.
Deep Learning is a subset of Machine Learning.
AI is used in healthcare and finance.
Natural Language Processing is a branch of Artificial Intelligence.
"""

def normalize(text):
    return text.lower().strip()

sentences = sent_tokenize(text)

quiz = []

for sentence in sentences:

    sentence = sentence.strip()

    if " is a subset of " in sentence:

        parts = sentence.replace(".", "").split(" is a subset of ")

        question = f"What is {parts[0]} a subset of?"
        answer = parts[1]

        quiz.append({
            "question": question,
            "answer": answer
        })

    elif " is used in " in sentence:

        parts = sentence.replace(".", "").split(" is used in ")

        question = f"Where is {parts[0]} used?"
        answer = parts[1]

        quiz.append({
            "question": question,
            "answer": answer
        })

    elif " is a branch of " in sentence:

        parts = sentence.replace(".", "").split(" is a branch of ")

        question = f"What is {parts[0]} a branch of?"
        answer = parts[1]

        quiz.append({
            "question": question,
            "answer": answer
        })

random.shuffle(quiz)

print("\n========================")
print("      STUDY BUDDY")
print("========================")

score = 0

for index, item in enumerate(quiz, start=1):

    print(f"\nQuestion {index}")
    print(item["question"])

    user_answer = input("Your Answer: ")

    if normalize(user_answer) == normalize(item["answer"]):

        print("Correct!")
        score += 1

    else:

        print("Wrong!")
        print("Correct Answer:", item["answer"])

print("\n========================")
print("QUIZ COMPLETED")
print("========================")

print(f"Final Score: {score}/{len(quiz)}")

percentage = (score / len(quiz)) * 100

print(f"Percentage: {percentage:.2f}%")

if percentage >= 80:
    print("Excellent!")
elif percentage >= 50:
    print("Good Job!")
else:
    print("Keep Studying!")