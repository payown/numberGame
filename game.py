import random
import sys
correctNumber = random.randint(1,100)
name = str(input("What is your name?"))
tries = int(input(f"Hi {name}, how mini guesses would you like?"))
attempts = 0
while attempts <= tries:
    guess = int(input(f"ok so {name}, what's your guess?"))
    if guess < correctNumber:
        print(f"Sorry {name}, your guess is to low")
        attempts = attempts+1
    elif guess > correctNumber:
        print(f"Sorry {name}, your guess is to high")
        attempts = attempts+1
    elif guess == correctNumber:
        print(f"Congrats {name}, you got it")
        sys.exit()
else:
        print("Error, no number guessed.")
        quit()