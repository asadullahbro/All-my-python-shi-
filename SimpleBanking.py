import json

try:
    with open("accounts.json", "r") as f:
        accounts = json.load(f)
except FileNotFoundError:
    accounts = {}

while True:
    print("\nWelcome to Simple Banking")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("Enter a valid number between 1-5!")
        continue

    if choice == 1:
        name = input("Enter your name: ")
        if name in accounts:
            print("Account already exists!")
        else:
            try:
                balance = float(input("Enter initial balance: "))
                if balance < 0:
                    print("Balance cannot be negative!")
                    continue
            except ValueError:
                print("Enter a valid number for balance!")
                continue

            accounts[name] = balance
            with open("accounts.json", "w") as f:
                json.dump(accounts, f)
            print(f"Account for {name} created with balance {balance}.")

    elif choice == 2:
        name = input("Enter your name: ")
        if name in accounts:
            try:
                deposit = float(input("Enter deposit amount: "))
                if deposit <= 0:
                    print("Deposit must be positive!")
                    continue
            except ValueError:
                print("Enter a valid number for deposit!")
                continue

            accounts[name] += deposit
            with open("accounts.json", "w") as f:
                json.dump(accounts, f)
            print(f"{deposit} deposited to {name}'s account. New balance: {accounts[name]}")

        else:
            print("Account not found! Create an account first.")

    elif choice == 3:
        name = input("Enter your name: ")
        if name in accounts:
            try:
                withdraw = float(input("Enter withdraw amount: "))
                if withdraw <= 0:
                    print("Withdraw must be positive!")
                    continue
            except ValueError:
                print("Enter a valid number for withdraw!")
                continue

            if withdraw > accounts[name]:
                print("Insufficient balance!")
            else:
                accounts[name] -= withdraw
                with open("accounts.json", "w") as f:
                    json.dump(accounts, f)
                print(f"{withdraw} withdrawn from {name}'s account. New balance: {accounts[name]}")

        else:
            print("Account not found! Create an account first.")

    elif choice == 4:
        name = input("Enter your name: ")
        if name in accounts:
            print(f"{name}'s balance: {accounts[name]}")
        else:
            print("Account not found! Create an account first.")

    elif choice == 5:
        print("Thanks for using Simple Banking! Goodbye.")
        break

    else:
        print("Invalid choice! Enter a number between 1-5.")
