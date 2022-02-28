# "Find number [0-100]" console application. To exit, select -1.

import random
import sys

drawn_number = random.randrange(0, 100)
counter = 1
is_valid = True


def fun_guess_number():
    try:
        number = int(input("Guess what number is drawn [0-100]: "))
    except ValueError:
        print("It is not a number!")
        raise ValueError
    return number


def fun_validation(number_to_validation):
    global is_valid
    if number_to_validation > 101 or number_to_validation < -1:
        print(f"Your value {number_to_validation} is out of range!")
        is_valid = False
    else:
        if number_to_validation > drawn_number:
            print("Your number is too high!")
            is_valid = True
        else:
            print("Your number is too small!")
            is_valid = True
    return is_valid


def fun_exit():
    if guess_number == -1:
        sys.exit(0)


if __name__ == "__main__":
    guess_number = fun_guess_number()

    while guess_number != drawn_number:
        fun_exit()
        if fun_validation(guess_number):
            guess_number = fun_guess_number()
            counter += 1
        else:
            guess_number = fun_guess_number()

        if guess_number == drawn_number:
            print(f"You guessed! That's the number {drawn_number}! You hit in {counter} shots.")
