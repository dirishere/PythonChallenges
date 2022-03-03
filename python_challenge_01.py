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
        raise ValueError
    return number


def fun_validation(number_to_validation):
    if 101 > number_to_validation > -1:
        is_valid = True
        if number_to_validation > drawn_number:
            print("Your number is too high!")
        else:
            print("Your number is too small!")
    else:
        is_valid = False
        print(f"Your value {number_to_validation} is out of range!")
    return is_valid


def fun_exit():
    if guess_number == -1:
        print("The user has terminated the program.")
        sys.exit(-1)
    if guess_number == drawn_number:
        print(f"You guessed! That's the number {drawn_number}! You hit in {counter} shots.")


if __name__ == "__main__":
    guess_number = fun_guess_number()
    while guess_number != drawn_number:
        fun_exit()
        if fun_validation(guess_number):
            guess_number = fun_guess_number()
            counter += 1
        else:
            guess_number = fun_guess_number()
    fun_exit()
