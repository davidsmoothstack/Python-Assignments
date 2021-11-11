
import random

random_number = random.randint(1, 9)

while True:
    guess = int(input("Please guess a number from 1 to 9: "))

    if guess > 9 or guess < 1:
        print("Invalid number.")
        continue
    elif guess == random_number:
        print("Well guessed!")
        break
