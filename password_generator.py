import random
from string import ascii_letters
letters = "qwertyuiopasdfghjklzxcvbnm"
symbols = "!@#$%^&*()_-+={[}]|:;"'.>,<`~'
numbers = "0123456789"

num_letters = int(input("How many letters? "))
num_symbols = int(input("How many symbols? "))
num_numbers = int(input("How many numbers? "))
password_chars = []
for _ in range(num_letters):
    password_chars.append(random.choice(letters))
for _ in range(num_symbols):
    password_chars.append(random.choice(symbols))
for _ in range(num_numbers):
    password_chars.append(random.choice(numbers))
random.shuffle(password_chars)
password = "".join(password_chars)

print(password)