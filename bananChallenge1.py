# "Find number [0-100]" console application. To exit, select -1.

import random
import sys

drawn_number = random.randrange(0, 100)
counter = 1


def fun_guess_number():
    try:
        number = int(input("Guess what number is drawn [0-100]: "))
    except ValueError:
        print("It is not a number!")
        sys.exit(0)
    return number


guess_number = fun_guess_number()

while guess_number != drawn_number:
    if guess_number == -1:
        sys.exit(0)

    if guess_number > 101 or guess_number < -1:
        print(f"Your value {guess_number} is out of range!")
        guess_number = fun_guess_number()
    else:
        if guess_number > drawn_number:
            print("Your number is too high!")
        else:
            print("Your number is too small!")
        guess_number = fun_guess_number()
        counter += 1
    if guess_number == drawn_number:
        print(f"You guessed! That's the number {drawn_number}! You hit in {counter} shots.")