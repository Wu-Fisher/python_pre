
import random

def guess(x):
    random_number =  random.randint(1,x)
    guess = 0
    while True:
        guess = int(input(f"Guess a number between 1 and {x}:"))
        if guess<random_number:
            print("Sorry too low")
        elif guess > random_number:
            print("Sorry too high")
        else:
            print("congadulation")
            break

guess(10)