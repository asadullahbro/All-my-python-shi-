import random
score = 10
random_number = random.randint(0, 100)
guessed_numbers = []
while True:
    try:
        user_input = int(input('Enter a number between 0-100: '))
        if user_input == random_number:
            print('Correct ✅')
            break
        elif user_input in guessed_numbers:
            print(f"{user_input} has already been chosen!")
        elif user_input > 100 or user_input < 0:
            print("You should try guessing between 0 to 100!")    
        elif user_input > random_number:
            print('Your guess is high')
            guessed_numbers.append(user_input)
            score -= 1
            print(f'Score: {score}')
        elif user_input < random_number:
            print("Your guess is low!")
            guessed_numbers.append(user_input)
            score -= 1
            print(f"Score: {score}")
        if score <= 0:
            print("DAMN! no attempts left 😒")
            break
    except ValueError:
        print('Invalid input.')
print('------ Score -----')
print(score)
print('------------------')
