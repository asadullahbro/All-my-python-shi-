import random

symbols = ["🍎", "🍌", "🍊", "🍒", "⭐", "🔔"]

coin = 10

print("🎰 Welcome to the Slot Machine! 🎰")
print(f"You start with {coin} coins. Each spin costs 1 coin.\n")

while True:
    play = input("Press Enter to spin (q to quit): ")
    if play == 'q':
        print("Thanks for playing!")
        break

    # Deduct cost per spin
    coin -= 1

    # Generate random result
    result = [random.choice(symbols) for _ in range(3)]
    print(result)

    # Check results
    if result[0] == result[1] == result[2]:
        coin += 5
        print("🎉 JACKPOT! You won 5 coins!")
    elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
        coin += 2
        print("✨ Small Win! You won 2 coins!")
    else:
        print("No match this time. Try again!")

    # Show remaining coins
    print(f"Coins left: {coin}\n")

    # Check if player is out of coins
    if coin <= 0:
        print("Game over! You ran out of coins. 💸")
        break
