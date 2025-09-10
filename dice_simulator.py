import random
results = []
while True:

    result = random.randint(1, 6)
    ask = input("Welcome to Dice Roll simulator press enter to roll: (q to quit) ")
    if ask == "q":
        break
    else:
        print(result)
        results.append(result)


print("your rolls:", results)