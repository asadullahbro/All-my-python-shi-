import random

questions = {
    "What is 5 + 7?": "12",
    "What is 9 - 4?": "5",
    "What is 3 * 6?": "18",
    "What is 15 / 3?": "5",
    "What is the capital of France?": "Paris",
    "What color is the sky on a clear day?": "Blue",
    "Which animal is known as the King of the Jungle?": "Lion",
    "How many days are there in a leap year?": "366",
    "What is 10 squared?": "100",
    "Who wrote Harry Potter?": "J.K. Rowling",
    "What is the largest planet in our Solar System?": "Jupiter",
    "What does CPU stand for?": "Central Processing Unit",
    "Which gas do plants breathe in?": "Carbon Dioxide",
    "What is 7 x 8?": "56",
    "How many continents are there on Earth?": "7",
    "What is the boiling point of water in Celsius?": "100",
    "What is the opposite of 'cold'?": "Hot",
    "How many minutes are in an hour?": "60",
    "What is the national language of Pakistan?": "Urdu",
    "What is 25 % 7? (Remainder)": "4"
}

sample = random.sample(list(questions), 5)
print("Welcome to the quiz game")

score = 0
for q in sample:

  ask =  input(q + ": " ).lower()

  if ask == questions[q].lower():
      score += 1
      print("Correct")
  else:
    print(f"Wrong! correct answer is {questions[q]}")
print(f"\nyou scored {score}/5")
